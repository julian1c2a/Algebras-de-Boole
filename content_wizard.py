import os
import argparse
from pathlib import Path
import re

ROOT_DIR = Path(__file__).parent.resolve()
SRC_LATEX_DIR = ROOT_DIR / "src" / "latex"

def create_skeleton(project: str, chapter_name: str):
    """Crea un archivo tex de esqueleto básico para un nuevo capítulo."""
    project_dir = SRC_LATEX_DIR / project
    if not project_dir.exists():
        print(f"Error: El proyecto {project} no existe en src/latex.")
        return

    chapter_file = project_dir / f"{chapter_name}.tex"
    if chapter_file.exists():
        print(f"Error: El archivo {chapter_file.name} ya existe.")
        return

    skeleton_content = f"""\\chapter{{Nuevo Capítulo}}

\\section{{Introducción}}

%% Escribe aquí la introducción

\\section{{Desarrollo}}

%% Escribe aquí el desarrollo principal

\\section{{Conclusión}}

%% Escribe aquí la conclusión

"""
    with open(chapter_file, "w", encoding="utf-8") as f:
        f.write(skeleton_content)
    print(f"Éxito: Se ha creado el esqueleto en {chapter_file.relative_to(ROOT_DIR)}")

def apply_typography_fixes(file_path: Path):
    """Aplica correcciones tipográficas basadas en guia_de_estilo.md."""
    if not file_path.exists():
        print(f"Error: El archivo {file_path} no existe.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Correcciones basadas en la guía de estilo
    # 1. P caligráfica (Power Set)
    content = re.sub(r'\\wp\(U\)', r'\\wp(U)', content) # Esto es correcto pero por si acaso.
    content = re.sub(r'@\(U\)', r'\\wp(U)', content)
    content = re.sub(r'@ U', r'\\wp(U)', content)
    content = re.sub(r'B := \\wp\(U\)', r'B \\triangleq \\wp(U)', content)
    
    # 4. Igualdad por Definición
    content = re.sub(r' \:= ', r' \\triangleq ', content)
    
    # 5. Diferencia Simétrica y Operadores de Triángulo
    content = re.sub(r'\\bigtriangleup', r'\\mathbin{\\Delta}', content)
    
    # Algunas otras correcciones comunes (Listas enumeradas simples)
    # Por ahora sólo aplicaremos las sustituciones regex más seguras.
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Éxito: Correcciones tipográficas aplicadas a {file_path.name}")
    
    # Después de las correcciones, aplicar saneamiento de puntuación matemática
    fix_math_punctuation(file_path)

def fix_math_punctuation(file_path: Path):
    """Corrige signos de puntuación fuera del entorno desplegado y advierte de abuso de \\[ \\]."""
    if not file_path.exists():
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Corrección automática de puntuación para modo desplegado
    content = re.sub(r'\\\]\s*,', r' , \\]', content)
    content = re.sub(r'\\\]\s*\.', r' . \\]', content)
    content = re.sub(r'\\\]\s*;', r' ; \\]', content)
    content = re.sub(r'\\\]\s*:', r' : \\]', content)
    
    # Regla: Convertir bloques matemáticos desplegados cortos (<= 10 caracteres) a modo en línea
    def replace_small_math(match):
        inner = match.group(1)
        if len(inner.strip()) <= 10 and '\n' not in inner:
            return f"${inner}$"
        return match.group(0)

    # Reemplazar \[ ... \] y $$ ... $$ que sean cortos
    content = re.sub(r'\\\[(.*?)\\\]', replace_small_math, content, flags=re.DOTALL)
    content = re.sub(r'\$\$(.*?)\$\$', replace_small_math, content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Éxito: Puntuación matemática corregida en {file_path.name}")
    
    # Análisis de advertencias para abuso de \[ ... \]
    lines = content.split('\n')
    warnings = []
    suspicious_pattern = re.compile(r'[a-zA-ZáéíóúÁÉÍÓÚñÑ]\s*\\\[|\\\]\s*[a-zA-ZáéíóúÁÉÍÓÚñÑ]')
    for i, line in enumerate(lines):
        if suspicious_pattern.search(line):
            warnings.append((i + 1, line.strip()))
            
    if warnings:
        print(f"\n[ADVERTENCIA] Posible abuso del modo desplegado '\\[ \\]' detectado en {file_path.name}:")
        print("La guía de estilo (Sec. 7) recomienda usar modo en línea '$ ... $' en medio de una frase.")
        for line_num, text in warnings:
            if len(text) > 80:
                text = text[:77] + "..."
            print(f"  Línea {line_num}: {text}")
        print("Por favor, revisa manualmente y cambia '\\[ \\]' por '$ $' donde corresponda.\n")

def lint_file(file_path: Path):
    """Realiza auditorías de estilo y estructura sobre el archivo .tex y lanza advertencias."""
    if not file_path.exists():
        print(f"Error: El archivo {file_path} no existe.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')
    
    in_tcolorbox = False
    tcolorbox_env = ""
    warnings = []
    
    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Entrada a tcolorbox
        m = re.search(r'\\begin\{(teorema|definicion|postulado|preaxioma)\}', line)
        if m:
            in_tcolorbox = True
            tcolorbox_env = m.group(1)
            
        # Salida de tcolorbox
        if in_tcolorbox and re.search(r'\\end\{' + tcolorbox_env + r'\}', line):
            in_tcolorbox = False
            
        # REGLA 1: Evitar cases/Bmatrix dentro de tcolorbox
        if in_tcolorbox and re.search(r'\\begin\{(cases|Bmatrix)\}', line):
            warnings.append((line_num, f"[REGLA 1] Anidamiento profundo. Un entorno 'cases' o 'Bmatrix' dentro de '{tcolorbox_env}' puede provocar overfull hbox. Sugerencia: align o itemize."))
            
        # REGLA 2: Proofs fuera de tcolorbox
        if in_tcolorbox and r'\begin{proof}' in line:
            warnings.append((line_num, "[REGLA 2] Las demostraciones (\\begin{proof}) deben ir fuera de las cajas de teorema/definición."))

        # REGLA 3: Puntuación fuera de inline math
        # Buscamos un $ seguido de puntuación
        if re.search(r'\$(?!\$)\s*[,.;:]', line):
            # Filtramos para asegurarnos de que la parte izq tiene algo
            if re.search(r'[^\\$]\$(?!\$)\s*[,.;:]', line):
                warnings.append((line_num, "[REGLA 3] Signo de puntuación fuera de entorno matemático. Formato correcto: $... ,$ o $... .$"))

        # REGLA 4: MathBB para Boole
        if r'\mathcal{B}' in line or re.search(r'\bB\b', line):
            # Detectar si habla de álgebra de boole
            if 'Boole' in content or 'álgebra' in content:
                # Warning condicionado para evitar spam si solo es la variable B
                if r'\mathcal{B}' in line:
                    warnings.append((line_num, "[REGLA 4] Uso de \\mathcal{B} detectado. Usar \\mathbb{B} para el Álgebra de Boole."))

    # REGLA 5: Orden de los anexos
    if file_path.name == 'book_on_digital.tex':
        includes = [line for line in lines if line.strip().startswith('\\include{')]
        found_annex = False
        for inc in includes:
            if 'anexo_' in inc:
                found_annex = True
            elif found_annex and 'capitulo_' in inc:
                warnings.append((0, f"[REGLA 5] Capítulo incluido ('{inc.strip()}') después de un anexo. Los anexos van al final."))
                break

    if warnings:
        print(f"\n[LINTER] Problemas en {file_path.name}:")
        for line_num, msg in warnings:
            if line_num == 0:
                print(f"  -> {msg}")
            else:
                print(f"  Línea {line_num}: {msg}")
    else:
        pass # Todo bien

def lint_project(project_dir: Path):
    if not project_dir.exists():
        print(f"Error: El proyecto {project_dir} no existe.")
        return
    
    tex_files = list(project_dir.glob('*.tex'))
    print(f"\n{'='*40}\nEjecutando linter sobre {project_dir.name}\n{'='*40}")
    for f in tex_files:
        lint_file(f)
    print("\nAuditoría finalizada.\n")

def manage_review_status(file_path: Path, status: str):
    """Añade o actualiza un comentario de estado al principio del archivo LaTeX."""
    if not file_path.exists():
        print(f"Error: El archivo {file_path} no existe.")
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    status_line = f"%% ESTADO_REVISION: {status}\n"
    
    if lines and lines[0].startswith("%% ESTADO_REVISION:"):
        lines[0] = status_line
        print(f"Éxito: Estado actualizado a '{status}' en {file_path.name}")
    else:
        lines.insert(0, status_line)
        print(f"Éxito: Estado '{status}' añadido a {file_path.name}")
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

def main():
    parser = argparse.ArgumentParser(description="Asistente de contenido para Álgebras de Boole.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Comando para crear esqueleto
    parser_create = subparsers.add_parser("create", help="Crear un esqueleto de capítulo.")
    parser_create.add_argument("project", type=str, help="Nombre del proyecto (ej. book_on_digital)")
    parser_create.add_argument("chapter_name", type=str, help="Nombre del archivo (ej. capitulo_11)")

    # Comando para correcciones tipográficas (y alias sanitize)
    parser_fix = subparsers.add_parser("fix", aliases=["sanitize"], help="Aplicar correcciones tipográficas (guia de estilo).")
    parser_fix.add_argument("file", type=str, help="Ruta relativa o absoluta al archivo .tex")

    # Comando para estado de revisión
    parser_status = subparsers.add_parser("status", help="Actualizar estado de revisión de un archivo.")
    parser_status.add_argument("file", type=str, help="Ruta relativa o absoluta al archivo .tex")
    parser_status.add_argument("state", type=str, choices=["borrador", "revision", "final"], help="Estado a establecer")

    # Comando para linter
    parser_lint = subparsers.add_parser("lint", help="Auditar un archivo o proyecto buscando problemas.")
    parser_lint.add_argument("target", type=str, help="Ruta al archivo .tex o nombre del proyecto (ej. book_on_digital)")

    args = parser.parse_args()

    if args.command == "create":
        create_skeleton(args.project, args.chapter_name)
    elif args.command == "fix":
        apply_typography_fixes(Path(args.file))
    elif args.command == "status":
        manage_review_status(Path(args.file), args.state)
    elif args.command == "lint":
        target_path = Path(args.target)
        if target_path.is_file():
            lint_file(target_path)
        else:
            proj_path = SRC_LATEX_DIR / args.target
            if proj_path.is_dir():
                lint_project(proj_path)
            else:
                print(f"Error: No se encontró el proyecto o archivo {args.target}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
