# Guía de Estilo y Convenciones Tipográficas

Esta guía documenta la notación matemática, normas tipográficas, nomenclatura estandarizada y corrección de erratas de conversión (como las procedentes del rescate de documentos ODT) para el desarrollo del libro y artículos sobre **Álgebras de Boole**.

---

## 1. Conjunto de las Partes (Power Set)

- **Norma Estándar**:
  - El conjunto de las partes de un conjunto $U$ debe representarse siempre utilizando la **$P$ caligráfica** de Weierstrass (`\wp` en LaTeX):
    $$\wp(U) \quad \text{o} \quad \wp\left(U\right)$$

- **Patrón de Errata por Rescate desde ODT / LibreOffice Math**:
  - Debido a artefactos del motor de ecuaciones de LibreOffice, el símbolo `\wp` se convierte frecuentemente como `@U`, `@(U)` o `@ U`.
  - **Regla de Corrección**: Sustituir de manera sistemática cualquier caso de `@U`, `@(U)` o `B := @U` por `\wp(U)` / `B \triangleq \wp(U)`.

---

## 2. Signatura Notacional y Progresión Formal

Para evitar confusiones con la aritmética elemental, el documento evoluciona progresivamente a lo largo de dos notaciones:

### Phase I: Signatura de Retículos (Formalismo Inicial)
- **Operaciones binarias**:
  - supremo / join: $\vee$ (`\vee`)
  - ínfimo / meet: $\wedge$ (`\wedge`)
- **Constantes extremas**:
  - elemento mínimo: $\bot$ (`\bot`)
  - elemento máximo: $\top$ (`\top`)
- **Operación unaria de complemento**:
  - negación lógica: $\neg a$ (`\neg a`)
- **Condiciones iniciales de estructura (Pre-axiomas)**:
  - Conjunto base: $\text{EsConjunto}(\mathbb{B})$
  - Constantes pertenecientes: $\bot \in \mathbb{B}$, $\top \in \mathbb{B}$

### Phase II: Notación de Sistemas Digitales (Transición Práctica)
- **Suma lógica**: $+$
- **Producto lógico**: $\cdot$
- **Cero y Uno**: $0, 1$
- **Complementario**: $\overline{x}$ (`\overline{x}`) o $x'$ (`x'`)

---

## 3. Identificadores Cortos para Teoremas y Justificaciones

Para las líneas de deducción lógica en las demostraciones (especialmente en los entornos desplegables de `ocgx2`), utilizaremos las siguientes etiquetas cortas estandarizadas:

| Concepto | Signatura Retículo | Signatura Digital |
| :--- | :--- | :--- |
| Elemento neutro supremo/suma | $ElemNeu_\vee$ | $ElemNeu_+$ |
| Elemento neutro ínfimo/producto | $ElemNeu_\wedge$ | $ElemNeu_\cdot$ |
| Conmutatividad supremo/suma | $Comm_\vee$ | $Comm_+$ |
| Conmutatividad ínfimo/producto | $Comm_\wedge$ | $Comm_\cdot$ |
| Distributividad supremo/suma | $Dist_\vee$ | $Dist_+$ |
| Distributividad ínfimo/producto | $Dist_\wedge$ | $Dist_\cdot$ |
| Complementario supremo/suma | $Comp_\vee$ | $Comp_+$ |
| Complementario ínfimo/producto | $Comp_\wedge$ | $Comp_\cdot$ |
| Idempotencia | $Idemp_\vee, Idemp_\wedge$ | $Idemp_+, Idemp_\cdot$ |
| Unicidad de neutros | $Unic_e, Unic_u$ | $Unic_0, Unic_1$ |
| Leyes de De Morgan | $Mor_\vee, Mor_\wedge$ | $Mor_+, Mor_\cdot$ |
| Leyes de Absorción | $Abs_{\vee,\wedge}$ | $Abs_{+,\cdot}$ |
| Álgebra Trivial | $Triv$ | $Triv$ |

---

## 4. Tipografía y Mapeo de Caracteres en LaTeX

1. **Símbolo de Igualdad por Definición**:
   - Usar `\triangleq` ($\triangleq$) o la macro `\newunicodechar{≝}{\triangleq}`. Evitar meter el carácter UTF-8 sin declarar.

2. **Clases de Equivalencia y Corchetes Dobles**:
   - Usar `\llbracket` y `\rrbracket` (`\usepackage{stmaryrd}`) para representar $\llbracket A \rrbracket$.
   - Mapear `⟦` $\rightarrow$ `\llbracket` y `⟧` $\rightarrow$ `\rrbracket`.

3. **Matrices y Tablas de Cayley**:
   - Al renderizar tablas de operaciones completas (como la tabla $17 \times 17$ de $B_{16}$), asegurar la definición `\setcounter{MaxMatrixCols}{25}` en el preámbulo para evitar el error `! Extra alignment tab has been changed to \cr.`.

4. **Variables y Alfabeto Griego**:
   - Usar notación LaTeX estándar `\alpha`, `\beta`, `\gamma`, `\delta` o mapear explícitamente las mayúsculas griegas UTF-8 (`Α`, `Β`, `Γ`, `Δ`) a `\mathrm{A}`, `\mathrm{B}`, `\Gamma`, `\Delta`.

---

## 5. Diferencia Simétrica y Operadores de Triángulo ($\Delta$)

- **Causa de Renderizado Gigante**:
  - En las fórmulas convertidas automáticamente desde ODT / LibreOffice Math, el operador de diferencia simétrica se exportó como `\bigtriangleup`.
  - En TeX, `\bigtriangleup` está definido por defecto como un operador de pantalla de gran tamaño (clase `\mathop`), similar a `\sum` o `\bigcup`. En expresiones matemáticas independientes (`\[ ... \]` o `$$ ... $$`), TeX lo escala a tamaño gigante.

- **Norma y Solución Estándar**:
  - La diferencia simétrica de dos conjuntos $A$ y $B$ debe escribirse con la Delta mayúscula y espaciado de operador binario:
    $$A \mathbin{\Delta} B \quad \text{o} \quad A \symdiff B$$
  - En LaTeX estándar (`amsmath`/`amssymb`), no existe un comando nativo por defecto denominado `\symdiff`. Para dotar al código fuente de mayor claridad semántica, hemos definido la macro `\symdiff` y redefinido `\bigtriangleup`:
    ```latex
    \providecommand{\symdiff}{\mathbin{\Delta}}
    \renewcommand{\bigtriangleup}{\symdiff}
    ```
  - En el código fuente TeX y Markdown, se recomienda usar directamente `A \symdiff B` o `A \mathbin{\Delta} B`.

---

## 6. Operadores Universales (Axiomática de Sheffer y Peirce)

- **Convención Adoptada**:
  - Para los operadores binarios universales (capaces de definir toda la estructura del Álgebra de Boole de forma autosuficiente):
    - **NAND (Trazo de Sheffer)**: Flecha vertical hacia arriba $\uparrow$ (`\uparrow` o `\mathbin{\uparrow}`).
    - **NOR (Flecha de Peirce)**: Flecha vertical hacia abajo $\downarrow$ (`\downarrow` o `\mathbin{\downarrow}`).

- **Justificación de Diseño Tipográfico**:
  - Aunque en la literatura clásica se emplea en ocasiones la barra vertical ($|$) para el trazo de Sheffer, se rechaza dicha opción por su asimetría tipográfica respecto a la flecha. Se adopta la convención simétrica de flechas verticales ($\uparrow$ y $\downarrow$).
  - Queda **descartado el uso del símbolo `@`** como operador formal en los textos definitivos.

- **Expresiones Canónicas en Función de $\uparrow$ (NAND)**:
  - Complementario: $x' \triangleq x \uparrow x$
  - Suma lógica (OR): $x + y \triangleq (x \uparrow y)' = (x \uparrow y) \uparrow (x \uparrow y)$
  - Producto lógico (AND): $x \cdot y \triangleq x' \uparrow y' = (x \uparrow x) \uparrow (y \uparrow y)$
  - Cero ($0$): $0 \triangleq x \uparrow x'$
  - Uno ($1$): $1 \triangleq 0'$
