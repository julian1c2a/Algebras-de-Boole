# Guía del Protocolo de Compilación y Revisión de Documentos LaTeX

Este documento establece la metodología y los pasos necesarios para la compilación, revisión y depuración individualizada de cada archivo `.tex` del proyecto.

---

## 1. Reglas Generales de Estructura de Salida

1. **Aislamiento por Documento**:
   - Cada archivo `.tex` se compilará en su propio subdirectorio dedicado dentro de la carpeta `build/`:
     ```
     build/<nombre_de_documento_tex>/
     ```
   - *Ejemplo*: El documento `material/Capitulo_01_Primeros_Axiomas_de_Huntington_y_ejemplos_varios.tex` compilará su salida en:
     ```
     build/Capitulo_01_Primeros_Axiomas_de_Huntington_y_ejemplos_varios/
     ```
   - El PDF final resultante se ubicará en `build/<nombre_de_documento_tex>/<nombre_de_documento_tex>.pdf`.

2. **Directorio de Tests**:
   - Todo ejecutable o artefacto de pruebas asociadas se compilará en la ruta especificada:
     ```
     build/build_tests/
     ```

---

## 2. Tipos de Archivos TeX y Tratamiento

- **Documentos Autónomos Completos** (ej. `main.tex`, memorias TFG, etc.):
  - Contienen su propia cabecera (`\documentclass`, preámbulo, `\begin{document}`).
  - Se compilan directamente indicando el directorio de salida correspondiente.

- **Fragmentos TeX Rescatados de ODT** (ej. Capítulos 1 al 9):
  - Proceden de la conversión mediante Pandoc. Si carecen de estructura de documento autónoma, se compilarán utilizando una plantilla/wrapper autónomo o la opción de cabecera autónoma de Pandoc (`-s`), generando el PDF en su subdirectorio correspondiente.

---

## 3. Protocolo de Compilación y Depuración Paso a Paso

Para cada documento de la lista, seguiremos secuencialmente los siguientes 5 pasos:

### Paso 1: Creación del subdirectorio de salida
Crear la estructura previa de carpetas antes de invocar el motor de LaTeX:
```bash
mkdir -p build/<nombre_de_documento_tex>
```

### Paso 2: Compilación (Doble Pasada)
Ejecutar `pdflatex` direccionando la salida al subdirectorio correspondiente:
```powershell
$env:PATH = "C:\msys64\ucrt64\bin;C:\msys64\usr\bin;" + $env:PATH
pdflatex -interaction=nonstopmode -output-directory=build/<nombre_de_documento_tex> <ruta_al_archivo.tex>
```
*(Se realizará una segunda pasada cuando sea necesario resolver referencias cruzadas o tablas de contenidos)*.

### Paso 3: Inspección de Logs y Errores
- Analizar el archivo de log generado en `build/<nombre_de_documento_tex>/<nombre_de_documento_tex>.log`.
- Verificar la ausencia de errores fatales (`! Emergency stop`, `! Undefined control sequence`, etc.).
- Registrar advertencias de formato (`Overfull \hbox`, desbordamientos de ecuaciones o símbolos no reconocidos).

### Paso 4: Corrección de Sintaxis LaTeX
- En caso de detectar errores tipográficos, símbolos no soportados o desajustes matemáticos derivados del rescate desde ODT, aplicar correcciones sobre el archivo `.tex` fuente.

### Paso 5: Confirmación y Registro de PDF
- Confirmar la correcta generación del PDF en `build/<nombre_de_documento_tex>/<nombre_de_documento_tex>.pdf`.
- Anotar el número de páginas y el estado final de la revisión.

---

## 4. Matriz de Estado de Compilación

| # | Archivo `.tex` | Subdirectorio de Salida | Estado | Páginas / Tamaño | Notas / Correcciones |
|---|----------------|-------------------------|--------|------------------|----------------------|
| 1 | `main.tex` | `build/main/` | OK | 17 págs | Documento principal completo |
| 2 | `Capitulo_01...tex` | `build/Capitulo_01_Primeros_Axiomas.../` | OK | 249 KB | `\wp(U)` para Partes, `\symdiff` ($\mathbin{\Delta}$) |
| 3 | `Capitulo_02...tex` | `build/Capitulo_02_Desarrollo_de_teoremas/` | OK | 129 KB | Desarrollo de teoremas iniciales |
| 4 | `Capitulo_03...tex` | `build/Capitulo_03/` | OK | 117 KB | Reemplazo `@` por `\uparrow` (Sheffer) |
| 5 | `Capitulo_04...tex` | `build/Capitulo_04_Dualidad/` | OK | 218 KB | Principio de Dualidad |
| 6 | `Capitulo_05...tex` | `build/Capitulo_05/` | Pendiente | - | - |
| 7 | `Capitulo_06...tex` | `build/Capitulo_06/` | Pendiente | - | - |
| 8 | `Capitulo_07...tex` | `build/Capitulo_07/` | Pendiente | - | - |
| 9 | `Capitulo_08...tex` | `build/Capitulo_08/` | Pendiente | - | - |
| 10| `Capitulo_09...tex` | `build/Capitulo_09/` | Pendiente | - | - |
| 11| `Fundamentos_2023_rescatado.tex` | `build/Fundamentos_2023_rescatado/` | Pendiente | - | - |
| 12| `Fundamentos_de_Electronica_Parte_Digital-2023...tex` | `build/Fundamentos_de_Electronica_Parte_Digital_2023/` | Pendiente | - | - |
| 13| `Matematicas_subyacentes.tex` | `build/Matematicas_subyacentes/` | Pendiente | - | - |
| 14| `Matemáticas_que_subyacen_a_la_Electrónica_Digital-2012...tex` | `build/Matemáticas_que_subyacen_2012/` | Pendiente | - | - |
| 15| `Independencia_de_los_axiomas_de_Huntington_de_1904.tex` | `build/Independencia_Huntington_1904/` | Pendiente | - | - |
| 16| `independencia_huntington.tex` | `build/independencia_huntington/` | Pendiente | - | - |
| 17| `indep_raw.tex` | `build/indep_raw/` | Pendiente | - | - |
| 18| `Álgebras de Boole - otro.tex` | `build/Algebras_de_Boole_otro/` | Pendiente | - | - |
| 19| `ÁlgebrasDeBoole.tex` | `build/AlgebrasDeBoole/` | Pendiente | - | - |
| 20| `Sets.tex` | `build/Sets/` | Pendiente | - | - |
| 21| `memoria_TFG_...12_15.tex` | `build/memoria_TFG_12_15/` | Pendiente | - | - |
| 22| `memoria_TFG_...12_17.tex` | `build/memoria_TFG_12_17/` | Pendiente | - | - |
| 23| `memoria_TFG_...orden_22.tex` | `build/memoria_TFG_orden_22/` | Pendiente | - | - |
| 24| `memoria_TFG_...22_08.tex` | `build/memoria_TFG_22_08/` | Pendiente | - | - |
| 25| `TFG_Matematicas_...doc.tex` | `build/TFG_Matematicas_doc/` | Pendiente | - | - |
