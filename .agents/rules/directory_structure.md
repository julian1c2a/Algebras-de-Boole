# Estructura de Directorios

Esta regla describe la estructura de directorios del proyecto y cómo deben manejarse los archivos recuperados.

## Directorio `recuperaciones`

Todo el material antiguo o rescatado debe residir dentro de `./recuperaciones`, subdividido en:

- `./recuperaciones/tfg/`: Para todos los archivos relacionados con `TFG_Matematicas_*` y `memoria_TFG_*`.
  - `markdown/`: Archivos `.md`.
  - `tex/`: Archivos `.tex`.

- `./recuperaciones/digital/`: Para el resto del contenido de digital y Álgebras de Boole (Capítulos, fundamentos, etc.).
  - `markdown/`: Archivos `.md`.
  - `tex/`: Archivos `.tex`.

*(Nota: Los archivos PDF, ODT, BIB y otros formatos afines se quedan en la raíz de su carpeta correspondiente, es decir, en `tfg/` o `digital/`)*.

## Construcción (Build)

A la hora de construir y compilar:
- El esquema del directorio `recuperaciones` se respetará dentro del directorio de construcción (`./build/recuperaciones/...`).
- El documento principal del proyecto (`main.tex`) se construirá en su propia subcarpeta: `./build/main/`.

El `Makefile` ya está configurado para depositar los archivos generados en estos directorios. No se deben mezclar los outputs de compilación con el código fuente.
