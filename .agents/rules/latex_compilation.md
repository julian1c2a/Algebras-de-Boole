# Regla de Compilación LaTeX

Siempre que se modifique un archivo `.tex` (especialmente `main.tex`), es obligatorio compilarlo inmediatamente.
Si se producen errores, se debe corregir el código fuente y recompilar tantas veces como sea necesario hasta que la compilación sea exitosa.

**REGLA ESTRICTA**: Está terminantemente prohibido ejecutar compilaciones LaTeX (ej. `pdflatex`) cuyo output caiga en el directorio raíz del proyecto. Siempre se debe proveer el flag `-output-directory=build/<subcarpeta>` de forma que el directorio raíz quede limpio de archivos `.aux`, `.log`, `.pdf`, etc. Si accidentalmente se compila en el raíz, se deben limpiar los archivos generados inmediatamente.
