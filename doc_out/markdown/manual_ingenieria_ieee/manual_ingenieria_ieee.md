$$
\gdef\symdiff{\mathbin{\vartriangle}}
\gdef\llbracket{\lbrack\!\lbrack}
\gdef\rrbracket{\rbrack\!\rbrack}
\gdef\triangleq{\stackrel{\mathrm{def}}{=}}
$$

# Introducción a las Puertas Lógicas

En la ingeniería y el diseño digital, las operaciones abstractas del
álgebra de Boole se implementan físicamente mediante circuitos
integrados denominados **puertas lógicas**. Existen dos normativas
principales para representar gráficamente estas puertas:

- **Normativa Tradicional Distintiva (MIL-STD-806B / ANSI Y32.14)**: Es
  la representación clásica donde cada operación se asocia a una forma
  geométrica distinta. Es el estándar de facto en la enseñanza, en los
  diagramas de ingeniería y en la mayoría de herramientas de diseño
  (CAD).

- **Normativa Rectangular Moderna (IEEE Std 91-1984 / IEC 60617)**:
  Utiliza bloques rectangulares uniformes, diferenciando la operación
  mediante un símbolo identificador interno (por ejemplo, `&` para AND,
  $\ge 1$ para OR, `=1` para XOR). Aunque es el estándar internacional
  vigente, su uso es menos intuitivo visualmente y, por tanto, menos
  popular.

A continuación se comparan ambas nomenclaturas para las puertas
fundamentales y derivadas. En el resto del documento utilizaremos la
representación tradicional distintiva (ANSI) por su claridad visual.

## Puertas Lógicas Universales y Derivadas

## Tablas de Verdad

Las tablas de verdad describen exhaustivamente el comportamiento de cada
puerta lógica para todos los valores posibles de entrada en el álgebra
bivaluada ($0$ y $1$).

   $a$   $\overline{a}$
  ----- ----------------
   $0$        $1$
   $1$        $0$

  : Tablas de verdad para las compuertas lógicas básicas y derivadas.

   $a$   $b$   $a + b$   $a \cdot b$   $\overline{a \cdot b}$   $\overline{a + b}$   $a \oplus b$   $\overline{a \oplus b}$
  ----- ----- --------- ------------- ------------------------ -------------------- -------------- -------------------------
   $0$   $0$     $0$         $0$                $1$                    $1$               $0$                  $1$
   $0$   $1$     $1$         $0$                $1$                    $0$               $1$                  $0$
   $1$   $0$     $1$         $0$                $1$                    $0$               $1$                  $0$
   $1$   $1$     $1$         $1$                $0$                    $0$               $0$                  $1$

  : Tablas de verdad para las compuertas lógicas básicas y derivadas.

# Postulados de Huntington (Versión Circuital)

Los postulados del álgebra de Boole se pueden representar de forma
circuital asumiendo que los valores booleanos $0$ y $1$ son niveles
lógicos (GND y VCC respectivamente).

::::: preaxioma
Operaciones básicasoperaciones_ing Existen dos operaciones lógicas
fundamentales (AND y OR) y una operación unaria (NOT).

:::: center
::: circuitikz
(and) at (0,0) ; at (and.in 1) $a$; at (and.in 2) $b$; at (and.out)
$a \cdot b$;

(or) at (4,0) ; at (or.in 1) $a$; at (or.in 2) $b$; at (or.out) $a + b$;

(not) at (8,0) ; at (not.in) $a$; at (not.out) $\overline{a}$;
:::
::::
:::::

::: postulado
Elemento Neutroneutro_ing

- Para la suma lógica (OR), el elemento neutro es el $0$: $$a + 0 = a$$

  :::: center
  ::: circuitikz
  (or) at (0,0) ; at (or.in 1) $a$; at (or.in 2) $0$; at (or.out) $a$;
  :::
  ::::

- Para el producto lógico (AND), el elemento neutro es el $1$:
  $$a \cdot 1 = a$$

  :::: center
  ::: circuitikz
  (and) at (0,0) ; at (and.in 1) $a$; at (and.in 2) $1$; at (and.out)
  $a$;
  :::
  ::::
:::

::: postulado
Conmutatividadconmut_ing El orden de conexión de las entradas a una
puerta no altera la salida.

- $a + b = b + a$

  :::: center
  ::: circuitikz
  (or1) at (0,0) ; at (or1.in 1) $a$; at (or1.in 2) $b$; at (or1.out)
  $a+b$;

  at (2.5,0) $=$;

  (or2) at (5,0) ; at (or2.in 1) $b$; at (or2.in 2) $a$; at (or2.out)
  $b+a$;
  :::
  ::::

- $a \cdot b = b \cdot a$

  :::: center
  ::: circuitikz
  (and1) at (0,0) ; at (and1.in 1) $a$; at (and1.in 2) $b$; at
  (and1.out) $a \cdot b$;

  at (2.5,0) $=$;

  (and2) at (5,0) ; at (and2.in 1) $b$; at (and2.in 2) $a$; at
  (and2.out) $b \cdot a$;
  :::
  ::::
:::

::: postulado
Distributividaddistrib_ing

- Del producto sobre la suma:
  $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$

  :::: center
  ::: circuitikz
  (or1) at (0,-0.5) ; at (or1.in 1) $b$; at (or1.in 2) $c$;

  (and1) at (2.5,0) ; at (and1.in 1) $a$; (or1.out) -\| (and1.in 2);

  at (4.5,-0.25) $=$;

  (and2) at (7,0.5) ; at (and2.in 1) $a$; at (and2.in 2) $b$;

  (and3) at (7,-1) ; at (and3.in 1) $a$; at (and3.in 2) $c$;

  (or2) at (9.5,-0.25) ; (and2.out) -\| (or2.in 1); (and3.out) -\|
  (or2.in 2);
  :::
  ::::

- De la suma sobre el producto:
  $a + (b \cdot c) = (a + b) \cdot (a + c)$

  :::: center
  ::: circuitikz
  (and1) at (0,-0.5) ; at (and1.in 1) $b$; at (and1.in 2) $c$;

  (or1) at (2.5,0) ; at (or1.in 1) $a$; (and1.out) -\| (or1.in 2);

  at (4.5,-0.25) $=$;

  (or2) at (7,0.5) ; at (or2.in 1) $a$; at (or2.in 2) $b$;

  (or3) at (7,-1) ; at (or3.in 1) $a$; at (or3.in 2) $c$;

  (and2) at (9.5,-0.25) ; (or2.out) -\| (and2.in 1); (or3.out) -\|
  (and2.in 2);
  :::
  ::::
:::

::: postulado
Existencia de Elementos Inversos (Complementos)inverso_ing Para cada
variable, existe un inversor lógico tal que:

- $a + \overline{a} = 1$

  :::: center
  ::: circuitikz
  (not) at (0,-0.5) ; at (not.in) $a$;

  (or) at (2.5,0) ; at (or.in 1) $a$; (not.out) -\| (or.in 2);

  at (4,0) $=$; at (4.5,0) $1$;
  :::
  ::::

- $a \cdot \overline{a} = 0$

  :::: center
  ::: circuitikz
  (not) at (0,-0.5) ; at (not.in) $a$;

  (and) at (2.5,0) ; at (and.in 1) $a$; (not.out) -\| (and.in 2);

  at (4,0) $=$; at (4.5,0) $0$;
  :::
  ::::
:::

## El Principio de Dualidad

El Principio de Dualidad establece que si una expresión o teorema es
válido en álgebra de Boole, su expresión dual también lo será. La
expresión dual se obtiene intercambiando las operaciones AND ($\cdot$) y
OR ($+$), y las constantes lógicas $0$ y $1$. Este principio permite a
los ingenieros digitales transformar fácilmente diseños basados en sumas
a productos (y viceversa) y entender la simetría subyacente en todos los
teoremas que se exponen a continuación.

# Teoremas Fundamentales

::: teorema
Idempotenciaidemp_ing

- $a + a = a$

  :::: center
  ::: circuitikz
  (or) at (0,0) ; at (or.in 1) $a$; at (or.in 2) $a$;

  at (2.5,0) $=$; at (3,0) $a$;
  :::
  ::::

- $a \cdot a = a$

  :::: center
  ::: circuitikz
  (and) at (0,0) ; at (and.in 1) $a$; at (and.in 2) $a$;

  at (2.5,0) $=$; at (3,0) $a$;
  :::
  ::::
:::

::: teorema
Identidad (Elementos Absorbentes)identidad_ing

- $a + 1 = 1$

  :::: center
  ::: circuitikz
  (or) at (0,0) ; at (or.in 1) $a$; at (or.in 2) $1$;

  at (2.5,0) $=$; at (3,0) $1$;
  :::
  ::::

- $a \cdot 0 = 0$

  :::: center
  ::: circuitikz
  (and) at (0,0) ; at (and.in 1) $a$; at (and.in 2) $0$;

  at (2.5,0) $=$; at (3,0) $0$;
  :::
  ::::
:::

::: teorema
Absorciónabsorcion_ing

- $a + (a \cdot b) = a$

  :::: center
  ::: circuitikz
  (and) at (0,-0.5) ; at (and.in 1) $a$; at (and.in 2) $b$;

  (or) at (2.5,0) ; at (or.in 1) $a$; (and.out) -\| (or.in 2);

  at (4.5,0) $=$; at (5,0) $a$;
  :::
  ::::

- $a \cdot (a + b) = a$

  :::: center
  ::: circuitikz
  (or) at (0,-0.5) ; at (or.in 1) $a$; at (or.in 2) $b$;

  (and) at (2.5,0) ; at (and.in 1) $a$; (or.out) -\| (and.in 2);

  at (4.5,0) $=$; at (5,0) $a$;
  :::
  ::::
:::

::: teorema
Leyes de De Morgandemorgan_ing

- $\overline{a + b} = \overline{a} \cdot \overline{b}$ (Una puerta NOR
  equivale a una AND con entradas negadas)

  :::: center
  ::: circuitikz
  (nor) at (0,0) ; at (nor.in 1) $a$; at (nor.in 2) $b$; at (nor.out)
  $\overline{a+b}$;

  at (3.5,0) $=$;

  (and) at (7.5,0) ; (not1) at (4.5,0.7) ; (not2) at (4.5,-0.7) ; at
  (not1.in) $a$; at (not2.in) $b$; (not1.out) \|- (and.in 1); (not2.out)
  \|- (and.in 2); at (and.out) $\overline{a} \cdot \overline{b}$;
  :::
  ::::

- $\overline{a \cdot b} = \overline{a} + \overline{b}$ (Una puerta NAND
  equivale a una OR con entradas negadas)

  :::: center
  ::: circuitikz
  (nand) at (0,0) ; at (nand.in 1) $a$; at (nand.in 2) $b$; at
  (nand.out) $\overline{a \cdot b}$;

  at (3.5,0) $=$;

  (or) at (7.5,0) ; (not1) at (4.5,0.7) ; (not2) at (4.5,-0.7) ; at
  (not1.in) $a$; at (not2.in) $b$; (not1.out) \|- (or.in 1); (not2.out)
  \|- (or.in 2); at (or.out) $\overline{a} + \overline{b}$;
  :::
  ::::
:::

::::: teorema
Involución (Doble Negación)involucion_ing $\overline{\overline{a}} = a$

:::: center
::: circuitikz
(not1) at (0,0) ; (not2) at (2,0) ; at (not1.in) $a$; (not1.out) --
(not2.in);

at (4,0) $=$; at (4.5,0) $a$;
:::
::::
:::::

::: teorema
Asociatividadasoc_ing

- $a + (b + c) = (a + b) + c$

  :::: center
  ::: circuitikz
  (or1) at (0,-0.5) ; at (or1.in 1) $b$; at (or1.in 2) $c$;

  (or2) at (2.5,0) ; at (or2.in 1) $a$; (or1.out) -\| (or2.in 2);

  at (4.5,0) $=$;

  (or3) at (6.5,0.5) ; at (or3.in 1) $a$; at (or3.in 2) $b$;

  (or4) at (9,0) ; (or3.out) -\| (or4.in 1); at (or4.in 2) $c$;
  :::
  ::::

- $a \cdot (b \cdot c) = (a \cdot b) \cdot c$

  :::: center
  ::: circuitikz
  (and1) at (0,-0.5) ; at (and1.in 1) $b$; at (and1.in 2) $c$;

  (and2) at (2.5,0) ; at (and2.in 1) $a$; (and1.out) -\| (and2.in 2);

  at (4.5,0) $=$;

  (and3) at (6.5,0.5) ; at (and3.in 1) $a$; at (and3.in 2) $b$;

  (and4) at (9,0) ; (and3.out) -\| (and4.in 1); at (and4.in 2) $c$;
  :::
  ::::
:::

::::: teorema
Orden de Retículoorden_ing La equivalencia entre que una compuerta OR
ignore una entrada y una compuerta AND fuerce la otra:
$$a + b = a \iff a \cdot b = b$$

:::: center
::: circuitikz
(or) at (0,0) ; at (or.in 1) $a$; at (or.in 2) $b$; at (or.out) $a$;

at (3,0) $\iff$;

(and) at (6,0) ; at (and.in 1) $a$; at (and.in 2) $b$; at (and.out) $b$;
:::
::::
:::::

::::: teorema
Equivalencia de Operacionesequa_op_ing Si una puerta OR y una puerta AND
con las mismas entradas producen el mismo resultado $Y$, entonces ambas
entradas deben ser idénticas: $$a + b = a \cdot b \implies a = b$$

:::: center
::: circuitikz
(or) at (0,1) ; (and) at (0,-1) ; at (or.in 1) $a$; at (or.in 2) $b$; at
(and.in 1) $a$; at (and.in 2) $b$; at (or.out) $Y$; at (and.out) $Y$;

at (3,0) $\implies$; at (4,0) $a = b$;
:::
::::
:::::

::: teorema
Cancelacióncancelacion_ing Si tanto la suma como el producto de $a$ con
$b$ coinciden con los de $a$ con $c$, entonces $b$ y $c$ son el mismo
valor.
$$(a + b = a + c) \text{ y } (a \cdot b = a \cdot c) \implies b = c$$
:::

# Propiedades de los Operadores Derivados

::: teorema
Conmutatividad (NAND y NOR)conmut_deriv_ing

- NAND: $\overline{a \cdot b} = \overline{b \cdot a}$

  :::: center
  ::: circuitikz
  (nand1) at (0,0) ; at (nand1.in 1) $a$; at (nand1.in 2) $b$;

  at (2.5,0) $=$;

  (nand2) at (5,0) ; at (nand2.in 1) $b$; at (nand2.in 2) $a$;
  :::
  ::::

- NOR: $\overline{a + b} = \overline{b + a}$

  :::: center
  ::: circuitikz
  (nor1) at (0,0) ; at (nor1.in 1) $a$; at (nor1.in 2) $b$;

  at (2.5,0) $=$;

  (nor2) at (5,0) ; at (nor2.in 1) $b$; at (nor2.in 2) $a$;
  :::
  ::::
:::

::: definicion
Ausencia de Asociatividad (NAND y NOR)no_asoc_ing A diferencia de AND y
OR, las operaciones NAND y NOR **no son asociativas**. Por lo tanto, no
se pueden conectar en cascada de forma directa manteniendo la misma
función.
$$\overline{\overline{a \cdot b} \cdot c} \neq \overline{a \cdot \overline{b \cdot c}}$$
$$\overline{\overline{a + b} + c} \neq \overline{a + \overline{b + c}}$$
:::

::::: teorema
NAND/NOR de 3 entradas vs Cascada Binarianand_cascada_ing A consecuencia
de su falta de asociatividad, una puerta NAND (o NOR) de múltiples
entradas **no** es equivalente a una cascada de puertas de 2 entradas.
$$\overline{a \cdot b \cdot c} \neq \overline{\overline{a \cdot b} \cdot c}$$

:::: center
::: circuitikz
(nand3) at (0,0) ; at (nand3.in 1) $a$; at (nand3.in 2) $b$; at
(nand3.in 3) $c$;

at (2.5,0) $\neq$;

(nand2a) at (5,0.5) ; at (nand2a.in 1) $a$; at (nand2a.in 2) $b$;

(nand2b) at (7.5,-0.25) ; (nand2a.out) -\| (nand2b.in 1); at (nand2b.in
2) $c$;
:::
::::
:::::

::: teorema
Inexistencia de Elemento Neutrono_neutro_ing Las puertas NAND y NOR
carecen de elemento neutro. No existe un valor $x \in \{0,1\}$ tal que
$\overline{a \cdot x} = a$.
:::

::: teorema
Operaciones Exclusivas (XOR y XNOR)xor_xnor_ing La operación XOR produce
un 1 solo si las entradas son diferentes. La operación XNOR produce un 1
solo si las entradas son iguales.

- XOR: $a \oplus b = \overline{a}b + a\overline{b}$

  :::: center
  ::: circuitikz
  (xor) at (0,0) ; at (xor.in 1) $a$; at (xor.in 2) $b$; at (xor.out)
  $a \oplus b$;

  at (3,0) $=$;

  (and1) at (6,0.8) ; (not1) at (4,1.5) ; at (not1.in) $a$; (not1.out)
  \|- (and1.in 1); (4,0.1) \|- (and1.in 2); at (4,0.1) $b$;

  (and2) at (6,-0.8) ; (not2) at (4,-1.5) ; at (not2.in) $b$; (not2.out)
  \|- (and2.in 2); (4,-0.1) \|- (and2.in 1); at (4,-0.1) $a$;

  (or) at (8.5,0) ; (and1.out) -\| (or.in 1); (and2.out) -\| (or.in 2);
  :::
  ::::

- XNOR: $\overline{a \oplus b} = \overline{a}\overline{b} + ab$

  :::: center
  ::: circuitikz
  (xnor) at (0,0) ; at (xnor.in 1) $a$; at (xnor.in 2) $b$; at
  (xnor.out) $\overline{a \oplus b}$;

  at (3,0) $=$;

  (and1) at (6,0.8) ; (not1) at (4,1.5) ; (not2) at (4,0.1) ; at
  (not1.in) $a$; at (not2.in) $b$; (not1.out) \|- (and1.in 1);
  (not2.out) \|- (and1.in 2);

  (and2) at (6,-0.8) ; at (4,-0.1) $a$; at (4,-1.5) $b$; (4,-0.1) \|-
  (and2.in 1); (4,-1.5) \|- (and2.in 2);

  (or) at (8.5,0) ; (and1.out) -\| (or.in 1); (and2.out) -\| (or.in 2);
  :::
  ::::
:::

::: teorema
Conmutatividad y Asociatividad de XORasoc_xor_ing La puerta XOR es
conmutativa y asociativa.

- Conmutatividad: $a \oplus b = b \oplus a$

  :::: center
  ::: circuitikz
  (xor1) at (0,0) ; at (xor1.in 1) $a$; at (xor1.in 2) $b$;

  at (2.5,0) $=$;

  (xor2) at (5,0) ; at (xor2.in 1) $b$; at (xor2.in 2) $a$;
  :::
  ::::

- Asociatividad: $a \oplus (b \oplus c) = (a \oplus b) \oplus c$

  :::: center
  ::: circuitikz
  (xor1) at (0,-0.5) ; at (xor1.in 1) $b$; at (xor1.in 2) $c$;

  (xor2) at (2.5,0) ; at (xor2.in 1) $a$; (xor1.out) -\| (xor2.in 2);

  at (4.5,0) $=$;

  (xor3) at (6.5,0.5) ; at (xor3.in 1) $a$; at (xor3.in 2) $b$;

  (xor4) at (9,0) ; (xor3.out) -\| (xor4.in 1); at (xor4.in 2) $c$;
  :::
  ::::
:::

::: teorema
Idempotencia Cruzada (NAND/NOR como NOT)idemp_cruzada_ing

- $\overline{a \cdot a} = \overline{a}$

  :::: center
  ::: circuitikz
  (nand) at (0,0) ; at (-2, 0) $a$; (-2,0) -- (-1.5,0); (-1.5,0) \|-
  (nand.in 1); (-1.5,0) \|- (nand.in 2);

  at (2.5,0) $=$;

  (not) at (5,0) ; at (not.in) $a$; at (not.out) $\overline{a}$;
  :::
  ::::

- $\overline{a + a} = \overline{a}$

  :::: center
  ::: circuitikz
  (nor) at (0,0) ; at (-2, 0) $a$; (-2,0) -- (-1.5,0); (-1.5,0) \|-
  (nor.in 1); (-1.5,0) \|- (nor.in 2);

  at (2.5,0) $=$;

  (not) at (5,0) ; at (not.in) $a$; at (not.out) $\overline{a}$;
  :::
  ::::
:::

::: teorema
Generación Universal Básicagen_univ_ing

- AND desde NAND: $(a \cdot b) = \overline{\overline{a \cdot b}}$

  :::: center
  ::: circuitikz
  (nand1) at (0,0) ; (nand2) at (3,0) ; at (nand1.in 1) $a$; at
  (nand1.in 2) $b$; (nand1.out) -- (1.5,0); (1.5,0) \|- (nand2.in 1);
  (1.5,0) \|- (nand2.in 2);

  at (5.5,0) $=$;

  (and) at (8,0) ; at (and.in 1) $a$; at (and.in 2) $b$; at (and.out)
  $a \cdot b$;
  :::
  ::::

- OR desde NOR: $(a + b) = \overline{\overline{a + b}}$

  :::: center
  ::: circuitikz
  (nor1) at (0,0) ; (nor2) at (3,0) ; at (nor1.in 1) $a$; at (nor1.in 2)
  $b$; (nor1.out) -- (1.5,0); (1.5,0) \|- (nor2.in 1); (1.5,0) \|-
  (nor2.in 2);

  at (5.5,0) $=$;

  (or) at (8,0) ; at (or.in 1) $a$; at (or.in 2) $b$; at (or.out)
  $a + b$;
  :::
  ::::
:::

::: teorema
Generación Universal Cruzada (De Morgan)gen_cruz_ing

- OR desde NAND: $a + b = \overline{\overline{a} \cdot \overline{b}}$

  :::: center
  ::: circuitikz
  (nand_a) at (0,1) ; (nand_b) at (0,-1) ; (nand_out) at (3,0) ;

  at (-2, 1) $a$; (-2,1) -- (-1.5,1); (-1.5,1) \|- (nand_a.in 1);
  (-1.5,1) \|- (nand_a.in 2);

  at (-2, -1) $b$; (-2,-1) -- (-1.5,-1); (-1.5,-1) \|- (nand_b.in 1);
  (-1.5,-1) \|- (nand_b.in 2);

  (nand_a.out) \|- (nand_out.in 1); (nand_b.out) \|- (nand_out.in 2);

  at (5.5,0) $=$;

  (or) at (8,0) ; at (or.in 1) $a$; at (or.in 2) $b$; at (or.out)
  $a + b$;
  :::
  ::::

- AND desde NOR: $a \cdot b = \overline{\overline{a} + \overline{b}}$

  :::: center
  ::: circuitikz
  (nor_a) at (0,1) ; (nor_b) at (0,-1) ; (nor_out) at (3,0) ;

  at (-2, 1) $a$; (-2,1) -- (-1.5,1); (-1.5,1) \|- (nor_a.in 1);
  (-1.5,1) \|- (nor_a.in 2);

  at (-2, -1) $b$; (-2,-1) -- (-1.5,-1); (-1.5,-1) \|- (nor_b.in 1);
  (-1.5,-1) \|- (nor_b.in 2);

  (nor_a.out) \|- (nor_out.in 1); (nor_b.out) \|- (nor_out.in 2);

  at (5.5,0) $=$;

  (and) at (8,0) ; at (and.in 1) $a$; at (and.in 2) $b$; at (and.out)
  $a \cdot b$;
  :::
  ::::
:::

::: teorema
Fijación y Absorción (NAND/NOR)constantes_deriv_ing

- Fijación (Inversión): $\overline{a \cdot 1} = \overline{a}$ y
  $\overline{a + 0} = \overline{a}$

  :::: center
  ::: circuitikz
  (nand) at (0,0) ; at (nand.in 1) $a$; at (nand.in 2) $1$; at
  (nand.out) $\overline{a}$;

  (nor) at (6,0) ; at (nor.in 1) $a$; at (nor.in 2) $0$; at (nor.out)
  $\overline{a}$;
  :::
  ::::

- Absorción (Salida constante): $\overline{a \cdot 0} = 1$ y
  $\overline{a + 1} = 0$

  :::: center
  ::: circuitikz
  (nand) at (0,0) ; at (nand.in 1) $a$; at (nand.in 2) $0$; at
  (nand.out) $1$;

  (nor) at (6,0) ; at (nor.in 1) $a$; at (nor.in 2) $1$; at (nor.out)
  $0$;
  :::
  ::::
:::

::: teorema
Elementos Inversores (XOR/XNOR)inv_xor_ing La puerta XOR actúa como
inversor controlado si una entrada es 1, y como buffer si es 0. La XNOR
se comporta de forma dual.

- Buffer: $a \oplus 0 = a$ y $\overline{a \oplus 1} = a$

  :::: center
  ::: circuitikz
  (xor) at (0,0) ; at (xor.in 1) $a$; at (xor.in 2) $0$; at (xor.out)
  $a$;

  (xnor) at (6,0) ; at (xnor.in 1) $a$; at (xnor.in 2) $1$; at
  (xnor.out) $a$;
  :::
  ::::

- Inversor: $a \oplus 1 = \overline{a}$ y
  $\overline{a \oplus 0} = \overline{a}$

  :::: center
  ::: circuitikz
  (xor) at (0,0) ; at (xor.in 1) $a$; at (xor.in 2) $1$; at (xor.out)
  $\overline{a}$;

  (xnor) at (6,0) ; at (xnor.in 1) $a$; at (xnor.in 2) $0$; at
  (xnor.out) $\overline{a}$;
  :::
  ::::
:::

::::: teorema
Elemento Inverso de sí mismo (Grupo Abeliano)idemp_nula_xor_ing La XOR
de una señal consigo misma siempre da $0$, mientras que la XNOR da $1$.

:::: center
::: circuitikz
(xor) at (0,0) ; (xor.in 1) -- ++(-0.5,0) coordinate(p1); (xor.in 2) --
++(-0.5,0) coordinate(p2); (p1) -- (p2); (p1) -- (p2)
coordinate\[midway\] (pmid); (pmid) node\[circ\] -- ++(-0.5,0)
node\[left\] $a$; at (xor.out) $0$;

(xnor) at (6,0) ; (xnor.in 1) -- ++(-0.5,0) coordinate(p3); (xnor.in 2)
-- ++(-0.5,0) coordinate(p4); (p3) -- (p4); (p3) -- (p4)
coordinate\[midway\] (pmid2); (pmid2) node\[circ\] -- ++(-0.5,0)
node\[left\] $a$; at (xnor.out) $1$;
:::
::::
:::::

::::: teorema
Propiedades de Negación en XOR/XNORnegacion_xor_ing Negar cualquiera de
las entradas invierte la salida (cambia de XOR a XNOR).
$$\overline{a} \oplus b = a \oplus \overline{b} = \overline{a \oplus b} = a \odot b$$

:::: center
::: circuitikz
(xor1) at (0,0) ; (not1) at (-1.5, 0.28) ; at (not1.in) $a$; at (-1.5,
-0.28) $b$; (not1.out) -- (xor1.in 1); (-1.5, -0.28) -- (xor1.in 2);

at (2,0) $=$;

(xor2) at (4,0) ; at (2.5, 0.28) $a$; (not2) at (2.5, -0.28) ; at
(not2.in) $b$; (2.5, 0.28) -- (xor2.in 1); (not2.out) -- (xor2.in 2);

at (6,0) $=$;

(xnor) at (8,0) ; at (xnor.in 1) $a$; at (xnor.in 2) $b$;
:::
::::
:::::

::: teorema
Distributividad de AND sobre XORdist_and_xor_ing
$$a \cdot (b \oplus c) = (a \cdot b) \oplus (a \cdot c)$$
:::

# Generalización a $n$ variables

Las propiedades de asociatividad de las puertas AND, OR, y XOR permiten
su generalización natural a $n$ variables. Gráficamente se representan
como puertas simples con $n$ patas de entrada. Aunque las puertas NAND y
NOR carecen de la propiedad de asociatividad, debido a su enorme
importancia práctica, se define por convención su generalización a $n$
variables como la negación de las correspondientes operaciones AND y OR
múltiples.

:::: center
::: circuitikz
(and4) at (0,0) ; at (and4.in 1) $a$; at (and4.in 2) $b$; at (and4.in 3)
$c$; at (and4.in 4) $d$; at (and4.out)
$\displaystyle \prod_{i=1}^4 x_i$;

(or3) at (5,0) ; at (or3.in 1) $a$; at (or3.in 2) $b$; at (or3.in 3)
$c$; at (or3.out) $\displaystyle \sum_{i=1}^3 x_i$;

(xor3) at (10,0) ; at (xor3.in 1) $a$; at (xor3.in 2) $b$; at (xor3.in
3) $c$; at (xor3.out) $\displaystyle \bigoplus_{i=1}^3 x_i$;

(nand3) at (2.5,-3.5) ; at (nand3.in 1) $a$; at (nand3.in 2) $b$; at
(nand3.in 3) $c$; at (nand3.out)
$\displaystyle \overline{\prod_{i=1}^3 x_i}$;

(nor3) at (7.5,-3.5) ; at (nor3.in 1) $a$; at (nor3.in 2) $b$; at
(nor3.in 3) $c$; at (nor3.out)
$\displaystyle \overline{\sum_{i=1}^3 x_i}$;
:::
::::
