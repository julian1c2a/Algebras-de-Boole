---
description: Mandatory rules defining the structure and compilation flow of the LaTeX/Markdown book project.
---

# Project Structure and Compilation Rules

These rules are **mandatory** and must be strictly followed when working on this repository.

## 1. Directory Hierarchy
- `src/latex`: All source LaTeX projects must reside here, each in its own subfolder (e.g., `src/latex/book_on_digital`).
- `src/markdown`: Reserved for future markdown source projects.
- `build/`: Used for intermediate compilation files (`.aux`, `.log`, temporary PDFs). **Never write source files here.**
- `build/build_tests/`: Executables from tests must be compiled into this specific directory.
- `doc_out/latex/`: Exclusively for the final generated `PDF` files.
- `doc_out/markdown/`: Exclusively for the final generated `Markdown` files (usually via Pandoc).

## 2. Compilation Flow
- **Never invoke `pdflatex` or `pandoc` manually** for the main projects unless debugging a specific internal issue.
- Always use the provided Python build system:
  ```powershell
  python build.py --project <nombre_del_proyecto>
  ```
  Or to compile all projects:
  ```powershell
  python build.py --all
  ```
- The `build.py` script automatically:
  1. Creates the necessary output folders.
  2. Runs a 2-pass `pdflatex` inside `build/`.
  3. Moves the final PDF to `doc_out/latex/`.
  4. Generates a Markdown version using KaTeX bindings and places it in `doc_out/markdown/`.

## 3. Formatting and Style Guidelines
- **Math Notation**: Use standard LaTeX math environments (`\[ ... \]`, `\begin{equation}`, `$ ... $`). 
- **Digital vs Lattice Notation**: Ensure the context is respected. E.g., early chapters of `book_on_digital` use lattice notation ($\vee$, $\wedge$, $\neg$, $\top$, $\bot$), while later engineering texts use digital notation ($+$, $\cdot$, $\overline{x}$, $1$, $0$).
- **Cross-References**: Do not use absolute paths. Always use relative paths from the project's root folder (`src/latex/<project>/`).
- **Margins and Headers**: All top-level LaTeX projects should use `\usepackage[a4paper, left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}` to prevent layout overflows. For long chapter titles, use `\chapter[Short Title]{Long Title}` to avoid header bleeding.

## 4. Automation and External Tools
- The repository supports both `make` and `build.py`. 
- Treat `build.py` as the main orchestrator for multi-format document generation.
