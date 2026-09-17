# Introducción

El álgebra de Boole, originalmente introducida por George Boole en su
obra de 1854 *The Laws of Thought*, fue posteriormente axiomatizada de
forma rigurosa. En 1904, el matemático estadounidense Edward Vermilye
Huntington presentó un conjunto de postulados independientes que definen
formalmente una estructura de álgebra de Boole.

Para evitar cualquier confusión conceptual con la aritmética
tradicional, en esta fase inicial emplearemos la signatura propia de la
teoría de retículos, utilizando los símbolos $\vee$ (supremo o join) y
$\wedge$ (ínfimo o meet), junto a los elementos constantes $\bot$
(mínimo) y $\top$ (máximo). El complemento se denotará con el símbolo
clásico de la negación lógica $\neg$. Más adelante, y por conveniencia
práctica, transitaremos hacia la notación clásica de sistemas digitales
($+$, $\cdot$, $0$, $1$).

## Nomenclatura y Convenios

Antes de comenzar con el desarrollo formal del álgebra, estableceremos
una serie de convenios notacionales que utilizaremos a lo largo de este
texto:

- $0 \notin \mathbb{N}$. Ante la definición de los números naturales,
  nosotros adoptamos este convenio excluyendo al cero.

- $\widetilde{\mathbb{N}} \triangleq \left( \mathbb{N} \cup \{0\} \right)$.
  Representará el conjunto de los naturales extendidos que incluye el
  cero.

- Definición recurrente de los conjuntos
  $\lbrack 0,1 \rbrack_{\mathbb{Q}}$ y
  $\lbrack 0,1 \rbrack_{\mathbb{Q}}^n$, donde $n \in \mathbb{N}$ y
  $n > 1$:

  - $\lbrack 0,1 \rbrack_{\mathbb{Q}} := \lbrack 0,1 \rbrack \cap \mathbb{Q}$

  - $\lbrack 0,1 \rbrack_{\mathbb{Q}}^1 := \lbrack 0,1 \rbrack_{\mathbb{Q}}$

  - $\lbrack 0,1 \rbrack_{\mathbb{Q}}^n := \lbrack 0,1 \rbrack_{\mathbb{Q}}^{n-1} \times \lbrack 0,1 \rbrack_{\mathbb{Q}}^1$

- Por lo general, los elementos de un conjunto se representarán por
  letras minúsculas (alfabetos griego y latino) con o sin subíndices
  (ejemplo: $a_3$, $b$, $\gamma_{1547}$, $\delta$) y dígitos decimales
  ($\{0, 1, \ldots, 9\}$). Por el contrario, los conjuntos se
  representarán por letras mayúsculas (alfabeto griego y latino),
  igualmente con o sin subíndices. Este convenio será válido a excepción
  de que se exprese de forma explícita otro nombre para elementos o
  conjuntos.

- En ocasiones aseguraremos que existe un conjunto asociado a un
  elemento: en general serán letras mayúsculas, como corresponde a un
  conjunto, pero con un subíndice escrito exactamente como el elemento
  asociado.

- Cuando expresemos $a \ast B$, es decir, el elemento $a$ operado con un
  conjunto $B$ mediante una operación binaria $\ast$, nos estaremos
  refiriendo al conjunto formado por operar $a$ con todos los elementos
  de $B$: $a \ast B = \{ a \ast b \mid b \in B \}$. De igual manera, la
  operación entre dos conjuntos se entenderá como:
  $A \ast B = \{ a \ast b \mid a \in A \land b \in B \}$.

- El universo de discurso principal será un conjunto $\mathbb{B}$. Para
  aligerar la notación, evitaremos en lo posible el uso explícito del
  cuantificador universal ($\forall$). Cuando aparezca una variable,
  conjunto o constante sin cuantificar, asumiremos implícitamente una
  cuantificación universal sobre los elementos de $\mathbb{B}$. Si la
  cuantificación debiera aplicarse a un subconjunto particular, se
  omitirá el símbolo $\forall$ pero se precederá la proposición con la
  relación de pertenencia.

- De igual forma, cuando una variable asuma como valor un conjunto, se
  entenderá implícitamente que pertenece al conjunto partes
  $\wp(\mathbb{B}) \smallsetminus \{ \varnothing \}$.

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
$\bot \in \mathbb{B}$ y $\top \in \mathbb{B}$. En principio, no asumimos
nada sobre la igualdad o desigualdad de estas constantes.
:::

Además, vamos a definir dos operaciones binarias internas que
denotaremos por $\vee$ y $\wedge$. Estas deben satisfacer rigurosamente
la definición de función:

::: preaxioma
Operación Binaria Interna $\vee$ - OpBinInt$_\vee$opbinint_vee
$\vee : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una operación
binaria interna.
:::

::: preaxioma
Operación Binaria Interna $\wedge$ - OpBinInt$_\wedge$opbinint_wedge
$\wedge : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una operación
binaria interna.
:::

Para poder usar estos conceptos con mayor seguridad y flexibilidad en
las futuras demostraciones formales, asignaremos nombres cortos a las
condiciones de existencia y unicidad de la imagen para estas
operaciones:

::: preaxioma
Existencia $\vee$ - Existencia$_\vee$exist_vee Para todo par existe
imagen en $\mathbb{B}$. Es decir,
$\forall \langle a,b \rangle \in \mathbb{B} \times \mathbb{B}$,
$\exists c \in \mathbb{B}$ tal que $a \vee b = c$.
:::

::: preaxioma
Existencia $\wedge$ - Existencia$_\wedge$exist_wedge Análogamente,
$\forall \langle a,b \rangle \in \mathbb{B} \times \mathbb{B}$,
$\exists d \in \mathbb{B}$ tal que $a \wedge b = d$.
:::

::: preaxioma
Unicidad $\vee$ - Unicidad$_\vee$unic_vee Para un par solo existe una
imagen. Esto es, si $a \vee b = c$ y $a \vee b = d$, entonces $c = d$.
:::

::: preaxioma
Unicidad $\wedge$ - Unicidad$_\wedge$unic_wedge De igual forma para el
ínfimo, si $a \wedge b = c$ y $a \wedge b = d$, entonces $c = d$.
:::

## Los Postulados de Huntington (1904)

Sobre el sistema $(\mathbb{B}, \vee, \wedge, \bot, \top)$ que cumple los
pre-axiomas anteriores, diremos que forma un álgebra de Boole si
satisface los siguientes postulados:

::: postulado
Elemento neutro $\vee$ - $ElemNeu_\vee$neutro_vee Todo elemento operado
mediante $\vee$ con el mínimo $\bot$ da como resultado el mismo
elemento; es decir, $\bot$ no altera el valor original:
$$\forall a \in \mathbb{B}, \quad a \vee \bot = a$$
:::

::: postulado
Elemento neutro $\wedge$ - $ElemNeu_\wedge$neutro_wedge Todo elemento
operado mediante $\wedge$ con el máximo $\top$ da como resultado el
mismo elemento, quedando inalterado:
$$\forall a \in \mathbb{B}, \quad a \wedge \top = a$$
:::

::: postulado
Conmutatividad $\vee$ - $Comm_\vee$conmut_vee El orden de los operandos
al aplicar la operación $\vee$ es indiferente, obteniéndose exactamente
el mismo resultado:
$$\forall a, b \in \mathbb{B}, \quad a \vee b = b \vee a$$
:::

::: postulado
Conmutatividad $\wedge$ - $Comm_\wedge$conmut_wedge De la misma forma,
el orden de los operandos al aplicar la operación $\wedge$ tampoco
altera el resultado final:
$$\forall a, b \in \mathbb{B}, \quad a \wedge b = b \wedge a$$
:::

::: postulado
Distributividad $\vee$ sobre $\wedge$ - $Dist_\vee$distrib_vee_wedge La
operación $\vee$ se distribuye sobre la operación $\wedge$. Operar un
elemento con el resultado de un $\wedge$ equivale a operar con $\vee$
cada componente individualmente y luego aplicar $\wedge$:
$$\forall a, b, c \in \mathbb{B}, \quad a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$$
:::

::: postulado
Distributividad $\wedge$ sobre $\vee$ - $Dist_\wedge$distrib_wedge_vee
De manera equivalente, el ínfimo ($\wedge$) se reparte de forma
distributiva entre los componentes de un supremo ($\vee$):
$$\forall a, b, c \in \mathbb{B}, \quad a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$$
:::

::: postulado
Complementario - $Comp_\vee, Comp_\wedge$comp Todo elemento del conjunto
posee al menos un \"complemento\" (o elemento opuesto). Al operarlo con
su complemento mediante $\vee$ siempre alcanzamos el máximo $\top$, y
mediante $\wedge$ siempre caemos al mínimo $\bot$: $$\begin{align*}
\forall a \in \mathbb{B}, \exists b \in \mathbb{B} \quad : \quad a \vee b &= \top \quad (Comp_\vee) \\
a \wedge b &= \bot \quad (Comp_\wedge)
\end{align*}$$
:::

*Nota: A diferencia de algunas formulaciones clásicas que imponen un
axioma de cardinalidad ($\bot \neq \top$) para evitar el álgebra
trivial, en este desarrollo permitiremos la existencia del álgebra
trivial.*

# Independencia de los Axiomas de Huntington de 1904

Para esto demostrar que los axiomas antes dados son independientes entre
sí, primero daremos un modelo consistente y sencillo, en el que haremos
variaciones y obtendremos modelos (ejemplos) de sistemas que cumplan
todos los axiomas excepto uno de ellos. Si se logra quedará claro que no
podemos deducir el axioma fallido del resto de axiomas que sí que se
cumplen: el axioma fallido es lógicamente independiente del resto de
axiomas. Esto es fácil de conseguir, comenzando con modelos de álgebras
con base en un conjunto de dos elementos ${\mathbb{B}}_2 = \{0,1\}$. En
esto copiamos los modelos dados por Huntington en su artículo de 1904.

### Modelo mínimo de álgebra de Boole.

Definimos: $$\begin{flalign}
{\mathbb{B}}_2 &\triangleq\{0,1\} = \{0\} \cup \{1\} \\
0 &\triangleq\emptyset \\
1 &\triangleq\{\emptyset\} \cup \{ \{ \emptyset \} \} = \{ \emptyset,
\{ \emptyset \} \} \\
0 &\;\in\; 1 \\
0 &\;\subsetneq\; 1 \\
0 &\;\neq\; 1 \\
\end{flalign}$$ $$\begin{flalign}
\textsf{\textbf{s}} &:  {\mathbb{B}}_2 \times {\mathbb{B}}_2{\qquad}\longrightarrow{\qquad} {\mathbb{B}}_2\\
\end{flalign}$$ $$\begin{flalign}
\textsf{\textbf{s}} &:: \left({0,0}\right) {\qquad} \mapsto {\qquad} 0\\
\textsf{\textbf{s}} &:: \left({0,1}\right) {\qquad} \mapsto {\qquad} 1\\
\textsf{\textbf{s}} &:: \left({1,0}\right) {\qquad} \mapsto {\qquad} 1\\
\textsf{\textbf{s}} &:: \left({1,1}\right) {\qquad} \mapsto {\qquad} 1
\end{flalign}$$ $$\begin{flalign}
\textsf{\textbf{p}} &:  {\mathbb{B}}_2 \times {\mathbb{B}}_2{\qquad}\longrightarrow{\qquad} {\mathbb{B}}_2\\
\end{flalign}$$ $$\begin{flalign}
\textsf{\textbf{p}} &:: \left({0,0}\right) {\qquad} \mapsto {\qquad} 0\\
\textsf{\textbf{p}} &:: \left({0,1}\right) {\qquad} \mapsto {\qquad} 0\\
\textsf{\textbf{p}} &:: \left({1,0}\right) {\qquad} \mapsto {\qquad} 0\\
\textsf{\textbf{p}} &:: \left({1,1}\right) {\qquad} \mapsto {\qquad} 1
\end{flalign}$$ $$\begin{flalign}
\textsf{\textbf{c}} &:  {\mathbb{B}}_2 {\qquad} \longrightarrow{\qquad} {\mathbb{B}}_2
\end{flalign}$$ $$\begin{flalign}
\textsf{\textbf{c}} &:: 0 {\qquad} \mapsto {\qquad} 1\\
\textsf{\textbf{c}} &:: 1 {\qquad} \mapsto {\qquad} 0
\end{flalign}$$

El conjunto ${\mathbb{B}}_2$ es conjunto en **ZFS**, desde el momento
que la el axioma de unión nos asegura que ${\mathbb{B}}_2$ es conjunto
unión de dos conjuntos de un solo elemento,
${\mathbb{B}}_2 \triangleq{ \{0\} } \cup {
\{1\} }$. Los elementos $0 \triangleq\emptyset$ y $1 \triangleq\{
\emptyset, \{ \emptyset \} \}$. De nuevo para definir $1$ como conjunto
necesitamos el axioma de unión (o de pares no ordenados) de **ZFS**,
siendo $1 \triangleq\{0\}\cup\{\{0\}\}$. Podemos ver que $0 \cap 1 =
\emptyset$ por lo que $0 \neq 1$. También $0 \in 1$. Todo este párrafo
constituye la satisfacción de los requerimientos
[\[axm:H0\]](#axm:H0){reference-type="ref" reference="axm:H0"}.

Tal como hemos definido nuestro modelo de álgebra de Boole, lo primero
que queda claro es que $\vee$ y $\wedge$ son funciones binarias bien
definidas, y esta última es además biyectiva. Luego los axiomas
[\[axm:H1s\]](#axm:H1s){reference-type="ref" reference="axm:H1s"} y
[\[axm:H1p\]](#axm:H1p){reference-type="ref" reference="axm:H1p"} quedan
satisfechos.

Los axiomas [\[axm:H2s\]](#axm:H2s){reference-type="ref"
reference="axm:H2s"} y [\[axm:H2p\]](#axm:H2p){reference-type="ref"
reference="axm:H2p"} (existencia del elemento neutro) quedan
directamente satisfechos por simple inspección de las tablas.

Para el axioma [\[axm:H2s\]](#axm:H2s){reference-type="ref"
reference="axm:H2s"} observamos que $0 \vee 0 = 0$ y
$0 \vee 1 = 1 \vee 0 = 1$ nos muestra el elemento neutro de la suma, el
elemento $0$.

Para el axioma [\[axm:H2p\]](#axm:H2p){reference-type="ref"
reference="axm:H2p"} observamos que $1 \wedge 0 =
0 \wedge 1 = 0$ y $1 \wedge 1 = 1$ nos muestra el elemento neutro del
producto, el elemento $1$.

Para los axiomas de conmutatividad solo hay que observar en la
definición de las funciones binarias
$\vee,\wedge: \mathbb{B}_2 \times \mathbb{B}_2
\longrightarrow\mathbb{B}_2$, que $0 \vee 1 = 1 \vee 0 = 1$ y se cumple
[\[axm:H3s\]](#axm:H3s){reference-type="ref" reference="axm:H3s"}, que
$0 \wedge 1 = 1 \wedge 0 = 0$ y se cumple
[\[axm:H3p\]](#axm:H3p){reference-type="ref" reference="axm:H3p"}.

Para las distribuciones de una operación interna sobre otra elegiré
construir unas tablas que muestren la igualdades necesarias.

Primero veremos la distribución de la suma sobre el producto, o, lo que
es lo mismo, su inversa, sacar factor común.

Lo haremos rellenando y comparando la siguiente tabla de verdad.

El método de relleno es fácil. Primero rellenamos las tres primeras
columnas, corresponden a las variables independientes, que al ser tres
con dos valores posibles en cada ocasión, son un total de ocho
combinaciones distintas. Esas columnas están marcadas con $1$ en la
última fila (fila que se ve separada). A continuación rellenamos las
columnas correspondientes a una operación binaria interna de dos
variables independientes ya rellenas. Para rellenarlas, solo tenemos que
buscar los valores en las tablas dadas para las operaciones internas en
ka definición de este álgebra de Boole. Estas están marcadas con un $2$
en la última línea, la línea separada. Corresponden con la cuarta
columna, la suma $\textsf{b}  \vee 
\textsf{c}$, y con las columnas siete y ocho: la ocho es un producto
$\textsf{a} \wedge \textsf{c}$ y la siete otro
$\textsf{a}  \wedge  \textsf{b}$. Las columnas centrales, la cinco y la
seis corresponden a todas las valoraciones posibles (y en el mismo orden
de valor de las variables independientes) de las dos expresiones que
queremos comparar, las afirmadas por el postulado
[\[axm:H4s\]](#axm:H4s){reference-type="ref" reference="axm:H4s"}.
Podemos ver que ambas columnas son idénticas, luego se cumple el citado
postulado.

$$\begin{flalign}
\begin{matrix}
\hline
\textsf{a} & \textsf{b} & \textsf{c} &
\textsf{b} \vee \textsf{c} &
\textsf{a} \wedge \textsf{b} \vee \textsf{c} &
\textsf{a} \wedge \textsf{b} \vee \textsf{a} \wedge \textsf{c}
&
{\textsf{a} \wedge \textsf{b}}
&
{\textsf{a} \wedge \textsf{c}}
\\
\hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 1 & 1 & 1 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 1 & 1 & 1 & 0 & 1 \\
1 & 1 & 0 & 1 & 1 & 1 & 1 & 0 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\hline
1 & 1 & 1 & 2 & 3 & 3 & 2 & 2 \\ 
\hline
\end{matrix}
\end{flalign}$$

Por último veremos la distribución del producto sobre la suma, o, lo que
es lo mismo, su inversa, sacar sumando común. El método es en todo
idéntico al seguido para la otra distributiva.

$$\begin{flalign}
\begin{matrix}
\hline
\textsf{a} & \textsf{b} & \textsf{c} &
\textsf{b} \wedge \textsf{c} &
\textsf{a} \vee \textsf{b} \wedge \textsf{c} &
\textsf{a} \vee \textsf{b} \wedge \textsf{a} \vee \textsf{c}
&
{\textsf{a} \vee \textsf{b}}
&
{\textsf{a} \vee \textsf{c}}
\\
\hline
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \\
1 & 0 & 1 & 0 & 1 & 1 & 1 & 1 \\
1 & 1 & 0 & 0 & 1 & 1 & 1 & 1 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\hline
1 & 1 & 1 & 2 & 3 & 3 & 2 & 2 \\ 
\hline
\end{matrix}
\end{flalign}$$

Para el axioma [\[axm:H5\]](#axm:H5){reference-type="ref"
reference="axm:H5"} observamos que $\neg 0 = 1$ y $\neg 1 = 0$ y por
inspección en las tablas vemos que $0 \vee \neg 0 = 0 \vee 1 = 1$ y que
$0 \wedge \neg 0 = 0 \wedge 1 = 0$ cumpliendo para el elemento $0$ se
cumple que $\exists 1 = \neg 0 \in \mathbb{B}_2$
$1 \vee \neg 1 = 1 \vee 0 = 1$, que coincide con la ecuación segunda
(ecuación: 2.15) de [\[eqn:H5\]](#eqn:H5){reference-type="ref"
reference="eqn:H5"} y $1 \wedge \neg 1=1 \wedge 0 = 0$ que coincide con
la tercera ecuación (ecuación: 2.16) de
[\[eqn:H5\]](#eqn:H5){reference-type="ref" reference="eqn:H5"}, e
igualmente para el elemento $1$, $\exists 0 = \neg 1 \in \mathbb{B}_2$
$0 \vee \neg 0 = 0 \vee 1 = 1$ (ecuación: 2.15) y
$0 \wedge \neg 0 =0 \wedge 1 = 0$ (ecuación: 2.16) de
[\[eqn:H5\]](#eqn:H5){reference-type="ref" reference="eqn:H5"}.

Como las ecuaciones 2.15 y 2.16 se cumplen para $0$ y $1$, esto es,
$\forall x \in \mathbb{B}_2$ como se requiere en la ecuación 2.14, queda
satisfecho el postulado [\[axm:H5\]](#axm:H5){reference-type="ref"
reference="axm:H5"}.

### Independencia de la suma está siempre definida.

Modelo en el que solo falla [\[axm:H1s\]](#axm:H1s){reference-type="ref"
reference="axm:H1s"}, esto es, que la operación suma no es operación
interna: no es función, pero en el sentido que $1 + 1 \notin
\mathbb{B}$.

$$\begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {x} & \big{\vert} \\
        \hline
    \end{matrix}
    \qquad\qquad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}$$

Al ser $1 + 1 = x$, dónde $x$ es ningún elemento de $\mathbb{B}$, o
dicho de otro modo, $1 + 1 \notin \mathbb{B}$, vemos que sigue
existiendo el elemento neutro de la suma, $0$, que la suma sigue siendo
conmutativa y las distributivas siguen valiendo mientras la suma tenga
sentido (mientras no aparezca $x$). El complementario de $0$ es $1$ y el
de $1$ es $0$.

### Independencia de la unicidad de la definición de la suma.

Modelo en el que no se cumple
[\[axm:H1s\]](#axm:H1s){reference-type="ref" reference="axm:H1s"}, en el
sentido que $1 + 1
\mapsto 1$ y $1 + 1 \mapsto 0$.

$$\begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {x=0 \vee x=1} & \big{\vert} \\
        \hline
    \end{matrix}
    \qquad\qquad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}$$

Exactamente igual que en la versión anterior, se cumplen todos los demás
postulados, sea cual sea el valor tomado para $1 + 1$.

### Independencia de el producto está siempre definido.

Modelo en el que solo falla [\[axm:H1p\]](#axm:H1p){reference-type="ref"
reference="axm:H1p"}, esto es, que la operación producto no es operación
interna: no es función. Este es el caso en que
$0 \cdot 0 \notin \mathbb{B}$. Ponemos en ese caso $0 \cdot 0 = x$ pero
igualmente podríamos haber dejado en blanco ese lugar.

$$\begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {x} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}$$

Como es fácil ver, existe elemento neutro tanto de la suma como del
producto. Ambas operaciones son conmutativas y se dan las dos
propiedades de distribución, siempre que tenga sentido el producto, esto
es, no aparezca $0 \cdot 0$. El complementario del $0$ es
$\overline 0 = 1$ y el del $1$ es $\overline 1 = 0$.

### Independencia de la unicidad de la definición del producto.

Modelo en el que solo falla [\[axm:H1s\]](#axm:H1s){reference-type="ref"
reference="axm:H1s"}, esto es, en el sentido que $0
\cdot 0 \mapsto 0$ y también $0 \cdot 0 \mapsto 1$.

$$\begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {x=0 \vee x=1} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}$$

### Independencia de la existencia de elemento neutro de la suma.

Modelo en el que solo falla [\[axm:H2s\]](#axm:H2s){reference-type="ref"
reference="axm:H2s"}, esto es, la existencia de elemento neutro en la
operación binaria interna suma.

$$\begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}             & \big{\vert} & {0} & {0} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}$$

Primero, está claro que las operaciones internas están bien construidas
en cuanto a que son funciones.

Queda claro que no hay elemento neutro de la suma pues $\forall xy \in
\mathbb{B}\quad x + y = 0$.

Segundo, existe el elemento neutro del producto: $0 \cdot 1 = 1 \cdot 0
= 0$ y $1 \cdot 1 = 1$. Luego se cumple
[\[aciom:H2p\]](#aciom:H2p){reference-type="ref" reference="aciom:H2p"}.

La conmutatividad se hace patente al ver las diagonales inversas de las
tablas de operación, que muestran un único valor. $0 + 1 = 1 + 0 = 0$ y
$0 \cdot 1 = 1 \cdot 0 = 0$. Se cumplen
[\[axm:H3s\]](#axm:H3s){reference-type="ref" reference="axm:H3s"} y
[\[axm:H3p\]](#axm:H3p){reference-type="ref" reference="axm:H3p"}.

En cuanto a la distribución del producto sobre la suma, veamos si
podemos comprobarla de forma sencilla:
$a \cdot ( b + c ) = (a \cdot b) + (a \cdot
c)$. Sabemos que $b + c = 0$ siempre, y que, pongamos que $a \cdot b = x
\in \mathbb{B}$ y que $a \cdot c = y \in \mathbb{B}$. Ahora bien
$x + y = 0$. Así que todo lo que tenemos que probar es que
$a \cdot 0 = 0$, pero esto es claro en la table del producto. Luego se
cumple [\[axm:H4s\]](#axm:H4s){reference-type="ref"
reference="axm:H4s"}.

Ahora la distribución de la suma sobre el producto. $a + ( b \cdot c )
= (a + b) \cdot (a + c)$. Sabemos que $a + (b \cdot c) = 0$ siempre, y
que, pongamos que $a + b = 0$ y que $a + c = 0$. Ahora bien $0 \cdot
0 = 0$. Luego se cumple [\[axm:H4p\]](#axm:H4p){reference-type="ref"
reference="axm:H4p"}.

Nos queda encontrar un complemento para el $0$. Pero encontrar el
complemento solo tiene sentido si existen los dos elementos neutros,
pero en este caso no existe el neutro de la suma: no tiene sentido
buscar el complementario.

### Independencia de la existencia de elemento neutro del producto.

Exponemos un modelo en el que solo falla
[\[axm:H2p\]](#axm:H2p){reference-type="ref" reference="axm:H2p"}, esto
es, la existencia de elemento neutro en la operación binaria interna
producto.

$$\begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {1} & {1} & \big{\vert} \\
        {1}                   & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}$$

Este modelo es completamente simétrico al anterior, por lo que no nos
hará falta demostrar que se dan el resto de postulados. Solo hay que
seguir el esquema de la sub-sección anterior.

### Independencia de la conmutatividad de la suma.

Modelo en que la conmutatividad de la suma
[\[axm:H3s\]](#axm:H3s){reference-type="ref" reference="axm:H3s"} no se
dá, pero si que se dan el resto de postulados.

$$\begin{equation}
    \begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
\end{equation}$$

Que la suma y el producto están bien definidos como función es
inmediato.

Podemos comprobar que tanto $\forall x \; x + 0 = x$ como que $\forall
x \; x + 1 = x$. Esto quiere decir que la suma tiene dos neutros, el $0$
y el $1$. Esto tendrá repercusiones sobre el elemento complementario.
Podemos ver por otra parte que $1 + 0 \neq 0 + 1$, por lo que
efectivamente la suma no es conmutativa. Para el producto todo es
idéntico, tiene elemento neutro general y único $0$ y
$1\cdot 0 = 0\cdot 1$ por lo que el producto es conmutativo.

Por otro lado, vemos que el complementario de $0$ es $1$, $0 + 1 =
1$ -es neutro del producto- y $0 * 1 = 0$ -es neutro de la suma-. Para
ver que $1$ tiene complementario, hay que ir con más cuidado,
$1 + 1 = 1$ - $1$ es neutro del producto - y $1 * 1 = 1$ - $1$ es
también neutro del producto -. Luego existe complementario de $1$ y es
$1$.

Vamos ahora con las distribuciones:

Nos preguntamos si se cumple $x \cdot ( y + z ) = ( x \cdot y ) + ( x
\cdot z )$ en el actual modelo. Si $x = 0$ entonces $0 \cdot (x + y) =
0$ y la parte derecha de la igualdad se resuelve en $( 0 \cdot y ) + ( 0
\cdot z )$ pero como $0 \cdot x = 0$ obtenemos que la distribución
[\[axm:H4s\]](#axm:H4s){reference-type="ref" reference="axm:H4s"} será
verdad para $x = 0$ si $0 = 0 + 0$, cosa que es cierta. Si $x = 1$, la
igualdad a verificar quedaría $1 \cdot ( y + z )
= ( 1 \cdot y ) + ( 1 \cdot z )$ y por
[\[axm:H2p\]](#axm:H2p){reference-type="ref" reference="axm:H2p"} queda
$y + z  =  y
+ z$ que no es más que la identidad lógica de la igualdad. Se satisface
[\[axm:H4s\]](#axm:H4s){reference-type="ref" reference="axm:H4s"}.

Nos preguntamos por la satisfacción de
[\[axm:H4p\]](#axm:H4p){reference-type="ref" reference="axm:H4p"}
$x + ( y \cdot z
) = ( x + y ) \cdot ( x + z )$ en el actual modelo. Procedemos como en
el párrafo anterior, por casos. Si $x = 0$ entonces
$x + ( y \cdot z ) = ( x
+ y ) \cdot ( x + z )$ $\Longrightarrow$ $0 + ( y \cdot z ) = ( 0 + y )
\cdot ( 0 + z )$ $\Longrightarrow$ $0 = 0 \cdot 0$ lo que es cierto.
Para el caso $x = 1$, obtenemos $x + ( y \cdot z ) = ( x + y ) \cdot ( x
+ z )$ $\Longrightarrow$ $1 + ( y \cdot z ) = ( 1 + y ) \cdot ( 1 + z
)$ $\Longrightarrow$ $1 = 1 \cdot 1$. Por lo tanto también se verifica
[\[axm:H4p\]](#axm:H4p){reference-type="ref" reference="axm:H4p"}.

Queda comprobado que la conmutatividad de la suma
[\[axm:H3s\]](#axm:H3s){reference-type="ref" reference="axm:H3s"} es
independiente del resto de postulados.

### Independencia de la conmutatividad del producto.

Modelo en que la conmutatividad del producto
[\[axm:H3p\]](#axm:H3p){reference-type="ref" reference="axm:H3p"} no se
da, pero, si se satisfacen el resto de postulados.

$$\begin{equation}
    \begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
\end{equation}$$

El modelo es totalmente simétrico al anterior por lo que se puede
comprobar todo siguiendo los mismos pasos que en la sub-sección
anterior.

### Independencia de la distribución de la suma sobre el producto.

El postulado del título no se cumple. Existen valores del modelo
$\exists x \in \mathbb{B}$ que no cumplen
[\[axm:H4p\]](#axm:H4p){reference-type="ref" reference="axm:H4p"},
$x + ( y \cdot z )
\neq ( x + y ) \cdot (x + z)$.

$$\begin{equation}
    \begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {0} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
\end{equation}$$

Este modelo es virtualmente idéntico al cuerpo sobre $\mathbb{Z}$ de
restos módulo 2, $\mathbb{Z}/{\mod2}$. Ese es el cambio que se da en la
suma. Ahora $1
+ 1 = 0$.

Se dan por lo tanto todos los teoremas conocidos incluida la
distribución [\[axm:H4s\]](#axm:H4s){reference-type="ref"
reference="axm:H4s"} e incluso sabemos que las operaciones son
asociativas.

Pero en aritmética no se da la dualidad que buscamos y la distribución
del producto sobre la suma no es una verdad.

Solo nos queda ver si cumple la existencia de elemento complementario
que se encuentra visualmente por inspección de las tablas:
$\overline{1} = 0$ y $\overline{0} = 1$.

Nos queda verificar que efectivamente no se cumple la distribución de la
suma sobre el producto (que intuitivamente vemos). Encontramos un caso,
$1 + ( y \cdot z ) \neq ( 1 + y ) \cdot ( 1 + z )$. Lo vemos a
continuación.

$$\begin{flalign}
  x = 1 &{} \\
  1 + ( y \cdot z ) &= ( 1 + y ) \cdot ( 1 + z ) \\
  \overline{y \cdot z} &= \overline{y} \cdot \overline{z} \\
  y = 0 &{} \\
  \overline{0 \cdot z} &= \overline{0} \cdot \overline{z} \\
  \overline{0} &= 1 \cdot \overline{z} \\
  1 &= \overline{z} \\
  z &= 0\\
  x=1 \wedge y=0 \wedge z=1 &\Longrightarrow \neg\ref{axm:H4p}
\end{flalign}$$

De dónde efectivamente este modelo no distribuye la suma sobre un
producto. Y la independencia de
[\[axm:H4p\]](#axm:H4p){reference-type="ref" reference="axm:H4p"} queda
probada.

### Independencia de la distribución del producto sobre la suma.

$$\begin{equation}
    \begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {1} & {0} & \big{\vert} \\
        {1}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
\end{equation}$$

Completamente simétrico al caso anterior.

### Independencia de la existencia del elemento complementario.

Por último presentamos un modelo que no cumple la existencia del
complementario y si satisface el resto de postulados.

$$\begin{equation}
    \begin{matrix}
        {\cdot + \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}             & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}             & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
    \quad
    \begin{matrix}
        {\cdot * \cdot} & \big{\vert} & {0} & {1} & \big{\vert} \\
        \hline
        {0}                   & \big{\vert} & {0} & {1} & \big{\vert} \\
        {1}                   & \big{\vert} & {1} & {1} & \big{\vert} \\
        \hline
    \end{matrix}
\end{equation}$$

Como podemos ver en este modelo la suma y el producto son idénticos, por
lo que el $0$ es el único neutro, tanto de la suma como del producto. La
conmutatividad es evidente a primera vista.

Veamos la distribución del producto respecto de la suma. Com la suma y
el producto son idénticos, bastará con probar este caso únicamente.

$$\begin{equation}
x \cdot (y + z) = x + ( y + z ) = ( x + x ) + ( y + z ) = ( x + y ) + ( x + z
) = ( x + y ) \cdot ( x + z )
\end{equation}$$

Solo queda probar que $x = x + x$ (que se hace por simple inspección
visual de las tablas) y la propiedad asociativa para este modelo, que
tendremos que probar. Lo haremos mediante una tabla.

$$\begin{equation}
  \begin{matrix}
  \hline
  \mathsf{a} & \mathsf{b} & \mathsf{c} & \mathsf{b}\cdot\mathsf{c} &
  \mathsf{a}\cdot\left( \mathsf{b} \cdot \mathsf{c} \right) &
  \left(\mathsf{a}\cdot \mathsf{b}\right) \cdot \mathsf{c} &
  \mathsf{a}\cdot\mathsf{b}\\
  \hline
%%a   b   c   bc a(bc)(ab)c ab
  0 & 0 & 0 & 0 & 0    & 0 & 0 \\
  0 & 0 & 1 & 1 & 1    & 1 & 0 \\
  0 & 1 & 0 & 1 & 1    & 1 & 1 \\
  0 & 1 & 1 & 1 & 1    & 1 & 1 \\
  1 & 0 & 0 & 0 & 1    & 1 & 1 \\
  1 & 0 & 1 & 1 & 1    & 1 & 1 \\
  1 & 1 & 0 & 1 & 1    & 1 & 1 \\
  1 & 1 & 1 & 1 & 1    & 1 & 1 \\
  \hline
  1 & 1 & 1 & 2 & 3    & 3 & 2 \\
  \hline
  \end{matrix}
\end{equation}$$

# El Principio de Dualidad

Si observamos los postulados de Huntington, notaremos una perfecta
simetría entre las operaciones $\vee$ y $\wedge$, y entre las constantes
$\bot$ y $\top$. Si en cualquier postulado intercambiamos $\vee$ por
$\wedge$ y $\bot$ por $\top$, obtenemos otro postulado válido del
sistema.

Este rasgo estructural da lugar al **Principio de Dualidad**: toda
proposición o teorema deducido a partir de estos axiomas tiene un
*teorema dual* que también es válido. La demostración de un teorema dual
se construye manipulando la prueba original y aplicando sistemáticamente
el intercambio de operaciones ($\vee \leftrightarrow \wedge$) y
constantes ($\bot \leftrightarrow \top$). En las siguientes pruebas no
evitaremos repetir las versiones duales; al contrario, haremos hincapié
en cómo se manipula la prueba de uno para obtener la del otro.

## Teoremas Principales Derivados

::: teorema
Unicidad de los elementos neutros - $Unic_e, Unic_u$unicidad_neutros Los
elementos neutros descritos en los postulados son únicos. No existe
ningún otro elemento en el conjunto que se comporte como el mínimo
$\bot$ para la operación $\vee$, ni ningún otro que actúe como el máximo
$\top$ para la operación $\wedge$: $$\begin{align*}
    \exists! e \in \mathbb{B}, \forall a \in \mathbb{B}, a \vee e &= a \implies e = \bot \quad (Unic_e) \\
    \exists! u \in \mathbb{B}, \forall a \in \mathbb{B}, a \wedge u &= a \implies u = \top \quad (Unic_u)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $Unic_e$.* Sea $e \in \mathbb{B}$ tal que
$\forall a \in \mathbb{B}, a \vee e = a$. Tomando $a = \bot$:
$$\begin{align*}
    e &= e \vee \bot & (ElemNeu_\vee) \\
      &= \bot \vee e & (Comm_\vee) \\
      &= \bot & (\text{Hipótesis sobre } e)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Unic_u$ (Dual).* Para obtener la prueba dual,
intercambiamos $\vee$ por $\wedge$ y $\bot$ por $\top$. Sea
$u \in \mathbb{B}$ tal que $\forall a \in \mathbb{B}, a \wedge u = a$.
Tomando $a = \top$: $$\begin{align*}
    u &= u \wedge \top & (ElemNeu_\wedge) \\
      &= \top \wedge u & (Comm_\wedge) \\
      &= \top & (\text{Hipótesis sobre } u)
\end{align*}$$ ◻
:::

::: teorema
Idempotencia - $Idemp_\vee, Idemp_\wedge$idempotencia Operar un elemento
consigo mismo, independientemente de si usamos $\vee$ o $\wedge$, no
altera su valor. El elemento se mantiene idéntico a sí mismo:
$$\begin{align*}
    \forall a \in \mathbb{B}, \quad a \vee a &= a \quad (Idemp_\vee) \\
    \forall a \in \mathbb{B}, \quad a \wedge a &= a \quad (Idemp_\wedge)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $Idemp_\vee$.* $$\begin{align*}
    a &= a \vee \bot & (ElemNeu_\vee) \\
      &= a \vee (a \wedge \neg a) & (Comp_\wedge) \\
      &= (a \vee a) \wedge (a \vee \neg a) & (Dist_\vee) \\
      &= (a \vee a) \wedge \top & (Comp_\vee) \\
      &= \top \wedge (a \vee a) & (Comm_\wedge) \\
      &= a \vee a & (ElemNeu_\wedge)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Idemp_\wedge$ (Dual).* Intercambiando los operadores y
constantes de la prueba anterior paso a paso: $$\begin{align*}
    a &= a \wedge \top & (ElemNeu_\wedge) \\
      &= a \wedge (a \vee \neg a) & (Comp_\vee) \\
      &= (a \wedge a) \vee (a \wedge \neg a) & (Dist_\wedge) \\
      &= (a \wedge a) \vee \bot & (Comp_\wedge) \\
      &= \bot \vee (a \wedge a) & (Comm_\vee) \\
      &= a \wedge a & (ElemNeu_\vee)
\end{align*}$$ ◻
:::

::: teorema
Elementos absorbentes - $Abs_{\bot}, Abs_{\top}$absorbentes Cualquier
elemento operado mediante $\vee$ con el máximo $\top$ es absorbido por
este, dando como resultado $\top$. De igual manera, operar cualquier
elemento mediante $\wedge$ con el mínimo $\bot$ siempre resulta en
$\bot$: $$\begin{align*}
    \forall a \in \mathbb{B}, \quad a \vee \top &= \top \\
    \forall a \in \mathbb{B}, \quad a \wedge \bot &= \bot
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $a \vee \top = \top$.* $$\begin{align*}
    a \vee \top &= (a \vee \top) \wedge \top & (ElemNeu_\wedge) \\
               &= (a \vee \top) \wedge (a \vee \neg a) & (Comp_\vee) \\
               &= a \vee (\top \wedge \neg a) & (Dist_\vee) \\
               &= a \vee (\neg a \wedge \top) & (Comm_\wedge) \\
               &= a \vee \neg a & (ElemNeu_\wedge) \\
               &= \top & (Comp_\vee)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $a \wedge \bot = \bot$ (Dual).* $$\begin{align*}
    a \wedge \bot &= (a \wedge \bot) \vee \bot & (ElemNeu_\vee) \\
               &= (a \wedge \bot) \vee (a \wedge \neg a) & (Comp_\wedge) \\
               &= a \wedge (\bot \vee \neg a) & (Dist_\wedge) \\
               &= a \wedge (\neg a \vee \bot) & (Comm_\vee) \\
               &= a \wedge \neg a & (ElemNeu_\vee) \\
               &= \bot & (Comp_\wedge)
\end{align*}$$ ◻
:::

::: teorema
Condición de Álgebra Trivialtrivial_cond Si se da el caso extremo de que
el elemento mínimo $\bot$ y el máximo $\top$ son exactamente el mismo,
entonces estamos ante un álgebra que contiene un único elemento en todo
su conjunto (el álgebra trivial):
$$\bot = \top \implies \mathbb{B} = \{\top\} = \{\bot\}$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos que $\bot = \top$. Sea $x \in \mathbb{B}$ un
elemento cualquiera: $$\begin{align*}
    x &= x \vee \bot & (ElemNeu_\vee) \\
      &= x \vee \top & (\text{Hipótesis } \bot = \top) \\
      &= \top & (Abs_\top)
\end{align*}$$ Por tanto, todo elemento $x$ del conjunto es idéntico a
$\top$, lo que implica que $\mathbb{B} = \{\top\} = \{\bot\}$. ◻
:::

::: teorema
Complemento Idéntico implica Álgebra Trivialtrivial_comp Si dentro de la
estructura existe algún elemento que sea igual a su propio complemento
($\neg a = a$), entonces forzosamente todo el sistema colapsa en el
álgebra trivial de un solo elemento:
$$(\exists a \in \mathbb{B} : \neg a = a) \implies \mathbb{B} = \{\top\} = \{\bot\}$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos que existe $a \in \mathbb{B}$ tal que $\neg a = a$.
Por el postulado del Complemento ($Comp_\vee$ y $Comp_\wedge$), sabemos
que $a \vee \neg a = \top$ y $a \wedge \neg a = \bot$. Sustituyendo la
hipótesis $\neg a = a$ en ambas ecuaciones, obtenemos:
$$a \vee a = \top \quad \text{y} \quad a \wedge a = \bot$$ Aplicando el
teorema de Idempotencia ($Idemp_\vee$ y $Idemp_\wedge$), sabemos que
$a \vee a = a$ y $a \wedge a = a$. Por tanto:
$$a = \top \quad \text{y} \quad a = \bot$$ Lo cual implica que
$\bot = \top$. Aplicando el teorema anterior (Condición de Álgebra
Trivial), concluimos que $\mathbb{B} = \{\top\} = \{\bot\}$. ◻
:::

::: teorema
Propiedades de absorción - $Abs_{\vee}, Abs_{\wedge}$absorcion Cuando se
combinan ambas operaciones anidando un elemento consigo mismo y con un
tercero, el elemento repetido \"absorbe\" al otro, independientemente
del valor del segundo: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a \vee (a \wedge b) &= a \\
    \forall a, b \in \mathbb{B}, \quad a \wedge (a \vee b) &= a
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $Abs_\vee$.* $$\begin{align*}
    a \vee (a \wedge b) &= (a \wedge \top) \vee (a \wedge b) & (ElemNeu_\wedge) \\
                        &= a \wedge (\top \vee b) & (Dist_\wedge) \\
                        &= a \wedge (b \vee \top) & (Comm_\vee) \\
                        &= a \wedge \top & (Abs_\top) \\
                        &= a & (ElemNeu_\wedge)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Abs_\wedge$ (Dual).* $$\begin{align*}
    a \wedge (a \vee b) &= (a \vee \bot) \wedge (a \vee b) & (ElemNeu_\vee) \\
                        &= a \vee (\bot \wedge b) & (Dist_\vee) \\
                        &= a \vee (b \wedge \bot) & (Comm_\wedge) \\
                        &= a \vee \bot & (Abs_\bot) \\
                        &= a & (ElemNeu_\vee)
\end{align*}$$ ◻
:::

::: teorema
Propiedades de orden de retículo - $Prop_{\vee,\wedge}$prop_reticulo
Existe una correspondencia biunívoca fundamental entre las dos
operaciones: afirmar que un elemento domina a otro mediante $\vee$
equivale matemáticamente a afirmar que el segundo se impone al primero
mediante $\wedge$:
$$\forall a, b \in \mathbb{B}: \quad a \vee b = a \iff a \wedge b = b$$
:::

**Demostración:**

::: proof
*Demostración de $\implies$.* Supongamos que $a \vee b = a$.
$$\begin{align*}
    a \wedge b &= b \wedge a & (Comm_\wedge) \\
               &= b \wedge (a \vee b) & (\text{Hipótesis } a \vee b = a) \\
               &= b & (Abs_\wedge)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $\impliedby$ (Dual).* Supongamos que $a \wedge b = b$.
$$\begin{align*}
    a \vee b &= b \vee a & (Comm_\vee) \\
               &= (a \wedge b) \vee a & (\text{Hipótesis } a \wedge b = b) \\
               &= a \vee (a \wedge b) & (Comm_\vee) \\
               &= a & (Abs_\vee)
\end{align*}$$ ◻
:::

::: teorema
Equivalencia de operaciones - $Equa_{\vee,\wedge}$equa_operaciones Si
operar dos elementos mediante $\vee$ da exactamente el mismo resultado
que operarlos mediante $\wedge$, esto sólo es lógicamente posible si
ambos elementos son en realidad el mismo:
$$\forall a, b \in \mathbb{B}: \quad a \vee b = a \wedge b \implies a = b$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos $a \vee b = a \wedge b$. Observamos que:
$$\begin{align*}
    a &= a \vee (a \wedge b) & (Abs_\vee) \\
      &= a \vee (a \vee b) & (\text{Hipótesis})
\end{align*}$$ Aplicando $Prop_{\vee,\wedge}$, dado que
$a \vee (a \vee b) = a$, deducimos que $a \wedge (a \vee b) = a \vee b$.
$$\begin{align*}
    a \vee b &= a \wedge (a \vee b) & (\text{Resultado anterior}) \\
             &= a & (Abs_\wedge)
\end{align*}$$ De manera simétrica para $b$: $$\begin{align*}
    b &= b \vee (a \wedge b) & (Abs_\vee) \\
      &= b \vee (a \vee b) & (\text{Hipótesis}) \\
      &= (a \vee b) \vee b & (Comm_\vee)
\end{align*}$$ Aplicando de nuevo $Prop_{\vee,\wedge}$ sobre esta
igualdad, obtenemos que $(a \vee b) \wedge b = a \vee b$. Pero sabemos
por $Abs_\wedge$ que $(a \vee b) \wedge b = b \wedge (a \vee b) = b$.
Por consiguiente, $a \vee b = b$. Finalmente, uniendo ambos resultados:
$a = a \vee b = b$. ◻
:::

::: teorema
Teorema de Cancelación - $Equa_{canc}$equa_canc Si un elemento $a$ se
opera mediante $\vee$ con $b$ y con $c$ dando el mismo resultado, y
además se opera mediante $\wedge$ con $b$ y con $c$ coincidiendo también
los resultados, entonces forzosamente $b$ y $c$ son el mismo elemento:
$$\forall a, b, c \in \mathbb{B}: \quad a \vee b = a \vee c \quad \text{y} \quad a \wedge b = a \wedge c \implies b = c$$
:::

**Demostración:**

::: proof
*Proof.* Este teorema es automejor dualizable al ser sus hipótesis
perfectamente simétricas. $$\begin{align*}
    b &= b \wedge (a \vee b) & (Abs_\wedge) \\
      &= b \wedge (a \vee c) & (\text{Hipótesis } a \vee b = a \vee c) \\
      &= (b \wedge a) \vee (b \wedge c) & (Dist_\wedge) \\
      &= (a \wedge b) \vee (b \wedge c) & (Comm_\wedge) \\
      &= (a \wedge c) \vee (b \wedge c) & (\text{Hipótesis } a \wedge b = a \wedge c) \\
      &= (c \wedge a) \vee (c \wedge b) & (Comm_\wedge \text{ aplicado dos veces}) \\
      &= c \wedge (a \vee b) & (Dist_\wedge) \\
      &= c \wedge (a \vee c) & (\text{Hipótesis } a \vee b = a \vee c) \\
      &= c & (Abs_\wedge)
\end{align*}$$ ◻
:::

::: teorema
Unicidad del complemento - $Unic_{comp}$unic_comp Todo elemento del
conjunto tiene un complemento $\neg a$, y este es estrictamente único.
Ningún otro elemento puede cumplir simultáneamente las dos condiciones
del postulado del complemento para un mismo $a$:
$$\forall a, x \in \mathbb{B} : \quad (a \vee x = \top \quad \text{y} \quad a \wedge x = \bot) \implies x = \neg a$$
:::

**Demostración:**

::: proof
*Proof.* Supongamos que existe $x \in \mathbb{B}$ tal que
$a \vee x = \top$ y $a \wedge x = \bot$. $$\begin{align*}
    x &= x \wedge \top & (ElemNeu_\wedge) \\
      &= x \wedge (a \vee \neg a) & (Comp_\vee) \\
      &= (x \wedge a) \vee (x \wedge \neg a) & (Dist_\wedge) \\
      &= (a \wedge x) \vee (x \wedge \neg a) & (Comm_\wedge) \\
      &= \bot \vee (x \wedge \neg a) & (\text{Hipótesis } a \wedge x = \bot) \\
      &= (a \wedge \neg a) \vee (x \wedge \neg a) & (Comp_\wedge) \\
      &= (a \vee x) \wedge \neg a & (Dist_\wedge) \\
      &= \top \wedge \neg a & (\text{Hipótesis } a \vee x = \top) \\
      &= \neg a \wedge \top & (Comm_\wedge) \\
      &= \neg a & (ElemNeu_\wedge)
\end{align*}$$ Por tanto, si $x$ cumple las condiciones de complemento,
$x$ tiene que ser necesariamente $\neg a$. ◻
:::

::: teorema
Involución - $Comp_{inv}$comp_inv Aplicar la operación de complemento (o
negación) dos veces consecutivas sobre un mismo elemento cancela su
efecto, devolviendo el elemento original intacto:
$$\forall a \in \mathbb{B}, \quad \neg (\neg a) = a$$
:::

**Demostración:**

::: proof
*Proof.* Por definición, el complemento de $\neg a$, denotado como
$\neg (\neg a)$, es el elemento único que satisface:
$$\neg a \vee \neg (\neg a) = \top \quad \text{y} \quad \neg a \wedge \neg (\neg a) = \bot$$
Sin embargo, por la conmutatividad ($Comm_\vee$ y $Comm_\wedge$),
sabemos que:
$$\neg a \vee a = a \vee \neg a = \top \quad \text{y} \quad \neg a \wedge a = a \wedge \neg a = \bot$$
Esto demuestra que $a$ actúa como un complemento de $\neg a$. Por el
teorema de unicidad del complemento ($Unic_{comp}$), concluimos
necesariamente que $\neg (\neg a) = a$. ◻
:::

::: teorema
Leyes de De Morgan - $Mor_{\vee, \wedge}$morgan La negación matemática
se distribuye sobre las operaciones, pero al hacerlo, invierte la
operación original: un supremo ($\vee$) negado se convierte en el ínfimo
($\wedge$) de las negaciones, y viceversa: $$\begin{align}
    \neg (a \vee b) &= \neg a \wedge \neg b \\
    \neg (a \wedge b) &= \neg a \vee \neg b
\end{align}$$ De forma equivalente, aislando las variables mediante la
involución, podemos expresar las operaciones básicas exclusivamente a
partir de su dual negada: $$\begin{align}
    a \vee b &= \neg (\neg a \wedge \neg b) \\
    a \wedge b &= \neg (\neg a \vee \neg b)
\end{align}$$
:::

**Demostración:**

::: proof
*Demostración de $\neg (a \vee b) = \neg a \wedge \neg b$.* Para
demostrarlo sin recurrir a la asociatividad, usaremos las propiedades de
absorción. Comprobemos primero la suma:
$(a \vee b) \vee (\neg a \wedge \neg b) = \top$. Sabemos por
$Abs_\wedge$ que $a \wedge (a \vee b) = a$. $$\begin{align*}
    \neg a \vee (a \wedge (a \vee b)) &= \neg a \vee a = \top & (Comp_\vee) \\
    (\neg a \vee a) \wedge (\neg a \vee (a \vee b)) &= \top & (Dist_\vee) \\
    \top \wedge (\neg a \vee (a \vee b)) &= \top & (Comp_\vee) \\
    \neg a \vee (a \vee b) &= \top & (ElemNeu_\wedge)
\end{align*}$$ Simétricamente, como
$b \wedge (a \vee b) = b \wedge (b \vee a) = b$, obtenemos
$\neg b \vee (a \vee b) = \top$. Por tanto: $$\begin{align*}
    (a \vee b) \vee (\neg a \wedge \neg b) &= ((a \vee b) \vee \neg a) \wedge ((a \vee b) \vee \neg b) & (Dist_\vee) \\
    &= (\neg a \vee (a \vee b)) \wedge (\neg b \vee (a \vee b)) & (Comm_\vee) \\
    &= \top \wedge \top & (\text{Resultados anteriores}) \\
    &= \top & (Idemp_\wedge)
\end{align*}$$

Segundo, comprobemos el producto:
$(a \vee b) \wedge (\neg a \wedge \neg b) = \bot$. Sabemos por
$Abs_\vee$ que $\neg a \vee (\neg a \wedge \neg b) = \neg a$.
$$\begin{align*}
    a \wedge (\neg a \vee (\neg a \wedge \neg b)) &= a \wedge \neg a = \bot & (Comp_\wedge) \\
    (a \wedge \neg a) \vee (a \wedge (\neg a \wedge \neg b)) &= \bot & (Dist_\wedge) \\
    \bot \vee (a \wedge (\neg a \wedge \neg b)) &= \bot & (Comp_\wedge) \\
    a \wedge (\neg a \wedge \neg b) &= \bot & (ElemNeu_\vee)
\end{align*}$$ Simétricamente, como
$\neg b \vee (\neg a \wedge \neg b) = \neg b \vee (\neg b \wedge \neg a) = \neg b$,
obtenemos $b \wedge (\neg a \wedge \neg b) = \bot$. Por tanto:
$$\begin{align*}
    (a \vee b) \wedge (\neg a \wedge \neg b) &= (\neg a \wedge \neg b) \wedge (a \vee b) & (Comm_\wedge) \\
    &= ((\neg a \wedge \neg b) \wedge a) \vee ((\neg a \wedge \neg b) \wedge b) & (Dist_\wedge) \\
    &= (a \wedge (\neg a \wedge \neg b)) \vee (b \wedge (\neg a \wedge \neg b)) & (Comm_\wedge) \\
    &= \bot \vee \bot & (\text{Resultados anteriores}) \\
    &= \bot & (Idemp_\vee)
\end{align*}$$ Por el teorema de unicidad ($Unic_{comp}$), concluimos
que $\neg (a \vee b) = \neg a \wedge \neg b$. ◻
:::

::: proof
*Demostración de $\neg (a \wedge b) = \neg a \vee \neg b$ (Dual).*
Intercambiando operaciones y constantes, comprobamos el producto:
$(a \wedge b) \wedge (\neg a \vee \neg b) = \bot$. Sabemos por
$Abs_\vee$ que $a \vee (a \wedge b) = a$. $$\begin{align*}
    \neg a \wedge (a \vee (a \wedge b)) &= \neg a \wedge a = \bot & (Comp_\wedge) \\
    (\neg a \wedge a) \vee (\neg a \wedge (a \wedge b)) &= \bot & (Dist_\wedge) \\
    \bot \vee (\neg a \wedge (a \wedge b)) &= \bot & (Comp_\wedge) \\
    \neg a \wedge (a \wedge b) &= \bot & (ElemNeu_\vee)
\end{align*}$$ Simétricamente, $\neg b \wedge (a \wedge b) = \bot$. Por
tanto: $$\begin{align*}
    (a \wedge b) \wedge (\neg a \vee \neg b) &= ((a \wedge b) \wedge \neg a) \vee ((a \wedge b) \wedge \neg b) & (Dist_\wedge) \\
    &= (\neg a \wedge (a \wedge b)) \vee (\neg b \wedge (a \wedge b)) & (Comm_\wedge) \\
    &= \bot \vee \bot = \bot & (\text{Resultados anteriores})
\end{align*}$$

Comprobemos la suma: $(a \wedge b) \vee (\neg a \vee \neg b) = \top$.
Sabemos por $Abs_\wedge$ que
$\neg a \wedge (\neg a \vee \neg b) = \neg a$. $$\begin{align*}
    a \vee (\neg a \wedge (\neg a \vee \neg b)) &= a \vee \neg a = \top & (Comp_\vee) \\
    (a \vee \neg a) \wedge (a \vee (\neg a \vee \neg b)) &= \top & (Dist_\vee) \\
    \top \wedge (a \vee (\neg a \vee \neg b)) &= \top & (Comp_\vee) \\
    a \vee (\neg a \vee \neg b) &= \top & (ElemNeu_\wedge)
\end{align*}$$ Simétricamente, $b \vee (\neg a \vee \neg b) = \top$. Por
tanto: $$\begin{align*}
    (a \wedge b) \vee (\neg a \vee \neg b) &= (\neg a \vee \neg b) \vee (a \wedge b) & (Comm_\vee) \\
    &= ((\neg a \vee \neg b) \vee a) \wedge ((\neg a \vee \neg b) \vee b) & (Dist_\vee) \\
    &= (a \vee (\neg a \vee \neg b)) \wedge (b \vee (\neg a \vee \neg b)) & (Comm_\vee) \\
    &= \top \wedge \top = \top & (\text{Resultados anteriores})
\end{align*}$$ Por $Unic_{comp}$,
$\neg (a \wedge b) = \neg a \vee \neg b$. ◻
:::

::: proof
*Demostración de $a \vee b = \neg (\neg a \wedge \neg b)$ y su dual.*
Partiendo de $\neg (\neg a \wedge \neg b)$, aplicamos De Morgan a sus
componentes: $$\begin{align*}
    \neg (\neg a \wedge \neg b) &= \neg (\neg a) \vee \neg (\neg b) & (Mor_\wedge) \\
    &= a \vee b & (Comp_{inv})
\end{align*}$$ Dualizando la expresión, obtenemos de manera idéntica que
$\neg (\neg a \vee \neg b) = a \wedge b$. ◻
:::

::: teorema
Asociatividad - $Asoc_\vee, Asoc_\wedge$asociatividad El orden en el que
se agrupan tres o más elementos al aplicar de forma consecutiva la misma
operación ($\vee$ o $\wedge$) no altera el resultado final. Al ubicar
este teorema después de De Morgan, podemos simplificar enormemente su
demostración: $$\begin{align*}
    a \vee (b \vee c) &= (a \vee b) \vee c \\
    a \wedge (b \wedge c) &= (a \wedge b) \wedge c
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $a \vee (b \vee c) = (a \vee b) \vee c$.* Primero,
demostraremos un pequeño **Lema de Igualdad por Casos**: Si
$x \wedge y = x \wedge z$ y $\neg x \wedge y = \neg x \wedge z$,
entonces $y = z$. $$\begin{align*}
    y &= \top \wedge y & (ElemNeu_\wedge) \\
      &= (x \vee \neg x) \wedge y & (Comp_\vee) \\
      &= (x \wedge y) \vee (\neg x \wedge y) & (Dist_\wedge) \\
      &= (x \wedge z) \vee (\neg x \wedge z) & (\text{Por hipótesis del Lema}) \\
      &= (x \vee \neg x) \wedge z & (Dist_\wedge) \\
      &= \top \wedge z = z & (Comp_\vee, ElemNeu_\wedge)
\end{align*}$$ Sea $L = a \vee (b \vee c)$ y $R = (a \vee b) \vee c$.
Aplicaremos el lema usando $x = a$, por lo que debemos demostrar que
$a \wedge L = a \wedge R$ y $\neg a \wedge L = \neg a \wedge R$.

1\) Comprobamos $a \wedge L = a \wedge R$: $$\begin{align*}
    a \wedge L &= a \wedge (a \vee (b \vee c)) = a & (Abs_\wedge) \\
    a \wedge R &= a \wedge ((a \vee b) \vee c) \\
               &= (a \wedge (a \vee b)) \vee (a \wedge c) & (Dist_\wedge) \\
               &= a \vee (a \wedge c) = a & (Abs_\wedge, Abs_\vee)
\end{align*}$$ Por tanto, $a \wedge L = a \wedge R$.

2\) Comprobamos $\neg a \wedge L = \neg a \wedge R$: $$\begin{align*}
    \neg a \wedge L &= \neg a \wedge (a \vee (b \vee c)) \\
                    &= (\neg a \wedge a) \vee (\neg a \wedge (b \vee c)) & (Dist_\wedge) \\
                    &= \bot \vee (\neg a \wedge (b \vee c)) & (Comp_\wedge) \\
                    &= \neg a \wedge (b \vee c) & (ElemNeu_\vee)
\end{align*}$$ $$\begin{align*}
    \neg a \wedge R &= \neg a \wedge ((a \vee b) \vee c) \\
                    &= (\neg a \wedge (a \vee b)) \vee (\neg a \wedge c) & (Dist_\wedge) \\
                    &= ((\neg a \wedge a) \vee (\neg a \wedge b)) \vee (\neg a \wedge c) & (Dist_\wedge) \\
                    &= (\bot \vee (\neg a \wedge b)) \vee (\neg a \wedge c) & (Comp_\wedge) \\
                    &= (\neg a \wedge b) \vee (\neg a \wedge c) & (ElemNeu_\vee) \\
                    &= \neg a \wedge (b \vee c) & (Dist_\wedge)
\end{align*}$$ Como $\neg a \wedge L = \neg a \wedge R$, aplicando el
Lema concluimos que $L = R$, es decir,
$a \vee (b \vee c) = (a \vee b) \vee c$. ◻
:::

::: proof
*Demostración de $a \wedge (b \wedge c) = (a \wedge b) \wedge c$ (Dual
mediante De Morgan).* Al haber demostrado previamente las leyes de De
Morgan, podemos probar la asociatividad del ínfimo de forma directa y
elegante sin necesidad de repetir la manipulación algebraica de la
demostración dual: $$\begin{align*}
    a \wedge (b \wedge c) &= \neg (\neg a \vee \neg (b \wedge c)) & (Mor_\wedge \text{ y } Comp_{inv}) \\
                          &= \neg (\neg a \vee (\neg b \vee \neg c)) & (Mor_\wedge) \\
                          &= \neg ((\neg a \vee \neg b) \vee \neg c) & (Asoc_\vee \text{ demostrada arriba}) \\
                          &= \neg (\neg (a \wedge b) \vee \neg c) & (Mor_\wedge) \\
                          &= (a \wedge b) \wedge c & (Mor_\wedge \text{ y } Comp_{inv})
\end{align*}$$ ◻
:::

## Generalización a $n$ variables

Habiendo demostrado la asociatividad ($Asoc_\vee$ y $Asoc_\wedge$) de
las operaciones fundamentales del álgebra de Boole, el orden en el que
se agrupan las variables al aplicar consecutivamente una misma operación
resulta irrelevante. Esto nos permite prescindir de los paréntesis y
extender de forma natural las operaciones binarias a un número
arbitrario $n$ de operandos.

::: definicion
Disyunción (Supremo) de $n$ variablesor_n_variables La disyunción
múltiple de $n$ variables, denotada de forma compacta mediante el
operador $\bigvee$, se define como la aplicación sucesiva de la
operación $\vee$:
$$\bigvee_{i=1}^n x_i \triangleq x_1 \vee x_2 \vee \dots \vee x_n$$
:::

::: definicion
Conjunción (Ínfimo) de $n$ variablesand_n_variables De manera análoga,
la conjunción múltiple de $n$ variables, denotada mediante el operador
$\bigwedge$, se define como la aplicación sucesiva de la operación
$\wedge$:
$$\bigwedge_{i=1}^n x_i \triangleq x_1 \wedge x_2 \wedge \dots \wedge x_n$$
:::

La existencia de estas operaciones múltiples bien definidas es un pilar
fundamental para desarrollar formas canónicas (como la suma de productos
o producto de sumas) y, como veremos a continuación, servirá de base
para extender el número de entradas de los operadores derivados.

# Operadores Derivados: NAND, NOR, XOR y XNOR

Las ecuaciones obtenidas a partir de las Leyes de De Morgan demuestran
que las operaciones básicas $\vee$ y $\wedge$ pueden ser expresadas
íntegramente en términos de la negación de su operación dual. Esto
motiva la definición de varios operadores lógicos fundamentales en
sistemas digitales. Dos de ellos (NAND y NOR) son de gran relevancia por
ser funcionalmente completos por sí solos, mientras que otros dos (XOR y
XNOR) son esenciales para funciones aritméticas y de comprobación de
paridad:

::: definicion
Operador NAND (Barra de Sheffer)nand Denotado clásicamente con una
flecha hacia arriba ($\uparrow$), se define como la negación del ínfimo.
$$a \uparrow b \triangleq \neg (a \wedge b) = \neg a \vee \neg b$$
:::

::: definicion
Operador NOR (Flecha de Peirce)nor Denotado con una flecha hacia abajo
($\downarrow$), se define como la negación del supremo.
$$a \downarrow b \triangleq \neg (a \vee b) = \neg a \wedge \neg b$$
:::

::: definicion
Operador XOR (O-exclusiva)xor Denotado con el símbolo de suma exclusiva
($\oplus$), evalúa a $\top$ cuando exactamente uno de los operandos es
$\top$ y el otro $\bot$.
$$a \oplus b \triangleq (a \wedge \neg b) \vee (\neg a \wedge b)$$
:::

::: definicion
Operador XNOR (No-O-exclusiva o Equivalencia)xnor Denotado
frecuentemente con $\odot$ o $\leftrightarrow$, es la negación de la
operación XOR y evalúa a $\top$ cuando ambos operandos son idénticos.
$$a \odot b \triangleq \neg (a \oplus b) = (a \wedge b) \vee (\neg a \wedge \neg b)$$
:::

::: definicion
Generalización a $n$ variables de NAND y NORgen_nand_nor A diferencia de
los operadores $\vee$, $\wedge$ y $\oplus$, los operadores NAND
($\uparrow$) y NOR ($\downarrow$) **no son asociativos**. Sin embargo,
debido a su inmensa importancia práctica en la construcción de circuitos
digitales, se define convencionalmente su generalización a $n$ variables
como la negación de la conjunción o disyunción múltiple,
respectivamente:
$$\text{NAND}(x_1, x_2, \dots, x_n) \triangleq \neg \left( \bigwedge_{i=1}^n x_i \right)$$
$$\text{NOR}(x_1, x_2, \dots, x_n) \triangleq \neg \left( \bigvee_{i=1}^n x_i \right)$$
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
    \forall a \in \mathbb{B}, \quad a \uparrow a &= \neg a \\
    \forall a \in \mathbb{B}, \quad a \downarrow a &= \neg a
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la operación NAND: $$\begin{align*}
    a \uparrow a &\triangleq \neg (a \wedge a) & (\text{Definicion de NAND}) \\
                 &= \neg a & (Idemp_\wedge)
\end{align*}$$ Para la operación NOR: $$\begin{align*}
    a \downarrow a &\triangleq \neg (a \vee a) & (\text{Definicion de NOR}) \\
                   &= \neg a & (Idemp_\vee)
\end{align*}$$ ◻
:::

::: teorema
Generación del Ínfimo y Supremo (AND y OR)gen_inf_sup A partir de la
propiedad anterior, podemos recuperar las operaciones básicas anidando
las puertas consigo mismas: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a \wedge b &= \neg (a \uparrow b) = (a \uparrow b) \uparrow (a \uparrow b) \\
    \forall a, b \in \mathbb{B}, \quad a \vee b &= \neg (a \downarrow b) = (a \downarrow b) \downarrow (a \downarrow b)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la generación del ínfimo (AND): $$\begin{align*}
    \neg(a \uparrow b) &\triangleq \neg(\neg(a \wedge b)) & (\text{Definicion de NAND}) \\
                       &= a \wedge b & (Involucion)
\end{align*}$$ Además, por la idempotencia cruzada demostrada
anteriormente, $x \uparrow x = \neg x$, por tanto:
$$\neg(a \uparrow b) = (a \uparrow b) \uparrow (a \uparrow b)$$ La
demostración para la generación del supremo (OR) es idéntica por
dualidad. ◻
:::

::: teorema
Generación cruzada (Leyes de De Morgan para NAND/NOR)gen_cruzada Podemos
generar la operación opuesta (supremo desde NAND, e ínfimo desde NOR)
negando previamente las entradas: $$\begin{align*}
    \forall a, b \in \mathbb{B}, \quad a \vee b &= (\neg a) \uparrow (\neg b) = (a \uparrow a) \uparrow (b \uparrow b) \\
    \forall a, b \in \mathbb{B}, \quad a \wedge b &= (\neg a) \downarrow (\neg b) = (a \downarrow a) \downarrow (b \downarrow b)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para el supremo (OR): $$\begin{align*}
    (\neg a) \uparrow (\neg b) &\triangleq \neg (\neg a \wedge \neg b) & (\text{Definicion de NAND}) \\
                               &= \neg (\neg (a \vee b)) & (Mor_\vee) \\
                               &= a \vee b & (Involucion)
\end{align*}$$ La demostración para el ínfimo (AND) sigue los mismos
pasos de manera dual, aplicando $Mor_\wedge$. ◻
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
    a \uparrow b &\triangleq \neg (a \wedge b) & (\text{Definicion de NAND}) \\
                 &= \neg (b \wedge a) & (Comm_\wedge) \\
                 &\triangleq b \uparrow a & (\text{Definicion de NAND})
\end{align*}$$ Para la operación NOR, es análogo aplicando
$Comm_\vee$. ◻
:::

::: teorema
Inexistencia de Elemento Neutrono_neutro No existe ningún elemento
neutro para las operaciones NAND ni NOR en un álgebra de Boole general.
:::

**Demostración:**

::: proof
*Demostración.* Si existiera un neutro $e$ para la operación NAND,
debería cumplirse que $\forall a, a \uparrow e = a$, es decir,
$\neg(a \wedge e) = a$. Si probamos con $e=\top$, obtenemos
$\neg a = a$, lo cual obliga al colapso en un álgebra trivial. Si
probamos con $e=\bot$, obtenemos $\neg \bot = a \implies \top = a$, lo
cual obviamente no se cumple para cualquier elemento $a$. Lo mismo
aplica a la operación NOR. ◻
:::

::: teorema
Comportamiento con las constantes (Fijación y Absorción)constantes_deriv
Fijar una constante específica en uno de los operandos genera
directamente la negación, mientras que usar la constante opuesta actúa
como un pseudo-elemento absorbente (devolviendo un valor constante
inalterable por $a$): $$\begin{align*}
    \text{Inversión: } & a \uparrow \top = \neg a \qquad & a \downarrow \bot &= \neg a \\
    \text{Absorción: } & a \uparrow \bot = \top \qquad & a \downarrow \top &= \bot
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Para la inversión: $$\begin{align*}
    a \uparrow \top &= \neg(a \wedge \top) = \neg a & (ElemNeu_\wedge) \\
    a \downarrow \bot &= \neg(a \vee \bot) = \neg a & (ElemNeu_\vee)
\end{align*}$$ Para la absorción: $$\begin{align*}
    a \uparrow \bot &= \neg(a \wedge \bot) = \neg \bot = \top & (Abs_\bot) \\
    a \downarrow \top &= \neg(a \vee \top) = \neg \top = \bot & (Abs_\top)
\end{align*}$$ ◻
:::

::: teorema
Ausencia de Asociatividadno_asoc_deriv A diferencia del supremo ($\vee$)
y el ínfimo ($\wedge$), las operaciones NAND y NOR son positivamente NO
asociativas: $$\begin{align*}
    (a \uparrow b) \uparrow c &\neq a \uparrow (b \uparrow c) \\
    (a \downarrow b) \downarrow c &\neq a \downarrow (b \downarrow c)
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración.* Desarrollando el lado izquierdo para NAND:
$$(a \uparrow b) \uparrow c = \neg ( (\neg (a \wedge b)) \wedge c ) = (a \wedge b) \vee \neg c$$
Desarrollando el lado derecho:
$$a \uparrow (b \uparrow c) = \neg ( a \wedge (\neg (b \wedge c)) ) = \neg a \vee (b \wedge c)$$
Resulta evidente que
$(a \wedge b) \vee \neg c \neq \neg a \vee (b \wedge c)$ para
combinaciones arbitrarias de variables. El mismo razonamiento aplica de
manera estricta y análoga para demostrar la carencia de asociatividad en
la operación NOR ($\downarrow$). ◻
:::

::: definicion
NAND y NOR de $n$ entradasdef_n_entradas Dado que las puertas NAND y NOR
físicas a menudo tienen más de dos entradas, se definen algebraicamente
para múltiples entradas como la negación de la conjunción o disyunción
de todas ellas: $$\begin{align*}
    \uparrow(x_1, x_2, \dots, x_n) &\triangleq \neg \left( \bigwedge_{i=1}^n x_i \right) \\
    \downarrow(x_1, x_2, \dots, x_n) &\triangleq \neg \left( \bigvee_{i=1}^n x_i \right)
\end{align*}$$ En particular, para el caso de 3 entradas que
estudiaremos a continuación: $$\begin{align*}
    \uparrow(a,b,c) &\triangleq \neg(a \wedge b \wedge c) \\
    \downarrow(a,b,c) &\triangleq \neg(a \vee b \vee c)
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
$$\uparrow(a,b,c) \triangleq \neg(a \wedge b \wedge c) = \neg a \vee \neg b \vee \neg c$$
Sin embargo, la agrupación de dos en dos evaluada anteriormente daba:
$$(a \uparrow b) \uparrow c = (a \wedge b) \vee \neg c$$ Evidentemente,
$\neg a \vee \neg b \vee \neg c \neq (a \wedge b) \vee \neg c$. Lo mismo
aplica a las agrupaciones derechas y a las operaciones NOR
equivalentes. ◻
:::

::: teorema
Extensión del Principio de Dualidad (NAND y NOR)dualidad_nand_nor La
inclusión de los operadores derivados expande el Principio de Dualidad
establecido en los postulados iniciales. La expresión dual de cualquier
teorema o identidad que contenga operaciones NAND o NOR se obtiene
intercambiando los operadores $\uparrow$ y $\downarrow$ (además de los
ya conocidos $\vee \leftrightarrow \wedge$ y
$\bot \leftrightarrow \top$).
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
    a \oplus b &\triangleq (a \wedge \neg b) \vee (\neg a \wedge b) & (\text{Definición de XOR}) \\
               &= (\neg a \wedge b) \vee (a \wedge \neg b) & (Comm_\vee) \\
               &= (b \wedge \neg a) \vee (\neg b \wedge a) & (Comm_\wedge) \\
               &\triangleq b \oplus a & (\text{Definición de XOR})
\end{align*}$$ La demostración para XNOR sigue pasos idénticos
aprovechando la conmutatividad del ínfimo y el supremo. ◻
:::

::: teorema
Elementos Neutros e Inversoresneutro_xor El elemento $\bot$ actúa como
neutro para la XOR, y $\top$ actúa como inversor. De manera dual, $\top$
es el neutro de la XNOR, y $\bot$ actúa como inversor: $$\begin{align*}
    a \oplus \bot &= a & a \oplus \top &= \neg a \\
    a \odot \top &= a & a \odot \bot &= \neg a
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración para XOR.* Para el elemento $\bot$ (neutro):
$$\begin{align*}
    a \oplus \bot &\triangleq (a \wedge \neg \bot) \vee (\neg a \wedge \bot) & (\text{Definición}) \\
                  &= (a \wedge \top) \vee \bot & (Comp_{inv} \text{ y } Fij_\wedge) \\
                  &= a \vee \bot & (ElemNeu_\wedge) \\
                  &= a & (ElemNeu_\vee)
\end{align*}$$ Para el elemento $\top$ (inversor): $$\begin{align*}
    a \oplus \top &\triangleq (a \wedge \neg \top) \vee (\neg a \wedge \top) & (\text{Definición}) \\
                  &= (a \wedge \bot) \vee \neg a & (Comp_{inv} \text{ y } ElemNeu_\wedge) \\
                  &= \bot \vee \neg a & (Fij_\wedge) \\
                  &= \neg a & (ElemNeu_\vee)
\end{align*}$$ Las pruebas para XNOR son totalmente duales. ◻
:::

::: teorema
Elemento Inverso de sí mismo (Grupo Abeliano)idemp_nula_xor La
combinación de un elemento consigo mismo produce una anulación (devuelve
el neutro de la operación correspondiente), actuando cada elemento como
su propio inverso:
$$a \oplus a = \bot \qquad \text{y} \qquad a \odot a = \top$$
:::

**Demostración:**

::: proof
*Demostración.* Para XOR: $$\begin{align*}
    a \oplus a &\triangleq (a \wedge \neg a) \vee (\neg a \wedge a) \\
               &= \bot \vee \bot & (Comp_\wedge \text{ y } Comm_\wedge) \\
               &= \bot & (Idemp_\vee)
\end{align*}$$ Para XNOR: $$\begin{align*}
    a \odot a &\triangleq (a \wedge a) \vee (\neg a \wedge \neg a) \\
              &= a \vee \neg a & (Idemp_\wedge) \\
              &= \top & (Comp_\vee)
\end{align*}$$ ◻
:::

::: teorema
Propiedades de Negaciónnegacion_xor Negar cualquiera de las entradas de
forma independiente equivale a negar la operación completa, lo que a su
vez alterna entre XOR y XNOR: $$\begin{align*}
    \neg (a \oplus b) &= \neg a \oplus b = a \oplus \neg b = a \odot b \\
    \neg (a \odot b) &= \neg a \odot b = a \odot \neg b = a \oplus b
\end{align*}$$
:::

**Demostración:**

::: proof
*Demostración de $a \oplus \neg b = \neg(a \oplus b)$.* $$\begin{align*}
    a \oplus \neg b &\triangleq (a \wedge \neg(\neg b)) \vee (\neg a \wedge \neg b) \\
                    &= (a \wedge b) \vee (\neg a \wedge \neg b) & (Involucion) \\
                    &\triangleq a \odot b & (\text{Definición de XNOR})
\end{align*}$$ Sabiendo por definición que
$a \odot b \triangleq \neg(a \oplus b)$, se concluye de forma inmediata
que $a \oplus \neg b = \neg (a \oplus b)$. ◻
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
    X \oplus c &\triangleq (X \wedge \neg c) \vee (\neg X \wedge c) \\
               &= \big( ((a \wedge \neg b) \vee (\neg a \wedge b)) \wedge \neg c \big) \vee \big( \neg ((a \wedge \neg b) \vee (\neg a \wedge b)) \wedge c \big) \\
               &= \big( ((a \wedge \neg b) \vee (\neg a \wedge b)) \wedge \neg c \big) \vee \big( (a \odot b) \wedge c \big) \quad (\text{Definición de XNOR}) \\
               &= \big( (a \wedge \neg b \wedge \neg c) \vee (\neg a \wedge b \wedge \neg c) \big) \vee \big( ((a \wedge b) \vee (\neg a \wedge \neg b)) \wedge c \big) \quad (Dist_\wedge) \\
               &= (a \wedge \neg b \wedge \neg c) \vee (\neg a \wedge b \wedge \neg c) \\
               &\quad \vee (a \wedge b \wedge c) \vee (\neg a \wedge \neg b \wedge c) \quad (Dist_\wedge)
\end{align*}$$ Ahora evaluaremos el miembro derecho
$a \oplus (b \oplus c)$. Llamaremos $Y = b \oplus c$. $$\begin{align*}
    a \oplus Y &\triangleq (a \wedge \neg Y) \vee (\neg a \wedge Y) \\
               &= (a \wedge (b \odot c)) \vee (\neg a \wedge ((b \wedge \neg c) \vee (\neg b \wedge c))) \\
               &= (a \wedge ((b \wedge c) \vee (\neg b \wedge \neg c))) \vee (\neg a \wedge b \wedge \neg c) \vee (\neg a \wedge \neg b \wedge c) \\
               &= (a \wedge b \wedge c) \vee (a \wedge \neg b \wedge \neg c) \\
               &\quad \vee (\neg a \wedge b \wedge \neg c) \vee (\neg a \wedge \neg b \wedge c)
\end{align*}$$ Como podemos observar, ambas expansiones resultan
exactamente en los mismos cuatro minitérminos. Reordenándolos por
conmutatividad ($Comm_\vee$) demostramos que son idénticos. ◻
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
$$a \wedge (b \oplus c) = (a \wedge b) \oplus (a \wedge c)$$
$$a \vee (b \odot c) = (a \vee b) \odot (a \vee c)$$
:::

**Demostración:**

::: proof
*Demostración de AND sobre XOR.* Desarrollando el lado derecho (RHS):
$$\begin{align*}
    (a \wedge b) \oplus (a \wedge c) &\triangleq ((a \wedge b) \wedge \neg(a \wedge c)) \vee (\neg(a \wedge b) \wedge (a \wedge c)) \\
                                     &= (a \wedge b \wedge (\neg a \vee \neg c)) \vee ((\neg a \vee \neg b) \wedge a \wedge c) \quad (Mor_\wedge) \\
                                     &= ((a \wedge b \wedge \neg a) \vee (a \wedge b \wedge \neg c)) \\
                                     &\quad \vee ((a \wedge c \wedge \neg a) \vee (a \wedge c \wedge \neg b)) \quad (Dist_\wedge) \\
                                     &= (\bot \vee (a \wedge b \wedge \neg c)) \vee (\bot \vee (a \wedge \neg b \wedge c)) \quad (Comp_\wedge \text{ y } Fij_\wedge) \\
                                     &= (a \wedge b \wedge \neg c) \vee (a \wedge \neg b \wedge c) \quad (ElemNeu_\vee) \\
                                     &= a \wedge ((b \wedge \neg c) \vee (\neg b \wedge c)) \quad (Dist_\wedge \text{ a la inversa}) \\
                                     &\triangleq a \wedge (b \oplus c) \quad (\text{Def. XOR})
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
de un elemento neutro para la disyunción ($\bot \in B$) y otro para la
conjunción ($\top \in B$), y puesto que el conjunto solo contiene un
único elemento, estos deben forzosamente coincidir: $$\bot = \top = c$$

Al instanciar cualquier operación definida sobre este conjunto, los
resultados siempre evalúan a dicha constante $c$.

- **Negación:** Por el postulado del complemento, $c \vee \neg c = c$ y
  $c \wedge \neg c = c$, lo que implica que $\neg c = c$.

- **Disyunción y Conjunción:** Por la propiedad de idempotencia,
  $c \vee c = c$ y $c \wedge c = c$.

- **Operadores Derivados:** Por definición,
  $c \uparrow c = \neg (c \wedge c) = \neg c = c$. Lo mismo sucede con
  el resto de operadores.

Visualizar esto en tablas de operación (comúnmente conocidas como tablas
de verdad) resulta en estructuras degeneradas de una sola celda, donde
$\circ \in \{ \vee, \wedge, \uparrow, \downarrow, \oplus, \odot \}$:

::: center
   $a$   $\neg a$
  ----- ----------
   $c$     $c$

   $a$   $b$   $a \circ b$
  ----- ----- -------------
   $c$   $c$       $c$
:::

### Álgebra Bivaluada ($|B| = 2$)

El caso más importante para la ingeniería es el álgebra de Boole
bivaluada, donde el conjunto soporte consta exactamente de los dos
elementos garantizados por los postulados: el neutro disyuntivo y el
neutro conjuntivo. $$B = \{ \bot, \top \}$$ (Asumiendo lógicamente que
$\bot \neq \top$).

Procederemos a deducir el comportamiento (las tablas de operación)
instanciando los teoremas y postulados axiomáticos en estos dos únicos
valores.

#### Operaciones Básicas ($\neg$, $\vee$, $\wedge$)

**1. Negación (Operación unaria $\neg$)**\
El Postulado 5 (Complemento) exige que:
$$\bot \vee \neg \bot = \top \quad \text{y} \quad \top \vee \neg \top = \top$$
Al existir solo dos elementos en el conjunto, el único valor que sumado
a $\bot$ (que es el neutro disyuntivo, por lo que no altera el
resultado) da $\top$, es el propio $\top$. Por lo tanto, deducimos que
$\neg \bot = \top$. De igual manera, por dualidad, $\neg \top = \bot$.

**2. Disyunción (Operación binaria $\vee$)**\
Calculamos los cuatro casos posibles instanciando los valores:

- $\bot \vee \bot = \bot$ (Por Idempotencia, Teorema 1).

- $\bot \vee \top = \top$ (Por ser $\bot$ el elemento neutro, Postulado
  2a).

- $\top \vee \bot = \top$ (Por Conmutatividad, Postulado 3a).

- $\top \vee \top = \top$ (Por Idempotencia, Teorema 1).

**3. Conjunción (Operación binaria $\wedge$)**\
Análogamente:

- $\top \wedge \top = \top$ (Por Idempotencia, Teorema 1).

- $\top \wedge \bot = \bot$ (Por ser $\top$ el elemento neutro,
  Postulado 2b).

- $\bot \wedge \top = \bot$ (Por Conmutatividad, Postulado 3b).

- $\bot \wedge \bot = \bot$ (Por Idempotencia, Teorema 1).

#### Operadores Derivados ($\uparrow, \downarrow, \oplus, \odot$)

Podemos obtener las tablas de los operadores derivados aplicando
directamente sus definiciones algebraicas sobre las tablas básicas ya
obtenidas:

**1. NAND y NOR**\
Dado que $a \uparrow b = \neg(a \wedge b)$ y
$a \downarrow b = \neg(a \vee b)$, los resultados consisten simplemente
en aplicar el operador complemento ($\neg$) a las tablas de conjunción y
disyunción calculadas previamente.

**2. XOR y XNOR**\
Recordando la definición algebraica
$a \oplus b = (a \wedge \neg b) \vee (\neg a \wedge b)$, se puede
evaluar caso por caso (por ejemplo,
$\top \oplus \bot = (\top \wedge \top) \vee (\bot \wedge \bot) = \top \vee \bot = \top$),
pero también podemos usar directamente los teoremas derivados
anteriormente:

- $a \oplus \bot = a$ (Elemento neutro). Por lo tanto:
  $\bot \oplus \bot = \bot$, y $\top \oplus \bot = \top$.

- $a \oplus \top = \neg a$ (Inversor). Por lo tanto:
  $\bot \oplus \top = \top$, y $\top \oplus \top = \bot$.

Por dualidad, y sabiendo que el XNOR es la negación del XOR, se obtiene
trivialmente que $a \odot b = \neg(a \oplus b)$.

#### Resumen: Tablas de Operación Bivaluadas

A continuación, presentamos la consolidación matricial de todas las
operaciones deducidas, conformando las tablas de verdad definitivas del
álgebra de dos valores:

::: {#tab:tablas_bivaluadas}
    $a$     $\neg a$
  -------- ----------
   $\bot$    $\top$
   $\top$    $\bot$

  : Tablas de Verdad consolidadas para las Operaciones del Álgebra de
  Boole de 2 elementos.
:::

::: {#tab:tablas_bivaluadas}
    $a$      $b$     $a \vee b$   $a \wedge b$   $a \uparrow b$   $a \downarrow b$   $a \oplus b$   $a \odot b$
  -------- -------- ------------ -------------- ---------------- ------------------ -------------- -------------
   $\bot$   $\bot$     $\bot$        $\bot$          $\top$            $\top$           $\bot$        $\top$
   $\bot$   $\top$     $\top$        $\bot$          $\top$            $\bot$           $\top$        $\bot$
   $\top$   $\bot$     $\top$        $\bot$          $\top$            $\bot$           $\top$        $\bot$
   $\top$   $\top$     $\top$        $\top$          $\bot$            $\bot$           $\bot$        $\top$

  : Tablas de Verdad consolidadas para las Operaciones del Álgebra de
  Boole de 2 elementos.
:::

## Conclusiones y Transición a la Lógica Digital

Tras haber establecido formalmente la estructura matemática del álgebra
de Boole a partir de los postulados de Huntington, y haber demostrado
rigurosamente sus propiedades fundamentales operando con la signatura
clásica de la teoría de retículos ($\vee, \wedge, \bot, \top$), estamos
en disposición de dar el salto al dominio de la ingeniería.

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

- **Constantes lógicas:** El elemento mínimo $\bot$ (falso) se denotará
  como **0** (ó nivel bajo de tensión, $L$). El elemento máximo $\top$
  (verdadero) se denotará como **1** (ó nivel alto de tensión, $H$).

- **Supremo (Join / Disyunción):** La operación $\vee$ se denotará
  mediante el operador suma $\mathbf{+}$. En circuitos lógicos,
  implementa la puerta **OR**.

- **Ínfimo (Meet / Conjunción):** La operación $\wedge$ se denotará
  mediante el operador producto $\mathbf{\cdot}$ (frecuentemente
  omitido, escribiendo $ab$ en lugar de $a \cdot b$). Implementa la
  puerta **AND**.

- **Complemento (Negación):** La operación de complemento $\neg a$ se
  denotará convencionalmente colocando una barra superior sobre la
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

## Anexo: Resumen de Postulados y Teoremas (Notación Ingenieril)

En esta sección se recopilan los postulados de Huntington y los teoremas
principales derivados, transcritos a la notación propia del álgebra de
conmutación y la lógica digital ($+$, $\cdot$, $0$, $1$,
$\overline{a}$), concebidos como hoja de referencia rápida.

### Pre-Axiomas de la Estructura {#pre-axiomas-de-la-estructura-1 .unnumbered}

::: preaxioma
Estructura de Conjuntoesconj_eng Se requiere que se defina sobre un
conjunto (por ejemplo, $\mathbb{B}_2 = \{0, 1\}$).
:::

::: preaxioma
Constantes Lógicasconstantes_eng Este conjunto contiene dos constantes
fundamentales: $0$ (falso) y $1$ (verdadero).
:::

::: preaxioma
Operaciones Binarias Internasopbinint_eng Se definen dos operaciones
binarias internas, la suma ($+$) y el producto ($\cdot$):
$$\begin{align*}
+ &: \mathbb{B}_2 \times \mathbb{B}_2 \to \mathbb{B}_2 \\
\cdot &: \mathbb{B}_2 \times \mathbb{B}_2 \to \mathbb{B}_2
\end{align*}$$
:::

::: preaxioma
Existencia y Unicidad de Imagenexist_unic_eng Para cada par de elementos
del conjunto, las operaciones $+$ y $\cdot$ siempre producen un
resultado que también pertenece al conjunto, y ese resultado es siempre
único.
:::

### Postulados de Huntington {#postulados-de-huntington .unnumbered}

::: postulado
Elemento neutroneutro_eng
$$a + 0 = a \qquad \text{y} \qquad a \cdot 1 = a$$
:::

::: postulado
Conmutatividadconmut_eng
$$a + b = b + a \qquad \text{y} \qquad a \cdot b = b \cdot a$$
:::

::: postulado
Distributividaddistrib_eng
$$a \cdot (b + c) = (a \cdot b) + (a \cdot c) \qquad \text{y} \qquad a + (b \cdot c) = (a + b) \cdot (a + c)$$
:::

::: postulado
Complementariocomp_eng Para cada elemento $a$, existe un complemento
$\overline{a}$ tal que:
$$a + \overline{a} = 1 \qquad \text{y} \qquad a \cdot \overline{a} = 0$$
:::

### Teoremas Fundamentales {#teoremas-fundamentales .unnumbered}

::: teorema
Unicidad de los elementos neutrosunicidad_neutros_eng El elemento neutro
para la suma ($0$) y para el producto ($1$) son únicos.
:::

::: teorema
Idempotenciaidempotencia_eng
$$a + a = a \qquad \text{y} \qquad a \cdot a = a$$
:::

::: teorema
Elementos absorbentesabsorbentes_eng
$$a + 1 = 1 \qquad \text{y} \qquad a \cdot 0 = 0$$
:::

::: teorema
Propiedades de absorciónabsorcion_eng
$$a + (a \cdot b) = a \qquad \text{y} \qquad a \cdot (a + b) = a$$
:::

::: teorema
Leyes de De Morganmorgan_eng
$$\overline{a + b} = \overline{a} \cdot \overline{b} \qquad \text{y} \qquad \overline{a \cdot b} = \overline{a} + \overline{b}$$
:::

::: teorema
Involución (Doble negación)involucion_eng
$$\overline{\overline{a}} = a$$
:::

::: teorema
Asociatividadasociatividad_eng
$$a + (b + c) = (a + b) + c \qquad \text{y} \qquad a \cdot (b \cdot c) = (a \cdot b) \cdot c$$
:::

::: teorema
Unicidad del complementounic_comp_eng El complemento $\overline{a}$ de
un elemento $a$ es único.
:::

::: teorema
Otras propiedades equivalentesotras_prop_eng

- **Orden de retículo:** $a + b = a \iff a \cdot b = b$

- **Equivalencia de operaciones:** $a + b = a \cdot b \implies a = b$

- **Cancelación:**
  $(a + b = a + c \text{ y } a \cdot b = a \cdot c) \implies b = c$
:::

::: definicion
Generalización a $n$ variablesgen_n_vars_eng Las operaciones disyunción
y conjunción pueden extenderse a un número $n$ de variables mediante los
símbolos sumatorio y productorio:
$$\sum_{i=1}^{n} x_i = x_1 + x_2 + \dots + x_n$$
$$\prod_{i=1}^{n} x_i = x_1 \cdot x_2 \cdot \dots \cdot x_n$$
:::

::: teorema
Casos de Álgebra Trivialtrivial_eng Si $0 = 1$, o si existe algún
elemento tal que $\overline{a} = a$, entonces el álgebra contiene un
único elemento (álgebra trivial).
:::

### Comportamiento de Operadores Derivados {#comportamiento-de-operadores-derivados .unnumbered}

::: teorema
Idempotencia cruzada (NAND/NOR)idemp_cruzada_eng
$$a \uparrow a = \overline{a} \qquad \text{y} \qquad a \downarrow a = \overline{a}$$
:::

::: teorema
Generación de AND y ORgen_inf_sup_eng
$$a \cdot b = \overline{a \uparrow b} = (a \uparrow b) \uparrow (a \uparrow b) \qquad \text{y} \qquad a + b = \overline{a \downarrow b} = (a \downarrow b) \downarrow (a \downarrow b)$$
:::

::: teorema
Generación cruzadagen_cruzada_eng
$$a + b = \overline{a} \uparrow \overline{b} = (a \uparrow a) \uparrow (b \uparrow b) \qquad \text{y} \qquad a \cdot b = \overline{a} \downarrow \overline{b} = (a \downarrow a) \downarrow (b \downarrow b)$$
:::

::: teorema
Conmutatividadconmut_deriv_eng
$$a \uparrow b = b \uparrow a \qquad \text{y} \qquad a \downarrow b = b \downarrow a$$
:::

::: teorema
Comportamiento con las constantesconstantes_deriv_eng $$\begin{align*}
    a \uparrow 1 &= \overline{a} \qquad & a \downarrow 0 &= \overline{a} \\
    a \uparrow 0 &= 1 \qquad & a \downarrow 1 &= 0
\end{align*}$$
:::

::: teorema
Ausencia de Asociatividadno_asoc_deriv_eng
$$(a \uparrow b) \uparrow c \neq a \uparrow (b \uparrow c) \qquad \text{y} \qquad (a \downarrow b) \downarrow c \neq a \downarrow (b \downarrow c)$$
:::

::: definicion
NAND y NOR de 3 entradasn_entradas_eng
$$\uparrow(a,b,c) = \overline{a \cdot b \cdot c} \qquad \text{y} \qquad \downarrow(a,b,c) = \overline{a + b + c}$$
:::

::: teorema
NAND/NOR múltiple vs cascada binariamultiple_vs_binaria_eng
$$\begin{align*}
    \uparrow(a,b,c) &\neq (a \uparrow b) \uparrow c \qquad & \uparrow(a,b,c) &\neq a \uparrow (b \uparrow c) \\
    \downarrow(a,b,c) &\neq (a \downarrow b) \downarrow c \qquad & \downarrow(a,b,c) &\neq a \downarrow (b \downarrow c)
\end{align*}$$
:::

### Comportamiento de los Operadores XOR y XNOR {#comportamiento-de-los-operadores-xor-y-xnor-1 .unnumbered}

::: definicion
Definición de XOR y XNORdef_xor_xnor_eng
$$a \oplus b = (a \cdot \overline{b}) + (\overline{a} \cdot b) \qquad \text{y} \qquad a \odot b = \overline{a \oplus b} = (a \cdot b) + (\overline{a} \cdot \overline{b})$$
:::

::: teorema
Conmutatividadconmut_xor_eng
$$a \oplus b = b \oplus a \qquad \text{y} \qquad a \odot b = b \odot a$$
:::

::: teorema
Elementos Neutros e Inversoresneutros_xor_eng $$\begin{align*}
    a \oplus 0 &= a \qquad & a \odot 1 &= a \\
    a \oplus 1 &= \overline{a} \qquad & a \odot 0 &= \overline{a}
\end{align*}$$
:::

::: teorema
Elemento Inverso de sí mismo (Grupo Abeliano)idemp_nula_eng
$$a \oplus a = 0 \qquad \text{y} \qquad a \odot a = 1$$
:::

::: teorema
Propiedades de Negaciónneg_xor_eng
$$\overline{a \oplus b} = \overline{a} \oplus b = a \oplus \overline{b} = a \odot b$$
$$\overline{a \odot b} = \overline{a} \odot b = a \odot \overline{b} = a \oplus b$$
:::

::: teorema
Asociatividad y Generalizaciónasoc_gen_xor_eng Ambos operadores son
asociativos:
$$a \oplus (b \oplus c) = (a \oplus b) \oplus c \qquad \text{y} \qquad a \odot (b \odot c) = (a \odot b) \odot c$$
Lo cual permite su generalización a un número arbitrario $n$ de
entradas:
$$\bigoplus_{i=1}^{n} x_i = x_1 \oplus x_2 \oplus \dots \oplus x_n \qquad \text{y} \qquad \bigodot_{i=1}^{n} x_i = x_1 \odot x_2 \odot \dots \odot x_n$$
:::

::: teorema
Distributividad con el producto y la sumadist_xor_eng
$$a \cdot (b \oplus c) = (a \cdot b) \oplus (a \cdot c) \qquad \text{y} \qquad a + (b \odot c) = (a + b) \odot (a + c)$$
:::

### Tablas de Verdad Bivaluadas {#tablas-de-verdad-bivaluadas .unnumbered}

Resumen de las tablas de operación del álgebra de Boole para el caso de
dos elementos ($B=\{0,1\}$), transcritas al lenguaje ingenieril:

   $a$   $\overline{a}$
  ----- ----------------
   $0$        $1$
   $1$        $0$

   $a$   $b$   $a + b$   $a \cdot b$   $a \uparrow b$   $a \downarrow b$   $a \oplus b$   $a \odot b$
  ----- ----- --------- ------------- ---------------- ------------------ -------------- -------------
   $0$   $0$     $0$         $0$            $1$               $1$              $0$            $1$
   $0$   $1$     $1$         $0$            $1$               $0$              $1$            $0$
   $1$   $0$     $1$         $0$            $1$               $0$              $1$            $0$
   $1$   $1$     $1$         $1$            $0$               $0$              $0$            $1$

# Operadores NOR y NAND

1.  1.  1.  Operadores "nor" y "nand" que representaremos
            respectivamente como $$\downarrow$$y $$\uparrow$$.

            1.  Definición de "nor":
                $${x\downarrow y}{: =}{{\overline{x} \cdot \overline{y}} = \overline{x+y}}$$.

            2.  Definición de "nand":
                $${x\uparrow y}{: =}{{\overline{x} + \overline{y}} = \overline{x\cdot y}}$$.

        2.  No asociatividad en general de "nor" y de "nand". Dar algún
            ejemplo en $$B_{2}$$.

        3.  Cualquier expresión de las que hasta ahora se ha podido
            utilizar es expresable con solo funciones "nand" y con solo
            funciones "nor".

            1.  "NOR":

                1.  $${{x + y} = {({x\downarrow y})}}\downarrow{({x\downarrow y})}$$

                2.  $${x \cdot y} = {({{({x\downarrow x})}}\downarrow{({y\downarrow y})})}$$

                3.  $$\overline{x} = {x\downarrow x}$$

            2.  "NAND":

                1.  $${{x \cdot y} = {({x\uparrow y})}}\uparrow{({x\uparrow y})}$$

                2.  $${{x + y} = {({x\uparrow x})}}\uparrow{({y\uparrow y})}$$

                3.  $$\overline{x} = {x\uparrow x}$$

        4.  Ahora podemos establecer el álgebra de Boole en solo función
            de operadores "nor" o sólo de operadores "nand". Los
            postulados de Huntington se establecieron de esta manera,
            aunque con una propiedad que acortaba la longitud total del
            sistema de axiomas. Actualmente se han desarrollado en
            formas cada vez más cortas mediante el postulado de Robinson
            y los de Wolfram más recientemente. (La legibilidad de estos
            sistemas queda definitivamente aniquilada, ya que el sistema
            de pruebas es por lo general un software probador de
            teoremas automático).

        5.  Extensión de la dualidad: solo hay que añadir que hay que
            intercambiar todos los operadores "nor" por "nand" y
            viceversa, además de las sustituciones ya enunciadas en
            18.1.

        6.  Nuevos operadores "exor" y "exnor".

            1.  Definición del operador "exor":
                $${x \oplus y}{: =}{{{({x \cdot \bar{y}})} + {({\bar{x} \cdot y})}} = {{({x + y})} \cdot {({\bar{x} + \bar{y}})}}}$$

            2.  Definición del operador "exnor":
                $${x \odot y}{: =}{{{({x + \bar{y}})} \cdot {({\bar{x} + y})}} = {{({x \cdot y})} + {({\bar{x} \cdot \bar{y}})}}}$$

        7.  Nueva extensión del teorema de dualidad: solo hay que
            intercambiar "exor" por "ex­nor " y viceversa, además de
            todos los intercambios que anteriormente se han des­crito en
            22.

        8.  Propiedad de elemento inverso (el inverso de cada elemento
            existe y es él mismo):

            1.  Para la operación "exor" :
                $$\forall{x \in B}x \oplus {x = 0}$$

                1.  Prueba:

                2.  $$x \oplus {{{x = {{({x \cdot \overline{x}})} + {({\overline{x} \cdot x})}}} = {0 + 0}} = 0}$$

            2.  Para la operación "exnor":
                $$\forall{x \in B}x \odot {x = 1}$$

                1.  Prueba:

                2.  $$x \odot {{{x = {{({x + \overline{x}})} \cdot {({\overline{x} + x})}}} = {1 \cdot 1}} = 1}$$

        9.  Valor para un elemento operado con su complementario:

            1.  $$\forall{x \in B}x \oplus {\bar{x} = 1}$$

                1.  Prueba:

                2.  $$x \oplus {{{{\bar{x} = {{({x \cdot \overline{\overline{x}}})} + {({\overline{x} \cdot \overline{x}})}}} = {({{({x \cdot x})} + \overline{x}})}} = {x + \overline{x}}} = 1}$$

            2.  $$\forall{x \in B}x \odot {\bar{x} = 0}$$

                1.  Prueba:

                2.  $$x \odot {{{{\overline{x} = {{({x + \overline{\overline{x}}})} \cdot {({\overline{x} + \overline{x}})}}} = {({{({x + x})} \cdot \overline{x}})}} = {x \cdot \overline{x}}} = 0}$$

        10. Más valores de estas operaciones:

            1.  $$\forall{x \in B}x \oplus {1 = \bar{x}}$$

                1.  Prueba:

                2.  $$x \oplus {{{{1 = {{({\overline{x} \cdot 1})} + {({x \cdot \overline{1}})}}} = {\overline{x} + {({x \cdot 0})}}} = {\overline{x} + 0}} = \overline{x}}$$

            2.  $$\forall{x \in B}x \odot {0 = \bar{x}}$$

                1.  Prueba:

                2.  $$x \odot {{{{0 = {{({\overline{x} + 0})} \cdot {({x + \overline{0}})}}} = {\overline{x} \cdot {({x + 1})}}} = {\overline{x} + 1}} = \overline{x}}$$

        11. Elementos neutros:

            1.  $$\forall{x \in B}x \oplus {0 = x}$$

                1.  Prueba:

                2.  $$x \oplus {{{0 = {{({\overline{x} \cdot 0})} + {({x \cdot \overline{0}})}}} = {0 + {({x \cdot 1})}}} = x}$$

            2.  $$\forall{x \in B}x \odot {1 = x}$$

                1.  Prueba:

                2.  $$x \odot {{{1 = {{({\overline{x} + 1})} \cdot {({x + \overline{1}})}}} = {1 \cdot {({x + 0})}}} = x}$$

        12. Una propiedad de simetría:

            1.  $$\forall a,{b \in B}a \oplus {b = \bar{a}} \oplus \bar{b}$$

                1.  Prueba:

                2.  $$a \oplus {{{b = {{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}}} = {{\lbrack{{({\overline{a} \cdot b})} + a}\rbrack} \cdot {\lbrack{{({\overline{a} \cdot b})} + \overline{b}}\rbrack}}} = {{\lbrack{a + b}\rbrack} \cdot {\lbrack{\overline{a} + \overline{b}}\rbrack}}}$$

                3.  $$\overline{a} \oplus {{{{\overline{b} = {{\lbrack{\overline{a} + \overline{b}}\rbrack} \cdot {\lbrack{\overline{\overline{a}} + \overline{\overline{b}}}\rbrack}}} = {{\lbrack{\overline{a} + \overline{b}}\rbrack} \cdot {\lbrack{a + b}\rbrack}}} = {{\lbrack{a + b}\rbrack} \cdot {\lbrack{\overline{a} + \overline{b}}\rbrack}}} = a} \oplus b$$

            2.  $$\forall a,{b \in B}a \odot {b = \bar{a}} \odot \bar{b}$$

                1.  Prueba:

                2.  $$a \odot {{{b = {{({\overline{a} + b})} \cdot {({a + \overline{b}})}}} = {{\lbrack{{({\overline{a} + b})} \cdot a}\rbrack} + {\lbrack{{({\overline{a} + b})} \cdot \overline{b}}\rbrack}}} = {{\lbrack{a \cdot b}\rbrack} + {\lbrack{\overline{a} \cdot \overline{b}}\rbrack}}}$$

                3.  $$\overline{a} \odot {{{{\overline{b} = {{\lbrack{\overline{a} \cdot \overline{b}}\rbrack} + {\lbrack{\overline{\overline{a}} \cdot \overline{\overline{b}}}\rbrack}}} = {{\lbrack{\overline{a} \cdot \overline{b}}\rbrack} + {\lbrack{a \cdot b}\rbrack}}} = {{\lbrack{a \cdot b}\rbrack} + {\lbrack{\overline{a} \cdot \overline{b}}\rbrack}}} = a} \odot b$$

        13. Los operadores negados "nexor" y "nexnor" coinciden
            respectivamente con "exnor" y "exor" (y así no se producen
            nuevos operadores):

            1.  $$\forall a,{b \in B}{{\bar{a\oplus b} \equiv \overline{a\oplus b}} = \overline{a}} \oplus {b = a} \oplus {\overline{b} = a} \odot b$$

            2.  $$\forall a,{b \in B}{{\bar{a\odot b} \equiv \overline{a\odot b}} = \overline{a}} \odot {b = a} \odot {\overline{b} = a} \oplus b$$

        14. Asociatividad de los nuevos operadores "exor" y "exnor":

            1.  $$\forall a,b,{c \in B}{({a \oplus b})} \oplus {c = a} \oplus {({b \oplus c})}$$

                1.  Prueba:

                2.  $${({a \oplus b})} \oplus {c =}$$

                3.  $${= {({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})}} \oplus {c =}$$

                4.  $${= {{({\overline{({{({\overline{a}\cdot b})}+{({a\cdot\overline{b}})}})} \cdot c})} + {({{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot \overline{c}})}}} =$$

                5.  $${= {{({\overline{({{({\overline{a}\cdot b})}+{({a\cdot\overline{b}})}})} \cdot c})} + {({{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot \overline{c}})}}} =$$

                6.  $${= {{{({{({\overline{({\overline{a}\cdot b})} \cdot \overline{({a\cdot\overline{b}})}})} \cdot c})} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                7.  $${= {{{({{({{({a + \overline{b}})} \cdot {({\overline{a} + b})}})} \cdot c})} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                8.  $${= {{{{({{a \cdot b} \cdot c})} + {({{\overline{a} \cdot \overline{b}} \cdot c})}} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                9.  $${= {{({a \cdot {({{({b \cdot c})} + {({\overline{b} \cdot \overline{c}})}})}})} + {({\overline{a} \cdot {({{({\overline{b} \cdot c})} + {({b + \overline{c}})}})}})}}} =$$

                10. $${= {{({a \cdot {({b \odot c})}})} + {({\overline{a} \cdot {({b \oplus c})}})}}} =$$

                11. $${= {{({a \cdot \overline{({b\oplus c})}})} + {({\overline{a} \cdot {({b \oplus c})}})}}} =$$

                12. $${= a} \oplus {({b \oplus c})}$$

            2.  $$\forall a,b,{c \in B}{({a \odot b})} \odot {c = a} \odot {({b \odot c})}$$

                1.  Prueba:

                2.  $${({a \odot b})} \odot {c =}$$

                3.  $${= {({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})}} \odot {c =}$$

                4.  $${= {{({\overline{({{({\overline{a}+b})}\cdot{({a+\overline{b}})}})} + c})} \cdot {({{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + \overline{c}})}}} =$$

                5.  $${= {{({\overline{({{({\overline{a}+b})}\cdot{({a+\overline{b}})}})} + c})} \cdot {({{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + \overline{c}})}}} =$$

                6.  $${= {{{({{({\overline{({\overline{a}+b})} + \overline{({a+\overline{b}})}})} + c})} \cdot {({{\overline{a} + b} + \overline{c}})}} \cdot {({{a + \overline{b}} + \overline{c}})}}} =$$

                7.  $${= {{{({{({{({a \cdot \overline{b}})} + {({\overline{a} \cdot b})}})} + c})} \cdot {({{\overline{a} + b} + \overline{c}})}} \cdot {({{a + \overline{b}} + \overline{c}})}}} =$$

                8.  $${= {{{{({{a \cdot b} \cdot c})} + {({{\overline{a} \cdot \overline{b}} \cdot c})}} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                9.  $${= {{({a \cdot {({{({b \cdot c})} + {({\overline{b} \cdot \overline{c}})}})}})} + {({\overline{a} \cdot {({{({\overline{b} \cdot c})} + {({b + \overline{c}})}})}})}}} =$$

                10. $${= {{({a + {({b \oplus c})}})} \cdot {({\overline{a} + {({b \odot c})}})}}} =$$

                11. $${= {{({a \cdot \overline{({b\oplus c})}})} + {({\overline{a} \cdot {({b \oplus c})}})}}} =$$

                12. $${= a} \odot {({b \odot c})}$$

        15. Distributividad de "$$\oplus$$" respecto del producto lógico
            "$$\cdot$$" y de "$$\odot$$" res­pecto de la suma lógica
            "$$+$$":

            1.  $$\forall x,y,{z \in B}{{x \cdot {({y \oplus z})}} = {({x \cdot y})}} \oplus {({x \cdot z})}$$

                1.  Prueba:

                2.  $${{x \cdot {({y \oplus z})}} = {({x \cdot y})}} \oplus {({x \cdot z})}$$

                3.  $${\lbrack\mathbf{A}\rbrack}{{{({x \cdot {({y \oplus z})}})} \cdot \overline{({{({x\cdot y})}\oplus{({x\cdot z})}})}} =}$$

                4.  $${= {{({x \cdot {({y \oplus z})}})} \cdot {({{({x \cdot y})} \odot {({x \cdot z})}})}}} =$$

                5.  $${= {{({x \cdot {({y \oplus z})}})} \cdot {({\overline{({x\cdot y})} \oplus {({x \cdot z})}})}}} =$$

                6.  $${= {{({x \cdot {({{({\overline{y} \cdot z})} + {({y \cdot \overline{z}})}})}})} \cdot {({{({{({x \cdot y})} \cdot {({x \cdot z})}})} + {({\overline{({x\cdot y})} \cdot \overline{({x\cdot z})}})}})}}} =$$

                7.  $${= {{{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({{x \cdot y} \cdot z})}} + {{{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({\overline{x} + \overline{y}})}} \cdot {({\overline{x} + \overline{z}})}}}} =$$

                8.  $${= {{{{({x\overline{y}z})} \cdot {({xyz})}} + {{({xy\overline{z}})} \cdot {({xyz})}}} + {{({{({x\overline{y}z})} + {({xy\overline{z}})}})} \cdot {({{\overline{x} + \overline{x}}{\overline{z} + \overline{x}}{\overline{y} + \overline{y}}\overline{z}})}}}} =$$

                9.  $${= {{0 + 0} + {{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({\overline{x} + {\overline{y} \cdot \overline{z}}})}}}} =$$

                10. $${= {{{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot \overline{x}} + {{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({\overline{y} \cdot \overline{z}})}}}} =$$

                11. $${= {{{{x \cdot {({{\overline{y} \cdot z} + {y \cdot \overline{z}}})}} \cdot \overline{x}} + {{({{x \cdot \overline{y}} \cdot z})} \cdot {({\overline{y} \cdot \overline{z}})}}} + {{({{x \cdot y} \cdot \overline{z}})} \cdot {({\overline{y} \cdot \overline{z}})}}}} =$$

                12. $${= {{0 + 0} + 0}} = 0$$

                13. $${\lbrack\mathbf{B}\rbrack}{{{({x \cdot {({y \oplus z})}})} + \overline{({{({x\cdot y})}\oplus{({x\cdot z})}})}} =}$$

                14. $${= {{({x \cdot {({y \oplus z})}})} + {({{({x \cdot y})} \odot {({x \cdot z})}})}}} =$$

                15. $${= {{({x \cdot {({y \oplus z})}})} + {({\overline{({x\cdot y})} \oplus {({x \cdot z})}})}}} =$$

                16. $${= {{({x \cdot {({{({\overline{y} \cdot z})} + {({y \cdot \overline{z}})}})}})} + {({{({{({x \cdot y})} \cdot {({x \cdot z})}})} + {({\overline{({x\cdot y})} \cdot \overline{({x\cdot z})}})}})}}} =$$

                17. $${= {{{{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}} + {({{x \cdot y} \cdot z})}} + {({{({\overline{x} + \overline{y}})} \cdot {({\overline{x} + \overline{z}})}})}}} =$$

                18. $${= {{{{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}} + {({{x \cdot y} \cdot z})}} + {({\overline{x} + {\overline{y} \cdot \overline{z}}})}}} =$$

                19. $${= {{{{{{x \cdot \overline{y}} \cdot z} + {{x \cdot y} \cdot \overline{z}}} + {{x \cdot y} \cdot z}} + \overline{x}} + {\overline{y} \cdot \overline{z}}}} =$$

                20. $${= {{{{{{{{{{x \cdot \overline{y}} \cdot z} + {{x \cdot y} \cdot \overline{z}}} + {{x \cdot y} \cdot z}} + {{\overline{x} \cdot y} \cdot z}} + {{\overline{x} \cdot y} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot z}} + {{x \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot \overline{z}}}} =$$

                21. $${= {{{{{{{{{x \cdot \overline{y}} \cdot z} + {{x \cdot y} \cdot \overline{z}}} + {{x \cdot y} \cdot z}} + {{x \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot y} \cdot z}} + {{\overline{x} \cdot y} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot z}}} =$$

                22. $${= {{x \cdot {({{{{\overline{y} \cdot z} + {y \cdot \overline{z}}} + {y \cdot z}} + {\overline{y} \cdot \overline{z}}})}} + {\overline{x} \cdot {({{{{y \cdot z} + {y \cdot \overline{z}}} + {\overline{y} \cdot \overline{z}}} + {\overline{y} \cdot z}})}}}} =$$

                23. $${= {{{{\overline{y} \cdot z} + {y \cdot \overline{z}}} + {y \cdot z}} + {\overline{y} \cdot \overline{z}}}} =$$

                24. $${= {{\overline{y} \cdot {({z + \overline{z}})}} + {y \cdot {({z + \overline{z}})}}}} =$$

                25. $${= {z + \overline{z}}} = 1$$

                26. $$\text{De}{\lbrack\mathbf{A}\rbrack}\text{y de}{\lbrack\mathbf{B}\rbrack}\text{se obtiene que}{\overline{({x\cdot{({y\oplus z})}})} = \overline{({{({x\cdot y})}\oplus{({x\cdot z})}})}}$$

                27. $$\text{Y de aquí, por la unicidad del complementario obtenemos}$$

                28. $${{x \cdot {({y \oplus z})}} = {({x \cdot y})}} \oplus {({x \cdot z})}$$

                Es seguro que la prueba anterior puede ser acortada
                drásticamente, así que si al­guno encuentra una forma
                (quizás más directa) la pondremos en su lugar.

            2.  $$\forall x,y,{z \in B}{{x + {({y \odot z})}} = {({x + y})}} \odot {({x + z})}$$Se
                prueba como en el caso anterior, sólo que cambiando los
                operadores duales, y las dos constantes $$\{{0,1}\}$$
                entre sí y obtenemos el resultado que hemos enunciado.

                1.  Prueba:

                2.  $${{x + {({y \odot z})}} = {({x + y})}} \odot {({x + z})}$$

                3.  $${\lbrack\mathbf{A}\rbrack}{{{({x + {({y \odot z})}})} + \overline{({{({x+y})}\odot{({x+z})}})}} =}$$

                4.  $${= {{({x + {({y \odot z})}})} + {({{({x + y})} \oplus {({x + z})}})}}} =$$

                5.  $${= {{({x + {({y \odot z})}})} + {({\overline{({x+y})} \odot {({x + z})}})}}} =$$

                6.  $${= {{({x + {({{({\overline{y} + z})} \cdot {({y + \overline{z}})}})}})} + {({{({{({x + y})} + {({x + z})}})} \cdot {({\overline{({x+y})} + \overline{({x+z})}})}})}}} =$$

                7.  $${= {{{{({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})} + {{({{x + y} + z})} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}}} + {({\overline{x} \cdot \overline{y}})}} + {({\overline{x} \cdot \overline{z}})}}} =$$

                8.  $$= {{{{({{x + \overline{y}} + z})} + {{({{x + y} + z})} \cdot {({{x + y} + \overline{z}})}}} + {{({{x + y} + z})} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}}} +}$$

                9.  $${+ {({{{{\overline{x} \cdot \overline{x}} + {\overline{z} \cdot \overline{x}}} + {\overline{y} \cdot \overline{y}}} + \overline{z}})}} =$$

                10. $${= {{{1 \cdot 1} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}} + {({{\overline{x} \cdot \overline{y}} + \overline{z}})}}} =$$

                11. $${= {{{({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})} + {\overline{x} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}}} + {({\overline{y} + \overline{z}})}}} =$$

                12. $${= {{{{x + {({{\overline{y} + {z \cdot y}} + \overline{z}})}} + {\overline{x} \cdot {({{x + \overline{y}} + z})}}} + {{({\overline{y} + \overline{z}})} \cdot {({{x + y} + \overline{z}})}}} + {({\overline{y} + \overline{z}})}}} =$$

                13. $${= {{1 \cdot 1} \cdot 1}} = 1$$

                14. $${\lbrack\mathbf{B}\rbrack}{{{({x + {({y \odot z})}})} \cdot \overline{({{({x+y})}\odot{({x+z})}})}} =}$$

                15. $${= {{({x + {({y \odot z})}})} \cdot {({{({x + y})} \oplus {({x + z})}})}}} =$$

                16. $${= {{({x + {({y \odot z})}})} \cdot {({\overline{({x+y})} \odot {({x + z})}})}}} =$$

                17. $${= {{({x + {({{({\overline{y} + z})} \cdot {({y + \overline{z}})}})}})} \cdot {({{({{({x + y})} + {({x + z})}})} \cdot {({\overline{({x+y})} + \overline{({x+z})}})}})}}} =$$

                18. $${= {{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot \left( {\left( {\overline{x} \cdot \overline{y}} \right) + \left( {\overline{x} \cdot \overline{z}} \right)} \right)}} =$$

                19. $${= {{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot {({\overline{x} \cdot {({\overline{y} + \overline{z}})}})}}} =$$

                20. $$= {{{{{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot {({{\overline{x} + y} + z})}} \cdot {({{\overline{x} + y} + \overline{z}})}} \cdot {({{\overline{x} + \overline{y}} + \overline{z}})}} \cdot}$$$${{{\cdot {({{\overline{x} + \overline{y}} + z})}} \cdot {({{x + \overline{y}} + \overline{z}})}} \cdot {({{\overline{x} + \overline{y}} + \overline{z}})}} =$$

                21. $$= {{{{{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot {({{x + \overline{y}} + \overline{z}})}} \cdot {({{\overline{x} + y} + z})}} \cdot {({{\overline{x} + y} + \overline{z}})}} \cdot}$$$${{\cdot {({{\overline{x} + \overline{y}} + \overline{z}})}} \cdot {({{\overline{x} + \overline{y}} + z})}} =$$

                22. $${= {{({x + {({{{{({\overline{y} + z})} \cdot {({y + \overline{z}})}} \cdot {({y + z})}} \cdot {({\overline{y} + \overline{z}})}})}})} \cdot {({\overline{x} + {({{{{({y + z})} \cdot {({y + \overline{z}})}} \cdot {({\overline{y} + \overline{z}})}} \cdot {({\overline{y} + z})}})}})}}} =$$

                23. $${= {{{{({\overline{y} + z})} \cdot {({y + \overline{z}})}} \cdot {({y + z})}} \cdot {({\overline{y} + \overline{z}})}}} =$$

                24. $${= {{({\overline{y} + {({z \cdot \overline{z}})}})} \cdot {({y + {({z \cdot \overline{z}})}})}}} =$$

                25. $${= {z \cdot \overline{z}}} = 0$$

                26. $$\text{De}{\lbrack\mathbf{A}\rbrack}\text{y de}{\lbrack\mathbf{B}\rbrack}\text{se obtiene que}{\overline{({x+{({y\odot z})}})} = \overline{({{({x+y})}\odot{({x+z})}})}}$$

                27. $$\text{Y de aquí, por la unicidad del complementario obtenemos}$$

                28. $${{x + {({y \odot z})}} = {({x + y})}} \odot {({x + z})}$$

        16. Estructuras de anillo conmutativo con elemento unidad (es
            claro desde todas las pro­piedades anteriormente
            demostradas):

            1.  La más normal sería:
                $$({B,{{\{ 0,1\}} \subseteq B},{0 \neq 1}, \oplus , \cdot})$$

            2.  Su forma dual es
                :$$({B,{{\{ 0,1\}} \subseteq B},{0 \neq 1}, \odot , +})$$

        17. Estructuras respectivas a 33 de bimódulo
            de$$({B^{n}, \oplus})$$sobre el anillo
            $$({B, \oplus , \cdot})$$ y el dual, de
            $$({B^{n}, \odot})$$sobre el anillo $$({B, \odot , +})$$.

# Álgebras de Boole finitas

1.  1.  A continuación hablaremos sobre como son en general las álgebras
        de Boole, funda­mentalmente las finitas, y veremos que
        efectivamente podemos llegar a teoremas que nos dicen de forma
        muy concreta cuales son estas álgebras de Boole. Vamos a ver
        for­mas de generarlas y cuestiones parecidas.

        1.  En el caso que el cardinal de $$B$$sea finito,
            $$2 \mid {({\# B})}$$. Para demostrarlo solo hay que darse
            cuenta que $${B = \cup_{x \in B}}{\{{x,\overline{x}}\}}$$,
            que
            $${({{x \neq {y \land \overline{x}}} \neq y})}\Rightarrow{({{{\{{x,\overline{x}}\}} \cap {\{{y,\overline{y}}\}}} = \varnothing})}$$
            y que $$\forall{x \in B}\#{{\{{x,\overline{x}}\}} = 2}$$ y
            así cuando$$B$$sea finito, su cardinal será un múlti­plo de
            2.

        2.  Definición:

            $$\forall x,{y \in B}{x \leq y}\Leftrightarrow{{x \cdot y} = x}\Leftrightarrow{{x + y} = y}$$

        3.  $$\left\langle {B, \leq} \right\rangle\text{es un}\mathit{orden}$$.

            1.  Reflexiva: $$\forall{x \in B}{x \leq x}$$

                1.  $$\forall{x \in B}{{x \cdot x} = x}$$

                2.  $$\forall{x \in B}{x \leq x}$$

            2.  Antisimétrica:
                $$\forall x,{y \in B}{{x \leq {y \land y}} \leq x}\Rightarrow{x = y}$$

                1.  $$x,{y \in B}{{x \leq {y \land y}} \leq x}$$

                2.  $$x,{y \in B}{{{x \cdot y} = {{y \land x} \cdot y}} = x}$$

                3.  $$x,{y \in B}{x = y}$$

            3.  Transitiva:
                $$\forall x,y,{z \in B}{{x \leq {y \land y}} \leq z}\Rightarrow{x \leq z}$$

                1.  $${x \leq {y \land y}} \leq z$$

                2.  $${{x \cdot y} = {{x \land y} \cdot z}} = y$$

                3.  $${{x \cdot y} \cdot z} = {x \cdot z}$$

                4.  $${x \cdot y} = {x \cdot z}$$

                5.  $$x = {x \cdot z}$$

                6.  $$x \leq z$$

        4.  Definición:$$\forall x,{y \in B}{x \geq y}\Leftrightarrow{{x \cdot y} = y}\Leftrightarrow{{x + y} = x}$$

        5.  $$\left\langle {B, \geq} \right\rangle\text{es un}\mathit{orden}$$.

            1.  Reflexiva: $$\forall{x \in B}{x \geq x}$$

                1.  $$\forall{x \in B}{{x + x} = x}$$

                2.  $$\forall{x \in B}{x \geq x}$$

            2.  Antisimétrica:
                $$\forall x,{y \in B}{{x \geq {y \land y}} \geq x}\Rightarrow{x = y}$$

                1.  $$x,{y \in B}{{x \geq {y \land y}} \geq x}$$

                2.  $$x,{y \in B}{{{x + y} = {{y \land x} + y}} = x}$$

                3.  $$x,{y \in B}{x = y}$$

            3.  Transitiva:
                $$\forall x,y,{z \in B}{{x \geq {y \land y}} \geq z}\Rightarrow{x \geq z}$$

                1.  $${x \geq {y \land y}} \geq z$$

                2.  $${{x + y} = {{x \land y} + z}} = y$$

                3.  $${{x + y} + z} = {x + z}$$

                4.  $${x + y} = {x + z}$$

                5.  $$x = {x + z}$$

                6.  $$x \geq z$$

        6.  Definición:$$\mathit{atom}{(x)}\overset{\text{def}}{\Leftrightarrow}{\left\lbrack {x \in (1,0)_{B}} \right\rbrack \land \left\lbrack {\forall{y \in (1,0)_{B}}\left( {\left( {{x \cdot y} = x} \right) \vee \left( {{x \cdot y} = 0} \right)} \right)} \right\rbrack}$$

        7.  $$\forall x,{y \in B}\mathit{atom}{{(x)} \land \mathit{atom}}{(y)}\Rightarrow{{x \cdot y} = 0}$$.

        8.  Definición:$$\mathit{hatom}{(x)}\overset{\text{def}}{\Leftrightarrow}{\left\lbrack {x \in \left( {B \smallsetminus {\{ 0,1\}}} \right)} \right\rbrack \land \left\lbrack {\forall{y \in \left( {B \smallsetminus {\{ 0,1\}}} \right)}\left( {\left( {{x + y} = x} \right) \vee \left( {{x + y} = 1} \right)} \right)} \right\rbrack}$$

        9.  $$\forall x,{y \in B}\mathit{hatom}{{(x)} \land \mathit{hatom}}{(y)}\Rightarrow{{x + y} = 1}$$

        10. Definición$${x \in B}\Rightarrow{\lbrack{x,0}\rbrack}_{B}{: = {\{{{y \in B} \mid {y \leq x}}\}}}$$

        11. $$\#{{\lbrack{x,0}\rbrack}_{B} = 1}\Leftrightarrow{{\lbrack{x,0}\rbrack}_{B} = {\{ 0\}}}\Leftrightarrow{x = 0}$$

        12. Definición$${x \in B}\Rightarrow{\lbrack{1,x}\rbrack}_{B}{: = {\{{{y \in B} \mid {y \geq x}}\}}}$$

        13. $$\#{{\lbrack{1,x}\rbrack}_{B} = 1}\Leftrightarrow{{\lbrack{1,x}\rbrack}_{B} = {\{ 1\}}}\Leftrightarrow{x = 1}$$

        14. Definición$$x,{y \in B}{x \geq y}\Rightarrow\left\lbrack {x,y} \right\rbrack_{B}{: = {\{{{z \in B} \mid {{y \leq {z \land x}} \geq z}}\}}}$$

        15. Definición$$x,{y \in B}{x \geq y}\Rightarrow\left\lbrack {x,y} \right)_{B}{: = {\{{{z \in B} \mid {{{y \leq {z \land x}} \geq {z \land z}} \neq y}}\}}}$$

        16. Definición$$x,{y \in B}{x \geq y}\Rightarrow\left( {x,y} \right\rbrack_{B}{: = {\{{{z \in B} \mid {{{y \leq {z \land x}} \geq {z \land z}} \neq x}}\}}}$$

        17. Definición$$x,{y \in B}{x \geq y}\Rightarrow\left( {x,y} \right)_{B}{: = {\{{{z \in B} \mid {{{{y \leq {z \land x}} \geq {z \land z}} \neq {x \land z}} \neq y}}\}}}$$

        18. $${x \in B}\Rightarrow{{{\lbrack{x,0}\rbrack}_{B} \cap {\lbrack{1,x}\rbrack}_{B}} = {\{ x\}}}$$

        19. $${x \in B}\Rightarrow{{{\lbrack{x,0}\rbrack}_{B} \cap {\lbrack{\overline{x},0}\rbrack}_{B}} = {\{ 0\}}}$$

        20. $${x \in B}\Rightarrow{{{\lbrack{1,x}\rbrack}_{B} \cap {\lbrack{1,\overline{x}}\rbrack}_{B}} = {\{ 1\}}}$$

        21. $$\forall{x \in B}\forall{y \in \left( {x,0} \right)_{B}}{{({{\lbrack{y,0}\rbrack}_{B} \subset {\lbrack{x,0}\rbrack}_{B}})} \land {({{\lbrack{y,0}\rbrack}_{B} \neq {\lbrack{x,0}\rbrack}_{B}})}}$$

        22. $$\forall{x \in B}\forall{y \in \left( {1,x} \right)_{B}}{{({{\lbrack{1,y}\rbrack}_{B} \subset {\lbrack{1,x}\rbrack}_{B}})} \land {({{\lbrack{1,y}\rbrack}_{B} \neq {\lbrack{1,x}\rbrack}_{B}})}}$$

        23. Definición$$\mathit{Atom}B{: = {\{{{x \in (1,0)_{B}} \mid \mathit{atom}{(x)}}\}}}$$

        24. Definición$$\mathit{Hatom}B{: = {\{{{x \in (1,0)_{B}} \mid \mathit{hatom}{(x)}}\}}}$$

        25. $$\mathit{Atom}{{(B_{2})} = \mathit{Hatom}}{{(B_{2})} = \varnothing}$$

        26. Definición
            $$\left\lbrack B \right){: = {\{{{A \subset B} \mid \exists{x \in B}{A = \left\lbrack {x,0} \right)_{B}}}\}}}$$

        27. $$\left\lbrack B \right) \neq \varnothing$$. Pues es un
            álgebra de cardinal mayor o igual que 2 y existe al menos
            $$\{ 1\}$$.

        28. $${\langle{\left\lbrack B \right), \supseteq}\rangle}\mathit{es}\mathit{un}\mathit{orden}$$.

        29. $$B\mathit{finito}\forall{P \subset \left\lbrack B \right)}{\langle{P, \supseteq}\rangle}\mathit{orden}\mathit{total}\Rightarrow\exists!{x \in \underset{X \in P}{\cap}}X\mathit{atom}(x)$$

            1.  Prueba:

            2.  $${\langle{P, \supseteq}\rangle}\mathit{es}\mathit{un}\mathit{orden}\mathit{total}$$

            3.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{{X \supset {Y \vee Y}} \supset X}$$

            4.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{\left( {\left( {Y \supset X} \right) \vee \left( {Y \supset X} \right)} \right) \land \left( {\left( {{Y \cap X} = X} \right) \vee \left( {{Y \cap X} = Y} \right)} \right)}$$

            5.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{\left( {\left( {{Y \cap X} = X} \right) \vee \left( {{Y \cap X} = Y} \right)} \right) \land \left( {{X \neq {{\{ 0\}} \land Y}} \neq {\{ 0\}}} \right)}$$

            6.  $$\forall X,{Y \in P}\left( {X \neq Y} \right)\Rightarrow\left( {{Y \cap X} \neq {\{ 0\}}} \right)$$

            7.  $$\underset{X \in P}{\cap}{X \neq {{\{ 0\}} \land \underset{X \in P}{\cap}}}{X \supset {\{ 0\}}}$$

            8.  $$\underset{Y \in P}{\cap}Y \supsetneq {\{ 0\}}$$

            9.  $$\underset{Y \in P}{\cap}{Y \supseteq {\{{0,x}\}}}$$

            10. $$\underset{Y \in P}{\cap}{Y \supseteq {\lbrack{x,0}\rbrack}_{B}}$$

            11. $$\underset{Y \in P}{\cap}{{Y \supseteq {\lbrack{x,0}\rbrack}_{B}} \supseteq {\{{0,x}\}}}$$

            12. $${\lbrack{x,0}\rbrack}_{B} \in P$$

            13. $$\exists{X \in P}\exists{x \in X}{\underset{Y \in P}{\cap}{Y = {\lbrack{x,0}\rbrack}_{B}}}$$

            14. $$\exists!{x \in B}{\underset{Y \in P}{\cap}{Y = {\lbrack{x,0}\rbrack}_{B}}}$$

            15. $$\exists{x \in {\underset{Y \in P}{\cap}Y{{\lbrack{x,0}\rbrack}_{B} = {\{{0,x}\}}}}}$$

            16. $$\exists{x \in {\underset{Y \in P}{\cap}Y\forall{X \in P}{{X \supseteq {\lbrack{x,0}\rbrack}_{B}} = {\{{0,x}\}}}}}$$

            17. $$\forall{P \subset \left\lbrack B \right)}{\langle{P, \supseteq}\rangle}\mathit{orden}\mathit{total}\Rightarrow\exists!{x \in \underset{X \in P}{\cap}}X\mathit{atom}(x)$$

        30. $$B\mathit{finito}\Rightarrow\mathit{Atom}{B \neq \varnothing}$$.
            Desde 57 es inmediato.

        31. Ahora vamos a construir una función inyectiva del álgebra de
            Boole de las partes de los átomos de B (si este es finito)
            en el álgebra de Boole B. Así cuando menos sa­bremos que
            podemos interpretar este álgebra de las partes de un
            conjunto de los áto­mos de B como un subálgebra de la que
            estamos estudiando.

            La función $$\varphi$$que vamos a definir va a quedar
            completamente definida en la fór­mula que sigue. Tendremos
            que mostrar que está bien definida, que es inyectiva, que
            $$\varphi{{({x \cup y})} = \varphi}{{(x)} + \varphi}{(y)}$$,
            esto es que respeta la suma booleana en $$B$$que viene como
            unión de conjuntos desde
            $$\wp\left( {\mathit{Atom}{(B)}} \right)$$, que
            $$\varphi{{({x \cap y})} = \varphi}{{(x)} \cdot \varphi}{(y)}$$,
            esto es que respeta el producto booleano en $$B$$que viene
            como intersección de conjun­tos desde
            $$\wp\left( {\mathit{Atom}{(B)}} \right)$$ , y aunque ya no
            sería necesario, también veremos que
            $$\varphi{\left( {\mathit{Atom}{{(B)} \smallsetminus x}} \right) = \overline{\varphi(x)}}$$
            . Así quedará clara la relación entre ambas álgebras.

            1.  $$\begin{matrix}
                        {n{: = \#}\left( {\mathit{Atom}B} \right)} \\
                        {{n \leq m}{: = \#}\left( B \right)} \\
                        {\left\lbrack {1,n} \right\rbrack_{\mathbb{N}}{: = {\{{1,2,\ldots,n}\}}}} \\
                        {\varphi:\wp{\left( {\mathit{Atom}\left( B \right)} \right)\rightarrow B}} \\
                        {{\varphi{(x)}}{: =}\begin{Bmatrix}
                        0 & \Leftarrow & {{x = \varnothing} = {\{\}}} \\
                        {x_{1}'} & \Leftarrow & {x = {\{{x_{1}'}\}}} \\
                        {{\sum\limits_{\substack{k \in I \\ I \subset {\lbrack{1,n}\rbrack}_{\mathbb{N}}}}x_{k}}'} & \Leftarrow & {x = {\{{{x_{i}'} \mid {{i \in I} \subset \left\lbrack {1,n} \right\rbrack_{\mathbb{N}}}}\}}} \\
                        {x_{1}{{' + \ldots} + x_{i - 1}}{' + x_{i}}{{' + \ldots} + x_{n}}'} & \Leftarrow & {{x = \mathit{Atom}}{{(B)} \smallsetminus {\{{x_{i}'}\}}}} \\
                        1 & \Leftarrow & {{x = \mathit{Atom}}{(B)}}
                        \end{Bmatrix}}
                        \end{matrix}$$.

        32. $$\#{B_{a} = \#}{B_{b} = 2}\Rightarrow{B_{a} \simeq B_{b}}$$.
            Con la misma $$\varphi$$ anterior.

        33. $$\#{B_{a} = \#}{B_{b} = 4}\Rightarrow{B_{a} \simeq B_{b}}$$.
            Con la misma $$\varphi$$ anterior.

        34. $$\#{B > 4}\Rightarrow\mathit{Atom}{B \cap \mathit{Hatom}}{B = \varnothing}$$.
            Lo mejor sería demostrar que cualquier cadena completa
            saturada de 1 a 0 tiene una longitud (número de elementos)
            siempre igual al $$\#\mathit{Atom}{(B)}$$. De ahí se sigue
            que si el cardinal es el dicho, tendríamos más de 3 niveles,
            diferenciándose siempre los átomos y los hiperátomos.

        35. Para cada uno de los cardinales de $$B$$, cuando son
            finitos, existe una estructura no solo de anillo conmutativo
            con unidad como en 34, sino también de cuerpo. La po­demos
            encontrar explícitamente en el álgebra de las partes de un
            conjunto finito. Sólo nos queda ver que $$\varphi$$es
            sobreyectivo. Tenemos que
            $$\varphi{\left( {\mathit{Atom}{(B)}} \right) = B}$$. Así
            $$\varphi$$pasa a ser un isomorfismo de álgebras de Boole:
            esto es, en lo que a la estructu­ra de álgebra de Boole se
            refiere, haciendo abstracción de las operaciones $${} + {}$$
            y $${} \cdot {}$$concretas y los elementos concretos,
            $${\langle{B,0,1, + , \cdot}\rangle} \simeq {\langle{\wp\left( {\mathit{Atom}{(B)}} \right),\varnothing,\mathit{Atom}\left( B \right), \cup , \cap}\rangle}$$.

        36. De 74 se deduce que si $$B$$es un conjunto finito,
            $$\exists{n \in \mathbb{N}}\#{B = 2^{\mathbf{\mathrm{n}}}}$$.

# Espacios vectoriales booleanos y Códigos de Hamming

1.  1.  1.  Estructuras respectivas a 35 de espacio vectorial
            de$$({B^{n}, \oplus})$$sobre el cuerpo
            $$({B, \oplus , \cdot})$$ y el dual de
            $$({B^{n}, \odot})$$sobre el cuerpo dual
            $$({B, \odot , +})$$. Éste último es el caso cuando
            $${B = B_{2}} = {\{ 0,1\}}$$. Esto tendrá utilidad inmediata
            en los códigos de Hamming.

        2.  Para calcular los inversos en los cuerpos finitos de
            cardinal $$2^{\mathbf{\mathrm{n}}}$$ correspondientes hay
            que re­solver algunas ecuaciones sobre igualdades
            polinómicas. El producto del cuerpo fi­nito asociado (en
            número de elementos) a nuestro álgebra de Boole no es en
            general igual al producto del ani­llo booleano asociado.
            Tiene que ver con los cuerpos de Galois
            $$\mathit{GF}{(2^{n})}$$. Estos cuerpos y los polinomios
            mencionados son de gran utilidad en teoría de codificación
            (no sólo para álgebras de Boole).

        3.  Existen formulas sencillas para poner la suma "$$+$$", el
            producto "$$\cdot$$" en fun­ción de las funciones
            "$$\oplus$$" y "$$\cdot$$", y de "$$\odot$$" y "$$+$$":

            1.  $${{a + b} = {({a \oplus b})}} \oplus {({a \cdot b})}$$

                1.  Prueba:

                2.  $${({a \oplus b})} \oplus {{({a \cdot b})} =}$$

                3.  $${= {({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})}} \oplus {{({a \cdot b})} =}$$

                4.  $${= {{\lbrack{\overline{({{({\overline{a}\cdot b})}+{({a\cdot\overline{b}})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot \overline{({a\cdot b})}}\rbrack}}} =$$

                5.  $${= {{\lbrack{{({\overline{({\overline{a}\cdot b})} \cdot \overline{({a\cdot\overline{b}})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot {({\overline{a} + \overline{b}})}}\rbrack}}} =$$

                6.  $${= {{\lbrack{{({{({a + \overline{b}})} \cdot {({\overline{a} + b})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot {({\overline{a} + \overline{b}})}}\rbrack}}} =$$

                7.  $${= {{\lbrack{({a \cdot b})}\rbrack} + {\lbrack{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})}\rbrack}}} =$$

                8.  $${= {{{({a \cdot b})} + {({\overline{a} \cdot b})}} + {({a \cdot \overline{b}})}}} =$$

                9.  $${= {{\lbrack{{({a \cdot b})} + {({\overline{a} \cdot b})}}\rbrack} + {\lbrack{{({a \cdot b})} + {({a \cdot \overline{b}})}}\rbrack}}} =$$

                10. $${= {{\lbrack b\rbrack} + {\lbrack a\rbrack}}} =$$

                11. $$= {a + b}$$

            2.  $${{a \cdot b} = {({a \odot b})}} \odot {({a + b})}$$

                1.  Prueba:

                2.  $${({a \odot b})} \odot {{({a + b})} =}$$

                3.  $${= {({{({\overline{a} + b})} \cdot {({a \cdot \overline{b}})}})}} \odot {{({a + b})} =}$$

                4.  $${= {{\lbrack{\overline{({{({\overline{a}+b})}\cdot{({a+\overline{b}})}})} + {({a + b})}}\rbrack} \cdot {\lbrack{{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + \overline{({a+b})}}\rbrack}}} =$$

                5.  $${= {{\lbrack{{({\overline{({\overline{a}+b})} + \overline{({a+\overline{b}})}})} + {({a + b})}}\rbrack} \cdot {\lbrack{{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + {({\overline{a} \cdot \overline{b}})}}\rbrack}}} =$$

                6.  $${= {{\lbrack{{({{({a + \overline{b}})} \cdot {({\overline{a} + b})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot {({\overline{a} + \overline{b}})}}\rbrack}}} =$$

                7.  $${= {{\lbrack{({a + b})}\rbrack} \cdot {\lbrack{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})}\rbrack}}} =$$

                8.  $${= {{{({a + b})} \cdot {({\overline{a} + b})}} \cdot {({a + \overline{b}})}}} =$$

                9.  $${= {{\lbrack{{({a + b})} \cdot {({\overline{a} + b})}}\rbrack} \cdot {\lbrack{{({a + b})} \cdot {({a + \overline{b}})}}\rbrack}}} =$$

                10. $${= {{\lbrack b\rbrack} \cdot {\lbrack a\rbrack}}} =$$

                11. $$= {a \cdot b}$$

        4.  Si un anillo $$({B,0,1, \oplus , \cdot})$$ es tal que
            $$\forall{x \in B}{{x \cdot x} = x}$$, define de manera
            unívoca un álgebra de Boole (la estructura de la que
            hablamos se llama un anillo de Boole). Esta proposición, con
            ser matemáticamente importante, la vemos aquí como sólo una
            curiosidad. En el anillo no exigimos que sea conmutativo. La
            conmutatividad de la suma está asegurada para todo anillo, y
            la del producto está asegurada con la con­dición de
            idempotencia impuesta a todos los elementos del anillo. La
            idempotencia de la suma también se deduce fácilmente de la
            idempotencia del producto. La suma lógica la establecemos
            $${{x + y} = x} \oplus y \oplus {({x \cdot y})}$$(como en
            40.1, solo que aquí no su­ponemos nada sobre álgebras de
            Boole), mientras que el producto lógico lo pone­mos como
            idéntico al producto del anillo (idénticamente a lo
            anteriormente dicho). Nota: es importante darse cuenta que
            este anillo tendrá siempre divisores de cero, esto es habrá
            para cada elemento otro, distintos ambos de cero, que al
            multiplicarse dan cero, lo que impide que este anillo de
            Boole sea un dominio de integridad y por lo tanto también
            impide que sea cuerpo. El complementario, siguiendo la misma
            tó­nica que en 40.1, se define como
            $${\overline{x} = x} \oplus 1$$. Por la idempotencia de la
            suma, la asociatividad de la suma y la existencia y unicidad
            de la suma tenemos que la doble negación es igual a la
            identidad. Sólo quedaría ver las distributividades. Cómo
            hasta ahora las demostraciones son cálculos que verifican la
            aserción. Así tenemos una forma de ir de cada álgebra de
            Boole a cada anillo de Boole, y un camino (exacta­mente el
            inverso), que nos llevaría de cada anillo de Boole a cada
            álgebra de Boole. Las álgebras de Boole y los anillos de
            Boole son categorías equivalentes. A los ca­minos los
            llamamos funtores. Daré solo un comienzo de estos teoremas:

            1.  \[Axioma R0\]
                $$\forall{\left( {x,y} \right) \in {B \times B}}\exists\mathtt{\mathrm{!}}{z \in B}x \oplus {y = z}$$

            2.  \[Axioma R1\]
                $$\forall x,y,{z \in B}\left( {x \oplus y} \right) \oplus {z = x} \oplus \left( {y \oplus z} \right)$$

            3.  \[Axioma R2\]
                $$\exists{0 \in B}\forall{x \in B}0 \oplus {x = x}$$

            4.  \[Axioma R3\]
                $$\forall{x \in B}\exists{y_{x} \in B}y_{x} \oplus {x = 0}$$

            5.  \[Axioma R4\]
                $$\forall x,{y \in B}\exists\mathtt{\mathrm{!}}{z \in B}{{x \cdot y} = z}$$

            6.  \[Axioma R5\]
                $$\forall x,y,{z \in B}{{\left( {x \cdot y} \right) \cdot z} = {x \cdot \left( {y \cdot z} \right)}}$$

            7.  \[Axioma R6\]
                $$\exists{1 \in B}\forall{x \in B}{{1 \cdot x} = x}$$

            8.  \[Axioma R7\]
                $$\exists 1{' \in B}\forall{x \in B}{x \cdot 1}{' = x}$$

            9.  \[Axioma R8\]
                $${\left\{ 0,1 \right\} \subseteq {B \land 0}} \neq 1$$

            10. \[Axioma R9\]
                $$\forall x,y,{z \in B}{{\left( {x \oplus y} \right) \cdot z} = \left( {x \cdot z} \right)} \oplus \left( {y \cdot z} \right)$$

            11. \[Axioma
                R10\]$$\forall x,y,{z \in B}{{x \cdot \left( {y \oplus z} \right)} = \left( {x \cdot y} \right)} \oplus \left( {x \cdot z} \right)$$

            12. \[Axioma BR\]$$\forall{x \in B}{{x \cdot x} = x}$$

            13. $$\left\lbrack {{Lema}1} \right\rbrack\forall x,{y_{x} \in B}\left\lbrack {\left( {y_{x} \oplus x} \right) = 0} \right\rbrack\Rightarrow\left\lbrack {\left( {x \oplus y_{x}} \right) \oplus {\left( {x \oplus y_{x}} \right) = \left( {x \oplus y_{x}} \right)}} \right\rbrack$$

                1.  Prueba:

                2.  $$\left( {x \oplus y_{x}} \right) \oplus {\left( {x \oplus y_{x}} \right) =}$$

                3.  $${= \left( {x \oplus \left( {y_{x} \oplus \left( {x \oplus y_{x}} \right)} \right)} \right)} =$$

                4.  $${= \left( {x \oplus \left( {\left( {y_{x} \oplus x} \right) \oplus y_{x}} \right)} \right)} =$$

                5.  $${= \left( {x \oplus \left( {0 \oplus y_{x}} \right)} \right)} =$$

                6.  $$= \left( {x \oplus y_{x}} \right)$$

            14. $$\left\lbrack {{Lema}2} \right\rbrack\forall x,{y_{x} \in B}{\left( {y_{x} \oplus x} \right) = 0}\Rightarrow{\left( {x \oplus y_{x}} \right) = 0}$$

                1.  Prueba:

                2.  $$\forall x,{y_{x} \in B}\exists{u_{x + y_{x}} \in B}{{u_{x + y_{x}} \oplus \left( {x \oplus y_{x}} \right)} = 0}$$

                3.  $$\left( {u_{x \oplus y_{x}} \oplus \left( {x \oplus y_{x}} \right)} \right) \oplus {\left( {x \oplus y_{x}} \right) = 0} \oplus \left( {x \oplus y_{x}} \right)$$

                4.  $$u_{x \oplus y_{x}} \oplus {\left( {\left( {x \oplus y_{x}} \right) \oplus \left( {x \oplus y_{x}} \right)} \right) = \left( {x \oplus y_{x}} \right)}$$

                5.  $$u_{x \oplus y_{x}} \oplus {\left( {x \oplus y_{x}} \right) = \left( {x \oplus y_{x}} \right)}$$

                6.  $$0 = \left( {x \oplus y_{x}} \right)$$

            15. $$\left\lbrack {{Lema}3} \right\rbrack\forall{x \in B}0 \oplus {x = x}$$

                1.  Prueba:

                2.  $$\forall{x \in B}0 \oplus {x =}$$

                3.  $$\forall{x \in B}\exists{y_{x} \in B}{= \left( {x \oplus y_{x}} \right)} \oplus {x =}$$

                4.  $$\forall{x \in B}\exists{y_{x} \in B}{= x} \oplus {\left( {y_{x} \oplus x} \right) =}$$

                5.  $$\forall{x \in B}{= x} \oplus {0 = 0}$$

            16. $$\left\lbrack {{Lema}4} \right\rbrack\forall{e \in B}\left( {\forall{x \in B}x \oplus {e = x}} \right)\Rightarrow\left( {e = 0} \right)$$

                1.  Prueba:

                2.  $$\forall{x \in B}x \oplus {e = x}$$

                3.  $$\forall{x \in B}\exists{y_{x} \in B}y_{x} \oplus {x = 0}$$

                4.  $$\forall{x \in B}\exists{y_{x} \in B}y_{r} \oplus {\left( {x \oplus e} \right) = y_{r}} \oplus x$$

                5.  $$\forall{x \in B}\exists{y_{x} \in B}y_{r} \oplus {\left( {x \oplus e} \right) = 0}$$

                6.  $$\forall{x \in B}\exists{y_{x} \in B}\left( {y_{r} \oplus x} \right) \oplus {e = y_{r}} \oplus {x = 0}$$

                7.  $$\forall{x \in B}\left( {y_{r} \oplus x} \right) \oplus {e = 0}$$

                8.  $$\forall{x \in B}0 \oplus {e = 0}$$

                9.  $$\forall{x \in B}{e = 0}$$

            17. $$\left\lbrack {{Lema}5} \right\rbrack\forall{x \in B}\forall y_{x},{z_{x} \in B}\left\lbrack {{{x + y_{r}} = {{0 \land x} + z_{r}}} = 0} \right\rbrack\Rightarrow\left\lbrack {y_{x} = z_{r}} \right\rbrack$$

                1.  Prueba:

                2.  $$y_{r} \oplus {\left( {x \oplus z_{r}} \right) = y_{r}} \oplus 0$$

                3.  $$\left( {y_{r} \oplus x} \right) \oplus {z_{r} = y_{r}}$$

                4.  $$0 \oplus {z_{r} = y_{r}}$$

                5.  $$z_{r} = y_{r}$$

            18. $${\lbrack{{Notación}1}\rbrack}{{{y_{x} + x} = {{0 \vee x} + y_{x}}} = 0}\Rightarrow\left( {- x} \right){: = y_{r}}$$

                1.  Prueba:

                2.  $${{{x + {({\overline{x} \cdot y})}} = {{({x + \overline{x}})} \cdot {({x + y})}}} = {1 \cdot {({x + y})}}} = {x + y}$$

                3.  $$\forall x,{y \in B}{{x \cdot {({\overline{x} + y})}} = {x \cdot y}}$$

            19. $$\left\lbrack {{Lema}6} \right\rbrack\forall x,y,{z \in B}\left\lbrack {x \oplus {y = x} \oplus z} \right\rbrack\Rightarrow\left\lbrack {y = z} \right\rbrack$$

                1.  Prueba:

                2.  $$x \oplus {y_{r} = {0 \land x}} \oplus {z_{r} = 0}$$

                3.  $${({- x})} \oplus {{({x \oplus y})} = {({- x})}} \oplus {({x \oplus z})}$$

                4.  $$\left( {{({- x})} \oplus x} \right) \oplus {y = \left( {{({- x})} \oplus x} \right)} \oplus z$$

                5.  $$0 \oplus {y = 0} \oplus z$$

                6.  $$y = z$$

            20. $$\left\lbrack {{Lema}7} \right\rbrack\forall x,y,{z \in B}\left\lbrack {{y + x} = {z + x}} \right\rbrack\Rightarrow\left\lbrack {y = z} \right\rbrack$$

                1.  1.  1.  Prueba:

                        2.  $$y \oplus {x = z} \oplus x$$

                        3.  $${({- x})} \oplus {{({x \oplus y})} = {({- x})}} \oplus {({x \oplus z})}$$

                        4.  $$\left( {{({- x})} \oplus x} \right) \oplus {y = \left( {{({- x})} \oplus x} \right)} \oplus z$$

                        5.  $$y \oplus {0 = z} \oplus 0$$

                        6.  $$y = z$$

            21. $$\left\lbrack {{Lema}8} \right\rbrack\forall x,{y \in B}\exists\mathtt{\mathrm{!}}{z \in B}x \oplus {z = y}$$

                1.  Prueba:

                2.  $$z{: = \left( {- x} \right)} \oplus y$$

                3.  $$x \oplus {z = x} \oplus \left( {\left( {- x} \right) \oplus y} \right)$$

                4.  $$x \oplus {z = \left( {x \oplus \left( {- x} \right)} \right)} \oplus y$$

                5.  $$x \oplus {z = 0} \oplus y$$

                6.  $$x \oplus {z = y}$$

            22. $$\left\lbrack {{Lema}9} \right\rbrack\forall x,{y \in B}\exists\mathtt{\mathrm{!}}{z \in B}z \oplus {x = y}$$

                1.  Prueba:

                2.  $$z{: = y} \oplus \left( {- x} \right)$$

                3.  $$z \oplus {x = \left( {y \oplus \left( {- x} \right)} \right)} \oplus x$$

                4.  $$z \oplus {x = y} \oplus \left( {\left( {- x} \right) \oplus x} \right)$$

                5.  $$z \oplus {x = y} \oplus 0$$

                6.  $$z \oplus {x = y}$$

            23. $$\left\lbrack {{Lema}10} \right\rbrack\forall{x \in B}{\left( {- \left( {- x} \right)} \right) = x}$$

                1.  Prueba:

                2.  $$x \oplus {\left( {- x} \right) = 0}$$

                3.  $$\left( {- x} \right) \oplus {x = 0}$$

                4.  $$x \oplus {\left( {- x} \right) = 0}$$

                5.  $$x = \left( {- \left( {- x} \right)} \right)$$

            24. $$\left\lbrack {{Lema}11} \right\rbrack{\left( {- 0} \right) = 0}$$

                1.  Prueba:

                2.  $$\left( {- 0} \right) \oplus {0 = 0}$$

                3.  $$\left( {- 0} \right) \oplus {0 = \left( {- 0} \right)}$$

                4.  $$0 = \left( {- 0} \right)$$

            25. $$\left\lbrack {{Lema}12} \right\rbrack\forall{x \in B}{{0 \cdot x} = 0}$$

                1.  Prueba:

                2.  $$x \oplus {\left( {0 \cdot x} \right) =}$$

                3.  $${= \left( {1 \cdot x} \right)} \oplus {\left( {0 \cdot x} \right) =}$$

                4.  $${= {\left( {1 \oplus 0} \right) \cdot x}} =$$

                5.  $${= {1 \cdot x}} =$$

                6.  $$= x$$

                7.  $$x \oplus {{\left( {0 \cdot x} \right) = x} = x} \oplus 0$$

                8.  $$\left( {0 \cdot x} \right) = 0$$

            26. $$\left\lbrack {{Lema}13} \right\rbrack\forall{x \in B}{{x \cdot 0} = 0}$$

                1.  Prueba:

                2.  $$\left( {x \cdot 0} \right) \oplus {x =}$$

                3.  $${= \left( {x \cdot 0} \right)} \oplus {\left( {x \cdot 1} \right) =}$$

                4.  $${= {x \cdot \left( {0 \oplus 1} \right)}} =$$

                5.  $${= {x \cdot 1}} =$$

                6.  $$= x$$

                7.  $$\left( {x \cdot 0} \right) \oplus {{0 = x} = 0} \oplus x$$

                8.  $$\left( {x \cdot 0} \right) = 0$$

            27. $$\left\lbrack {{Lema}14} \right\rbrack\forall x,{y \in B}{\left( {- \left( {x \cdot y} \right)} \right) = {\left( {- x} \right) \cdot y}}$$

                1.  Prueba:

                2.  $$\left( {x \cdot y} \right) \oplus {\left( {\left( {- x} \right) \cdot y} \right) =}$$

                3.  $${\left( {(x) \oplus \left( {- x} \right)} \right) \cdot y} =$$

                4.  $${= {0 \cdot y}} =$$

                5.  $$= 0$$

            28. $$\left\lbrack {{Lema}15} \right\rbrack\forall x,{y \in B}{\left( {- \left( {x \cdot y} \right)} \right) = {x \cdot \left( {- y} \right)}}$$

                1.  Prueba:

                2.  $$\left( {x \cdot y} \right) \oplus {\left( {x \cdot \left( {- y} \right)} \right) =}$$

                3.  $${= {x \cdot \left( {y \oplus \left( {- y} \right)} \right)}} =$$

                4.  $${= {x \cdot 0}} =$$

                5.  $$= 0$$

            29. $${\lbrack{{Lema}16}\rbrack}\forall x,{y \in B}{{x \cdot y} = {\left( {- x} \right) \cdot \left( {- y} \right)}}$$

                1.  Prueba:

                2.  $$\left( {- \left( {x \cdot y} \right)} \right) \oplus {\left( {\left( {- x} \right) \cdot \left( {- y} \right)} \right) =}$$

                3.  $${= \left( {\left( {- x} \right) \cdot y} \right)} \oplus {\left( {\left( {- x} \right) \cdot \left( {- y} \right)} \right) =}$$

                4.  $${= {\left( {- x} \right) \cdot \left( {y \oplus \left( {- y} \right)} \right)}} =$$

                5.  $${= \left( {- \left( {x \cdot 0} \right)} \right)} =$$

                6.  $${= \left( {- 0} \right)} =$$

                7.  $$= 0$$

            30. $$\left\lbrack {{Lema}17} \right\rbrack\forall{x \in B}{{\left( {- 1} \right) \cdot x} = \left( {- x} \right)}$$

                1.  Prueba:

                2.  $$\left( {\left( {- 1} \right) \cdot x} \right) \oplus {x =}$$

                3.  $${= \left( {\left( {- 1} \right) \cdot x} \right)} \oplus {\left( {1 \cdot x} \right) =}$$

                4.  $${= {\left( {\left( {- 1} \right) \oplus 1} \right) \cdot x}} =$$

                5.  $${= {0 \cdot x}} =$$

                6.  $$= 0$$

            31. $$\left\lbrack {{Lema}18} \right\rbrack\forall{x \in B}1{' = 1}$$

                1.  Prueba:

                2.  $$\left\{ {\left\lbrack {{Axioma}{BR6}} \right\rbrack \land \left\{ {x{: = 1}'} \right\}} \right\}\Rightarrow\left\{ {{1 \cdot 1}{' = 1}'} \right\}$$

                3.  $$\left\{ {\left\lbrack {{Axioma}{BR7}} \right\rbrack \land \left\{ {x{: = 1}} \right\}} \right\}\Rightarrow\left\{ {{1 \cdot 1}{' = 1}} \right\}$$

                4.  $$1{' = {1 \cdot 1}}{' = 1}$$

            32. $$\left\lbrack {{Lema}19} \right\rbrack\forall{x \in B}{{x \cdot 1} = x}$$

            33. $${\lbrack{{Notación}1}\rbrack}\text{En adelante no usaremos}1'\text{sino solamente}1\text{.}$$

            34. $${\lbrack{{Lema}20}\rbrack}\forall{x \in B}{{x \cdot \left( {- 1} \right)} = \left( {- x} \right)}$$

                1.  Prueba:

                2.  $${x \cdot \left( {- 1} \right)} =$$

                3.  $${= \left( {- \left( {x \cdot 1} \right)} \right)} =$$

                4.  $$= \left( {- x} \right)$$

            35. $${\lbrack{{Lema}21}\rbrack}\forall{e \in B}\left( {\left( {\forall{x \in B}{{e \cdot x} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

                1.  Prueba:

                2.  $$\left( {\left( {\forall{x \in B}{{e \cdot x} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

                3.  $$\left( {x{: = 1}} \right)\left( {{e \cdot 1} = 1} \right)$$

                4.  $${e \cdot 1} = e$$

                5.  $$e = 1$$

            36. $${\lbrack{{Lema}22}\rbrack}\forall{e \in B}\left( {\left( {\forall{x \in B}{{x \cdot e} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

                1.  Prueba:

                2.  $$\left( {\left( {\forall{x \in B}{{x \cdot e} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

                3.  $$\left( {x{: = 1}} \right)$$

                4.  $${1 \cdot e} = 1$$

                5.  $${1 \cdot e} = {e \cdot 1}$$

                6.  $${e \cdot 1} = e$$

                7.  $$1 = e$$

            37. $${\lbrack{{Lema}23}\rbrack}\forall x,{y \in B}{\left( {- \left( {x \oplus y} \right)} \right) = \left( {- y} \right)} \oplus \left( {- x} \right)$$

                1.  Prueba:

                2.  $$\left( {x \oplus y} \right) \oplus {\left( {\left( {- y} \right) \oplus \left( {- x} \right)} \right) =}$$

                3.  $${= \left( {x \oplus \left( {\left( {y \oplus \left( {- y} \right)} \right) \oplus \left( {- x} \right)} \right)} \right)} =$$

                4.  $${= \left( {x \oplus \left( {0 \oplus \left( {- x} \right)} \right)} \right)} =$$

                5.  $${= \left( {x \oplus \left( {- x} \right)} \right)} =$$

                6.  $$= 0$$

            Esta fórmula que acabamos de exponer es la fórmula universal
            para el inverso en cualquier grupo, o in­cluso, para
            cualquier operación con neutro asociativa, siempre que
            existan los inversos, tanto el total como los individuales.

            1.  $${\lbrack{{Teorema}1}\rbrack}\forall x,{y \in B}x \oplus {y = y} \oplus x$$

                1.  Prueba:

                2.  $$\left( {- \left( {x \oplus y} \right)} \right) =$$

                3.  $${= {\left( {- 1} \right) \cdot \left( {x \oplus y} \right)}} =$$

                4.  $${= \left( {\left( {- 1} \right) \cdot x} \right)} \oplus {\left( {\left( {- 1} \right) \cdot y} \right) =}$$

                5.  $${= \left( {- x} \right)} \oplus \left( {- y} \right)$$

                6.  $$= \left( {- \left( {y \oplus x} \right)} \right)$$

                7.  $${- \left( {x \oplus y} \right)} = {- \left( {y \oplus x} \right)}$$

                8.  $$\left( {{- \left( {x \oplus y} \right)} = {- \left( {y \oplus x} \right)}} \right)\Rightarrow\left( {x \oplus {y = y} \oplus x} \right)$$

                9.  $$x \oplus {y = y} \oplus x$$

            El grupo aditivo de un anillo con unidad multiplicativa por
            ambos lados es siempre un grupo abeliano.

            1.  $${\lbrack{{Teorema}2}\rbrack}\forall{x \in B}x \oplus {x = 0}$$

                1.  Prueba:

                2.  $${0 = x} \oplus \left( {- x} \right)$$

                3.  $${0 = x} \oplus \left( {\left( {- x} \right) \cdot \left( {- x} \right)} \right)$$

                4.  $${0 = x} \oplus \left( {x \cdot x} \right)$$

                5.  $${0 = x} \oplus x$$

            En el grupo aditivo de un anillo booleano $$B$$ es siempre
            $$\left( {- x} \right) = x$$.

            1.  $${\lbrack{{Notación}2}\rbrack}\forall{x \in B}\overline{x}{: = x} \oplus 1$$

            2.  $${\lbrack{{Teorema}3}\rbrack}\forall{x \in B}{{x \cdot \overline{x}} = 0}$$

                1.  Prueba:

                2.  $${x \cdot \overline{x}} =$$

                3.  $${= {x \cdot \left( {x \oplus 1} \right)}} =$$

                4.  $${= {x^{2} \oplus {x \cdot 1}}} =$$

                5.  $${= {x \oplus x}} =$$

                6.  $$= 0$$

            3.  $${\lbrack{{Notación}3}\rbrack}\forall x,{y \in B}{x + y}{: = \left( {x \oplus y} \right)} \oplus \left( {x \cdot y} \right)$$

            4.  $${\lbrack{{Teorema}3}\rbrack}\forall x,{y \in B}{{x \cdot y} = {y \cdot x}}$$

                1.  Prueba:

                2.  $${\lbrack A\rbrack}{{\left( {x + y} \right)^{2} = {{{x^{2} + {x \cdot y}} + {y \cdot x}} + y^{2}}} = {{{x + {x \cdot y}} + {y \cdot x}} + y}}$$

                3.  $${\lbrack B\rbrack}{\left( {x + y} \right)^{2} = {x + y}}$$

                4.  $$\mathit{De}{\lbrack A\rbrack}y{\lbrack B\rbrack}:$$

                5.  $${x + y} = {{{x + {x \cdot y}} + {y \cdot x}} + y}$$

                6.  $$0 = {{x \cdot y} + {y \cdot x}}$$

                7.  $${x \cdot y} = {{- y} \cdot x}$$

                8.  $${x \cdot y} = {y \cdot x}$$

            La operación multiplicativa de un anillo de Boole $$B$$ es
            siempre abeliana. Un anillo de Boole es una subcategoría de
            la categoría de los anillos conmutativos.

            1.  $${\lbrack{{Teorema}4}\rbrack}\forall{x \in B}{{x \cdot \overline{x}} = 0}$$

                1.  Prueba:

                2.  $${x \cdot \overline{x}} =$$

                3.  $${= {x \cdot \left( {x \oplus 1} \right)}} =$$

                4.  $${= {x^{2} \oplus {x \cdot 1}}} =$$

                5.  $${= {x \oplus x}} =$$

                6.  $$= 0$$

            2.  $${\lbrack{{Teorema}5}\rbrack}\forall{x \in B}x \oplus {\overline{x} = 1}$$

                1.  Prueba:

                2.  $$x \oplus {\overline{x} =}$$

                3.  $${= {x \oplus \left( {x \oplus 1} \right)}} =$$

                4.  $${= \left( {x \oplus x} \right)} \oplus {1 =}$$

                5.  $${= {0 \oplus 1}} =$$

                6.  $$= 1$$

            3.  $${\lbrack{{Teorema}6}\rbrack}\forall{x \in B}{{x + \overline{x}} = 1}$$

                1.  Prueba:

                2.  $${x + \overline{x}} =$$

                3.  $${= \left( {x \oplus \overline{x} \oplus \left( {x \cdot \overline{x}} \right)} \right)} =$$

                4.  $${= {1 \oplus 0}} =$$

                5.  $$= 1$$

            4.  $${\lbrack{{Teorema}7}\rbrack}\forall{x \in B}{{x + x} = x}$$

                1.  Prueba:

                2.  $${x + x} =$$

                3.  $${= \left( {x \oplus x \oplus \left( {x \cdot x} \right)} \right)} =$$

                4.  $${= {0 \oplus x}} =$$

                5.  $$= x$$

            5.  $${\lbrack{{Teorema}8}\rbrack}\forall{x \in B}{{x + 0} = x}$$

                1.  Prueba:

                2.  $${x + x} =$$

                3.  $${= \left( {\left( {x \oplus 0} \right) \oplus \left( {x \cdot 0} \right)} \right)} =$$

                4.  $${= {x \oplus 0}} =$$

                5.  $$= x$$

            6.  $${\lbrack{{Teorema}9}\rbrack}\forall x,{y \in B}{{x + y} = {y + x}}$$

                1.  Prueba:

                2.  $${x + y} =$$

                3.  $${= \left( {x \oplus y} \right)} \oplus {\left( {x \cdot y} \right) =}$$

                4.  $${= \left( {y \oplus x} \right)} \oplus {\left( {y \cdot x} \right) =}$$

                5.  $$= {y + x}$$

            7.  $${\lbrack{{Teorema}10}\rbrack}\forall x,y,{z \in B}{{\left( {x + y} \right) + z} = {x + \left( {y + z} \right)}}$$

                1.  Prueba:

                2.  $${\lbrack A\rbrack}{{{({x + y})} + z} =}$$

                3.  $${{({{({x \oplus y})} \oplus {({x \cdot y})}})} + z} =$$

                4.  $${= {({{({x \oplus y})} \oplus {({x \cdot y})}})}} \oplus z \oplus {{({{({{({x \oplus y})} \oplus {({x \cdot y})}})} \cdot z})} =}$$

                5.  $${= x} \oplus y \oplus {({x \cdot y})} \oplus z \oplus {({x \cdot z})} \oplus {({y \cdot z})} \oplus {({{x \cdot y} \cdot z})}$$

                6.  $${\lbrack B\rbrack}{{x + {({y + z})}} =}$$

                7.  $${= x} \oplus {({y + z})} \oplus {{({x \cdot {({y + z})}})} =}$$

                8.  $${= x} \oplus {({y \oplus z \oplus {({y \cdot z})}})} \oplus {{({x \cdot {({y \oplus z \oplus {({y \cdot z})}})}})} =}$$

                9.  $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{obtenemos:}$$

                10. $${= x} \oplus y \oplus z \oplus {({y \cdot z})} \oplus {({x \cdot y})} \oplus {({x \cdot z})} \oplus {({{x \cdot y} \cdot z})}$$

                11. $${\left( {{({x + y})} + z} \right) + \left( {x + {({y + z})}} \right)} = 0$$

            8.  $${\lbrack{{Teorema}11}\rbrack}\forall x,y,{z \in B}{{{({x + y})} \cdot z} = {{({x \cdot z})} + {({y \cdot z})}}}$$

                1.  Prueba:

                2.  $${\lbrack A\rbrack}{{{({x + y})} \cdot z} =}$$

                3.  $${{({{({x \oplus y})} \oplus {({x \cdot y})}})} \cdot z} =$$

                4.  $${({{({x \cdot z})} \oplus {({y \cdot z})}})} \oplus {({{x \cdot y} \cdot z})}$$

                5.  $${\lbrack B\rbrack}{}{}{}{{{({x \cdot z})} + {({y \cdot z})}} =}$$

                6.  $${({{({x \cdot z})} \oplus {({y \cdot z})}})} \oplus {({{x \cdot y} \cdot z})}$$

                7.  $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{se obtine la igualdad deseada.}$$

            9.  $${\lbrack{{Teorema}12}\rbrack}\forall x,y,{z \in B}{}{}{}{{{({x \cdot y})} + z} = {{({x + z})} \cdot {({y + z})}}}$$

                1.  Prueba:

                2.  $${\lbrack A\rbrack}{}{}{}{{{({x \cdot y})} + z} =}$$

                3.  $${= {{({x \cdot y})} + z}} = {}$$

                4.  $${= {({{({x \cdot y})} \oplus z})}} \oplus {{({{({x \cdot y})} \cdot z})} =}$$

                5.  $${= {({x \cdot y})}} \oplus z \oplus {({{x \cdot y} \cdot z})}$$

                6.  $${\lbrack B\rbrack}{}{}{}{{{({x + z})} \cdot {({y + z})}} =}$$

                7.  $${= {{({{({x \oplus z})} \oplus {({x \cdot z})}})} \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}}} = {}$$

                8.  $${= {({{x \cdot {({y \oplus z})}} \oplus {x \cdot {({y \cdot z})}}})}} \oplus {({{z \cdot {({y \oplus z})}} \oplus {z \cdot {({y \cdot z})}}})} \oplus {{({{{x \cdot z} \cdot {({y \oplus z})}} \oplus {{x \cdot z} \cdot {({y \cdot z})}}})} =}$$

                9.  $${= {x \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}}} \oplus {z \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}} \oplus {{{x \cdot z} \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}} =}$$

                10. $${= {({{({{x \cdot y} \oplus {x \cdot z}})} \oplus {({{x \cdot y} \cdot z})}})}} \oplus {({{({{z \cdot y} \oplus {z \cdot z}})} \oplus {({{z \cdot y} \cdot z})}})} \oplus {{({{({{{x \cdot z} \cdot y} \oplus {{x \cdot z} \cdot z}})} \oplus {({{{x \cdot z} \cdot y} \cdot z})}})} =}$$

                11. $${= {x \cdot y}} \oplus {x \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {z \cdot y} \oplus {z \cdot z} \oplus {{z \cdot y} \cdot z} \oplus {{x \cdot z} \cdot y} \oplus {{x \cdot z} \cdot z} \oplus {{{{x \cdot z} \cdot y} \cdot z} =}$$

                12. $${= {x \cdot y}} \oplus {x \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {y \cdot z} \oplus z \oplus {y \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {x \cdot z} \oplus {{{x \cdot y} \cdot z} =}$$

                13. $${= {x \cdot y}} \oplus {{x \cdot y} \cdot z} \oplus {y \cdot z} \oplus z \oplus {y \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {{{x \cdot y} \cdot z} =}$$

                14. $${= {x \cdot y}} \oplus {y \cdot z} \oplus z \oplus {y \cdot z} \oplus {{{x \cdot y} \cdot z} =}$$

                15. $${= {x \cdot y}} \oplus z \oplus {{{x \cdot y} \cdot z} =}$$

                16. $${= \left( {x \cdot y} \right)} \oplus z \oplus \left( {{x \cdot y} \cdot z} \right)$$

                17. $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{se obtine la igualdad deseada.}$$

# Funciones booleanas

1.  Estudio de las funciones booleanas, sobre álgebras de Boole finitas.

    1.  Estudiaremos sólo las funciones $$f:{B^{n}\rightarrow B}$$ dónde
        $${B = B_{2}} = {\{ 0,1\}}$$. Esto es
        $$f:{{B_{2}}^{n}\rightarrow B_{2}}$$.

    2.  Formas normales. Toda función
        $$f:{{B_{2}}^{n}\rightarrow B_{2}}$$ se puede poner en la forma
        $$f{{({x_{1,}x_{2,...},x_{n}})} = {\sum\limits_{k = 1}^{m < 2^{n}}{\prod\limits_{l = 1}^{n}x_{l}}}}$$.

    3.  En general, el número de funciones de un conjunto $$C$$de
        cardinal $$n_{C} \in \mathbb{N}$$ en un conjunto $$D$$de
        cardinal $$n_{D} \in \mathbb{N}$$será $${n_{D}}^{n_{C}}$$. Así
        una función de $$n$$ variables en $$C$$con valores en $$D$$será
        $${n_{D}}^{({n_{C}}^{n})}$$. Para el caso en que
        $${C = D} = B_{2}$$que toma como argumento$$n$$ variables,
        obtenemos que el número de funciones será de
        $$2^{(2^{\mathbf{\mathrm{n}}})}$$. En una pequeña tabla vemos
        como crece esta cantidad:

  ------------------------ ----------------------------------------------------------------
  $\mathbf{N}$ variables   Número de funciones distintas: $2^{(2^{\mathbf{\mathrm{N}}})}$
  0                        2
  1                        4
  2                        16
  3                        256
  4                        65536
  5                        4294967296
  6                        18446744073709551616
  7                        340282366920938463463374607431768211456
  ------------------------ ----------------------------------------------------------------

1.  1.  El punto anterior es fácil de probar:

        1.  Para el caso de $$N = 0$$ y de $$N = 1$$ es fácil probar
            (por enumeración) la vali­dez de la fórmula. Más tarde
            mostraremos tablas de todas las funciones hasta $$N = 2$$
            inclusive.

        2.  Para el caso general, la Hipótesis de Inducción será
            :$${\lbrack\mathbf{\mathit{HI}}\rbrack}\forall{N \in {({\mathbb{N} \cup {\{ 0\}}})}}{{0 \leq N} \leq {n - 1}}\Rightarrow 2^{(2^{\mathbf{\mathrm{N}}})}\mathit{es}\mathit{el}\mathit{cardinal}\mathit{buscado.}$$

        3.  Veremos si para el caso $$N = n$$ se sigue cumpliendo la
            fórmula anterior. Pero esto es claro: al añadir una variable
            en el argumento tendremos todas las funcio­nes del caso
            $$N = {n - 1}$$ $$(2^{n - 1})$$ para el valor $$0$$ de la
            nueva variable y otros $$(2^{n - 1})$$ para el valor $$1$$
            de la nueva variable, y no quedan otros casos. Las funciones
            totales para $$N = n$$ serán :

            1.  $$\mathit{card}{{({{\{{f:{{B_{\mathbf{\mathrm{2}}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}} \times {\{{f:{B_{\mathbf{\mathrm{2}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}}})} =}$$

            2.  $${= {{({\mathit{card}{({\{{f:{B_{\mathbf{\mathrm{2}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}})}})} \cdot {({\mathit{card}{({\{{f:{B_{\mathbf{\mathrm{2}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}})}})}}} = {}$$

            3.  $${{{= {{(2^{(2^{\mathbf{\mathrm{n - 1}}})})} \cdot {(2^{(2^{\mathbf{\mathrm{n - 1}}})})}}} = {(2^{{(2^{\mathbf{\mathrm{n - 1}}})} + {(2^{\mathbf{\mathrm{n - 1}}})}})}} = {(2^{2 \cdot {(2^{\mathbf{\mathrm{n - 1}}})}})}} = {(2^{(2^{\mathbf{\mathrm{n}}})})}$$.

Y así queda establecida la fórmula.

1.  1.  Como se ve en el punto anterior, el crecimiento es desmesurado
        al compararlo al crecimiento lineal de los argumentos. En un
        futuro, cuan­do intentemos hacer reducciones de expresiones
        booleanas, este crecimiento nos im­pedirá construir métodos
        eficaces para resolver las minimizaciones.

    2.  Aunque hemos visto que podemos poner las expresiones booleanas
        en los conjuntos de operadores
        $$\{{{\{{+ ,\overline{}}\}},{\{{\cdot ,\overline{}}\}},{\{ \uparrow \}},{\{ \downarrow \}},{\{{\oplus , \cdot}\}},{\{{\odot , +}\}}}\}$$,
        por comprensibilidad y para una lectura normal se utilizan
        frecuentemente los dos primeros conjuntos unidos, pu­diendo
        variarse bien el orden de los operadores binarios:
        $$\{{{\{{{({+ , \cdot})},\overline{}}\}},{\{{{({\cdot , +})},\overline{}}\}}}\}$$.
        El primer conjunto $$\{{{({+ , \cdot})},\overline{}}\}$$será el
        que estudiemos por defecto, el segundo se tratará con una
        simetría de dualidad (hay que tener algunos cuidados). El
        conjunto elegido de operaciones se llamará desarrollo en sumas
        de productos de términos simples (una variable, o su negada, o
        una constante). También se llamará desarrollo por minitérminos o
        SOP (inglés) o SdP. El segundo será el desarrollo en producto de
        sumas de términos simples (una variable, o su negada, o una
        constante). También se llamará desarrollo por maxitérminos o POS
        (inglés) o PdS.

    3.  En el desarrollo por minitérminos expresamos sólo los términos
        de la expresión en que la función tiene como valor
        $$\mathbf{1}$$. Veamos:

    4.  $${f_{B_{\mathbf{\mathrm{2}}}}{({x_{1,}x_{2,...},x_{n}})}} = {\sum\limits_{{({i_{1,}i_{2...,}i_{n}})} = {({0,...,0})}}^{{({1,...,1})}\text{All Combinations}}{({\sigma_{1}^{({i_{1,}i_{2...,}i_{n}})}{{(i_{1})} \cdot \sigma_{2}^{({i_{1,}i_{2...,}i_{n}})}}{{(i_{2})} \cdot}...{\cdot \sigma_{n}^{({i_{1,}i_{2...,}i_{n}})}}{(i_{n})}})}}$$

        $$\mathit{dónde}{}{}{}{}{}{}\sigma_{k}^{({i_{1,}i_{2...,}i_{n}})}{{(i_{k})} \in {\{{i_{k},\overline{i_{k}}}\}}}y{\{{{0 \leq k} \leq n}\}}$$

    5.  Para más sencillez:

        $${{{{f_{B_{\mathbf{\mathrm{2}}}}{(x)}} = {f_{B_{2}}{({x_{1,}x_{2,...},x_{n}})}}} = {\sum\limits_{\iota \in {B_{\mathbf{\mathrm{2}}}}^{\mathbf{\mathrm{n}}}}{({\sigma_{1}^{\iota}{{(\iota_{1})} \cdot \sigma_{2}^{\iota}}{{(\iota_{2})} \cdot}...{\cdot \sigma_{n}^{\iota}}{{(\iota_{n})} \cdot {f_{B_{2}}{(\iota)}}}})}}} = \sum\limits_{\iota \in {B_{\mathbf{\mathrm{2}}}}^{\mathbf{\mathrm{n}}}}}{({\sigma^{\iota} \cdot {f_{B_{2}}{(\iota)}}})}$$$$\mathit{dónde}{}{}{}{}{}\sigma_{k}^{\iota}{{(\iota_{k})} \in {\{{\iota_{k},\overline{\iota_{k}}}\}}}{}{}{}{}y{}{}{}{}{{0 \leq k} \leq n}{}{}{}{}y{}{}{}{}\sigma^{\iota}{}\mathit{es}{}\mathit{un}{}\mathit{minitérmino}$$

    6.  Cuándo la sigma (el minitérmino) es en todos los casos (para
        todas las iotas) completo (es un producto de
        $$\mathbf{{n - \mathit{términos}}\mathit{simples}}$$), el valor
        de la función en esa iota concreta indica si el minitérmino
        aparece o no.

    7.  En el desarrollo por maxitérminos de una función de
        $$\mathbf{n}$$ variables, los $$\mathbf{\mathit{maxitérminos}}$$
        son sumatorios de
        $$\mathbf{{n - \mathit{términos}}\mathit{simples}}$$. Así
        termina consis­tiendo la función en un producto de maxitérminos.
        Los maxitérminos indican un $$\mathbf{0}$$ de la función.

    8.  Además de expresar las funciones por cadenas de símbolos que
        constituyen un térmi­no, existe una posibilidad de expresar estas
        funciones por tablas lineales o por cua­dros (tablas
        bidimensionales). Para cada combinación de valores booleanos a
        la en­trada de una función obtenemos un valor booleano de salida.

    9.  Para que las funciones booleanas representen algo de interés
        para la ingeniería, lo primero que debemos tener es una forma de
        representar la información que queremos procesar. ¿Cómo
        representamos un número?. ¿Cómo una letra?. Haremos un alto en
        la exposición de funciones booleanas, para detallar más esta
        pregunta, poder respon­derla y así ver para qué estamos viendo
        las álgebras de Boole.

# Representación de la información

1.  Representación de la información.

    1.  Un alfabeto es un conjunto de valores diferentes que podemos
        aplicar para represen­tar información. En el sentido que nosotros
        lo utilizamos el alfabeto de la escritura en español no solo se
        compone de las letras del abecedario, digamos en minúsculas,
        sino además, de otro conjunto similar pero en mayúsculas. A esto
        hay que añadir todos los signos de puntuación en párrafos.
        Además hay que añadir todas las vocales que son susceptibles de
        tener tilde o diéresis, además, el guión para separar las
        palabras en dos y por último un elemento muy frecuente que suele
        pasar desapercibido: el espa­cio en blanco. Por último los
        guarismos de los números del 0 al 9. Si consideramos los números
        naturales estos guarismos son un alfabeto de los números
        naturales. Como vemos los alfabetos tienen la común propiedad de
        ser finitos. Para los núme­ros naturales (como para cualquier
        otra cosa que representar) basta con
        $$B_{\mathbf{\mathrm{2}}} = {\{{\mathbf{0,}\mathbf{1}}\}}$$ .

    2.  Para nosotros un lenguaje sobre un alfabeto será un conjunto,
        donde los elementos serán ristras de letras de ese alfabeto. Una
        ristra de letras (una ristra finita) de ese al­fabeto no tiene
        porqué pertenecer al lenguaje. Por ejemplo, podemos establecer
        un lenguaje de los números naturales sobre un alfabeto
        cualquiera. Si es sobre el alfabe­to $$B_{\mathbf{\mathrm{2}}}$$,
        de cardinal 2, diremos que una palabra de nuestro lenguaje es
        bien un 0 o bien un 1 seguido de una ristra finita cualquiera de
        0s y 1s (formalmente se suele re­presentar como
        $${\{ 0\}} \cup {\{{1 \cdot {\lbrack{\{ 0,1\}}\rbrack}^{\ast}}\}}$$,
        dónde \'$$\cdot$$\' quiere decir seguido o conca­tenado, y
        \'\'$${\lbrack...\rbrack}^{\ast}$$\'\' quiere decir una ristra
        de letras de dentro del paréntesis, con la única condición que
        sea finita, y que puede ser vacía).

    3.  Una palabra del español podemos representarla sobre el alfabeto
        castellano en minús­culas unido al alfabeto castellano en
        mayúsculas, unido a la tilde y la diéresis cómo el conjunto de
        palabras del diccionario de la Real Academia de la Lengua,
        represen­tando una palabra con una diéresis como cigüeña como
        "cig#ueña", y si lleva una til­de como en Julián como "Juli\~an".
        Un nombre más habitual que el de lenguaje en electrónica suele
        ser el de código.

    4.  Antes de seguir el desarrollo, veamos algunos casos particulares
        de códigos: código binario natural de cualquier longitud, código
        binario natural de longitud fija, códigos 5 entre 2 (o
        biquinarios), códigos BCD (BCD natural, BCD exceso 3, BCD
        auto-complementario Aitken), códigos con distancias sucesivas 1
        (para longitud fija) (códigos continuos), códigos continuos con
        distancia 1 entre el primer elemento y el último elemento o
        circulares. Códigos especulares. Si son circulares y especulares
        se llaman códigos Gray (de una determinada longitud fija).
        Códigos con redundancia de infor­mación, entre los que destacan
        los códigos Hamming.

Podéis ver que en los códigos antes explicitados y sus propiedades hacen
referencia necesaria a algo más que al conjunto de las palabras de un
lenguaje, que se puede re­sumir en un orden en las palabras. Esto viene
dado normalmente por el significado de las palabras.

1.  1.  Hemos hablado de alfabetos, lenguajes sobre un alfabeto y
        después sobre el orden sobre esas palabras. Si llamamos a las
        reglas que cumplen las palabras de un lenguaje respecto a un
        alfabeto la gramática de ese lenguaje, el último elemento, el
        del orden, o más en general los significados, son la semántica.

    2.  En 3 hablamos de un lenguaje de los números naturales sobre un
        alfabeto $$\mathbf{B}_{\mathbf{\mathrm{2}}}$$. En general: ¿qué
        número significa 1001? ¿y el 1011101?. A qué valor natural
        apunta cada cadena es algo exterior al léxico y su gramática.
        Vamos a construir una semánti­ca: llamamos en una cadena de
        letras del alfabeto
        $$l_{\mathbf{\mathrm{n - 1}}}\ldots l_{\mathbf{\mathrm{1}}}l_{\mathbf{\mathrm{0}}}$$a
        $$l_{\mathbf{\mathrm{0}}}$$el dígito me­nos significativo
        (el$$\mathbf{lsb}$$) y al$$l_{\mathbf{\mathrm{n - 1}}}$$el
        dígito más significativo (el $$\mathbf{\mathrm{msb}}$$). Pri­mero
        asignamos unos valores naturales a los del alfabeto
        $$\nu:{B_{\mathbf{\mathrm{2}}}\rightarrow\mathbf{\mathbb{N}}}::\begin{Bmatrix}
            {\mathbf{0_{\mathrm{2}}}@0} \\
            {\mathbf{1_{\mathrm{2}}}@1}
            \end{Bmatrix}$$, y según el subíndice $$\mathbf{n}$$ de la
        letra $$l_{\mathbf{\mathrm{n}}}$$ obtenemos el valor
        $$\nu{{(l_{\mathbf{\mathrm{n}}})} \cdot {(2^{\mathbf{\mathrm{n}}})}}$$
        para esa letra en ese lugar concreto. Así el valor de una
        palabra de nuestro código será
        $$\sum\limits_{\iota = 0}^{n - 1}{({\nu{{(l_{\mathbf{\mathrm{\iota}}})} \cdot {(2^{\mathbf{\mathrm{\iota}}})}}})}$$.
        Más en general si $$\mathbf{D}_{\mathbf{\mathrm{n}}}$$es un
        alfabeto de cardinal $$\mathbf{n}$$, esto es, desde los dígitos
        $$\left\{ {d_{\mathbf{\mathrm{0}}},d_{\mathbf{\mathrm{1}}},\ldots,d_{\mathbf{\mathrm{n - 1}}}} \right\} = \mathbf{D}_{\mathbf{\mathrm{n}}}$$y
        establecemos la función
        $$\nu:{\mathbf{D}_{\mathbf{\mathrm{n}}}\rightarrow\mathbf{\mathbb{N}}}::\begin{matrix}
            {\mathbf{d_{\mathrm{\iota}}}@\mathbf{\iota}}
            \end{matrix}$$, el valor de una palabra del lenguaje
        (código)
        $$r \in {d_{i \neq 0} \cdot {\lbrack\mathbf{D}_{\mathbf{\mathrm{n}}}\rbrack}^{\ast}}$$
        será
        $$\nu{(r)}{=}{\sum\limits_{\iota = 0}^{l{{(r)} - 1}}{({\nu{{(d_{\mathbf{\mathrm{\iota}}})} \cdot {(n^{\mathbf{\mathrm{\iota}}})}}})}}$$,
        y $$l{(r)}$$ es la longitud de la representación $$r$$. Este
        tipo de representación es la más usada en el ámbito de los
        números desde hace seiscientos o setecientos años más o menos en
        Occidente, sólo que para base 10 (diez dígitos distintos).
        Nosotros usaremos también bastante la base 2, código que
        llamamos habitualmente binario natural.

    3.  Aquí es conveniente tener claro cómo pasamos de una base a otra.
        En general lo ha­cemos por pasos:

        1.  Paso de una base $$B$$ a base $$10$$. Esto lo hacemos por
            aplicación directa de la fórmula expresada anteriormente en
            2.6.

        2.  Paso de base $$10$$ a una base $$B$$. Esto se hace por el
            proceso inverso al ante­rior, dividimos sucesivamente por
            $$B$$los cocientes y nos vamos quedando con los restos,
            dónde los primeros son los dígitos de más bajo peso, y los
            últimos los de más alto. El proceso termina naturalmente
            cuando el cociente a dividir es más pequeño que la base
            $$B$$, cociente que pasa a ser el dígito
            $$\mathbf{\mathit{msb}}$$de la conver­sión.

        3.  Paso de una base $$B_{1}$$ a una base $$B_{2}$$:

            1.  Caso que $$B_{1}{=}{B_{2}}^{p}$$. Cada dígito de
                $$B_{1}$$ lo desarrollamos como su co­rrespondiente en
                $$p$$ dígitos de base $$B_{2}$$ (sin ahorrar los 0 a la
                izquierda). Así hemos terminado.

            2.  Caso que $${B_{1}}^{q}{=}B_{2}$$. Comenzando por el
                $$\mathbf{\mathit{lsb}}$$(el más a la derecha) agrupamos
                los dígitos de $$q\mathit{en}q$$ dígitos de $$B_{1}$$.
                Cada grupo de $$q$$ dí­gitos de $$B_{1}$$ es exactamente
                un dígito de $$B_{2}$$, hacemos así la sustitución
                predicha y hemos terminado. El único posible problema es
                el grupo de $$q$$ dígitos más alto, en el caso que tenga
                entre $$1$$ y $$q - 1$$ dígitos. Ese grupo se rellena
                con $$d_{0}$$(el que representa a$$0$$) por la izquierda
                hasta completar la longitud $$q$$.

            3.  Caso que
                $$B_{1}^{q}{=}B_{2}^{p} \land \mathit{mcd}{{({q,p})} = 1}$$.
                Lo dividimos en dos pasos: pasamos primero $$B_{1}$$ a
                $$B_{1}^{q}$$ y entonces de $$B_{1}^{q}{=}B_{2}^{p}$$ a
                $$B_{2}$$.

            4.  Caso en que no hay una relación entre $$B_{1}$$ y
                $$B_{2}$$ de las anteriores. Enton­ces pasamos de base
                $$B_{1}$$ a base $$10$$, y entonces de base $$10$$ a
                $$B_{2}$$. Este método es general, pero el anterior es
                más eficiente para los casos espe­cificados.

    4.  Para describir letras, esto es, caracteres alfabéticos de la
        lengua natural, utilizamos generalmente el código ASCII (de 7
        bits el estándar original o de 8 dígitos binarios o bits, el
        extendido de Microsoft). Existen otros códigos, como el EBCDIC
        de IBM, UTF8, UTF16 y Unicode. Permiten sobradamente trasladar
        los lenguajes naturales escritos a un alfabeto binario.

    5.  El conjunto de los naturales es insuficiente para muchas
        aplicaciones. La primera ampliación es el conjunto
        $$\mathbf{\mathbb{Z}}$$ de los enteros. Las formas de
        representar números enteros es variada pero la vamos a resumir
        en tres formas:

        1.  Magnitud y Signo ($$M\text{\&}S$$). Representamos el valor
            absoluto del número como un número en binario natural y le
            añadimos un $$0$$ o un $$1$$ en el
            $$\mathbf{\mathit{msb}}$$, dónde el $$0$$ representa el
            signo "$$-$$" y el $$1$$ representa el signo "$$+$$". Este
            lenguaje sería en
            general$${{\left\{ \mathbf{0} \right\} \vee \left\{ \mathbf{00} \right\}} \vee \left\{ \mathbf{10} \right\}} \vee \left( {{\mathbf{D}_{\mathbf{\mathrm{2}}} \cdot \left( {\mathbf{D}_{\mathbf{\mathrm{n}}} \smallsetminus \left\{ d_{0} \right\}} \right)} \cdot \left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\ast}} \right)$$,
            habida cuenta que
            $$\mathbf{D}_{\mathbf{\mathrm{2}}} \subseteq \mathbf{D}_{\mathbf{\mathrm{n}}}$$.
            Esta es una traducción directa de lo que hacemos cuando
            escribimos un número entero con signo. En general tenemos 2
            representa­ciones para el número 0.

        2.  En Complemento a la base B ($$\mathit{CbB}$$). En esta
            método de representación tene­mos una forma de representar
            los números positivos y otra los negativos. Los nú­meros
            positivos (incluido el $$d_{\mathbf{\mathrm{0}}}$$de
            valor$$\mathbf{0}$$) se representan de forma idéntica a como
            se hace en $$M\text{\&}S$$. La novedad está en los números
            negativos, cuyo $$\mathbf{\mathit{msb}}$$es $$\mathbf{1}$$,
            seguido de un dígito cualquiera distinto del más alto
            $$\mathbf{d}_{\mathbf{\mathrm{\iota \neq {n - 1}}}}$$y
            seguido de una ristra finita cualquiera de dígitos.

            1.  Primero introduciremos una operación, la complementación
                de dígitos que designaremos como un operador
                prefijo$$C_{\mathbf{\mathrm{Β\mathit{m1}}}}$$, de forma
                que dada una ris­tra cualquiera sobre un
                alfabeto$$\mathbf{D}_{\mathbf{\mathrm{n}}}$$,
                formalmente el
                lenguaje$$\left\{ \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}} \right\}$$,
                que definimos como:

                $$\mathbf{\upsilon}:{{\left\{ {0,1,\ldots,{n - 2,}{n - 1}} \right\} \subset \mathbb{N}}\rightarrow\mathbf{D}_{\mathbf{\mathrm{n}}}}::v@d_{\mathbf{\mathrm{v}}}$$

                $$\mathit{De}\mathit{forma}\mathit{que}\left( {\mathbf{\nu}{(d_{\mathbf{\mathrm{v}}})}{=}v} \right)\Leftrightarrow\left( {{\mathbf{\upsilon}{(v)}}{=}d_{\mathbf{\mathrm{v}}}} \right)$$

                $$\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}:{\mathbf{D}_{\mathbf{\mathrm{n}}}\rightarrow\mathbf{D}_{\mathbf{\mathrm{n}}}}::\delta@\mathbf{\upsilon}\left( {{{n - 1} - \mathbf{\nu}}{(\delta)}} \right)$$$$C_{\mathbf{\mathrm{Β\mathit{m1}}}}:{\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}\rightarrow\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}}::\delta_{n - 1}\cdots\delta_{1}\delta_{0}{:\rightarrow}\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{n - 1}\cdots\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{1}\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{0}$$

            Otra forma de llamar a esta operación es complemento a la
            base menos uno. Permite hacer operaciones sin ningún tipo de
            acarreo, dígito a dígito sin de­pendencias de la posición.
            Algunas propiedades de esta operación son:

            $$\forall{\mathit{r} \in \left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\ast}}C_{\mathbf{\mathrm{Β\mathit{m1}}}}{{({C_{\mathbf{\mathrm{Β\mathit{m1}}}}{(\mathit{r})}})} = \mathit{r}}$$

            $$\forall{\mathit{r} \in \left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\ast}}\mathit{siendo}\mathbf{l}{{(\mathit{r})} = s},\mathbf{\nu}{{({C_{\mathbf{\mathrm{Β\mathit{m1}}}}{(\mathit{r})}})} = {{\mathbf{n}^{\mathbf{\mathrm{s}}} - \mathbf{1}} - \mathbf{\nu}}}{(\mathit{r})}$$

            Esta operación es interesante porque nos va a permitir
            definir la complementa­ción a la base
            $$\mathbf{\mathtt{\mathrm{D}}}_{\mathtt{\mathrm{n}}} \equiv \mathtt{Β}$$
            de forma sencilla:

            $$\mathbf{C}_{\mathbf{\mathrm{Β}}}:{\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}\rightarrow\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}}::\mathit{r}{:\rightarrow}\mathbf{\upsilon}{({\mathbf{\nu}{{({C_{\mathbf{\mathrm{Β\mathit{m1}}}}^{\mathbf{\mathrm{l}}{(\mathit{r})}}{(\mathit{r})}})} + 1}})}$$

            Las propiedades de esta complementación son:

            $$\forall{\mathit{r} \in \mathbf{D}_{\mathbf{\mathrm{n}}}}\mathbf{C}_{\mathbf{\mathrm{Β}}}{{({\mathbf{C}_{\mathbf{\mathrm{Β}}}{(\mathit{r})}})} = \mathit{r}}$$

            $$\forall{\mathit{r} \in \left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\ast}}\mathit{siendo}\mathbf{l}{{(\mathit{r})} = s},\mathbf{\nu}{{({\mathbf{C}_{\mathbf{\mathrm{Β}}}{(\mathit{r})}})} = {\mathbf{n}^{\mathbf{\mathrm{s}}} - \mathbf{\nu}}}{(\mathit{r})}$$

            1.  Ahora ya podemos saber como interpretar los números
                negativos en represen­tación CbB. El
                $$\mathbf{\mathit{msb}}$$será $$\mathbf{1}$$, a
                continuación no tendremos un dígito
                $$\mathbf{d}_{\mathbf{\mathrm{n - 1}}}$$, sino cualquier
                otro, y una ristra finita cualquiera de dígitos sobre el
                alfabeto $$\mathbf{D}_{\mathbf{\mathrm{n}}}$$. Para
                cualquier palabra sobre el alfabeto dicho definimos el
                valor en Complemento a la base B con 1 y con 0.

                $$\forall{\mathit{r} \in \left\{ \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}} \right\}}\mathit{definimos}\mathit{el}\mathit{valor}\mathit{entero}$$

                $$\mathbf{\nu_{Β,1}}{(\mathit{r})}{: =}{\mathbf{n}^{\mathbf{\mathrm{l}}{(\mathit{r})}} - {\sum\limits_{\mathbf{\mathrm{\iota = 0}}}^{{\mathbf{\mathrm{l}}{(\mathit{r})}} - \mathbf{\mathrm{1}}}{({\mathbf{\nu}{{(\mathit{r}_{\mathbf{\mathrm{\iota}}})} \cdot \mathbf{n}^{\mathbf{\mathrm{\iota}}}}})}}}$$

                $$y$$

                $$\mathbf{\nu_{Β,0}}{(\mathit{r})}{: =}{\sum\limits_{\mathbf{\mathrm{\iota = 0}}}^{{\mathbf{\mathrm{l}}{(\mathit{r})}} - \mathbf{\mathrm{1}}}{({\mathbf{\nu}{{(\mathit{r}_{\mathbf{\mathrm{\iota}}})} \cdot \mathbf{n}^{\mathbf{\mathrm{\iota}}}}})}}$$

            2.  Ahora nos disponemos a representar el lenguaje de las
                representaciones ente­ras en $$CbB$$, y podemos ver bien
                que valores tienen:

            $$\mathit{CbD}_{n}^{-}{: =}\mathit{Rep}_{\mathit{CbB},\mathbf{\mathrm{D}}_{\mathbf{\mathrm{n}}}}{(\mathbb{Z}^{\mathbf{\mathrm{-}}})}{=}{{\mathbf{1} \cdot {\lbrack{\mathbf{D}_{\mathbf{\mathrm{n}}} \smallsetminus {\{\mathbf{d}_{\mathbf{\mathrm{n - 1}}}\}}}\rbrack}} \cdot \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}}}$$

            $$\mathit{CbD}_{n}^{+}{: =}\mathit{Rep}_{\mathit{CbB},\mathbf{\mathrm{D}}_{\mathbf{\mathrm{n}}}}{(\mathbb{Z}^{\mathbf{\mathrm{+}}})}{=}{{\mathbf{0} \cdot {\lbrack{\mathbf{D}_{\mathbf{\mathrm{n}}} \smallsetminus {\{\mathbf{d}_{\mathbf{\mathrm{0}}}\}}}\rbrack}} \cdot \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}}}$$

            $$\mathit{CbD}_{n}{: =}{{{\mathit{CbD}_{n}}^{-} \cup {\mathit{CbD}_{n}}^{+}} \cup {\{\mathbf{0}\}}}$$

            $$\forall{\mathit{r} \in \mathit{CbD}_{n}}\mathbf{\nu}_{\mathbf{\mathrm{Β}}}{(\mathit{r})}{: =}\begin{Bmatrix}
                  {\mathbf{\nu}_{\mathbf{\mathrm{Β,0}}}{(\mathit{r})}\mathit{si}{\mathit{s} \in \mathit{CbD}_{n}^{+}},{r = {\mathbf{0} \cdot s}}} \\
                  {\mathbf{\nu}_{\mathbf{\mathrm{Β,1}}}{(\mathit{s})}\mathit{si}{\mathit{r} \in \mathit{CbD}_{n}^{-}},{r = {\mathbf{1} \cdot s}}}
                  \end{Bmatrix}$$

            Y así queda definido el lenguaje de las representaciones en
            complemento a una base y su semántica de valores en
            $$\mathbb{Z}$$.

        3.  Exceso a $$\mathit{n}$$. Este tipo de representación no
            necesita signo siendo, el valor de la representación su
            valor en binario natural menos $$\mathit{n}$$. La
            representación $$\mathbf{0}$$tiene como valor
            $$- \mathit{n}$$. En general el valor de la representación
            $$\mathit{r}$$ en Exceso a $$\mathit{n}$$será
            $${\mathbf{\nu}{(\mathit{r})}} - \mathit{n}$$, siendo la
            función $${valor} - \nu$$ la correspondiente al bina­rio
            natural.

        4.  La siguiente ampliación es $$\mathbb{Q}$$. Existen de
            entrada dos formas comunes de repre­sentación: en punto fijo
            y en punto flotante.

        5.  En punto fijo tendremos siempre que saber dónde se encuentra
            el punto o coma deci­mal, conociendo cual es la longitud de
            la parte fraccionaria
            ($$\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{(\mathit{r})}$$)
            y cual la de la parte entera
            ($$\mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}{(\mathit{r})}$$).
            Hasta el momento solo hemos utilizado
            $$\mathbf{l}{{(\mathit{r})} = \mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}}{{(\mathit{r})} + \mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}}{(\mathit{r})}$$dónde
            $$\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{{(\mathit{r})} = \mathbf{0}}$$.

        6.  Representaciones de binario natural en punto fijo. Vamos a
            ver, en un primer mo­mento, estas representaciones solo si
            son positivas, esto es, representaciones de
            $$\mathbb{Q}^{\mathbf{\mathrm{+}}}$$en binario natural, que
            será la base para el resto de representaciones más
            com­plejas. En principio la parte entera vendrá dada por una
            expresión del tipo
            $$\mathit{{Ent}{\lbrack r\rbrack}} \in {\mathbf{d}_{\mathbf{\mathrm{\iota \neq 0}}} \cdot \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}}}$$,
            $${\mathbf{l}{(\mathit{{Ent}{\lbrack r\rbrack}})}} = {\mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}{(\mathit{r})}}$$,
            $$\mathit{{Frac}{\lbrack r\rbrack}} \in {\left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}} \cdot \mathbf{d}_{\mathbf{\mathrm{\iota \neq 0}}}}$$,
            $${\mathbf{l}{(\mathit{{Frac}{\lbrack r\rbrack}})}} = {\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{(\mathit{r})}}$$,
            $${\mathit{r} = {{\mathit{{Ent}{\lbrack r\rbrack}} \cdot \mathbf{\mathrm{.}}} \cdot \mathit{{Frac}{\lbrack r\rbrack}}}} \in {{{{\mathbf{d}_{\mathbf{\mathrm{\iota \neq 0}}} \cdot \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}}} \cdot \mathbf{\mathrm{.}}} \cdot \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}}} \cdot \mathbf{d}_{\mathbf{\mathrm{\iota \neq 0}}}}$$
            y
            $$\mathbf{l}{{(\mathit{r})} = \mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}}{{(\mathit{r})} + \mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}}{(\mathit{r})}$$.
            Para evaluar el valor de la representación la fórmula es la
            clásica
            $$\mathbf{\nu}_{\mathbb{Q}}{{(\mathit{r})} = {\sum\limits_{\mathbf{\mathrm{\iota}} = \mathbf{\mathrm{\mathit{l}{(\mathit{{{Ent}{\lbrack r\rbrack}} - 1})}}}}^{\mathbf{\mathrm{{- \mathit{l}}{(\mathit{{Frac}{\lbrack r\rbrack}})}}}}\left( {{\mathbf{\nu}{(\mathit{r}_{\mathbf{\mathrm{\iota}}})}} \cdot \mathbf{n}^{\mathbf{\mathrm{\iota}}}} \right)}}$$.
            En general aunque ponemos explícita­mente el punto, no es
            necesario una vez se conocen la longitudes de las partes
            entera y fraccionaria.

        7.  El siguiente paso es ¿cómo pasamos un número en punto fijo
            de una base a otra?. Para esto lo más sencillo es separar el
            número en punto fijo en dos partes, la entera y la
            fraccionaria. La parte entera, un número natural, seguirá
            siendo entera en cualquier base, por lo que aplicamos las
            reglas de conversión que ya conocemos para n-ario na­tural,
            ya vistas.

        ¿Y la parte fraccionaria?. También sigue siendo un número
        $${\mathbf{0} \leq \mathbf{\nu}_{\mathbb{Q}}}{{({\mathit{Frac}{\lbrack r\rbrack}})} < \mathbf{1}}$$para
        cualquier base, y en cualquier base sigue representándose como
        una cadena de­trás del punto fijo. A partir de ahora la
        representación $$\mathit{r}$$, representará siempre la parte
        fraccionaria, esto es
        $${\mathit{r} \in \lbrack}\mathbf{0},\mathbf{1}{) \subset \mathbb{Q}}$$
        , y su representación será siempre tal que confundiremos
        $$\mathit{r}$$con $$\mathbf{0}.\mathit{r}$$y
        $$\mathbf{l}{{(\mathit{r})} = \mathbf{l}_{\mathbf{\mathrm{\mathit{fracc}}}}}{{({\mathbf{0}.\mathit{r}})} = :}\mathbf{\mathrm{s}}$$.
        Veremos los distintos ca­sos:

        1.  Casos en que existe una relación entre
            $$\mathbf{D}_{\mathtt{\mathrm{n}}}$$y
            $$\mathbf{D}_{\mathtt{\mathrm{m}}}$$ tal que
            $$\exists p,{q \in \mathbb{N}}{n^{p} = m}o{n = m^{q}}o{n^{p} = m^{q}}$$.
            Los cambios son idénticos a los realizados para la parte
            entera excepto que los grupos de dígitos se cogen desde el
            punto decimal hacia la derecha, esto es, en sentido inverso
            al que tomábamos para los naturales.

        2.  Caso general. Hemos de utilizar una base intermedia, la
            habitual base 10$$\mathbf{D}_{\mathtt{\mathrm{10}}}$$. El
            método es el mismo explicado en su momento para números
            naturales en $${n - \mathit{ario}}\mathit{natural}$$. Solo
            que da pues ver como pasamos de
            base$$\mathbf{D}_{\mathtt{\mathrm{10}}}$$a$$\mathbf{D}_{\mathtt{\mathrm{n}}}$$y
            viceversa.

            1.  El caso inmediato
                es$$\mathbf{D}_{\mathtt{\mathrm{n}}}\rightarrow\mathbf{D}_{\mathtt{\mathrm{10}}}$$.
                Utilizamos la siguiente fórmula:
                $${\mathbf{\nu_{\mathrm{\mathbb{Q}}}}{(\mathit{r})}} = {\sum\limits_{\mathbf{\mathrm{\iota{=}1}}}^{\mathbf{\mathrm{s}}}\left( {{\mathbf{\nu}\left( \mathit{r}_{\mathbf{\mathrm{- \iota}}} \right)} \cdot \mathbf{\mathrm{\mathtt{\mathrm{n}}^{- \iota}}}} \right)}$$.

            2.  El caso inmediato
                es$$\mathbf{D}_{\mathtt{\mathrm{10}}}\rightarrow\mathbf{D}_{\mathtt{\mathrm{n}}}$$.
                Se trata del proceso inverso al anterior, esto es, como
                las potencias son negativas realizamos, el el caso
                anterior divi­siones sucesivas por
                $$\mathtt{\mathrm{n}}$$, el cardinal de la base. Pro lo
                tanto el proceso que nos atañe será el de multiplicar
                sucesivamente por la base$$\mathtt{\mathrm{n}}$$, el
                número fraccionario $$\mathtt{0.r}$$. En cada
                multiplicación por la base la parte entera será un
                dígito de la nueva base, y los obtenemos desde el primer
                lugar a la derecha del punto decimal hacia la derecha.
                En cada multiplicación nos quedamos con el resto, esto
                es, la parte fraccionaria del resultado (la parte entera
                ya ha sido incorporada al resultado final).

            3.  Podemos observar fácilmente que en los dos casos
                anteriores el procedimien­to de colocar decimales en la
                nueva base no tiene por qué ser un proceso que termine,
                esto es, finito. Es claro $$1/3$$ en base
                $$\mathbf{\mathrm{\mathtt{\mathrm{D}}}}_{3}$$tiene una
                representa­ción finita
                $${({1/3})} = 0.1_{\mathbf{\mathrm{\mathtt{\mathrm{3}}}}}$$,
                pero en base
                $$\mathbf{\mathrm{\mathtt{\mathrm{D}}}}_{2}$$, en
                binario, y en base $$\mathbf{\mathrm{\mathtt{10}}}$$y en
                otras bases tenemos que
                $$({1/3})$$$$=$$$${0.\widehat{3}}_{\mathbf{\mathrm{\mathtt{\mathrm{10}}}}}$$$$=$$$${0.\widehat{01}}_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}}$$$$=$$$$0.1_{\mathbf{\mathrm{\mathtt{\mathrm{3}}}}}$$$$=$$$${0.\widehat{1}}_{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}$$$$=$$$${0.\widehat{13}}_{\mathbf{\mathrm{\mathtt{\mathrm{5}}}}}$$$$=$$$${0.2}_{\mathbf{\mathrm{\mathtt{\mathrm{6}}}}}$$$$=$$$${0.\widehat{2}}_{\mathbf{\mathrm{\mathtt{\mathrm{7}}}}}$$$$=$$$${0.\widehat{25}}_{\mathbf{\mathrm{\mathtt{\mathrm{8}}}}}$$$$=$$$${0.3}_{\mathbf{\mathrm{\mathtt{\mathrm{9}}}}}$$$$= \ldots =$$$${0.4}_{\mathbf{\mathrm{\mathtt{\mathrm{12}}}}}$$$$= \ldots =$$$${0.5}_{\mathbf{\mathrm{\mathtt{\mathrm{15}}}}}$$$$= \ldots =$$$${0.\widehat{5}}_{\mathbf{\mathrm{\mathtt{\mathrm{16}}}}}$$$$= \ldots =$$$${0.9}_{\mathbf{\mathrm{\mathtt{\mathrm{27}}}}}$$$$= \ldots$$.

                Una vez hemos utilizado la representación en binario,
                las de base 4 y la octal (base 8) son inmediatas por
                reagrupamientos. Igualmente la representación en base 3
                es inmediata ya que
                $${({1/3})} = 3^{\mathtt{({- 1})}}$$, que corresponde a
                $${\mathtt{r_{\mathrm{\mathtt{- 1}}}} = \mathtt{\mathrm{d}}_{\mathtt{\mathrm{1}}}}\mathit{tal}\mathit{que}{{\mathbf{\nu}\left( \mathtt{r_{\mathrm{\mathtt{- 1}}}} \right)} = \mathtt{1}}$$,
                y confundiremos habitualmente
                $$\mathtt{\mathrm{d}}_{\mathtt{\mathrm{1}}}$$ con
                $$\mathtt{1}$$y queda claro que para cualquier otra
                posición tenemos que
                $${\mathtt{r_{\mathrm{\mathtt{- \iota}}}} = \mathtt{\mathrm{d}}_{\mathtt{\mathrm{\iota}}}}\mathit{es}{{\mathbf{\nu}\left( \mathtt{r_{\mathrm{\mathtt{- \iota}}}} \right)} = \mathtt{0}}\mathit{si}{\mathtt{\iota} > \mathtt{1}}$$.
                Igualmente tenemos por reagrupamien­to la representación
                para base 9.

            4.  Es importante darnos cuenta que en el caso de pasos
                entre $$\mathbf{D}_{\mathtt{\mathrm{n}}}$$y
                $$\mathbf{D}_{\mathtt{\mathrm{m}}}$$ tal que
                $$\exists p,{q \in \mathbb{N}}{n^{p} = m}o{n = m^{q}}o{n^{p} = m^{q}}$$,
                si la representación fuente es finita la destino también
                los será, y si la fuente es infinita con un periodo, el
                destino también lo será. En general si pasamos un número
                de base$$\mathbf{D}_{\mathtt{\mathrm{n}}}$$a
                base$$\mathbf{D}_{\mathtt{\mathrm{n \cdot m}}}$$la
                representación seguirá guardando su carácter finito no
                periódi­co si así ocurre en
                $$\mathbf{D}_{\mathtt{\mathrm{n}}}$$(como vemos al pasar
                de base 3 a base 6).

            5.  Habitualmente utilizaremos el guarismo confundido con el
                dígito$$\mathtt{\mathrm{\mathtt{\mathrm{d}}}_{\mathrm{\iota}}} \equiv \mathtt{\iota}$$
                $$\mathit{solo}\mathit{si}$$$${\mathtt{0} \leq \mathtt{\iota}} \leq \mathtt{9}$$.
                Para dígitos superiores, si los hubiera, hay varias
                es­trategias. En Electrónica Digital se suele utilizar el
                alfabeto latino, sin dife­renciar mayúsculas de
                minúsculas, lo más habitual para trabajar en base 16
                (hexadecimal),
                $$\mathtt{\left\{ {{\mathrm{d}_{\mathrm{10}} \equiv \mathrm{A}}\mathrm{,}{\mathrm{d}_{\mathrm{11}} \equiv \mathrm{B}}\mathrm{,}{\mathrm{d}_{\mathrm{12}} \equiv \mathrm{C}}\mathrm{,}{\mathrm{d}_{\mathrm{13}} \equiv \mathrm{D}}\mathrm{,}{\mathrm{d}_{\mathrm{14}} \equiv \mathrm{E}}\mathrm{,}{\mathrm{d}_{\mathrm{15}} \equiv \mathrm{F}}} \right\}}$$
                y en general podemos utilizar más letras, y más letras
                aún de otros abecedarios (y aún distinguir entre
                mayúsculas y minúsculas, acentuarlas de diferentes
                formas e inventarnos nuevas letras-gráficos, pero en
                general no es solución general del problema). Una
                solución general es utilizar cadenas que conten­gan el
                índice del dígito correspondiente en base 10
                (comprensible para todos) en una cadena que exprese la
                base en la que nos encontramos con
                $$d@\mathit{Rep}\left( {n \in \mathbb{N}} \right)_{\mathtt{\mathrm{10}}}@\mathtt{Β}\mathit{Rep}\left( {\mathit{base} \in \mathbb{N}} \right)_{\mathtt{\mathrm{10}}}$$,
                que es la solución que hemos adop­tado en el programa
                $$\mathit{CVarNum}$$ que podéis disponer para hacer
                conversio­nes etc en cualquier base. En este programa (en
                realidad un conjunto de clases del lenguaje de
                programación C++), además de representar y operar con
                dígi­tos de cualquier base, podemos representar y operar
                con números naturales en cualquier base (representación
                $${n - \mathit{ario}}\mathit{natural}$$) y con números
                enteros de cualquier base (representación interna en
                $$\mathit{CbB}$$). Los naturales los repre­sentamos como
                $$\mathit{num}\text{\_}\mathit{uint}@\left( n_{l - 1} \right)_{\mathtt{\mathrm{10}}};\left( n_{l - 2} \right)_{\mathtt{\mathrm{10}}};\ldots;\left( n_{1} \right)_{\mathtt{\mathrm{10}}};\left( n_{0} \right)_{\mathtt{\mathrm{10}}}@\mathtt{Β}\left( \mathit{base} \right)_{\mathtt{\mathrm{10}}}$$
                y los enteros por defecto entran y salen como en
                $$\mathit{CbB}$$. Hay algunas facili­dades para sacar los
                números enteros en pantalla en $$M\text{\&}S$$.

            6.  Por lo demás es fácil conseguir la representación de la
                parte fraccionaria en $$\mathit{CbB}$$ si ésta es
                negativa. Se realizan las operaciones de la misma forma
                que la hacíamos con la parte entera, solo que allí
                teníamos en cuenta la longi­tud de la representación,
                pero aquí, para la parte fraccionaria el complemento lo
                conseguimos básicamente con el complemento de la parte
                fraccionaria a la unidad
                $$\mathtt{\mathrm{1.0\ldots 0\ldots}}$$.

    6.  El último tipo de representación que vamos a ver es la
        representación en punto flo­tante
        ($$\mathit{floating}\mathit{point}$$, de forma que en C,C++ al
        tipo de números con decimales que habitualmente llamamos reales,
        toman el nombre de su forma de representación :
        $$\mathit{float}$$). Este tipo está estandarizado y tenemos un
        documento que lo detalla bastante bien. Este tipo tiene ventajas
        (relativas) con respecto al punto fijo porque amplía bastante el
        rango de valores a representar con el mismo número de dígitos, y
        porque se controla el error de representación en forma
        proporcional al valor absoluto del número, esto es, trabajamos
        con errores relativos, mientras en punto fijo se trabaja con
        errores absolutos que son fijos en todo el rango de
        representaciones. Como parte negativa hay que decir que los
        circuitos para trabajar con punto flotante son más complejos y
        voluminosos que los que teníamos para punto fijo, que eran los
        mismos circuitos que teníamos para trabajar con enteros.

    7.  Siguiendo con los códigos que utilizamos en Electrónica Digital,
        los más comunes son los códigos o lenguajes que tienen una
        longitud fija. Por ver un poco la noción de longitud, ésta
        determina básicamente la cantidad de valores de diferentes, de
        palabras diferentes que puede tener el lenguaje. Si trabajamos
        con el lenguaje $$\mathtt{\mathrm{L}}$$ sobre el alfabeto
        $$\mathtt{\mathrm{A}}$$, definiremos:

        $$\mathtt{\mathrm{L^{+}(A){: = {A \cdot A^{\ast}}}}} = \mathtt{\mathrm{A^{+}}}$$

        $$\mathtt{\mathrm{L(A){: = A^{\ast}}}} = {\mathtt{\mathrm{L^{+}(A)}} \cup \left\{ \epsilon \right\}}$$

        $$\mathtt{\mathrm{L^{({{\leq n}, \ast})}(A)}}{\mathtt{\mathrm{:}} =}\left\{ {{{r \in L^{\ast}}(A)}{\mid}\mathit{long}{(r) \leq n}} \right\}$$

        $$\mathtt{\mathrm{L^{({{\leq n}, +})}(A)}}{\mathtt{\mathrm{:}} =}\left\{ {{{r \in L^{+}}(A)}{\mid}\mathit{long}{(r) \leq n}} \right\}$$

        $${{\mathtt{\mathrm{L^{n}(A)}}{\mathtt{\mathrm{:}} =}\left\{ {{{r \in L^{\ast}}(A)}{\mid}\mathit{long}{(r) = n}} \right\}} \equiv \mathtt{\mathrm{A^{n}}}} \equiv {{{\mathtt{\mathrm{A}} \times \mathtt{\mathrm{A}}} \times \overset{\mathtt{\mathrm{n}}}{\ldots}} \times \mathtt{\mathrm{A}}}$$

        A este último lo suelo llamar código saturado de
        longitud$$\mathtt{\mathrm{n}}$$sobre el
        alfabeto$$\mathtt{\mathrm{A}}$$, y será la referencia para los
        distintos códigos de longitud fija. Para un código de este tipo
        el número de palabras máximo permitido será
        $$\left( \mathtt{\mathrm{\# A}} \right)^{\mathtt{\mathrm{n}}}$$.
        Si trabajamos en binario natural de longitud fija
        $$\mathtt{\mathrm{n}}$$, representaremos desde el
        $$\mathtt{\mathrm{0}}$$ al
        $$\mathtt{\mathrm{2}}^{\mathtt{\mathrm{n}}} - \mathtt{\mathrm{1}}$$.

    8.  Por ejemplo, el código $$\mathtt{{BCD} - {natural}}$$está dentro
        de
        $$\mathtt{\mathrm{L}}^{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}\left( B_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}} \right)$$,
        pero no son idénticos. Enumeraré los valores en una tabla de dos
        columnas:

  $\mathtt{{BCD} - {natural}}$   $\mathtt{\mathrm{L}}^{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}\left( B_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}} \right)$
  ------------------------------ -----------------------------------------------------------------------------------------------------------------------
                                 0000
  0001                           0001
  0010                           0010
  0011                           0011
  0100                           0100
  0101                           0101
  0110                           0110
  0111                           0111
  1000                           1000
  1001                           1001
  \-\-\--                        1010
  \-\-\--                        1011
  \-\-\--                        1100
  \-\-\--                        1101
  \-\-\--                        1110
  \-\-\--                        1111

1.  1.  Los códigos$$\mathtt{BCD}$$son códigos de longitud fija, por lo
        general 4, pero lo fundamen­tal es que remedan en binario el
        alfabeto$$\mathtt{\lbrack{0\ldots 9}\rbrack} \equiv D_{\mathtt{\mathrm{10}}}$$.
        Dependiendo de la finali­dad hay varios: el más sencillo el que
        acabamos de dar. El
        $$\mathtt{{{{BCD} - {Exceso}} - \mathrm{a}}3}$$, es de longitud
        4, pero con el 0 en 0011 y el 9 en 1100. Comprobaréis fácilmente
        que es un código dónde el
        $$\mathtt{\mathrm{C}}_{\mathtt{\mathrm{{({Β = 10})}{m1}}}}$$coincide
        con la negación lógica bit a bit. Esto fa­cilita el hacer
        operaciones directamente en$$D_{\mathtt{\mathrm{10}}}$$. El
        código$$\mathtt{{BCD} - {Aitken}}$$, es un código
        autocomplementario como el anterior pero además mantiene un
        sistema de pesos 2-4-2-1, en orden con su valores decimales
        sería:

        $$\begin{matrix}
            \mathtt{\{{(0000,0)}\mathrm{,}{(0001,1)}\mathrm{,}{(0010,2)}\mathrm{,}{(0011,3)}\mathrm{,}{(0100,4)}\mathrm{,}} \\
            \mathtt{{(1011,5)}\mathrm{,}{(1100,6)}\mathrm{,}{(1101,7)}\mathrm{,}{(1110,8)}\mathrm{,}{(1111,9)}\}}
            \end{matrix}$$

    2.  Otro tipo de códigos son los códigos continuos y los cíclicos.
        Decimos que un código es continuo si entre una palabra y la
        siguiente en el orden propio (valor semántico o significado)
        solo varía un dígito. Además es cíclico si entre la primera
        palabra y la última varía a su vez un solo bit. Para casos con
        más de dos valores en el alfabeto ha­bría que afinar la
        definición, pero para el caso que nos ocupa, que es el código
        Gray de $$n - \mathit{bits}$$basta con lo dicho y los ejemplos
        que a continuación se van a dar. Estos códigos son además
        códigos reflejados, esto es, se obtienen por un sistema
        especular. Para un solo bit sería:

        0

        1

        Para dos bits colocamos el anterior tal cual y lo copiamos en
        forma especular hacia abajo:

        0

        1

        1

        0

        Ahora añadimos 0 en el bit izquierdo a los primeros y 1 a los
        copiados:

        00

        01

        11

        10

        Ya hemos obtenido el código Gray de 2 bits. Pongo el proceso en
        una tabla para Gray de 3 bits. Comenzamos por el Gray de 2 bits
        en la primera columna, lo reflejamos en la segunda, y añadimos
        lo 0s y 1s para distinguir los bits más altos de los más bajos,
        quedando el Gray de 3 bits en la última columna:

        $$\begin{matrix}
            00 & 00 & 000 \\
            01 & 01 & 001 \\
            11 & 11 & 011 \\
            10 & 10 & 010 \\
             & 10 & 110 \\
             & 11 & 111 \\
             & 01 & 101 \\
             & 00 & 100
            \end{matrix}$$

        Para 4 bits sería:

        $$\begin{matrix}
            000 & 000 & 0000 \\
            001 & 001 & 0001 \\
            011 & 011 & 0011 \\
            010 & 010 & 0010 \\
            110 & 110 & 0110 \\
            111 & 111 & 0111 \\
            101 & 101 & 0101 \\
            100 & 100 & 0100 \\
             & 100 & 1100 \\
             & 101 & 1101 \\
             & 111 & 1111 \\
             & 110 & 1110 \\
             & 010 & 1010 \\
             & 011 & 1011 \\
             & 001 & 1001 \\
             & 000 & 1000
            \end{matrix}$$

        Y así sucesivamente.

    3.  Los códigos biquinarios (el 2 entre 5 en concreto, entre los
        muchos biquinarios que de hecho se han utilizado), es un código
        que mantiene el número de 1s en cada pala­bra del código que
        tiene longitud constante 5. Además proviene de un código
        ponde­rado, pero tal como lo ponemos aquí ya no lo es:

        $$\{{({01100,0})},{({11000,1})},{({10100,2})},{({10010,3})},{({01010,4})},$$

        $${({00110,5})},{({10001,6})},{({01001,7})},{({00101,8})},{({00011,9})}\}$$

        Proviene del siguiente, que es ponderado, de 7 bits de longitud,
        y ponderación $${{{{{5 - 0} - 4} - 3} - 2} - 1} - 0$$:

        $$\{{({0100001,0})},{({0100010,1})},{({0100100,2})},{({0101000,3})},{({0110000,4})}$$

        $${({1000001,5})},{({1000010,6})},{({1000100,7})},{({1001000,8})},{({1010000,9})}\}$$

    4.  El siguiente y último código es el Johnson (Johnson-Möbius) de 5
        bits de longitud, que es un código continuo y progresivo, pero
        que puede ser de longitud fija de $$\mathtt{\mathrm{n}}$$, con
        una capacidad de $$\mathtt{2 \cdot \mathrm{n}}$$valores
        distintos, así el de 5 bits es apropiado para re­presentar un
        $\text{\texttt{dígito BCD}}$, y es apropiado para tratamiento
        muy rápido de la in­formación mediante registros de
        desplazamientos y otros dispositivos:

        $$\{{({00000,0})},{({00001,1})},{({00011,2})},{({00111,3})},{({01111,4})},$$

        $${({11111,5})},{({11110,6})},{({11100,7})},{({11000,8})},{({10000,9})}\}$$

2.  Tratamiento del error en códigos de longitud fija.

    1.  Utilizaremos en principio varios métodos para esta finalidad:
        códigos Reed-Solomon, códigos lineales de grupo (dentro de estos
        se encuentran los códigos Hamming), códi­gos Golay, distintos
        bits de paridad, códigos de
        repetición$$\left( {n,{3 \cdot n}} \right)$$u otros, códigos
        CRC, y de suma igual. En general: en unos detectamos un error y
        devolvemos una peti­ción de reenvío o similar, en otros cubrimos
        los casos más importantes y probables y la detección y
        corrección ha de ser autónoma por el receptor. Es importante
        saber que es lo que suele pasar cuando hay una comunicación de
        tramas de bits:

        1.  Tenemos un Emisor y un Receptor de mensaje, que comparten un
            protocolo común de actuación además del alfabeto básico y el
            código a utilizar.

        2.  Entre el Emisor y el Receptor tenemos un Medio: una Línea de
            transmisión, sea esta cableada o no.

        3.  El Medio/Línea es ruidoso: existe la probabilidad que se
            cambien uno símbolos de alfabeto por otros, obteniendo así
            una palabra del código válida o no. Si la palabra re­cibida
            en el Emisor es recibida con cambios que no la convierten en
            una palabra prohibida (no del código común), el error pasará
            desapercibido. Por otra parte si per­cibimos como Receptor un
            error podremos bien corregirlo, bien no.

        4.  Suposiciones varias que hacen el tratamiento de errores
            manejable (suposiciones ra­zonables).

            1.  La longitud de la palabra enviada permanece inalterable.
                No se pierden bits por el trayecto: se transmutarán en
                otros pero no seguirá siendo un
                $n - \text{\textit{código}}$.

            2.  La probabilidad de error será pequeña, esto
                es$${0 \leq p_{\mathit{error}}}{{({1\mathit{bit}})} \ll 0,50}$$,
                aunque de hecho no importaría esta otra
                situación$${0,50 \ll p_{\mathit{error}}}{{({1\mathit{bit}})} \leq 1}$$,
                caso en que cambiamos 1s por 0s y viceversa, y cambiamos
                la probabilidad por
                $${0 \leq {1 - p_{\mathit{error}}}}{{({1\mathit{bit}})} \ll 0,50}$$.
                El problema grave aparece cuando
                $$p_{\mathit{error}}{{({1\mathit{bit}})} \in \left( {{0,50 - \varepsilon},{0,50 + \varepsilon}} \right)}$$
                con $$\varepsilon \in {\lbrack{0,0,10}\rbrack}$$(por
                poner un límite real­mente permisivo. Así permitimos
                que$$p_{\mathit{error}}{{({1\mathit{bit}})} \in {{\lbrack{0,0,39}\rbrack} \cup {\lbrack{0,61,1}\rbrack}}}$$,
                y por la reducción vista antes tenemos que
                $$p_{\mathit{error}}{{({1\mathit{bit}})} \in {\lbrack{0,0,39}\rbrack}}$$.
                Con un error de $$0,50$$el sistema es plenamente
                aleatorio. No hay absolutamente nada que hacer.

            3.  El error en un bit ha de ser independiente de los que
                hay alrededor. Esto es a ve­ces claramente no realista.
                La idea es que en una palabra recibida,
                $$l_{n - 1}l_{n - 2}\ldots l_{2}l_{1}l_{0}$$dados
                $${0 \leq i},{j \leq {n - 1}},{i \neq j}\Rightarrow p_{\mathit{error}}{{({l_{i}l_{j}})} = p_{\mathit{error}}}{{(l_{i})} \cdot p_{\mathit{error}}}{(l_{j})}$$.

            4.  Por la suposición 2 y 3, dada la palabra que se envía
                $$l_{n - 1}l_{n - 2}\ldots l_{2}l_{1}l_{0}$$, tene­mos
                entonces que
                $$\exists{\alpha \in {\lbrack{0,0,39}\rbrack}}$$, tal
                que para $${0 \leq i},{j \leq {n - 1}},{i \neq j}$$
                entonces
                $$p_{\mathit{error}}{{({1\mathit{bit}})} \leq \alpha}$$,
                y así
                $$p_{\mathit{error}}{{({l_{i}l_{j}})} = p_{\mathit{error}}}{{(l_{i})} \cdot p_{\mathit{error}}}{{(l_{j})} = {(\alpha)}^{2}}$$.
                En general
                $$p_{\mathit{error}}{\left( {q\mathit{bits}\mathit{distintos}} \right) = \left( \alpha \right)^{q}}$$.

            5.  La probabilidad de error sobre un valor 0 o un valor 1
                ha de ser muy parecida, de forma que la asimetría sea
                inapreciable.

        5.  Hay varios conceptos importantes en cuanto a los errores: el
            de distancia Hamming y el de paridad.

        6.  En un código de longitud fija, digamos un
            $$\mathtt{\mathrm{n}} - \text{\textit{código}}$$, la
            distancia Hamming en­tre dos palabras de longitud
            $$\mathtt{\mathrm{n}}$$ sobre un alfabeto
            $$\mathtt{\mathrm{A}}$$, digamos
            $$\mathtt{\mathrm{a}}{: = l_{n - 1}^{a}}\ldots l_{1}^{a}l_{0}^{a}$$y
            $$\mathtt{\mathrm{b}}{: = l_{n - 1}^{b}}\ldots l_{1}^{b}l_{0}^{b}$$,
            definimos:

            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}\left( \mathtt{\mathrm{a,b}} \right)\overset{\text{def}}{=}\mathit{card}\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$

            En palabras es el número de bits que son diferentes entre
            amabas palabras (posición por posición).

        7.  La función definida anteriormente, formalmente,
            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}:L^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{B_{2}}} \right) \times L^{\mathtt{\mathrm{n}}}}{{{\left( \mathtt{\mathrm{B_{2}}} \right)\rightarrow{\lbrack{0,n}\rbrack}} \subset \mathbb{N}} \subset \mathbb{R}}::\left( \mathtt{\mathrm{a,b}} \right)@\mathit{card}\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$es
            una distancia bien definida matemáticamente, la distancia
            entre dos palabras iguales es siempre 0, y si son distintas
            es necesariamente distinta de 0. Siempre es un número mayor
            o igual que 0 como corresponde a un cardinal de un conjunto.
            Además es si­métrica, esto es, la distancia entre dos
            palabras
            $$\mathit{de}\mathtt{\mathrm{a}}a\mathtt{\mathrm{b}}$$ es
            idéntica a la distancia
            $$\mathit{de}\mathtt{\mathrm{b}}a\mathtt{\mathrm{a}}$$. Por
            último se cumple la desigualdad triangular, para tres
            palabras cuales­quiera
            $${\mathtt{\mathrm{a,b,c}} \in \mathtt{\mathrm{L^{n}}}}\left( \mathtt{\mathrm{B_{2}}} \right)$$
            la distancia Hamming cumple
            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{a,b}} \right) \leq {d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{a,c}} \right) + d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}}\left( \mathtt{\mathrm{c,b}} \right)}}$$.
            Estas tres propiedades pueden verse que normales entre las
            distancias euclídeas normales. De hecho esta distancia nos
            habilita para ver una geometría
            en$$\mathtt{\mathrm{L^{n}}}{\left( \mathtt{\mathrm{B_{2}}} \right) \equiv B_{2}^{n}}$$,
            dónde podemos poner como puntos los
            $$\text{\textit{minitérminos}}$$o bien los
            $$\text{\textit{maxitérminos}}$$, en general, a estos,
            vistos desde el pris­ma geométrico, se les llama
            $$n - \mathit{cubos}$$.

        8.  Para un código cualquiera de longitud fija definimos ahora
            el concepto de
            $$\mathit{distancia}\text{\textit{mínima}}\text{de un}{\mathtt{\mathrm{n}} - \text{\textit{código}}}$$,
            que es, dado
            $$C^{\mathtt{\mathrm{n}}} \subseteq B_{2}^{\mathtt{\mathrm{n}}}$$,
            $$D_{\min H}\left( C^{n} \right)\overset{\text{def}}{=}\underset{a \neq b}{\overset{{({a,b})} \in {C^{n} \times C^{n}}}{\text{\texttt{mínimo}}}}\left( {d_{\mathtt{\mathrm{H}}}^{n}\left( \mathtt{\mathrm{a,b}} \right)} \right)$$.
            Para el lenguaje completo
            $$\mathtt{\mathrm{L}}{\left( B_{2} \right) \equiv B_{2}^{\mathtt{\mathrm{n}}}}$$,
            esta distancia mínima es 1. La idea que sigue es muy
            intuitiva: si la distancia entre dos palabras es 0, entonces
            las dos palabras son en realidad la misma, son el mismo
            pun­to-palabra del espacio-código de longitud fija. Si las
            palabras son de longitud 24, 24 es la distancia más alejada
            entre dos palabras y así.

            Para determinar la distancia mínima de un
            $$\mathtt{\mathrm{n}} - \text{\textit{código}}$$hay algunos
            trucos que nos ayudarán:

            1.  Con la primera distancia 1 que encontremos podemos dejar
                de comprobar. La distancia mínima de ese código es 1.

            2.  $$D_{\min H}{\left( B_{2}^{n} \right) = 1}$$.
                Si$$\#{C^{n} = 2^{n}}$$, entonces
                $$d_{\min H}{\left( C^{n} \right) = 1}$$.

            3.  Si$$\#{C^{n} > 2^{n - 1}}$$,
                entonces$$d_{\min H}{\left( C^{n} \right) = 1}$$. Este
                resultado, tipo cota de la dis­tancia mínima en función
                del cardinal del código, se puede extender para
                distancia mínima 2, \... Por
                ejemplo$$d_{\min H}{\left( C^{n} \right) = n}$$entonces$${\# C^{n}} = 2$$.

            4.  Una forma aumentar la distancia mínima en uno cuando la
                distancia mínima es 1, y a veces en otras ocasiones, es
                añadir un bit de paridad. Un bit de paridad es un bit
                que nos dice si el número de 1s que hay en una palabra
                es par o impar. Un bit de paridad par, es un bit que
                vale 1 si y solo si el número de 1s que hay en el resto
                de la palabra es impar (con él incluido el número de 1s
                de la palabra es par). Un bit de paridad impar es un bit
                que vale 1 si y solo si el número de 1s que hay en el
                resto de la palabra es par (con él incluido el número de
                1s de la palabra es impar). Si
                $${l_{n - 1}\ldots l_{1}l_{0}} \in {\mathtt{\mathrm{L}}^{\mathtt{\mathrm{n}}}\left( B_{2} \right)}$$y
                el bit de paridad lo ponemos (añadimos) en la posición
                $$\mathtt{\mathrm{n}}$$, la fórmula
                $$l_{n}{: = l_{n - 1}} \oplus \ldots \oplus l_{1} \oplus {l_{0} = \underset{\iota = 0}{\overset{n - 1}{\oplus}}}l_{\iota}$$
                nos da el valor del bit de paridad par. El de paridad
                impar es exactamente el inverso del formulado. La ra­zón
                por la que la fórmula funciona es sencilla, si
                recordamos que $$a \oplus {a = 0}$$ y que
                $$a \oplus {0 = a}$$. Así, para un código de un solo
                bit, el de paridad sería simple­mente la repetición del
                bit (el bit de paridad par sería simplemente del mismo
                va­lor que el ya existente). De esta forma lo dos bits
                son iguales y el número de 1s será o 0 o 2, esto es,
                siempre par. Si fuese el código original de 2 bits de
                longitud, el bit de paridad debería de valer 1 si solo
                uno de los dos (no los dos) valiese 1. Esto vuelve a ser
                la suma exclusiva. Y así sucesivamente.

            5.  Podemos realizar un bit de paridad par sobre los 0s de
                una palabra. Esto tiene mayor interés cuando la longitud
                de la palabra es impar. Solo hay que negar cada bit y
                utilizar la misma fórmula anterior:
                $$l_{n}{: = \overline{l_{n-1}}} \oplus \ldots \oplus \overline{l_{1}} \oplus {\overline{l_{0}} = \underset{\iota = 0}{\overset{n - 1}{\oplus}}}\overline{l_{\iota}}$$.
                Si la lon­gitud de la palabra es par podéis comprobar que
                es lo mismo poner que no poner todas las negaciones.

            6.  Si la distancia mínima de un código es 1, entonces, en
                general no podremos lle­gar a detectar fallos. Si un bit
                de una palabra nos llega equivocado tenemos que la
                palabra resultante puede estar perfectamente en el
                código, y así pasará inadvertido el error.

            7.  La distancia mínima requerida para conseguir detectar un
                error de un solo bit es 2. Así un error de un bit,
                cuando menos nos dejará la palabra errónea a distancia 1
                de cualquier palabra válida del código. Luego la palabra
                con el error no estará en el código. En general para
                poder detectar errores de hasta
                $$p\mathit{bits}$$necesitaremos que el código sea de
                distancia mínima $$p + 1$$. El razonamiento es igual al
                expre­sado para errores de 1 bit. Si la distancia mínima
                del código es $$p + 1$$entonces, en el peor caso,
                $$p\mathit{errores}$$pueden dejarnos la palabra a
                distancia 1 (como míni­mo) de cualquier palabra válida
                del código. Luego podemos detectar que la pala­bra
                recibida no está en el código.

            8.  Podemos dar un paso más e intentar no solo detectar sino
                corregir el bit equivo­cado. Para esto necesitamos que la
                palabra con el bit equivocado quede de forma tal que sea
                claro desde cual palabra del código correcto se ha
                producido el error. No podremos tener dos palabras
                distintas del código a distancia mínima de la pa­labra
                equivocada, sino solamente una. La corrección
                consistiría en cambiar la pa­labra equivocada por la
                única más cercana del código. El principio de corrección
                es el máxima verosimilitud.

            9.  Para poder corregir$$p\mathit{errores}$$necesitamos una
                distancia mínima$${2 \cdot p} + 1$$. Para corregir un
                solo bit necesitamos una distancia mínima de tres. Esto
                es claro. Si la distancia fuera dos, al producirse el
                error, quedaría a distancia uno de más de una palabra
                del código. Sin embargo si la distancia mínima es tres,
                al producirse un error quedará a distancia 2 como mínimo
                de todas las demás palabras del códi­go. En general desde
                una palabra $$\mathtt{\mathrm{p^{i}}}$$ se ha producido
                con error la palabra
                $$\mathtt{\mathrm{\widetilde{p}}}$$tal que
                $$\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \leq p}$$.
                Podemos decir que la palabra errónea está dentro del
                radio de la esfera que rodea a
                $$\mathtt{\mathrm{p^{i}}}$$. La pregunta que surge es
                ¿puede existir una palabra
                $$\mathtt{\mathrm{p^{j}}}$$con
                $$\mathtt{\mathrm{i \neq j}}$$tal que
                $$\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \leq p}$$?.
                Sabemos que
                $$\forall i,j{i \neq j}\Rightarrow\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{p^{j}}}} \right) \geq {{2 \cdot p} + 1}}$$.
                Esto quiere decir, que:

                $$\forall j{i \neq j}\Rightarrow\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) + \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \geq \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{p^{j}}}} \right) \geq \left( {{2 \cdot p} + 1} \right)}$$

                $$\forall j{i \neq j}\Rightarrow\left\lbrack {\left( {\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) + \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \geq \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{p^{j}}}} \right) \geq \left( {{2 \cdot p} + 1} \right)}} \right) \land \left( {\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \leq p}} \right)} \right\rbrack$$

                $$\forall j{i \neq j}\Rightarrow\left\lbrack {{p + \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \geq \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) + \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \geq \left( {{2 \cdot p} + 1} \right)}} \right\rbrack$$

                $$\forall j{i \neq j}\Rightarrow\left\lbrack {{p + \mathtt{\mathrm{d_{H}}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \geq \left( {{2 \cdot p} + 1} \right)}} \right\rbrack$$

                $$\forall j{i \neq j}\Rightarrow\left\lbrack {\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \geq \left( {p + 1} \right)}} \right\rbrack$$

                $$\forall j\left\lbrack {i \neq j} \right\rbrack\Rightarrow\left\lbrack {\mathtt{\mathrm{d_{H}}}{{{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) \leq p} < {p + 1}} \leq \mathtt{\mathrm{d_{H}}}}\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right)} \right\rbrack$$

                $$\forall j\left\lbrack {i \neq j} \right\rbrack\Rightarrow\left\lbrack {\mathtt{\mathrm{d_{H}}}{\left( {\mathtt{\mathrm{p^{i}}},\mathtt{\mathrm{\widetilde{p}}}} \right) < \mathtt{\mathrm{d_{H}}}}\left( {\mathtt{\mathrm{p^{j}}},\mathtt{\mathrm{\widetilde{p}}}} \right)} \right\rbrack$$

                Luego la corrección será
                $$\mathtt{\mathrm{\widetilde{p}}}\rightarrow\mathtt{\mathrm{p^{i}}}$$necesariamente.
                Siempre habrá una sola pala­bra de nuestro código que
                esté a distancia menor o igual que $$p$$, estando las
                de­más palabras del código a distancia mayor o igual que
                $$p + 1$$.

            10. El método de construcción de detectores/correctores de
                error de Hamming es en principio el más fácil de usar,
                es el método lineal de codificación por grupo. Se trata
                de utilizar una matriz (de 0s y 1s) para convertir el
                $$\mathtt{\mathrm{n}} - \text{\textit{código}}$$
                original, en
                un$$\left( \mathtt{\mathrm{n + l}} \right) - \text{\textit{código}}$$.
                La condición principal es que la transformación sea
                inyecti­va
                y$$\mathtt{\mathrm{H}}\left( {\mathtt{\mathrm{L}}^{\mathtt{\mathrm{n}}}\left( B_{2} \right)} \right) \subset_{\text{GRUPO}}\left( {\mathtt{\mathrm{L}}^{\mathtt{\mathrm{n + l}}}\left( B_{2} \right)} \right)$$.
                Para esto lo fundamental es que la matriz de
                codificación (de dimensión
                $$\left( \mathtt{\mathrm{n + l}} \right) \times \mathtt{\mathrm{n}}$$)
                mantenga el original (con $$n$$ colum­nas dónde el único
                1 está en la posición
                $$\left( {\iota,\iota} \right)$$con$$\iota \in {\lbrack{1,n}\rbrack}$$),
                esto es, siendo un bloque matricial completo la matriz
                identidad$$\mathtt{\mathrm{I_{n \times n}}}$$, uno de
                los dos bloques de construcción de la
                matriz$$\mathtt{\mathrm{H}}$$de codificación Hamming. El
                otro bloque lo de­notaremos por
                $$\mathtt{\mathrm{P_{n \times l}}}$$. Esto además lo
                conseguiremos si la matriz de decodifica­ción
                $$\mathtt{\mathrm{H}}^{\mathbf{\mathrm{\ast}}}$$de
                dimensión
                $$\mathtt{\mathrm{n \times \left( {n + l} \right)}}$$es
                tal que
                $$\mathtt{\mathrm{H^{\mathbf{\mathrm{\ast}}}}}{\left( {\mathtt{\mathrm{H}}\left( {\mathtt{\mathrm{L}}^{\mathtt{\mathrm{n}}}\left( B_{2} \right)} \right)} \right) = 0_{B_{2}}^{n + l}}$$.
                Si el resultado de la primera decodificación no es cero
                es que hay error. Entonces, si llamamos
                $$\widetilde{\mathtt{\mathrm{p}}}$$a la palabra recibida
                y $$\mathtt{\mathrm{p}}$$a la palabra enviada (siempre
                correcta), ha de existir un vector columna
                $$\mathtt{\mathrm{e_{\iota \in {\lbrack{1,{n + l}}\rbrack}}}}$$,
                con un único uno en $$\iota$$, tal que
                $${0 = \mathtt{\mathrm{H^{\mathbf{\mathrm{\text{*}}}}}}}{(p) = \mathtt{\mathrm{H^{\mathbf{\mathrm{\text{*}}}}}}}{\left( \widetilde{p} \right) + {\mathtt{\mathrm{H^{\mathbf{\mathrm{\text{*}}}}}}\left( e_{\iota} \right)}}$$.
                Por otra parte, condición necesaria y sufi­ciente para
                que la operación sea inyectiva es que no contenga
                columnas igua­les ni columnas vector 0.

                Ejemplo:

                Supongamos que nos llega un código de 2 bits cuyos bits
                llamaremos $$o_{1}o_{0}$$, a su vez los bits codificados
                por la matriz generadora serán$$c_{1 + l}\ldots c_{0}$$.
                En general para poder corregir un bit necesitamos
                distancia 3: ¿cuántos bits habrá que añadir?. En general
                si queremos corregir códigos, hemos de añadir un número
                $$l$$de bits a los $$n$$ originales tal que la distancia
                sea mayor o igual que$$3$$, y probando, tenemos que
                $$l{: = 2}$$ ya cumple. Así que la matriz de
                codificación de grupo será de dimensión$$4 \times 2$$.

                $${{\mathtt{\mathrm{H}} \cdot \begin{pmatrix}
                        o^{1} & o^{2}
                        \end{pmatrix}} = {\mathtt{\mathrm{H}} \cdot \mathtt{\mathrm{o}}}} =$$

$$\begin{matrix}
{{= {\begin{pmatrix}
1 & 0 \\
0 & 1 \\
a & b \\
c & d
\end{pmatrix} \cdot \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1
\end{pmatrix}}} =} \\
{= \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
a & b & {a \oplus b} \\
c & d & {c \oplus d}
\end{pmatrix}}
\end{matrix}$$

1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  

                La matriz izquierda de la primera fila es la matriz
                generadora de paridades, la de­recha son el código
                original de 4 bits en forma de una palabra por cada
                columna. Por último la matriz inferior son los vectores
                codificados con tres bits de paridad insertos. Solo
                queda ver la transformación inversa correspondiente.
                Para esto vea­mos que si observamos matriz izquierda de
                la primera fila$$\mathtt{\mathrm{H}} = \begin{pmatrix}
                        \mathtt{\mathrm{I}_{2 \times 2}} \\
                        \mathtt{\mathrm{P}_{2x2}}
                        \end{pmatrix}$$. Tomare­mos como matriz
                decodificadora (no necesariamente inyectiva) a

                $$\mathtt{\mathrm{H}}^{\mathbf{\mathrm{\ast}}} = \begin{pmatrix}
                        \mathtt{\mathrm{H}_{2 \times 2}} & \mathtt{\mathrm{P}_{2 \times 2}^{\mathrm{T}}}
                        \end{pmatrix}$$

                $$\mathtt{\mathrm{H}^{\mathbf{\mathrm{\ast}}}} = \begin{pmatrix}
                        1 & 0 & a & c \\
                        0 & 1 & b & d
                        \end{pmatrix}$$

                Ahora bien, sabemos que:

                $${{\mathtt{\mathrm{H}^{\mathbf{\mathrm{\ast}}}} \cdot \mathtt{\mathrm{H}}} \cdot \mathtt{\mathrm{o}}} = \mathtt{0}$$

                De dónde obtenemos un sistema de ecuaciones, con estos
                resultados (distintos del resultado trivial):

                $$\mathtt{{\mathrm{P}_{2 \times 2}}^{\mathbf{\mathrm{T}}}} = \begin{pmatrix}
                        a & c \\
                        b & d
                        \end{pmatrix}$$

                Que hace
                que$$\mathtt{\mathrm{H}} \cdot \mathtt{\mathrm{o}}$$quede
                como:

                $$\begin{pmatrix}
                        1 & 0 & 1 \\
                        0 & 1 & 1
                        \end{pmatrix}\rightarrow\begin{pmatrix}
                        1 & 0 & 1 \\
                        0 & 1 & 1 \\
                        a & b & {a \oplus b} \\
                        c & d & {c \oplus d}
                        \end{pmatrix}$$

                El sistema de ecuaciones se genera como se ve a
                continuación:

                $${\begin{pmatrix}
                        1 & 0 & a & c \\
                        0 & 1 & b & d
                        \end{pmatrix} \cdot \begin{pmatrix}
                        1 & 0 & 1 \\
                        0 & 1 & 1 \\
                        a & b & {a \oplus b} \\
                        c & d & {c \oplus d}
                        \end{pmatrix}} = {}$$

                $${} = \begin{pmatrix}
                        {1 \oplus a \oplus c} & {{a \cdot b} \oplus {c \cdot d}} & {1 \oplus {a \cdot {({a \oplus b})}} \oplus {c \cdot {({c \oplus d})}}} \\
                        {{a \cdot b} \oplus {c \cdot d}} & {1 \oplus b \oplus d} & {1 \oplus {b \cdot {({a \oplus b})}} \oplus {d \cdot {({c \oplus d})}}}
                        \end{pmatrix}$$

                $$\begin{bmatrix}
                        {1 \oplus a \oplus c} & {{a \cdot b} \oplus {c \cdot d}} & {1 \oplus {a \cdot {({a \oplus b})}} \oplus {c \cdot {({c \oplus d})}}} \\
                        {{a \cdot b} \oplus {c \cdot d}} & {1 \oplus b \oplus d} & {1 \oplus {b \cdot {({a \oplus b})}} \oplus {d \cdot {({c \oplus d})}}}
                        \end{bmatrix}$$

                $$\begin{bmatrix}
                        {c = \overline{a}} & {{a \cdot b} = {\overline{a} \cdot d}} & {1 \oplus {a \cdot \overline{b}} \oplus {c \cdot \overline{d}}} \\
                        {{a \cdot b} = {\overline{a} \cdot d}} & {d = \overline{b}} & {1 \oplus {b \cdot \overline{a}} \oplus {d \cdot \overline{c}}}
                        \end{bmatrix}$$

                $$\begin{bmatrix}
                        {c = \overline{a}} & {{a \cdot b} = {\overline{a} \cdot \overline{b}}} & {1 \oplus {a \cdot \overline{b}} \oplus {\overline{a} \cdot b}} \\
                        {{a \cdot b} = {\overline{a} \cdot \overline{b}}} & {d = \overline{b}} & {1 \oplus {b \cdot \overline{a}} \oplus {\overline{b} \cdot a}}
                        \end{bmatrix}$$

                $$\begin{bmatrix}
                        {c = \overline{a}} & {{a \cdot b} = {\overline{a} \cdot \overline{b}}} & {{a \cdot \overline{b}} = \overline{\overline{a}\cdot b}} \\
                        {{a \cdot b} = {\overline{a} \cdot \overline{b}}} & {d = \overline{b}} & {{b \cdot \overline{a}} = \overline{\overline{b}\cdot a}}
                        \end{bmatrix}$$

                $$\begin{bmatrix}
                        {c = \overline{a}} & {{a \cdot b} = {\overline{a} \cdot \overline{b}}} & {{a \cdot \overline{b}} = {a + \overline{b}}} \\
                        {{a \cdot b} = {\overline{a} \cdot \overline{b}}} & {d = \overline{b}} & {{a \cdot \overline{b}} = {a + \overline{b}}}
                        \end{bmatrix}$$

                $$\begin{matrix}
                        {a{: = 1}b{: = 0}} \\
                        \begin{bmatrix}
                        {c = 0} & {{{1 \cdot 0} = {0 \cdot 1}} = 0} & {{{1 \cdot 1} = {1 + 1}} = 1} \\
                        {{{1 \cdot 0} = {0 \cdot 1}} = 0} & {d = 1} & {{{1 \cdot 1} = {1 + 1}} = 1}
                        \end{bmatrix}
                        \end{matrix}$$

                $$\mathtt{{\mathrm{P}_{2 \times 2}}^{\mathbf{\mathrm{T}}}} = \begin{pmatrix}
                        1 & 0 \\
                        0 & 1
                        \end{pmatrix}$$

                $$\mathtt{\mathrm{H}^{\mathbf{\mathrm{\ast}}}} = \begin{pmatrix}
                        1 & 0 & 1 & 0 \\
                        0 & 1 & 0 & 1
                        \end{pmatrix}$$

                $$\mathtt{\mathrm{H}} = \begin{pmatrix}
                        1 & 0 \\
                        0 & 1 \\
                        1 & 0 \\
                        0 & 1
                        \end{pmatrix}$$

                $$\begin{pmatrix}
                        0 & 1 & 0 & 1 \\
                        0 & 0 & 1 & 1
                        \end{pmatrix}\rightarrow\begin{pmatrix}
                        0 & 1 & 0 & 1 \\
                        0 & 0 & 1 & 1 \\
                        0 & 1 & 0 & 1 \\
                        0 & 0 & 1 & 1
                        \end{pmatrix}$$

2.  Funciones de Boole de $$n - \mathit{variables}$$ en
    $$1 - \mathit{variable}$$: tablas lineales, 2-dimensiona­les,
    arreglos de tablas 2-dimensionales y otras formas de representación.
    Simplificación en 2 capas de puertas.
