# Introducción

El álgebra de las proposiciones. Éste es sin duda, el primer desarrollo
que se hizo del álgebra de Boole, hecha por el propio George Boole en
mitad del siglo XIX (edición 1851). Lo desarrolló como una "Una
investigación en las leyes del pensamiento". Amigo suyo que lo ayudó a
penetrar los ambientes académicos es Augustus De Morgan. Desde
Aristóteles (que funda por primera vez la lógica como ciencia analítica)
en el siglo IV a. C. no había habido ningún adelanto sustancial en la
lógica. Kant (medio siglo antes de Boole) había considerado que la
lógica era un cuerpo de doctrina cerrado y completo (esto es, no había
nada más que decir que lo que ya había desarrollado y escrito
Aristóteles en sus "Tratados de Lógica" u "Órganon", hacía ya 2.300
años). Aunque la verdadera revolución se da algunos años más tarde con
Frege, el lógico más importante desde Aristóteles. Si doy estos datos
sobre la historia de la lógica que todos asociaréis más a la filosofía,
que parece queda muy lejos del propósito de unos apuntes de matemáticas
discretas que cubran de la forma más amplia posible los Fundamentos de
Electrónica Digital, es porque no queda tan lejos. La idea de hacer un
lenguaje dónde el razonamiento siguiera unas pautas claras de forma que
siempre quedara todo tan cierto como en las matemáticas era ya antiguo.
Aristóteles ya advertía de una cierta indefinición insuperable de los
términos más importantes de la filosofía (en realidad de casi todos los
conceptos de la vida ordinaria): "existen conceptos o ideas que
corresponden con la realidad que no se usan de forma equívoca -- esto
es, su uso no es equívoco, este mismo concepto, palabra o idea que
hablamos no se refiere a realidades distintas y diferenciadas, de forma
que nos llevan a confusión -- pero tampoco de forma unívoca -- como las
definiciones desde axiomas en un lenguaje formal matemático, así tenemos
que existen conceptos análogos" (es una glosa de palabras de
Aristóteles). En la Modernidad, dado que el concepto de analogía lleva
aparejado un tratamiento difícil que no lleva fácilmente a certeza, se
intentan buscar criterios de certeza absoluta y unas definiciones que
aparentemente son unívocas y se tratan como tales. Es significativo el
nombre (y la estructura interna) de una importante obra de Spinoza:
"Ética demostrada según el orden geométrico". Será Leibniz quién escriba
ya cumplidamente sobre la necesidad de establecer un léxico
completamente unívoco (una tarea mastodonte, o mejor, imposible) y un
"cálculo" del pensamiento, de forma que "una cuestión como la existencia
de Dios pueda ser resuelto mediante la resolución de unas ecuaciones de
pensamiento" (de nuevo es una glosa). Se empezaba a buscar con ansiedad
una mecanización del pensamiento. Esta idea fue muy fructífera, dando un
primer paso hacia ella George Boole que hace un álgebra de las
proposiciones. Este álgebra no era más amplia que la de Aristóteles,
pero permitía el cálculo al modo matemático. De aquí a la llegada de
Frege, ya, Charles Babbage diseña y realiza (sin éxito debido al trabajo
de mecanizado excesivamente minucioso que requería el diseño) una
computadora universal mecánica (mediante engranajes) prácticamente
similar al modelo de Von Neumann. La condesa de Lovelace (Ada) es el
matemático que hace los primeros programas en lenguaje ensamblador de la
máquina de Babbage. La primera programadora de la historia. Después de
Frege siguen los desarrollos con gente como Bertrand Rusell, David
Hilbert, y otros hasta los increíbles resultados de Gödel que ponen
punto final a muchas de las pretensiones de mecanización del
pensamiento, pero que son ya base de la computación moderna, siendo los
trabajos definitivos los de Alan Turing. Como veis el camino recorrido
es largo y complicado, siendo el momento crucial para el arranque de la
ingeniería digital los trabajos de George Boole. No he mencionado el
papel de las máquinas de cifrado y descifrado de mensajes en la Gran
Guerra y la II Guerra Mundial (en las que intervinieron muchos de las
mentes antes mencionadas).

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
\[H0.0.0\] Estructura de Conjunto - EsConjunto($\mathbb{B}$)esconj Se
requiere que $\mathbb{B}$ sea un conjunto.
:::

::: preaxioma
\[H0.0.1, H0.0.2\] Elementos Constantes - Constantesconstantes Este
conjunto ha de cumplir que tiene dos elementos que llamaremos
constantes, tales que $\bot \in \mathbb{B}$ y $\top \in \mathbb{B}$. En
principio, no asumimos nada sobre la igualdad o desigualdad de estas
constantes.
:::

Además, vamos a definir dos operaciones binarias internas que
denotaremos por $\vee$ y $\wedge$. Estas deben satisfacer rigurosamente
la definición de función:

::: preaxioma
\[H0.1\] Operación Binaria Interna $\vee$ - OpBinInt$_\vee$opbinint_vee
$\vee : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una operación
binaria interna.
:::

::: preaxioma
\[H0.2\] Operación Binaria Interna $\wedge$ -
OpBinInt$_\wedge$opbinint_wedge
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
\[H1.1\] Elemento neutro $\vee$ - $ElemNeu_\vee$neutro_vee Todo elemento
operado mediante $\vee$ con el mínimo $\bot$ da como resultado el mismo
elemento; es decir, $\bot$ no altera el valor original:
$$\forall a \in \mathbb{B}, \quad a \vee \bot = a$$
:::

::: postulado
\[H1.2\] Elemento neutro $\wedge$ - $ElemNeu_\wedge$neutro_wedge Todo
elemento operado mediante $\wedge$ con el máximo $\top$ da como
resultado el mismo elemento, quedando inalterado:
$$\forall a \in \mathbb{B}, \quad a \wedge \top = a$$
:::

::: postulado
\[H2.1\] Conmutatividad $\vee$ - $Comm_\vee$conmut_vee El orden de los
operandos al aplicar la operación $\vee$ es indiferente, obteniéndose
exactamente el mismo resultado:
$$\forall a, b \in \mathbb{B}, \quad a \vee b = b \vee a$$
:::

::: postulado
\[H2.2\] Conmutatividad $\wedge$ - $Comm_\wedge$conmut_wedge De la misma
forma, el orden de los operandos al aplicar la operación $\wedge$
tampoco altera el resultado final:
$$\forall a, b \in \mathbb{B}, \quad a \wedge b = b \wedge a$$
:::

::: postulado
\[H3.1\] Distributividad $\vee$ sobre $\wedge$ -
$Dist_\vee$distrib_vee_wedge La operación $\vee$ se distribuye sobre la
operación $\wedge$. Operar un elemento con el resultado de un $\wedge$
equivale a operar con $\vee$ cada componente individualmente y luego
aplicar $\wedge$:
$$\forall a, b, c \in \mathbb{B}, \quad a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$$
:::

::: postulado
\[H3.2\] Distributividad $\wedge$ sobre $\vee$ -
$Dist_\wedge$distrib_wedge_vee De manera equivalente, el ínfimo
($\wedge$) se reparte de forma distributiva entre los componentes de un
supremo ($\vee$):
$$\forall a, b, c \in \mathbb{B}, \quad a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$$
:::

::: postulado
\[H4\] Complementario - $Comp_\vee, Comp_\wedge$comp Todo elemento del
conjunto posee al menos un \"complemento\" (o elemento opuesto). Al
operarlo con su complemento mediante $\vee$ siempre alcanzamos el máximo
$\top$, y mediante $\wedge$ siempre caemos al mínimo $\bot$:
$$\begin{align*}
\forall a \in \mathbb{B}, \exists b \in \mathbb{B} \quad : \quad a \vee b &= \top \quad (Comp_\vee) \quad \text{[H4.1]} \\
a \wedge b &= \bot \quad (Comp_\wedge) \quad \text{[H4.2]}
\end{align*}$$
:::

*Nota: A diferencia de algunas formulaciones clásicas que imponen un
axioma de cardinalidad ($\bot \neq \top$) para evitar el álgebra
trivial, en este desarrollo permitiremos la existencia del álgebra
trivial.*

# Modelos e Instancias de Álgebras de Boole

Como ejemplos que cumplen los anteriores postulados o axiomas vamos a
desarrollar unos cuántos. Para que este sistema de axiomas sea
relativamente consistente (al sistema ZFC por ejemplo) bastará ver la
independencia de unos axiomas de otros.

**\[Ejemplo 1\]** El primero y más sencillo de ver es el álgebra de las
partes de un conjunto. Dado un conjunto
cualquiera$$U \neq \varnothing$$,
$${\wp(U)} = {\{{X \mid {X \subseteq U}}\}}$$, esto es,
$${\wp(U)} = {\{{X \mid {{\forall x}\left( {{({x \in X})}\Rightarrow{({x \in U})}} \right)}}\}}$$,
dónde se verifica
que$$\left( {{\varnothing \in }\wp(U)} \right) \land \left( {{U \in }\wp(U)} \right)$$.
Ha­remos$$\left( {B{: = }\wp(U)} \right),\left( {0{: = \varnothing}} \right)y\left( {1{: = U}} \right)$$,
como producto lógico pondremos la intersección de
conjuntos$$\forall X,{Y \in }\wp(U){X \cdot Y}{: = {X \cap Y}}$$, como
suma lógica pondremos la unión de
conjuntos$$\forall X,{Y \in }\wp(U){X + Y}{: = {X \cup Y}}$$. Las tres
primeras (dobles) propiedades son di­rectamente cumplidas por la
estructura construida y la existencia del complementario es fá­cil de
ver. Sea
$$\forall{X \in }\wp(U)\Rightarrow\exists Y{: = {U \smallsetminus X}}$$y
a partir de ahí sabemos que$${Y \in }\wp(U)$$puesto
que$$\forall{x \in Y}{x \in {U \smallsetminus X}}\Rightarrow{x \in U}$$y
en el caso que$$X = U$$tenemos que
$${{Y = {U \smallsetminus X}} = {U \smallsetminus U}} = \varnothing$$de
forma que$${\varnothing \in }\wp(U)$$por definición. Ahora sólo se trata
de ver
que$${{{{Y \cdot X} = {Y \cap X}} = {{({U \smallsetminus X})} \cap X}} = \varnothing} = 0$$y
que la propiedad dual a
cumplir$${{{{Y + X} = {Y \cup X}} = {{({U \smallsetminus X})} \cup X}} = U} = 1$$.
Ya tenemos
que$$\forall{X \in }\wp(U)\exists{Y \in }\wp(U){Y \in \overline{X}}$$ha­biendo
tomado$$Y{: = {U \smallsetminus X}}$$.

**\[Ejemplo 2\]** Un ejemplo interesante fácil de construir es el
álgebra de Boole de los números que son producto de los primeros núme­ros
primos (cantidad finita de ellos) y sus divisores. Consideramos el
conjunto $$P_{n}{: = {\{{2,3,\ldots,p_{n}}\}}}$$, con­sideraremos el
$$1$$ booleano cómo $$1_{B}{: = {\prod\limits_{q \in P_{n}}q}}$$y el
$$0$$ cómo$$0_{B}{: = 1_{\mathbb{N}}}$$. Consideramos a
$$B{: = {\{{{n \in \mathbb{N}} \mid {n \mid \left( {\prod P_{n}} \right)}}\}}}$$,
y las operaciones serán el mínimo común múltiplo como suma booleana y el
máximo común divisor como producto booleano. El complemento de un
ele­mento resulta ser
$$\forall{k \in B}{{\overline{k} = {1_{B}/k}} = {\prod\limits_{q \in {\{{{{p \in P_{n}} \mid p} \nmid k}\}}}q}}$$.
Éste es un modelo fácil de desarrollar para poner ejemplos.

**\[Ejemplo 3\]** Partimos de un álgebra de Boole cualquiera y un
elemento no $$0$$ ni $$1$$ cualquie­ra tal
que$$x \in \left( {B \smallsetminus {\{ 0,1\}}} \right)$$. Definimos
ahora un
conjunto$$B_{\leq x}{: = {\{{{{y \in B} \mid {x \cdot y}} = y}\}}}$$y$$B_{\geq x}{: = {\{{{{y \in B} \mid {x \cdot y}} = x}\}}}$$.
Las álgebras de Boole nuevas a considerar son
$$\langle{B_{\leq x},{\{{{0 \equiv 0_{B}},{1 \equiv x}}\}},{\{{+_{B}, \cdot_{B}}\}}}\rangle$$
y
$$\langle{B_{\geq x},{\{{{0 \equiv x},{1 \equiv 1_{B}}}\}},{\{{+_{B}, \cdot_{B}}\}}}\rangle$$.
Consideramos el mismo producto booleano que en el conjunto inicial e
idéntica­mente con la suma booleana. Sólo varía el complemento, de la
siguiente
forma$${y \in B_{\geq x}}\Rightarrow y{' = {\overline{y} + x}}$$y$${y \in B_{\leq x}}\Rightarrow y{' = {\overline{y} \cdot x}}$$.
Es fácil comprobar la validez de esta definición de un álgebra de Boole,
de manera más concreta, que las operaciones son internas y el
complemento declarado es también interno y se comporta como complemento
del nuevo álgebra, esto
es,$${y \in B_{\geq x}}\Rightarrow y{{' \cdot y} = {x \land y}}{{' + y} = 1}$$
que$${y \in B_{\leq x}}\Rightarrow y{{' \cdot y} = {0 \land y}}{{' + y} = x}$$.

**\[Ejemplo 4\]** El álgebra de las proposiciones. Éste es sin duda, el
primer desarrollo que se hizo del álgebra de Boole, hecha por el propio
George Boole en mitad del siglo XIX (edición 1851). Lo desarrolló como
una "Una investigación en las leyes del pensamiento". Amigo suyo que lo
ayudó a penetrar los ambientes académi­cos es Augustus De Morgan. Desde
Aristóteles (que funda por primera vez la ló­gica como ciencia analítica)
en el siglo IV a. C. no había habido ningún adelanto sustancial en la
lógica. Kant (medio siglo antes de Boole) había considerado que la
lógica era un cuerpo de doctrina cerrado y completo (esto es, no había
nada más que decir que lo que ya había desarrollado y escrito
Aristóteles en sus "Tra­tados de Lógica" u "Órganon", hacía ya 2.300
años). Aunque la verdadera revolu­ción se da algunos años más tarde con
Frege, el lógico más importante desde Aristóteles. Si doy estos datos
sobre la historia de la lógica que todos asociaréis más a la filosofía,
que parece queda muy lejos del propósito de unos apuntes de matemáticas
discretas que cubran de la forma más amplia posible los Fundamentos de
Electró­nica en su parte Digital, es porque no queda tan lejos. La idea
de hacer un len­guaje dónde el razonamiento siguiera unas pautas claras
de forma que siempre quedara todo tan cierto como en las matemáticas era
ya antiguo. Aristóteles ya advertía de una cierta in-definición
insuperable de los términos más importantes de la filosofía (en realidad
de casi todos los conceptos de la vida ordinaria): "exis­ten conceptos o
ideas que corresponden con la realidad que no se usan de forma equívoca
-- esto es, su uso no es equívoco, este mismo concepto, palabra o idea
que hablamos no se refiere a realidades distintas y diferenciadas, de
forma que nos llevan a confusión -- pero tampoco de forma unívoca --
como las definiciones desde axiomas en un lenguaje formal matemático,
así tenemos que existen con­ceptos análogos" (es una glosa de palabras de
Aristóteles). En la Modernidad, dado que el concepto de analogía lleva
aparejado un tratamiento difícil que no lleva fácilmente a certeza, se
intentan buscar criterios de certeza absoluta y unas definiciones que
aparentemente son unívocas y se tratan como tales. Es significativo el
nombre (y la estructura interna) de una importante obra de Spino­za:
"Ética demostrada según el orden geométrico". Será Leibniz quién escriba
ya cumplidamente sobre la necesidad de establecer un léxico
completamente unívoco (una tarea mastodonte, o mejor, imposible) y un
"cálculo" del pensamiento, de forma que "una cuestión como la existencia
de Dios pueda ser resuelto mediante la resolución de unas ecuaciones de
pensamiento" (de nuevo es una glosa). Se empezaba a buscar con ansiedad
una mecanización del pensamiento. Esta idea fue muy fructífera, dando un
primer paso hacia ella George Boole que hace un ál­gebra de las
proposiciones. Esta álgebra no era más amplia que la de Aristóteles,
pero permitía el cálculo al modo matemático. De aquí a la llegada de
Frege, ya, Charles Babbage diseña y realiza (sin éxito debido al trabajo
de mecanizado ex­cesivamente minucioso que requería el diseño) una
computadora universal me­cánica (mediante engranajes) prácticamente
similar al modelo de Von Neumann. La condesa de Lovelace (Ada) es el
matemático que hace los primeros progra­mas en lenguaje ensamblador de la
máquina de Babbage. La primera programa­dora de la historia. Después de
Frege siguen los desarrollos con gente como Ber­trand Russell, David
Hilbert y otros, hasta los increíbles resultados de Gödel que ponen
punto final a muchas de las pretensiones de mecanización del
pensamiento, pero que son ya base de la computación moderna, siendo los
trabajos definitivos los de Alan Turing. Como veis el camino recorrido
es largo y complicado, siendo el momento crucial para el arranque de la
ingeniería digital los trabajos de George Boole. No he mencionado el
papel de las máquinas de cifrado y descifrado de mensajes en la Gran
Guerra y la II Guerra Mundial (en las que intervinieron muchos de las
mentes antes mencionadas).

De manera un tanto informal podemos ver una proposición (una frase que
afirma o niega una propiedad de un objeto, una relación entre objetos o
la existencia del mismo, una frase que ha de ser o verdadero,
$$1_{B}{{: = V} \equiv \mathbf{\mathit{true}}}$$, a falso,
$$0_{B}{{: = F} \equiv \mathbf{\mathit{false}}}$$) o conjunto de
proposiciones pueden ser operadas mediante la conjunción 'y', A 'y' B es
verdadero si A es verdadero y B es verdadero a la vez y falso en
cualquier otro caso. La disyunción sería la 'o', siendo A 'o' B
verdadero con que A sea verdadero o lo sea B, siendo falso sólo cuando A
es falso y B es falso a la vez. La notación más habitual es
$${{+ {: = \vee}} \equiv \text{or}} \equiv {\mid \mid}$$y$${{\cdot {: = \land}} \equiv \text{and}} \equiv {\&\&}$$.
Para el 'no' (negación) tenemos
que$${{\overline{\phantom{A}}{: = {\neg\phantom{A}}}} \equiv \text{not}}{\phantom{A} \equiv {/\phantom{A}}}$$.
El conjunto de Boole es el conjunto de proposiciones de la que partamos.

De manera más formal se considera un elemento del álgebra de Boole de la
lógica a las clases de equivalencia de las proposiciones equivalentes
lógicamente (en su valor de verdad o falsedad) entre sí.

**\[Ejemplo 5\]** El álgebra de conmutación. Este es el álgebra de Boole
más sencillo que hay. $$B{{: = B_{2}} \equiv {\{{0,1}\}}}$$. Las
operaciones las concretaremos en tablas:

enewcommandrraystretch2 $$\begin{bmatrix}
   + & 0 & 1 \\
  0 & 0 & 1 \\
  1 & 1 & 1
  \end{bmatrix}\begin{bmatrix}
   \cdot & 0 & 1 \\
  0 & 0 & 0 \\
  1 & 0 & 1
  \end{bmatrix}\begin{bmatrix}
  \overline{} & 0 & 1 \\
   & 1 & 0
  \end{bmatrix}$$

y podréis comprobar fácilmente que se cumplen todos los postulados de
Huntington. Ésta será usada frecuentemente durante el curso. Esta
álgebra está contenido en todo álgebra de Boole.

**\[Ejemplo 6\]** El álgebra de Boole de 4 elementos. Este es el álgebra
de Boole generada por un conjunto de 2 elementos. Es singular en el
sentido que sólo tiene 3 niveles, el más bajo
$$\{{0{{: = {\{\}}} \equiv \varnothing}}\}$$, el intermedio
$$\{{{\{\alpha\}},{\{\beta\}}}\}$$, y el superior
$$\{{1{: = {\{{\alpha,\beta}\}}}}\}$$.
$$B{{: = B_{4}} \equiv {\{{0,a,b,1}\}}}$$. Las operaciones las
concretaremos en tablas:

$$\begin{bmatrix}
   + & 0 & a & b & 1 \\
  0 & 0 & a & b & 1 \\
  a & a & a & 1 & 1 \\
  b & b & 1 & b & 1 \\
  1 & 1 & 1 & 1 & 1
  \end{bmatrix}\begin{bmatrix}
   + & 0 & a & b & 1 \\
  0 & 0 & 0 & 0 & 0 \\
  a & 0 & a & 0 & a \\
  b & 0 & 0 & b & b \\
  1 & 0 & a & b & 1
  \end{bmatrix}\begin{bmatrix}
  \overline{} & 0 & a & b & 1 \\
   & 1 & b & a & 0
  \end{bmatrix}$$

y podréis comprobar fácilmente que se cumplen todos los postulados de
Huntington si cam­biáis $$a$$ por $$\{\alpha\}$$, $$b$$ por
$$\{\beta\}$$, $$1$$ por $$\{{{\{\alpha\}},{\{\beta\}}}\}$$ y $$0$$ por
el conjunto vacío $$\varnothing$$.

**\[Ejemplo 7\]** El álgebra de Boole de 8 elementos. Este es el álgebra
de Boole generada por un conjunto de 3 elementos. Es singular en el
sentido que sólo tiene 4 niveles, el más bajo $$\{ 0\}$$, el de átomos
$$\{{a,b,c}\}$$, el de hiperátomos $$\{{A,B,C}\}$$ y el superior
$$\{ 1\}$$. Los niveles de átomos y de hiperátomos son especialmente
importantes, siendo esta álge­bra de Boole, la más pequeña que los
diferencia. Sería:

$$B{{: = B_{8}} \equiv {\{{0,a,b,c,A,C,B,1}\}}}$$.

Las operaciones las concretaremos en tablas:

enewcommandrraystretch2 $$\begin{bmatrix}
   + & 0 & a & b & c & A & C & B & 1 \\
  0 & 0 & a & b & c & A & C & B & 1 \\
  a & a & a & A & C & A & C & 1 & 1 \\
  b & b & A & b & B & A & 1 & B & 1 \\
  c & c & C & B & c & 1 & C & B & 1 \\
  A & A & A & A & 1 & A & 1 & 1 & 1 \\
  C & C & C & 1 & C & 1 & C & 1 & 1 \\
  B & B & 1 & B & B & 1 & 1 & B & 1 \\
  1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
  \end{bmatrix}\begin{bmatrix}
   \cdot & 0 & a & b & c & A & C & B & 1 \\
  0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
  a & 0 & a & 0 & 0 & a & a & 0 & a \\
  b & 0 & 0 & b & 0 & b & 0 & b & b \\
  c & 0 & 0 & 0 & c & 0 & c & c & c \\
  A & 0 & a & b & 0 & A & a & b & A \\
  C & 0 & a & 0 & c & a & C & c & C \\
  B & 0 & 0 & b & c & b & c & B & B \\
  1 & 0 & a & b & c & A & C & B & 1
  \end{bmatrix}$$

$$\begin{bmatrix}
  \neg & 0 & a & b & c & A & C & B & 1 \\
   & 1 & B & C & A & c & b & a & 0
  \end{bmatrix}\begin{Bmatrix}
  {{B_{8}\rightarrow\wp}{\{{\alpha,\beta,\gamma}\}}} & {0\rightarrow\varnothing} \\
  {a\rightarrow{\{\alpha\}}} & {b\rightarrow{\{\beta\}}} \\
  {c\rightarrow{\{\gamma\}}} & {A\rightarrow{\{{\alpha,\beta}\}}} \\
  {C\rightarrow{\{{\gamma,\alpha}\}}} & {B\rightarrow{\{{\beta,\gamma}\}}} \\
  {1\rightarrow{\{{\alpha,\beta,\gamma}\}}} & {{x \cdot y}\rightarrow{x \cap y}} \\
  {{x + y}\rightarrow{x \cup y}} & {\overline{x}\rightarrow{{\{{\alpha,\beta,\gamma}\}} \smallsetminus x}}
  \end{Bmatrix}$$

y podréis comprobar fácilmente que se cumplen todos los postulados de
Huntington si te­néis en cuenta los cambios aconsejados en el cuadro
entre llaves, dónde las flechas quieren decir "substituir por".

**\[Ejemplo 8\]** El álgebra de Boole de 16 elementos. Este es el
álgebra de Boole generada por un conjunto de 4 elementos. Es ya un
álgebra de Boole completamente regular. Tiene 5 niveles, el más bajo el
$$\{ 0\}$$, el de átomos $$\{{\alpha,\beta,\gamma,\delta}\}$$, el de
hiperátomos $$\{{A,B,\Gamma,\Delta}\}$$, el intermedio
$$\{{a,b,c,d,e,f}\}$$y finalmente el nivel superior con el $$\{ 1\}$$.
Sería:

$$B{{: = B_{16}} \equiv {\{{0,\alpha,\beta,\gamma,\delta,a,b,c,d,e,f,A,B,\Gamma,\Delta,1}\}}}$$.

Las operaciones las concretaremos en tablas:

enewcommandrraystretch2 $$\begin{bmatrix}
   + & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & A & B & \Gamma & \Delta & 1 \\
  0 & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & A & B & \Gamma & \Delta & 1 \\
  \alpha & \alpha & \alpha & a & b & c & a & b & c & A & B & \Gamma & A & B & \Gamma & 1 & 1 \\
  \beta & \beta & a & \beta & d & e & a & A & B & d & e & \Delta & A & B & 1 & \Delta & 1 \\
  \gamma & \gamma & b & d & \gamma & f & A & b & B & \Gamma & \Delta & f & A & 1 & \Gamma & \Delta & 1 \\
  \delta & \delta & c & e & f & \delta & B & \Gamma & c & \Delta & e & f & 1 & B & \Gamma & \Delta & 1 \\
  a & a & a & a & A & B & a & A & B & A & \Delta & 1 & A & B & 1 & 1 & 1 \\
  b & b & b & A & b & \Gamma & A & b & B & A & 1 & \Gamma & A & 1 & \Gamma & 1 & 1 \\
  c & c & c & B & \Gamma & c & B & \Gamma & c & 1 & B & \Gamma & 1 & B & 1 & \Delta & 1 \\
  d & d & A & d & d & \Delta & A & A & 1 & d & \Delta & \Delta & A & 1 & 1 & \Delta & 1 \\
  e & e & B & e & \Delta & e & B & 1 & B & \Delta & e & \Delta & 1 & B & 1 & \Delta & 1 \\
  f & f & \Gamma & \Delta & f & f & 1 & \Gamma & \Gamma & \Delta & \Delta & f & 1 & 1 & \Gamma & \Delta & 1 \\
  A & A & A & A & A & 1 & A & A & 1 & A & 1 & 1 & A & 1 & 1 & 1 & 1 \\
  B & B & B & B & 1 & B & B & 1 & B & 1 & B & 1 & 1 & B & 1 & 1 & 1 \\
  \Gamma & \Gamma & \Gamma & 1 & \Gamma & \Gamma & 1 & \Gamma & \Gamma & 1 & 1 & \Gamma & 1 & 1 & \Gamma & 1 & 1 \\
  \Delta & \Delta & 1 & \Delta & \Delta & \Delta & 1 & 1 & 1 & \Delta & \Delta & \Delta & 1 & 1 & 1 & \Delta & 1 \\
  1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
  \end{bmatrix}$$

$$\begin{bmatrix}
\neg & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & A & B & \Gamma & \Delta & 1 \\
 & 1 & \Delta & \Gamma & B & A & f & e & d & c & b & a & \delta & \gamma & \beta & \alpha & 0
\end{bmatrix}$$

$$\begin{bmatrix}
 \cdot & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & A & B & \Gamma & \Delta & 1 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\alpha & \alpha & \alpha & 0 & 0 & 0 & \alpha & \alpha & \alpha & 0 & 0 & 0 & \alpha & \alpha & \alpha & 0 & \alpha \\
\beta & \beta & 0 & \beta & 0 & 0 & \beta & 0 & 0 & \beta & \beta & 0 & \beta & \beta & 0 & \beta & \beta \\
\gamma & \gamma & 0 & 0 & \gamma & 0 & 0 & \gamma & 0 & \gamma & 0 & \gamma & \gamma & 0 & \gamma & \gamma & \gamma \\
\delta & \delta & 0 & 0 & 0 & \delta & 0 & 0 & \delta & 0 & \delta & \delta & 0 & \delta & \delta & \delta & \delta \\
a & a & \alpha & \beta & 0 & 0 & a & \alpha & \alpha & \beta & \beta & 0 & a & a & \alpha & \beta & a \\
b & b & \alpha & 0 & \gamma & 0 & \alpha & b & \alpha & \gamma & 0 & \gamma & a & a & \alpha & \beta & b \\
c & c & \alpha & 0 & 0 & \delta & \alpha & \alpha & c & 0 & \delta & \delta & \alpha & c & c & \delta & c \\
d & d & 0 & \beta & \gamma & 0 & \beta & \gamma & 0 & d & \beta & \gamma & d & \beta & \gamma & d & d \\
e & e & 0 & \beta & 0 & \delta & \beta & 0 & \delta & \beta & e & \delta & \beta & e & \delta & e & e \\
f & f & 0 & 0 & \gamma & \delta & 0 & \gamma & \delta & \gamma & \delta & f & \gamma & \delta & f & f & f \\
A & A & \alpha & \beta & \gamma & 0 & a & b & \alpha & d & e & \gamma & A & a & b & d & A \\
B & B & \alpha & \beta & 0 & \delta & a & \alpha & c & \beta & e & \delta & a & B & c & d & B \\
\Gamma & \Gamma & \alpha & 0 & \gamma & \delta & \alpha & b & c & \gamma & \delta & f & b & c & \Gamma & f & \Gamma \\
\Delta & \Delta & 0 & \beta & \gamma & \delta & \beta & \gamma & \delta & d & e & f & d & e & f & \Delta & \Delta \\
1 & 1 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & A & B & \Gamma & \Delta & 1
\end{bmatrix}$$

y podréis comprobar fácilmente que se cumplen todos los postulados de
Huntington, con solo tener en cuenta que todos los elementos se pueden
poner en función de $$\alpha\beta\gamma\delta$$y sumas de ellos. Las
sumas de dos de los anteriores elementos son $$abcdef$$y las sumas de
tres de ellos son $$AB\Gamma\Delta$$.

**\[Ejemplo 9\]** El álgebra de Boole de los conjuntos que se pueden
expresar como **unión des­junta finita de subintervalos genéricos de
$$\lbrack 0,1\rbrack \cap \mathbb{Q}$$. Definimos por conveniencia
$$\mathbf{\mathrm{I}}_{\mathbb{Q}} ≝ \left\lbrack {0,1} \right\rbrack_{\mathbb{Q}}$$**.
Para esto haremos abs­tracción de cualquier conjunto finito de puntos de
**$$\mathbf{\mathrm{I}}_{\mathbb{Q}}$$**, esto es, consideraremos que
dos conjuntos son iguales si su diferencia simétrica (la unión de las
diferencias, los elementos que no son comunes de ambos conjuntos) es
vacía o es un conjunto finito de puntos. Esta álgebra de Boole tiene un
cardinal infinito numerable (como el cardinal de los números naturales).
Lo más importante es que no puede desarrollarse de manera semejante a
como desarrolla­mos el álgebra de las partes de un conjunto. Lo
formalizaremos del siguiente modo:

1.  $$a,{b \in \mathbf{\mathrm{I}}_{\mathbb{Q}}}{a < b}\Rightarrow\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}} ≝ {\left\lbrack {a,b} \right\rbrack \cap \mathbb{Q}} ≝ \left\{ {{x \in \mathbf{\mathrm{I}}_{\mathbb{Q}}} \mid {{a \leq x} \leq b}} \right\}$$

    1.  Si escribimos $$\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}}$$
        entonces $${a < {b \land a}} \neq b$$.

    2.  Sea
        $$\mathbf{II}_{\mathbb{Q}} ≝ \left\{ {\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}} \mid {a,{{{b \in {I_{\mathbb{Q}} \land a}} < {b \land a}} \neq b}}} \right\}$$.

    3.  Sea
        $$\mathbf{\mathrm{III}}_{\mathbb{Q}} ≝ {\left\{ {{A \in {\wp\left( I_{\mathbb{Q}} \right)}} \mid {{A = \mathbf{\cup}_{\lambda \in \Lambda}}I_{\lambda}\forall{\lambda \in \Lambda}{I_{\lambda} \in {\mathbf{\mathrm{II}}_{\mathbb{Q}}{{\#\left( \Lambda \right)} \in \widetilde{\mathbb{N}}}}}}} \right\} \cup \left\{ \varnothing \right\}}$$
        .

    4.  Sea
        $$\mathit{Fin}\left( I_{\mathbb{Q}} \right) ≝ \left\{ {{A \in \wp}\left( I_{\mathbb{Q}} \right) \mid \#{(A) \in \widetilde{\mathbb{N}}}} \right\}$$.

    5.  $$A,B{\in}{\wp\left( \mathbf{\mathrm{I}}_{\mathbb{Q}} \right)}{A \approx B} ≝ {\#{\left( {A \mathbin{\vartriangle}B} \right) \in \widetilde{\mathbb{N}}}}$$.
        Esta relación es de equivalencia.

        1.  Reflexiva
            $$\#{\left( {A \mathbin{\vartriangle}A} \right) = \#}{{(\varnothing) = 0} \in \widetilde{\mathbb{N}}}$$.
            Luego $$A \approx A$$.

        2.  Simétrica
            $$A \mathbin{\vartriangle}{B = B} \mathbin{\vartriangle}A.\Rightarrow.A \approx B\Leftrightarrow B \approx A$$.

        3.  Transitiva
            $$A \approx {B \land B} \approx C\Rightarrow A \approx C$$.

            - $$\#{{\left( {A \mathbin{\vartriangle}B} \right) = n_{1}} \in {\widetilde{\mathbb{N}} \land \#}}{{\left( {B \mathbin{\vartriangle}C} \right) = n_{2}} \in \widetilde{\mathbb{N}}}.\Rightarrow.\#{{\left( {A \mathbin{\vartriangle}C} \right) \leq {n_{1} + n_{2}}} \in \widetilde{\mathbb{N}}}$$.
              Y queda de­mostrada la propiedad transitiva.

    6.  A partir de aquí hablaremos de $$⟦A⟧$$para hablar de la clase de
        equivalencia de $$A \in \mathbf{\mathrm{III}}_{\mathbb{Q}}$$bajo
        la relación de equivalencia $$\approx$$.

    7.  A partir de aquí hablaremos de nuestro conjunto
        $$\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}(0,1) ≝ \left\{ {{⟦A⟧} \mid {A \in \mathbf{\mathrm{III}}_{\mathbb{Q}}}} \right\}$$

    8.  Nuestro conjunto de Boole será
        $$B ≝ {\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}(0,1)}$$.

    9.  El $$0 ≝ {⟦\varnothing ⟧}$$.

    10. El $$1 ≝ {⟦\mathbf{\mathrm{I}}_{\mathbb{Q}}⟧}$$.

    11. Ahora veremos unas operaciones muy cercanas a la unión, la
        intersección y el com­plemento, que realmente nos dan un álgebra
        de Boole sobre
        $$\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}$$:

        $$\begin{matrix}
              {{⟦A⟧},{{⟦B⟧} \in \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}}} \\
              {{{⟦A⟧} + {⟦B⟧}} ≝ {⟦{A \cup B}⟧}} \\
              {{{⟦A⟧} \cdot {⟦B⟧}} ≝ {⟦{A \cap B}⟧}} \\
              {\overline{⟦A⟧} ≝ {⟦{\lbrack 0,1\rbrack_{\mathbb{Q}} \smallsetminus A}⟧}}
              \end{matrix}$$

    12. Convenio de
        notación:$${⟦{a,b}⟧} ≝ {⟦\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}}⟧}$$.
        Estos conjuntos serán nuestros subintervalos genéricos del
        intervalo genérico unidad.

    13. Sea una sucesión finita de un número par $$2 \cdot n$$ de
        elementos de $$\lbrack 0,1\rbrack_{\mathbb{Q}}$$, estricta­mente
        creciente
        $${{{{{{{0_{\mathbb{Q}} \leq a_{1}} < b_{1}} < a_{2}} < b_{2}} < \ldots} < a_{n}} < b_{n}} \leq 1_{\mathbb{Q}}$$
        dispuestos como

        $$⟦{a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}}⟧$$definirán los
        elementos de
        $$\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}$$,
        aparte de
        $${⟦⟧} ≝ {{{{⟦\varnothing ⟧} = {⟦{\{ 0\}}⟧}} = {⟦{\{ 1\}}⟧}} = 0_{\mathbf{\mathrm{I}}_{B}^{\mathbf{\mathrm{GEN}}}}}$$.

    14. Si escribimos
        $$⟦{a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}}⟧$$, significamos
        ya (suponemos que es un hecho que)
        $${{{{{{{0_{\mathbb{Q}} \leq a_{1}} < b_{1}} < a_{2}} < b_{2}} < \ldots} < a_{n}} < b_{n}} \leq 1_{\mathbb{Q}}$$.

    15. Ahora ya definimos (notación):

        $$\begin{matrix}
              {{⟦{a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}}⟧} ≝ {{⟦{\{{{x \in {\lbrack 0,1\rbrack}_{\mathbb{Q}}} \mid \exists{{{1 \leq k} \leq n} \in \mathbb{N}}{x \in {\lbrack{a_{k},b_{k}}\rbrack}_{\mathbb{Q}}}}\}}⟧} \equiv}} \\
              {\equiv {⟦{\mathbf{\cup}_{k = 1}^{n}{\lbrack{a_{k},b_{k}}\rbrack}}⟧}}
              \end{matrix}$$.

    16. Ahora ya tenemos el conjunto de Boole que buscábamos:

        $$\left\lbrack {⟦0,1⟧} \right\rbrack_{\mathbf{\mathrm{I}}} ≝ {\left\{ {{⟦{a_{1,}b_{1,}\ldots,a_{n},b_{n}}⟧} \mid {\exists{n \in \mathbb{N}}{{{{{{0_{\mathbb{Q}} \leq a_{1}} < b_{1}} < \ldots} < a_{n}} < b_{n}} \leq 1_{\mathbb{Q}}}}} \right\} \cup \left\{ {⟦⟧} \right\}}$$.

Que las uniones, complementos e intersecciones de intervalos genéricos
finitos siguen siendo intervalos genéricos finitos es claro desde el
principio. Sin embargo voy a exponer la cabalística, hacer las cuentas
vamos, para que no quede lugar a dudas. Con toda esta comprobación (o
re-definición) de que $$B$$ es cerrado bajo las distintas operaciones es
laborioso, un tanto enojoso.

La operación de complemento queda de la siguiente manera, y aunque aún
no podemos comprobar aún su corrección, si queda claro que es un
operación unaria interna:

$$A^{I} := \begin{cases}
  \llbracket 0, a_1, b_1, a_2, \ldots, b_{n-1}, a_n, b_n, 1 \rrbracket & \text{si } a_1 \neq 0 \land b_n \neq 1 \\
  \llbracket b_1, a_2, \ldots, b_{n-1}, a_n, b_n, 1 \rrbracket & \text{si } a_1 = 0 \land b_n \neq 1 \\
  \llbracket b_1, a_2, \ldots, b_{n-1}, a_n \rrbracket & \text{si } a_1 = 0 \land b_n = 1 \\
  \llbracket 0, a_1, b_1, a_2, \ldots, b_{n-1}, a_n \rrbracket & \text{si } a_1 \neq 0 \land b_n = 1 \\
  \llbracket \varnothing \rrbracket & \text{si } A = \llbracket 0, 1 \rrbracket \\
  \llbracket 0, 1 \rrbracket & \text{si } A = \llbracket \varnothing \rrbracket
\end{cases}$$

De dónde obtenemos $\forall A \in B, \exists A^{I} \in B$.

Tenemos que
$0 \in B, 0 := \llbracket \varnothing \rrbracket \equiv \llbracket \rrbracket$
y $1 \in B, 1 := \llbracket 0,1 \rrbracket$, y
$0^{I} = 1 \land 1^{I} = 0$. Además observamos con claridad que
$\forall A \in B, \exists A^{I} \in B$ tal que
$A + A^{I} = \llbracket \mathbf{\mathrm{I}}_{\mathbb{Q}} \rrbracket = 1$
y $A \cdot A^{I} = \llbracket \rrbracket = 0$. Además de
$\forall A \in B, (A^{I})^{I} = A$. Así nos queda
$A^{I} \equiv \overline{A}$ si se verifican los demás axiomas.

La suma quedará de la siguiente forma:

$$\forall A, B \in \left\lbrack \llbracket 0,1 \rrbracket \right\rbrack_{\mathbf{\mathrm{I}}} \exists (A,B) \subset (A \times B), A + B \triangleq \llbracket A \cup B \rrbracket$$

El producto seguirá un camino par:

$$\forall A, B \in \left\lbrack \llbracket 0,1 \rrbracket \right\rbrack_{\mathbf{\mathrm{I}}} \exists (A,B) \subset (A \times B), A \cdot B \triangleq \llbracket A \cap B \rrbracket$$

Sólo queda ver que efectivamente las operaciones son internas:

Prueba:

1.  Ahora vamos a desarrollar la suma de forma recurrente:

    $$B \in \left\lbrack \llbracket 0,1 \rrbracket \right\rbrack_{\mathbf{\mathrm{I}}}, B = \llbracket a_{1}^{B},b_{1}^{B},\ldots,a_{n}^{B},b_{n}^{B} \rrbracket$$
    $$A = \llbracket a_{1}^{A},b_{1}^{A},\ldots,a_{m}^{A},b_{m}^{A} \rrbracket$$

    Comenzaremos por $m = 0$ y algunos casos especiales:

    $$B + A := \begin{cases}
      \llbracket \varnothing \rrbracket & \text{si } A = \llbracket \varnothing \rrbracket \land B = \llbracket \varnothing \rrbracket \\
      A & \text{si } B = \llbracket \varnothing \rrbracket \\
      B & \text{si } A = \llbracket \varnothing \rrbracket \\
      1 & \text{si } \exists A \in A, \exists B \in B : \overline{B} \subseteq A \lor \overline{A} \subseteq B \\
      A & \text{si } \exists A \in A, \exists B \in B : B \subseteq A \\
      B & \text{si } \exists A \in A, \exists B \in B : A \subseteq B
    \end{cases}$$

    Para el caso general de $m = 1$:

    $$\begin{align*}
    B + A &:= \begin{cases}
      \llbracket a_1^A, b_1^A, a_1^B, b_1^B, \ldots, a_n^B, b_n^B \rrbracket & \text{si } b_1^A < a_1^B \\
      \llbracket a_1^A, b_1^B, a_2^B, b_2^B, \ldots, a_n^B, b_n^B \rrbracket & \text{si } b_1^A \ge a_1^B \land b_1^A \le b_1^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_n^B, b_n^B, a_1^A, b_1^A \rrbracket & \text{si } a_1^A > b_n^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_{n-1}^B, b_{n-1}^B, a_n^B, b_1^A \rrbracket & \text{si } a_1^A \le b_n^B \land a_1^A \ge a_n^B \land b_1^A > b_n^B \\
      \llbracket a_1^A, b_1^A, a_k^B, b_k^B, \ldots, a_n^B, b_n^B \rrbracket & \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A > b_{k-1}^B \land b_1^A < a_k^B \\
      \llbracket a_1^A, b_k^B, a_{k+1}^B, b_{k+1}^B, \ldots, a_n^B, b_n^B \rrbracket & \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A \ge a_k^B \land b_1^A \le b_k^B
    \end{cases} \\[1em]
    &\phantom{:=} \begin{cases}
      \llbracket a_1^B, b_1^B, \ldots, b_{k-1}^B, a_1^A, b_1^A, a_k^B, b_k^B, \ldots \rrbracket & \text{si } \exists k<n : a_1^A > b_{k-1}^B \land a_1^A \le a_k^B \land b_1^A < a_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^A, b_k^B, a_{k+1}^B, \dots \rrbracket & \text{si } \exists l<k<n : a_1^A \ge b_{l-1}^B \land a_1^A \le a_l^B \land b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^B, b_k^B, a_{k+1}^B, \dots \rrbracket & \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^B, b_1^A, a_{k+1}^B, \dots \rrbracket & \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A > b_k^B \land b_1^A < a_{k+1}^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^B, b_l^B, a_1^A, b_1^A, a_k^B, \dots \rrbracket & \text{si } \exists l<k<n : a_1^A > b_l^B \land a_1^A < a_{l+1}^B \land b_1^A > b_{k-1}^B \land b_1^A < a_k^B
    \end{cases}
    \end{align*}$$

    Para el caso $m = 1$ o $m = 0$ y especiales queda demostrado el
    cerramiento de $B$ bajo esta suma reducida. El caso siguiente se
    construye con facilidad por recurrencia en cualquier número finito
    de pasos.

    Para cualquier $m > 1$:

    $$B + A := \begin{cases}
      \sum_{i=1}^{m} \left( B + \llbracket a_i^A, b_i^A \rrbracket \right) & \text{si } 1 \le i \le m, A_0 := \llbracket \varnothing \rrbracket, A_{i+1} := A_i + \llbracket a_i^A, b_i^A \rrbracket
    \end{cases}$$

    Queda demostrado que toda suma da como resultado un conjunto finito
    de intervalos genéricos.

    A su vez el producto lo vamos a definir de forma recursiva también,
    comenzando primero con $A$ siendo la clase de un solo intervalo
    genérico, o la clase del vacío, además de algunos casos especiales.

    $$B \cdot A := \begin{cases}
      \llbracket \varnothing \rrbracket & \text{si } A = \llbracket \varnothing \rrbracket \lor B = \llbracket \varnothing \rrbracket \\
      A & \text{si } B = 1 \\
      B & \text{si } A = 1 \\
      \llbracket \varnothing \rrbracket & \text{si } \exists A \in A, B \in B : B \subseteq \overline{A} \lor A \subseteq \overline{B} \\
      A & \text{si } \exists A \in A, B \in B : A \subseteq B \\
      B & \text{si } \exists A \in A, B \in B : B \subseteq A
    \end{cases}$$

    Para el caso general de $m = 1$:

    $$\begin{align*}
    B \cdot A &:= \begin{cases}
      \llbracket a_1^A, a_1^B \dots \rrbracket & \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A \ge b_{k-1}^B \land b_1^A < a_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_k^B, b_1^A \rrbracket & \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^A, b_1^B, \ldots, a_{k-1}^B \dots \rrbracket & \text{si } a_1^A \ge a_1^B \land a_1^A \le b_1^B \land \exists k<n : b_1^A \ge b_{k-1}^B \land b_1^A < a_k^B \\
      \llbracket a_1^A, b_1^B, a_2^B, b_2^B, \ldots, a_k^B, b_1^A \rrbracket & \text{si } a_1^A \ge a_1^B \land a_1^A \le b_1^B \land \exists k<n : b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^A, b_l^B, \dots, a_k^B, b_1^A \rrbracket & \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^A, b_l^B, \dots, a_{k-1}^B, b_{k-1}^B \rrbracket & \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A > b_{k-1}^B \land b_1^A < a_k^B
    \end{cases}
    \end{align*}$$

    Para el caso $m > 1$:

    $$B \cdot A := \begin{cases}
      \sum_{i=1}^{m} \left( B \cdot \llbracket a_i^A, b_i^A \rrbracket \right) & \text{si } 1 \le i \le m, A_0 := \llbracket \varnothing \rrbracket, A_{i+1} := A_i + \llbracket a_i^A, b_i^A \rrbracket
    \end{cases}$$

Y queda demostrado que la forma del conjunto producto es una clase de
unión finita de subintervalos genéricos. Luego pertenece a nuestro
álgebra de Boole.

Este sistema es muy parecido a un álgebra de conjuntos subálgebra de
algún conjunto po­tencia, por lo que es fácil determinar que se trata de
un álgebra de Boole. Sin embargo su cardinal es
$$\#{\left( {\left( {\mathbb{Q} \times \mathbb{Q}} \right) \times \left( {\mathbb{N} \times \mathbb{N}} \right)} \right) = \#}\left( \mathbb{N} \right)$$.
Veámoslo:

$${{\#\left( \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}} \right)} = {\#\left( {\mathbf{\mathrm{\cup}}\begin{Bmatrix}
  {{⟦\varnothing ⟧},} & & & & & & \\
  {{⟦{a_{1,}b_{1}}⟧},} & & & & & & \\
  {{⟦{a_{1,}b_{1}}⟧},} & {{⟦{a_{2,}b_{2}}⟧},} & & & & & \\
  {{⟦{a_{1,}b_{1}}⟧},} & {{⟦{a_{2,}b_{2}}⟧},} & {{⟦{a_{3,}b_{3}}⟧},} & & & & \\
   \vdots & \vdots & \vdots & \ddots & & & \\
  {{⟦{a_{1,}b_{1}}⟧},} & {{⟦{a_{2,}b_{2}}⟧},} & {{⟦{a_{3,}b_{3}}⟧},} & \ldots & {{⟦{a_{n},b_{n}}⟧},} & & \\
   \vdots & \vdots & \vdots & \ddots & \vdots & \ddots & \\
  \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots
  \end{Bmatrix}} \right)}} \leq$$$${{\leq {1 + {\#\left( {\underset{i \in \mathbb{N}}{\mathbf{\mathrm{\cup}}}\underset{j \in \mathbb{N}}{\mathbf{\mathrm{\cup}}}{\mathbb{Q} \times \mathbb{Q}}} \right)}}} = \#}{\left( {{{\mathbb{N} \times \mathbb{N}} \times \mathbb{Q}} \times \mathbb{Q}} \right) = \#}{\mathbb{N} = \aleph_{0}}$$

En definitiva es un álgebra numerable (del mismo cardinal que los
números naturales). Puesto que el cardinal de los números naturales
$$\mathbb{N}$$no es conmensurable con el de la potencia de ningún
conjunto (es del cardinal infinito más pequeño posible y ningún conjunto
finito tiene como potencia uno infinito), no existe ningún conjunto para
el cual esta álgebra de Boole sea semejante (isomorfa) a un álgebra de
las potencias de un conjunto. Este ejemplo será de utilidad más
adelante, además de darnos un curioso ejemplo de álgebra de Boole nada
común.

**\[Ejemplo 10\]** El álgebra de Boole de los subconjuntos finitos y
cofinitos de los números naturales ($\mathbb{N}$). Consideremos el
conjunto base
$B = \{ X \subseteq \mathbb{N} \mid X \text{ es finito o } \mathbb{N} \setminus X \text{ es finito} \}$.
Las operaciones son las habituales de la teoría de conjuntos:

- **Suma ($+$):** La unión de conjuntos ($\cup$).

- **Producto ($\cdot$):** La intersección de conjuntos ($\cap$).

- **Complemento ($\overline{X}$):** El complementario relativo a
  $\mathbb{N}$ ($\mathbb{N} \setminus X$).

- **Cero ($0$):** El conjunto vacío ($\emptyset$).

- **Uno ($1$):** El conjunto de los naturales ($\mathbb{N}$).

Es inmediato comprobar que el complemento de un conjunto finito es
cofinito (y viceversa), y que la unión o intersección de dos conjuntos
finitos/cofinitos sigue produciendo un conjunto finito o cofinito. Por
tanto, este conjunto es cerrado bajo las operaciones topológicas y
constituye un álgebra de Boole de cardinalidad infinito numerable (igual
que el Ejemplo 9).

Sin embargo, es matemáticamente crucial señalar que **esta álgebra NO es
isomorfa a la del Ejemplo 9**. Mientras que el Ejemplo 9 carece por
completo de átomos (cualquier subintervalo racional puede subdividirse
en dos más pequeños), esta álgebra del Ejemplo 10 **sí es atómica**: sus
átomos son precisamente los conjuntos compuestos por un único número
natural, $\{n\}$. Esta genialidad geométrica demuestra que, en el
infinito, pueden existir álgebras de Boole del mismo cardinal que son
estructuralmente distintas (algo que, como demostramos en el Capítulo 7,
es imposible en las álgebras finitas).

**\[Ejemplo 11\]** El álgebra de las funciones de un álgebra de Boole
sobre otra. Supongamos $$f:{B\rightarrow B}'$$dónde $$f$$ es una
función. Llamaremos
$${\mathtt{F}{({B,B'})}} = {\{{f:{B\rightarrow B}' \mid \forall{x \in B}\exists!{y \in B}'f{{(x)} = y}}\}}$$
a nuestro conjunto de Boole. $$f_{0'}$$ es la función que asigna el cero
de $$B'$$ a cualquier elemento de $$B$$. Igualmente $$f_{1'}$$ es la
función que asigna el uno de $$B'$$ a cualquier elemento de $$B$$. Las
operaciones internas a introducir son:

La suma de funciones:
$$\forall{x \in B}{\lbrack{f + g}\rbrack}{(x)}{: = f}{{(x)} + g}{(x)}$$
.

La multiplicación de funciones:
$$\forall{x \in B}{\lbrack{f \cdot g}\rbrack}{(x)}{: = f}{{(x)} \cdot g}{(x)}$$.

La función complemento:
$$\forall{f \in \mathtt{F}}{({B,B'})}\forall{x \in B}\overline{f}{(x)}{: = \overline{f{(x)}}}$$.

De esta álgebra podemos entresacar otros conjuntos de funciones
interesantes, como. Por ejemplo:

$${\mathtt{\mathit{Hom}}{({B,B'})}} = \begin{Bmatrix}
  f & : & B & \rightarrow & {B'} & \mathbf{\mid} \\
  {\forall{x \in B}} & {\exists!} & {{y \in B}'} & {f{{(x)} = y}} & \mathbf{\mathrm{:}} & \\
   & & & & {f{{(0)} = 0}'} & \land \\
   & & & & {f{{(1)} = 1}'} & \land \\
   & & {\forall x,{y \in B}} & & {f{{({x + y})} = f}{{(x)} + f}{(y)}} & \land \\
   & & {\forall x,{y \in B}} & & {f{{({x \cdot y})} = f}{{(x)} \cdot f}{(y)}} & \land \\
   & & {\forall{x \in B}} & & {f{{(\overline{x})} = \overline{f{(x)}}}} & 
  \end{Bmatrix}$$

y aún otros subconjuntos más pequeños serían las inyecciones de los
anteriores homomorfismos. Si $${B'} \equiv B$$entonces uno de los
conjuntos de aplicaciones más interesantes son los endomorfimos o
isomorfimos en sí mismo.

Además el kernel de cualquier homomorfismo es un subálgebra de $$B$$.
Los homomorfismos de las álgebras booleanas tienen propiedades
interesantes que no veremos aquí.

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

El conjunto ${\mathbb{B}}_2$ es conjunto en **ZFS**[^1], desde el
momento que la el axioma de unión nos asegura que ${\mathbb{B}}_2$ es
conjunto unión de dos conjuntos de un solo elemento,
${\mathbb{B}}_2 \triangleq{ \{0\} } \cup {
\{1\} }$. Los elementos $0 \triangleq\emptyset$ y $1 \triangleq\{
\emptyset, \{ \emptyset \} \}$. De nuevo para definir $1$ como conjunto
necesitamos el axioma de unión (o de pares no ordenados) de **ZFS**,
siendo $1 \triangleq\{0\}\cup\{\{0\}\}$. Podemos ver que $0 \cap 1 =
\emptyset$ por lo que $0 \neq 1$. También $0 \in 1$. Todo este párrafo
constituye la satisfacción de los requerimientos Estructura de Conjunto
y Elementos Constantes[^2].

Tal como hemos definido nuestro modelo de álgebra de Boole, lo primero
que queda claro es que $\vee$ y $\wedge$ son funciones binarias bien
definidas, y esta última es además biyectiva. Luego los axiomas
Operación Binaria Interna $\vee$[^3] y Operación Binaria Interna
$\wedge$[^4] quedan satisfechos.

Los axiomas Elemento Neutro $\vee$[^5] y Elemento Neutro $\wedge$[^6]
(existencia del elemento neutro) quedan directamente satisfechos por
simple inspección de las tablas.

Para el axioma Elemento Neutro $\vee$[^7] observamos que $0 \vee 0 = 0$
y $0 \vee 1 = 1 \vee 0 = 1$ nos muestra el elemento neutro de la suma,
el elemento $0$.

Para el axioma Elemento Neutro $\wedge$[^8] observamos que $1 \wedge 0 =
0 \wedge 1 = 0$ y $1 \wedge 1 = 1$ nos muestra el elemento neutro del
producto, el elemento $1$.

Para los axiomas de conmutatividad solo hay que observar en la
definición de las funciones binarias
$\vee,\wedge: \mathbb{B}_2 \times \mathbb{B}_2
\longrightarrow\mathbb{B}_2$, que $0 \vee 1 = 1 \vee 0 = 1$ y se cumple
Conmutatividad $\vee$[^9], que $0 \wedge 1 = 1 \wedge 0 = 0$ y se cumple
Conmutatividad $\wedge$[^10].

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
queremos comparar, las afirmadas por el postulado Distributividad $\vee$
sobre $\wedge$[^11]. Podemos ver que ambas columnas son idénticas, luego
se cumple el citado postulado.

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

Para el axioma Complementario[^12] observamos que $\neg 0 = 1$ y
$\neg 1 = 0$ y por inspección en las tablas vemos que
$0 \vee \neg 0 = 0 \vee 1 = 1$ y que $0 \wedge \neg 0 = 0 \wedge 1 = 0$
cumpliendo para el elemento $0$ se cumple que
$\exists 1 = \neg 0 \in \mathbb{B}_2$ $1 \vee \neg 1 = 1 \vee 0 = 1$,
que coincide con la ecuación segunda (ecuación: 2.15) de postulado
Complementario[^13] y $1 \wedge \neg 1=1 \wedge 0 = 0$ que coincide con
la tercera ecuación (ecuación: 2.16) de postulado Complementario[^14], e
igualmente para el elemento $1$, $\exists 0 = \neg 1 \in \mathbb{B}_2$
$0 \vee \neg 0 = 0 \vee 1 = 1$ (ecuación: 2.15) y
$0 \wedge \neg 0 =0 \wedge 1 = 0$ (ecuación: 2.16) de postulado
Complementario[^15].

Como las ecuaciones 2.15 y 2.16 se cumplen para $0$ y $1$, esto es,
$\forall x \in \mathbb{B}_2$ como se requiere en la ecuación 2.14, queda
satisfecho el postulado Complementario[^16].

### Independencia de la suma está siempre definida.

Modelo en el que solo falla Operación Binaria Interna $\vee$[^17], esto
es, que la operación suma no es operación interna: no es función, pero
en el sentido que $1 + 1 \notin
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

Modelo en el que no se cumple Operación Binaria Interna $\vee$[^18], en
el sentido que $1 + 1
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

Modelo en el que solo falla Operación Binaria Interna $\wedge$[^19],
esto es, que la operación producto no es operación interna: no es
función. Este es el caso en que $0 \cdot 0 \notin \mathbb{B}$. Ponemos
en ese caso $0 \cdot 0 = x$ pero igualmente podríamos haber dejado en
blanco ese lugar.

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

Modelo en el que solo falla Operación Binaria Interna $\vee$[^20], esto
es, en el sentido que $0
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

Modelo en el que solo falla Elemento Neutro $\vee$[^21], esto es, la
existencia de elemento neutro en la operación binaria interna suma.

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
= 0$ y $1 \cdot 1 = 1$. Luego se cumple Elemento Neutro $\wedge$[^22].

La conmutatividad se hace patente al ver las diagonales inversas de las
tablas de operación, que muestran un único valor. $0 + 1 = 1 + 0 = 0$ y
$0 \cdot 1 = 1 \cdot 0 = 0$. Se cumplen Conmutatividad $\vee$[^23] y
Conmutatividad $\wedge$[^24].

En cuanto a la distribución del producto sobre la suma, veamos si
podemos comprobarla de forma sencilla:
$a \cdot ( b + c ) = (a \cdot b) + (a \cdot
c)$. Sabemos que $b + c = 0$ siempre, y que, pongamos que $a \cdot b = x
\in \mathbb{B}$ y que $a \cdot c = y \in \mathbb{B}$. Ahora bien
$x + y = 0$. Así que todo lo que tenemos que probar es que
$a \cdot 0 = 0$, pero esto es claro en la table del producto. Luego se
cumple Distributividad $\vee$ sobre $\wedge$[^25].

Ahora la distribución de la suma sobre el producto. $a + ( b \cdot c )
= (a + b) \cdot (a + c)$. Sabemos que $a + (b \cdot c) = 0$ siempre, y
que, pongamos que $a + b = 0$ y que $a + c = 0$. Ahora bien $0 \cdot
0 = 0$. Luego se cumple Distributividad $\wedge$ sobre $\vee$[^26].

Nos queda encontrar un complemento para el $0$. Pero encontrar el
complemento solo tiene sentido si existen los dos elementos neutros,
pero en este caso no existe el neutro de la suma: no tiene sentido
buscar el complementario.

### Independencia de la existencia de elemento neutro del producto.

Exponemos un modelo en el que solo falla Elemento Neutro $\wedge$[^27],
esto es, la existencia de elemento neutro en la operación binaria
interna producto.

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

Modelo en que la conmutatividad de la suma Conmutatividad $\vee$[^28] no
se dá, pero si que se dan el resto de postulados.

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
Distributividad $\vee$ sobre $\wedge$[^29] será verdad para $x = 0$ si
$0 = 0 + 0$, cosa que es cierta. Si $x = 1$, la igualdad a verificar
quedaría $1 \cdot ( y + z )
= ( 1 \cdot y ) + ( 1 \cdot z )$ y por Elemento Neutro $\wedge$[^30]
queda $y + z  =  y
+ z$ que no es más que la identidad lógica de la igualdad. Se satisface
Distributividad $\vee$ sobre $\wedge$[^31].

Nos preguntamos por la satisfacción de Distributividad $\wedge$ sobre
$\vee$[^32] $x + ( y \cdot z
) = ( x + y ) \cdot ( x + z )$ en el actual modelo. Procedemos como en
el párrafo anterior, por casos. Si $x = 0$ entonces
$x + ( y \cdot z ) = ( x
+ y ) \cdot ( x + z )$ $\Longrightarrow$ $0 + ( y \cdot z ) = ( 0 + y )
\cdot ( 0 + z )$ $\Longrightarrow$ $0 = 0 \cdot 0$ lo que es cierto.
Para el caso $x = 1$, obtenemos $x + ( y \cdot z ) = ( x + y ) \cdot ( x
+ z )$ $\Longrightarrow$ $1 + ( y \cdot z ) = ( 1 + y ) \cdot ( 1 + z
)$ $\Longrightarrow$ $1 = 1 \cdot 1$. Por lo tanto también se verifica
Distributividad $\wedge$ sobre $\vee$[^33].

Queda comprobado que la conmutatividad de la suma Conmutatividad
$\vee$[^34] es independiente del resto de postulados.

### Independencia de la conmutatividad del producto.

Modelo en que la conmutatividad del producto Conmutatividad
$\wedge$[^35] no se da, pero, si se satisfacen el resto de postulados.

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
$\exists x \in \mathbb{B}$ que no cumplen Distributividad $\wedge$ sobre
$\vee$[^36], $x + ( y \cdot z )
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
distribución Distributividad $\vee$ sobre $\wedge$[^37] e incluso
sabemos que las operaciones son asociativas.

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
  x=1 \wedge y=0 \wedge z=1 &\Longrightarrow \neg \text{Distributividad } \wedge \text{ sobre } \vee
\end{flalign}$$

De dónde efectivamente este modelo no distribuye la suma sobre un
producto. Y la independencia de Distributividad $\wedge$ sobre
$\vee$[^38] queda probada.

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

## Teoremas de Simplificación

Además de los teoremas deducidos directamente de los axiomas, existen
tres teoremas de simplificación de enorme utilidad práctica,
especialmente en la minimización de funciones booleanas.

:::: teorema
Teorema de Adyacencia (Expansión de Shannon) -
$Ady_{\vee, \wedge}$adyacencia Cualquier elemento $a$ puede ser
expandido con respecto a otra variable $b$ y su complemento.
$$\begin{align*}
    \text{Adyacencia en $\vee$: } & a = (a \wedge b) \vee (a \wedge \neg b) \\
    \text{Adyacencia en $\wedge$: } & a = (a \vee b) \wedge (a \vee \neg b)
\end{align*}$$

::: proof
*Proof.* Demostración para la suma: $$\begin{align*}
    a &= a \wedge \top & \text{Axioma de Elemento Neutro ($E_n$)} \\
    a &= a \wedge (b \vee \neg b) & \text{Axioma de Complementarios ($Comp$)} \\
    a &= (a \wedge b) \vee (a \wedge \neg b) & \text{Axioma de Distributividad ($Dist_{\wedge}$)}
\end{align*}$$ La prueba para el producto es estrictamente dual:
$$\begin{align*}
    a &= a \vee \bot & \text{Axioma de Elemento Neutro ($E_n$)} \\
    a &= a \vee (b \wedge \neg b) & \text{Axioma de Complementarios ($Comp$)} \\
    a &= (a \vee b) \wedge (a \vee \neg b) & \text{Axioma de Distributividad ($Dist_{\vee}$)}
\end{align*}$$ ◻
:::
::::

:::: teorema
Teorema de Reducción (Absorción Fuerte) - $Red_{\vee, \wedge}$reduccion
La disyunción de una variable con la conjunción de su complemento y otra
variable, se reduce a la disyunción de ambas variables. $$\begin{align*}
    \text{Para la disyunción: } & a \vee (\neg a \wedge b) = a \vee b \\
    \text{Para la conjunción (Dual): } & a \wedge (\neg a \vee b) = a \wedge b
\end{align*}$$

::: proof
*Proof.* Demostración para la disyunción: $$\begin{align*}
    a \vee (\neg a \wedge b) &= (a \vee \neg a) \wedge (a \vee b) & \text{Axioma de Distributividad ($Dist_{\vee}$)} \\
    &= \top \wedge (a \vee b) & \text{Axioma de Complementarios ($Comp$)} \\
    &= a \vee b & \text{Axioma de Elemento Neutro ($E_n$)}
\end{align*}$$ Demostración dual para la conjunción: $$\begin{align*}
    a \wedge (\neg a \vee b) &= (a \wedge \neg a) \vee (a \wedge b) & \text{Axioma de Distributividad ($Dist_{\wedge}$)} \\
    &= \bot \vee (a \wedge b) & \text{Axioma de Complementarios ($Comp$)} \\
    &= a \wedge b & \text{Axioma de Elemento Neutro ($E_n$)}
\end{align*}$$ ◻
:::
::::

:::: teorema
Teorema del Consenso (Quine) - $Cons_{\vee, \wedge}$consenso En una
expresión con tres variables donde una variable aparece afirmada en un
término, negada en otro, y el tercer término (el consenso) está formado
por las variables restantes, este último término es redundante.
$$\begin{align*}
    \text{Consenso en $\vee$: } & (a \wedge b) \vee (\neg a \wedge c) \vee (b \wedge c) = (a \wedge b) \vee (\neg a \wedge c) \\
    \text{Consenso en $\wedge$: } & (a \vee b) \wedge (\neg a \vee c) \wedge (b \vee c) = (a \vee b) \wedge (\neg a \vee c)
\end{align*}$$

::: proof
*Proof.* Demostración para la versión en $\vee$: $$\begin{align*}
    (a \wedge b) \vee (\neg a \wedge c) \vee (b \wedge c) &= (a \wedge b) \vee (\neg a \wedge c) \vee ((b \wedge c) \wedge \top) & \text{Ax. Neutro ($E_n$)} \\
    &= (a \wedge b) \vee (\neg a \wedge c) \vee ((b \wedge c) \wedge (a \vee \neg a)) & \text{Ax. Comp.} \\
    &= (a \wedge b) \vee (\neg a \wedge c) \vee (a \wedge b \wedge c) \vee (\neg a \wedge b \wedge c) & \text{Dist. y Asoc.} \\
    &= ((a \wedge b) \vee (a \wedge b \wedge c)) \\
    &\quad \vee ((\neg a \wedge c) \vee (\neg a \wedge c \wedge b)) & \text{Conm. y Asoc.} \\
    &= (a \wedge b) \vee (\neg a \wedge c) & \text{Absorción ($Abs_{\vee}$)}
\end{align*}$$ La prueba dual sigue el mismo principio (sumar $\bot$ al
consenso, expandirlo con $(a \wedge \neg a)$, y simplificar usando
absorción). ◻
:::
::::

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

**Propiedad de Paridad de la XOR (Suma Módulo 2):** La operación
$\bigoplus_{i=1}^{n} x_i$ es conocida matemáticamente como la *función
de paridad impar*. Su valor será $\top$ (o 1) si y solo si un número
impar de las variables de entrada $x_i$ tienen valor $\top$.

**Relación entre XOR y XNOR para $n$ variables:** Dado que
$x \odot y = x \oplus y \oplus \top$, cada aplicación sucesiva del
operador $\odot$ es matemáticamente equivalente a aplicar una suma
$\oplus$ y concatenar una constante $\top$. Puesto que la expresión
$\bigodot_{i=1}^{n} x_i$ entrelaza a sus operandos mediante exactamente
$n-1$ operadores de equivalencia, se deduce rigurosamente que:
$$\bigodot_{i=1}^{n} x_i = \left( \bigoplus_{i=1}^{n} x_i \right) \oplus \underbrace{\top \oplus \top \dots \oplus \top}_{n-1 \text{ veces}}$$
Por la propia idempotencia nula de la suma booleana exclusiva
($x \oplus x = \bot$), la suma de $n-1$ constantes $\top$ será igual a
$\bot$ si $n-1$ es par (lo cual ocurre cuando $n$ es impar), y será
igual a $\top$ si $n-1$ es impar (cuando $n$ es par). Por lo tanto:
$$\bigodot_{i=1}^{n} x_i = \begin{cases} 
\bigoplus_{i=1}^{n} x_i & \text{si } n \text{ es impar (es la misma función)} \\
\neg \left( \bigoplus_{i=1}^{n} x_i \right) & \text{si } n \text{ es par (son funciones negadas)}
\end{cases}$$
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

## Estructuras Algebraicas Superiores

Las propiedades demostradas anteriormente para los operadores XOR
($\oplus$) y AND ($\wedge$) permiten dotar al conjunto $B$ de
estructuras algebraicas más ricas y estándar dentro del álgebra
abstracta.

::: teorema
Estructura de Grupo Conmutativogrupo_xor El par $(B, \oplus)$ forma un
**grupo abeliano** (conmutativo), satisfaciendo:

1.  **Clausura:** $\forall a,b \in B, a \oplus b \in B$.

2.  **Asociatividad:** $a \oplus (b \oplus c) = (a \oplus b) \oplus c$.

3.  **Elemento neutro:** Existe $\bot \in B$ tal que
    $a \oplus \bot = a$.

4.  **Elemento inverso (Idempotencia aditiva):** Todo elemento es su
    propio inverso, ya que $a \oplus a = \bot$.

5.  **Conmutatividad:** $a \oplus b = b \oplus a$.
:::

::: teorema
Estructura de Anillo Conmutativo (Anillo Booleano)anillo_booleano La
terna $(B, \oplus, \wedge)$ forma un **anillo conmutativo con elemento
unidad** (comúnmente denominado Anillo Booleano), donde el XOR actúa
como la suma del anillo y el AND como el producto. Se satisfacen todas
las propiedades requeridas:

1.  $(B, \oplus)$ es un grupo abeliano (demostrado arriba).

2.  $(B, \wedge)$ es un monoide conmutativo (asociativo, conmutativo, y
    con elemento neutro $\top$).

3.  **Distributividad:** El producto ($\wedge$) se distribuye sobre la
    suma ($\oplus$), es decir,
    $a \wedge (b \oplus c) = (a \wedge b) \oplus (a \wedge c)$.
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

# Modelos Mentales en Ingeniería: Puertas Lógicas

Tras asentar el rigor algebraico y realizar la transición a la notación
ingenieril ($+, \cdot, 0, 1$), es de vital importancia desarrollar una
intuición electrónica. Un buen diseñador no solo opera ecuaciones;
*piensa* en circuitos, corrientes y topologías lógicas. Este capítulo
actúa como puente conceptual entre la pureza abstracta de Huntington y
la arquitectura física de los computadores.

## La Puerta AND (Conjunción Lógica)

La operación producto $a \cdot b$ se materializa físicamente en la
puerta lógica **AND**.

:::: center
::: circuitikz
(0,0) node\[and port\] (myand) (myand.in 1) node\[anchor=east\] $a$
(myand.in 2) node\[anchor=east\] $b$ (myand.out) node\[anchor=west\]
$a \cdot b$;
:::
::::

Desde una perspectiva ingenieril y de diseño de sistemas, la puerta AND
debe asimilarse bajo los siguientes modelos mentales:

- **Como condición indispensable en un diseño lógico:** En la jerarquía
  de control, la puerta AND representa los requisitos obligatorios. Si
  una acción requiere que la máquina esté encendida ($a=1$) *y* que la
  puerta de seguridad esté cerrada ($b=1$), el AND asegura que *todas*
  las condiciones estructurales se cumplan inexcusablemente.

- **Como función Mínimo (Min):** Si asumimos la cardinalidad ordinal
  $0 < 1$, la puerta AND siempre devuelve el valor más pequeño de todas
  sus entradas. La única manera de que la salida escape del $0$ y sea
  $1$ (nivel alto) es que absolutamente todas las entradas sean $1$.

- **Como Interruptor de Señal (Enmascaramiento):** Si fijamos la entrada
  $b=0$, la salida se fuerza a $0$, cortando el paso de cualquier rastro
  de datos en $a$. Si $b=1$, la puerta \"se abre\" de forma transparente
  y la señal de datos $a$ fluye intacta hacia la salida
  ($a \cdot 1 = a$).

- **Como Producto Aritmético:** A nivel de bit, coincide algebraicamente
  con la multiplicación tradicional: $0 \times 0 = 0$, $0 \times 1 = 0$,
  $1 \times 1 = 1$.

**Generalización a $n$ variables:** Una puerta AND de $n$ entradas
($\prod_{i=1}^n x_i$) sigue comportándose como un estricto detector de
*unanimidad*. Da $1$ única y exclusivamente si las $n$ entradas son $1$.
Con que un solo eslabón falle y valga $0$, toda la cadena colapsa a $0$.

## La Puerta OR (Disyunción Lógica)

La operación suma $a + b$ se materializa físicamente en la puerta lógica
**OR**.

:::: center
::: circuitikz
(0,0) node\[or port\] (myor) (myor.in 1) node\[anchor=east\] $a$
(myor.in 2) node\[anchor=east\] $b$ (myor.out) node\[anchor=west\]
$a + b$;
:::
::::

Nuestros modelos mentales para asimilar la puerta OR son rigurosamente
duales a los de la AND:

- **Como alternativa o \"fallback\" en un diseño práctico:** Representa
  redundancias o caminos opcionales. Hace que un estado global o total
  sea aceptable (es decir, dé $1$) por la sola inclusión o cumplimiento
  de una de sus ramas, compensando las carencias del resto.

- **Como función Máximo (Max):** Devuelve siempre el mayor de los
  valores de entrada. Basta con que detecte un mísero $1$ en cualquiera
  de sus pines para que la salida se erija inmediatamente como $1$.

- **Como Interruptor de Forzado a $1$:** Si fijamos la entrada de
  control $b=1$, la salida se queda anclada permanentemente a $1$,
  independientemente de las fluctuaciones de $a$. Si $b=0$, la puerta
  ignora el nivel de control y deja fluir la señal $a$ inalterada
  ($a + 0 = a$).

**Generalización a $n$ variables:** Una puerta OR de $n$ entradas
($\sum_{i=1}^n x_i$) actúa como un detector ultrasensible al nivel alto.
Escanea $n$ líneas de entrada buscando energía; al menor atisbo de un
único $1$, su salida se dispara a $1$. Solo mantendrá el $0$ si existe
unanimidad absoluta de ceros.

## La Puerta XOR (Suma Exclusiva)

La operación de disyunción exclusiva $a \oplus b$ es matemáticamente una
de las más ricas del álgebra, materializada en la puerta **XOR**.

:::: center
::: circuitikz
(0,0) node\[xor port\] (myxor) (myxor.in 1) node\[anchor=east\] $a$
(myxor.in 2) node\[anchor=east\] $b$ (myxor.out) node\[anchor=west\]
$a \oplus b$;
:::
::::

- **Como Inversor Controlado:** Esta es su aplicación práctica más
  elegante. Si la entrada de control es $0$, la señal de datos pasa
  inalterada ($a \oplus 0 = a$). Pero si la entrada de control es $1$,
  la señal de datos se *invierte* o niega ($a \oplus 1 = \overline{a}$).
  Esto permite cambiar la polaridad de un bus de datos a voluntad, lo
  que lo hace omnipresente en el hardware de criptografía.

- **Como Detector de Diferencia:** Su respuesta es $1$ si y solo si las
  dos entradas tienen niveles distintos. Constituye un comparador de
  desigualdad primario.

- **Como Suma Módulo 2:** Aritméticamente opera como la columna de las
  unidades de una suma binaria que deliberadamente desprecia el acarreo
  hacia la izquierda ($1+1=0$).

**Generalización a $n$ variables:** La generalización a $n$ entradas
($\bigoplus_{i=1}^n x_i$) transfigura el significado intuitivo de la
puerta original. Como ya demostramos en el Capítulo 4, ya no es un
detector general de \"hay un solo 1\". Su modelo mental debe anclarse
como el **Detector de Paridad Impar**. No importa cómo se configuren las
señales de entrada: si el cómputo total de bits $1$ es impar (1, 3,
5\...), la salida arrojará un $1$. Si el recuento arroja un número par
de unos (0, 2, 4\...), la salida arrojará $0$.

## La Puerta XNOR (Equivalencia)

La negación sistemática del XOR es el $a \odot b$, que implementa en
hardware la puerta **XNOR**.

:::: center
::: circuitikz
(0,0) node\[xnor port\] (myxnor) (myxnor.in 1) node\[anchor=east\] $a$
(myxnor.in 2) node\[anchor=east\] $b$ (myxnor.out) node\[anchor=west\]
$a \odot b$;
:::
::::

- **Como Detector de Igualdad ($==$ o $\iff$):** Se dispara a $1$ única
  y exclusivamente si ambas entradas alcanzan idéntico nivel (ambas $0$
  o ambas $1$). Este simple mecanismo fundamenta toda la arquitectura de
  comparadores dentro de las Unidades Aritmético-Lógicas (ALUs) de los
  microprocesadores modernos.

**Generalización a $n$ variables:** El modelo relacional de \"todos
iguales\" fracasa de estrépito al generalizar a
$\bigodot_{i=1}^{n} x_i$. Conectando con los teoremas previos, la
versión generalizada del XNOR sigue estando maniatada al cálculo de
paridades subyacente. Su naturaleza dependerá del cardinal $n$: si $n$
es impar, replica el comportamiento de paridad de la propia puerta XOR.
Si $n$ es par, detecta paridades pares (arrojando $1$ frente a recuentos
pares de bits).

## El Conector de Implicación Lógica ($\implies$)

Aunque los fabricantes de semiconductores no ensamblan una \"puerta
implica\", su modelado algebraico es la piedra angular del control de
ejecución en programación y en las lógicas de estados abstractos.

El conector \"$\implies$\" encarna el contrato semántico \"Si $A$ es
verdad, entonces $B$ también debe serlo\". Sin embargo, las máquinas no
procesan inferencias gramaticales, solo álgebra plana, reduciéndose este
comportamiento a las operaciones primarias:
$$A \implies B \equiv \overline{A} + B$$

¿De dónde sale esta traducción en términos de hardware? Si la señal de
premisa $A$ es falsa ($0$), el circuito asume que el contrato se cumple
\"por defecto vacío\" independientemente de lo que ocurra con el
consecuente $B$. Esto se refleja en el inversor que inyecta
$\overline{A} = 1$ a la puerta OR, garantizando un $1$ en la salida. El
contrato solo se declara roto o falso ($0$) cuando se exige la condición
inicial ($A=1$) pero la máquina defrauda entregando una respuesta
negativa ($B=0$).

## Primera Etapa Práctica: Multiplexores y Demultiplexores

Armados con la intuición cruda de las puertas lógicas, es hora de
fusionarlas para sintetizar las arquitecturas primitivas más cruciales
del trasiego de información en cualquier computadora. El flujo masivo de
bits requiere enrutadores lógicos que los guíen con precisión.

### El Multiplexor (MUX)

Es el análogo digital a la vía conmutada de un ferrocarril. Un MUX de 2
entradas absorbe dos canales de información diferentes ($D_0$ y $D_1$) y
una línea central de decisión que actúa como timón ($S$, de Selección).
De acuerdo al valor de $S$, deja que solo uno de los dos flujos
atraviese el bloque para alcanzar la salida maestra $Y$.

Algebraicamente, esculpimos esta selectividad combinando la habilidad de
\"interruptor de señal\" de dos puertas AND, y unificando el tráfico en
un canal común con una puerta OR tolerante:
$$Y = (\overline{S} \cdot D_0) + (S \cdot D_1)$$ *Despliegue mental del
diseño:* Si forzamos la señal a $S=0$, el brazo derecho de la ecuación
queda bloqueado (multiplicado por $0$) abortando a $D_1$.
Simultáneamente, el brazo izquierdo ve el $0$ invertido, abriendo de par
en par la puerta para que viaje la señal de $D_0$. Si cambiamos el timón
a $S=1$, la ruta de $D_0$ colapsa y el torrente de $D_1$ encuentra paso
libre.

### El Demultiplexor (DEMUX)

Despliega la táctica geométricamente inversa. Atrapa un único flujo
torrencial de datos $D$ y tiene el mandato de derivarlo hacia la ruta
$Y_0$ o hacia la ruta de escape $Y_1$, de nuevo basándose en la orden
ejecutiva $S$. $$\begin{align*}
Y_0 &= \overline{S} \cdot D \\
Y_1 &= S \cdot D
\end{align*}$$ *Despliegue mental del diseño:* Si dictamos $S=0$, la
válvula $Y_1$ se clausura en $0$, y el flujo $D$ atraviesa impertérrito
la válvula $Y_0$. Si comandamos $S=1$, la situación se transpone
simétricamente operando como el disyuntor perfecto del mundo digital.

# Sistemas Axiomáticos de Sheffer (1913)

## Reducción de Operadores

En 1913, Henry M. Sheffer demostró que el álgebra de Boole puede ser
completamente definida utilizando un único operador lógico, en lugar de
los tres (disyunción, conjunción y negación) requeridos por el sistema
de Huntington. Los dos operadores capaces de esta universalidad
funcional son el operador **NAND** (Barra de Sheffer, $\uparrow$) y el
operador **NOR** (Flecha de Peirce, $\downarrow$).

Todos los axiomas de Huntington (1904) de los que hemos partido son
reducibles a un grupo más pequeño y estricto de axiomas basados
exclusivamente en uno de estos dos operadores.

## Axiomatización mediante NAND (Barra de Sheffer)

El sistema axiomático propuesto por Sheffer para la operación NAND
consta de los siguientes cinco postulados sobre una clase $K$:

::: teorema
Postulados de Sheffer (1913) - Operador NANDsheffer_nand

1.  Existen al menos dos elementos distintos en $K$.

2.  Clausura: Para cualesquiera $a, b \in K$, el resultado de
    $a \uparrow b$ también pertenece a $K$.

3.  $(a \uparrow a) \uparrow (a \uparrow a) = a$

4.  $a \uparrow (b \uparrow (b \uparrow b)) = a \uparrow a$

5.  $(a \uparrow (b \uparrow c)) \uparrow (a \uparrow (b \uparrow c)) = ((b \uparrow b) \uparrow a) \uparrow ((c \uparrow c) \uparrow a)$
:::

Es directo demostrar que los axiomas de Huntington implican estos cinco
postulados:

::: proof
*Proof.* Los postulados 1 y 2 son inmediatos y se asumen de base,
garantizando la existencia de los elementos y la definición del operador
binario.

Para demostrar el postulado 3, usamos la equivalencia
$x \uparrow x = \neg x$: $$\begin{align*}
(a \uparrow a) \uparrow (a \uparrow a) &= \neg a \uparrow \neg a & \text{Definición de } \uparrow \\
&= \neg (\neg a) & \text{Definición de } \uparrow \\
&= a & \text{Involución (Doble Negación)}
\end{align*}$$

Para el postulado 4, partimos del lado izquierdo sabiendo que
$x \uparrow 1 = \neg x$: $$\begin{align*}
a \uparrow (b \uparrow (b \uparrow b)) &= a \uparrow (b \uparrow \neg b) & \text{Definición de } \uparrow \\
&= a \uparrow \neg (b \wedge \neg b) & \text{Definición de } \uparrow \\
&= a \uparrow \neg (\bot) & \text{Axioma de Complementarios ($Comp$)} \\
&= a \uparrow \top & \text{Complemento del Neutro} \\
&= \neg (a \wedge \top) & \text{Definición de } \uparrow \\
&= \neg a & \text{Axioma de Elemento Neutro ($E_n$)} \\
&= a \uparrow a & \text{Definición de } \uparrow
\end{align*}$$

Para el postulado 5, desarrollamos ambas partes de la igualdad hasta
alcanzar una expresión booleana idéntica. Empezamos por el lado
izquierdo: $$\begin{align*}
(a \uparrow (b \uparrow c)) \uparrow (a \uparrow (b \uparrow c)) &= \neg (a \uparrow (b \uparrow c)) & \text{Por postulado 3} \\
&= \neg (\neg (a \wedge (b \uparrow c))) & \text{Definición de } \uparrow \\
&= a \wedge (b \uparrow c) & \text{Involución} \\
&= a \wedge \neg (b \wedge c) & \text{Definición de } \uparrow \\
&= a \wedge (\neg b \vee \neg c) & \text{Leyes de De Morgan}
\end{align*}$$

Desarrollamos ahora el lado derecho: $$\begin{align*}
((b \uparrow b) \uparrow a) \uparrow ((c \uparrow c) \uparrow a) &= (\neg b \uparrow a) \uparrow (\neg c \uparrow a) & \text{Definición de } \uparrow \\
&= \neg (\neg b \wedge a) \uparrow \neg (\neg c \wedge a) & \text{Definición de } \uparrow \\
&= (b \vee \neg a) \uparrow (c \vee \neg a) & \text{De Morgan e Involución} \\
&= \neg ((b \vee \neg a) \wedge (c \vee \neg a)) & \text{Definición de } \uparrow \\
&= \neg (\neg a \vee (b \wedge c)) & \text{Axioma de Distributividad ($Dist_\vee$)} \\
&= a \wedge \neg (b \wedge c) & \text{De Morgan e Involución} \\
&= a \wedge (\neg b \vee \neg c) & \text{Leyes de De Morgan}
\end{align*}$$ Al llegar ambos desarrollos a la misma expresión booleana
($a \wedge (\neg b \vee \neg c)$), la igualdad queda estrictamente
demostrada. ◻
:::

## Axiomatización mediante NOR (Flecha de Peirce)

El razonamiento es rigurosamente simétrico si se escoge el operador dual
$\downarrow$.

::: teorema
Postulados de Sheffer Duales - Operador NORsheffer_nor

1.  Existen al menos dos elementos distintos en $K$.

2.  Clausura: Para cualesquiera $a, b \in K$, el resultado de
    $a \downarrow b$ pertenece a $K$.

3.  $(a \downarrow a) \downarrow (a \downarrow a) = a$

4.  $a \downarrow (b \downarrow (b \downarrow b)) = a \downarrow a$

5.  $(a \downarrow (b \downarrow c)) \downarrow (a \downarrow (b \downarrow c)) = ((b \downarrow b) \downarrow a) \downarrow ((c \downarrow c) \downarrow a)$
:::

::: proof
*Proof.* La demostración sigue un patrón idéntico de dualidad. El
postulado 3 se demuestra recordando que $x \downarrow x = \neg x$:
$$\begin{align*}
(a \downarrow a) \downarrow (a \downarrow a) &= \neg a \downarrow \neg a = \neg (\neg a) = a
\end{align*}$$

En el postulado 4, sabiendo que $x \downarrow 0 = \neg x$, el término
interior $b \downarrow (b \downarrow b)$ se evalúa a $\bot$, y por
tanto: $$\begin{align*}
a \downarrow (b \downarrow (b \downarrow b)) &= a \downarrow (b \downarrow \neg b) = a \downarrow \neg (b \vee \neg b) = a \downarrow \neg (\top) = a \downarrow \bot \\
&= \neg (a \vee \bot) = \neg a = a \downarrow a
\end{align*}$$

Para el postulado 5, el proceso dual lleva ambos lados de la ecuación a
la forma idéntica $a \vee (\neg b \wedge \neg c)$. ◻
:::

# Estructura de Anillo y Cuerpo Booleano

## Anillos Booleanos

Un álgebra de Boole puede ser interpretada desde la perspectiva del
álgebra abstracta clásica como un tipo especial de anillo. Para ello,
nos apoyamos en los operadores derivados introducidos anteriormente, en
particular la operación O-exclusiva (XOR, $\oplus$) y la conjunción
(AND, $\wedge$).

::: definicion
Anillo Booleanodef_anillo_booleano_cap Un anillo booleano es un anillo
conmutativo con elemento unidad $(R, +, \cdot, 0_R, 1_R)$ en el cual
todo elemento es idempotente respecto a la multiplicación:
$$\forall x \in R, x \cdot x = x$$
:::

A partir de esta aparente simplicidad (la idempotencia de todos sus
elementos), emergen propiedades estructurales muy rígidas que limitan la
forma de estos anillos.

::: teorema
Característica 2caracteristica_dos Todo anillo booleano tiene
característica 2, es decir, $\forall x \in R, x + x = 0_R$. Todo
elemento es su propio inverso aditivo.
:::

::: proof
*Proof.* Consideremos el elemento $(x+x)$ y apliquemos la idempotencia:
$$\begin{align*}
(x + x) &= (x + x) \cdot (x + x) \\
x + x &= x^2 + x^2 + x^2 + x^2 \\
x + x &= x + x + x + x \\
0_R &= x + x
\end{align*}$$ Por tanto, al restar $x$ en ambos lados obtenemos
$x = -x$. ◻
:::

::: teorema
Conmutatividad estrictaconmutatividad_estricta Todo anillo booleano es
obligatoriamente conmutativo ($x \cdot y = y \cdot x$).
:::

::: proof
*Proof.* Evaluando el elemento $(x+y)$ al cuadrado: $$\begin{align*}
x + y &= (x + y)^2 \\
x + y &= x^2 + xy + yx + y^2 \\
x + y &= x + xy + yx + y \\
0_R &= xy + yx \\
xy &= -yx
\end{align*}$$ Como acabamos de demostrar que el anillo tiene
característica 2 (cada elemento es su propio inverso aditivo), sabemos
que $-yx = yx$, luego $xy = yx$. ◻
:::

## Funtores de Equivalencia Estructural

Existe una equivalencia estructural perfecta (un isomorfismo de
categorías) entre las Álgebras de Boole y los Anillos Booleanos.

### De Álgebra de Boole a Anillo Booleano

Dada un Álgebra de Boole $(\mathbb{B}, \vee, \wedge, \neg, \bot, \top)$,
podemos construir un anillo booleano definiendo los operadores del
anillo de la siguiente manera:

- Suma del anillo:
  $a + b \triangleq a \oplus b = (a \wedge \neg b) \vee (\neg a \wedge b)$

- Producto del anillo: $a \cdot b \triangleq a \wedge b$

- Elemento neutro aditivo ($0_R$): $\bot$

- Elemento unidad multiplicativo ($1_R$): $\top$

Es trivial comprobar que la idempotencia multiplicativa se cumple por
definición ($a \wedge a = a$), por lo que la estructura resultante es
efectivamente un anillo booleano. La estructura dual
$(\mathbb{B}, \odot, \vee)$ forma un anillo isomorfo asumiendo a $\top$
como el cero del anillo y a $\bot$ como la unidad multiplicativa.

### De Anillo Booleano a Álgebra de Boole

Inversamente, dado un Anillo Booleano $(R, +, \cdot, 0_R, 1_R)$, podemos
recuperar las operaciones lógicas booleanas mediante el siguiente funtor
de transformación:

- Disyunción: $a \vee b \triangleq a + b + (a \cdot b)$

- Conjunción: $a \wedge b \triangleq a \cdot b$

- Negación: $\neg a \triangleq 1_R + a$

- Mínimo ($\bot$): $0_R$

- Máximo ($\top$): $1_R$

## Cuerpos Booleanos

La teoría de Espacios Vectoriales (que trataremos en detalle más
adelante) exige que el conjunto de escalares sobre el que se fundamenta
el espacio tenga estructura matemática de **Cuerpo** (*Field* en
inglés). Un cuerpo es un anillo conmutativo unitario donde todo elemento
distinto de cero tiene inverso multiplicativo; como consecuencia directa
fundamental, **un cuerpo no puede tener divisores de cero**.

::: teorema
El único Cuerpo Booleano es $\mathbb{F}_2$cuerpo_booleano Un anillo
booleano es un cuerpo matemático si y solo si contiene exactamente dos
elementos.
:::

::: proof
*Proof.* Sea $R$ un anillo booleano que además cumple las propiedades de
un cuerpo. Sea $x \in R$ cualquier elemento del anillo. Por la propiedad
de idempotencia inherente al anillo booleano: $$\begin{align*}
x^2 &= x \\
x^2 - x &= 0_R \\
x(x - 1_R) &= 0_R
\end{align*}$$ Dado que en un cuerpo no existen divisores de cero, el
producto de dos elementos es cero si y solo si al menos uno de los
factores es cero. Por lo tanto, obligatoriamente se debe cumplir una de
estas dos condiciones para cualquier $x$:
$$x = 0_R \quad \text{o} \quad (x - 1_R) = 0_R \implies x = 1_R$$ En
consecuencia, el conjunto de elementos del anillo $R$ solo puede estar
formado por $\{0_R, 1_R\}$. ◻
:::

Esta demostración es crucial para nuestro propósito arquitectónico de
los sistemas digitales. Nos indica de manera absoluta que si queremos
construir espacios vectoriales utilizando operaciones lógicas (que
requeriremos para los códigos correctores de errores), **el único
álgebra de Boole que puede actuar como cuerpo de escalares es el álgebra
bivaluada $\mathbb{B}_2$**, la cual es algebraicamente isomorfa al
cuerpo de Galois $\mathbb{F}_2$.

Cualquier álgebra de Boole con más de dos elementos (por ejemplo, el
álgebra de los subconjuntos de un conjunto de 3 elementos, que tiene
$2^3=8$ elementos) es un anillo booleano perfectamente válido, pero
fallará al intentar ser un cuerpo por tener divisores de cero, y por lo
tanto fracasará si intentamos usarla como escalares para formar un
espacio vectorial consigo misma.

# Estructura de Retículo (Orden)

## Relaciones de Orden

El álgebra de Boole también puede formularse íntegramente prescindiendo
de los operadores algebraicos, para fundamentarse de manera topológica o
relacional mediante la Teoría del Orden.

Para ello, introducimos una relación binaria $\le$ sobre el conjunto
$\mathbb{B}$.

::: definicion
Conjunto Parcialmente Ordenado (Poset)poset Un conjunto $P$ equipado con
una relación binaria $\le$ es un conjunto parcialmente ordenado (poset)
si la relación satisface los siguientes axiomas para todo
$a, b, c \in P$:

1.  **Reflexividad**: $a \le a$.

2.  **Antisimetría**: Si $a \le b$ y $b \le a$, entonces $a = b$.

3.  **Transitividad**: Si $a \le b$ y $b \le c$, entonces $a \le c$.
:::

En este contexto, escribiremos $a \ge b$ como sinónimo estricto de
$b \le a$, y $a < b$ si $a \le b$ pero $a \ne b$.

## Ínfimo y Supremo

Dado un poset $(P, \le)$, consideremos un par de elementos $a, b \in P$.

- Un elemento $u \in P$ es una **cota superior** de $\{a, b\}$ si
  $a \le u$ y $b \le u$. El **supremo** de $a$ y $b$, denotado como
  $a \sqcup b$, es la menor de todas sus cotas superiores (si existe).

- Un elemento $l \in P$ es una **cota inferior** de $\{a, b\}$ si
  $l \le a$ y $l \le b$. El **ínfimo** de $a$ y $b$, denotado como
  $a \sqcap b$, es la mayor de todas sus cotas inferiores (si existe).

::: definicion
Retículo (Lattice)reticulo Un **retículo** es un conjunto parcialmente
ordenado en el cual todo par de elementos tiene un supremo
($a \sqcup b$) y un ínfimo ($a \sqcap b$) definidos y únicos dentro del
conjunto.
:::

## Funtores de Equivalencia Estructural

Al igual que ocurrió con los Anillos Booleanos, existe un isomorfismo
total entre las Álgebras de Boole algebraicas y ciertos retículos con
propiedades especiales.

### De Álgebra a Retículo

Toda álgebra de Boole $(\mathbb{B}, \vee, \wedge)$ induce de forma
natural un retículo definiendo la relación de orden parcial de la
siguiente manera: $$a \le b \iff a \wedge b = a$$ Por las propiedades de
absorción demostradas en capítulos previos, esta definición es
lógicamente equivalente a su forma dual: $$a \le b \iff a \vee b = b$$
Bajo esta métrica de orden impuesta por las operaciones lógicas, es
directo demostrar que el operador lógico $\vee$ computa exactamente el
supremo topológico de los dos elementos ($a \sqcup b = a \vee b$), y que
el operador lógico $\wedge$ computa su ínfimo
($a \sqcap b = a \wedge b$). A partir de este punto, el círculo se
cierra y se revela que las operaciones algebraicas abstractas de Boole
no son más que el cálculo de cotas topológicas en un espacio ordenado.

### De Retículo a Álgebra (Retículos Booleanos)

No todo retículo es un álgebra de Boole. Para recuperar un álgebra de
Boole plena desde la topología de orden puro, el retículo subyacente
debe poseer tres propiedades restrictivas adicionales, dando lugar a lo
que matemáticamente se conoce como **Retículo Booleano**:

::: teorema
Axiomas del Retículo Booleanoaxiomas_reticulo_booleano Un retículo
$(L, \le)$ es isomórfico a un Álgebra de Boole si y solo si es:

1.  **Acotado**: Existen elementos universales mínimo ($\bot$) y máximo
    ($\top$) tales que $\forall x \in L$, $\bot \le x \le \top$.

2.  **Distributivo**: El cálculo del ínfimo se distribuye sobre el
    cálculo del supremo, y viceversa.

3.  **Complementado**: Para cada elemento $a \in L$ existe un elemento
    único $b \in L$ (denominado su complemento, $\neg a$) tal que el
    ínfimo de ambos es $\bot$ y su supremo es $\top$.
:::

## Implicación para las Álgebras Finitas

Esta profunda visión topológica como un retículo complementado y
distributivo es la base fundamental que nos permitirá visualizar las
álgebras de Boole en el espacio mediante *Diagramas de Hasse*.

Más importante aún, esta estructura de orden estricto impone un límite
severo a la cardinalidad. Si un álgebra de Boole tiene un número finito
de elementos, su retículo subyacente se construirá forzosamente como el
conjunto potencia de sus átomos (los elementos inmediatamente superiores
al $\bot$). Esto revela, por el Teorema de Representación de Stone para
retículos finitos, que **toda álgebra de Boole finita debe tener
forzosamente $2^n$ elementos**.

Este hecho es el puente de entrada y la justificación absoluta para
adentrarnos en el siguiente capítulo: el estudio y la forma de las
Álgebras de Boole Finitas.

# Álgebras de Boole Finitas

En el capítulo anterior descubrimos que la estructura algebraica pura de
Boole encierra en su interior una rigurosa topología de orden.
Comprobamos cómo todo par de elementos está sometido a las leyes del
supremo ($\vee$) y el ínfimo ($\wedge$) dentro de un retículo acotado,
distributivo y complementado.

Esta dualidad álgebra/topología es la clave matemática que nos va a
revelar la forma exacta de todas las álgebras de Boole que tienen un
número finito de elementos.

## Estructura Atómica

Para comprender la anatomía de un álgebra finita, debemos identificar
sus \"ladrillos fundamentales\", es decir, los elementos indivisibles a
partir de los cuales se puede construir todo el conjunto operando con
supremos (sumas).

::: definicion
Átomosatomos Un elemento $x \in \mathbb{B}$ se denomina **átomo** si es
un elemento estrictamente positivo, $x \ne \bot$, y no existe ningún
elemento intermedio entre él y el $\bot$. Formalmente:
$$\mathit{atom}(x) \iff (x > \bot) \wedge \left( \forall y \in \mathbb{B}, \bot < y \le x \implies y = x \right)$$
:::

En términos puramente algebraicos, un átomo $x$ es aquel cuyo producto
(ínfimo) con cualquier otro elemento $y \in \mathbb{B}$ es el
aniquilador total o bien él mismo (absorbente total):
$$\mathit{atom}(x) \iff (x \ne \bot) \wedge \left( \forall y \in \mathbb{B}, (x \wedge y = \bot) \vee (x \wedge y = x) \right)$$
El conjunto de todos los átomos de un álgebra de Boole se denota como
$\mathit{Atom}(\mathbb{B})$. Una propiedad inmediata es que el ínfimo de
dos átomos distintos es siempre nulo:
$$\forall a, b \in \mathit{Atom}(\mathbb{B}), a \ne b \implies a \wedge b = \bot$$

::: definicion
Hiperátomos (Co-átomos)hiperatomos De forma dual, un **hiperátomo** o
**co-átomo** es un elemento estrictamente inferior a $\top$ tal que no
existe ningún elemento intermedio entre él y el máximo.
$$\mathit{hatom}(x) \iff (x < \top) \wedge \left( \forall y \in \mathbb{B}, x \le y < \top \implies y = x \right)$$
:::

En cualquier álgebra finita no trivial (donde $\top \ne \bot$), los
conjuntos $\mathit{Atom}(\mathbb{B})$ e $\mathit{Hatom}(\mathbb{B})$
nunca están vacíos.

## El Teorema de Representación de Stone (Caso Finito)

Si tomamos el conjunto de todos los átomos $\mathit{Atom}(\mathbb{B})$,
podemos generar el conjunto potencia $\wp(\mathit{Atom}(\mathbb{B}))$,
es decir, el conjunto de todos sus posibles subconjuntos. Vamos a
construir una función $\varphi$ que conecte este álgebra de subconjuntos
con el álgebra de Boole original.

### El Funtor $\varphi$

Definimos la función
$\varphi : \wp(\mathit{Atom}(\mathbb{B})) \to \mathbb{B}$ que toma un
subconjunto de átomos $S$ y devuelve el supremo topológico (la suma
booleana) de todos ellos: $$\varphi(S) = \begin{cases}
\bot & \text{si } S = \emptyset \\
\bigvee_{a \in S} a & \text{si } S \ne \emptyset
\end{cases}$$

Esta función preserva de forma natural las operaciones del álgebra de
subconjuntos hacia las del álgebra de Boole original: $$\begin{align*}
\varphi(S_1 \cup S_2) &= \varphi(S_1) \vee \varphi(S_2) \\
\varphi(S_1 \cap S_2) &= \varphi(S_1) \wedge \varphi(S_2) \\
\varphi(\mathit{Atom}(\mathbb{B}) \setminus S) &= \neg \varphi(S)
\end{align*}$$

### Isomorfismo y Cardinalidad

El gran triunfo matemático para las álgebras finitas se resume en el
siguiente teorema.

::: teorema
Representación de Álgebras de Boole Finitasrep_stone Toda álgebra de
Boole finita $\mathbb{B}$ es algebraicamente isomorfa al álgebra del
conjunto potencia de sus átomos. Es decir, la función $\varphi$ es una
biyección perfecta: $$\mathbb{B} \simeq \wp(\mathit{Atom}(\mathbb{B}))$$
:::

::: proof
*Proof.* Dado que el álgebra es finita, no existen cadenas infinitas
descendentes. Todo elemento $x \in \mathbb{B}$ (salvo el $\bot$) acota
por arriba a al menos un átomo. Por distributividad y ortogonalidad de
los átomos ($a \wedge b = \bot$), cualquier elemento $x$ puede
expresarse de forma única como el supremo de los átomos que lo preceden:
$$x = \bigvee \{ a \in \mathit{Atom}(\mathbb{B}) \mid a \le x \}$$ Por
lo tanto, la función inversa de $\varphi$ está perfectamente definida,
demostrando que $\varphi$ es sobreyectiva e inyectiva (biyectiva). ◻
:::

De este isomorfismo se desprende una consecuencia colosal, formulada
previamente de soslayo en nuestro análisis de los conjuntos topológicos.

::: teorema
Cardinalidad de un Álgebra Finitacardinalidad Si un álgebra de Boole es
finita, su número total de elementos debe ser, forzosamente, una
potencia de 2.
$$|\mathbb{B}| = 2^n \quad \text{donde} \quad n = |\mathit{Atom}(\mathbb{B})|$$
:::

Cualquier conjunto que no tenga exactamente $2, 4, 8, 16, \ldots$
elementos **jamás podrá** constituir un álgebra de Boole, sin importar
qué operaciones intentemos definir sobre él. Y aún más importante: todas
las álgebras de Boole que tengan el mismo número de elementos son
exactamente la misma álgebra (son algebraicamente isomorfas). Solo hay
*un* álgebra de Boole de 2 elementos, *una* de 4 elementos, *una* de 8
elementos, etc.

Esta uniformidad matemática nos da luz verde para enfocar nuestros
esfuerzos en el álgebra bivaluada $\mathbb{B}_2 = \{0, 1\}$ (es decir,
la Lógica Proposicional binaria). Sabemos de antemano que cualquier
álgebra de cardinal superior no es más que el espacio vectorial
n-dimensional $\mathbb{B}_2^n$, un tema que exploraremos a fondo en el
siguiente capítulo.

# Espacios Vectoriales Booleanos y Códigos de Hamming

## El Espacio Vectorial Binario $\mathbb{B}^n$

En el Capítulo 6b demostramos que, si bien cualquier álgebra de Boole
puede ser interpretada como un anillo, el **único** álgebra de Boole que
tiene la estructura rigurosa de un **Cuerpo Matemático** (es decir,
carente de divisores de cero y donde todo elemento no nulo tiene inverso
multiplicativo) es el álgebra bivaluada $\mathbb{B}_2 = \{0, 1\}$.
Algebraicamente, este cuerpo es exactamente el cuerpo de Galois
$\mathbb{F}_2$.

Dado que la condición insoslayable para construir un espacio vectorial
lineal es operar sobre un cuerpo de escalares, deducimos que los únicos
espacios vectoriales puramente booleanos que pueden existir deben tener
como conjunto base a $\mathbb{F}_2$.

::: definicion
El Espacio Vectorial $\mathbb{B}^n$espacio_bn Se define el espacio
vectorial booleano $\mathbb{B}^n$ como el conjunto de todas las
$n$-tuplas (vectores de $n$ bits) cuyos elementos pertenecen a
$\mathbb{F}_2$. Las dos operaciones que dotan al conjunto de estructura
de espacio vectorial son:

1.  **Suma vectorial:** Se define como la operación XOR ($\oplus$)
    aplicada bit a bit entre dos vectores.
    $$\vec{u} \oplus \vec{v} = (u_1 \oplus v_1, u_2 \oplus v_2, \ldots, u_n \oplus v_n)$$

2.  **Producto por escalar:** Se define como la operación AND ($\wedge$)
    entre un escalar booleano $k \in \mathbb{F}_2$ y cada elemento del
    vector.
    $$k \wedge \vec{v} = (k \wedge v_1, k \wedge v_2, \ldots, k \wedge v_n)$$
:::

Al operar sobre $\mathbb{F}_2$, este espacio vectorial hereda
directamente la característica 2 de su cuerpo base. Esto significa que
**todo vector es su propio inverso aditivo**:
$$\vec{v} \oplus \vec{v} = \vec{0}$$ lo cual simplifica
extraordinariamente el cálculo matricial (sumar y restar vectores es
exactamente la misma operación).

## Métrica: Peso y Distancia de Hamming

Para que este espacio abstracto tenga utilidad práctica en ingeniería
(en concreto, para analizar cómo de parecidos son dos mensajes
digitales), necesitamos dotarlo de una métrica que nos permita medir
\"distancias\" entre vectores.

::: definicion
Peso de Hammingpeso_hamming El **peso de Hamming** de un vector
$\vec{v}$, denotado como $w(\vec{v})$, es el número de componentes no
nulas (número de unos) que contiene.
:::

::: definicion
Distancia de Hammingdistancia_hamming La **distancia de Hamming** entre
dos vectores $\vec{u}$ y $\vec{v}$, denotada como $d(\vec{u}, \vec{v})$,
es el número de posiciones en las que difieren. Operacionalmente,
coincide con el peso de Hamming de su suma vectorial:
$$d(\vec{u}, \vec{v}) = w(\vec{u} \oplus \vec{v})$$
:::

La función $d$ cumple todas las propiedades matemáticas de una métrica
(no negatividad, identidad de los indiscernibles, simetría y desigualdad
triangular).

## Códigos de Corrección de Errores (Hamming)

La aplicación más brillante de dotar a las cadenas de bits de una
estructura de espacio vectorial sobre $\mathbb{F}_2$ es la invención de
los **códigos correctores de errores**.

En un canal de comunicación ruidoso, un vector $\vec{v}$ enviado puede
sufrir corrupciones (cambios de 0 a 1 o viceversa), recibiéndose un
vector diferente $\vec{r}$. Richard Hamming propuso solucionar esto no
usando todo el espacio vectorial $\mathbb{B}^n$, sino limitando los
mensajes válidos a un subespacio vectorial más pequeño y controlado.

### El Subespacio Código y la Matriz de Paridad

Un código lineal por bloques de longitud $n$ y dimensión $k$ se define
matemáticamente como un **subespacio vectorial**
$C \subset \mathbb{B}^n$ de dimensión $k$. Todo subespacio vectorial
puede definirse como el núcleo (kernel) de una transformación lineal,
representada por una matriz llamada **Matriz de Paridad ($H$)** de
dimensiones $(n-k) \times n$.

::: teorema
Validación del Síndromesindrome_hamming Un vector recibido $\vec{r}$ es
una palabra código válida (pertenece al subespacio código $C$) si y solo
si su producto por la matriz de paridad $H$ (utilizando aritmética en
$\mathbb{F}_2$) da como resultado el vector nulo. A este resultado se le
denomina **síndrome** ($\vec{s}$). $$\vec{s} = H \cdot \vec{r}^T$$ Si
$\vec{s} = \vec{0}$, el vector pertenece al subespacio (no hay errores
detectados). Si $\vec{s} \ne \vec{0}$, el vector ha salido del
subespacio, lo que indica que se ha corrompido durante la transmisión.
:::

Dado que operar matrices sobre $\mathbb{F}_2$ requiere únicamente
puertas lógicas XOR y AND, el cálculo del síndrome
$\vec{s} = H \cdot \vec{r}^T$ se puede implementar directamente en
hardware digital con una eficiencia extrema, constituyendo la base de
los modernos sistemas de memoria ECC (Error-Correcting Code).

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

[^1]: Aunque en textos recientes es común encontrar simplemente la
    abreviatura **ZF** (Zermelo-Fraenkel), en este libro volvemos a usar
    la notación **ZFS** (Zermelo-Fraenkel-Skolem) para incluir
    explícitamente y advertir la aportación fundamental de Skolem, tal y
    como exigen y reivindican algunos autores contemporáneos.

[^2]: Véase pre-axiomas
    [\[prax:esconj\]](#prax:esconj){reference-type="ref"
    reference="prax:esconj"} y
    [\[prax:constantes\]](#prax:constantes){reference-type="ref"
    reference="prax:constantes"}

[^3]: Véase pre-axioma
    [\[prax:opbinint_vee\]](#prax:opbinint_vee){reference-type="ref"
    reference="prax:opbinint_vee"}

[^4]: Véase pre-axioma
    [\[prax:opbinint_wedge\]](#prax:opbinint_wedge){reference-type="ref"
    reference="prax:opbinint_wedge"}

[^5]: Véase postulado
    [\[post:neutro_vee\]](#post:neutro_vee){reference-type="ref"
    reference="post:neutro_vee"}

[^6]: Véase postulado
    [\[post:neutro_wedge\]](#post:neutro_wedge){reference-type="ref"
    reference="post:neutro_wedge"}

[^7]: Véase postulado
    [\[post:neutro_vee\]](#post:neutro_vee){reference-type="ref"
    reference="post:neutro_vee"}

[^8]: Véase postulado
    [\[post:neutro_wedge\]](#post:neutro_wedge){reference-type="ref"
    reference="post:neutro_wedge"}

[^9]: Véase postulado
    [\[post:conmut_vee\]](#post:conmut_vee){reference-type="ref"
    reference="post:conmut_vee"}

[^10]: Véase postulado
    [\[post:conmut_wedge\]](#post:conmut_wedge){reference-type="ref"
    reference="post:conmut_wedge"}

[^11]: Véase postulado
    [\[post:distrib_vee_wedge\]](#post:distrib_vee_wedge){reference-type="ref"
    reference="post:distrib_vee_wedge"}

[^12]: Véase postulado [\[post:comp\]](#post:comp){reference-type="ref"
    reference="post:comp"}

[^13]: Véase postulado [\[post:comp\]](#post:comp){reference-type="ref"
    reference="post:comp"}

[^14]: Véase postulado [\[post:comp\]](#post:comp){reference-type="ref"
    reference="post:comp"}

[^15]: Véase postulado [\[post:comp\]](#post:comp){reference-type="ref"
    reference="post:comp"}

[^16]: Véase postulado [\[post:comp\]](#post:comp){reference-type="ref"
    reference="post:comp"}

[^17]: Véase pre-axioma
    [\[prax:opbinint_vee\]](#prax:opbinint_vee){reference-type="ref"
    reference="prax:opbinint_vee"}

[^18]: Véase pre-axioma
    [\[prax:opbinint_vee\]](#prax:opbinint_vee){reference-type="ref"
    reference="prax:opbinint_vee"}

[^19]: Véase pre-axioma
    [\[prax:opbinint_wedge\]](#prax:opbinint_wedge){reference-type="ref"
    reference="prax:opbinint_wedge"}

[^20]: Véase pre-axioma
    [\[prax:opbinint_vee\]](#prax:opbinint_vee){reference-type="ref"
    reference="prax:opbinint_vee"}

[^21]: Véase postulado
    [\[post:neutro_vee\]](#post:neutro_vee){reference-type="ref"
    reference="post:neutro_vee"}

[^22]: Véase postulado
    [\[post:neutro_wedge\]](#post:neutro_wedge){reference-type="ref"
    reference="post:neutro_wedge"}

[^23]: Véase postulado
    [\[post:conmut_vee\]](#post:conmut_vee){reference-type="ref"
    reference="post:conmut_vee"}

[^24]: Véase postulado
    [\[post:conmut_wedge\]](#post:conmut_wedge){reference-type="ref"
    reference="post:conmut_wedge"}

[^25]: Véase postulado
    [\[post:distrib_vee_wedge\]](#post:distrib_vee_wedge){reference-type="ref"
    reference="post:distrib_vee_wedge"}

[^26]: Véase postulado
    [\[post:distrib_wedge_vee\]](#post:distrib_wedge_vee){reference-type="ref"
    reference="post:distrib_wedge_vee"}

[^27]: Véase postulado
    [\[post:neutro_wedge\]](#post:neutro_wedge){reference-type="ref"
    reference="post:neutro_wedge"}

[^28]: Véase postulado
    [\[post:conmut_vee\]](#post:conmut_vee){reference-type="ref"
    reference="post:conmut_vee"}

[^29]: Véase postulado
    [\[post:distrib_vee_wedge\]](#post:distrib_vee_wedge){reference-type="ref"
    reference="post:distrib_vee_wedge"}

[^30]: Véase postulado
    [\[post:neutro_wedge\]](#post:neutro_wedge){reference-type="ref"
    reference="post:neutro_wedge"}

[^31]: Véase postulado
    [\[post:distrib_vee_wedge\]](#post:distrib_vee_wedge){reference-type="ref"
    reference="post:distrib_vee_wedge"}

[^32]: Véase postulado
    [\[post:distrib_wedge_vee\]](#post:distrib_wedge_vee){reference-type="ref"
    reference="post:distrib_wedge_vee"}

[^33]: Véase postulado
    [\[post:distrib_wedge_vee\]](#post:distrib_wedge_vee){reference-type="ref"
    reference="post:distrib_wedge_vee"}

[^34]: Véase postulado
    [\[post:conmut_vee\]](#post:conmut_vee){reference-type="ref"
    reference="post:conmut_vee"}

[^35]: Véase postulado
    [\[post:conmut_wedge\]](#post:conmut_wedge){reference-type="ref"
    reference="post:conmut_wedge"}

[^36]: Véase postulado
    [\[post:distrib_wedge_vee\]](#post:distrib_wedge_vee){reference-type="ref"
    reference="post:distrib_wedge_vee"}

[^37]: Véase postulado
    [\[post:distrib_vee_wedge\]](#post:distrib_vee_wedge){reference-type="ref"
    reference="post:distrib_vee_wedge"}

[^38]: Véase postulado
    [\[post:distrib_wedge_vee\]](#post:distrib_wedge_vee){reference-type="ref"
    reference="post:distrib_wedge_vee"}
