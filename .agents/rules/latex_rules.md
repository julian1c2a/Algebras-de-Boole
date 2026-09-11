# LaTeX Compilation Rules

- **Nunca compilar LaTeX dejando resultados en el directorio raíz.** Siempre se debe usar un directorio `build/` (o similar) para los resultados de compilación (usando `-output-directory=build`).
- Se debe mantener el directorio raíz libre de archivos auxiliares (`.aux`, `.log`, `.out`, etc.). Si se generan accidentalmente en la raíz, deben eliminarse o utilizar el comando `make clean` para automatizar su limpieza.
