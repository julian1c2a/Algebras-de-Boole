# Bitácora de Aprendizajes sobre LaTeX, Errores de Compilación y Entorno

Este documento recoge los problemas técnicos, errores de compilación de LaTeX y soluciones de configuración del entorno descubiertos durante la formalización y rescate de los materiales sobre Álgebra de Boole.

---

## 1. Configuración del Entorno TeX en Windows / MSYS2

### 1.1 Rutas corruptas en `texmf.cnf`
- **Síntoma**:
  - `pdflatex` o `fmtutil-sys` fallan al buscar archivos de formato (`pdflatex.fmt`) o archivos `.ini` con errores del tipo `no appropriate script or program found: fmtutil`.
- **Causa**:
  - `texmf.cnf` (tanto en `/ucrt64/share/texmf-dist/web2c/texmf.cnf` como en `/ucrt64/etc/texmf/web2c/texmf.cnf`) contenía cadenas de rutas corruptas tipo `/C;C:msys64msys64Crt64/share`.
- **Solución**:
  - Modificar las variables base en ambos archivos `texmf.cnf`:
    ```ini
    TEXMFROOT = C:/msys64/ucrt64/share
    TEXMFLOCAL = C:/msys64/ucrt64/local/share/texmf;C:/msys64/ucrt64/share/texmf
    TEXMFSYSVAR = C:/msys64/ucrt64/var/lib/texmf
    TEXMFSYSCONFIG = C:/msys64/ucrt64/etc/texmf
    ```

### 1.2 Búsqueda directa en disco (Restricción `!!`)
- **Síntoma**:
  - `kpsewhich` no encontraba archivos existentes en el sistema (ej. `pdflatex.ini`).
- **Causa**:
  - La presencia del prefijo `!!` en la definición `TEXMFDBS` de `texmf.cnf` obliga a TeX a buscar **únicamente** en la base de datos `ls-R`. Si `ls-R` está incompleto o desactualizado, el archivo se considera inexistente.
- **Solución**:
  - Eliminar los prefijos `!!` en `TEXMFDBS` y `TEXMF` para permitir la búsqueda directa en el sistema de archivos cuando sea necesario:
    ```ini
    TEXMFDBS = {$TEXMFLOCAL,$TEXMFSYSCONFIG,$TEXMFSYSVAR,$TEXMFDIST}
    ```

### 1.3 Incompatibilidad de subcarpeta `bin/windows` en scripts TeX Live
- **Síntoma**:
  - `fmtutil.pl` o `runscript.tlu` fallan buscando la ruta `bin/windows/kpsewhich`.
- **Causa**:
  - En Windows nativo TeX Live organiza ejecutables en `bin/win32` o `bin/windows`, mientras que en MSYS2 están directamente en `bin/`.
- **Solución**:
  - Crear un directorio de enlace/Junction en MSYS2:
    ```cmd
    mklink /j "C:\msys64\ucrt64\bin\windows" "C:\msys64\ucrt64\bin"
    ```

### 1.4 Reconstrucción de formatos `.fmt`
- **Síntoma**:
  - Error `I can't find the format file pdflatex.fmt!` o desajuste de versión del ejecutable.
- **Solución**:
  - Generar el formato en modo extendido e instalarlo en `var/lib/texmf`:
    ```powershell
    pdftex -ini -jobname=pdflatex -progname=pdflatex "*pdflatex.ini"
    Copy-Item "C:\msys64\ucrt64\share\texmf-dist\tex\latex\tex-ini-files\pdflatex.fmt" "C:\msys64\ucrt64\var\lib\texmf\web2c\pdftex\pdflatex.fmt"
    ```

---

## 2. Resoluciones de Errores de Sintaxis LaTeX

### 2.1 Tablas y Matrices Grandes (Superación del límite de 10 columnas)
- **Error**:
  ```text
  ! Extra alignment tab has been changed to \cr.
  ```
- **Causa**:
  - El paquete `amsmath` limita por defecto a 10 el número máximo de columnas permitidas en entornos de matriz como `bmatrix` o `pmatrix`. Al representar tablas de Cayley para álgebras de 16 elementos ($B_{16}$, 17 columnas), se supera el límite.
- **Solución**:
  - Incrementar el contador `MaxMatrixCols` en el preámbulo:
    ```latex
    \usepackage{amsmath}
    \setcounter{MaxMatrixCols}{25}
    ```

### 2.2 Anidamiento Profundo de Listas (`enumerate` / `itemize`)
- **Error**:
  ```text
  ! LaTeX Error: Too deeply nested.
  ```
- **Causa**:
  - LaTeX estándar restringe el anidamiento de entornos `enumerate` a un máximo de 4 niveles. La conversión desde ODT con subapartados jerárquicos profundos genera listas anidadas hasta 6 u 8 niveles.
- **Solución**:
  - Configurar el paquete `enumitem` en el preámbulo para soportar hasta 9 niveles:
    ```latex
    \usepackage{enumitem}
    \setlistdepth{9}
    \renewlist{enumerate}{enumerate}{9}
    \setlist[enumerate,1]{label=\arabic*.}
    \setlist[enumerate,2]{label=\alph*.}
    \setlist[enumerate,3]{label=\roman*.}
    \setlist[enumerate,4]{label=\arabic*.}
    \setlist[enumerate,5]{label=\alph*.}
    \setlist[enumerate,6]{label=\roman*.}
    \setlist[enumerate,7]{label=\arabic*.}
    \setlist[enumerate,8]{label=\alph*.}
    \setlist[enumerate,9]{label=\roman*.}
    ```

### 2.3 Símbolos Matemáticos y Caracteres Unicode no reconocidos en `pdflatex`
- **Error**:
  ```text
  ! LaTeX Error: Unicode character <código> not set up for use with LaTeX.
  ```
- **Causa**:
  - `pdflatex` trabaja en 8 bits y no reconoce directamente caracteres UTF-8 como el símbolo de definición `≝` (U+225D), los corchetes dobles de equivalencia `⟦` (U+27E8) y `⟧` (U+27E9), o caracteres griegos en UTF-8 (`Α`, `Β`, `Γ`, `Δ`, etc.).
- **Solución**:
  - Utilizar `newunicodechar` junto a `stmaryrd` para remapear cada símbolo al comando LaTeX correspondiente:
    ```latex
    \usepackage{amssymb,amsmath}
    \usepackage{stmaryrd}
    \usepackage{newunicodechar}

    \providecommand{\triangleq}{\stackrel{\text{def}}{=}}
    \newunicodechar{≝}{\triangleq}
    \newunicodechar{⟦}{\llbracket}
    \newunicodechar{⟧}{\rrbracket}

    % Mayúsculas griegas en notación matemática
    \newunicodechar{Α}{\mathrm{A}}
    \newunicodechar{Β}{\mathrm{B}}
    \newunicodechar{Γ}{\Gamma}
    \newunicodechar{Δ}{\Delta}
    \newunicodechar{Λ}{\Lambda}
    % Minúsculas griegas
    \newunicodechar{α}{\alpha}
    \newunicodechar{β}{\beta}
    \newunicodechar{γ}{\gamma}
    \newunicodechar{δ}{\delta}
    \newunicodechar{λ}{\lambda}
    ```

---

## 3. Protocolo de Gestión de Salida de Compilación

1. Cada archivo `.tex` compila en su subdirectorio aislado:
   `build/<nombre_de_documento_tex>/`
2. Los ejecutables de test o pruebas automatizadas se alojan en:
   `build/build_tests/`
