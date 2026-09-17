# Introducción

El álgebra de Boole, originalmente introducida por George Boole en su
obra de 1854 *The Laws of Thought*, fue posteriormente axiomatizada de
forma rigurosa. En 1904, el matemático estadounidense Edward Vermilye
Huntington presentó un conjunto de postulados independientes que definen
formalmente una estructura de álgebra de Boole.

Para evitar cualquier confusión conceptual con la aritmética
tradicional, en esta fase inicial emplearemos la signatura propia de la
teoría de retículos, utilizando los símbolos $+$ (supremo o join) y
$\cdot$ (ínfimo o meet), junto a los elementos constantes $0$ (mínimo) y
$1$ (máximo). El complemento se denotará con el símbolo de la barra
superior, como en $\overline{a}$. Más adelante, y por conveniencia
práctica, transitaremos hacia la notación clásica de sistemas digitales
($+$, $\cdot$, $0$, $1$).

## Pre-Axiomas de la Estructura

Antes de enunciar los postulados, debemos definir rigurosamente sobre
qué elementos y operaciones estamos trabajando.

Partimos de un ente matemático $\mathbb{B}$.

::: preaxioma
Estructura de Conjunto - EsConjunto($\mathbb{B}$)esconj Se requiere que
$\mathbb{B}$ sea un conjunto.
:::

::: preaxioma
Elementos Constantes - Constantesconstantes Este conjunto ha de cumplir
que tiene dos elementos que llamaremos constantes, tales que
$0 \in \mathbb{B}$ y $1 \in \mathbb{B}$. En principio, no asumimos nada
sobre la igualdad o desigualdad de estas constantes.
:::

Además, vamos a definir dos operaciones binarias internas que
denotaremos por $+$ y $\cdot$. Estas deben satisfacer rigurosamente la
definición de función:

::: preaxioma
Operación Binaria Interna $+$ - OpBinInt$_+$opbinint_vee
$+ : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una operación
binaria interna.
:::

::: preaxioma
Operación Binaria Interna $\cdot$ - OpBinInt$_\cdot$opbinint_wedge
$\cdot : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una operación
binaria interna.
:::

Para poder usar estos conceptos con mayor seguridad y flexibilidad en
las futuras demostraciones formales, asignaremos nombres cortos a las
condiciones de existencia y unicidad de la imagen para estas
operaciones:

::: preaxioma
Existencia $+$ - Existencia$_+$exist_vee Para todo par existe imagen en
$\mathbb{B}$. Es decir,
$\forall \langle a,b \rangle \in \mathbb{B} \times \mathbb{B}$,
$\exists c \in \mathbb{B}$ tal que $a + b = c$.
:::

::: preaxioma
Existencia $\cdot$ - Existencia$_\cdot$exist_wedge Análogamente,
$\forall \langle a,b \rangle \in \mathbb{B} \times \mathbb{B}$,
$\exists d \in \mathbb{B}$ tal que $a \cdot b = d$.
:::

::: preaxioma
Unicidad $+$ - Unicidad$_+$unic_vee Para un par solo existe una imagen.
Esto es, si $a + b = c$ y $a + b = d$, entonces $c = d$.
:::

::: preaxioma
Unicidad $\cdot$ - Unicidad$_\cdot$unic_wedge De igual forma para el
ínfimo, si $a \cdot b = c$ y $a \cdot b = d$, entonces $c = d$.
:::

## Los Postulados de Huntington (1904)

Sobre el sistema $(\mathbb{B}, +, \cdot, 0, 1)$ que cumple los
pre-axiomas anteriores, diremos que forma un álgebra de Boole si
satisface los siguientes postulados:

::: postulado
Elemento neutro $+$ - $ElemNeu_+$neutro_vee Todo elemento operado
mediante $+$ con el mínimo $0$ da como resultado el mismo elemento; es
decir, $0$ no altera el valor original:
$$\forall a \in \mathbb{B}, \quad a + 0 = a$$
:::

::: postulado
Elemento neutro $\cdot$ - $ElemNeu_\cdot$neutro_wedge Todo elemento
operado mediante $\cdot$ con el máximo $1$ da como resultado el mismo
elemento, quedando inalterado:
$$\forall a \in \mathbb{B}, \quad a \cdot 1 = a$$
:::

::: postulado
Conmutatividad $+$ - $Comm_+$conmut_vee El orden de los operandos al
aplicar la operación $+$ es indiferente, obteniéndose exactamente el
mismo resultado: $$\forall a, b \in \mathbb{B}, \quad a + b = b + a$$
:::

::: postulado
Conmutatividad $\cdot$ - $Comm_\cdot$conmut_wedge De la misma forma, el
orden de los operandos al aplicar la operación $\cdot$ tampoco altera el
resultado final:
$$\forall a, b \in \mathbb{B}, \quad a \cdot b = b \cdot a$$
:::

::: postulado
Distributividad $+$ sobre $\cdot$ - $Dist_+$distrib_vee_wedge La
operación $+$ se distribuye sobre la operación $\cdot$. Operar un
elemento con el resultado de un $\cdot$ equivale a operar con $+$ cada
componente individualmente y luego aplicar $\cdot$:
$$\forall a, b, c \in \mathbb{B}, \quad a + (b \cdot c) = (a + b) \cdot (a + c)$$
:::

::: postulado
Distributividad $\cdot$ sobre $+$ - $Dist_\cdot$distrib_wedge_vee De
manera equivalente, el ínfimo ($\cdot$) se reparte de forma distributiva
entre los componentes de un supremo ($+$):
$$\forall a, b, c \in \mathbb{B}, \quad a \cdot (b + c) = (a \cdot b) + (a \cdot c)$$
:::

::: postulado
Complementario - $Comp_+, Comp_\cdot$comp Todo elemento del conjunto
posee al menos un \"complemento\" (o elemento opuesto). Al operarlo con
su complemento mediante $+$ siempre alcanzamos el máximo $1$, y mediante
$\cdot$ siempre caemos al mínimo $0$: $$\begin{align*}
\forall a \in \mathbb{B}, \exists b \in \mathbb{B} \quad : \quad a + b &= 1 \quad (Comp_+) \\
a \cdot b &= 0 \quad (Comp_\cdot)
\end{align*}$$
:::

*Nota: A diferencia de algunas formulaciones clásicas que imponen un
axioma de cardinalidad ($0 \neq 1$) para evitar el álgebra trivial, en
este desarrollo permitiremos la existencia del álgebra trivial.*

# El Principio de Dualidad

Si observamos los postulados de Huntington, notaremos una perfecta
simetría entre las operaciones $+$ y $\cdot$, y entre las constantes $0$
y $1$. Si en cualquier postulado intercambiamos $+$ por $\cdot$ y $0$
por $1$, obtenemos otro postulado válido del sistema.

Este rasgo estructural da lugar al **Principio de Dualidad**: toda
proposición o teorema deducido a partir de estos axiomas tiene un
*teorema dual* que también es válido. La demostración de un teorema dual
se construye manipulando la prueba original y aplicando sistemáticamente
el intercambio de operaciones ($+ \leftrightarrow \cdot$) y constantes
($0 \leftrightarrow 1$). En las siguientes pruebas no evitaremos repetir
las versiones duales; al contrario, haremos hincapié en cómo se manipula
la prueba de uno para obtener la del otro.

## Teoremas Principales Derivados

::: teorema
Unicidad de los elementos neutros - $Unic_e, Unic_u$unicidad_neutros Los
elementos neutros descritos en los postulados son únicos. No existe
ningún otro elemento en el conjunto que se comporte como el mínimo $0$
para la operación $+$, ni ningún otro que actúe como el máximo $1$ para
la operación $\cdot$: $$\begin{align*}
    \exists! e \in \mathbb{B}, \forall a \in \mathbb{B}, a + e &= a \implies e = 0 \quad (Unic_e) \\
    \exists! u \in \mathbb{B}, \forall a \in \mathbb{B}, a \cdot u &= a \implies u = 1 \quad (Unic_u)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $Unic_e$.* Sea $e \in \mathbb{B}$ tal que
$\forall a \in \mathbb{B}, a + e = a$. Tomando $a = 0$: $$\begin{align*}
    e &= e + 0 & (ElemNeu_+) \\
      &= 0 + e & (Comm_+) \\
      &= 0 & (\text{Hipótesis sobre } e)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Unic_u$ (Dual).* Para obtener la prueba dual,
intercambiamos $+$ por $\cdot$ y $0$ por $1$. Sea $u \in \mathbb{B}$ tal
que $\forall a \in \mathbb{B}, a \cdot u = a$. Tomando $a = 1$:
$$\begin{align*}
    u &= u \cdot 1 & (ElemNeu_\cdot) \\
      &= 1 \cdot u & (Comm_\cdot) \\
      &= 1 & (\text{Hipótesis sobre } u)
\end{align*}$$ ◻
:::

::: teorema
Idempotencia - $Idemp_+, Idemp_\cdot$idempotencia Operar un elemento
consigo mismo, independientemente de si usamos $+$ o $\cdot$, no altera
su valor. El elemento se mantiene idéntico a sí mismo: $$\begin{align*}
    \forall a \in \mathbb{B}, \quad a + a &= a \quad (Idemp_+) \\
    \forall a \in \mathbb{B}, \quad a \cdot a &= a \quad (Idemp_\cdot)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $Idemp_+$.* $$\begin{align*}
    a &= a + 0 & (ElemNeu_+) \\
      &= a + (a \cdot \overline{a}) & (Comp_\cdot) \\
      &= (a + a) \cdot (a + \overline{a}) & (Dist_+) \\
      &= (a + a) \cdot 1 & (Comp_+) \\
      &= 1 \cdot (a + a) & (Comm_\cdot) \\
      &= a + a & (ElemNeu_\cdot)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Idemp_\cdot$ (Dual).* Intercambiando los operadores y
constantes de la prueba anterior paso a paso: $$\begin{align*}
    a &= a \cdot 1 & (ElemNeu_\cdot) \\
      &= a \cdot (a + \overline{a}) & (Comp_+) \\
      &= (a \cdot a) + (a \cdot \overline{a}) & (Dist_\cdot) \\
      &= (a \cdot a) + 0 & (Comp_\cdot) \\
      &= 0 + (a \cdot a) & (Comm_+) \\
      &= a \cdot a & (ElemNeu_+)
\end{align*}$$ ◻
:::

::: teorema
Elementos absorbentes - $Abs_{0}, Abs_{1}$absorbentes Cualquier elemento
operado mediante $+$ con el máximo $1$ es absorbido por este, dando como
resultado $1$. De igual manera, operar cualquier elemento mediante
$\cdot$ con el mínimo $0$ siempre resulta en $0$: $$\begin{align*}
    \forall a \in \mathbb{B}, \quad a + 1 &= 1 \\
    \forall a \in \mathbb{B}, \quad a \cdot 0 &= 0
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $a + 1 = 1$.* $$\begin{align*}
    a + 1 &= (a + 1) \cdot 1 & (ElemNeu_\cdot) \\
               &= (a + 1) \cdot (a + \overline{a}) & (Comp_+) \\
               &= a + (1 \cdot \overline{a}) & (Dist_+) \\
               &= a + (\overline{a} \cdot 1) & (Comm_\cdot) \\
               &= a + \overline{a} & (ElemNeu_\cdot) \\
               &= 1 & (Comp_+)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $a \cdot 0 = 0$ (Dual).* $$\begin{align*}
    a \cdot 0 &= (a \cdot 0) + 0 & (ElemNeu_+) \\
               &= (a \cdot 0) + (a \cdot \overline{a}) & (Comp_\cdot) \\
               &= a \cdot (0 + \overline{a}) & (Dist_\cdot) \\
               &= a \cdot (\overline{a} + 0) & (Comm_+) \\
               &= a \cdot \overline{a} & (ElemNeu_+) \\
               &= 0 & (Comp_\cdot)
\end{align*}$$ ◻
:::

::: teorema
Condición de Álgebra Trivialtrivial_cond Si se da el caso extremo de que
el elemento mínimo $0$ y el máximo $1$ son exactamente el mismo,
entonces estamos ante un álgebra que contiene un único elemento en todo
su conjunto (el álgebra trivial):
$$0 = 1 \implies \mathbb{B} = \{1\} = \{0\}$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos que $0 = 1$. Sea $x \in \mathbb{B}$ un elemento
cualquiera: $$\begin{align*}
    x &= x + 0 & (ElemNeu_+) \\
      &= x + 1 & (\text{Hipótesis } 0 = 1) \\
      &= 1 & (Abs_1)
\end{align*}$$ Por tanto, todo elemento $x$ del conjunto es idéntico a
$1$, lo que implica que $\mathbb{B} = \{1\} = \{0\}$. ◻
:::

::: teorema
Complemento Idéntico implica Álgebra Trivialtrivial_comp Si dentro de la
estructura existe algún elemento que sea igual a su propio complemento
($\overline{a} = a$), entonces forzosamente todo el sistema colapsa en
el álgebra trivial de un solo elemento:
$$(\exists a \in \mathbb{B} : \overline{a} = a) \implies \mathbb{B} = \{1\} = \{0\}$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos que existe $a \in \mathbb{B}$ tal que
$\overline{a} = a$. Por el postulado del Complemento ($Comp_+$ y
$Comp_\cdot$), sabemos que $a + \overline{a} = 1$ y
$a \cdot \overline{a} = 0$. Sustituyendo la hipótesis $\overline{a} = a$
en ambas ecuaciones, obtenemos:
$$a + a = 1 \quad \text{y} \quad a \cdot a = 0$$ Aplicando el teorema de
Idempotencia ($Idemp_+$ y $Idemp_\cdot$), sabemos que $a + a = a$ y
$a \cdot a = a$. Por tanto: $$a = 1 \quad \text{y} \quad a = 0$$ Lo cual
implica que $0 = 1$. Aplicando el teorema anterior (Condición de Álgebra
Trivial), concluimos que $\mathbb{B} = \{1\} = \{0\}$. ◻
:::

::: teorema
Propiedades de absorción - $Abs_{+}, Abs_{\cdot}$absorcion Cuando se
combinan ambas operaciones anidando un elemento consigo mismo y con un
tercero, el elemento repetido \"absorbe\" al otro, independientemente
del valor del segundo: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a + (a \cdot b) &= a \\
    \forall a, b \in \mathbb{B}, \quad a \cdot (a + b) &= a
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $Abs_+$.* $$\begin{align*}
    a + (a \cdot b) &= (a \cdot 1) + (a \cdot b) & (ElemNeu_\cdot) \\
                        &= a \cdot (1 + b) & (Dist_\cdot) \\
                        &= a \cdot (b + 1) & (Comm_+) \\
                        &= a \cdot 1 & (Abs_1) \\
                        &= a & (ElemNeu_\cdot)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Abs_\cdot$ (Dual).* $$\begin{align*}
    a \cdot (a + b) &= (a + 0) \cdot (a + b) & (ElemNeu_+) \\
                        &= a + (0 \cdot b) & (Dist_+) \\
                        &= a + (b \cdot 0) & (Comm_\cdot) \\
                        &= a + 0 & (Abs_0) \\
                        &= a & (ElemNeu_+)
\end{align*}$$ ◻
:::

::: teorema
Propiedades de orden de retículo - $Prop_{+,\cdot}$prop_reticulo Existe
una correspondencia biunívoca fundamental entre las dos operaciones:
afirmar que un elemento domina a otro mediante $+$ equivale
matemáticamente a afirmar que el segundo se impone al primero mediante
$\cdot$:
$$\forall a, b \in \mathbb{B}: \quad a + b = a \iff a \cdot b = b$$
:::

**Demostración:**

::: proof
*Demostración de $\implies$.* Supongamos que $a + b = a$.
$$\begin{align*}
    a \cdot b &= b \cdot a & (Comm_\cdot) \\
               &= b \cdot (a + b) & (\text{Hipótesis } a + b = a) \\
               &= b & (Abs_\cdot)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $\impliedby$ (Dual).* Supongamos que $a \cdot b = b$.
$$\begin{align*}
    a + b &= b + a & (Comm_+) \\
               &= (a \cdot b) + a & (\text{Hipótesis } a \cdot b = b) \\
               &= a + (a \cdot b) & (Comm_+) \\
               &= a & (Abs_+)
\end{align*}$$ ◻
:::

::: teorema
Equivalencia de operaciones - $Equa_{+,\cdot}$equa_operaciones Si operar
dos elementos mediante $+$ da exactamente el mismo resultado que
operarlos mediante $\cdot$, esto sólo es lógicamente posible si ambos
elementos son en realidad el mismo:
$$\forall a, b \in \mathbb{B}: \quad a + b = a \cdot b \implies a = b$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos $a + b = a \cdot b$. Observamos que:
$$\begin{align*}
    a &= a + (a \cdot b) & (Abs_+) \\
      &= a + (a + b) & (\text{Hipótesis})
\end{align*}$$ Aplicando $Prop_{+,\cdot}$, dado que $a + (a + b) = a$,
deducimos que $a \cdot (a + b) = a + b$. $$\begin{align*}
    a + b &= a \cdot (a + b) & (\text{Resultado anterior}) \\
             &= a & (Abs_\cdot)
\end{align*}$$ De manera simétrica para $b$: $$\begin{align*}
    b &= b + (a \cdot b) & (Abs_+) \\
      &= b + (a + b) & (\text{Hipótesis}) \\
      &= (a + b) + b & (Comm_+)
\end{align*}$$ Aplicando de nuevo $Prop_{+,\cdot}$ sobre esta igualdad,
obtenemos que $(a + b) \cdot b = a + b$. Pero sabemos por $Abs_\cdot$
que $(a + b) \cdot b = b \cdot (a + b) = b$. Por consiguiente,
$a + b = b$. Finalmente, uniendo ambos resultados: $a = a + b = b$. ◻
:::

::: teorema
Teorema de Cancelación - $Equa_{canc}$equa_canc Si un elemento $a$ se
opera mediante $+$ con $b$ y con $c$ dando el mismo resultado, y además
se opera mediante $\cdot$ con $b$ y con $c$ coincidiendo también los
resultados, entonces forzosamente $b$ y $c$ son el mismo elemento:
$$\forall a, b, c \in \mathbb{B}: \quad a + b = a + c \quad \text{y} \quad a \cdot b = a \cdot c \implies b = c$$
:::

**Demostración:**

::: proof
*Proof.* Este teorema es automejor dualizable al ser sus hipótesis
perfectamente simétricas. $$\begin{align*}
    b &= b \cdot (a + b) & (Abs_\cdot) \\
      &= b \cdot (a + c) & (\text{Hipótesis } a + b = a + c) \\
      &= (b \cdot a) + (b \cdot c) & (Dist_\cdot) \\
      &= (a \cdot b) + (b \cdot c) & (Comm_\cdot) \\
      &= (a \cdot c) + (b \cdot c) & (\text{Hipótesis } a \cdot b = a \cdot c) \\
      &= (c \cdot a) + (c \cdot b) & (Comm_\cdot \text{ aplicado dos veces}) \\
      &= c \cdot (a + b) & (Dist_\cdot) \\
      &= c \cdot (a + c) & (\text{Hipótesis } a + b = a + c) \\
      &= c & (Abs_\cdot)
\end{align*}$$ ◻
:::

::: teorema
Unicidad del complemento - $Unic_{comp}$unic_comp Todo elemento del
conjunto tiene un complemento $\overline{a}$, y este es estrictamente
único. Ningún otro elemento puede cumplir simultáneamente las dos
condiciones del postulado del complemento para un mismo $a$:
$$\forall a, x \in \mathbb{B} : \quad (a + x = 1 \quad \text{y} \quad a \cdot x = 0) \implies x = \overline{a}$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos que existe $x \in \mathbb{B}$ tal que $a + x = 1$ y
$a \cdot x = 0$. $$\begin{align*}
    x &= x \cdot 1 & (ElemNeu_\cdot) \\
      &= x \cdot (a + \overline{a}) & (Comp_+) \\
      &= (x \cdot a) + (x \cdot \overline{a}) & (Dist_\cdot) \\
      &= (a \cdot x) + (x \cdot \overline{a}) & (Comm_\cdot) \\
      &= 0 + (x \cdot \overline{a}) & (\text{Hipótesis } a \cdot x = 0) \\
      &= (a \cdot \overline{a}) + (x \cdot \overline{a}) & (Comp_\cdot) \\
      &= (a + x) \cdot \overline{a} & (Dist_\cdot) \\
      &= 1 \cdot \overline{a} & (\text{Hipótesis } a + x = 1) \\
      &= \overline{a} \cdot 1 & (Comm_\cdot) \\
      &= \overline{a} & (ElemNeu_\cdot)
\end{align*}$$ Por tanto, si $x$ cumple las condiciones de complemento,
$x$ tiene que ser necesariamente $\overline{a}$. ◻
:::

::: teorema
Involución - $Comp_{inv}$comp_inv Aplicar la operación de complemento (o
negación) dos veces consecutivas sobre un mismo elemento cancela su
efecto, devolviendo el elemento original intacto:
$$\forall a \in \mathbb{B}, \quad \overline{(\neg a)} = a$$
:::

**Demostración:**

::: proof
*Proof.* Por definición, el complemento de $\overline{a}$, denotado como
$\overline{(\neg a)}$, es el elemento único que satisface:
$$\overline{a} + \overline{(\neg a)} = 1 \quad \text{y} \quad \overline{a} \cdot \overline{(\neg a)} = 0$$
Sin embargo, por la conmutatividad ($Comm_+$ y $Comm_\cdot$), sabemos
que:
$$\overline{a} + a = a + \overline{a} = 1 \quad \text{y} \quad \overline{a} \cdot a = a \cdot \overline{a} = 0$$
Esto demuestra que $a$ actúa como un complemento de $\overline{a}$. Por
el teorema de unicidad del complemento ($Unic_{comp}$), concluimos
necesariamente que $\overline{(\neg a)} = a$. ◻
:::

::: teorema
Leyes de De Morgan - $Mor_{+, \cdot}$morgan La negación matemática se
distribuye sobre las operaciones, pero al hacerlo, invierte la operación
original: un supremo ($+$) negado se convierte en el ínfimo ($\cdot$) de
las negaciones, y viceversa: $$\begin{align}
    \overline{(a + b)} &= \overline{a} \cdot \overline{b} \\
    \overline{(a \cdot b)} &= \overline{a} + \overline{b}
\end{align}$$ De forma equivalente, aislando las variables mediante la
involución, podemos expresar las operaciones básicas exclusivamente a
partir de su dual negada: $$\begin{align}
    a + b &= \overline{(\neg a \cdot \neg b)} \\
    a \cdot b &= \overline{(\neg a + \neg b)}
\end{align}$$
:::

**Demostración:**

::: proof
*Demostración de
$\overline{(a + b)} = \overline{a} \cdot \overline{b}$.* Para
demostrarlo sin recurrir a la asociatividad, usaremos las propiedades de
absorción. Comprobemos primero la suma:
$(a + b) + (\overline{a} \cdot \overline{b}) = 1$. Sabemos por
$Abs_\cdot$ que $a \cdot (a + b) = a$. $$\begin{align*}
    \overline{a} + (a \cdot (a + b)) &= \overline{a} + a = 1 & (Comp_+) \\
    (\overline{a} + a) \cdot (\overline{a} + (a + b)) &= 1 & (Dist_+) \\
    1 \cdot (\overline{a} + (a + b)) &= 1 & (Comp_+) \\
    \overline{a} + (a + b) &= 1 & (ElemNeu_\cdot)
\end{align*}$$ Simétricamente, como
$b \cdot (a + b) = b \cdot (b + a) = b$, obtenemos
$\overline{b} + (a + b) = 1$. Por tanto: $$\begin{align*}
    (a + b) + (\overline{a} \cdot \overline{b}) &= ((a + b) + \overline{a}) \cdot ((a + b) + \overline{b}) & (Dist_+) \\
    &= (\overline{a} + (a + b)) \cdot (\overline{b} + (a + b)) & (Comm_+) \\
    &= 1 \cdot 1 & (\text{Resultados anteriores}) \\
    &= 1 & (Idemp_\cdot)
\end{align*}$$

Segundo, comprobemos el producto:
$(a + b) \cdot (\overline{a} \cdot \overline{b}) = 0$. Sabemos por
$Abs_+$ que
$\overline{a} + (\overline{a} \cdot \overline{b}) = \overline{a}$.
$$\begin{align*}
    a \cdot (\overline{a} + (\overline{a} \cdot \overline{b})) &= a \cdot \overline{a} = 0 & (Comp_\cdot) \\
    (a \cdot \overline{a}) + (a \cdot (\overline{a} \cdot \overline{b})) &= 0 & (Dist_\cdot) \\
    0 + (a \cdot (\overline{a} \cdot \overline{b})) &= 0 & (Comp_\cdot) \\
    a \cdot (\overline{a} \cdot \overline{b}) &= 0 & (ElemNeu_+)
\end{align*}$$ Simétricamente, como
$\overline{b} + (\overline{a} \cdot \overline{b}) = \overline{b} + (\overline{b} \cdot \overline{a}) = \overline{b}$,
obtenemos $b \cdot (\overline{a} \cdot \overline{b}) = 0$. Por tanto:
$$\begin{align*}
    (a + b) \cdot (\overline{a} \cdot \overline{b}) &= (\overline{a} \cdot \overline{b}) \cdot (a + b) & (Comm_\cdot) \\
    &= ((\overline{a} \cdot \overline{b}) \cdot a) + ((\overline{a} \cdot \overline{b}) \cdot b) & (Dist_\cdot) \\
    &= (a \cdot (\overline{a} \cdot \overline{b})) + (b \cdot (\overline{a} \cdot \overline{b})) & (Comm_\cdot) \\
    &= 0 + 0 & (\text{Resultados anteriores}) \\
    &= 0 & (Idemp_+)
\end{align*}$$ Por el teorema de unicidad ($Unic_{comp}$), concluimos
que $\overline{(a + b)} = \overline{a} \cdot \overline{b}$. ◻
:::

::: proof
*Demostración de $\overline{(a \cdot b)} = \overline{a} + \overline{b}$
(Dual).* Intercambiando operaciones y constantes, comprobamos el
producto: $(a \cdot b) \cdot (\overline{a} + \overline{b}) = 0$. Sabemos
por $Abs_+$ que $a + (a \cdot b) = a$. $$\begin{align*}
    \overline{a} \cdot (a + (a \cdot b)) &= \overline{a} \cdot a = 0 & (Comp_\cdot) \\
    (\overline{a} \cdot a) + (\overline{a} \cdot (a \cdot b)) &= 0 & (Dist_\cdot) \\
    0 + (\overline{a} \cdot (a \cdot b)) &= 0 & (Comp_\cdot) \\
    \overline{a} \cdot (a \cdot b) &= 0 & (ElemNeu_+)
\end{align*}$$ Simétricamente, $\overline{b} \cdot (a \cdot b) = 0$. Por
tanto: $$\begin{align*}
    (a \cdot b) \cdot (\overline{a} + \overline{b}) &= ((a \cdot b) \cdot \overline{a}) + ((a \cdot b) \cdot \overline{b}) & (Dist_\cdot) \\
    &= (\overline{a} \cdot (a \cdot b)) + (\overline{b} \cdot (a \cdot b)) & (Comm_\cdot) \\
    &= 0 + 0 = 0 & (\text{Resultados anteriores})
\end{align*}$$

Comprobemos la suma: $(a \cdot b) + (\overline{a} + \overline{b}) = 1$.
Sabemos por $Abs_\cdot$ que
$\overline{a} \cdot (\overline{a} + \overline{b}) = \overline{a}$.
$$\begin{align*}
    a + (\overline{a} \cdot (\overline{a} + \overline{b})) &= a + \overline{a} = 1 & (Comp_+) \\
    (a + \overline{a}) \cdot (a + (\overline{a} + \overline{b})) &= 1 & (Dist_+) \\
    1 \cdot (a + (\overline{a} + \overline{b})) &= 1 & (Comp_+) \\
    a + (\overline{a} + \overline{b}) &= 1 & (ElemNeu_\cdot)
\end{align*}$$ Simétricamente, $b + (\overline{a} + \overline{b}) = 1$.
Por tanto: $$\begin{align*}
    (a \cdot b) + (\overline{a} + \overline{b}) &= (\overline{a} + \overline{b}) + (a \cdot b) & (Comm_+) \\
    &= ((\overline{a} + \overline{b}) + a) \cdot ((\overline{a} + \overline{b}) + b) & (Dist_+) \\
    &= (a + (\overline{a} + \overline{b})) \cdot (b + (\overline{a} + \overline{b})) & (Comm_+) \\
    &= 1 \cdot 1 = 1 & (\text{Resultados anteriores})
\end{align*}$$ Por $Unic_{comp}$,
$\overline{(a \cdot b)} = \overline{a} + \overline{b}$. ◻
:::

::: proof
*Demostración de $a + b = \overline{(\neg a \cdot \neg b)}$ y su dual.*
Partiendo de $\overline{(\neg a \cdot \neg b)}$, aplicamos De Morgan a
sus componentes: $$\begin{align*}
    \overline{(\neg a \cdot \neg b)} &= \overline{(\neg a)} + \overline{(\neg b)} & (Mor_\cdot) \\
    &= a + b & (Comp_{inv})
\end{align*}$$ Dualizando la expresión, obtenemos de manera idéntica que
$\overline{(\neg a + \neg b)} = a \cdot b$. ◻
:::

::: teorema
Asociatividad - $Asoc_+, Asoc_\cdot$asociatividad El orden en el que se
agrupan tres o más elementos al aplicar de forma consecutiva la misma
operación ($+$ o $\cdot$) no altera el resultado final. Al ubicar este
teorema después de De Morgan, podemos simplificar enormemente su
demostración: $$\begin{align*}
    a + (b + c) &= (a + b) + c \\
    a \cdot (b \cdot c) &= (a \cdot b) \cdot c
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $a + (b + c) = (a + b) + c$.* Primero, demostraremos un
pequeño **Lema de Igualdad por Casos**: Si $x \cdot y = x \cdot z$ y
$\overline{x} \cdot y = \overline{x} \cdot z$, entonces $y = z$.
$$\begin{align*}
    y &= 1 \cdot y & (ElemNeu_\cdot) \\
      &= (x + \overline{x}) \cdot y & (Comp_+) \\
      &= (x \cdot y) + (\overline{x} \cdot y) & (Dist_\cdot) \\
      &= (x \cdot z) + (\overline{x} \cdot z) & (\text{Por hipótesis del Lema}) \\
      &= (x + \overline{x}) \cdot z & (Dist_\cdot) \\
      &= 1 \cdot z = z & (Comp_+, ElemNeu_\cdot)
\end{align*}$$ Sea $L = a + (b + c)$ y $R = (a + b) + c$. Aplicaremos el
lema usando $x = a$, por lo que debemos demostrar que
$a \cdot L = a \cdot R$ y $\overline{a} \cdot L = \overline{a} \cdot R$.

1\) Comprobamos $a \cdot L = a \cdot R$: $$\begin{align*}
    a \cdot L &= a \cdot (a + (b + c)) = a & (Abs_\cdot) \\
    a \cdot R &= a \cdot ((a + b) + c) \\
               &= (a \cdot (a + b)) + (a \cdot c) & (Dist_\cdot) \\
               &= a + (a \cdot c) = a & (Abs_\cdot, Abs_+)
\end{align*}$$ Por tanto, $a \cdot L = a \cdot R$.

2\) Comprobamos $\overline{a} \cdot L = \overline{a} \cdot R$:
$$\begin{align*}
    \overline{a} \cdot L &= \overline{a} \cdot (a + (b + c)) \\
                    &= (\overline{a} \cdot a) + (\overline{a} \cdot (b + c)) & (Dist_\cdot) \\
                    &= 0 + (\overline{a} \cdot (b + c)) & (Comp_\cdot) \\
                    &= \overline{a} \cdot (b + c) & (ElemNeu_+)
\end{align*}$$ $$\begin{align*}
    \overline{a} \cdot R &= \overline{a} \cdot ((a + b) + c) \\
                    &= (\overline{a} \cdot (a + b)) + (\overline{a} \cdot c) & (Dist_\cdot) \\
                    &= ((\overline{a} \cdot a) + (\overline{a} \cdot b)) + (\overline{a} \cdot c) & (Dist_\cdot) \\
                    &= (0 + (\overline{a} \cdot b)) + (\overline{a} \cdot c) & (Comp_\cdot) \\
                    &= (\overline{a} \cdot b) + (\overline{a} \cdot c) & (ElemNeu_+) \\
                    &= \overline{a} \cdot (b + c) & (Dist_\cdot)
\end{align*}$$ Como $\overline{a} \cdot L = \overline{a} \cdot R$,
aplicando el Lema concluimos que $L = R$, es decir,
$a + (b + c) = (a + b) + c$. ◻
:::

::: proof
*Demostración de $a \cdot (b \cdot c) = (a \cdot b) \cdot c$ (Dual
mediante De Morgan).* Al haber demostrado previamente las leyes de De
Morgan, podemos probar la asociatividad del ínfimo de forma directa y
elegante sin necesidad de repetir la manipulación algebraica de la
demostración dual: $$\begin{align*}
    a \cdot (b \cdot c) &= \overline{(\neg a + \neg (b \cdot c))} & (Mor_\cdot \text{ y } Comp_{inv}) \\
                          &= \overline{(\neg a + (\neg b + \neg c))} & (Mor_\cdot) \\
                          &= \overline{((\neg a + \neg b) + \neg c)} & (Asoc_+ \text{ demostrada arriba}) \\
                          &= \overline{(\neg (a \cdot b) + \neg c)} & (Mor_\cdot) \\
                          &= (a \cdot b) \cdot c & (Mor_\cdot \text{ y } Comp_{inv})
\end{align*}$$ ◻
:::

## Generalización a $n$ variables

Habiendo demostrado la asociatividad ($Asoc_+$ y $Asoc_\cdot$) de las
operaciones fundamentales del álgebra de Boole, el orden en el que se
agrupan las variables al aplicar consecutivamente una misma operación
resulta irrelevante. Esto nos permite prescindir de los paréntesis y
extender de forma natural las operaciones binarias a un número
arbitrario $n$ de operandos.

::: definicion
Disyunción (Supremo) de $n$ variablesor_n_variables La disyunción
múltiple de $n$ variables, denotada de forma compacta mediante el
operador $\sum$, se define como la aplicación sucesiva de la operación
$+$: $$\sum_{i=1}^n x_i \triangleq x_1 + x_2 + \dots + x_n$$
:::

::: definicion
Conjunción (Ínfimo) de $n$ variablesand_n_variables De manera análoga,
la conjunción múltiple de $n$ variables, denotada mediante el operador
$\prod$, se define como la aplicación sucesiva de la operación $\cdot$:
$$\prod_{i=1}^n x_i \triangleq x_1 \cdot x_2 \cdot \dots \cdot x_n$$
:::

La existencia de estas operaciones múltiples bien definidas es un pilar
fundamental para desarrollar formas canónicas (como la suma de productos
o producto de sumas) y, como veremos a continuación, servirá de base
para extender el número de entradas de los operadores derivados.

# Operadores Derivados: NAND, NOR, XOR y XNOR

Las ecuaciones obtenidas a partir de las Leyes de De Morgan demuestran
que las operaciones básicas $+$ y $\cdot$ pueden ser expresadas
íntegramente en términos de la negación de su operación dual. Esto
motiva la definición de varios operadores lógicos fundamentales en
sistemas digitales. Dos de ellos (NAND y NOR) son de gran relevancia por
ser funcionalmente completos por sí solos, mientras que otros dos (XOR y
XNOR) son esenciales para funciones aritméticas y de comprobación de
paridad:

::: definicion
Operador NAND (Barra de Sheffer)nand Denotado clásicamente con una
flecha hacia arriba ($\uparrow$), se define como la negación del ínfimo.
$$a \uparrow b \triangleq \overline{(a \cdot b)} = \overline{a} + \overline{b}$$
:::

::: definicion
Operador NOR (Flecha de Peirce)nor Denotado con una flecha hacia abajo
($\downarrow$), se define como la negación del supremo.
$$a \downarrow b \triangleq \overline{(a + b)} = \overline{a} \cdot \overline{b}$$
:::

::: definicion
Operador XOR (O-exclusiva)xor Denotado con el símbolo de suma exclusiva
($\oplus$), evalúa a $1$ cuando exactamente uno de los operandos es $1$
y el otro $0$.
$$a \oplus b \triangleq (a \cdot \overline{b}) + (\overline{a} \cdot b)$$
:::

::: definicion
Operador XNOR (No-O-exclusiva o Equivalencia)xnor Denotado
frecuentemente con $\odot$ o $\leftrightarrow$, es la negación de la
operación XOR y evalúa a $1$ cuando ambos operandos son idénticos.
$$a \odot b \triangleq \overline{(a \oplus b)} = (a \cdot b) + (\overline{a} \cdot \overline{b})$$
:::

::: definicion
Generalización a $n$ variables de NAND y NORgen_nand_nor A diferencia de
los operadores $+$, $\cdot$ y $\oplus$, los operadores NAND ($\uparrow$)
y NOR ($\downarrow$) **no son asociativos**. Sin embargo, debido a su
inmensa importancia práctica en la construcción de circuitos digitales,
se define convencionalmente su generalización a $n$ variables como la
negación de la conjunción o disyunción múltiple, respectivamente:
$$\text{NAND}(x_1, x_2, \dots, x_n) \triangleq \overline{\left( \prod_{i=1}^n x_i \right)}$$
$$\text{NOR}(x_1, x_2, \dots, x_n) \triangleq \overline{\left( \sum_{i=1}^n x_i \right)}$$
:::

## Comportamiento de los Operadores Derivados

Los operadores NAND ($\uparrow$) y NOR ($\downarrow$) presentan una
serie de propiedades algebraicas particulares. Al ser operadores
funcionalmente completos, permiten expresar cualquier otra operación
booleana utilizando exclusivamente uno de ellos.

::: teorema
Idempotencia cruzada (Generación de NOT)idemp_cruzada Operar un elemento
consigo mismo usando NAND o NOR equivale a su complemento (negación):
$$\begin{align*}
    \forall a \in \mathbb{B}, \quad a \uparrow a &= \overline{a} \\
    \forall a \in \mathbb{B}, \quad a \downarrow a &= \overline{a}
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la operación NAND: $$\begin{align*}
    a \uparrow a &\triangleq \overline{(a \cdot a)} & (\text{Definicion de NAND}) \\
                 &= \overline{a} & (Idemp_\cdot)
\end{align*}$$ Para la operación NOR: $$\begin{align*}
    a \downarrow a &\triangleq \overline{(a + a)} & (\text{Definicion de NOR}) \\
                   &= \overline{a} & (Idemp_+)
\end{align*}$$ ◻
:::

::: teorema
Generación del Ínfimo y Supremo (AND y OR)gen_inf_sup A partir de la
propiedad anterior, podemos recuperar las operaciones básicas anidando
las puertas consigo mismas: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a \cdot b &= \overline{(a \uparrow b)} = (a \uparrow b) \uparrow (a \uparrow b) \\
    \forall a, b \in \mathbb{B}, \quad a + b &= \overline{(a \downarrow b)} = (a \downarrow b) \downarrow (a \downarrow b)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la generación del ínfimo (AND): $$\begin{align*}
    \overline{(a \uparrow b)} &\triangleq \overline{(\neg(a \cdot b))} & (\text{Definicion de NAND}) \\
                       &= a \cdot b & (Involucion)
\end{align*}$$ Además, por la idempotencia cruzada demostrada
anteriormente, $x \uparrow x = \overline{x}$, por tanto:
$$\overline{(a \uparrow b)} = (a \uparrow b) \uparrow (a \uparrow b)$$
La demostración para la generación del supremo (OR) es idéntica por
dualidad. ◻
:::

::: teorema
Generación cruzada (Leyes de De Morgan para NAND/NOR)gen_cruzada Podemos
generar la operación opuesta (supremo desde NAND, e ínfimo desde NOR)
negando previamente las entradas: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a + b &= (\overline{a}) \uparrow (\overline{b}) = (a \uparrow a) \uparrow (b \uparrow b) \\
    \forall a, b \in \mathbb{B}, \quad a \cdot b &= (\overline{a}) \downarrow (\overline{b}) = (a \downarrow a) \downarrow (b \downarrow b)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para el supremo (OR): $$\begin{align*}
    (\overline{a}) \uparrow (\overline{b}) &\triangleq \overline{(\neg a \cdot \neg b)} & (\text{Definicion de NAND}) \\
                               &= \overline{(\neg (a + b))} & (Mor_+) \\
                               &= a + b & (Involucion)
\end{align*}$$ La demostración para el ínfimo (AND) sigue los mismos
pasos de manera dual, aplicando $Mor_\cdot$. ◻
:::

::: teorema
Conmutatividadconmut_deriv Al igual que sus operaciones base, ambos
operadores son perfectamente conmutativos: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a \uparrow b &= b \uparrow a \\
    \forall a, b \in \mathbb{B}, \quad a \downarrow b &= b \downarrow a
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la operación NAND: $$\begin{align*}
    a \uparrow b &\triangleq \overline{(a \cdot b)} & (\text{Definicion de NAND}) \\
                 &= \overline{(b \cdot a)} & (Comm_\cdot) \\
                 &\triangleq b \uparrow a & (\text{Definicion de NAND})
\end{align*}$$ Para la operación NOR, es análogo aplicando $Comm_+$. ◻
:::

::: teorema
Inexistencia de Elemento Neutrono_neutro No existe ningún elemento
neutro para las operaciones NAND ni NOR en un álgebra de Boole general.
:::

**Demostración:**

::: proof
*Demostración.* Si existiera un neutro $e$ para la operación NAND,
debería cumplirse que $\forall a, a \uparrow e = a$, es decir,
$\overline{(a \cdot e)} = a$. Si probamos con $e=1$, obtenemos
$\overline{a} = a$, lo cual obliga al colapso en un álgebra trivial. Si
probamos con $e=0$, obtenemos $\overline{0} = a \implies 1 = a$, lo cual
obviamente no se cumple para cualquier elemento $a$. Lo mismo aplica a
la operación NOR. ◻
:::

::: teorema
Comportamiento con las constantes (Fijación y Absorción)constantes_deriv
Fijar una constante específica en uno de los operandos genera
directamente la negación, mientras que usar la constante opuesta actúa
como un pseudo-elemento absorbente (devolviendo un valor constante
inalterable por $a$): $$\begin{align*}
    \text{Inversión: } & a \uparrow 1 = \overline{a} \qquad & a \downarrow 0 &= \overline{a} \\
    \text{Absorción: } & a \uparrow 0 = 1 \qquad & a \downarrow 1 &= 0
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la inversión: $$\begin{align*}
    a \uparrow 1 &= \overline{(a \cdot 1)} = \overline{a} & (ElemNeu_\cdot) \\
    a \downarrow 0 &= \overline{(a + 0)} = \overline{a} & (ElemNeu_+)
\end{align*}$$ Para la absorción: $$\begin{align*}
    a \uparrow 0 &= \overline{(a \cdot 0)} = \overline{0} = 1 & (Abs_0) \\
    a \downarrow 1 &= \overline{(a + 1)} = \overline{1} = 0 & (Abs_1)
\end{align*}$$ ◻
:::

::: teorema
Ausencia de Asociatividadno_asoc_deriv A diferencia del supremo ($+$) y
el ínfimo ($\cdot$), las operaciones NAND y NOR son positivamente NO
asociativas: $$\begin{align*}
    (a \uparrow b) \uparrow c &\neq a \uparrow (b \uparrow c) \\
    (a \downarrow b) \downarrow c &\neq a \downarrow (b \downarrow c)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Desarrollando el lado izquierdo para NAND:
$$(a \uparrow b) \uparrow c = \overline{( (\neg (a \cdot b)) \cdot c )} = (a \cdot b) + \overline{c}$$
Desarrollando el lado derecho:
$$a \uparrow (b \uparrow c) = \overline{( a \cdot (\neg (b \cdot c)) )} = \overline{a} + (b \cdot c)$$
Resulta evidente que
$(a \cdot b) + \overline{c} \neq \overline{a} + (b \cdot c)$ para
combinaciones arbitrarias de variables. El mismo razonamiento aplica de
manera estricta y análoga para demostrar la carencia de asociatividad en
la operación NOR ($\downarrow$). ◻
:::

::: definicion
NAND y NOR de $n$ entradasdef_n_entradas Dado que las puertas NAND y NOR
físicas a menudo tienen más de dos entradas, se definen algebraicamente
para múltiples entradas como la negación de la conjunción o disyunción
de todas ellas: $$\begin{align*}
    \uparrow(x_1, x_2, \dots, x_n) &\triangleq \overline{\left( \prod_{i=1}^n x_i \right)} \\
    \downarrow(x_1, x_2, \dots, x_n) &\triangleq \overline{\left( \sum_{i=1}^n x_i \right)}
\end{align*}$$ En particular, para el caso de 3 entradas que
estudiaremos a continuación: $$\begin{align*}
    \uparrow(a,b,c) &\triangleq \overline{(a \cdot b \cdot c)} \\
    \downarrow(a,b,c) &\triangleq \overline{(a + b + c)}
\end{align*}$$
:::

::: teorema
NAND/NOR múltiple vs agrupación binariamultiple_vs_binaria Como
consecuencia directa de su falta de asociatividad, una operación NAND o
NOR de 3 entradas no es equivalente a la agrupación secuencial en
cascada de operaciones de 2 entradas: $$\begin{align*}
    \uparrow(a,b,c) &\neq (a \uparrow b) \uparrow c \qquad \text{y} \qquad \uparrow(a,b,c) \neq a \uparrow (b \uparrow c) \\
    \downarrow(a,b,c) &\neq (a \downarrow b) \downarrow c \qquad \text{y} \qquad \downarrow(a,b,c) \neq a \downarrow (b \downarrow c)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la NAND de 3 entradas tenemos, por definición y
leyes de De Morgan:
$$\uparrow(a,b,c) \triangleq \overline{(a \cdot b \cdot c)} = \overline{a} + \overline{b} + \overline{c}$$
Sin embargo, la agrupación de dos en dos evaluada anteriormente daba:
$$(a \uparrow b) \uparrow c = (a \cdot b) + \overline{c}$$
Evidentemente,
$\overline{a} + \overline{b} + \overline{c} \neq (a \cdot b) + \overline{c}$.
Lo mismo aplica a las agrupaciones derechas y a las operaciones NOR
equivalentes. ◻
:::

::: teorema
Extensión del Principio de Dualidad (NAND y NOR)dualidad_nand_nor La
inclusión de los operadores derivados expande el Principio de Dualidad
establecido en los postulados iniciales. La expresión dual de cualquier
teorema o identidad que contenga operaciones NAND o NOR se obtiene
intercambiando los operadores $\uparrow$ y $\downarrow$ (además de los
ya conocidos $+ \leftrightarrow \cdot$ y $0 \leftrightarrow 1$).
:::

### Comportamiento de los Operadores XOR y XNOR

A diferencia de los operadores NAND y NOR, que destacan por su
universalidad funcional pero carecen de propiedades algebraicas
deseables (como asociatividad o elemento neutro), los operadores XOR
($\oplus$) y XNOR ($\odot$) exhiben una rica estructura algebraica. A
continuación demostraremos estas propiedades.

::: teorema
Conmutatividadconmut_xor Ambos operadores son conmutativos:
$$a \oplus b = b \oplus a \qquad \text{y} \qquad a \odot b = b \odot a$$
:::

**Demostración:**

::: proof
*Demostración.* Para XOR: $$\begin{align*}
    a \oplus b &\triangleq (a \cdot \overline{b}) + (\overline{a} \cdot b) & (\text{Definición de XOR}) \\
               &= (\overline{a} \cdot b) + (a \cdot \overline{b}) & (Comm_+) \\
               &= (b \cdot \overline{a}) + (\overline{b} \cdot a) & (Comm_\cdot) \\
               &\triangleq b \oplus a & (\text{Definición de XOR})
\end{align*}$$ La demostración para XNOR sigue pasos idénticos
aprovechando la conmutatividad del ínfimo y el supremo. ◻
:::

::: teorema
Elementos Neutros e Inversoresneutro_xor El elemento $0$ actúa como
neutro para la XOR, y $1$ actúa como inversor. De manera dual, $1$ es el
neutro de la XNOR, y $0$ actúa como inversor: $$\begin{align*}
    a \oplus 0 &= a & a \oplus 1 &= \overline{a} \\
    a \odot 1 &= a & a \odot 0 &= \overline{a}
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración para XOR.* Para el elemento $0$ (neutro): $$\begin{align*}
    a \oplus 0 &\triangleq (a \cdot \overline{0}) + (\overline{a} \cdot 0) & (\text{Definición}) \\
                  &= (a \cdot 1) + 0 & (Comp_{inv} \text{ y } Fij_\cdot) \\
                  &= a + 0 & (ElemNeu_\cdot) \\
                  &= a & (ElemNeu_+)
\end{align*}$$ Para el elemento $1$ (inversor): $$\begin{align*}
    a \oplus 1 &\triangleq (a \cdot \overline{1}) + (\overline{a} \cdot 1) & (\text{Definición}) \\
                  &= (a \cdot 0) + \overline{a} & (Comp_{inv} \text{ y } ElemNeu_\cdot) \\
                  &= 0 + \overline{a} & (Fij_\cdot) \\
                  &= \overline{a} & (ElemNeu_+)
\end{align*}$$ Las pruebas para XNOR son totalmente duales. ◻
:::

::: teorema
Elemento Inverso de sí mismo (Grupo Abeliano)idemp_nula_xor La
combinación de un elemento consigo mismo produce una anulación (devuelve
el neutro de la operación correspondiente), actuando cada elemento como
su propio inverso:
$$a \oplus a = 0 \qquad \text{y} \qquad a \odot a = 1$$
:::

**Demostración:**

::: proof
*Demostración.* Para XOR: $$\begin{align*}
    a \oplus a &\triangleq (a \cdot \overline{a}) + (\overline{a} \cdot a) \\
               &= 0 + 0 & (Comp_\cdot \text{ y } Comm_\cdot) \\
               &= 0 & (Idemp_+)
\end{align*}$$ Para XNOR: $$\begin{align*}
    a \odot a &\triangleq (a \cdot a) + (\overline{a} \cdot \overline{a}) \\
              &= a + \overline{a} & (Idemp_\cdot) \\
              &= 1 & (Comp_+)
\end{align*}$$ ◻
:::

::: teorema
Propiedades de Negaciónnegacion_xor Negar cualquiera de las entradas de
forma independiente equivale a negar la operación completa, lo que a su
vez alterna entre XOR y XNOR: $$\begin{align*}
    \overline{(a \oplus b)} &= \overline{a} \oplus b = a \oplus \overline{b} = a \odot b \\
    \overline{(a \odot b)} &= \overline{a} \odot b = a \odot \overline{b} = a \oplus b
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $a \oplus \overline{b} = \overline{(a \oplus b)}$.*
$$\begin{align*}
    a \oplus \overline{b} &\triangleq (a \cdot \overline{(\neg b)}) + (\overline{a} \cdot \overline{b}) \\
                    &= (a \cdot b) + (\overline{a} \cdot \overline{b}) & (Involucion) \\
                    &\triangleq a \odot b & (\text{Definición de XNOR})
\end{align*}$$ Sabiendo por definición que
$a \odot b \triangleq \overline{(a \oplus b)}$, se concluye de forma
inmediata que $a \oplus \overline{b} = \overline{(a \oplus b)}$. ◻
:::

::: teorema
Asociatividadasoc_xor Tanto XOR como XNOR son operadores algebraicamente
asociativos:
$$(a \oplus b) \oplus c = a \oplus (b \oplus c) \qquad \text{y} \qquad (a \odot b) \odot c = a \odot (b \odot c)$$
:::

**Demostración:**

::: proof
*Demostración para XOR.* Primero evaluaremos el miembro izquierdo
$(a \oplus b) \oplus c$. Llamaremos $X = a \oplus b$. $$\begin{align*}
    X \oplus c &\triangleq (X \cdot \overline{c}) + (\overline{X} \cdot c) \\
               &= \big( ((a \cdot \overline{b}) + (\overline{a} \cdot b)) \cdot \overline{c} \big) + \big( \overline{((a \cdot \neg b) + (\neg a \cdot b))} \cdot c \big) \\
               &= \big( ((a \cdot \overline{b}) + (\overline{a} \cdot b)) \cdot \overline{c} \big) + \big( (a \odot b) \cdot c \big) \quad (\text{Definición de XNOR}) \\
               &= \big( (a \cdot \overline{b} \cdot \overline{c}) + (\overline{a} \cdot b \cdot \overline{c}) \big) + \big( ((a \cdot b) + (\overline{a} \cdot \overline{b})) \cdot c \big) \quad (Dist_\cdot) \\
               &= (a \cdot \overline{b} \cdot \overline{c}) + (\overline{a} \cdot b \cdot \overline{c}) \\
               &\quad + (a \cdot b \cdot c) + (\overline{a} \cdot \overline{b} \cdot c) \quad (Dist_\cdot)
\end{align*}$$ Ahora evaluaremos el miembro derecho
$a \oplus (b \oplus c)$. Llamaremos $Y = b \oplus c$. $$\begin{align*}
    a \oplus Y &\triangleq (a \cdot \overline{Y}) + (\overline{a} \cdot Y) \\
               &= (a \cdot (b \odot c)) + (\overline{a} \cdot ((b \cdot \overline{c}) + (\overline{b} \cdot c))) \\
               &= (a \cdot ((b \cdot c) + (\overline{b} \cdot \overline{c}))) + (\overline{a} \cdot b \cdot \overline{c}) + (\overline{a} \cdot \overline{b} \cdot c) \\
               &= (a \cdot b \cdot c) + (a \cdot \overline{b} \cdot \overline{c}) \\
               &\quad + (\overline{a} \cdot b \cdot \overline{c}) + (\overline{a} \cdot \overline{b} \cdot c)
\end{align*}$$ Como podemos observar, ambas expansiones resultan
exactamente en los mismos cuatro minitérminos. Reordenándolos por
conmutatividad ($Comm_+$) demostramos que son idénticos. ◻
:::

::: teorema
Generalización n-aria (XOR y XNOR)gen_xor Dado que ambos operadores han
demostrado ser asociativos y conmutativos, es posible omitir los
paréntesis y generalizar la operación a un número arbitrario $n$ de
variables. Se denotan mediante los operadores de sumatoria y productorio
modificados:
$$\bigoplus_{i=1}^{n} x_i = x_1 \oplus x_2 \oplus \dots \oplus x_n$$
$$\bigodot_{i=1}^{n} x_i = x_1 \odot x_2 \odot \dots \odot x_n$$
:::

::: teorema
Distributividad (AND sobre XOR y OR sobre XNOR)dist_xor El producto
(AND) se distribuye sobre la suma exclusiva (XOR), y dualmente, la suma
(OR) se distribuye sobre la equivalencia (XNOR):
$$a \cdot (b \oplus c) = (a \cdot b) \oplus (a \cdot c)$$
$$a + (b \odot c) = (a + b) \odot (a + c)$$
:::

**Demostración:**

::: proof
*Demostración de AND sobre XOR.* Desarrollando el lado derecho (RHS):
$$\begin{align*}
    (a \cdot b) \oplus (a \cdot c) &\triangleq ((a \cdot b) \cdot \overline{(a \cdot c)}) + (\overline{(a \cdot b)} \cdot (a \cdot c)) \\
                                     &= (a \cdot b \cdot (\overline{a} + \overline{c})) + ((\overline{a} + \overline{b}) \cdot a \cdot c) \quad (Mor_\cdot) \\
                                     &= ((a \cdot b \cdot \overline{a}) + (a \cdot b \cdot \overline{c})) \\
                                     &\quad + ((a \cdot c \cdot \overline{a}) + (a \cdot c \cdot \overline{b})) \quad (Dist_\cdot) \\
                                     &= (0 + (a \cdot b \cdot \overline{c})) + (0 + (a \cdot \overline{b} \cdot c)) \quad (Comp_\cdot \text{ y } Fij_\cdot) \\
                                     &= (a \cdot b \cdot \overline{c}) + (a \cdot \overline{b} \cdot c) \quad (ElemNeu_+) \\
                                     &= a \cdot ((b \cdot \overline{c}) + (\overline{b} \cdot c)) \quad (Dist_\cdot \text{ a la inversa}) \\
                                     &\triangleq a \cdot (b \oplus c) \quad (\text{Def. XOR})
\end{align*}$$ Lo cual demuestra la igualdad. La demostración de la
distributividad para XNOR es rigurosamente dual. ◻
:::

::: teorema
Extensión del Principio de Dualidad (XOR y XNOR)dualidad_xor_xnor De
forma análoga a la relación entre NAND y NOR, los operadores XOR y XNOR
son mutuamente duales. Para obtener la expresión dual de cualquier
proposición que involucre estos operadores, se deben intercambiar
$\oplus$ y $\odot$, manteniendo las reglas de dualidad estándar para los
demás elementos y constantes.
:::

# Instanciación en Álgebras Finitas: Trivial y Bivaluada

La teoría desarrollada en los capítulos anteriores es aplicable a
cualquier álgebra de Boole, sin importar el número de elementos que
contenga el conjunto $B$ (siempre que se cumplan los postulados de
Huntington). Sin embargo, existen dos álgebras finitas de interés
particular por su extrema simplicidad y su aplicación directa en la
teoría de circuitos.

### Álgebra Trivial ($|B| = 1$)

Si definimos el conjunto soporte con un único elemento, $B = \{ c \}$,
nos encontramos ante el álgebra de Boole trivial o degenerada.

Dado que los postulados de Huntington (Postulado 2) exigen la existencia
de un elemento neutro para la disyunción ($0 \in B$) y otro para la
conjunción ($1 \in B$), y puesto que el conjunto solo contiene un único
elemento, estos deben forzosamente coincidir: $$0 = 1 = c$$

Al instanciar cualquier operación definida sobre este conjunto, los
resultados siempre evalúan a dicha constante $c$.

- **Negación:** Por el postulado del complemento, $c + \overline{c} = c$
  y $c \cdot \overline{c} = c$, lo que implica que $\overline{c} = c$.

- **Disyunción y Conjunción:** Por la propiedad de idempotencia,
  $c + c = c$ y $c \cdot c = c$.

- **Operadores Derivados:** Por definición,
  $c \uparrow c = \overline{(c \cdot c)} = \overline{c} = c$. Lo mismo
  sucede con el resto de operadores.

Visualizar esto en tablas de operación (comúnmente conocidas como tablas
de verdad) resulta en estructuras degeneradas de una sola celda, donde
$\circ \in \{ +, \cdot, \uparrow, \downarrow, \oplus, \odot \}$:

::: center
   $a$   $\overline{a}$
  ----- ----------------
   $c$        $c$

   $a$   $b$   $a \circ b$
  ----- ----- -------------
   $c$   $c$       $c$
:::

### Álgebra Bivaluada ($|B| = 2$)

El caso más importante para la ingeniería es el álgebra de Boole
bivaluada, donde el conjunto soporte consta exactamente de los dos
elementos garantizados por los postulados: el neutro disyuntivo y el
neutro conjuntivo. $$B = \{ 0, 1 \}$$ (Asumiendo lógicamente que
$0 \neq 1$).

Procederemos a deducir el comportamiento (las tablas de operación)
instanciando los teoremas y postulados axiomáticos en estos dos únicos
valores.

#### Operaciones Básicas ($\overline{a}$, $+$, $\cdot$)

**1. Negación (Operación unaria $\overline{a}$)**\
El Postulado 5 (Complemento) exige que:
$$0 + \overline{0} = 1 \quad \text{y} \quad 1 + \overline{1} = 1$$ Al
existir solo dos elementos en el conjunto, el único valor que sumado a
$0$ (que es el neutro disyuntivo, por lo que no altera el resultado) da
$1$, es el propio $1$. Por lo tanto, deducimos que $\overline{0} = 1$.
De igual manera, por dualidad, $\overline{1} = 0$.

**2. Disyunción (Operación binaria $+$)**\
Calculamos los cuatro casos posibles instanciando los valores:

- $0 + 0 = 0$ (Por Idempotencia, Teorema 1).

- $0 + 1 = 1$ (Por ser $0$ el elemento neutro, Postulado 2a).

- $1 + 0 = 1$ (Por Conmutatividad, Postulado 3a).

- $1 + 1 = 1$ (Por Idempotencia, Teorema 1).

**3. Conjunción (Operación binaria $\cdot$)**\
Análogamente:

- $1 \cdot 1 = 1$ (Por Idempotencia, Teorema 1).

- $1 \cdot 0 = 0$ (Por ser $1$ el elemento neutro, Postulado 2b).

- $0 \cdot 1 = 0$ (Por Conmutatividad, Postulado 3b).

- $0 \cdot 0 = 0$ (Por Idempotencia, Teorema 1).

#### Operadores Derivados ($\uparrow, \downarrow, \oplus, \odot$)

Podemos obtener las tablas de los operadores derivados aplicando
directamente sus definiciones algebraicas sobre las tablas básicas ya
obtenidas:

**1. NAND y NOR**\
Dado que $a \uparrow b = \overline{(a \cdot b)}$ y
$a \downarrow b = \overline{(a + b)}$, los resultados consisten
simplemente en aplicar el operador complemento ($\overline{a}$) a las
tablas de conjunción y disyunción calculadas previamente.

**2. XOR y XNOR**\
Recordando la definición algebraica
$a \oplus b = (a \cdot \overline{b}) + (\overline{a} \cdot b)$, se puede
evaluar caso por caso (por ejemplo,
$1 \oplus 0 = (1 \cdot 1) + (0 \cdot 0) = 1 + 0 = 1$), pero también
podemos usar directamente los teoremas derivados anteriormente:

- $a \oplus 0 = a$ (Elemento neutro). Por lo tanto: $0 \oplus 0 = 0$, y
  $1 \oplus 0 = 1$.

- $a \oplus 1 = \overline{a}$ (Inversor). Por lo tanto:
  $0 \oplus 1 = 1$, y $1 \oplus 1 = 0$.

Por dualidad, y sabiendo que el XNOR es la negación del XOR, se obtiene
trivialmente que $a \odot b = \overline{(a \oplus b)}$.

#### Resumen: Tablas de Operación Bivaluadas

A continuación, presentamos la consolidación matricial de todas las
operaciones deducidas, conformando las tablas de verdad definitivas del
álgebra de dos valores:

::: {#tab:tablas_bivaluadas}
   $a$   $\overline{a}$
  ----- ----------------
   $0$        $1$
   $1$        $0$

  : Tablas de Verdad consolidadas para las Operaciones del Álgebra de
  Boole de 2 elementos.
:::

::: {#tab:tablas_bivaluadas}
   $a$   $b$   $a + b$   $a \cdot b$   $a \uparrow b$   $a \downarrow b$   $a \oplus b$   $a \odot b$
  ----- ----- --------- ------------- ---------------- ------------------ -------------- -------------
   $0$   $0$     $0$         $0$            $1$               $1$              $0$            $1$
   $0$   $1$     $1$         $0$            $1$               $0$              $1$            $0$
   $1$   $0$     $1$         $0$            $1$               $0$              $1$            $0$
   $1$   $1$     $1$         $1$            $0$               $0$              $0$            $1$

  : Tablas de Verdad consolidadas para las Operaciones del Álgebra de
  Boole de 2 elementos.
:::

## Conclusiones y Transición a la Lógica Digital

Tras haber establecido formalmente la estructura matemática del álgebra
de Boole a partir de los postulados de Huntington, y haber demostrado
rigurosamente sus propiedades fundamentales operando con la signatura
clásica de la teoría de retículos ($+, \cdot, 0, 1$), estamos en
disposición de dar el salto al dominio de la ingeniería.

En la electrónica digital, el interés recae de forma exclusiva sobre un
modelo concreto de álgebra de Boole: el **Álgebra de Conmutación de
Shannon**. Esta es el álgebra de Boole más sencilla posible, cuyo
conjunto subyacente consta únicamente de dos elementos,
$\mathbb{B}_2 = \{0, 1\}$.

A pesar de su aparente simplicidad, el álgebra de $\mathbb{B}_2$ cumple
estrictamente todos los postulados de Huntington (y por ende, todos los
teoremas que hemos derivado) y está contenida formalmente como
subestructura en cualquier otra álgebra de Boole más compleja.

Para adecuar nuestra matemática al diseño de circuitos y sistemas
digitales, adoptaremos a partir de ahora la **notación ingenieril**,
realizando el siguiente isomorfismo simbólico sobre nuestras operaciones
y constantes:

- **Constantes lógicas:** El elemento mínimo $0$ (falso) se denotará
  como **0** (ó nivel bajo de tensión, $L$). El elemento máximo $1$
  (verdadero) se denotará como **1** (ó nivel alto de tensión, $H$).

- **Supremo (Join / Disyunción):** La operación $+$ se denotará mediante
  el operador suma $\mathbf{+}$. En circuitos lógicos, implementa la
  puerta **OR**.

- **Ínfimo (Meet / Conjunción):** La operación $\cdot$ se denotará
  mediante el operador producto $\mathbf{\cdot}$ (frecuentemente
  omitido, escribiendo $ab$ en lugar de $a \cdot b$). Implementa la
  puerta **AND**.

- **Complemento (Negación):** La operación de complemento $\overline{a}$
  se denotará convencionalmente colocando una barra superior sobre la
  variable, $\mathbf{\overline{a}}$, o mediante una comilla
  $\mathbf{a'}$. Implementa la puerta **NOT** (inversor).

- **Operadores Derivados (NAND y NOR):** Las operaciones $\uparrow$ y
  $\downarrow$ mantienen sus símbolos, o bien se expresan directamente
  como el complemento del producto o de la suma ($\overline{a \cdot b}$,
  $\overline{a+b}$). Representan las puertas universales **NAND** y
  **NOR**, fundamentales en el diseño de circuitos integrados.

- **Suma Exclusiva y Equivalencia (XOR y XNOR):** Las operaciones
  introducidas como suma exclusiva y equivalencia lógica se denotan
  mediante $\mathbf{\oplus}$ y $\mathbf{\odot}$. Representan las puertas
  **XOR** (útiles en sumadores o detectores de paridad) y **XNOR**
  (comparadores de igualdad).

- **Operadores n-arios:** Las versiones generalizadas para múltiples
  variables formarán estructuras de puertas lógicas de $n$ entradas. Se
  denotarán mediante los operadores $\sum$ (puerta OR de $n$ entradas),
  $\prod$ (puerta AND de $n$ entradas), $\bigoplus$ (puerta XOR de $n$
  entradas) y $\bigodot$ (puerta XNOR de $n$ entradas).

Esta notación algebraica clásica resulta mucho más ágil y familiar para
la manipulación y simplificación de funciones lógicas complejas. Así,
teoremas como el de la distributividad se reescriben de forma natural
como $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$, y las leyes de De
Morgan cobran su célebre forma visual:
$$\overline{a + b} = \overline{a} \cdot \overline{b} \qquad \text{y} \qquad \overline{a \cdot b} = \overline{a} + \overline{b}$$
De igual modo, la estructura de las operaciones derivadas queda plasmada
directamente en ecuaciones como
$a \oplus b = (a \cdot \overline{b}) + (\overline{a} \cdot b)$.

Además, gracias a nuestra previa instanciación en el álgebra bivaluada
($|B|=2$), sabemos que las tablas de operación algebraicas que hemos
deducido analíticamente se corresponden de manera idéntica y biunívoca
con las **tablas de verdad** de las puertas lógicas físicas.

Con estos fundamentos matemáticos sólidamente establecidos, la
transición hacia el diseño, análisis y simplificación de circuitos
digitales queda completamente justificada y carente de ambigüedades.
