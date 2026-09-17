# Guía de Compilación de Proyectos

Este documento describe la arquitectura de compilación centralizada para los proyectos de LaTeX y Markdown en este repositorio. Se ha implementado un sistema automatizado para garantizar que todos los proyectos se construyan de manera limpia, sin dejar archivos residuales en los directorios fuente.

---

## 1. Reglas Generales de Estructura de Salida

1. **Aislamiento por Documento**:
   - Cada proyecto (ej. `apuntes_AB`, `book_on_digital`) tiene su código fuente en `src/latex/<nombre_del_proyecto>/`.
   - Durante la compilación, los archivos temporales (`.aux`, `.log`, `.out`, etc.) y el PDF preliminar se generan en la carpeta `build/`. **El directorio `build/` no debe contener código fuente**.
   - El PDF final resultante se ubicará automáticamente en `doc_out/latex/`.
   - La versión en Markdown resultante (generada vía Pandoc con soporte para KaTeX) se ubicará en `doc_out/markdown/<nombre_del_proyecto>/`.

2. **Directorio de Tests**:
   - Todo ejecutable o artefacto de pruebas asociadas se compila en la ruta especificada:
     ```
     build/build_tests/
     ```

---

## 2. Tipos de Proyectos

- **Proyectos de Libro** (`book_on_digital`):
  - Proyectos modulares divididos en varios capítulos (`capitulo_01.tex`, `capitulo_02.tex`, etc.) compilados desde un archivo raíz (`book_on_digital.tex`).
- **Proyectos Autónomos** (`apuntes_AB.tex`, `apuntes_AB_ing.tex`):
  - Archivos únicos con su propia cabecera que incluyen todo el contenido.
- **Manuales Ingenieriles** (`manual_ingenieria_ansi.tex`, `manual_ingenieria_ieee.tex`):
  - Proyectos técnicos que pueden usar paquetes específicos (como `circuitikz`) para la generación de esquemas lógicos.

---

## 3. Protocolo de Compilación: `build.py`

El método oficial de compilación es mediante el script `build.py`, situado en la raíz del repositorio. Este script automatiza el proceso de doble pasada, limpieza y generación de markdown.

### Compilar un único proyecto:
```powershell
python build.py --project <nombre_del_proyecto>
```
*Ejemplo: `python build.py --project book_on_digital`*

### Compilar todos los proyectos detectados:
```powershell
python build.py --all
```

### Funciones del script:
1. **Creación de directorios**: Verifica y crea las carpetas `build/` y `doc_out/` necesarias.
2. **Doble pasada pdflatex**: Ejecuta `pdflatex` dos veces sobre el directorio `build/` para resolver índices y referencias cruzadas.
3. **Migración de PDF**: Copia el PDF final a `doc_out/latex/`.
4. **Limpieza temporal**: Borra el PDF de la carpeta `build/` para evitar confusiones.
5. **Generación Pandoc**: Genera una versión Markdown a partir del código LaTeX original y la coloca en `doc_out/markdown/<proyecto>/<proyecto>.md`.

---

## 4. Convenciones de Código y Solución de Errores

- **Notación Matemática**: Se deben usar los entornos estándar de LaTeX.
- **Rutas a imágenes/recursos**: Usar SIEMPRE rutas relativas al archivo principal compilable, nunca rutas absolutas.
- **Inspección de Errores**: Si `build.py` falla en la fase de `pdflatex`, revisa el archivo de log generado en `build/<proyecto>.log`.
- **Desbordamientos**: Para prevenir desbordamientos visuales de la cabecera en los PDFs generados, asegúrate de que el documento utiliza márgenes estándar (`\usepackage[a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}`) y usa el argumento opcional de los títulos si son muy largos: `\chapter[Título corto]{Título exageradamente largo que rompe el margen}`.
