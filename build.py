import os
import shutil
import subprocess
import sys
from pathlib import Path

# Configuración de directorios
ROOT_DIR = Path(__file__).parent.resolve()
SRC_LATEX_DIR = ROOT_DIR / "src" / "latex"
BUILD_LATEX_DIR = ROOT_DIR / "build" / "latex"
DOC_OUT_LATEX_DIR = ROOT_DIR / "doc_out" / "latex"
DOC_OUT_MARKDOWN_DIR = ROOT_DIR / "doc_out" / "markdown"

# Ruta a pdflatex (intenta usar la de MSYS2 por defecto, si no, usa la del PATH)
PDFLATEX_MSYS2 = Path("C:/msys64/ucrt64/bin/pdflatex.exe")
PDFLATEX_CMD = str(PDFLATEX_MSYS2) if PDFLATEX_MSYS2.exists() else "pdflatex"


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

        if pdf_build_path.exists():
            print(f"-> Copiando {proj_name}.pdf a doc_out...")
            shutil.copy2(pdf_build_path, pdf_final_path)
            
            print(f"-> Limpiando PDF temporal en build...")
            pdf_build_path.unlink()
            
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
                cwd=proj_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            if result_md.returncode != 0:
                print(f"[Error] Falló la generación de Markdown para {proj_name}.")
                print(result_md.stdout)
            
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


def main():
    if not SRC_LATEX_DIR.exists():
        print(f"El directorio fuente {SRC_LATEX_DIR.relative_to(ROOT_DIR)} no existe.")
        return

    # Buscar todos los subdirectorios en src/latex
    projects = [d for d in SRC_LATEX_DIR.iterdir() if d.is_dir()]
    
    if not projects:
        print("No se encontraron proyectos en src/latex.")
        return

    success_count = 0
    for proj in projects:
        if build_project(proj):
            success_count += 1

    print(f"\nResumen: {success_count}/{len(projects)} proyectos compilados con éxito.")

if __name__ == "__main__":
    main()
