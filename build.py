import os
import shutil
import subprocess
import sys
import argparse
from pathlib import Path

# Configuración de directorios
ROOT_DIR = Path(__file__).parent.resolve()
SRC_LATEX_DIR = ROOT_DIR / "src" / "latex"
BUILD_LATEX_DIR = ROOT_DIR / "build" / "latex"
DOC_OUT_LATEX_DIR = ROOT_DIR / "doc_out" / "latex"
DOC_OUT_MARKDOWN_DIR = ROOT_DIR / "doc_out" / "markdown"
TEST_BUILD_DIR = ROOT_DIR / "build" / "build_tests"

# Ruta a pdflatex (intenta usar la de MSYS2 por defecto, si no, usa la del PATH)
PDFLATEX_MSYS2 = Path("C:/msys64/ucrt64/bin/pdflatex.exe")
PDFLATEX_CMD = str(PDFLATEX_MSYS2) if PDFLATEX_MSYS2.exists() else "pdflatex"


def prepare_for_pandoc(proj_path: Path, temp_dir: Path):
    """Copia los archivos .tex a temp_dir y traduce entornos tcolorbox a bloque de citas estándar."""
    import re
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir(parents=True)
    
    # Copiar todos los archivos tex
    for file in proj_path.glob('*.tex'):
        shutil.copy2(file, temp_dir / file.name)
        
    # Reemplazos en cada archivo
    for file in temp_dir.glob('*.tex'):
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            
        envs = ['teorema', 'definicion', 'postulado', 'preaxioma']
        for env in envs:
            env_title = env.capitalize()
            # Patrón para \begin{env}{Titulo}{label}
            pattern = r'\\begin\{' + env + r'\}\{(.*?)\}\{(.*?)\}'
            replacement = r'\\begin{quote}\\textbf{' + env_title + r' (\1):}\\label{\2}'
            text = re.sub(pattern, replacement, text)
            
            # Cierre
            text = re.sub(r'\\end\{' + env + r'\}', r'\\end{quote}', text)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)

def build_project(proj_path: Path):
    proj_name = proj_path.name
    tex_file = proj_path / f"{proj_name}.tex"

    if not tex_file.exists():
        print(f"[Aviso] No se encontró {tex_file.relative_to(ROOT_DIR)}. Saltando...")
        return False

    print(f"\n{'='*40}")
    print(f"Compilando {proj_name}...")
    print(f"{'='*40}")

    # Preparar directorios de salida
    build_dir = BUILD_LATEX_DIR / proj_name
    doc_out_dir = DOC_OUT_LATEX_DIR / proj_name
    doc_out_md_dir = DOC_OUT_MARKDOWN_DIR / proj_name
    
    build_dir.mkdir(parents=True, exist_ok=True)
    doc_out_dir.mkdir(parents=True, exist_ok=True)
    doc_out_md_dir.mkdir(parents=True, exist_ok=True)

    # Calcular la ruta relativa desde el directorio fuente hasta el directorio de build
    # pdflatex prefiere rutas relativas o absolutas, pero le daremos la absoluta para evitar problemas.
    
    # Comando de compilación
    cmd = [
        PDFLATEX_CMD,
        "-interaction=nonstopmode",
        "-synctex=1",
        f"-output-directory={build_dir.resolve()}",
        tex_file.name
    ]

    try:
        # Ejecutamos dos veces para resolver referencias cruzadas, TOC, etc.
        for i in range(2):
            print(f"-> Pasada {i+1}/2...")
            result = subprocess.run(
                cmd,
                cwd=proj_path, # Ejecutar dentro del directorio del proyecto
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            # Ignoramos códigos de salida distintos de cero aquí porque LaTeX suele
            # devolverlos en caso de warnings o cajas overfull, aunque genere el PDF.
            
        # Mover el PDF al directorio final
        pdf_build_path = build_dir / f"{proj_name}.pdf"
        pdf_final_path = doc_out_dir / f"{proj_name}.pdf"
        synctex_build_path = build_dir / f"{proj_name}.synctex.gz"
        synctex_final_path = doc_out_dir / f"{proj_name}.synctex.gz"

        if pdf_build_path.exists():
            print(f"-> Copiando {proj_name}.pdf a doc_out...")
            shutil.copy2(pdf_build_path, pdf_final_path)
            
            if synctex_build_path.exists():
                print(f"-> Copiando {proj_name}.synctex.gz a doc_out...")
                shutil.copy2(synctex_build_path, synctex_final_path)
                synctex_build_path.unlink()
            
            print(f"-> Limpiando PDF temporal en build...")
            pdf_build_path.unlink()
            
            print(f"-> Preprocesando LaTeX para Pandoc...")
            pandoc_temp_dir = BUILD_LATEX_DIR / (proj_name + '_pandoc_temp')
            prepare_for_pandoc(proj_path, pandoc_temp_dir)
            
            print(f"-> Generando Markdown con Pandoc...")
            md_final_path = doc_out_md_dir / f"{proj_name}.md"
            pandoc_cmd = [
                "pandoc",
                tex_file.name,
                "-o", str(md_final_path.resolve()),
                "--katex",
                "--from=latex",
                "--to=markdown"
            ]
            result_md = subprocess.run(
                pandoc_cmd,
                cwd=pandoc_temp_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            if result_md.returncode != 0:
                print(f"[Error] Falló la generación de Markdown para {proj_name}.")
                print(result_md.stdout)
            
            if md_final_path.exists():
                print(f"-> Inyectando macros de KaTeX en Markdown...")
                with open(md_final_path, "r", encoding="utf-8") as f:
                    md_content = f.read()
                
                macros = "$$\n\\gdef\\symdiff{\\mathbin{\\vartriangle}}\n\\gdef\\llbracket{\\lbrack\\!\\lbrack}\n\\gdef\\rrbracket{\\rbrack\\!\\rbrack}\n\\gdef\\triangleq{\\stackrel{\\mathrm{def}}{=}}\n$$\n\n"
                with open(md_final_path, "w", encoding="utf-8") as f:
                    f.write(macros + md_content)
                
                print(f"-> Generando HTML desde Markdown...")
                html_final_path = doc_out_md_dir / f"{proj_name}.html"
                pandoc_html_cmd = [
                    "pandoc",
                    str(md_final_path.resolve()),
                    "-o", str(html_final_path.resolve()),
                    "-s",
                    "--katex"
                ]
                subprocess.run(pandoc_html_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                
                print(f"-> Generando PDF desde Markdown...")
                pdf_from_md_path = doc_out_md_dir / f"{proj_name}_from_md.pdf"
                pandoc_pdf_cmd = [
                    "pandoc",
                    str(md_final_path.resolve()),
                    "-o", str(pdf_from_md_path.resolve()),
                    "--pdf-engine=" + PDFLATEX_CMD
                ]
                subprocess.run(pandoc_pdf_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
            print(f"[Éxito] {proj_name} compilado correctamente.")
            return True
        else:
            print(f"[Error] No se pudo generar el PDF para {proj_name}.")
            # Mostrar las últimas 20 líneas del log si falló
            log_output = result.stdout.splitlines()[-20:]
            print("\n".join(log_output))
            return False

    except FileNotFoundError:
        print(f"[Error crítico] No se encontró el ejecutable '{PDFLATEX_CMD}'.")
        print("Asegúrate de tener LaTeX instalado y en el PATH.")
        sys.exit(1)


def build_tests():
    print(f"\n{'='*40}")
    print("Construyendo tests...")
    print(f"{'='*40}")
    TEST_BUILD_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Directorio de tests creado en: {TEST_BUILD_DIR.relative_to(ROOT_DIR)}")
    # Lógica adicional de test building se puede añadir aquí.
    return True

def main():
    parser = argparse.ArgumentParser(description="Script de compilación para los proyectos LaTeX.")
    parser.add_argument('--all', action='store_true', help='Compilar todos los proyectos detectados.')
    parser.add_argument('--project', type=str, help='Compilar un único proyecto por nombre.')
    parser.add_argument('--test', action='store_true', help='Construir los ejecutables de test.')
    
    args = parser.parse_args()

    if not SRC_LATEX_DIR.exists():
        print(f"El directorio fuente {SRC_LATEX_DIR.relative_to(ROOT_DIR)} no existe.")
        return

    # Si se piden pruebas, las construimos
    if args.test:
        build_tests()
        if not args.all and not args.project:
            return

    # Buscar subdirectorios en src/latex
    available_projects = [d for d in SRC_LATEX_DIR.iterdir() if d.is_dir()]
    if not available_projects:
        print("No se encontraron proyectos en src/latex.")
        return

    projects_to_build = []
    if args.project:
        target = SRC_LATEX_DIR / args.project
        if target.is_dir():
            projects_to_build.append(target)
        else:
            print(f"[Error] No se encontró el proyecto '{args.project}' en {SRC_LATEX_DIR.relative_to(ROOT_DIR)}")
            return
    elif args.all:
        projects_to_build = available_projects
    else:
        # Por defecto si no hay argumentos compilamos todo (o podríamos mostrar la ayuda)
        # Seguiremos la convención de compilar todo si no se especifica nada
        projects_to_build = available_projects

    success_count = 0
    for proj in projects_to_build:
        if build_project(proj):
            success_count += 1

    print(f"\nResumen: {success_count}/{len(projects_to_build)} proyectos compilados con éxito.")

if __name__ == "__main__":
    main()
