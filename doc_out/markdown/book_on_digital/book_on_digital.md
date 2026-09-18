$$
\gdef\symdiff{\mathbin{\vartriangle}}
\gdef\llbracket{\lbrack\!\lbrack}
\gdef\rrbracket{\rbrack\!\rbrack}
\gdef\triangleq{\stackrel{\mathrm{def}}{=}}
$$

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
clásico de la negación lógica $\neg.$ Más adelante, y por conveniencia
práctica, transitaremos hacia la notación clásica de sistemas digitales
($+,$ $\cdot,$ $0,$ $1$).

## Nomenclatura y Convenios

Antes de comenzar con el desarrollo formal del álgebra, estableceremos
una serie de convenios notacionales que utilizaremos a lo largo de este
texto:

- $0 \notin \mathbb{N}.$ Ante la definición de los números naturales,
  nosotros adoptamos este convenio excluyendo al cero.

- $\widetilde{\mathbb{N}} \triangleq \left( \mathbb{N} \cup \{0\} \right).$
  Representará el conjunto de los naturales extendidos que incluye el
  cero.

- Definición recurrente de los conjuntos
  $\lbrack 0,1 \rbrack_{\mathbb{Q}}$ y
  $\lbrack 0,1 \rbrack_{\mathbb{Q}}^n,$ donde $n \in \mathbb{N}$ y
  $n > 1:$

  - $\lbrack 0,1 \rbrack_{\mathbb{Q}} := \lbrack 0,1 \rbrack \cap \mathbb{Q}$

  - $\lbrack 0,1 \rbrack_{\mathbb{Q}}^1 := \lbrack 0,1 \rbrack_{\mathbb{Q}}$

  - $\lbrack 0,1 \rbrack_{\mathbb{Q}}^n := \lbrack 0,1 \rbrack_{\mathbb{Q}}^{n-1} \times \lbrack 0,1 \rbrack_{\mathbb{Q}}^1$

- Por lo general, los elementos de un conjunto se representarán por
  letras minúsculas (alfabetos griego y latino) con o sin subíndices
  (ejemplo: $a_3,$ $b,$ $\gamma_{1547},$ $\delta$) y dígitos decimales
  ($\{0, 1, \ldots, 9\}$). Por el contrario, los conjuntos se
  representarán por letras mayúsculas (alfabeto griego y latino),
  igualmente con o sin subíndices. Este convenio será válido a excepción
  de que se exprese de forma explícita otro nombre para elementos o
  conjuntos.

- En ocasiones aseguraremos que existe un conjunto asociado a un
  elemento: en general serán letras mayúsculas, como corresponde a un
  conjunto, pero con un subíndice escrito exactamente como el elemento
  asociado.

- Cuando expresemos $a \ast B,$ es decir, el elemento $a$ operado con un
  conjunto $B$ mediante una operación binaria $\ast,$ nos estaremos
  refiriendo al conjunto formado por operar $a$ con todos los elementos
  de $B:$ $a \ast B = \{ a \ast b \mid b \in B \}.$ De igual manera, la
  operación entre dos conjuntos se entenderá como:
  $A \ast B = \{ a \ast b \mid a \in A \land b \in B \}.$

- El universo de discurso principal será un conjunto $\mathbb{B}.$ Para
  aligerar la notación, evitaremos en lo posible el uso explícito del
  cuantificador universal ($\forall$). Cuando aparezca una variable,
  conjunto o constante sin cuantificar, asumiremos implícitamente una
  cuantificación universal sobre los elementos de $\mathbb{B}.$ Si la
  cuantificación debiera aplicarse a un subconjunto particular, se
  omitirá el símbolo $\forall$ pero se precederá la proposición con la
  relación de pertenencia.

- De igual forma, cuando una variable asuma como valor un conjunto, se
  entenderá implícitamente que pertenece al conjunto partes
  $\wp(\mathbb{B}) \smallsetminus \{ \varnothing \}.$

## Pre-Axiomas de la Estructura

Antes de enunciar los postulados, debemos definir rigurosamente sobre
qué elementos y operaciones estamos trabajando.

Partimos de un ente matemático $\mathbb{B}.$

> **Preaxioma (\[H0.0.0\] Estructura de Conjunto -
> EsConjunto($\mathbb{B}$)):**[]{#esconj label="esconj"} Se requiere que
> $\mathbb{B}$ sea un conjunto.

> **Preaxioma (\[H0.0.1, H0.0.2\] Elementos Constantes -
> Constantes):**[]{#constantes label="constantes"} Este conjunto ha de
> cumplir que tiene dos elementos que llamaremos constantes, tales que
> $\bot \in \mathbb{B}$ y $\top \in \mathbb{B}.$ En principio, no
> asumimos nada sobre la igualdad o desigualdad de estas constantes.

Además, vamos a definir dos operaciones binarias internas que
denotaremos por $\vee$ y $\wedge.$ Estas deben satisfacer rigurosamente
la definición de función:

> **Preaxioma (\[H0.1\] Operación Binaria Interna $\vee$ -
> OpBinInt$_\vee$):**[]{#opbinint_vee label="opbinint_vee"}
> $\vee : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una operación
> binaria interna.

> **Preaxioma (\[H0.2\] Operación Binaria Interna $\wedge$ -
> OpBinInt$_\wedge$):**[]{#opbinint_wedge label="opbinint_wedge"}
> $\wedge : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ es una
> operación binaria interna.

Para poder usar estos conceptos con mayor seguridad y flexibilidad en
las futuras demostraciones formales, asignaremos nombres cortos a las
condiciones de existencia y unicidad de la imagen para estas
operaciones:

> **Preaxioma (\[H.0.1.0\] Existencia $\vee$ -
> Existencia$_\vee$):**[]{#exist_vee label="exist_vee"} Para todo par
> existe imagen en $\mathbb{B}.$ Es decir,
> $\forall \langle a,b \rangle \in \mathbb{B} \times \mathbb{B},$
> $\exists c \in \mathbb{B}$ tal que $a \vee b = c.$

> **Preaxioma (\[H.0.2.0\] Existencia $\wedge$ -
> Existencia$_\wedge$):**[]{#exist_wedge label="exist_wedge"}
> Análogamente,
> $\forall \langle a,b \rangle \in \mathbb{B} \times \mathbb{B},$
> $\exists d \in \mathbb{B}$ tal que $a \wedge b = d.$

> **Preaxioma (\[H.0.1.1\] Unicidad $\vee$ -
> Unicidad$_\vee$):**[]{#unic_vee label="unic_vee"} Para un par solo
> existe una imagen. Esto es, si $a \vee b = c$ y $a \vee b = d,$
> entonces $c = d.$

> **Preaxioma (\[H.0.2.1\] Unicidad $\wedge$ -
> Unicidad$_\wedge$):**[]{#unic_wedge label="unic_wedge"} De igual forma
> para el ínfimo, si $a \wedge b = c$ y $a \wedge b = d,$ entonces
> $c = d.$

## Los Postulados de Huntington (1904)

Sobre el sistema $(\mathbb{B}, \vee, \wedge, \bot, \top)$ que cumple los
pre-axiomas anteriores, diremos que forma un álgebra de Boole si
satisface los siguientes postulados:

> **Postulado (\[H1.1\] Elemento neutro $\vee$ -
> $ElemNeu_\vee$):**[]{#neutro_vee label="neutro_vee"} Todo elemento
> operado mediante $\vee$ con el mínimo $\bot$ da como resultado el
> mismo elemento; es decir, $\bot$ no altera el valor original:
> $$\forall a \in \mathbb{B}, \quad a \vee \bot = a$$

> **Postulado (\[H1.2\] Elemento neutro $\wedge$ -
> $ElemNeu_\wedge$):**[]{#neutro_wedge label="neutro_wedge"} Todo
> elemento operado mediante $\wedge$ con el máximo $\top$ da como
> resultado el mismo elemento, quedando inalterado:
> $$\forall a \in \mathbb{B}, \quad a \wedge \top = a$$

> **Postulado (\[H2.1\] Conmutatividad $\vee$ -
> $Comm_\vee$):**[]{#conmut_vee label="conmut_vee"} El orden de los
> operandos al aplicar la operación $\vee$ es indiferente, obteniéndose
> exactamente el mismo resultado:
> $$\forall a, b \in \mathbb{B}, \quad a \vee b = b \vee a$$

> **Postulado (\[H2.2\] Conmutatividad $\wedge$ -
> $Comm_\wedge$):**[]{#conmut_wedge label="conmut_wedge"} De la misma
> forma, el orden de los operandos al aplicar la operación $\wedge$
> tampoco altera el resultado final:
> $$\forall a, b \in \mathbb{B}, \quad a \wedge b = b \wedge a$$

> **Postulado (\[H3.1\] Distributividad $\vee$ sobre $\wedge$ -
> $Dist_\vee$):**[]{#distrib_vee_wedge label="distrib_vee_wedge"} La
> operación $\vee$ se distribuye sobre la operación $\wedge.$ Operar un
> elemento con el resultado de un $\wedge$ equivale a operar con $\vee$
> cada componente individualmente y luego aplicar $\wedge:$
> $$\forall a, b, c \in \mathbb{B}, \quad a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$$

> **Postulado (\[H3.2\] Distributividad $\wedge$ sobre $\vee$ -
> $Dist_\wedge$):**[]{#distrib_wedge_vee label="distrib_wedge_vee"} De
> manera equivalente, el ínfimo ($\wedge$) se reparte de forma
> distributiva entre los componentes de un supremo ($\vee$):
> $$\forall a, b, c \in \mathbb{B}, \quad a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$$

> **Postulado (\[H4\] Complementario -
> $Comp_\vee, Comp_\wedge$):**[]{#comp label="comp"} Todo elemento del
> conjunto posee al menos un \"complemento\" (o elemento opuesto). Al
> operarlo con su complemento mediante $\vee$ siempre alcanzamos el
> máximo $\top,$ y mediante $\wedge$ siempre caemos al mínimo $\bot:$
> $$\begin{align*}
> \forall a \in \mathbb{B}, \exists b \in \mathbb{B} \quad : \quad a \vee b &= \top \quad (Comp_\vee) \quad \text{[H4.1]} \\
> a \wedge b &= \bot \quad (Comp_\wedge) \quad \text{[H4.2]}
> \end{align*}$$

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
partes de un conjunto. Dado un conjunto cualquiera $U \neq \varnothing,$
$\wp(U) = \{X \mid X \subseteq U\},$ esto es,
$\wp(U) = \{X \mid \forall x ( (x \in X) \Rightarrow (x \in U) ) \},$
dónde se verifica que $(\varnothing \in \wp(U)) \land (U \in \wp(U)).$
Haremos $B \triangleq \wp(U),$ $0 \triangleq \varnothing$ y
$1 \triangleq U,$ como producto lógico pondremos la intersección de
conjuntos $\forall X, Y \in \wp(U) \quad X \cdot Y \triangleq X \cap Y,$
como suma lógica pondremos la unión de conjuntos
$\forall X, Y \in \wp(U) \quad X + Y \triangleq X \cup Y.$ Las tres
primeras (dobles) propiedades son directamente cumplidas por la
estructura construida y la existencia del complementario es fácil de
ver. Sea
$\forall X \in \wp(U) \Rightarrow \exists Y \triangleq U \smallsetminus X$
y a partir de ahí sabemos que $Y \in \wp(U)$ puesto que
$\forall x \in Y \quad x \in U \smallsetminus X \Rightarrow x \in U$ y
en el caso que $X = U$ tenemos que
$Y = U \smallsetminus X = U \smallsetminus U = \varnothing$ de forma que
$\varnothing \in \wp(U)$ por definición. Ahora sólo se trata de ver que
$Y \cdot X = Y \cap X = (U \smallsetminus X) \cap X = \varnothing = 0$ y
que la propiedad dual a cumplir
$Y + X = Y \cup X = (U \smallsetminus X) \cup X = U = 1.$ Ya tenemos que
$\forall X \in \wp(U) \exists Y \in \wp(U) \quad Y \in \overline{X}$
habiendo tomado $Y \triangleq U \smallsetminus X.$

**\[Ejemplo 2\]** Un ejemplo interesante fácil de construir es el
álgebra de Boole de los números que son producto de los primeros números
primos (cantidad finita de ellos) y sus divisores. Consideramos el
conjunto $P_{n} \triangleq \{2,3,\ldots,p_{n}\},$ consideraremos el $1$
booleano cómo $1_{B} \triangleq \prod\limits_{q \in P_{n}}q$ y el $0$
cómo $0_{B} \triangleq 1_{\mathbb{N}}.$ Consideramos a
$B \triangleq \{n \in \mathbb{N} \mid n \mid ( \prod P_{n} ) \},$ y las
operaciones serán el mínimo común múltiplo como suma booleana y el
máximo común divisor como producto booleano. El complemento de un
elemento resulta ser
$\forall k \in B \quad \overline{k} = 1_{B}/k = \prod\limits_{q \in \{p \in P_{n} \mid p \nmid k\}}q.$
Éste es un modelo fácil de desarrollar para poner ejemplos.

**\[Ejemplo 3\]** Partimos de un álgebra de Boole cualquiera y un
elemento no $0$ ni $1$ cualquiera tal que
$x \in B \smallsetminus \{ 0,1 \}.$ Definimos ahora un conjunto
$B_{\leq x} \triangleq \{y \in B \mid x \cdot y = y\}$ y
$B_{\geq x} \triangleq \{y \in B \mid x \cdot y = x\}.$ Las álgebras de
Boole nuevas a considerar son
$\langle B_{\leq x}, \{0 \equiv 0_{B}, 1 \equiv x\}, \{+_{B}, \cdot_{B}\} \rangle$
y
$\langle B_{\geq x}, \{0 \equiv x, 1 \equiv 1_{B}\}, \{+_{B}, \cdot_{B}\} \rangle.$
Consideramos el mismo producto booleano que en el conjunto inicial e
idénticamente con la suma booleana. Sólo varía el complemento, de la
siguiente forma $y \in B_{\geq x} \Rightarrow y' = \overline{y} + x$ y
$y \in B_{\leq x} \Rightarrow y' = \overline{y} \cdot x.$ Es fácil
comprobar la validez de esta definición de un álgebra de Boole, de
manera más concreta, que las operaciones son internas y el complemento
declarado es también interno y se comporta como complemento del nuevo
álgebra, esto
es,$${y \in B_{\geq x}}\Rightarrow y{{' \cdot y} = {x \land y}}{{' + y} = 1}$$
que$${y \in B_{\leq x}}\Rightarrow y{{' \cdot y} = {0 \land y}}{{' + y} = x} .$$

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
$$1_{B}{{: = V} \equiv \mathbf{\mathit{true}}} ,$$ a falso,
$$0_{B}{{: = F} \equiv \mathbf{\mathit{false}}}$$) o conjunto de
proposiciones pueden ser operadas mediante la conjunción 'y', A 'y' B es
verdadero si A es verdadero y B es verdadero a la vez y falso en
cualquier otro caso. La disyunción sería la 'o', siendo A 'o' B
verdadero con que A sea verdadero o lo sea B, siendo falso sólo cuando A
es falso y B es falso a la vez. La notación más habitual es
$${{+ {: = \vee}} \equiv \text{or}} \equiv {\mid \mid}$$y$${{\cdot {: = \land}} \equiv \text{and}} \equiv {\&\&} .$$
Para el 'no' (negación) tenemos
que$${{\overline{\phantom{A}}{: = {\neg\phantom{A}}}} \equiv \text{not}}{\phantom{A} \equiv {/\phantom{A}}} .$$
El conjunto de Boole es el conjunto de proposiciones de la que partamos.

De manera más formal se considera un elemento del álgebra de Boole de la
lógica a las clases de equivalencia de las proposiciones equivalentes
lógicamente (en su valor de verdad o falsedad) entre sí.

**\[Ejemplo 5\]** El álgebra de conmutación. Este es el álgebra de Boole
más sencillo que hay. $$B{{: = B_{2}} \equiv {\{{0,1}\}}} .$$ Las
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
$\{0 \triangleq \{\} \equiv \varnothing \},$ el intermedio
$\{\{\alpha\},\{\beta\}\},$ y el superior
$\{1 \triangleq \{\alpha,\beta\}\}.$
$B \triangleq B_{4} \equiv \{0,a,b,1\}.$ Las operaciones las
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
Huntington si cambiáis $a$ por $\{\alpha\},$ $b$ por $\{\beta\},$ $1$
por $\{\{\alpha\},\{\beta\}\}$ y $0$ por el conjunto vacío
$\varnothing.$

**\[Ejemplo 7\]** El álgebra de Boole de 8 elementos. Este es el álgebra
de Boole generada por un conjunto de 3 elementos. Es singular en el
sentido que sólo tiene 4 niveles, el más bajo $\{0\},$ el de átomos
$\{a,b,c\},$ el de hiperátomos $\{A,B,C\}$ y el superior $\{1\}.$ Los
niveles de átomos y de hiperátomos son especialmente importantes, siendo
esta álgebra de Boole, la más pequeña que los diferencia. Sería:

$B \triangleq B_{8} \equiv \{0,a,b,c,A,C,B,1\}.$

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
$\{0\},$ el de átomos $\{\alpha,\beta,\gamma,\delta\},$ el de
hiperátomos $\{A,B,\Gamma,\Delta\},$ el intermedio $\{a,b,c,d,e,f\}$ y
finalmente el nivel superior con el $\{1\}.$ Sería:

$B \triangleq B_{16} \equiv \{0,\alpha,\beta,\gamma,\delta,a,b,c,d,e,f,A,B,\Gamma,\Delta,1\}.$

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

$$\begin{bmatrix}
\neg & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & A & B & \Gamma & \Delta & 1 \\
 & 1 & \Delta & \Gamma & B & A & f & e & d & c & b & a & \delta & \gamma & \beta & \alpha & 0
\end{bmatrix}$$

y podréis comprobar fácilmente que se cumplen todos los postulados de
Huntington, con solo tener en cuenta que todos los elementos se pueden
poner en función de $\alpha, \beta, \gamma, \delta$ y sumas de ellos.
Las sumas de dos de los anteriores elementos son $a, b, c, d, e, f$ y
las sumas de tres de ellos son $A, B, \Gamma, \Delta.$

**\[Ejemplo 9\]** El álgebra de Boole de los conjuntos que se pueden
expresar como **unión disjunta finita de subintervalos genéricos de
$[0,1] \cap \mathbb{Q}.$ Definimos por conveniencia
$\mathbf{I}_{\mathbb{Q}} \triangleq [0,1]_{\mathbb{Q}}$**. Para esto
haremos abstracción de cualquier conjunto finito de puntos de
$\mathbf{I}_{\mathbb{Q}},$ esto es, consideraremos que dos conjuntos son
iguales si su diferencia simétrica (la unión de las diferencias, los
elementos que no son comunes de ambos conjuntos) es vacía o es un
conjunto finito de puntos. Esta álgebra de Boole tiene un cardinal
infinito numerable (como el cardinal de los números naturales). Lo más
importante es que no puede desarrollarse de manera semejante a como
desarrolla­mos el álgebra de las partes de un conjunto. Lo formalizaremos
del siguiente modo:

1.  $a, b \in \mathbf{I}_{\mathbb{Q}}, a < b \Rightarrow [a,b]_{\mathbb{Q}} \triangleq [a,b] \cap \mathbb{Q} \triangleq \{ x \in \mathbf{I}_{\mathbb{Q}} \mid a \leq x \leq b \}$

    1.  Si escribimos $[a,b]_{\mathbb{Q}}$ entonces
        $a \leq b \land a \neq b.$

    2.  Sea
        $\mathbf{II}_{\mathbb{Q}} \triangleq \{ [a,b]_{\mathbb{Q}} \mid a, b \in \mathbf{I}_{\mathbb{Q}} \land a < b \land a \neq b \}.$

    3.  Sea
        $\mathbf{\mathrm{III}}_{\mathbb{Q}} \triangleq \{ A \in \wp( \mathbf{I}_{\mathbb{Q}} ) \mid A = \bigcup_{\lambda \in \Lambda} I_{\lambda} \quad \forall \lambda \in \Lambda \quad I_{\lambda} \in \mathbf{II}_{\mathbb{Q}} \land \#(\Lambda) \in \mathbb{N} \} \cup \{ \varnothing \}.$

    4.  Sea
        $\mathit{Fin}( \mathbf{I}_{\mathbb{Q}} ) \triangleq \{ A \in \wp( \mathbf{I}_{\mathbb{Q}} ) \mid \#(A) \in \mathbb{N} \}.$

    5.  $A, B \in \wp( \mathbf{I}_{\mathbb{Q}} ), \quad A \approx B \triangleq \#( A \mathbin{\vartriangle}B ) \in \mathbb{N}.$
        Esta relación es de equivalencia.

        1.  Reflexiva
            $$\#{\left( {A \mathbin{\vartriangle}A} \right) = \#}{{(\varnothing) = 0} \in \widetilde{\mathbb{N}}} .$$
            Luego $$A \approx A .$$

        2.  Simétrica
            $$A \mathbin{\vartriangle}{B = B} \mathbin{\vartriangle}A.\Rightarrow.A \approx B\Leftrightarrow B \approx A .$$

        3.  Transitiva
            $A \approx B \land B \approx C \Rightarrow A \approx C.$

            - $\#(A \mathbin{\vartriangle}B) = n_{1} \in \mathbb{N} \land \#(B \mathbin{\vartriangle}C) = n_{2} \in \mathbb{N} \Rightarrow \#(A \mathbin{\vartriangle}C) \leq n_{1} + n_{2} \in \mathbb{N}.$
              Y queda demostrada la propiedad transitiva.

    6.  A partir de aquí hablaremos de $⟦A⟧$ para hablar de la clase de
        equivalencia de $A \in \mathbf{\mathrm{III}}_{\mathbb{Q}}$ bajo
        la relación de equivalencia $\approx.$

    7.  A partir de aquí hablaremos de nuestro conjunto
        $\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}(0,1) \triangleq \{ ⟦A⟧ \mid A \in \mathbf{\mathrm{III}}_{\mathbb{Q}} \}.$

    8.  Nuestro conjunto de Boole será
        $\mathbb{B} \triangleq \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}(0,1).$

    9.  El $0 \triangleq ⟦\varnothing⟧.$

    10. El $1 \triangleq ⟦\mathbf{\mathrm{I}}_{\mathbb{Q}}⟧.$

    11. Ahora veremos unas operaciones muy cercanas a la unión, la
        intersección y el complemento, que realmente nos dan un álgebra
        de Boole sobre
        $\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}:$

        $$\begin{matrix}
              ⟦A⟧, ⟦B⟧ \in \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}} \\
              ⟦A⟧ + ⟦B⟧ \triangleq ⟦A \cup B⟧ \\
              ⟦A⟧ \cdot ⟦B⟧ \triangleq ⟦A \cap B⟧ \\
              \overline{⟦A⟧} \triangleq ⟦\lbrack 0,1\rbrack_{\mathbb{Q}} \smallsetminus A⟧
              \end{matrix}$$

    12. Convenio de notación:
        $⟦a,b⟧ \triangleq ⟦\left\lbrack a,b \right\rbrack_{\mathbb{Q}}⟧.$
        Estos conjuntos serán nuestros subintervalos genéricos del
        intervalo genérico unidad.

    13. Sea una sucesión finita de un número par $2 \cdot n$ de
        elementos de $\lbrack 0,1\rbrack_{\mathbb{Q}},$ estrictamente
        creciente
        $0_{\mathbb{Q}} \leq a_{1} < b_{1} < a_{2} < b_{2} < \ldots < a_{n} < b_{n} \leq 1_{\mathbb{Q}}$
        dispuestos como $⟦a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}⟧$
        definirán los elementos de
        $\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}},$
        aparte de
        $⟦⟧ \triangleq ⟦\varnothing⟧ = ⟦\{0\}⟧ = ⟦\{1\}⟧ = 0_{\mathbf{\mathrm{I}}_{\mathbb{B}}^{\mathbf{\mathrm{GEN}}}}.$

    14. Si escribimos $⟦a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}⟧,$
        significamos ya (suponemos que es un hecho que)
        $0_{\mathbb{Q}} \leq a_{1} < b_{1} < a_{2} < b_{2} < \ldots < a_{n} < b_{n} \leq 1_{\mathbb{Q}}.$

    15. Ahora ya definimos (notación):

        $$\begin{aligned}
              ⟦a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}⟧ &\triangleq ⟦\{x \in \lbrack 0,1\rbrack_{\mathbb{Q}} \mid \\
              &\quad \exists k \in \mathbb{N}, 1 \leq k \leq n : x \in \lbrack a_{k},b_{k}\rbrack_{\mathbb{Q}}\}⟧ \\
              &\equiv ⟦\bigcup_{k = 1}^{n}\lbrack a_{k},b_{k}\rbrack⟧
              \end{aligned}$$

    16. Ahora ya tenemos el conjunto de Boole que buscábamos:

        $$\begin{aligned}
              \left\lbrack ⟦0,1⟧ \right\rbrack_{\mathbf{\mathrm{I}}} \triangleq \{ &⟦a_{1},b_{1},\ldots,a_{n},b_{n}⟧ \mid \\
              &\exists n \in \mathbb{N} : 0_{\mathbb{Q}} \leq a_{1} < b_{1} < \ldots < a_{n} < b_{n} \leq 1_{\mathbb{Q}} \} \cup \{ ⟦⟧ \}
              \end{aligned}$$

Que las uniones, complementos e intersecciones de intervalos genéricos
finitos siguen siendo intervalos genéricos finitos es claro desde el
principio. Sin embargo voy a exponer la cabalística, hacer las cuentas
vamos, para que no quede lugar a dudas. Con toda esta comprobación (o
re-definición) de que $\mathbb{B}$ es cerrado bajo las distintas
operaciones es laborioso, un tanto enojoso.

La operación de complemento queda de la siguiente manera, y aunque aún
no podemos comprobar aún su corrección, si queda claro que es un
operación unaria interna:

$$A^{I} \triangleq \begin{cases}
  \llbracket 0, a_1, b_1, a_2, \ldots, b_{n-1}, a_n, b_n, 1 \rrbracket & \text{si } a_1 \neq 0 \land b_n \neq 1 \\
  \llbracket b_1, a_2, \ldots, b_{n-1}, a_n, b_n, 1 \rrbracket & \text{si } a_1 = 0 \land b_n \neq 1 \\
  \llbracket b_1, a_2, \ldots, b_{n-1}, a_n \rrbracket & \text{si } a_1 = 0 \land b_n = 1 \\
  \llbracket 0, a_1, b_1, a_2, \ldots, b_{n-1}, a_n \rrbracket & \text{si } a_1 \neq 0 \land b_n = 1 \\
  \llbracket \varnothing \rrbracket & \text{si } A = \llbracket 0, 1 \rrbracket \\
  \llbracket 0, 1 \rrbracket & \text{si } A = \llbracket \varnothing \rrbracket
\end{cases}$$

De dónde obtenemos
$\forall A \in \mathbb{B}, \exists A^{I} \in \mathbb{B}.$

Tenemos que
$0 \in \mathbb{B}, 0 \triangleq \llbracket \varnothing \rrbracket \equiv \llbracket \rrbracket$
y $1 \in \mathbb{B}, 1 \triangleq \llbracket 0,1 \rrbracket,$ y
$0^{I} = 1 \land 1^{I} = 0.$ Además observamos con claridad que
$\forall A \in \mathbb{B}, \exists A^{I} \in \mathbb{B}$ tal que
$A + A^{I} = \llbracket \mathbf{\mathrm{I}}_{\mathbb{Q}} \rrbracket = 1$
y $A \cdot A^{I} = \llbracket \rrbracket = 0.$ Además de
$\forall A \in \mathbb{B}, (A^{I})^{I} = A.$ Así nos queda
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

    $$B + A \triangleq \begin{cases}
      \llbracket \varnothing \rrbracket & \text{si } A = \llbracket \varnothing \rrbracket \land B = \llbracket \varnothing \rrbracket \\
      A & \text{si } B = \llbracket \varnothing \rrbracket \\
      B & \text{si } A = \llbracket \varnothing \rrbracket \\
      1 & \text{si } \exists A \in A, \exists B \in B : \overline{B} \subseteq A \lor \overline{A} \subseteq B \\
      A & \text{si } \exists A \in A, \exists B \in B : B \subseteq A \\
      B & \text{si } \exists A \in A, \exists B \in B : A \subseteq B
    \end{cases}$$

    Para el caso general de $m = 1:$

    $$\begin{align*}
    B + A &\triangleq \begin{cases}
      \llbracket a_1^A, b_1^A, a_1^B, b_1^B, \ldots, a_n^B, b_n^B \rrbracket \\
      \quad \text{si } b_1^A < a_1^B \\
      \llbracket a_1^A, b_1^B, a_2^B, b_2^B, \ldots, a_n^B, b_n^B \rrbracket \\
      \quad \text{si } b_1^A \ge a_1^B \land b_1^A \le b_1^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_n^B, b_n^B, a_1^A, b_1^A \rrbracket \\
      \quad \text{si } a_1^A > b_n^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_{n-1}^B, b_{n-1}^B, a_n^B, b_1^A \rrbracket \\
      \quad \text{si } a_1^A \le b_n^B \land a_1^A \ge a_n^B \land b_1^A > b_n^B \\
      \llbracket a_1^A, b_1^A, a_k^B, b_k^B, \ldots, a_n^B, b_n^B \rrbracket \\
      \quad \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A > b_{k-1}^B \land b_1^A < a_k^B \\
      \llbracket a_1^A, b_k^B, a_{k+1}^B, b_{k+1}^B, \ldots, a_n^B, b_n^B \rrbracket \\
      \quad \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A \ge a_k^B \land b_1^A \le b_k^B
    \end{cases} \\[1em]
    &\phantom{\triangleq} \begin{cases}
      \llbracket a_1^B, b_1^B, \ldots, b_{k-1}^B, a_1^A, b_1^A, a_k^B, b_k^B, \ldots \rrbracket \\
      \quad \text{si } \exists k<n : a_1^A > b_{k-1}^B \land a_1^A \le a_k^B \land b_1^A < a_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^A, b_k^B, a_{k+1}^B, \dots \rrbracket \\
      \quad \text{si } \exists l<k<n : a_1^A \ge b_{l-1}^B \land a_1^A \le a_l^B \land b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^B, b_k^B, a_{k+1}^B, \dots \rrbracket \\
      \quad \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^B, b_1^A, a_{k+1}^B, \dots \rrbracket \\
      \quad \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A > b_k^B \land b_1^A < a_{k+1}^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_l^B, b_l^B, a_1^A, b_1^A, a_k^B, \dots \rrbracket \\
      \quad \text{si } \exists l<k<n : a_1^A > b_l^B \land a_1^A < a_{l+1}^B \land b_1^A > b_{k-1}^B \land b_1^A < a_k^B
    \end{cases}
    \end{align*}$$

    Para el caso $m = 1$ o $m = 0$ y especiales queda demostrado el
    cerramiento de $\mathbb{B}$ bajo esta suma reducida. El caso
    siguiente se construye con facilidad por recurrencia en cualquier
    número finito de pasos.

    Para cualquier $m > 1:$

    $$B + A \triangleq \begin{cases}
      \sum_{i=1}^{m} \left( B + \llbracket a_i^A, b_i^A \rrbracket \right) & \text{si } 1 \le i \le m, A_0 \triangleq \llbracket \varnothing \rrbracket, A_{i+1} \triangleq A_i + \llbracket a_i^A, b_i^A \rrbracket
    \end{cases}$$

    Queda demostrado que toda suma da como resultado un conjunto finito
    de intervalos genéricos.

    A su vez el producto lo vamos a definir de forma recursiva también,
    comenzando primero con $A$ siendo la clase de un solo intervalo
    genérico, o la clase del vacío, además de algunos casos especiales.

    $$B \cdot A \triangleq \begin{cases}
      \llbracket \varnothing \rrbracket & \text{si } A = \llbracket \varnothing \rrbracket \lor B = \llbracket \varnothing \rrbracket \\
      A & \text{si } B = 1 \\
      B & \text{si } A = 1 \\
      \llbracket \varnothing \rrbracket & \text{si } \exists A \in A, B \in B : B \subseteq \overline{A} \lor A \subseteq \overline{B} \\
      A & \text{si } \exists A \in A, B \in B : A \subseteq B \\
      B & \text{si } \exists A \in A, B \in B : B \subseteq A
    \end{cases}$$

    Para el caso general de $m = 1:$

    $$\begin{align*}
    B \cdot A &\triangleq \begin{cases}
      \llbracket a_1^A, a_1^B \dots \rrbracket \\
      \quad \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A \ge b_{k-1}^B \land b_1^A < a_k^B \\
      \llbracket a_1^B, b_1^B, \ldots, a_k^B, b_1^A \rrbracket \\
      \quad \text{si } a_1^A \le a_1^B \land \exists k<n : b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^A, b_1^B, \ldots, a_{k-1}^B \dots \rrbracket \\
      \quad \text{si } a_1^A \ge a_1^B \land a_1^A \le b_1^B \land \exists k<n : b_1^A \ge b_{k-1}^B \land b_1^A < a_k^B \\
      \llbracket a_1^A, b_1^B, a_2^B, b_2^B, \ldots, a_k^B, b_1^A \rrbracket \\
      \quad \text{si } a_1^A \ge a_1^B \land a_1^A \le b_1^B \land \exists k<n : b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^A, b_l^B, \dots, a_k^B, b_1^A \rrbracket \\
      \quad \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A \ge a_k^B \land b_1^A \le b_k^B \\
      \llbracket a_1^A, b_l^B, \dots, a_{k-1}^B, b_{k-1}^B \rrbracket \\
      \quad \text{si } \exists l<k<n : a_1^A \ge a_l^B \land a_1^A \le b_l^B \land b_1^A > b_{k-1}^B \land b_1^A < a_k^B
    \end{cases}
    \end{align*}$$

    Para el caso $m = 1$ o $m = 0$ y especiales queda demostrado el
    cerramiento de $\mathbb{B}$ bajo este producto reducido.

    Para el caso $m > 1:$

    $$B \cdot A \triangleq \begin{cases}
      \sum_{i=1}^{m} \left( B \cdot \llbracket a_i^A, b_i^A \rrbracket \right) & \text{si } 1 \le i \le m, A_0 \triangleq \llbracket \varnothing \rrbracket, A_{i+1} \triangleq A_i + \llbracket a_i^A, b_i^A \rrbracket
    \end{cases}$$

Y queda demostrado que la forma del conjunto producto es una clase de
unión finita de subintervalos genéricos. Luego pertenece a nuestro
álgebra de Boole.

Este sistema es muy parecido a un álgebra de conjuntos subálgebra de
algún conjunto po­tencia, por lo que es fácil determinar que se trata de
un álgebra de Boole. Sin embargo su cardinal es
$$\#{\left( {\left( {\mathbb{Q} \times \mathbb{Q}} \right) \times \left( {\mathbb{N} \times \mathbb{N}} \right)} \right) = \#}\left( \mathbb{N} \right) .$$
Veámoslo:

$$\begin{align*}
  \#\left( \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}} \right) &= \#\left( \bigcup \begin{Bmatrix}
  \llbracket\varnothing \rrbracket, \\
  \llbracket a_1, b_1 \rrbracket, \\
  \llbracket a_1, b_1, a_2, b_2 \rrbracket, \\
  \llbracket a_1, b_1, a_2, b_2, a_3, b_3 \rrbracket, \\
  \vdots \\
  \llbracket a_1, b_1, a_2, b_2, a_3, b_3, \ldots, a_n, b_n \rrbracket, \\
  \vdots
  \end{Bmatrix} \right) \\
  &\leq 1 + \#\left( \bigcup_{i \in \mathbb{N}} \bigcup_{j \in \mathbb{N}} (\mathbb{Q} \times \mathbb{Q}) \right) = \#( \mathbb{N} \times \mathbb{N} \times \mathbb{Q} \times \mathbb{Q} ) = \#\mathbb{N} = \aleph_{0}
\end{align*}$$

En definitiva es un álgebra numerable (del mismo cardinal que los
números naturales). Puesto que el cardinal de los números naturales
$\mathbb{N}$ no es conmensurable con el de la potencia de ningún
conjunto (es del cardinal infinito más pequeño posible y ningún conjunto
finito tiene como potencia uno infinito), no existe ningún conjunto para
el cual esta álgebra de Boole sea semejante (isomorfa) a un álgebra de
las potencias de un conjunto. Este ejemplo será de utilidad más
adelante, además de darnos un curioso ejemplo de álgebra de Boole nada
común.

**\[Ejemplo 10\]** El álgebra de Boole de los subconjuntos finitos y
cofinitos de los números naturales ($\mathbb{N}$). Consideremos el
conjunto base
$B = \{ X \subseteq \mathbb{N} \mid X \text{ es finito o } \mathbb{N} \setminus X \text{ es finito} \}.$
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
natural, $\{n\}.$ Esta genialidad geométrica demuestra que, en el
infinito, pueden existir álgebras de Boole del mismo cardinal que son
estructuralmente distintas (algo que, como demostramos en el Capítulo 7,
es imposible en las álgebras finitas).

**\[Ejemplo 11\]** El álgebra de las funciones de un álgebra de Boole
sobre otra. Supongamos $f: B \rightarrow B'$ dónde $f$ es una función.
Llamaremos
$$\mathtt{F}(B,B') = \{ f:B\rightarrow B' \mid \forall x \in B \exists! y \in B', f(x) = y \}$$
a nuestro conjunto de Boole. $f_{0'}$ es la función que asigna el cero
de $B'$ a cualquier elemento de $B.$ Igualmente $f_{1'}$ es la función
que asigna el uno de $B'$ a cualquier elemento de $B.$ Las operaciones
internas a introducir son:

- La suma de funciones:
  $\forall x \in B, [f + g](x) \triangleq f(x) + g(x).$

- La multiplicación de funciones:
  $\forall x \in B, [f \cdot g](x) \triangleq f(x) \cdot g(x).$

- La función complemento:
  $\forall f \in \mathtt{F}(B,B'), \forall x \in B, \overline{f}(x) \triangleq \overline{f(x)}.$

De esta álgebra podemos entresacar otros conjuntos de funciones
interesantes, como. Por ejemplo:

$$\begin{align*}
  \mathtt{Hom}(B,B') = \{ f \in \mathtt{F}(B,B') \mid \ &f(0) = 0', f(1) = 1', \\
  &\forall x,y \in B : f(x + y) = f(x) + f(y) \land f(x \cdot y) = f(x) \cdot f(y), \\
  &\forall x \in B : f(\overline{x}) = \overline{f(x)} \}
\end{align*}$$

y aún otros subconjuntos más pequeños serían las inyecciones de los
anteriores homomorfismos. Si $B' \equiv B$ entonces uno de los conjuntos
de aplicaciones más interesantes son los endomorfimos o isomorfimos en
sí mismo.

Además el kernel de cualquier homomorfismo es un subálgebra de $B.$ Los
homomorfismos de las álgebras booleanas tienen propiedades interesantes
que no veremos aquí.

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

Al ser $1 + 1 = x$, dónde $x$ es ningún elemento de $\mathbb{B},$ o
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
simetría entre las operaciones $\vee$ y $\wedge,$ y entre las constantes
$\bot$ y $\top.$ Si en cualquier postulado intercambiamos $\vee$ por
$\wedge$ y $\bot$ por $\top,$ obtenemos otro postulado válido del
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

> **Teorema (Unicidad de los elementos neutros -
> $Unic_e, Unic_u$):**[]{#unicidad_neutros label="unicidad_neutros"} Los
> elementos neutros descritos en los postulados son únicos. No existe
> ningún otro elemento en el conjunto que se comporte como el mínimo
> $\bot$ para la operación $\vee,$ ni ningún otro que actúe como el
> máximo $\top$ para la operación $\wedge:$ $$\begin{align*}
>     \exists! e \in \mathbb{B}, \forall a \in \mathbb{B}, a \vee e &= a \implies e = \bot \quad (Unic_e) \\
>     \exists! u \in \mathbb{B}, \forall a \in \mathbb{B}, a \wedge u &= a \implies u = \top \quad (Unic_u)
> \end{align*}$$

**Demostración:**

::: proof
*Demostración de $Unic_e$.* Sea $e \in \mathbb{B}$ tal que
$\forall a \in \mathbb{B}, a \vee e = a.$ Tomando $a = \bot:$
$$\begin{align*}
    e &= e \vee \bot & (ElemNeu_\vee) \\
      &= \bot \vee e & (Comm_\vee) \\
      &= \bot & (\text{Hipótesis sobre } e)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $Unic_u$ (Dual).* Para obtener la prueba dual,
intercambiamos $\vee$ por $\wedge$ y $\bot$ por $\top.$ Sea
$u \in \mathbb{B}$ tal que $\forall a \in \mathbb{B}, a \wedge u = a.$
Tomando $a = \top:$ $$\begin{align*}
    u &= u \wedge \top & (ElemNeu_\wedge) \\
      &= \top \wedge u & (Comm_\wedge) \\
      &= \top & (\text{Hipótesis sobre } u)
\end{align*}$$ ◻
:::

> **Teorema (Idempotencia -
> $Idemp_\vee, Idemp_\wedge$):**[]{#idempotencia label="idempotencia"}
> Operar un elemento consigo mismo, independientemente de si usamos
> $\vee$ o $\wedge,$ no altera su valor. El elemento se mantiene
> idéntico a sí mismo: $$\begin{align*}
>     \forall a \in \mathbb{B}, \quad a \vee a &= a \quad (Idemp_\vee) \\
>     \forall a \in \mathbb{B}, \quad a \wedge a &= a \quad (Idemp_\wedge)
> \end{align*}$$

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

> **Teorema (Elementos absorbentes -
> $Abs_{\bot}, Abs_{\top}$):**[]{#absorbentes label="absorbentes"}
> Cualquier elemento operado mediante $\vee$ con el máximo $\top$ es
> absorbido por este, dando como resultado $\top.$ De igual manera,
> operar cualquier elemento mediante $\wedge$ con el mínimo $\bot$
> siempre resulta en $\bot:$ $$\begin{align*}
>     \forall a \in \mathbb{B}, \quad a \vee \top &= \top \\
>     \forall a \in \mathbb{B}, \quad a \wedge \bot &= \bot
> \end{align*}$$

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

> **Teorema (Condición de Álgebra Trivial):**[]{#trivial_cond
> label="trivial_cond"} Si se da el caso extremo de que el elemento
> mínimo $\bot$ y el máximo $\top$ son exactamente el mismo, entonces
> estamos ante un álgebra que contiene un único elemento en todo su
> conjunto (el álgebra trivial):
> $$\bot = \top \implies \mathbb{B} = \{\top\} = \{\bot\}$$

**Demostración:**

::: proof
*Proof.* Supongamos que $\bot = \top.$ Sea $x \in \mathbb{B}$ un
elemento cualquiera: $$\begin{align*}
    x &= x \vee \bot & (ElemNeu_\vee) \\
      &= x \vee \top & (\text{Hipótesis } \bot = \top) \\
      &= \top & (Abs_\top)
\end{align*}$$ Por tanto, todo elemento $x$ del conjunto es idéntico a
$\top,$ lo que implica que $\mathbb{B} = \{\top\} = \{\bot\}.$ ◻
:::

> **Teorema (Complemento Idéntico implica Álgebra
> Trivial):**[]{#trivial_comp label="trivial_comp"} Si dentro de la
> estructura existe algún elemento que sea igual a su propio complemento
> ($\neg a = a$), entonces forzosamente todo el sistema colapsa en el
> álgebra trivial de un solo elemento:
> $$(\exists a \in \mathbb{B} : \neg a = a) \implies \mathbb{B} = \{\top\} = \{\bot\}$$

**Demostración:**

::: proof
*Proof.* Supongamos que existe $a \in \mathbb{B}$ tal que $\neg a = a.$
Por el postulado del Complemento ($Comp_\vee$ y $Comp_\wedge$), sabemos
que $a \vee \neg a = \top$ y $a \wedge \neg a = \bot.$ Sustituyendo la
hipótesis $\neg a = a$ en ambas ecuaciones, obtenemos:
$$a \vee a = \top \quad \text{y} \quad a \wedge a = \bot$$ Aplicando el
teorema de Idempotencia ($Idemp_\vee$ y $Idemp_\wedge$), sabemos que
$a \vee a = a$ y $a \wedge a = a.$ Por tanto:
$$a = \top \quad \text{y} \quad a = \bot$$ Lo cual implica que
$\bot = \top.$ Aplicando el teorema anterior (Condición de Álgebra
Trivial), concluimos que $\mathbb{B} = \{\top\} = \{\bot\}.$ ◻
:::

> **Teorema (Propiedades de absorción -
> $Abs_{\vee}, Abs_{\wedge}$):**[]{#absorcion label="absorcion"} Cuando
> se combinan ambas operaciones anidando un elemento consigo mismo y con
> un tercero, el elemento repetido \"absorbe\" al otro,
> independientemente del valor del segundo: $$\begin{align*}
>     \forall a, b \in \mathbb{B}, \quad a \vee (a \wedge b) &= a \\
>     \forall a, b \in \mathbb{B}, \quad a \wedge (a \vee b) &= a
> \end{align*}$$

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

> **Teorema (Propiedades de orden de retículo -
> $Prop_{\vee,\wedge}$):**[]{#prop_reticulo label="prop_reticulo"}
> Existe una correspondencia biunívoca fundamental entre las dos
> operaciones: afirmar que un elemento domina a otro mediante $\vee$
> equivale matemáticamente a afirmar que el segundo se impone al primero
> mediante $\wedge:$
> $$\forall a, b \in \mathbb{B}: \quad a \vee b = a \iff a \wedge b = b$$

**Demostración:**

::: proof
*Demostración de $\implies$.* Supongamos que $a \vee b = a.$
$$\begin{align*}
    a \wedge b &= b \wedge a & (Comm_\wedge) \\
               &= b \wedge (a \vee b) & (\text{Hipótesis } a \vee b = a) \\
               &= b & (Abs_\wedge)
\end{align*}$$ ◻
:::

::: proof
*Demostración de $\impliedby$ (Dual).* Supongamos que $a \wedge b = b.$
$$\begin{align*}
    a \vee b &= b \vee a & (Comm_\vee) \\
               &= (a \wedge b) \vee a & (\text{Hipótesis } a \wedge b = b) \\
               &= a \vee (a \wedge b) & (Comm_\vee) \\
               &= a & (Abs_\vee)
\end{align*}$$ ◻
:::

> **Teorema (Equivalencia de operaciones -
> $Equa_{\vee,\wedge}$):**[]{#equa_operaciones label="equa_operaciones"}
> Si operar dos elementos mediante $\vee$ da exactamente el mismo
> resultado que operarlos mediante $\wedge,$ esto sólo es lógicamente
> posible si ambos elementos son en realidad el mismo:
> $$\forall a, b \in \mathbb{B}: \quad a \vee b = a \wedge b \implies a = b$$

**Demostración:**

::: proof
*Proof.* Supongamos $a \vee b = a \wedge b.$ Observamos que:
$$\begin{align*}
    a &= a \vee (a \wedge b) & (Abs_\vee) \\
      &= a \vee (a \vee b) & (\text{Hipótesis})
\end{align*}$$ Aplicando $Prop_{\vee,\wedge},$ dado que
$a \vee (a \vee b) = a,$ deducimos que $a \wedge (a \vee b) = a \vee b.$
$$\begin{align*}
    a \vee b &= a \wedge (a \vee b) & (\text{Resultado anterior}) \\
             &= a & (Abs_\wedge)
\end{align*}$$ De manera simétrica para $b:$ $$\begin{align*}
    b &= b \vee (a \wedge b) & (Abs_\vee) \\
      &= b \vee (a \vee b) & (\text{Hipótesis}) \\
      &= (a \vee b) \vee b & (Comm_\vee)
\end{align*}$$ Aplicando de nuevo $Prop_{\vee,\wedge}$ sobre esta
igualdad, obtenemos que $(a \vee b) \wedge b = a \vee b.$ Pero sabemos
por $Abs_\wedge$ que $(a \vee b) \wedge b = b \wedge (a \vee b) = b.$
Por consiguiente, $a \vee b = b.$ Finalmente, uniendo ambos resultados:
$a = a \vee b = b.$ ◻
:::

> **Teorema (Teorema de Cancelación - $Equa_{canc}$):**[]{#equa_canc
> label="equa_canc"} Si un elemento $a$ se opera mediante $\vee$ con $b$
> y con $c$ dando el mismo resultado, y además se opera mediante
> $\wedge$ con $b$ y con $c$ coincidiendo también los resultados,
> entonces forzosamente $b$ y $c$ son el mismo elemento:
> $$\forall a, b, c \in \mathbb{B}: \quad a \vee b = a \vee c \quad \text{y} \quad a \wedge b = a \wedge c \implies b = c$$

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

> **Teorema (Unicidad del complemento - $Unic_{comp}$):**[]{#unic_comp
> label="unic_comp"} Todo elemento del conjunto tiene un complemento
> $\neg a,$ y este es estrictamente único. Ningún otro elemento puede
> cumplir simultáneamente las dos condiciones del postulado del
> complemento para un mismo $a:$
> $$\forall a, x \in \mathbb{B} : \quad (a \vee x = \top \quad \text{y} \quad a \wedge x = \bot) \implies x = \neg a$$

**Demostración:**

::: proof
*Proof.* Supongamos que existe $x \in \mathbb{B}$ tal que
$a \vee x = \top$ y $a \wedge x = \bot.$ $$\begin{align*}
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
$x$ tiene que ser necesariamente $\neg a.$ ◻
:::

> **Teorema (Involución - $Comp_{inv}$):**[]{#comp_inv label="comp_inv"}
> Aplicar la operación de complemento (o negación) dos veces
> consecutivas sobre un mismo elemento cancela su efecto, devolviendo el
> elemento original intacto:
> $$\forall a \in \mathbb{B}, \quad \neg (\neg a) = a$$

**Demostración:**

::: proof
*Proof.* Por definición, el complemento de $\neg a,$ denotado como
$\neg (\neg a),$ es el elemento único que satisface:
$$\neg a \vee \neg (\neg a) = \top \quad \text{y} \quad \neg a \wedge \neg (\neg a) = \bot$$
Sin embargo, por la conmutatividad ($Comm_\vee$ y $Comm_\wedge$),
sabemos que:
$$\neg a \vee a = a \vee \neg a = \top \quad \text{y} \quad \neg a \wedge a = a \wedge \neg a = \bot$$
Esto demuestra que $a$ actúa como un complemento de $\neg a.$ Por el
teorema de unicidad del complemento ($Unic_{comp}$), concluimos
necesariamente que $\neg (\neg a) = a.$ ◻
:::

> **Teorema (Leyes de De Morgan - $Mor_{\vee, \wedge}$):**[]{#morgan
> label="morgan"} La negación matemática se distribuye sobre las
> operaciones, pero al hacerlo, invierte la operación original: un
> supremo ($\vee$) negado se convierte en el ínfimo ($\wedge$) de las
> negaciones, y viceversa: $$\begin{align}
>     \neg (a \vee b) &= \neg a \wedge \neg b \\
>     \neg (a \wedge b) &= \neg a \vee \neg b
> \end{align}$$ De forma equivalente, aislando las variables mediante la
> involución, podemos expresar las operaciones básicas exclusivamente a
> partir de su dual negada: $$\begin{align}
>     a \vee b &= \neg (\neg a \wedge \neg b) \\
>     a \wedge b &= \neg (\neg a \vee \neg b)
> \end{align}$$

**Demostración:**

::: proof
*Demostración de $\neg (a \vee b) = \neg a \wedge \neg b$.* Para
demostrarlo sin recurrir a la asociatividad, usaremos las propiedades de
absorción. Comprobemos primero la suma:
$(a \vee b) \vee (\neg a \wedge \neg b) = \top.$ Sabemos por
$Abs_\wedge$ que $a \wedge (a \vee b) = a.$ $$\begin{align*}
    \neg a \vee (a \wedge (a \vee b)) &= \neg a \vee a = \top & (Comp_\vee) \\
    (\neg a \vee a) \wedge (\neg a \vee (a \vee b)) &= \top & (Dist_\vee) \\
    \top \wedge (\neg a \vee (a \vee b)) &= \top & (Comp_\vee) \\
    \neg a \vee (a \vee b) &= \top & (ElemNeu_\wedge)
\end{align*}$$ Simétricamente, como
$b \wedge (a \vee b) = b \wedge (b \vee a) = b,$ obtenemos
$\neg b \vee (a \vee b) = \top.$ Por tanto: $$\begin{align*}
    (a \vee b) \vee (\neg a \wedge \neg b) &= ((a \vee b) \vee \neg a) \wedge ((a \vee b) \vee \neg b) & (Dist_\vee) \\
    &= (\neg a \vee (a \vee b)) \wedge (\neg b \vee (a \vee b)) & (Comm_\vee) \\
    &= \top \wedge \top & (\text{Resultados anteriores}) \\
    &= \top & (Idemp_\wedge)
\end{align*}$$

Segundo, comprobemos el producto:
$(a \vee b) \wedge (\neg a \wedge \neg b) = \bot.$ Sabemos por
$Abs_\vee$ que $\neg a \vee (\neg a \wedge \neg b) = \neg a.$
$$\begin{align*}
    a \wedge (\neg a \vee (\neg a \wedge \neg b)) &= a \wedge \neg a = \bot & (Comp_\wedge) \\
    (a \wedge \neg a) \vee (a \wedge (\neg a \wedge \neg b)) &= \bot & (Dist_\wedge) \\
    \bot \vee (a \wedge (\neg a \wedge \neg b)) &= \bot & (Comp_\wedge) \\
    a \wedge (\neg a \wedge \neg b) &= \bot & (ElemNeu_\vee)
\end{align*}$$ Simétricamente, como
$\neg b \vee (\neg a \wedge \neg b) = \neg b \vee (\neg b \wedge \neg a) = \neg b,$
obtenemos $b \wedge (\neg a \wedge \neg b) = \bot.$ Por tanto:
$$\begin{align*}
    (a \vee b) \wedge (\neg a \wedge \neg b) &= (\neg a \wedge \neg b) \wedge (a \vee b) & (Comm_\wedge) \\
    &= ((\neg a \wedge \neg b) \wedge a) \vee ((\neg a \wedge \neg b) \wedge b) & (Dist_\wedge) \\
    &= (a \wedge (\neg a \wedge \neg b)) \vee (b \wedge (\neg a \wedge \neg b)) & (Comm_\wedge) \\
    &= \bot \vee \bot & (\text{Resultados anteriores}) \\
    &= \bot & (Idemp_\vee)
\end{align*}$$ Por el teorema de unicidad ($Unic_{comp}$), concluimos
que $\neg (a \vee b) = \neg a \wedge \neg b.$ ◻
:::

::: proof
*Demostración de $\neg (a \wedge b) = \neg a \vee \neg b$ (Dual).*
Intercambiando operaciones y constantes, comprobamos el producto:
$(a \wedge b) \wedge (\neg a \vee \neg b) = \bot.$ Sabemos por
$Abs_\vee$ que $a \vee (a \wedge b) = a.$ $$\begin{align*}
    \neg a \wedge (a \vee (a \wedge b)) &= \neg a \wedge a = \bot & (Comp_\wedge) \\
    (\neg a \wedge a) \vee (\neg a \wedge (a \wedge b)) &= \bot & (Dist_\wedge) \\
    \bot \vee (\neg a \wedge (a \wedge b)) &= \bot & (Comp_\wedge) \\
    \neg a \wedge (a \wedge b) &= \bot & (ElemNeu_\vee)
\end{align*}$$ Simétricamente, $\neg b \wedge (a \wedge b) = \bot.$ Por
tanto: $$\begin{align*}
    (a \wedge b) \wedge (\neg a \vee \neg b) &= ((a \wedge b) \wedge \neg a) \vee ((a \wedge b) \wedge \neg b) & (Dist_\wedge) \\
    &= (\neg a \wedge (a \wedge b)) \vee (\neg b \wedge (a \wedge b)) & (Comm_\wedge) \\
    &= \bot \vee \bot = \bot & (\text{Resultados anteriores})
\end{align*}$$

Comprobemos la suma: $(a \wedge b) \vee (\neg a \vee \neg b) = \top.$
Sabemos por $Abs_\wedge$ que
$\neg a \wedge (\neg a \vee \neg b) = \neg a.$ $$\begin{align*}
    a \vee (\neg a \wedge (\neg a \vee \neg b)) &= a \vee \neg a = \top & (Comp_\vee) \\
    (a \vee \neg a) \wedge (a \vee (\neg a \vee \neg b)) &= \top & (Dist_\vee) \\
    \top \wedge (a \vee (\neg a \vee \neg b)) &= \top & (Comp_\vee) \\
    a \vee (\neg a \vee \neg b) &= \top & (ElemNeu_\wedge)
\end{align*}$$ Simétricamente, $b \vee (\neg a \vee \neg b) = \top.$ Por
tanto: $$\begin{align*}
    (a \wedge b) \vee (\neg a \vee \neg b) &= (\neg a \vee \neg b) \vee (a \wedge b) & (Comm_\vee) \\
    &= ((\neg a \vee \neg b) \vee a) \wedge ((\neg a \vee \neg b) \vee b) & (Dist_\vee) \\
    &= (a \vee (\neg a \vee \neg b)) \wedge (b \vee (\neg a \vee \neg b)) & (Comm_\vee) \\
    &= \top \wedge \top = \top & (\text{Resultados anteriores})
\end{align*}$$ Por $Unic_{comp},$
$\neg (a \wedge b) = \neg a \vee \neg b.$ ◻
:::

::: proof
*Demostración de $a \vee b = \neg (\neg a \wedge \neg b)$ y su dual.*
Partiendo de $\neg (\neg a \wedge \neg b),$ aplicamos De Morgan a sus
componentes: $$\begin{align*}
    \neg (\neg a \wedge \neg b) &= \neg (\neg a) \vee \neg (\neg b) & (Mor_\wedge) \\
    &= a \vee b & (Comp_{inv})
\end{align*}$$ Dualizando la expresión, obtenemos de manera idéntica que
$\neg (\neg a \vee \neg b) = a \wedge b.$ ◻
:::

> **Teorema (Asociatividad -
> $Asoc_\vee, Asoc_\wedge$):**[]{#asociatividad label="asociatividad"}
> El orden en el que se agrupan tres o más elementos al aplicar de forma
> consecutiva la misma operación ($\vee$ o $\wedge$) no altera el
> resultado final. Al ubicar este teorema después de De Morgan, podemos
> simplificar enormemente su demostración: $$\begin{align*}
>     a \vee (b \vee c) &= (a \vee b) \vee c \\
>     a \wedge (b \wedge c) &= (a \wedge b) \wedge c
> \end{align*}$$

**Demostración:**

::: proof
*Demostración de $a \vee (b \vee c) = (a \vee b) \vee c$.* Primero,
demostraremos un pequeño **Lema de Igualdad por Casos**: Si
$x \wedge y = x \wedge z$ y $\neg x \wedge y = \neg x \wedge z,$
entonces $y = z.$ $$\begin{align*}
    y &= \top \wedge y & (ElemNeu_\wedge) \\
      &= (x \vee \neg x) \wedge y & (Comp_\vee) \\
      &= (x \wedge y) \vee (\neg x \wedge y) & (Dist_\wedge) \\
      &= (x \wedge z) \vee (\neg x \wedge z) & (\text{Por hipótesis del Lema}) \\
      &= (x \vee \neg x) \wedge z & (Dist_\wedge) \\
      &= \top \wedge z = z & (Comp_\vee, ElemNeu_\wedge)
\end{align*}$$ Sea $L = a \vee (b \vee c)$ y $R = (a \vee b) \vee c.$
Aplicaremos el lema usando $x = a,$ por lo que debemos demostrar que
$a \wedge L = a \wedge R$ y $\neg a \wedge L = \neg a \wedge R.$

1\) Comprobamos $a \wedge L = a \wedge R:$ $$\begin{align*}
    a \wedge L &= a \wedge (a \vee (b \vee c)) = a & (Abs_\wedge) \\
    a \wedge R &= a \wedge ((a \vee b) \vee c) \\
               &= (a \wedge (a \vee b)) \vee (a \wedge c) & (Dist_\wedge) \\
               &= a \vee (a \wedge c) = a & (Abs_\wedge, Abs_\vee)
\end{align*}$$ Por tanto, $a \wedge L = a \wedge R.$

2\) Comprobamos $\neg a \wedge L = \neg a \wedge R:$ $$\begin{align*}
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
\end{align*}$$ Como $\neg a \wedge L = \neg a \wedge R,$ aplicando el
Lema concluimos que $L = R,$ es decir,
$a \vee (b \vee c) = (a \vee b) \vee c.$ ◻
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

> **Teorema (Teorema de Adyacencia (Expansión de Shannon) -
> $Ady_{\vee, \wedge}$):**[]{#adyacencia label="adyacencia"} Cualquier
> elemento $a$ puede ser expandido con respecto a otra variable $b$ y su
> complemento. $$\begin{align*}
>     \text{Adyacencia en $\vee:$ } & a = (a \wedge b) \vee (a \wedge \neg b) \\
>     \text{Adyacencia en $\wedge:$ } & a = (a \vee b) \wedge (a \vee \neg b)
> \end{align*}$$

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

> **Teorema (Teorema de Reducción (Absorción Fuerte) -
> $Red_{\vee, \wedge}$):**[]{#reduccion label="reduccion"} La disyunción
> de una variable con la conjunción de su complemento y otra variable,
> se reduce a la disyunción de ambas variables. $$\begin{align*}
>     \text{Para la disyunción: } & a \vee (\neg a \wedge b) = a \vee b \\
>     \text{Para la conjunción (Dual): } & a \wedge (\neg a \vee b) = a \wedge b
> \end{align*}$$

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

> **Teorema (Teorema del Consenso (Quine) -
> $Cons_{\vee, \wedge}$):**[]{#consenso label="consenso"} En una
> expresión con tres variables donde una variable aparece afirmada en un
> término, negada en otro, y el tercer término (el consenso) está
> formado por las variables restantes, este último término es
> redundante. $$\begin{align*}
>     \text{Consenso en $\vee:$ } & (a \wedge b) \vee (\neg a \wedge c) \vee (b \wedge c) = (a \wedge b) \vee (\neg a \wedge c) \\
>     \text{Consenso en $\wedge:$ } & (a \vee b) \wedge (\neg a \vee c) \wedge (b \vee c) = (a \vee b) \wedge (\neg a \vee c)
> \end{align*}$$

::: proof
*Proof.* Demostración para la versión en $\vee:$ $$\begin{align*}
    (a \wedge b) \vee (\neg a \wedge c) \vee (b \wedge c) &= (a \wedge b) \vee (\neg a \wedge c) \vee ((b \wedge c) \wedge \top) & \text{Ax. Neutro ($E_n$)} \\
    &= (a \wedge b) \vee (\neg a \wedge c) \vee ((b \wedge c) \wedge (a \vee \neg a)) & \text{Ax. Comp.} \\
    &= (a \wedge b) \vee (\neg a \wedge c) \vee (a \wedge b \wedge c) \vee (\neg a \wedge b \wedge c) & \text{Dist. y Asoc.} \\
    &= ((a \wedge b) \vee (a \wedge b \wedge c)) \\
    &\quad \vee ((\neg a \wedge c) \vee (\neg a \wedge c \wedge b)) & \text{Conm. y Asoc.} \\
    &= (a \wedge b) \vee (\neg a \wedge c) & \text{Absorción ($Abs_{\vee}$)}
\end{align*}$$ La prueba dual sigue el mismo principio (sumar $\bot$ al
consenso, expandirlo con $(a \wedge \neg a),$ y simplificar usando
absorción). ◻
:::

## Generalización a $n$ variables

Habiendo demostrado la asociatividad ($Asoc_\vee$ y $Asoc_\wedge$) de
las operaciones fundamentales del álgebra de Boole, el orden en el que
se agrupan las variables al aplicar consecutivamente una misma operación
resulta irrelevante. Esto nos permite prescindir de los paréntesis y
extender de forma natural las operaciones binarias a un número
arbitrario $n$ de operandos.

> **Definicion (Disyunción (Supremo) de $n$
> variables):**[]{#or_n_variables label="or_n_variables"} La disyunción
> múltiple de $n$ variables, denotada de forma compacta mediante el
> operador $\bigvee,$ se define como la aplicación sucesiva de la
> operación $\vee:$
> $$\bigvee_{i=1}^n x_i \triangleq x_1 \vee x_2 \vee \dots \vee x_n$$

> **Definicion (Conjunción (Ínfimo) de $n$
> variables):**[]{#and_n_variables label="and_n_variables"} De manera
> análoga, la conjunción múltiple de $n$ variables, denotada mediante el
> operador $\bigwedge,$ se define como la aplicación sucesiva de la
> operación $\wedge:$
> $$\bigwedge_{i=1}^n x_i \triangleq x_1 \wedge x_2 \wedge \dots \wedge x_n$$

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

> **Definicion (Operador NAND (Barra de Sheffer)):**[]{#nand
> label="nand"} Denotado clásicamente con una flecha hacia arriba
> ($\uparrow$), se define como la negación del ínfimo.
> $$a \uparrow b \triangleq \neg (a \wedge b) = \neg a \vee \neg b$$

> **Definicion (Operador NOR (Flecha de Peirce)):**[]{#nor label="nor"}
> Denotado con una flecha hacia abajo ($\downarrow$), se define como la
> negación del supremo.
> $$a \downarrow b \triangleq \neg (a \vee b) = \neg a \wedge \neg b$$

> **Definicion (Operador XOR (O-exclusiva)):**[]{#xor label="xor"}
> Denotado con el símbolo de suma exclusiva ($\oplus$), evalúa a $\top$
> cuando exactamente uno de los operandos es $\top$ y el otro $\bot.$
> $$a \oplus b \triangleq (a \wedge \neg b) \vee (\neg a \wedge b)$$

> **Definicion (Operador XNOR (No-O-exclusiva o
> Equivalencia)):**[]{#xnor label="xnor"} Denotado frecuentemente con
> $\odot$ o $\leftrightarrow,$ es la negación de la operación XOR y
> evalúa a $\top$ cuando ambos operandos son idénticos.
> $$a \odot b \triangleq \neg (a \oplus b) = (a \wedge b) \vee (\neg a \wedge \neg b)$$

> **Definicion (Generalización a $n$ variables de NAND y
> NOR):**[]{#gen_nand_nor label="gen_nand_nor"} A diferencia de los
> operadores $\vee,$ $\wedge$ y $\oplus,$ los operadores NAND
> ($\uparrow$) y NOR ($\downarrow$) **no son asociativos**. Sin embargo,
> debido a su inmensa importancia práctica en la construcción de
> circuitos digitales, se define convencionalmente su generalización a
> $n$ variables como la negación de la conjunción o disyunción múltiple,
> respectivamente:
> $$\text{NAND}(x_1, x_2, \dots, x_n) \triangleq \neg \left( \bigwedge_{i=1}^n x_i \right)$$
> $$\text{NOR}(x_1, x_2, \dots, x_n) \triangleq \neg \left( \bigvee_{i=1}^n x_i \right)$$

## Comportamiento de los Operadores Derivados

Los operadores NAND ($\uparrow$) y NOR ($\downarrow$) presentan una
serie de propiedades algebraicas particulares. Al ser operadores
funcionalmente completos, permiten expresar cualquier otra operación
booleana utilizando exclusivamente uno de ellos.

> **Teorema (Idempotencia cruzada (Generación de
> NOT)):**[]{#idemp_cruzada label="idemp_cruzada"} Operar un elemento
> consigo mismo usando NAND o NOR equivale a su complemento (negación):
> $$\begin{align*}
>     \forall a \in \mathbb{B}, \quad a \uparrow a &= \neg a \\
>     \forall a \in \mathbb{B}, \quad a \downarrow a &= \neg a
> \end{align*}$$

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

> **Teorema (Generación del Ínfimo y Supremo (AND y
> OR)):**[]{#gen_inf_sup label="gen_inf_sup"} A partir de la propiedad
> anterior, podemos recuperar las operaciones básicas anidando las
> puertas consigo mismas: $$\begin{align*}
>     \forall a, b \in \mathbb{B}, \quad a \wedge b &= \neg (a \uparrow b) = (a \uparrow b) \uparrow (a \uparrow b) \\
>     \forall a, b \in \mathbb{B}, \quad a \vee b &= \neg (a \downarrow b) = (a \downarrow b) \downarrow (a \downarrow b)
> \end{align*}$$

**Demostración:**

::: proof
*Demostración.* Para la generación del ínfimo (AND): $$\begin{align*}
    \neg(a \uparrow b) &\triangleq \neg(\neg(a \wedge b)) & (\text{Definicion de NAND}) \\
                       &= a \wedge b & (Involucion)
\end{align*}$$ Además, por la idempotencia cruzada demostrada
anteriormente, $x \uparrow x = \neg x,$ por tanto:
$$\neg(a \uparrow b) = (a \uparrow b) \uparrow (a \uparrow b)$$ La
demostración para la generación del supremo (OR) es idéntica por
dualidad. ◻
:::

> **Teorema (Generación cruzada (Leyes de De Morgan para
> NAND/NOR)):**[]{#gen_cruzada label="gen_cruzada"} Podemos generar la
> operación opuesta (supremo desde NAND, e ínfimo desde NOR) negando
> previamente las entradas: $$\begin{align*}
>     \forall a, b \in \mathbb{B}, \quad a \vee b &= (\neg a) \uparrow (\neg b) = (a \uparrow a) \uparrow (b \uparrow b) \\
>     \forall a, b \in \mathbb{B}, \quad a \wedge b &= (\neg a) \downarrow (\neg b) = (a \downarrow a) \downarrow (b \downarrow b)
> \end{align*}$$

**Demostración:**

::: proof
*Demostración.* Para el supremo (OR): $$\begin{align*}
    (\neg a) \uparrow (\neg b) &\triangleq \neg (\neg a \wedge \neg b) & (\text{Definicion de NAND}) \\
                               &= \neg (\neg (a \vee b)) & (Mor_\vee) \\
                               &= a \vee b & (Involucion)
\end{align*}$$ La demostración para el ínfimo (AND) sigue los mismos
pasos de manera dual, aplicando $Mor_\wedge.$ ◻
:::

> **Teorema (Conmutatividad):**[]{#conmut_deriv label="conmut_deriv"} Al
> igual que sus operaciones base, ambos operadores son perfectamente
> conmutativos: $$\begin{align*}
>     \forall a, b \in \mathbb{B}, \quad a \uparrow b &= b \uparrow a \\
>     \forall a, b \in \mathbb{B}, \quad a \downarrow b &= b \downarrow a
> \end{align*}$$

**Demostración:**

::: proof
*Demostración.* Para la operación NAND: $$\begin{align*}
    a \uparrow b &\triangleq \neg (a \wedge b) & (\text{Definicion de NAND}) \\
                 &= \neg (b \wedge a) & (Comm_\wedge) \\
                 &\triangleq b \uparrow a & (\text{Definicion de NAND})
\end{align*}$$ Para la operación NOR, es análogo aplicando
$Comm_\vee.$ ◻
:::

> **Teorema (Inexistencia de Elemento Neutro):**[]{#no_neutro
> label="no_neutro"} No existe ningún elemento neutro para las
> operaciones NAND ni NOR en un álgebra de Boole general.

**Demostración:**

::: proof
*Demostración.* Si existiera un neutro $e$ para la operación NAND,
debería cumplirse que $\forall a, a \uparrow e = a,$ es decir,
$\neg(a \wedge e) = a.$ Si probamos con $e=\top,$ obtenemos
$\neg a = a,$ lo cual obliga al colapso en un álgebra trivial. Si
probamos con $e=\bot,$ obtenemos $\neg \bot = a \implies \top = a,$ lo
cual obviamente no se cumple para cualquier elemento $a.$ Lo mismo
aplica a la operación NOR. ◻
:::

> **Teorema (Comportamiento con las constantes (Fijación y
> Absorción)):**[]{#constantes_deriv label="constantes_deriv"} Fijar una
> constante específica en uno de los operandos genera directamente la
> negación, mientras que usar la constante opuesta actúa como un
> pseudo-elemento absorbente (devolviendo un valor constante inalterable
> por $a$): $$\begin{align*}
>     \text{Inversión: } & a \uparrow \top = \neg a \qquad & a \downarrow \bot &= \neg a \\
>     \text{Absorción: } & a \uparrow \bot = \top \qquad & a \downarrow \top &= \bot
> \end{align*}$$

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

> **Teorema (Ausencia de Asociatividad):**[]{#no_asoc_deriv
> label="no_asoc_deriv"} A diferencia del supremo ($\vee$) y el ínfimo
> ($\wedge$), las operaciones NAND y NOR son positivamente NO
> asociativas: $$\begin{align*}
>     (a \uparrow b) \uparrow c &\neq a \uparrow (b \uparrow c) \\
>     (a \downarrow b) \downarrow c &\neq a \downarrow (b \downarrow c)
> \end{align*}$$

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

> **Definicion (NAND y NOR de $n$ entradas):**[]{#def_n_entradas
> label="def_n_entradas"} Dado que las puertas NAND y NOR físicas a
> menudo tienen más de dos entradas, se definen algebraicamente para
> múltiples entradas como la negación de la conjunción o disyunción de
> todas ellas: $$\begin{align*}
>     \uparrow(x_1, x_2, \dots, x_n) &\triangleq \neg \left( \bigwedge_{i=1}^n x_i \right) \\
>     \downarrow(x_1, x_2, \dots, x_n) &\triangleq \neg \left( \bigvee_{i=1}^n x_i \right)
> \end{align*}$$ En particular, para el caso de 3 entradas que
> estudiaremos a continuación: $$\begin{align*}
>     \uparrow(a,b,c) &\triangleq \neg(a \wedge b \wedge c) \\
>     \downarrow(a,b,c) &\triangleq \neg(a \vee b \vee c)
> \end{align*}$$

> **Teorema (NAND/NOR múltiple vs agrupación
> binaria):**[]{#multiple_vs_binaria label="multiple_vs_binaria"} Como
> consecuencia directa de su falta de asociatividad, una operación NAND
> o NOR de 3 entradas no es equivalente a la agrupación secuencial en
> cascada de operaciones de 2 entradas: $$\begin{align*}
>     \uparrow(a,b,c) &\neq (a \uparrow b) \uparrow c \qquad \text{y} \qquad \uparrow(a,b,c) \neq a \uparrow (b \uparrow c) \\
>     \downarrow(a,b,c) &\neq (a \downarrow b) \downarrow c \qquad \text{y} \qquad \downarrow(a,b,c) \neq a \downarrow (b \downarrow c)
> \end{align*}$$

**Demostración:**

::: proof
*Demostración.* Para la NAND de 3 entradas tenemos, por definición y
leyes de De Morgan:
$$\uparrow(a,b,c) \triangleq \neg(a \wedge b \wedge c) = \neg a \vee \neg b \vee \neg c$$
Sin embargo, la agrupación de dos en dos evaluada anteriormente daba:
$$(a \uparrow b) \uparrow c = (a \wedge b) \vee \neg c$$ Evidentemente,
$\neg a \vee \neg b \vee \neg c \neq (a \wedge b) \vee \neg c.$ Lo mismo
aplica a las agrupaciones derechas y a las operaciones NOR
equivalentes. ◻
:::

> **Teorema (Extensión del Principio de Dualidad (NAND y
> NOR)):**[]{#dualidad_nand_nor label="dualidad_nand_nor"} La inclusión
> de los operadores derivados expande el Principio de Dualidad
> establecido en los postulados iniciales. La expresión dual de
> cualquier teorema o identidad que contenga operaciones NAND o NOR se
> obtiene intercambiando los operadores $\uparrow$ y $\downarrow$
> (además de los ya conocidos $\vee \leftrightarrow \wedge$ y
> $\bot \leftrightarrow \top$).

### Comportamiento de los Operadores XOR y XNOR

A diferencia de los operadores NAND y NOR, que destacan por su
universalidad funcional pero carecen de propiedades algebraicas
deseables (como asociatividad o elemento neutro), los operadores XOR
($\oplus$) y XNOR ($\odot$) exhiben una rica estructura algebraica. A
continuación demostraremos estas propiedades.

> **Teorema (Conmutatividad):**[]{#conmut_xor label="conmut_xor"} Ambos
> operadores son conmutativos:
> $$a \oplus b = b \oplus a \qquad \text{y} \qquad a \odot b = b \odot a$$

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

> **Teorema (Elementos Neutros e Inversores):**[]{#neutro_xor
> label="neutro_xor"} El elemento $\bot$ actúa como neutro para la XOR,
> y $\top$ actúa como inversor. De manera dual, $\top$ es el neutro de
> la XNOR, y $\bot$ actúa como inversor: $$\begin{align*}
>     a \oplus \bot &= a & a \oplus \top &= \neg a \\
>     a \odot \top &= a & a \odot \bot &= \neg a
> \end{align*}$$

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

> **Teorema (Elemento Inverso de sí mismo (Grupo
> Abeliano)):**[]{#idemp_nula_xor label="idemp_nula_xor"} La combinación
> de un elemento consigo mismo produce una anulación (devuelve el neutro
> de la operación correspondiente), actuando cada elemento como su
> propio inverso:
> $$a \oplus a = \bot \qquad \text{y} \qquad a \odot a = \top$$

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

> **Teorema (Propiedades de Negación):**[]{#negacion_xor
> label="negacion_xor"} Negar cualquiera de las entradas de forma
> independiente equivale a negar la operación completa, lo que a su vez
> alterna entre XOR y XNOR: $$\begin{align*}
>     \neg (a \oplus b) &= \neg a \oplus b = a \oplus \neg b = a \odot b \\
>     \neg (a \odot b) &= \neg a \odot b = a \odot \neg b = a \oplus b
> \end{align*}$$

**Demostración:**

::: proof
*Demostración de $a \oplus \neg b = \neg(a \oplus b)$.* $$\begin{align*}
    a \oplus \neg b &\triangleq (a \wedge \neg(\neg b)) \vee (\neg a \wedge \neg b) \\
                    &= (a \wedge b) \vee (\neg a \wedge \neg b) & (Involucion) \\
                    &\triangleq a \odot b & (\text{Definición de XNOR})
\end{align*}$$ Sabiendo por definición que
$a \odot b \triangleq \neg(a \oplus b),$ se concluye de forma inmediata
que $a \oplus \neg b = \neg (a \oplus b).$ ◻
:::

> **Teorema (Asociatividad):**[]{#asoc_xor label="asoc_xor"} Tanto XOR
> como XNOR son operadores algebraicamente asociativos:
> $$(a \oplus b) \oplus c = a \oplus (b \oplus c) \qquad \text{y} \qquad (a \odot b) \odot c = a \odot (b \odot c)$$

**Demostración:**

::: proof
*Demostración para XOR.* Primero evaluaremos el miembro izquierdo
$(a \oplus b) \oplus c.$ Llamaremos $X = a \oplus b.$ $$\begin{align*}
    X \oplus c &\triangleq (X \wedge \neg c) \vee (\neg X \wedge c) \\
               &= \big( ((a \wedge \neg b) \vee (\neg a \wedge b)) \wedge \neg c \big) \vee \big( \neg ((a \wedge \neg b) \vee (\neg a \wedge b)) \wedge c \big) \\
               &= \big( ((a \wedge \neg b) \vee (\neg a \wedge b)) \wedge \neg c \big) \vee \big( (a \odot b) \wedge c \big) \quad (\text{Definición de XNOR}) \\
               &= \big( (a \wedge \neg b \wedge \neg c) \vee (\neg a \wedge b \wedge \neg c) \big) \vee \big( ((a \wedge b) \vee (\neg a \wedge \neg b)) \wedge c \big) \quad (Dist_\wedge) \\
               &= (a \wedge \neg b \wedge \neg c) \vee (\neg a \wedge b \wedge \neg c) \\
               &\quad \vee (a \wedge b \wedge c) \vee (\neg a \wedge \neg b \wedge c) \quad (Dist_\wedge)
\end{align*}$$ Ahora evaluaremos el miembro derecho
$a \oplus (b \oplus c).$ Llamaremos $Y = b \oplus c.$ $$\begin{align*}
    a \oplus Y &\triangleq (a \wedge \neg Y) \vee (\neg a \wedge Y) \\
               &= (a \wedge (b \odot c)) \vee (\neg a \wedge ((b \wedge \neg c) \vee (\neg b \wedge c))) \\
               &= (a \wedge ((b \wedge c) \vee (\neg b \wedge \neg c))) \vee (\neg a \wedge b \wedge \neg c) \vee (\neg a \wedge \neg b \wedge c) \\
               &= (a \wedge b \wedge c) \vee (a \wedge \neg b \wedge \neg c) \\
               &\quad \vee (\neg a \wedge b \wedge \neg c) \vee (\neg a \wedge \neg b \wedge c)
\end{align*}$$ Como podemos observar, ambas expansiones resultan
exactamente en los mismos cuatro minitérminos. Reordenándolos por
conmutatividad ($Comm_\vee$) demostramos que son idénticos. ◻
:::

> **Teorema (Generalización n-aria (XOR y XNOR)):**[]{#gen_xor
> label="gen_xor"} Dado que ambos operadores han demostrado ser
> asociativos y conmutativos, es posible omitir los paréntesis y
> generalizar la operación a un número arbitrario $n$ de variables. Se
> denotan mediante los operadores de sumatoria y productorio
> modificados:
> $$\bigoplus_{i=1}^{n} x_i = x_1 \oplus x_2 \oplus \dots \oplus x_n$$
> $$\bigodot_{i=1}^{n} x_i = x_1 \odot x_2 \odot \dots \odot x_n$$

**Propiedad de Paridad de la XOR (Suma Módulo 2):** La operación
$\bigoplus_{i=1}^{n} x_i$ es conocida matemáticamente como la *función
de paridad impar*. Su valor será $\top$ (o 1) si y solo si un número
impar de las variables de entrada $x_i$ tienen valor $\top.$

**Relación entre XOR y XNOR para $n$ variables:** Dado que
$x \odot y = x \oplus y \oplus \top,$ cada aplicación sucesiva del
operador $\odot$ es matemáticamente equivalente a aplicar una suma
$\oplus$ y concatenar una constante $\top.$ Puesto que la expresión
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

> **Teorema (Distributividad (AND sobre XOR y OR sobre
> XNOR)):**[]{#dist_xor label="dist_xor"} El producto (AND) se
> distribuye sobre la suma exclusiva (XOR), y dualmente, la suma (OR) se
> distribuye sobre la equivalencia (XNOR):
> $$a \wedge (b \oplus c) = (a \wedge b) \oplus (a \wedge c)$$
> $$a \vee (b \odot c) = (a \vee b) \odot (a \vee c)$$

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

> **Teorema (Extensión del Principio de Dualidad (XOR y
> XNOR)):**[]{#dualidad_xor_xnor label="dualidad_xor_xnor"} De forma
> análoga a la relación entre NAND y NOR, los operadores XOR y XNOR son
> mutuamente duales. Para obtener la expresión dual de cualquier
> proposición que involucre estos operadores, se deben intercambiar
> $\oplus$ y $\odot,$ manteniendo las reglas de dualidad estándar para
> los demás elementos y constantes.

## Estructuras Algebraicas Superiores

Las propiedades demostradas anteriormente para los operadores XOR
($\oplus$) y AND ($\wedge$) permiten dotar al conjunto $B$ de
estructuras algebraicas más ricas y estándar dentro del álgebra
abstracta.

> **Teorema (Estructura de Grupo Conmutativo):**[]{#grupo_xor
> label="grupo_xor"} El par $(B, \oplus)$ forma un **grupo abeliano**
> (conmutativo), satisfaciendo:
>
> 1.  **Clausura:** $\forall a,b \in B, a \oplus b \in B.$
>
> 2.  **Asociatividad:**
>     $a \oplus (b \oplus c) = (a \oplus b) \oplus c.$
>
> 3.  **Elemento neutro:** Existe $\bot \in B$ tal que
>     $a \oplus \bot = a.$
>
> 4.  **Elemento inverso (Idempotencia aditiva):** Todo elemento es su
>     propio inverso, ya que $a \oplus a = \bot.$
>
> 5.  **Conmutatividad:** $a \oplus b = b \oplus a.$

> **Teorema (Estructura de Anillo Conmutativo (Anillo
> Booleano)):**[]{#anillo_booleano label="anillo_booleano"} La terna
> $(B, \oplus, \wedge)$ forma un **anillo conmutativo con elemento
> unidad** (comúnmente denominado Anillo Booleano), donde el XOR actúa
> como la suma del anillo y el AND como el producto. Se satisfacen todas
> las propiedades requeridas:
>
> 1.  $(B, \oplus)$ es un grupo abeliano (demostrado arriba).
>
> 2.  $(B, \wedge)$ es un monoide conmutativo (asociativo, conmutativo,
>     y con elemento neutro $\top$).
>
> 3.  **Distributividad:** El producto ($\wedge$) se distribuye sobre la
>     suma ($\oplus$), es decir,
>     $a \wedge (b \oplus c) = (a \wedge b) \oplus (a \wedge c).$

# Instanciación en Álgebras Finitas: Trivial y Bivaluada

La teoría desarrollada en los capítulos anteriores es aplicable a
cualquier álgebra de Boole, sin importar el número de elementos que
contenga el conjunto $B$ (siempre que se cumplan los postulados de
Huntington). Sin embargo, existen dos álgebras finitas de interés
particular por su extrema simplicidad y su aplicación directa en la
teoría de circuitos.

### Álgebra Trivial ($|B| = 1$)

Si definimos el conjunto soporte con un único elemento, $B = \{ c \},$
nos encontramos ante el álgebra de Boole trivial o degenerada.

Dado que los postulados de Huntington (Postulado 2) exigen la existencia
de un elemento neutro para la disyunción ($\bot \in B$) y otro para la
conjunción ($\top \in B$), y puesto que el conjunto solo contiene un
único elemento, estos deben forzosamente coincidir: $$\bot = \top = c$$

Al instanciar cualquier operación definida sobre este conjunto, los
resultados siempre evalúan a dicha constante $c.$

- **Negación:** Por el postulado del complemento, $c \vee \neg c = c$ y
  $c \wedge \neg c = c,$ lo que implica que $\neg c = c.$

- **Disyunción y Conjunción:** Por la propiedad de idempotencia,
  $c \vee c = c$ y $c \wedge c = c.$

- **Operadores Derivados:** Por definición,
  $c \uparrow c = \neg (c \wedge c) = \neg c = c.$ Lo mismo sucede con
  el resto de operadores.

Visualizar esto en tablas de operación (comúnmente conocidas como tablas
de verdad) resulta en estructuras degeneradas de una sola celda, donde
$\circ \in \{ \vee, \wedge, \uparrow, \downarrow, \oplus, \odot \}:$

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

#### Operaciones Básicas ($\neg,$ $\vee,$ $\wedge$)

**1. Negación (Operación unaria $\neg$)**\
El Postulado 5 (Complemento) exige que:
$$\bot \vee \neg \bot = \top \quad \text{y} \quad \top \vee \neg \top = \top$$
Al existir solo dos elementos en el conjunto, el único valor que sumado
a $\bot$ (que es el neutro disyuntivo, por lo que no altera el
resultado) da $\top,$ es el propio $\top.$ Por lo tanto, deducimos que
$\neg \bot = \top.$ De igual manera, por dualidad, $\neg \top = \bot.$

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
$a \downarrow b = \neg(a \vee b),$ los resultados consisten simplemente
en aplicar el operador complemento ($\neg$) a las tablas de conjunción y
disyunción calculadas previamente.

**2. XOR y XNOR**\
Recordando la definición algebraica
$a \oplus b = (a \wedge \neg b) \vee (\neg a \wedge b),$ se puede
evaluar caso por caso (por ejemplo,
$\top \oplus \bot = (\top \wedge \top) \vee (\bot \wedge \bot) = \top \vee \bot = \top$),
pero también podemos usar directamente los teoremas derivados
anteriormente:

- $a \oplus \bot = a$ (Elemento neutro). Por lo tanto:
  $\bot \oplus \bot = \bot,$ y $\top \oplus \bot = \top.$

- $a \oplus \top = \neg a$ (Inversor). Por lo tanto:
  $\bot \oplus \top = \top,$ y $\top \oplus \top = \bot.$

Por dualidad, y sabiendo que el XNOR es la negación del XOR, se obtiene
trivialmente que $a \odot b = \neg(a \oplus b).$

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
$\mathbb{B}_2 = \{0, 1\}.$

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
  mediante el operador suma $\mathbf{+}.$ En circuitos lógicos,
  implementa la puerta **OR**.

- **Ínfimo (Meet / Conjunción):** La operación $\wedge$ se denotará
  mediante el operador producto $\mathbf{\cdot}$ (frecuentemente
  omitido, escribiendo $ab$ en lugar de $a \cdot b$). Implementa la
  puerta **AND**.

- **Complemento (Negación):** La operación de complemento $\neg a$ se
  denotará convencionalmente colocando una barra superior sobre la
  variable, $\mathbf{\overline{a}},$ o mediante una comilla
  $\mathbf{a'}.$ Implementa la puerta **NOT** (inversor).

- **Operadores Derivados (NAND y NOR):** Las operaciones $\uparrow$ y
  $\downarrow$ mantienen sus símbolos, o bien se expresan directamente
  como el complemento del producto o de la suma ($\overline{a \cdot b},$
  $\overline{a+b}$). Representan las puertas universales **NAND** y
  **NOR**, fundamentales en el diseño de circuitos integrados.

- **Suma Exclusiva y Equivalencia (XOR y XNOR):** Las operaciones
  introducidas como suma exclusiva y equivalencia lógica se denotan
  mediante $\mathbf{\oplus}$ y $\mathbf{\odot}.$ Representan las puertas
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
como $a \cdot (b + c) = (a \cdot b) + (a \cdot c),$ y las leyes de De
Morgan cobran su célebre forma visual:
$$\overline{a + b} = \overline{a} \cdot \overline{b} \qquad \text{y} \qquad \overline{a \cdot b} = \overline{a} + \overline{b}$$
De igual modo, la estructura de las operaciones derivadas queda plasmada
directamente en ecuaciones como
$a \oplus b = (a \cdot \overline{b}) + (\overline{a} \cdot b).$

Además, gracias a nuestra previa instanciación en el álgebra bivaluada
($|B|=2$), sabemos que las tablas de operación algebraicas que hemos
deducido analíticamente se corresponden de manera idéntica y biunívoca
con las **tablas de verdad** de las puertas lógicas físicas.

Con estos fundamentos matemáticos sólidamente establecidos, la
transición hacia el diseño, análisis y simplificación de circuitos
digitales queda completamente justificada y carente de ambigüedades.

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
(0,0) node\[american and port\] (myand_ansi) (myand_ansi.in 1)
node\[anchor=east\] $a$ (myand_ansi.in 2) node\[anchor=east\] $b$
(myand_ansi.out) node\[anchor=west\] $a \cdot b$; at (0, -1.5) Símbolo
ANSI;

(5,0) node\[european and port\] (myand_ieee) (myand_ieee.in 1)
node\[anchor=east\] $a$ (myand_ieee.in 2) node\[anchor=east\] $b$
(myand_ieee.out) node\[anchor=west\] $a \cdot b$; at (5, -1.5) Símbolo
IEEE/IEC;
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
  $0 < 1,$ la puerta AND siempre devuelve el valor más pequeño de todas
  sus entradas. La única manera de que la salida escape del $0$ y sea
  $1$ (nivel alto) es que absolutamente todas las entradas sean $1.$

- **Como Interruptor de Señal (Enmascaramiento):** Si fijamos la entrada
  $b=0,$ la salida se fuerza a $0,$ cortando el paso de cualquier rastro
  de datos en $a.$ Si $b=1,$ la puerta \"se abre\" de forma transparente
  y la señal de datos $a$ fluye intacta hacia la salida
  ($a \cdot 1 = a$).

- **Como Producto Aritmético:** A nivel de bit, coincide algebraicamente
  con la multiplicación tradicional: $0 \times 0 = 0,$ $0 \times 1 = 0,$
  $1 \times 1 = 1.$

**Generalización a $n$ variables:** Una puerta AND de $n$ entradas
($\prod_{i=1}^n x_i$) sigue comportándose como un estricto detector de
*unanimidad*. Da $1$ única y exclusivamente si las $n$ entradas son $1.$
Con que un solo eslabón falle y valga $0,$ toda la cadena colapsa a $0.$

## La Puerta OR (Disyunción Lógica)

La operación suma $a + b$ se materializa físicamente en la puerta lógica
**OR**.

:::: center
::: circuitikz
(0,0) node\[american or port\] (myor_ansi) (myor_ansi.in 1)
node\[anchor=east\] $a$ (myor_ansi.in 2) node\[anchor=east\] $b$
(myor_ansi.out) node\[anchor=west\] $a + b$; at (0, -1.5) Símbolo ANSI;

(5,0) node\[european or port\] (myor_ieee) (myor_ieee.in 1)
node\[anchor=east\] $a$ (myor_ieee.in 2) node\[anchor=east\] $b$
(myor_ieee.out) node\[anchor=west\] $a + b$; at (5, -1.5) Símbolo
IEEE/IEC;
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
  de sus pines para que la salida se erija inmediatamente como $1.$

- **Como Interruptor de Forzado a $1:$** Si fijamos la entrada de
  control $b=1,$ la salida se queda anclada permanentemente a $1,$
  independientemente de las fluctuaciones de $a.$ Si $b=0,$ la puerta
  ignora el nivel de control y deja fluir la señal $a$ inalterada
  ($a + 0 = a$).

**Generalización a $n$ variables:** Una puerta OR de $n$ entradas
($\sum_{i=1}^n x_i$) actúa como un detector ultrasensible al nivel alto.
Escanea $n$ líneas de entrada buscando energía; al menor atisbo de un
único $1,$ su salida se dispara a $1.$ Solo mantendrá el $0$ si existe
unanimidad absoluta de ceros.

## La Puerta XOR (Suma Exclusiva)

La operación de disyunción exclusiva $a \oplus b$ es matemáticamente una
de las más ricas del álgebra, materializada en la puerta **XOR**.

:::: center
::: circuitikz
(0,0) node\[american xor port\] (myxor_ansi) (myxor_ansi.in 1)
node\[anchor=east\] $a$ (myxor_ansi.in 2) node\[anchor=east\] $b$
(myxor_ansi.out) node\[anchor=west\] $a \oplus b$; at (0, -1.5) Símbolo
ANSI;

(5,0) node\[european xor port\] (myxor_ieee) (myxor_ieee.in 1)
node\[anchor=east\] $a$ (myxor_ieee.in 2) node\[anchor=east\] $b$
(myxor_ieee.out) node\[anchor=west\] $a \oplus b$; at (5, -1.5) Símbolo
IEEE/IEC;
:::
::::

- **Como Inversor Controlado:** Esta es su aplicación práctica más
  elegante. Si la entrada de control es $0,$ la señal de datos pasa
  inalterada ($a \oplus 0 = a$). Pero si la entrada de control es $1,$
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
5\...), la salida arrojará un $1.$ Si el recuento arroja un número par
de unos (0, 2, 4\...), la salida arrojará $0.$

## La Puerta XNOR (Equivalencia)

La negación sistemática del XOR es el $a \odot b,$ que implementa en
hardware la puerta **XNOR**.

:::: center
::: circuitikz
(0,0) node\[american xnor port\] (myxnor_ansi) (myxnor_ansi.in 1)
node\[anchor=east\] $a$ (myxnor_ansi.in 2) node\[anchor=east\] $b$
(myxnor_ansi.out) node\[anchor=west\] $a \odot b$; at (0, -1.5) Símbolo
ANSI;

(5,0) node\[european xnor port\] (myxnor_ieee) (myxnor_ieee.in 1)
node\[anchor=east\] $a$ (myxnor_ieee.in 2) node\[anchor=east\] $b$
(myxnor_ieee.out) node\[anchor=west\] $a \odot b$; at (5, -1.5) Símbolo
IEEE/IEC;
:::
::::

- **Como Detector de Igualdad ($==$ o $\iff$):** Se dispara a $1$ única
  y exclusivamente si ambas entradas alcanzan idéntico nivel (ambas $0$
  o ambas $1$). Este simple mecanismo fundamenta toda la arquitectura de
  comparadores dentro de las Unidades Aritmético-Lógicas (ALUs) de los
  microprocesadores modernos.

**Generalización a $n$ variables:** El modelo relacional de \"todos
iguales\" fracasa de estrépito al generalizar a
$\bigodot_{i=1}^{n} x_i.$ Conectando con los teoremas previos, la
versión generalizada del XNOR sigue estando maniatada al cálculo de
paridades subyacente. Su naturaleza dependerá del cardinal $n:$ si $n$
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
consecuente $B.$ Esto se refleja en el inversor que inyecta
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
una línea central de decisión que actúa como timón ($S,$ de Selección).
De acuerdo al valor de $S,$ deja que solo uno de los dos flujos
atraviese el bloque para alcanzar la salida maestra $Y.$

Algebraicamente, esculpimos esta selectividad combinando la habilidad de
\"interruptor de señal\" de dos puertas AND, y unificando el tráfico en
un canal común con una puerta OR tolerante:
$$Y = (\overline{S} \cdot D_0) + (S \cdot D_1)$$ *Despliegue mental del
diseño:* Si forzamos la señal a $S=0,$ el brazo derecho de la ecuación
queda bloqueado (multiplicado por $0$) abortando a $D_1.$
Simultáneamente, el brazo izquierdo ve el $0$ invertido, abriendo de par
en par la puerta para que viaje la señal de $D_0.$ Si cambiamos el timón
a $S=1,$ la ruta de $D_0$ colapsa y el torrente de $D_1$ encuentra paso
libre.

### El Demultiplexor (DEMUX)

Despliega la táctica geométricamente inversa. Atrapa un único flujo
torrencial de datos $D$ y tiene el mandato de derivarlo hacia la ruta
$Y_0$ o hacia la ruta de escape $Y_1,$ de nuevo basándose en la orden
ejecutiva $S.$ $$\begin{align*}
Y_0 &= \overline{S} \cdot D \\
Y_1 &= S \cdot D
\end{align*}$$ *Despliegue mental del diseño:* Si dictamos $S=0,$ la
válvula $Y_1$ se clausura en $0,$ y el flujo $D$ atraviesa impertérrito
la válvula $Y_0.$ Si comandamos $S=1,$ la situación se transpone
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
consta de los siguientes cinco postulados sobre una clase $K:$

> **Teorema (Postulados de Sheffer (1913) - Operador
> NAND):**[]{#sheffer_nand label="sheffer_nand"}
>
> 1.  Existen al menos dos elementos distintos en $K.$
>
> 2.  Clausura: Para cualesquiera $a, b \in K,$ el resultado de
>     $a \uparrow b$ también pertenece a $K.$
>
> 3.  $(a \uparrow a) \uparrow (a \uparrow a) = a$
>
> 4.  $a \uparrow (b \uparrow (b \uparrow b)) = a \uparrow a$
>
> 5.  $(a \uparrow (b \uparrow c)) \uparrow (a \uparrow (b \uparrow c)) = ((b \uparrow b) \uparrow a) \uparrow ((c \uparrow c) \uparrow a)$

Es directo demostrar que los axiomas de Huntington implican estos cinco
postulados:

::: proof
*Proof.* Los postulados 1 y 2 son inmediatos y se asumen de base,
garantizando la existencia de los elementos y la definición del operador
binario.

Para demostrar el postulado 3, usamos la equivalencia
$x \uparrow x = \neg x:$ $$\begin{align*}
(a \uparrow a) \uparrow (a \uparrow a) &= \neg a \uparrow \neg a & \text{Definición de } \uparrow \\
&= \neg (\neg a) & \text{Definición de } \uparrow \\
&= a & \text{Involución (Doble Negación)}
\end{align*}$$

Para el postulado 4, partimos del lado izquierdo sabiendo que
$x \uparrow 1 = \neg x:$ $$\begin{align*}
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
$\downarrow.$

> **Teorema (Postulados de Sheffer Duales - Operador
> NOR):**[]{#sheffer_nor label="sheffer_nor"}
>
> 1.  Existen al menos dos elementos distintos en $K.$
>
> 2.  Clausura: Para cualesquiera $a, b \in K,$ el resultado de
>     $a \downarrow b$ pertenece a $K.$
>
> 3.  $(a \downarrow a) \downarrow (a \downarrow a) = a$
>
> 4.  $a \downarrow (b \downarrow (b \downarrow b)) = a \downarrow a$
>
> 5.  $(a \downarrow (b \downarrow c)) \downarrow (a \downarrow (b \downarrow c)) = ((b \downarrow b) \downarrow a) \downarrow ((c \downarrow c) \downarrow a)$

::: proof
*Proof.* La demostración sigue un patrón idéntico de dualidad. El
postulado 3 se demuestra recordando que $x \downarrow x = \neg x:$
$$\begin{align*}
(a \downarrow a) \downarrow (a \downarrow a) &= \neg a \downarrow \neg a = \neg (\neg a) = a
\end{align*}$$

En el postulado 4, sabiendo que $x \downarrow 0 = \neg x,$ el término
interior $b \downarrow (b \downarrow b)$ se evalúa a $\bot,$ y por
tanto: $$\begin{align*}
a \downarrow (b \downarrow (b \downarrow b)) &= a \downarrow (b \downarrow \neg b) = a \downarrow \neg (b \vee \neg b) = a \downarrow \neg (\top) = a \downarrow \bot \\
&= \neg (a \vee \bot) = \neg a = a \downarrow a
\end{align*}$$

Para el postulado 5, el proceso dual lleva ambos lados de la ecuación a
la forma idéntica $a \vee (\neg b \wedge \neg c).$ ◻
:::

## Equivalencia Inversa: Sheffer implica Huntington

Para demostrar que el sistema de Sheffer es estrictamente equivalente al
sistema algebraico de Huntington, debemos recorrer el camino inverso:
asumiendo como ciertas *únicamente* las cinco propiedades del operador
$\uparrow$ (NAND), debemos construir los operadores $\neg, \vee, \wedge$
y derivar algebraicamente todos los postulados de Huntington originales.

### Definición de las operaciones fundamentales

Definimos los operadores clásicos en base estricta al operador
$\uparrow:$

- **Negación:** $\neg a \triangleq a \uparrow a$

- **Disyunción:**
  $a \vee b \triangleq (a \uparrow a) \uparrow (b \uparrow b)$

- **Conjunción:**
  $a \wedge b \triangleq (a \uparrow b) \uparrow (a \uparrow b)$

El desarrollo formal completo exige demostrar primeramente una serie de
lemas a partir de los Postulados 3, 4 y 5 de Sheffer.

> **Teorema (Lema 1: Involución Doble Negación):**[]{#sheffer_inv
> label="sheffer_inv"} $\forall a \in K, \neg(\neg a) = a$

::: proof
*Proof.* Utilizando nuestra definición de negación
($\neg x = x \uparrow x$): $$\begin{align*}
\neg(\neg a) &= (\neg a) \uparrow (\neg a) & \text{Definición de } \neg \\
&= (a \uparrow a) \uparrow (a \uparrow a) & \text{Sustituyendo } \neg a \\
&= a & \text{Por el Postulado 3 de Sheffer explícitamente}
\end{align*}$$ ◻
:::

> **Teorema (Lema 2: Conmutatividad del Operador
> NAND):**[]{#sheffer_conmut label="sheffer_conmut"}
> $\forall a,b \in K, a \uparrow b = b \uparrow a$

::: proof
*Proof.* El Postulado 5 de Sheffer establece una simetría fundamental
que permite, tras varias sustituciones algebraicas con el Postulado 4
(identidad), aislar los términos para probar la conmutatividad estricta
de la barra de Sheffer. Este paso (cuya extensión algebraica omitimos
por ser un resultado canónico de Sheffer (1913)) garantiza la simetría
de las operaciones derivadas. ◻
:::

### Demostración de los Axiomas de Huntington

> **Teorema (Conmutatividad (Huntington 3)):**[]{#hunt_conmut_sheffer
> label="hunt_conmut_sheffer"} $a \vee b = b \vee a$ y
> $a \wedge b = b \wedge a.$

::: proof
*Proof.* Para la disyunción, apoyándonos en el Lema 2: $$\begin{align*}
a \vee b &= (a \uparrow a) \uparrow (b \uparrow b) & \text{Definición de } \vee \\
&= (b \uparrow b) \uparrow (a \uparrow a) & \text{Lema 2 (Conmutatividad de } \uparrow\text{)} \\
&= b \vee a & \text{Definición de } \vee
\end{align*}$$ Para la conjunción: $$\begin{align*}
a \wedge b &= (a \uparrow b) \uparrow (a \uparrow b) & \text{Definición de } \wedge \\
&= (b \uparrow a) \uparrow (b \uparrow a) & \text{Lema 2 (Conmutatividad de } \uparrow\text{)} \\
&= b \wedge a & \text{Definición de } \wedge
\end{align*}$$ ◻
:::

> **Teorema (Axioma del Complementario (Huntington
> 5)):**[]{#hunt_comp_sheffer label="hunt_comp_sheffer"} Se cumple que
> $a \vee \neg a = \top$ y $a \wedge \neg a = \bot.$

::: proof
*Proof.* El álgebra de Sheffer carece inicialmente de constantes. Estas
emergen dinámicamente como invariantes algebraicos. Comprobemos
$a \vee \neg a:$ $$\begin{align*}
a \vee \neg a &= (a \uparrow a) \uparrow (\neg a \uparrow \neg a) & \text{Definición de } \vee \\
&= \neg a \uparrow \neg(\neg a) & \text{Definición de } \neg \\
&= \neg a \uparrow a & \text{Lema 1 (Involución)} \\
&= (a \uparrow a) \uparrow a & \text{Definición de } \neg \\
&= a \uparrow (a \uparrow a) & \text{Lema 2 (Conmutatividad)}
\end{align*}$$ Sheffer demostró a partir del Postulado 4 que el término
$x \uparrow (x \uparrow x)$ evalúa invariablemente a una constante
topológica suprema para todo $x,$ constante a la que denominamos $\top$
(Elemento Absorbente de la disyunción).

Por dualidad constructiva en la conjunción: $$\begin{align*}
a \wedge \neg a &= (a \uparrow \neg a) \uparrow (a \uparrow \neg a) & \text{Definición de } \wedge \\
&= (a \uparrow (a \uparrow a)) \uparrow (a \uparrow (a \uparrow a)) & \text{Definición de } \neg \\
&= \top \uparrow \top & \text{Por la invariante hallada arriba} \\
&= \neg \top = \bot & \text{Lo que se define como la constante } \bot
\end{align*}$$ ◻
:::

> **Teorema (Distributividad y Elementos
> Neutros):**[]{#hunt_dist_sheffer label="hunt_dist_sheffer"} Quedan
> demostrados formalmente los postulados de Distributividad y Elemento
> Neutro mediante expansión iterativa de la conmutatividad y sustitución
> del Postulado 5.

::: proof
*Proof.* La demostración del axioma de distributividad
($a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$) en el sistema
de Sheffer requiere desarrollar la parte derecha mediante más de treinta
expansiones sucesivas empleando el Lema 1 y el Postulado 5. Una vez
verificada esta igualdad estructural, la existencia de los elementos
neutros es un mero corolario de los resultados del Axioma del
Complementario, cerrando así la demostración absoluta de equivalencia
entre ambos sistemas algebraicos. ◻
:::

# Estructura de Anillo y Cuerpo Booleano

## Anillos Booleanos

Un álgebra de Boole puede ser interpretada desde la perspectiva del
álgebra abstracta clásica como un tipo especial de anillo. Para ello,
nos apoyamos en los operadores derivados introducidos anteriormente, en
particular la operación O-exclusiva (XOR, $\oplus$) y la conjunción
(AND, $\wedge$).

> **Definicion (Anillo Booleano):**[]{#def_anillo_booleano_cap
> label="def_anillo_booleano_cap"} Un anillo booleano es un anillo
> conmutativo con elemento unidad $(R, +, \cdot, 0_R, 1_R)$ en el cual
> todo elemento es idempotente respecto a la multiplicación:
> $$\forall x \in R, x \cdot x = x$$

A partir de esta aparente simplicidad (la idempotencia de todos sus
elementos), emergen propiedades estructurales muy rígidas que limitan la
forma de estos anillos.

> **Teorema (Característica 2):**[]{#caracteristica_dos
> label="caracteristica_dos"} Todo anillo booleano tiene característica
> 2, es decir, $\forall x \in R, x + x = 0_R.$ Todo elemento es su
> propio inverso aditivo.

::: proof
*Proof.* Consideremos el elemento $(x+x)$ y apliquemos la idempotencia:
$$\begin{align*}
(x + x) &= (x + x) \cdot (x + x) \\
x + x &= x^2 + x^2 + x^2 + x^2 \\
x + x &= x + x + x + x \\
0_R &= x + x
\end{align*}$$ Por tanto, al restar $x$ en ambos lados obtenemos
$x = -x.$ ◻
:::

> **Teorema (Conmutatividad estricta):**[]{#conmutatividad_estricta
> label="conmutatividad_estricta"} Todo anillo booleano es
> obligatoriamente conmutativo ($x \cdot y = y \cdot x$).

::: proof
*Proof.* Evaluando el elemento $(x+y)$ al cuadrado: $$\begin{align*}
x + y &= (x + y)^2 \\
x + y &= x^2 + xy + yx + y^2 \\
x + y &= x + xy + yx + y \\
0_R &= xy + yx \\
xy &= -yx
\end{align*}$$ Como acabamos de demostrar que el anillo tiene
característica 2 (cada elemento es su propio inverso aditivo), sabemos
que $-yx = yx,$ luego $xy = yx.$ ◻
:::

## Funtores de Equivalencia Estructural

Existe una equivalencia estructural perfecta (un isomorfismo de
categorías) entre las Álgebras de Boole y los Anillos Booleanos.

### De Álgebra de Boole a Anillo Booleano

Dada un Álgebra de Boole $(\mathbb{B}, \vee, \wedge, \neg, \bot, \top),$
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

Inversamente, dado un Anillo Booleano $(R, +, \cdot, 0_R, 1_R),$ podemos
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

> **Teorema (El único Cuerpo Booleano es
> $\mathbb{F}_2$):**[]{#cuerpo_booleano label="cuerpo_booleano"} Un
> anillo booleano es un cuerpo matemático si y solo si contiene
> exactamente dos elementos.

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
estas dos condiciones para cualquier $x:$
$$x = 0_R \quad \text{o} \quad (x - 1_R) = 0_R \implies x = 1_R$$ En
consecuencia, el conjunto de elementos del anillo $R$ solo puede estar
formado por $\{0_R, 1_R\}.$ ◻
:::

Esta demostración es crucial para nuestro propósito arquitectónico de
los sistemas digitales. Nos indica de manera absoluta que si queremos
construir espacios vectoriales utilizando operaciones lógicas (que
requeriremos para los códigos correctores de errores), **el único
álgebra de Boole que puede actuar como cuerpo de escalares es el álgebra
bivaluada $\mathbb{B}_2$**, la cual es algebraicamente isomorfa al
cuerpo de Galois $\mathbb{F}_2.$

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
$\mathbb{B}.$

> **Definicion (Conjunto Parcialmente Ordenado (Poset)):**[]{#poset
> label="poset"} Un conjunto $P$ equipado con una relación binaria $\le$
> es un conjunto parcialmente ordenado (poset) si la relación satisface
> los siguientes axiomas para todo $a, b, c \in P:$
>
> 1.  **Reflexividad**: $a \le a.$
>
> 2.  **Antisimetría**: Si $a \le b$ y $b \le a,$ entonces $a = b.$
>
> 3.  **Transitividad**: Si $a \le b$ y $b \le c,$ entonces $a \le c.$

En este contexto, escribiremos $a \ge b$ como sinónimo estricto de
$b \le a,$ y $a < b$ si $a \le b$ pero $a \ne b.$

## Ínfimo y Supremo

Dado un poset $(P, \le),$ consideremos un par de elementos $a, b \in P.$

- Un elemento $u \in P$ es una **cota superior** de $\{a, b\}$ si
  $a \le u$ y $b \le u.$ El **supremo** de $a$ y $b,$ denotado como
  $a \sqcup b,$ es la menor de todas sus cotas superiores (si existe).

- Un elemento $l \in P$ es una **cota inferior** de $\{a, b\}$ si
  $l \le a$ y $l \le b.$ El **ínfimo** de $a$ y $b,$ denotado como
  $a \sqcap b,$ es la mayor de todas sus cotas inferiores (si existe).

> **Definicion (Retículo (Lattice)):**[]{#reticulo label="reticulo"} Un
> **retículo** es un conjunto parcialmente ordenado en el cual todo par
> de elementos tiene un supremo ($a \sqcup b$) y un ínfimo
> ($a \sqcap b$) definidos y únicos dentro del conjunto.

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
debe poseer tres propiedades restrictivas adicionales. Analizaremos cada
una de ellas de forma formal:

> **Definicion (Retículo Acotado):**[]{#reticulo_acotado
> label="reticulo_acotado"} Un retículo $(L, \le)$ es un **retículo
> acotado** si posee un elemento universal máximo (denotado como $\top$
> o $1$) y un elemento universal mínimo (denotado como $\bot$ o $0$). Es
> decir, existe $\top, \bot \in L$ tal que para todo $x \in L:$
> $$\bot \le x \le \top$$

En un retículo acotado, para cualquier elemento $x,$ se cumple de forma
natural que $x \sqcap \bot = \bot,$ $x \sqcup \top = \top,$
$x \sqcup \bot = x$ y $x \sqcap \top = x.$

> **Definicion (Retículo Distributivo (y
> Bidistributivo)):**[]{#reticulo_distributivo
> label="reticulo_distributivo"} Un retículo es **distributivo** si la
> operación de ínfimo distribuye sobre la operación de supremo. Es
> decir, para cualesquiera $a,b,c \in L:$
> $$a \sqcap (b \sqcup c) = (a \sqcap b) \sqcup (a \sqcap c)$$

En la teoría de retículos se demuestra que, de cumplirse esta
distributividad, entonces obligatoriamente se cumple también la dual (el
supremo distribuye sobre el ínfimo), por lo que todo retículo
distributivo es estructuralmente **bidistributivo**:
$a \sqcup (b \sqcap c) = (a \sqcup b) \sqcap (a \sqcup c).$

> **Definicion (Retículo Complementado):**[]{#reticulo_complementado
> label="reticulo_complementado"} Un retículo acotado es un **retículo
> complementado** si, para todo elemento $a \in L,$ existe al menos un
> elemento $b \in L$ (denominado complemento de $a,$ y a menudo escrito
> como $\neg a$) tal que:
> $$a \sqcup b = \top \qquad \text{y} \qquad a \sqcap b = \bot$$

Si un retículo es distributivo, se puede demostrar algebraicamente que,
si un elemento posee complemento, dicho complemento es absolutamente
**único**. Esta combinación de las tres propiedades descritas da lugar a
la estructura fundamental que nos ocupa:

> **Teorema (Axiomas del Retículo
> Booleano):**[]{#axiomas_reticulo_booleano
> label="axiomas_reticulo_booleano"} Un retículo $(L, \le)$ es isomorfo
> a un Álgebra de Boole si y solo si es a la vez un retículo
> **acotado**, **distributivo** y **complementado**. A esta
> superestructura se la conoce matemáticamente como *Retículo Booleano*.

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

# Álgebra de Zhegalkin (Polinomios Booleanos) {#capitulo:zhegalkin}

A lo largo de los capítulos previos hemos estudiado sistemas axiomáticos
fundamentados en las tríadas $\{\vee, \wedge, \neg\}$ (Huntington) y en
monádicas como $\{\uparrow\}$ y $\{\downarrow\}$ (Sheffer y Peirce).
Existe, sin embargo, una formulación alternativa que conecta de forma
directa la lógica matemática con la teoría de anillos abstractos y la
criptografía moderna: la axiomatización basada en la **disyunción
exclusiva (XOR, $\oplus$)** y la **conjunción (AND, $\wedge$)**,
formulada por el matemático ruso Ivan Zhegalkin en 1927.

## El Sistema de Zhegalkin: XOR y AND

En la estructura de Zhegalkin, un álgebra de Boole se define sobre un
conjunto $K$ dotado de dos constantes $\{0, 1\}$ y las operaciones
binarias $\oplus$ y $\wedge$ (frecuentemente denotada simplemente como
multiplicación $\cdot$).

Los postulados fundamentales que definen este sistema algebraico (y que
coinciden con la definición de un Anillo Booleano conmutativo unitario)
son los siguientes:

> **Teorema (Postulados del Sistema de
> Zhegalkin):**[]{#zhegalkin_postulados label="zhegalkin_postulados"}
>
> 1.  **Asociatividad:**
>     $$a \oplus (b \oplus c) = (a \oplus b) \oplus c \qquad \text{y} \qquad a \cdot (b \cdot c) = (a \cdot b) \cdot c$$
>
> 2.  **Conmutatividad:**
>     $$a \oplus b = b \oplus a \qquad \text{y} \qquad a \cdot b = b \cdot a$$
>
> 3.  **Elementos Neutros:**
>     $$a \oplus 0 = a \qquad \text{y} \qquad a \cdot 1 = a$$
>
> 4.  **Idempotencia multiplicativa y Nulidad aditiva:**
>     $$a \cdot a = a \qquad \text{y} \qquad a \oplus a = 0$$
>
> 5.  **Distributividad (AND sobre XOR):**
>     $$a \cdot (b \oplus c) = (a \cdot b) \oplus (a \cdot c)$$

Nótese una diferencia radical con el álgebra de Huntington: en el
sistema de Zhegalkin **no existe dualidad simétrica**. La operación AND
distribuye sobre la operación XOR (postulado 5), pero la operación XOR
**no** distribuye sobre la operación AND. Además, la constante $0$ es
absorbente para el AND ($a \cdot 0 = 0$), pero la constante $1$ no lo es
para el XOR ($a \oplus 1 = \neg a \neq 1$).

### Equivalencia con el Álgebra de Huntington

Para demostrar que este sistema genera un álgebra de Boole completa,
basta con definir los operadores clásicos a partir de las herramientas
de Zhegalkin:

- **Negación:** $\neg a \triangleq a \oplus 1$

- **Disyunción (OR):**
  $a \vee b \triangleq a \oplus b \oplus (a \cdot b)$

Demostremos algebraicamente que esta definición de OR cumple el Axioma
del Complementario ($a \vee \neg a = 1$): $$\begin{align*}
a \vee \neg a &= a \oplus (\neg a) \oplus (a \cdot \neg a) & \text{Definición de } \vee \\
&= a \oplus (a \oplus 1) \oplus (a \cdot (a \oplus 1)) & \text{Definición de } \neg \\
&= (a \oplus a) \oplus 1 \oplus (a \cdot a \oplus a \cdot 1) & \text{Asociatividad y Distributividad} \\
&= 0 \oplus 1 \oplus (a \oplus a) & \text{Nulidad, Idempotencia y Neutro} \\
&= 1 \oplus 0 = 1 & \text{Nulidad y Conmutatividad}
\end{align*}$$

## El Sistema Dual: XNOR y OR

Aplicando el Principio de Dualidad lógico al sistema de Zhegalkin,
obtenemos un sistema equivalente que reposa sobre la equivalencia o
co-disyunción exclusiva (**XNOR, $\odot$**) y la disyunción clásica
(**OR, $+$**).

> **Teorema (Postulados Duales (Sistema XNOR /
> OR)):**[]{#xnor_or_postulados label="xnor_or_postulados"} Sustituyendo
> $\oplus$ por $\odot,$ $\cdot$ por $+,$ y permutando $0$ con $1:$
>
> 1.  **Asociatividad:**
>     $$a \odot (b \odot c) = (a \odot b) \odot c \qquad \text{y} \qquad a + (b + c) = (a + b) + c$$
>
> 2.  **Conmutatividad:**
>     $$a \odot b = b \odot a \qquad \text{y} \qquad a + b = b + a$$
>
> 3.  **Elementos Neutros:**
>     $$a \odot 1 = a \qquad \text{y} \qquad a + 0 = a$$
>
> 4.  **Idempotencia aditiva y Unidad de equivalencia:**
>     $$a + a = a \qquad \text{y} \qquad a \odot a = 1$$
>
> 5.  **Distributividad (OR sobre XNOR):**
>     $$a + (b \odot c) = (a + b) \odot (a + c)$$

En este sistema, podemos recuperar la lógica clásica definiendo la
negación y la conjunción:

- **Negación:** $\neg a \triangleq a \odot 0$

- **Conjunción (AND):** $a \wedge b \triangleq a \odot b \odot (a + b)$

## Polinomios de Reed-Muller

Una de las aplicaciones más profundas del Álgebra de Zhegalkin es el
teorema de que **toda función booleana** puede expresarse de forma única
como un polinomio multivariable utilizando exclusivamente XOR y AND, sin
negaciones previas. A esta forma canónica se le denomina Polinomio de
Zhegalkin o forma canónica de **Reed-Muller**.

Para una función de $n$ variables, el polinomio consta de la suma XOR
($\oplus$) de constantes y productos de variables no negadas:
$$f(x_1, x_2, \dots, x_n) = a_0 \oplus (a_1 x_1 \oplus a_2 x_2 \dots) \oplus (a_{12} x_1 x_2 \oplus \dots) \oplus \dots \oplus (a_{12\dots n} x_1 x_2 \dots x_n)$$
donde cada coeficiente $a_i \in \{0, 1\}.$ La ausencia matemática de
negaciones y la tratabilidad matricial de esta forma algebraica la
convierten en la base teórica de los códigos de detección y corrección
de errores en sistemas de telecomunicación.

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

> **Definicion (Átomos):**[]{#atomos label="atomos"} Un elemento
> $x \in \mathbb{B}$ se denomina **átomo** si es un elemento
> estrictamente positivo, $x \ne \bot,$ y no existe ningún elemento
> intermedio entre él y el $\bot.$ Formalmente:
> $$\mathit{atom}(x) \iff (x > \bot) \wedge \left( \forall y \in \mathbb{B}, \bot < y \le x \implies y = x \right)$$

En términos puramente algebraicos, un átomo $x$ es aquel cuyo producto
(ínfimo) con cualquier otro elemento $y \in \mathbb{B}$ es el
aniquilador total o bien él mismo (absorbente total):
$$\mathit{atom}(x) \iff (x \ne \bot) \wedge \left( \forall y \in \mathbb{B}, (x \wedge y = \bot) \vee (x \wedge y = x) \right)$$
El conjunto de todos los átomos de un álgebra de Boole se denota como
$\mathit{Atom}(\mathbb{B}).$ Una propiedad inmediata es que el ínfimo de
dos átomos distintos es siempre nulo:
$$\forall a, b \in \mathit{Atom}(\mathbb{B}), a \ne b \implies a \wedge b = \bot$$

> **Definicion (Hiperátomos (Co-átomos)):**[]{#hiperatomos
> label="hiperatomos"} De forma dual, un **hiperátomo** o **co-átomo**
> es un elemento estrictamente inferior a $\top$ tal que no existe
> ningún elemento intermedio entre él y el máximo.
> $$\mathit{hatom}(x) \iff (x < \top) \wedge \left( \forall y \in \mathbb{B}, x \le y < \top \implies y = x \right)$$

En cualquier álgebra finita no trivial (donde $\top \ne \bot$), los
conjuntos $\mathit{Atom}(\mathbb{B})$ e $\mathit{Hatom}(\mathbb{B})$
nunca están vacíos.

## El Teorema de Representación de Stone (Caso Finito)

Si tomamos el conjunto de todos los átomos $\mathit{Atom}(\mathbb{B}),$
podemos generar el conjunto potencia $\wp(\mathit{Atom}(\mathbb{B})),$
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

> **Teorema (Representación de Álgebras de Boole
> Finitas):**[]{#rep_stone label="rep_stone"} Toda álgebra de Boole
> finita $\mathbb{B}$ es algebraicamente isomorfa al álgebra del
> conjunto potencia de sus átomos. Es decir, la función $\varphi$ es una
> biyección perfecta:
> $$\mathbb{B} \simeq \wp(\mathit{Atom}(\mathbb{B}))$$

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

> **Teorema (Cardinalidad de un Álgebra Finita):**[]{#cardinalidad
> label="cardinalidad"} Si un álgebra de Boole es finita, su número
> total de elementos debe ser, forzosamente, una potencia de 2.
> $$|\mathbb{B}| = 2^n \quad \text{donde} \quad n = |\mathit{Atom}(\mathbb{B})|$$

Cualquier conjunto que no tenga exactamente $2, 4, 8, 16, \ldots$
elementos **jamás podrá** constituir un álgebra de Boole, sin importar
qué operaciones intentemos definir sobre él. Y aún más importante: todas
las álgebras de Boole finitas que tengan el mismo número de elementos
son exactamente la misma álgebra (son algebraicamente isomorfas). Solo
hay *un* álgebra de Boole de 2 elementos, *una* de 4 elementos, *una* de
8 elementos, etc.

## Generalización a Álgebras Infinitas

En el caso de las álgebras de Boole infinitas, el Teorema de
Representación que acabamos de ver no se cumple de forma incondicional.
Como comprobamos en el primer capítulo con los modelos matemáticos, en
el infinito la topología puede volverse mucho más exótica.

Para que un álgebra infinita sea isomorfa al conjunto potencia de sus
átomos, debe poseer dos propiedades estructurales estrictas:

1.  **Ser atómica:** Todo elemento no nulo de $\mathbb{B}$ debe estar
    acotado inferiormente por al menos un átomo.

2.  **Ser completa:** Todo subconjunto (incluso infinito) de elementos
    debe poseer un supremo y un ínfimo que pertenezcan obligatoriamente
    al álgebra.

> **Teorema (Isomorfismo de Álgebras Atómicas y
> Completas):**[]{#rep_stone_infinito label="rep_stone_infinito"}
> Cualquier álgebra de Boole $\mathbb{B}$ que sea simultáneamente
> completa y atómica es isomorfa al álgebra del conjunto potencia de sus
> átomos: $$\mathbb{B} \simeq \wp(\mathit{Atom}(\mathbb{B}))$$

Si falla alguna de estas dos propiedades, el isomorfismo se rompe.
Podemos revisitar los modelos topológicos de cardinalidad $\aleph_0$
para ilustrar este fenómeno:

- El **Ejemplo 9** (la familia de subintervalos racionales) es un
  álgebra infinita que carece por completo de átomos. Puesto que
  cualquier subintervalo racional siempre puede subdividirse en dos más
  pequeños, no existe el \"ladrillo indivisible\".

- El **Ejemplo 10** (los subconjuntos finitos y cofinitos de
  $\mathbb{N}$) *sí* es un álgebra atómica (cuyos átomos son los
  conjuntos unitarios $\{n\}$). Sin embargo, *no* es completa. Si
  reuniésemos una infinidad de estos átomos (por ejemplo, los números
  pares), su supremo lógico sería el conjunto de todos los pares, pero
  dicho conjunto no es finito ni cofinito y, por ende, no pertenece al
  álgebra. Al no ser completa, esta álgebra no es isomorfa al conjunto
  potencia $\wp(\mathbb{N}).$

Esta diversidad matemática infinita es fascinante, pero en la
electrónica digital nos da luz verde para restringir nuestros esfuerzos
puramente al caso finito y bivaluado. Sabemos de antemano que, bajo
limitaciones finitas, cualquier álgebra de Boole es idéntica al espacio
vectorial $n$-dimensional $\mathbb{B}_2^n,$ un tema que exploraremos a
fondo en el siguiente capítulo.

# Espacios Vectoriales Booleanos y Códigos de Hamming

## El Espacio Vectorial Binario $\mathbb{B}^n$

En el Capítulo 6b demostramos que, si bien cualquier álgebra de Boole
puede ser interpretada como un anillo, el **único** álgebra de Boole que
tiene la estructura rigurosa de un **Cuerpo Matemático** (es decir,
carente de divisores de cero y donde todo elemento no nulo tiene inverso
multiplicativo) es el álgebra bivaluada $\mathbb{B}_2 = \{0, 1\}.$
Algebraicamente, este cuerpo es exactamente el cuerpo de Galois
$\mathbb{F}_2.$

Dado que la condición insoslayable para construir un espacio vectorial
lineal es operar sobre un cuerpo de escalares, deducimos que los únicos
espacios vectoriales puramente booleanos que pueden existir deben tener
como conjunto base a $\mathbb{F}_2.$

> **Definicion (El Espacio Vectorial $\mathbb{B}^n$):**[]{#espacio_bn
> label="espacio_bn"} Se define el espacio vectorial booleano
> $\mathbb{B}^n$ como el conjunto de todas las $n$-tuplas (vectores de
> $n$ bits) cuyos elementos pertenecen a $\mathbb{F}_2.$ Las dos
> operaciones que dotan al conjunto de estructura de espacio vectorial
> son:
>
> 1.  **Suma vectorial:** Se define como la operación XOR ($\oplus$)
>     aplicada bit a bit entre dos vectores.
>     $$\vec{u} \oplus \vec{v} = (u_1 \oplus v_1, u_2 \oplus v_2, \ldots, u_n \oplus v_n)$$
>
> 2.  **Producto por escalar:** Se define como la operación AND
>     ($\wedge$) entre un escalar booleano $k \in \mathbb{F}_2$ y cada
>     elemento del vector.
>     $$k \wedge \vec{v} = (k \wedge v_1, k \wedge v_2, \ldots, k \wedge v_n)$$

Al operar sobre $\mathbb{F}_2,$ este espacio vectorial hereda
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

> **Definicion (Función Distancia (Métrica)):**[]{#metrica
> label="metrica"} Dado un conjunto $X,$ una **métrica** o **función
> distancia** sobre $X$ es una función $d: X \times X \to \mathbb{R}$
> que, para cualesquiera $x, y, z \in X,$ satisface las siguientes
> cuatro propiedades:
>
> 1.  **No negatividad:** $d(x, y) \ge 0.$
>
> 2.  **Identidad de los indiscernibles:** $d(x, y) = 0 \iff x = y.$
>
> 3.  **Simetría:** $d(x, y) = d(y, x).$
>
> 4.  **Desigualdad triangular:** $d(x, z) \le d(x, y) + d(y, z).$

> **Definicion (Peso de Hamming):**[]{#peso_hamming
> label="peso_hamming"} El **peso de Hamming** de un vector
> $\vec{v} \in \mathbb{B}^n,$ denotado como $w(\vec{v}),$ es el número
> de componentes no nulas (número de unos) que contiene. En términos
> formales, si $\vec{v} = (v_1, v_2, \dots, v_n),$ entonces:
> $$w(\vec{v}) = \sum_{i=1}^n v_i$$ donde la suma se entiende en la
> aritmética ordinaria de $\mathbb{R}.$

> **Definicion (Distancia de Hamming):**[]{#distancia_hamming
> label="distancia_hamming"} La **distancia de Hamming** entre dos
> vectores $\vec{u}, \vec{v} \in \mathbb{B}^n,$ denotada como
> $d(\vec{u}, \vec{v}),$ es el número de posiciones en las que difieren.
> Operacionalmente, coincide con el peso de Hamming de su suma vectorial
> en $\mathbb{B}^n:$ $$d(\vec{u}, \vec{v}) = w(\vec{u} \oplus \vec{v})$$

> **Teorema (La Distancia de Hamming es una
> Métrica):**[]{#hamming_metrica label="hamming_metrica"} La función
> $d(\vec{u}, \vec{v}) = w(\vec{u} \oplus \vec{v})$ cumple todas las
> propiedades matemáticas de una métrica sobre el espacio
> $\mathbb{B}^n.$

::: proof
*Proof.* Debemos verificar el cumplimiento de las cuatro propiedades
definitorias para cualesquiera vectores
$\vec{u}, \vec{v}, \vec{z} \in \mathbb{B}^n:$

1.  **No negatividad:** Dado que el peso de Hamming $w(\vec{x})$ cuenta
    el número de bits a $1$ en un vector, es una suma de números enteros
    no negativos, por lo que $w(\vec{u} \oplus \vec{v}) \ge 0.$ Por
    definición, $d(\vec{u}, \vec{v}) \ge 0.$

2.  **Identidad de los indiscernibles:**
    $$d(\vec{u}, \vec{v}) = 0 \iff w(\vec{u} \oplus \vec{v}) = 0$$ El
    peso de un vector es cero si y solo si todos sus componentes son
    cero, es decir, $\vec{u} \oplus \vec{v} = \vec{0}.$ En el espacio
    booleano, dos elementos suman cero (vía XOR) si y solo si son
    idénticos, por tanto $\vec{u} = \vec{v}.$

3.  **Simetría:** Por la conmutatividad intrínseca de la operación XOR
    en el cuerpo $\mathbb{F}_2:$
    $$d(\vec{u}, \vec{v}) = w(\vec{u} \oplus \vec{v}) = w(\vec{v} \oplus \vec{u}) = d(\vec{v}, \vec{u})$$

4.  **Desigualdad triangular:** Demostraremos que
    $d(\vec{u}, \vec{z}) \le d(\vec{u}, \vec{v}) + d(\vec{v}, \vec{z})$
    mediante dos enfoques distintos.

    *Enfoque A (Algebraico a través del peso):* Primero, observemos una
    propiedad fundamental del peso respecto a la suma vectorial: un bit
    en $\vec{a} \oplus \vec{b}$ solo es $1$ si los bits correspondientes
    en $\vec{a}$ y $\vec{b}$ son distintos. Por tanto, los $1$s en
    $\vec{a} \oplus \vec{b}$ provienen como máximo de la unión de los
    $1$s presentes en $\vec{a}$ y en $\vec{b}.$ Esto implica que
    $w(\vec{a} \oplus \vec{b}) \le w(\vec{a}) + w(\vec{b}).$ Si tomamos
    $\vec{a} = \vec{u} \oplus \vec{v}$ y
    $\vec{b} = \vec{v} \oplus \vec{z},$ obtenemos:
    $$w((\vec{u} \oplus \vec{v}) \oplus (\vec{v} \oplus \vec{z})) \le w(\vec{u} \oplus \vec{v}) + w(\vec{v} \oplus \vec{z})$$
    Aplicando asociatividad y el hecho de que
    $\vec{v} \oplus \vec{v} = \vec{0},$ el lado izquierdo se simplifica
    a $w(\vec{u} \oplus \vec{z}).$ Sustituyendo la definición de
    distancia:
    $$d(\vec{u}, \vec{z}) \le d(\vec{u}, \vec{v}) + d(\vec{v}, \vec{z})$$

    *Enfoque B (Componente a componente):* Analicemos una única
    coordenada $i$ cualquiera. Las posibles combinaciones de valores
    $(u_i, v_i, z_i) \in \{0, 1\}^3$ y su contribución a la distancia
    (donde la contribución a $d(\vec{x}, \vec{y})_i$ es
    $x_i \oplus y_i$) son:

    - Si $u_i = z_i,$ entonces $d(\vec{u}, \vec{z})_i = 0.$ Como la suma
      $d(\vec{u}, \vec{v})_i + d(\vec{v}, \vec{z})_i$ solo contiene
      valores no negativos (0 o 1), la desigualdad
      $0 \le d(\vec{u}, \vec{v})_i + d(\vec{v}, \vec{z})_i$ se cumple
      trivialmente independientemente del valor de $v_i.$

    - Si $u_i \ne z_i,$ entonces $d(\vec{u}, \vec{z})_i = 1.$ En este
      caso, el valor intermedio $v_i$ debe ser igual a $u_i$ o igual a
      $z_i$ (ya que solo hay dos estados posibles en $\mathbb{F}_2$).

      - Si $v_i = u_i \ne z_i,$ entonces $d(\vec{u}, \vec{v})_i = 0$ y
        $d(\vec{v}, \vec{z})_i = 1,$ cuya suma es $1.$

      - Si $v_i = z_i \ne u_i,$ entonces $d(\vec{u}, \vec{v})_i = 1$ y
        $d(\vec{v}, \vec{z})_i = 0,$ cuya suma es $1.$

      En ambos sub-casos obtenemos $1 \le 1,$ verificándose la
      desigualdad para la coordenada $i.$

    Dado que la distancia total es la suma de las contribuciones de las
    $n$ componentes, y la desigualdad se sostiene componente a
    componente, la desigualdad triangular global queda demostrada.

 ◻
:::

> **Teorema (Invarianza Traslacional de la
> Distancia):**[]{#inv_traslacional label="inv_traslacional"} La
> distancia de Hamming es invariante bajo traslaciones. Es decir, sumar
> un mismo vector $\vec{w}$ a dos vectores dados no altera la distancia
> entre ellos:
> $$d(\vec{u} \oplus \vec{w}, \vec{v} \oplus \vec{w}) = d(\vec{u}, \vec{v})$$

::: proof
*Proof.* Partimos de la definición de distancia aplicada a los vectores
trasladados:
$$d(\vec{u} \oplus \vec{w}, \vec{v} \oplus \vec{w}) = w((\vec{u} \oplus \vec{w}) \oplus (\vec{v} \oplus \vec{w}))$$
Por las propiedades de asociatividad y conmutatividad de la operación
suma en nuestro espacio vectorial, podemos reordenar los términos:
$$= w(\vec{u} \oplus \vec{v} \oplus (\vec{w} \oplus \vec{w}))$$ Sabemos
que cualquier vector sumado consigo mismo resulta en el vector nulo
($\vec{w} \oplus \vec{w} = \vec{0}$) en un espacio de característica
$2.$ Así:
$$= w(\vec{u} \oplus \vec{v} \oplus \vec{0}) = w(\vec{u} \oplus \vec{v}) = d(\vec{u}, \vec{v})$$ ◻
:::

> **Teorema (Acotación de la Distancia en
> $\mathbb{B}^n$):**[]{#cota_hamming label="cota_hamming"} En el espacio
> vectorial bivaluado de dimensión finita $\mathbb{B}^n,$ la distancia
> de Hamming entre cualquier par de vectores está acotada estrictamente
> superior e inferiormente: $$0 \le d(\vec{u}, \vec{v}) \le n$$

::: proof
*Proof.* Por la propia definición axiomática de la métrica que hemos
comprobado previamente, el límite inferior $d(\vec{u}, \vec{v}) \ge 0$
es trivial (no negatividad).

Para el límite superior, consideremos la definición
$d(\vec{u}, \vec{v}) = w(\vec{u} \oplus \vec{v}).$ El peso de Hamming de
un vector cuenta el número de posiciones no nulas. Puesto que los
vectores en $\mathbb{B}^n$ están formados por exactamente $n$
componentes (es decir, tienen dimensión $n$), el número máximo de
componentes que pueden ser distintas de cero (y por tanto, el número
máximo de posiciones en las que $\vec{u}$ y $\vec{v}$ difieren) es el
número total de componentes del vector, que es $n.$

En el caso extremo en el que los vectores difieren en todos los bits
(siendo uno el complemento bit a bit del otro,
$\vec{v} = \neg \vec{u}$), obtenemos:
$$d(\vec{u}, \neg \vec{u}) = w(\vec{u} \oplus \neg \vec{u}) = w(\vec{1}) = n$$
Por tanto, la distancia jamás puede exceder la dimensión $n$ del
espacio. ◻
:::

## Códigos de Corrección de Errores (Hamming)

La aplicación más brillante de dotar a las cadenas de bits de una
estructura de espacio vectorial sobre $\mathbb{F}_2$ es la invención de
los **códigos correctores de errores**.

En un canal de comunicación ruidoso, un vector $\vec{v}$ enviado puede
sufrir corrupciones (cambios de 0 a 1 o viceversa), recibiéndose un
vector diferente $\vec{r}.$ Richard Hamming propuso solucionar esto no
usando todo el espacio vectorial $\mathbb{B}^n,$ sino limitando los
mensajes válidos a un subespacio vectorial más pequeño y controlado.

### El Subespacio Código y la Matriz de Paridad

Un código lineal por bloques de longitud $n$ y dimensión $k$ se define
matemáticamente como un **subespacio vectorial**
$C \subset \mathbb{B}^n$ de dimensión $k.$ Todo subespacio vectorial
puede definirse como el núcleo (kernel) de una transformación lineal,
representada por una matriz llamada **Matriz de Paridad ($H$)** de
dimensiones $(n-k) \times n.$

> **Teorema (Validación del Síndrome):**[]{#sindrome_hamming
> label="sindrome_hamming"} Un vector recibido $\vec{r}$ es una palabra
> código válida (pertenece al subespacio código $C$) si y solo si su
> producto por la matriz de paridad $H$ (utilizando aritmética en
> $\mathbb{F}_2$) da como resultado el vector nulo. A este resultado se
> le denomina **síndrome** ($\vec{s}$). $$\vec{s} = H \cdot \vec{r}^T$$
> Si $\vec{s} = \vec{0},$ el vector pertenece al subespacio (no hay
> errores detectados). Si $\vec{s} \ne \vec{0},$ el vector ha salido del
> subespacio, lo que indica que se ha corrompido durante la transmisión.

Dado que operar matrices sobre $\mathbb{F}_2$ requiere únicamente
puertas lógicas XOR y AND, el cálculo del síndrome
$\vec{s} = H \cdot \vec{r}^T$ se puede implementar directamente en
hardware digital con una eficiencia extrema, constituyendo la base de
los modernos sistemas de memoria ECC (Error-Correcting Code).

# Funciones booleanas

## Estudio de las funciones booleanas sobre álgebras de Boole finitas

Estudiaremos sólo las funciones $f: B^{n} \rightarrow B$ dónde
$B = B_{2} = \{0, 1\}.$ Esto es $f: B_{2}^{n} \rightarrow B_{2}.$

### Formas normales

Toda función $f: B_{2}^{n} \rightarrow B_{2}$ se puede poner en la
forma:
$$f(x_{1}, x_{2}, \dots, x_{n}) = \sum_{k=1}^{m < 2^{n}} \prod_{l=1}^{n} x_{l}$$

### Número de funciones posibles

En general, el número de funciones de un conjunto $C$ de cardinal
$n_{C} \in \mathbb{N}$ en un conjunto $D$ de cardinal
$n_{D} \in \mathbb{N}$ será $n_{D}^{n_{C}}.$ Así, una función de $n$
variables en $C$ con valores en $D$ será $n_{D}^{(n_{C}^{n})}.$ Para el
caso en que $C = D = B_{2}$ que toma como argumento $n$ variables,
obtenemos que el número de funciones será de $2^{(2^{n})}.$

En la siguiente tabla vemos cómo crece esta cantidad:

  **N variables**   **Longitud tabla ($2^N$)**   **Número de funciones distintas: $2^{(2^{N})}$**
  ----------------- ---------------------------- --------------------------------------------------
  0                 1                            2
  1                 2                            4
  2                 4                            16
  3                 8                            256
  4                 16                           65536
  5                 32                           4294967296
  6                 64                           18446744073709551616
  7                 128                          340282366920938463463374607431768211456

## Demostración por Inducción del número de funciones

El punto anterior es fácil de probar:

1.  Para el caso de $N = 0$ y de $N = 1$ es fácil probar (por
    enumeración) la validez de la fórmula. Más tarde mostraremos tablas
    de todas las funciones hasta $N = 2$ inclusive.

2.  Para el caso general, la Hipótesis de Inducción (HI) será:
    $$[\mathrm{HI}] \quad \forall N \in (\mathbb{N} \cup \{0\}), \ 0 \leq N \leq n - 1 \implies 2^{(2^{N})} \text{ es el cardinal buscado.}$$

3.  Veremos si para el caso $N = n$ se sigue cumpliendo la fórmula
    anterior. Pero esto es claro: al añadir una variable en el argumento
    tendremos todas las funciones del caso $N = n - 1$ ($2^{n - 1}$)
    para el valor $0$ de la nueva variable y otros $2^{n - 1}$ para el
    valor $1$ de la nueva variable, y no quedan otros casos. Las
    funciones totales para $N = n$ serán:
    $$\mathrm{card} \left( \left\{ f: B_{2}^{n - 1} \rightarrow B_{2} \right\} \times \left\{ f: B_{2}^{n - 1} \rightarrow B_{2} \right\} \right) =$$
    $$= \mathrm{card} \left( \left\{ f: B_{2}^{n - 1} \rightarrow B_{2} \right\} \right) \cdot \mathrm{card} \left( \left\{ f: B_{2}^{n - 1} \rightarrow B_{2} \right\} \right) =$$
    $$= 2^{(2^{n - 1})} \cdot 2^{(2^{n - 1})} = 2^{(2^{n - 1} + 2^{n - 1})} = 2^{2 \cdot (2^{n - 1})} = 2^{(2^{n})}$$

Y así queda establecida la fórmula.

## Minitérminos y Maxitérminos

Como se ve en el punto anterior, el crecimiento es desmesurado al
compararlo al crecimiento lineal de los argumentos. En un futuro, cuando
intentemos hacer reducciones de expresiones booleanas, este crecimiento
nos impedirá construir métodos eficaces para resolver las
minimizaciones.

Aunque hemos visto que podemos poner las expresiones booleanas en los
conjuntos de operadores
$\{ \{+, \overline{\quad}\}, \{\cdot, \overline{\quad}\}, \{\uparrow\}, \{\downarrow\}, \{\oplus, \cdot\}, \{\odot, +\} \},$
por comprensibilidad y para una lectura normal se utilizan
frecuentemente los dos primeros conjuntos unidos, pudiendo variarse bien
el orden de los operadores binarios:
$\{ \{+, \cdot, \overline{\quad}\}, \{\cdot, +, \overline{\quad}\} \}.$

El primer conjunto $\{+, \cdot, \overline{\quad}\}$ será el que
estudiemos por defecto, el segundo se tratará con una simetría de
dualidad (hay que tener algunos cuidados). El conjunto elegido de
operaciones se llamará desarrollo en sumas de productos de términos
simples (una variable, o su negada, o una constante). También se llamará
desarrollo por minitérminos o SOP (inglés) o SdP. El segundo será el
desarrollo en producto de sumas de términos simples. También se llamará
desarrollo por maxitérminos o POS (inglés) o PdS.

### Desarrollo por minitérminos

En el desarrollo por minitérminos expresamos sólo los términos de la
expresión en que la función tiene como valor $1.$ Veamos:

$$f_{B_{2}}(x_{1}, x_{2}, \dots, x_{n}) = \sum_{(i_{1}, i_{2}, \dots, i_{n}) = (0, \dots, 0)}^{(1, \dots, 1)} \left( \sigma_{1}^{(i_{1}, i_{2}, \dots, i_{n})}(i_{1}) \cdot \sigma_{2}^{(i_{1}, i_{2}, \dots, i_{n})}(i_{2}) \cdot \dots \cdot \sigma_{n}^{(i_{1}, i_{2}, \dots, i_{n})}(i_{n}) \right)$$

dónde
$\sigma_{k}^{(i_{1}, i_{2}, \dots, i_{n})}(i_{k}) \in \{i_{k}, \overline{i_{k}}\}$
y $0 \leq k \leq n.$

Para más sencillez:

$$f_{B_{2}}(x) = f_{B_{2}}(x_{1}, x_{2}, \dots, x_{n}) = \sum_{\iota \in B_{2}^{n}} \left( \sigma_{1}^{\iota}(\iota_{1}) \cdot \sigma_{2}^{\iota}(\iota_{2}) \cdot \dots \cdot \sigma_{n}^{\iota}(\iota_{n}) \cdot f_{B_{2}}(\iota) \right) = \sum_{\iota \in B_{2}^{n}} (\sigma^{\iota} \cdot f_{B_{2}}(\iota))$$
dónde
$\sigma_{k}^{\iota}(\iota_{k}) \in \{\iota_{k}, \overline{\iota_{k}}\},$
$0 \leq k \leq n$ y $\sigma^{\iota}$ es un minitérmino.

Cuándo la sigma (el minitérmino) es en todos los casos (para todas las
iotas) completo (es un producto de $n$-términos simples), el valor de la
función en esa iota concreta indica si el minitérmino aparece o no.

### Desarrollo por maxitérminos

En el desarrollo por maxitérminos de una función de $n$ variables, los
maxitérminos son sumatorios de $n$-términos simples. Así termina
consistiendo la función en un producto de maxitérminos. Los maxitérminos
indican un $0$ de la función.

> **Teorema (Universalidad de las Formas Canónicas (Expansión de
> Shannon)):**[]{#shannon_expansion label="shannon_expansion"} Toda
> función booleana $f: \mathbb{B}^n \to \mathbb{B}$ puede expresarse de
> manera única (salvo conmutatividad) de dos formas canónicas duales:
>
> 1.  **Suma de Productos (SOP) / Minitérminos:**
>     $f(x_1, \dots, x_n) = \sum_{\iota \in \mathbb{B}^n} f(\iota) \cdot \sigma^\iota$
>
> 2.  **Producto de Sumas (POS) / Maxitérminos:**
>     $f(x_1, \dots, x_n) = \prod_{\iota \in \mathbb{B}^n} (f(\iota) + \Pi^\iota)$
>
> donde $\sigma^\iota$ es el minitérmino (producto en el que todas las
> variables aparecen afirmadas si $\iota_k=1$ o negadas si $\iota_k=0$),
> y $\Pi^\iota$ es el maxitérmino dual.

::: proof
*Proof.* Demostraremos la forma de minitérminos (SOP). Sea
$\vec{x} \in \mathbb{B}^n$ un vector de entrada arbitrario. Por la
construcción de los minitérminos, el término $\sigma^\iota(\vec{x}) = 1$
si y solo si el vector de entrada $\vec{x}$ es exactamente idéntico al
vector constante $\iota.$ Para cualquier otro vector
$\iota' \ne \vec{x},$ se cumple $\sigma^{\iota'}(\vec{x}) = 0.$

Al evaluar la expresión completa
$\sum_{\iota \in \mathbb{B}^n} f(\iota) \cdot \sigma^\iota(\vec{x}),$
todos los sumandos en los que $\iota \ne \vec{x}$ se anulan, ya que
$\sigma^\iota(\vec{x}) = 0 \implies f(\iota) \cdot 0 = 0.$ El único
sumando que sobrevive a la suma (OR) es aquel en el que
$\iota = \vec{x},$ para el cual $\sigma^{\vec{x}}(\vec{x}) = 1.$ Por lo
tanto, la suma se colapsa a: $$f(\vec{x}) \cdot 1 = f(\vec{x})$$ Esto
demuestra que la expresión reproduce exactamente la tabla de verdad de
la función $f.$ La demostración para los maxitérminos (POS) es idéntica
por el Principio de Dualidad, donde $\Pi^\iota(\vec{x}) = 0$ si y solo
si $\vec{x} = \iota,$ colapsando el producto (AND) al valor
$f(\vec{x}) + 0 = f(\vec{x}).$ ◻
:::

### Transformación a Compuertas XOR y AND (Zhegalkin)

Hemos visto en el capítulo dedicado al Sistema de Zhegalkin (ver
Capítulo [11](#capitulo:zhegalkin){reference-type="ref"
reference="capitulo:zhegalkin"}) que el anillo booleano
$\langle \mathbb{B}, \oplus, \cdot \rangle$ forma un conjunto
funcionalmente completo. Surge la pregunta práctica: dada una función
expresada en su forma canónica de minitérminos (con 2 capas lógicas de
AND $\to$ OR), ¿cómo podemos transformarla sistemáticamente a un
circuito equivalente usando exclusivamente puertas XOR y AND?

> **Teorema (Conversión de Minitérminos a Polinomio de
> Zhegalkin):**[]{#minterms_to_zhegalkin label="minterms_to_zhegalkin"}
> Toda expresión canónica en Suma de Productos (SOP) puede transformarse
> directamente en un Polinomio de Zhegalkin (XOR-AND) aplicando dos
> reglas:
>
> 1.  Reemplazar directamente todas las sumas lógicas (OR, $+$) por
>     sumas exclusivas (XOR, $\oplus$).
>
> 2.  Reemplazar cada variable negada $\overline{x_k}$ por
>     $(x_k \oplus 1)$ y aplicar la distributividad del producto sobre
>     la suma exclusiva.

::: proof
*Proof.* Para demostrar la regla 1, recordamos la relación fundamental
entre OR y XOR: $$A + B = A \oplus B \oplus (A \cdot B)$$ En una
expansión canónica por minitérminos, cualquier par de minitérminos
distintos $\sigma^i$ y $\sigma^j$ ($i \ne j$) son **mutuamente
excluyentes**. Esto significa que nunca pueden valer $1$ simultáneamente
para la misma entrada, por lo que su producto lógico es siempre falso:
$\sigma^i \cdot \sigma^j = 0.$ Sustituyendo esto en la relación
anterior, obtenemos:
$$\sigma^i + \sigma^j = \sigma^i \oplus \sigma^j \oplus 0 = \sigma^i \oplus \sigma^j$$
Por inducción, una suma lógica de cualquier cantidad de minitérminos
mutuamente excluyentes es estrictamente equivalente a su suma exclusiva.
Así, la capa OR exterior puede ser sustituida por una capa XOR sin
alterar la función matemática.

Para demostrar la regla 2, sabemos por la definición de la negación en
el Anillo de Zhegalkin que $\overline{x} = x \oplus 1.$ Al realizar esta
sustitución en los literales de cada minitérmino, obtenemos una
expresión que solo contiene multiplicaciones ($\cdot$), sumas exclusivas
($\oplus$) y la constante $1.$ Dado que el operador AND distribuye sobre
el XOR ($A \cdot (B \oplus C) = (A \cdot B) \oplus (A \cdot C)$),
podemos expandir algebraicamente todos los paréntesis para obtener un
polinomio multilineal puro compuesto únicamente por sumas exclusivas de
productos no negados. Este resultado es el Polinomio de Zhegalkin único
de la función. ◻
:::

Además de expresar las funciones por cadenas de símbolos que constituyen
un término, existe una posibilidad de expresar estas funciones por
tablas lineales o por cuadros (tablas bidimensionales). Para cada
combinación de valores booleanos a la entrada de una función obtenemos
un valor booleano de salida.

Para que las funciones booleanas representen algo de interés para la
ingeniería, lo primero que debemos tener es una forma de representar la
información que queremos procesar. ¿Cómo representamos un número?. ¿Cómo
una letra?. Haremos un alto en la exposición de funciones booleanas,
para detallar más esta pregunta, poder responderla y así ver para qué
estamos viendo las álgebras de Boole.

# Minimización de Funciones Booleanas

## El Problema de la Optimización Lógica

En capítulos anteriores hemos estudiado cómo expresar cualquier función
matemática utilizando formas canónicas (minitérminos o maxitérminos).
Sin embargo, la implementación directa en hardware de estas expresiones
canónicas es extremadamente ineficiente. Un minitérmino requiere $n$
entradas para su puerta AND, y la expresión completa puede requerir
cientos de puertas lógicas.

En la ingeniería de hardware computacional, la **optimización** (o
minimización) de expresiones booleanas persigue encontrar una expresión
equivalente a la original que reduzca alguna métrica de coste:

- **Área de silicio:** Minimizar la cantidad total de puertas lógicas y
  el número de entradas de las mismas (fan-in).

- **Latencia (Retardo):** Reducir el número de capas o \"saltos
  lógicos\" que la señal debe atravesar. Las formas SOP minimizadas
  suelen mantener una profundidad de dos capas lógicas constantes,
  garantizando alta velocidad.

- **Consumo de energía:** Menos transistores implican menos
  capacitancias parásitas que cargar y descargar.

Para lograr esto, explotamos sistemáticamente el teorema de la
adyacencia lógica:
$x \cdot y + x \cdot \overline{y} = x \cdot (y + \overline{y}) = x.$ Es
decir, si dos términos del mismo tamaño difieren en el estado de una
sola variable, esta variable es redundante y ambos términos pueden
fusionarse, eliminándola.

## Mapas de Karnaugh

El Mapa de Karnaugh (K-Map) es una representación tabular geométrica
bidimensional de la tabla de verdad de una función, diseñada
específicamente para que las celdas físicamente adyacentes correspondan
a combinaciones de entrada que difieren en un único bit (distancia de
Hamming = 1). Esto se logra ordenando los índices de las filas y
columnas utilizando código Gray.

En el mapa de Karnaugh buscamos agrupar las celdas que contienen unos
lógicos en bloques rectangulares. Las reglas de agrupación son las
siguientes:

1.  Todo agrupamiento debe contener un número de celdas que sea potencia
    de $2$ ($1, 2, 4, 8, \dots$).

2.  Los agrupamientos deben ser lo más grandes posibles (maximizan el
    número de variables eliminadas).

3.  Se permite el solapamiento de agrupamientos (reutilizar celdas,
    gracias a la idempotencia $x+x=x$).

4.  Los bordes del mapa son adyacentes entre sí de forma toroidal (el
    borde superior es adyacente al inferior, el izquierdo al derecho).

5.  Se pueden agrupar los términos indiferentes (*Don't Care*)
    representados con una 'X', si y sólo si ayudan a crear un
    agrupamiento más grande.

### Mapas de 3 y 4 variables

Un mapa de 3 variables ($v_1, v_2, v_3$) posee $8$ celdas, dispuestas
típicamente en $2 \times 4.$ Un mapa de 4 variables
($v_1, v_2, v_3, v_4$) tiene $16$ celdas, dispuestas en $4 \times 4.$

::: center
**Mapa de Karnaugh de 3 variables**\

   $v_1 \setminus v_2v_3$   **00**   **01**   **11**   **10**
  ------------------------ -------- -------- -------- --------
           **0**              1        0        0        1
           **1**              1        1        1        1
:::

Analizando el mapa de 3 variables:

- La fila inferior completa de unos da el implicante $v_1.$

- Las esquinas (00 y 10) de la fila superior se agrupan con las esquinas
  de la inferior formando un grupo de 4 celdas, lo que elimina $v_1$ y
  $v_2,$ resultando en el implicante $\overline{v_3}.$

- La función mínima es $v_1 + \overline{v_3}.$

::: center
**Mapa de Karnaugh de 4 variables**\

   $v_1v_2 \setminus v_3v_4$   **00**   **01**   **11**   **10**
  --------------------------- -------- -------- -------- --------
            **00**               0        1        1        0
            **01**               0        1        1        0
            **11**               1        1        1        1
            **10**               1        0        0        1
:::

Analizando el mapa superior:

- El bloque de 4 unos centrales (columnas 01 y 11, filas 00 y 01) es
  independiente de $v_1$ y $v_4,$ resultando en el implicante
  $\overline{v_1}v_3.$

- La fila completa de unos en 11 (independiente de $v_3, v_4$) da el
  implicante $v_1v_2.$

- Los cuatros unos en las esquinas de la mitad inferior (filas 11 y 10,
  columnas 00 y 10) forman el implicante $v_1\overline{v_4}.$

### Mapas de 5 y 6 variables

Para mapas de más de 4 variables, la dimensión 2D pura deja de ser útil
para representar adyacencias unitarias. Para 5 variables, se utilizan
dos tablas de $4 \times 4$ ubicadas lado a lado. La primera tabla asume
que la variable adicional $v_1 = 0$ y la segunda asume $v_1 = 1.$ Dos
celdas en la misma posición relativa dentro de ambas tablas se
consideran lógicamente adyacentes.

Para 6 variables ($v_1, v_2, v_3, v_4, v_5, v_6$), el método se expande
organizando cuatro mapas de $4 \times 4$ en un esquema de $2 \times 2.$
Cada cuadrante (\"supercelda\") viene determinado por las dos variables
de mayor peso ($v_1, v_2$):

::: center
+:-----------------------------------------------------------------:+:-----------------------------------------------------------------:+
| **Mapa $\overline{v_1}\overline{v_2}$ (00)**                      | **Mapa $\overline{v_1}v_2$ (01)**                                 |
+-------------------------------------------------------------------+-------------------------------------------------------------------+
|    $v_3v_4 \setminus v_5v_6$   **00**   **01**   **11**   **10**  |    $v_3v_4 \setminus v_5v_6$   **00**   **01**   **11**   **10**  |
|   --------------------------- -------- -------- -------- -------- |   --------------------------- -------- -------- -------- -------- |
|             **00**                                                |             **00**                                                |
|             **01**                                                |             **01**                                                |
|             **11**                                                |             **11**                                                |
|             **10**                                                |             **10**                                                |
+-------------------------------------------------------------------+-------------------------------------------------------------------+
|                                                                   |                                                                   |
+-------------------------------------------------------------------+-------------------------------------------------------------------+
| **Mapa $v_1\overline{v_2}$ (10)**                                 | **Mapa $v_1v_2$ (11)**                                            |
+-------------------------------------------------------------------+-------------------------------------------------------------------+
|    $v_3v_4 \setminus v_5v_6$   **00**   **01**   **11**   **10**  |    $v_3v_4 \setminus v_5v_6$   **00**   **01**   **11**   **10**  |
|   --------------------------- -------- -------- -------- -------- |   --------------------------- -------- -------- -------- -------- |
|             **00**                                                |             **00**                                                |
|             **01**                                                |             **01**                                                |
|             **11**                                                |             **11**                                                |
|             **10**                                                |             **10**                                                |
+-------------------------------------------------------------------+-------------------------------------------------------------------+
:::

Para realizar agrupaciones en este formato de 6 variables, las
adyacencias clásicas de K-Map se aplican *dentro* de cada cuadrante de
16 celdas individualmente. Además, existen adyacencias *intercuadrante*:
celdas idénticas superpuestas entre el cuadrante superior izquierdo e
inferior izquierdo, entre superior izquierdo y superior derecho, etc.,
formando un \"hipercubo\". Para agruparlas, la silueta del grupo debe
ser visualmente idéntica en los cuadrantes adyacentes involucrados.

## Algoritmo Sistemático de Quine-McCluskey

El mapa de Karnaugh, si bien es una herramienta visual e intuitiva
sumamente útil para diseñadores, carece de escalabilidad y no es
programable, dependiendo del reconocimiento de patrones ópticos.

El algoritmo de Quine-McCluskey (Q-M) es una solución puramente tabular
y sistemática que garantiza matemáticamente la obtención de todas las
simplificaciones mínimas y que opera, esencialmente, de la siguiente
forma:

### Fase 1: Búsqueda Exhaustiva de Implicantes Primos

1.  Se listan todos los minitérminos (y términos \"Don't Care\") para
    los que la función es 1, agrupados por su peso de Hamming (número de
    1s lógicos en su codificación binaria).

2.  Se compara iterativamente cada término de un grupo de peso $k$
    contra todos los términos del grupo contiguo de peso $k+1.$ Si dos
    términos difieren en exactamente un bit, se genera un nuevo término
    unificado con un guion ('-') en la posición donde diferían,
    representando la variable eliminada.

3.  Se marcan ambos términos \"padre\" como simplificados mediante un
    indicador o tick ($\checkmark$).

4.  Este proceso se repite con las nuevas listas generadas (donde los
    guiones deben coincidir en posición para fusionar dos términos).

5.  Todos los términos que no lograron combinarse (y por lo tanto no
    reciben la marca $\checkmark$) al finalizar todas las rondas
    posibles son etiquetados como **Implicantes Primos**.

### Fase 2: Resolución de la Tabla de Cobertura

La lista resultante de implicantes primos puede tener redundancias.

1.  Se construye una tabla de cobertura, donde las filas son los
    implicantes primos y las columnas son los minitérminos obligatorios
    originales (se excluyen los \"Don't Care\"). Se marca con una \"X\"
    si un implicante primo cubre un minitérmino concreto.

2.  Se buscan columnas que posean **una única \"X\"**. Estas se
    denominan Implicantes Primos **Esenciales**, y forman parte
    irrenunciable del resultado simplificado.

3.  Se seleccionan estas filas, marcando como cubiertos todos los demás
    minitérminos que también abarquen.

4.  Si tras seleccionar los esenciales aún quedan minitérminos por
    cubrir (columnas sin seleccionar), se aplica un proceso de
    dominancia de filas y columnas, o algoritmos de bifurcación (método
    de Petrick) para elegir la cobertura más barata restante.

La expresión final es la suma lógica (OR) de todos los Implicantes
Primos seleccionados para lograr la cobertura completa de los
minitérminos objetivo de la función.

### Ejemplo Práctico de Quine-McCluskey

Consideremos la función de 4 variables definida por los minitérminos
$m(0, 1, 2, 5, 6, 7).$

**Fase 1: Encontrar Implicantes Primos**

::: center
   **Grupo**   **Min.**   **Binario**   $\checkmark$   **Comb. (1a)**   **Binario**   **Comb. (2a)**   **Binario**
  ----------- ---------- ------------- -------------- ---------------- ------------- ---------------- -------------
       0          0          0000       $\checkmark$       (0,1)           000-                       
                                                           (0,2)           00-0                       
       1          1          0001       $\checkmark$       (1,5)           0-01                       
                  2          0010       $\checkmark$       (2,6)           0-10                       
       2          5          0101       $\checkmark$       (5,7)           01-1                       
                  6          0110       $\checkmark$       (6,7)           011-                       
       3          7          0111       $\checkmark$                                                  
:::

Observemos que ninguna de las combinaciones resultantes en la segunda
columna (Comb. 1a) puede combinarse en un siguiente nivel (Comb. 2a)
porque los guiones no coinciden en posición y bits restantes a distancia
1 simultáneamente. Por tanto, todas las agrupaciones de tamaño 2
resultantes (0,1), (0,2), (1,5), (2,6), (5,7) y (6,7) son implicantes
primos.

**Fase 2: Tabla de Cobertura**

::: center
                           **Implicante**                           **0**   **1**   **2**   **5**   **6**   **7**
  ---------------------------------------------------------------- ------- ------- ------- ------- ------- -------
   (0,1) $\rightarrow \overline{v_1}\overline{v_2}\overline{v_3}$     X       X                            
   (0,2) $\rightarrow \overline{v_1}\overline{v_2}\overline{v_4}$     X               X                    
        (1,5) $\rightarrow \overline{v_1}\overline{v_3}v_4$                   X               X            
        (2,6) $\rightarrow \overline{v_1}v_3\overline{v_4}$                           X               X    
              (5,7) $\rightarrow \overline{v_1}v_2v_4$                                        X               X
              (6,7) $\rightarrow \overline{v_1}v_2v_3$                                                X       X
:::

En este ejemplo particular, no hay ninguna columna que posea una única
\"X\" (ningún minitérmino está cubierto por un único implicante primo).
Esto significa que no hay **Implicantes Primos Esenciales**. Debemos
utilizar métodos de selección (como Petrick) o inspección heurística.
Una posible selección mínima de cobertura es tomar (0,1), (2,6) y (5,7).
Otra es (0,2), (1,5) y (6,7). En cualquier caso, la función requiere de
3 términos de 3 literales. Tomando la segunda, el resultado minimizado
es:
$$f = \overline{v_1}\overline{v_2}\overline{v_4} + \overline{v_1}\overline{v_3}v_4 + \overline{v_1}v_2v_3$$

# Circuitos Combinacionales y Aritméticos

## Metodología de Diseño Combinacional

Un circuito digital se denomina **combinacional** si sus salidas en
cualquier instante de tiempo dependen *única y exclusivamente* de los
valores presentes en sus entradas en ese mismo instante.
Matemáticamente, carecen de estado o memoria. Todo circuito
combinacional implementa físicamente una o más funciones booleanas
puras.

El flujo de trabajo clásico para el diseño de estos sistemas sigue un
enfoque *Top-Down*:

1.  **Especificación:** Definición verbal y formal del comportamiento
    deseado del sistema (qué entradas recibe y qué salidas debe
    producir).

2.  **Tabla de verdad:** Captura exhaustiva de las especificaciones
    mapeando cada combinación de $N$ entradas a las salidas requeridas.

3.  **Obtención de Funciones y Minimización:** Extracción de la forma
    canónica y reducción mediante Karnaugh o Quine-McCluskey para
    optimizar el hardware resultante.

4.  **Implementación (Síntesis Lógica):** Traducción de las ecuaciones
    booleanas minimizadas a un diagrama esquemático con compuertas
    lógicas (AND, OR, NOT, XOR, NAND, NOR).

Para evitar diseñar todo desde cero a nivel de puertas lógicas básicas,
la ingeniería agrupa ciertos patrones repetitivos en **bloques
funcionales** o \"macros\" (MSI - Medium Scale Integration). A
continuación, revisamos los fundamentales.

## Multiplexores y Demultiplexores

### Multiplexores (MUX)

Un multiplexor actúa como un conmutador electrónico. Posee $2^n$ líneas
de entrada de datos, $n$ líneas de selección (o control) y $1$ línea de
salida. Dependiendo del código binario presente en las líneas de
selección, el MUX conecta internamente una y solo una de las líneas de
entrada de datos hacia la salida.

La ecuación lógica de un MUX de $4 \to 1$ (2 líneas de selección
$S_1, S_0$ y 4 entradas $D_0 \dots D_3$) es:
$$Y = \overline{S_1}\overline{S_0}D_0 + \overline{S_1}S_0D_1 + S_1\overline{S_0}D_2 + S_1S_0D_3$$

**Aplicación avanzada:** Dado que los términos de selección conforman
explícitamente los minitérminos de las variables $S,$ un MUX de
$2^n \to 1$ puede implementar directamente *cualquier* función booleana
de $n$ variables, simplemente conectando a las entradas de datos ($D_i$)
constantes lógicas (0 o 1) equivalentes a la tabla de verdad de la
función.

### Demultiplexores (DEMUX)

El demultiplexor realiza la función dual: recibe una única entrada de
datos y, en base a $n$ líneas de selección, enruta ese dato a una
específica de entre $2^n$ líneas de salida. (Las líneas no seleccionadas
permanecen inactivas, típicamente en 0 lógico).

## Codificadores y Decodificadores

### Decodificadores

Un decodificador de $n$ a $2^n$ toma un código binario de $n$ bits de
entrada y activa de forma exclusiva una (y solo una) de sus $2^n$
salidas. Básicamente, computa simultáneamente los $2^n$ minitérminos del
alfabeto de entrada. Un uso clásico es la selección de chips en bancos
de memoria.

### Codificadores

Hacen la operación inversa: dadas $2^n$ líneas de entrada, devuelven en
sus $n$ líneas de salida el código binario asociado a la línea de
entrada que está activa. El principal problema del codificador estándar
es la *colisión*: ¿qué ocurre si dos líneas de entrada se activan
simultáneamente? El codificador generará una salida corrupta (el OR
lógico de ambos códigos).

Para solucionar esto, surgieron los **Codificadores con Prioridad
(Priority Encoders)**. Estos circuitos asignan un peso jerárquico a cada
entrada. Si varias entradas están activas simultáneamente, el
codificador devuelve únicamente el código correspondiente a la entrada
con mayor prioridad, ignorando las demás.

## Problemática de la Inversa de una Función

Supongamos un sistema combinacional que calcula una función $f(x) = y.$
¿Es posible construir un circuito combinacional $f^{-1}$ tal que al
ingresar $y$ recupere $x$?

En general, **no es posible**. Para que una función sea estrictamente
invertible, debe ser matemática y lógicamente **biyectiva** (inyectiva y
sobreyectiva). La gran mayoría de funciones lógicas prácticas proyectan
muchas entradas sobre una única salida (por ejemplo, una puerta AND de 2
entradas proyecta 3 combinaciones de entrada distintas hacia un '0' a la
salida).

Esta compresión de estados conlleva una *pérdida de información (aumento
de entropía termodinámica)*. Una vez que la salida es '0', el hardware
no retiene rastro de qué combinación original provocó ese '0'. La
invertibilidad pura solo existe en conjuntos muy restrictivos de puertas
lógicas denominadas reversibles (como Fredkin y Toffoli), empleadas en
computación cuántica, pero no en las familias lógicas combinacionales
estándar basadas en compuertas irreversibles.

## Circuitos Aritméticos

La aritmética binaria es el núcleo de las ALUs (Arithmetic Logic Units)
de las computadoras. Al trabajar con números naturales binarios de
longitud de palabra fija, podemos construir circuitos aritméticos
utilizando pura lógica combinacional.

### Comparadores de Magnitud

Un comparador toma dos palabras binarias $A$ y $B$ de $n$ bits y
determina su relación de orden, produciendo tres salidas mutuamente
excluyentes: $(A = B),$ $(A > B),$ y $(A < B).$ La igualdad se computa
trivialmente operando bit a bit mediante puertas XNOR, y haciendo un AND
global del resultado: si todos los bits homólogos son idénticos, las
palabras son iguales.

### Suma: Half-Adder y Full-Adder

El sumador básico o **Semisumador (Half-Adder)** suma dos bits
individuales ($A$ y $B$) produciendo una Suma ($S$) y un Acarreo
($C_{out}$ o Carry Out): $$S = A \oplus B$$ $$C_{out} = A \cdot B$$ Sin
embargo, para sumar números de varios bits, necesitamos sumar columnas
intermedias que también reciben un acarreo de la columna anterior. Para
ello construimos el **Sumador Completo (Full-Adder)**, que toma tres
bits ($A, B, C_{in}$) y devuelve $S$ y $C_{out}:$
$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = (A \cdot B) + C_{in} \cdot (A \oplus B)$$ Conectando $n$
Full-Adders en cascada (conectando el $C_{out}$ de la posición $i$ al
$C_{in}$ de la posición $i+1$) formamos un sumador **Ripple-Carry**
capaz de sumar palabras completas de $n$ bits.

### Restadores (Borrow Clásico)

El **Restador Completo (Full-Subtractor)** funciona análogamente al
sumador, pero restando $A - B - B_{in}$ (donde $B_{in}$ es el préstamo o
*Borrow* de la columna anterior). Devuelve una Diferencia ($D$) y genera
un Borrow Out ($B_{out}$): $$D = A \oplus B \oplus B_{in}$$
$$B_{out} = (\overline{A} \cdot B) + B_{in} \cdot \overline{(A \oplus B)}$$
La similitud de las ecuaciones demuestra la dualidad entre suma y resta
en hardware natural.

### Multiplicadores Combinacionales

El algoritmo de multiplicación en papel consiste en multiplicar (bit a
bit) y luego sumar versiones desplazadas. En hardware, la
\"multiplicación\" bit a bit entre $A_i$ y $B_j$ se implementa
directamente con una única puerta AND ($A_i \cdot B_j = 1$ solo si ambos
son 1). Un multiplicador combinacional básico consiste en una matriz
bidimensional de puertas AND que calculan todos los productos parciales
simultáneamente, cuyos resultados alimentan una red paralela o árbol de
sumadores que agregan los productos parciales (desplazados por cableado
geométrico) para formar el producto final de $2n$ bits.

## Otros Bloques Combinacionales Clásicos

Aparte de la aritmética estricta y el enrutamiento, existen otros
componentes MSI esenciales en el diseño de computadoras y sistemas de
comunicación.

### Generadores y Detectores de Paridad

En la transmisión de datos binarios, es común que el ruido
electromagnético altere algún bit. Una técnica clásica de detección de
errores (que no corrección) es el bit de paridad. Un **Generador de
Paridad** toma una palabra de $n$ bits y genera un bit extra, de forma
que el número total de unos transmitidos sea siempre par (Paridad Par) o
siempre impar (Paridad Impar).

Matemáticamente, la paridad par de una palabra se calcula haciendo la
suma exclusiva (XOR) de todos sus bits:
$$P = b_0 \oplus b_1 \oplus b_2 \oplus \dots \oplus b_{n-1}$$ El
circuito es simplemente un \"árbol de XORs\". En el extremo receptor, el
**Detector de Paridad** toma los $n$ bits de datos más el bit de
paridad, y los pasa todos por otro árbol XOR. Si no ha habido ningún
error (o un número par de errores), el resultado global será $0.$ Si ha
habido un error en un bit, el resultado será $1,$ disparando una alarma
de integridad de datos.

### Desplazadores de Barril (Barrel Shifters)

Desplazar los bits de un número a la izquierda o derecha es el
equivalente hardware a multiplicar o dividir por potencias de 2, una
operación fundamental en los microprocesadores. Si bien el
desplazamiento suele hacerse de forma secuencial (un bit por ciclo de
reloj) usando registros de desplazamiento, los procesadores de alto
rendimiento exigen hacerlo en **un solo ciclo**.

El **Barrel Shifter** es un circuito puramente combinacional que puede
desplazar o rotar una palabra de $n$ bits por un número arbitrario de
posiciones especificadas por una entrada de control binaria. Se
construye típicamente usando una red de multiplexores: una primera capa
que decide si desplazar 1 posición o nada, una segunda que decide si
desplazar 2 posiciones o nada, una tercera para 4 posiciones, etc.

### La Unidad Lógica Aritmética (ALU)

Finalmente, la cúspide de la integración combinacional es la ALU. Una
ALU integra un sumador, un restador, comparadores y puertas lógicas bit
a bit (AND, OR, XOR, NOT) dentro de un único bloque funcional unificado.

Para seleccionar qué operación debe ejecutarse sobre los operandos $A$ y
$B,$ la ALU dispone de unas líneas de selección especiales llamadas
**Código de Operación (OpCode)**. Internamente, la ALU calcula *todas*
las operaciones simultáneamente en paralelo, y utiliza un
**Multiplexor** gigante, gobernado por el OpCode, para enrutar
únicamente el resultado deseado hacia la salida final. Todo este
conjunto sigue siendo estrictamente combinacional.

# Familias Lógicas y Parámetros Eléctricos

El Álgebra de Boole opera sobre un universo inmaculado de ceros y unos
perfectos. En él, los cambios de estado ocurren en cero segundos, y las
puertas lógicas pueden conectarse a infinitas compuertas sin que la
señal sufra degradación. Sin embargo, en la ingeniería del mundo real,
las funciones booleanas se implementan utilizando transistores,
voltajes, y cables que presentan capacitancias parásitas y resistencias.

Este capítulo cierra la brecha entre la lógica abstracta y la
circuitería física, estudiando cómo los componentes electrónicos reales
fallan, se retrasan, e imponen límites estrictos al diseño digital.

## Tecnologías de Familias Lógicas

Históricamente, los interruptores digitales evolucionaron desde los
relés electromecánicos a las válvulas de vacío. La verdadera revolución
llegó con los semiconductores. En un circuito integrado (CI), una puerta
lógica se construye interconectando transistores. Al conjunto de chips
que comparten la misma arquitectura subyacente de transistores, niveles
de voltaje, e interfaces eléctricas, se le denomina **Familia Lógica**.

### La Tecnología TTL

La Lógica Transistor-Transistor (TTL) dominó la industria desde los años
70 hasta los 90. Internamente emplea transistores bipolares (BJT). El
estándar original utilizaba una tensión de alimentación unificada de
$5\text{V}.$

La variante más famosa y ubicua de esta tecnología es la serie comercial
**74LS** (*Low-power Schottky*). En esta serie, la adición de diodos
Schottky previene que los transistores entren en saturación profunda,
aumentando drásticamente la velocidad de conmutación. Pese a ser
obsoleta comercialmente frente a tecnologías modernas, la serie TTL
sigue siendo el pilar de los laboratorios docentes debido a su extrema
robustez frente a cortocircuitos accidentales y maltrato eléctrico,
además de establecer el estándar histórico de facto para los voltajes
lógicos de $5\text{V}.$

### La Tecnología CMOS

La llegada de la lógica basada en semiconductores de óxido metálico
complementarios (CMOS) revolucionó por completo la densidad de
integración y el consumo de energía. CMOS utiliza parejas de
transistores MOSFET (tipo N y tipo P) dispuestos de forma que
**siempre** uno de ellos esté cortado en estado de reposo.

- **Ventaja Absoluta:** El consumo estático (cuando las entradas no
  cambian) es virtualmente cero. Esto permitió la miniaturización sin
  fundir térmicamente el chip, habilitando procesadores con miles de
  millones de transistores.

- **Serie 74HC (*High-Speed CMOS*):** Velocidad comparable al 74LS, pero
  con el consumo microscópico de la tecnología CMOS.

- **Serie 74HCT (*CMOS TTL-compatible*):** Construida en CMOS pero con
  los umbrales de detección de voltaje deliberadamente alterados en
  fábrica para ser compatibles con los niveles clásicos del TTL,
  actuando como un puente entre ambos mundos.

## Parámetros de Voltaje y Márgenes de Ruido

En el mundo físico, un "$1$" lógico o un "$0$" no es un punto escalar
perfecto, sino una franja o *banda de voltaje*.

### Niveles Lógicos Garantizados

Todo fabricante especifica cuatro voltajes críticos en sus diagramas
eléctricos:

- $V_{IL}$ (*Voltage Input Low*): Voltaje máximo garantizado que el chip
  reconocerá sin ambigüedades como un cero lógico a la entrada.

- $V_{IH}$ (*Voltage Input High*): Voltaje mínimo garantizado que el
  chip interpretará sólidamente como un uno lógico.

- $V_{OL}$ (*Voltage Output Low*): Voltaje máximo que entregará la
  puerta por su pin de salida cuando intente expulsar un cero lógico.

- $V_{OH}$ (*Voltage Output High*): Voltaje mínimo garantizado de salida
  cuando se intente expulsar un uno lógico.

Para que una puerta A pueda excitar correctamente a una puerta B, la
señal eléctrica de la salida de A debe caer sobradamente dentro de las
tolerancias de lectura de B. Por diseño, siempre debe cumplirse que
$V_{OH} > V_{IH}$ y $V_{OL} < V_{IL}.$

### La Zona Prohibida (\"Tierra de Nadie\")

El espacio comprendido estrictamente entre $V_{IL}$ y $V_{IH}$ se
denomina zona de transición o zona prohibida. Si una entrada analógica
cae en este voltaje intermedio, ocurren varios fenómenos indeseados:

1.  **Comportamiento Erróneo o Oscilante:** La salida podría fluctuar de
    0 a 1 caóticamente ante el mínimo ruido electromagnético ambiental
    (antena).

2.  **Sobreconsumo Térmico:** Especialmente crítico en CMOS. Si un
    transistor de entrada se detiene a mitad de camino, ambos
    transistores (Pull-up y Pull-down) conducirán simultáneamente,
    generando un cortocircuito directo entre $V_{CC}$ y Tierra que
    disipará calor masivamente.

### Márgenes de Inmunidad al Ruido

El margen de ruido cuantifica cuánta interferencia electromagnética
(voltaje parásito inducido en las pistas de cobre) puede soportar un
cable antes de que la compuerta receptora lea un valor equivocado. Se
define asimétricamente para ambos estados:
$$M_{N_H} \text{ (Margen Alto)} = V_{OH} - V_{IH}$$
$$M_{N_L} \text{ (Margen Bajo)} = V_{IL} - V_{OL}$$ La tecnología CMOS
no solo consume menos, sino que proporciona márgenes de ruido
drásticamente superiores al TTL, rozando casi el $\sim 1.5\text{V}$ de
inmunidad frente a los $\sim 0.4\text{V}$ típicos del 74LS, blindándola
para entornos ruidosos industriales.

## Parámetros de Corriente y Carga (Fan-Out)

Las compuertas lógicas están formadas por semiconductores, y enviar
voltajes requiere mover electrones. Adoptamos una convención de signo
estándar: la corriente que **entra** al chip desde el exterior se denota
positiva, y la corriente que **sale** del chip impulsada por él se
denota negativa.

### Especificaciones de Corriente

Encontramos cuatro corrientes limitantes en toda familia lógica:

- $I_{IL} / I_{IH}:$ Corriente requerida para inyectar/drenar de un pin
  de entrada al forzar un estado bajo ($L$) o alto ($H$). Es el
  \"coste\" de empujar electrones hacia la puerta.

- $I_{OL} / I_{OH}:$ Capacidad máxima de conducción de la etapa de
  salida (cuántos amperios puede hundir a Tierra o proporcionar desde la
  fuente antes de que el voltaje caiga fuera de tolerancia).

### Fan-in y Fan-out Estático

El **Fan-in** es, estructuralmente, el número máximo de pines de entrada
físicos que un modelo de puerta concreta tiene diseñados (una NAND de 3
entradas tiene un Fan-in de 3).

El **Fan-out** es mucho más crítico. Es la cantidad máxima de compuertas
idénticas que una única compuerta conductora puede pilotar conectadas en
paralelo sin que se viole ningún nivel de voltaje de seguridad. Se
calcula como el peor caso de ambos regímenes (High y Low):
$$\text{Fan-out} = \min \left( \left\lfloor \frac{|I_{OH}|}{|I_{IH}|} \right\rfloor, \left\lfloor \frac{|I_{OL}|}{|I_{IL}|} \right\rfloor \right)$$

**Paradigma TTL vs CMOS:** En la tecnología TTL Bipolar (74LS), los
transistores requieren corrientes físicas sustanciales en la base para
mantenerse abiertos. Esto limita el Fan-Out estático rígidamente a
$10 \text{ ó } 20$ puertas. Si conectas $21,$ la puerta no tendrá fuerza
para empujar a todas, $V_{OH}$ colapsará hacia tierra y los unos lógicos
se leerán como ceros lógicos. En la tecnología CMOS (74HC), las
compuertas (Gates) de los MOSFET están aisladas con cristal de óxido de
silicio; su resistencia de entrada es casi infinita. Su corriente de
entrada $I_{IN}$ es de picoamperios. Esto arroja un Fan-out teórico
estático colosal (millones). Sin embargo, el Fan-out en CMOS no está
limitado por la corriente continua, sino por el límite de capacitancia
*dinámica*: cada compuerta añadida añade pequeños capacitores parásitos;
empujar muchas compuertas CMOS a la vez no destruye el voltaje, pero
ralentiza astronómicamente el flanco de subida, arruinando la velocidad
temporal del circuito.

## Problemas Temporales (Timing) y Glitches

El sustrato físico tiene masa inercial eléctrica (capacitancias).
Modificar un voltaje de $0\text{V}$ a $5\text{V}$ no ocurre
instantáneamente en un instante $t=0.$

### Tiempos Característicos

Para dimensionar sistemas secuenciales o calcular límites de frecuencia,
observamos los diagramas de tiempos (*Timing Diagrams*) buscando los
parámetros:

- **Tiempos de Transición ($t_r$ y $t_f$):** El tiempo de subida (*Rise
  Time*, $t_r$) es el lapso requerido para que la señal eléctrica escale
  del $10\%$ al $90\%$ del voltaje objetivo. Análogamente para la caída
  (*Fall Time*, $t_f$).

- **Retardos de Propagación ($t_{pLH}$ y $t_{pHL}$):** Es el retraso
  fundamental de reacción de la propia puerta. Si alteramos los
  estímulos en la entrada, la puerta tarda decenas de nanosegundos en
  evaluar y propagar el nuevo resultado matemático a su salida (medido
  generalmente al cruzar el $50\%$ del voltaje nominal). Se define un
  $t_{pd}$ promedio general como $(t_{pLH} + t_{pHL}) / 2.$

### Pulsos Espurios (Hazards y Glitches)

Los retardos de propagación $t_{pd}$ no son idénticos para diferentes
transistores ni para diferentes caminos en un grafo combinacional.
Cuando la información fluye desde las entradas hacia la salida final de
un combinacional cruzando rutas con distinto número de puertas
intercaladas, algunas señales llegarán *después* que otras. Durante este
régimen transitorio microscópico, la función matemática de salida evalúa
resultados inválidos (estado intermedio). Esto puede traducirse en picos
afilados de voltaje llamados **Glitches** o *Hazards* de estado.

En álgebra pura $x \wedge \neg x = \bot$ siempre. Físicamente, si a una
puerta AND le entra una señal y su respectiva señal invertida
(proveniente de una puerta NOT con $t_{pd} = 15\text{ns}$), durante $15$
nanosegundos la puerta AND observará accidentalmente ambas entradas
altas al mismo tiempo en el instante de transición, devolviendo
momentáneamente un $\top$ falso. Estos glitches son fatales si la red
combinacional está pilotando sistemas secuenciales sensibles al flanco
(como veremos en capítulos de memorias biestables y Flip-Flops).

# Representación de la Información

Para que las funciones lógicas y los circuitos descritos en capítulos
anteriores tengan utilidad práctica en el mundo de la ingeniería,
necesitamos vincular los estados electromagnéticos abstractos (los ceros
y unos del hardware) con entidades del mundo real: números naturales,
enteros, reales, o caracteres de nuestro lenguaje escrito. Este capítulo
formaliza el paso del sustrato físico-lógico hacia la semántica
interpretativa.

## Sintaxis Lógica: Alfabetos y Lenguajes

Antes de asignar significado, debemos definir rígidamente la estructura
de lo que vamos a interpretar. Un **alfabeto** $\Sigma$ es un conjunto
finito, no vacío, de símbolos indivisibles. En electrónica digital
elemental, nuestro alfabeto principal es el alfabeto booleano
$\mathbb{B}_2 = \{0, 1\}.$ Sin embargo, la teoría es generalizable a
cualquier alfabeto finito $\mathbb{D}_B = \{d_0, d_1, \dots, d_{B-1}\},$
donde $B$ es la cardinalidad o base del alfabeto.

Un **lenguaje formal** sobre un alfabeto $\Sigma$ es un conjunto de
*palabras*, donde una palabra se define como una secuencia (ristra)
ordenada y finita de símbolos concatenados extraídos de $\Sigma.$ El
conjunto de todas las palabras posibles de cualquier longitud,
incluyendo la palabra vacía, se denota mediante la Clausura de Kleene
$\Sigma^*.$

En el contexto de la arquitectura de computadores, el hardware está
compuesto por buses y registros de un tamaño rígidamente predefinido.
Por ello, no trabajamos con $\Sigma^*,$ sino que nos restringimos al
subconjunto de palabras de **longitud constante** $n.$ Podemos
visualizar formalmente una palabra $w$ de longitud $n$ como un vector
perteneciente al espacio vectorial unidimensional o producto cartesiano
$(\mathbb{D}_B)^n:$
$$w = (w_{n-1}, w_{n-2}, \dots, w_1, w_0) \quad \text{donde } w_i \in \mathbb{D}_B$$
Al símbolo de índice $0$ ($w_0$) se le denomina dígito menos
significativo (*Least Significant Digit*, LSB en binario), y al símbolo
de índice $n-1$ ($w_{n-1}$) dígito más significativo (*Most Significant
Digit*, MSB). Hasta este punto, una palabra es una pura estructura
sintáctica sin valor intrínseco.

## Semántica: Números Naturales en Base $B$

Para dotar de significado numérico a las palabras sintácticas,
establecemos una aplicación semántica (función de evaluación)
$V: (\mathbb{D}_B)^n \to \mathbb{N}.$ La convención universal para esta
aplicación es la **notación posicional**, donde el aporte de cada
símbolo al valor total está ponderado exponencialmente según su índice
(posición) $i.$ Dado el alfabeto $\mathbb{D}_B$ con cardinal $B,$
asociamos a cada símbolo $d_k$ un valor primitivo $k.$ El valor natural
total $V$ representado por la palabra $w = w_{n-1} \dots w_0$ es:
$$V(w) = \sum_{i=0}^{n-1} V(w_i) \cdot B^i$$ Por ejemplo, en el alfabeto
decimal ($B=10$), la palabra $402$ se evalúa como
$4 \cdot 10^2 + 0 \cdot 10^1 + 2 \cdot 10^0 = 402.$ En el alfabeto
binario ($B=2$), la palabra $1101_2$ evalúa a
$1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 13_{10}.$

Para un alfabeto arbitrario de base $B$ y una longitud de palabra de $n$
posiciones, el mínimo valor representable es $0$ (todas las posiciones
en $d_0$) y el máximo valor representable está acotado algebraicamente
por: $$V_{\max} = \sum_{i=0}^{n-1} (B-1) \cdot B^i = B^n - 1$$ Toda
operación aritmética cuyo resultado sobrepase $B^n - 1$ sufrirá pérdida
de información o *Desbordamiento (Overflow)*.

## Operaciones a Nivel de Palabra (Sintácticas)

Previo a introducir semánticas más complejas como los números negativos,
resulta imperativo definir matemáticamente dos operaciones unarias
puramente sintácticas aplicables a cualquier palabra en un alfabeto de
base $B.$

### Complementación a la Base menos 1 (Cb-1)

Dada una palabra $w,$ el complemento a la base menos 1, que denotaremos
provisoriamente como $C_{B-1}(w),$ se obtiene invirtiendo cada símbolo
individualmente contra el valor máximo del alfabeto ($B-1$).
$$(C_{B-1}(w))_i = (B - 1) - w_i$$ En el caso particular del alfabeto
binario ($B=2$), el valor $B-1 = 1,$ por lo que la operación se reduce a
$(C_1(w))_i = 1 - w_i.$ Esta es estrictamente la definición de la
compuerta lógica NOT ($\neg$). Por lo tanto, el Complemento a 1 de un
número binario es simplemente su inversión bit a bit lógica.

### Complementación a la Base (Cb)

El Complemento a la Base, denotado $C_B(w),$ se define matemáticamente
partiendo del anterior y sumando $1$ a la palabra resultante:
$$C_B(w) = C_{B-1}(w) + 1$$ Algebraicamente, esto es equivalente a
calcular $B^n - V(w).$ Dado que operamos en hardware de longitud fija
$n,$ la suma genera frecuentemente un acarreo que escapa a la posición
$n,$ el cual simplemente se descarta (operación módulo $B^n$). En
binario, esto corresponde al célebre Complemento a 2, que consiste en
invertir todos los bits y sumar $1.$

## Semántica Avanzada: Enteros con Signo

Para procesar números negativos (el conjunto $\mathbb{Z}$), la solución
trivial de reservar un símbolo físico exclusivo tipo \"$-$\" es
imposible, ya que el hardware solo dispone de su alfabeto base (ej. $0$
y $1$). Por ende, el signo debe ser codificado implícitamente empleando
parte de la entropía de los símbolos existentes.

### Magnitud y Signo (M&S)

En este esquema, dividimos rígidamente la palabra $w$ de longitud $n$ en
dos campos semánticos:

1.  El símbolo más significativo ($w_{n-1}$) se reserva exclusivamente
    para el signo. Por convención unánime en computación binaria, $0$
    representa positivo y $1$ negativo.

2.  Los $n-1$ símbolos restantes se interpretan como la magnitud
    absoluta del número en notación posicional natural.

El valor representado es:
$$V(w) = (-1)^{w_{n-1}} \cdot \sum_{i=0}^{n-2} V(w_i) \cdot B^i$$ Este
modelo presenta dos graves problemas de ingeniería: Primero, genera una
doble representación del cero ($+0$ y $-0$), un desperdicio entrópico
inaceptable. Segundo, requiere de una Unidad Lógica Aritmética (ALU)
notablemente compleja, ya que la suma y resta de variables requieren
circuitos distintos dependientes del análisis de los signos previos.

### Complemento a la Base general (Cb)

El estándar computacional moderno para representar enteros solventa los
problemas anteriores asumiendo la semántica de la complementación a la
base (Complemento a 2 en binario). En este esquema, el dígito $w_{n-1}$
sigue decidiendo el signo, pero lo hace asignando un peso posicional
estrictamente **negativo** al MSB. La ecuación de valor para un sistema
binario en C2 es:
$$V(w) = -w_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} w_i \cdot 2^i$$
Generalizado a base $B,$ los números negativos se construyen calculando
explícitamente el complemento a la base de la magnitud absoluta. Las
ventajas son abrumadoras:

- Existe un único cero (el $-0$ colapsa tras sumar 1 y descartar el
  rebose).

- Rango asimétrico maximizado: $[-B^{n-1}, B^{n-1} - 1].$

- **Ceguera Aritmética:** La maravilla del Cb es que las restas $A - B$
  se realizan como sumas $A + C_B(B).$ El hardware sumador (Full-Adder)
  no necesita saber si está sumando naturales, enteros positivos o
  negativos; el mismo circuito lógico produce el resultado binario
  correcto módulo $B^n.$

### Exceso a Bias (Exceso a $K$)

Una alternativa para enteros es la semántica desplazada. En lugar de
manipular el signo bit a bit, redefinimos el cero desplazándolo al
centro del rango representable natural. Elegimos una constante de sesgo
o *Bias* $K.$ El valor representado $V$ es la evaluación natural
estricta de la palabra binaria $V_{\text{nat}}(w)$ menos la constante
$K:$ $$V(w) = V_{\text{nat}}(w) - K$$ Convencionalmente, para $n$
dígitos, $K = B^{n-1}$ o bien $K = B^{n-1}-1.$ Este sistema garantiza
que los números más negativos estén codificados sintácticamente con
todos los ceros, y los más positivos con todos los unos. Aunque no es
ideal para aritmética general (requiere ajustar el bias tras cada suma),
es el sistema predilecto universal para comparar exponentes, dado que el
hardware del comparador de magnitud binario estándar funciona de forma
directa sin alteraciones.

## Representación Fraccionaria (Punto Fijo)

Para representar los números Reales ($\mathbb{R}$), comenzamos asumiendo
un \"Punto Radix\" o coma decimal inamovible (implícita por diseño
hardware). Separamos la palabra de longitud total $N$ en dos tramos
fijos: $n$ posiciones para la parte entera y $m$ posiciones para la
parte fraccionaria ($N = n + m$).

Las ponderaciones posicionales decrecen, continuando a través del límite
cero hacia potencias negativas de la base $B.$ La ecuación de un natural
de punto fijo es la generalización natural:
$$V(w) = \sum_{i=-m}^{n-1} V(w_i) \cdot B^i$$ Tanto la representación de
Magnitud y Signo fraccionaria como la del Complemento a la Base
fraccionario operan idénticamente al caso entero. En Complemento a 2
fraccionario, el bit de signo ocupa la posición ponderada a $-2^{n-1},$
y el resto de la estructura se mantiene, permitiendo a la ALU sumar
decimales como si fueran enteros, simplemente ignorando lógicamente
dónde ubicó el diseñador la coma de forma imaginaria.

## Representación en Punto Flotante

El punto fijo es rígido: o perdemos exactitud en valores pequeños (poco
tramo fraccionario) o perdemos alcance en los valores inmensos (poco
tramo entero). La notación científica solventa esto disociando el tamaño
del número (el orden de magnitud) de sus cifras significativas. El
estándar generalizado de punto flotante descompone la palabra binaria
general en tres campos lógicos yuxtapuestos:

1.  **Signo (S):** Un solo bit (o equivalente en otra base) donde $0$ es
    positivo y $1$ negativo.

2.  **Exponente (E):** Una secuencia de $k$ posiciones tratadas siempre
    como un entero representado en **Exceso a Bias**. Este Bias permite
    manejar exponentes negativos.

3.  **Mantisa o Fracción (M):** Las $m$ cifras significativas del valor,
    operando estrictamente como un campo de coma fija fraccionario.

El formato impone una **Normalización**. En notación científica
estándar, un número siempre se desliza para que la coma recaiga tras el
primer dígito no nulo (ej. $5.32 \times 10^4$). En la base binaria
($B=2$), el único dígito distinto de $0$ es el $1.$ Esto nos regala un
ahorro enorme: no necesitamos almacenar explícitamente el '1' inicial,
ahorrando un bit completo. A este '1' no almacenado se le denomina **bit
fantasma** o bit implícito.

La ecuación unificada de evaluación de un número de punto flotante
normalizado en base binaria genérica es:
$$V = (-1)^S \cdot (1 + M_{fracc}) \cdot 2^{E_{\text{nat}} - \text{Bias}}$$

### El Estándar IEEE-754

El estándar real sobre el que funciona toda la electrónica y computación
modernas para la precisión fraccionaria es el **IEEE-754**. Su
encarnación más famosa son los tipos de datos nativos de punto flotante
de los lenguajes de programación:

- **Precisión Simple (float, 32 bits):** Un bit de signo, un exponente
  $E$ de 8 bits (Bias = $127$), y una mantisa $M$ de 23 bits
  fraccionarios.

- **Doble Precisión (double, 64 bits):** Un bit de signo, exponente de
  11 bits (Bias = $1023$), y una descomunal mantisa de 52 bits para
  altísima precisión computacional.

Además, el IEEE-754 reserva combinaciones particulares del exponente y
la mantisa para semánticas de excepción, como representar el Infinito
($\pm \infty$), el Cero ($\pm 0$ matemáticamente estricto) o entidades
No Numéricas (*Not a Number, NaN*), vitales cuando se intenta dividir
por cero o hacer una raíz cuadrada de un número negativo.

## Códigos Alfanuméricos y Códigos Especiales

La semántica posicional sirve para modelar la matemática. Pero para
procesar cadenas de texto o interaccionar con entornos físicos, debemos
establecer codificaciones puramente convencionales, diccionarios de
traducción (Look-up tables).

### Códigos de Caracteres

- **ASCII:** El *American Standard Code for Information Interchange*
  original codificaba 128 caracteres utilizando un alfabeto binario de
  longitud $n=7$ bits. Mapeaba los valores numéricos decimales del 0 al
  127 contra los caracteres anglosajones y de control de los teletipos
  (por ejemplo, el 65 corresponde a la 'A' mayúscula y el 32 al espacio
  en blanco). Se extendió posteriormente a 8 bits (Añadiendo eñes,
  vocales acentuadas, etc).

- **Unicode:** Un inmenso consorcio internacional dedicado a codificar
  todos los sistemas de escritura humanos (desde el alfabeto latino,
  cirílico o chino, hasta símbolos matemáticos y emojis). Un
  identificador Unicode (Code Point) es un valor teórico abstracto, no
  una forma de escribir bits en memoria.

- **UTF (Unicode Transformation Format):** Son las formas reales de
  inyectar Unicode en memoria.

  - **UTF-8:** Estándar de longitud *variable*. Mapea cada carácter
    usando de 1 a 4 bytes. Es universalmente retrocompatible con el
    ASCII básico.

  - **UTF-16 y UTF-32:** Ocupan tamaños mínimos de 2 bytes (16 bits) o 4
    bytes fijos (32 bits), útiles en bases de datos pesadas que
    prefieren ancho fijo para facilitar la indexación a costa de
    desperdiciar memoria.

### Códigos de Distancia Unitaria (Código Gray)

Existen dominios electromecánicos (como codificadores rotatorios o
discos ópticos en brazos robóticos) donde el código posicional numérico
puro de base 2 es desastroso. Si pasamos del número binario 3 ($011_2$)
al número 4 ($100_2$), tres bits cambian de estado de forma
completamente simultánea. Físicamente, un contacto eléctrico
inevitablemente conmutará picosegundos antes que el otro, provocando que
la máquina, durante una fracción minúscula de tiempo, lea un número
intermedio basura disparando rutinas de fallo.

Para solucionar esto se inventaron los códigos continuos de distancia
unitaria, el más famoso siendo el **Código Gray**. En el código Gray,
dos valores consecutivos cualquiera \*\*siempre\*\* difieren en
exactamente un único bit (distancia de Hamming = $1$). Esto garantiza
transiciones mecánicas inmaculadas sin lecturas esporádicas.
Adicionalmente, esta propiedad de adyacencia de Gray es precisamente la
infraestructura que organiza los ejes lógicos en los Mapas de Karnaugh
que estudiamos en minimización.

# Resumen de Postulados y Teoremas (Notación Ingenieril)

En esta sección se recopilan los postulados de Huntington y los teoremas
principales derivados, transcritos a la notación propia del álgebra de
conmutación y la lógica digital ($+,$ $\cdot,$ $0,$ $1,$
$\overline{a}$), concebidos como hoja de referencia rápida.

### Pre-Axiomas de la Estructura {#pre-axiomas-de-la-estructura-1 .unnumbered}

> **Preaxioma (Estructura de Conjunto):**[]{#esconj_eng
> label="esconj_eng"} Se requiere que se defina sobre un conjunto (por
> ejemplo, $\mathbb{B}_2 = \{0, 1\}$).

> **Preaxioma (Constantes Lógicas):**[]{#constantes_eng
> label="constantes_eng"} Este conjunto contiene dos constantes
> fundamentales: $0$ (falso) y $1$ (verdadero).

> **Preaxioma (Operaciones Binarias Internas):**[]{#opbinint_eng
> label="opbinint_eng"} Se definen dos operaciones binarias internas, la
> suma ($+$) y el producto ($\cdot$): $$\begin{align*}
> + &: \mathbb{B}_2 \times \mathbb{B}_2 \to \mathbb{B}_2 \\
> \cdot &: \mathbb{B}_2 \times \mathbb{B}_2 \to \mathbb{B}_2
> \end{align*}$$

> **Preaxioma (Existencia y Unicidad de Imagen):**[]{#exist_unic_eng
> label="exist_unic_eng"} Para cada par de elementos del conjunto, las
> operaciones $+$ y $\cdot$ siempre producen un resultado que también
> pertenece al conjunto, y ese resultado es siempre único.

### Postulados de Huntington {#postulados-de-huntington .unnumbered}

> **Postulado (Elemento neutro):**[]{#neutro_eng label="neutro_eng"}
> $$a + 0 = a \qquad \text{y} \qquad a \cdot 1 = a$$

> **Postulado (Conmutatividad):**[]{#conmut_eng label="conmut_eng"}
> $$a + b = b + a \qquad \text{y} \qquad a \cdot b = b \cdot a$$

> **Postulado (Distributividad):**[]{#distrib_eng label="distrib_eng"}
> $$a \cdot (b + c) = (a \cdot b) + (a \cdot c) \qquad \text{y} \qquad a + (b \cdot c) = (a + b) \cdot (a + c)$$

> **Postulado (Complementario):**[]{#comp_eng label="comp_eng"} Para
> cada elemento $a,$ existe un complemento $\overline{a}$ tal que:
> $$a + \overline{a} = 1 \qquad \text{y} \qquad a \cdot \overline{a} = 0$$

### Teoremas Fundamentales {#teoremas-fundamentales .unnumbered}

> **Teorema (Unicidad de los elementos
> neutros):**[]{#unicidad_neutros_eng label="unicidad_neutros_eng"} El
> elemento neutro para la suma ($0$) y para el producto ($1$) son
> únicos.

> **Teorema (Idempotencia):**[]{#idempotencia_eng
> label="idempotencia_eng"}
> $$a + a = a \qquad \text{y} \qquad a \cdot a = a$$

> **Teorema (Elementos absorbentes):**[]{#absorbentes_eng
> label="absorbentes_eng"}
> $$a + 1 = 1 \qquad \text{y} \qquad a \cdot 0 = 0$$

> **Teorema (Propiedades de absorción):**[]{#absorcion_eng
> label="absorcion_eng"}
> $$a + (a \cdot b) = a \qquad \text{y} \qquad a \cdot (a + b) = a$$

> **Teorema (Leyes de De Morgan):**[]{#morgan_eng label="morgan_eng"}
> $$\overline{a + b} = \overline{a} \cdot \overline{b} \qquad \text{y} \qquad \overline{a \cdot b} = \overline{a} + \overline{b}$$

> **Teorema (Involución (Doble negación)):**[]{#involucion_eng
> label="involucion_eng"} $$\overline{\overline{a}} = a$$

> **Teorema (Asociatividad):**[]{#asociatividad_eng
> label="asociatividad_eng"}
> $$a + (b + c) = (a + b) + c \qquad \text{y} \qquad a \cdot (b \cdot c) = (a \cdot b) \cdot c$$

> **Teorema (Unicidad del complemento):**[]{#unic_comp_eng
> label="unic_comp_eng"} El complemento $\overline{a}$ de un elemento
> $a$ es único.

> **Teorema (Otras propiedades equivalentes):**[]{#otras_prop_eng
> label="otras_prop_eng"}
>
> - **Orden de retículo:** $a + b = a \iff a \cdot b = b$
>
> - **Equivalencia de operaciones:** $a + b = a \cdot b \implies a = b$
>
> - **Cancelación:**
>   $(a + b = a + c \text{ y } a \cdot b = a \cdot c) \implies b = c$

> **Definicion (Generalización a $n$ variables):**[]{#gen_n_vars_eng
> label="gen_n_vars_eng"} Las operaciones disyunción y conjunción pueden
> extenderse a un número $n$ de variables mediante los símbolos
> sumatorio y productorio:
> $$\sum_{i=1}^{n} x_i = x_1 + x_2 + \dots + x_n$$
> $$\prod_{i=1}^{n} x_i = x_1 \cdot x_2 \cdot \dots \cdot x_n$$

> **Teorema (Casos de Álgebra Trivial):**[]{#trivial_eng
> label="trivial_eng"} Si $0 = 1,$ o si existe algún elemento tal que
> $\overline{a} = a,$ entonces el álgebra contiene un único elemento
> (álgebra trivial).

> **Teorema (Teorema de Adyacencia (Expansión de
> Shannon)):**[]{#adyacencia_eng label="adyacencia_eng"}
> $$a = (a \cdot b) + (a \cdot \overline{b}) \qquad \text{y} \qquad a = (a + b) \cdot (a + \overline{b})$$

> **Teorema (Teorema de Reducción (Absorción
> Fuerte)):**[]{#reduccion_eng label="reduccion_eng"}
> $$a + (\overline{a} \cdot b) = a + b \qquad \text{y} \qquad a \cdot (\overline{a} + b) = a \cdot b$$

> **Teorema (Teorema del Consenso (Quine)):**[]{#consenso_eng
> label="consenso_eng"}
> $$(a \cdot b) + (\overline{a} \cdot c) + (b \cdot c) = (a \cdot b) + (\overline{a} \cdot c)$$
> $$(a + b) \cdot (\overline{a} + c) \cdot (b + c) = (a + b) \cdot (\overline{a} + c)$$

### Comportamiento de Operadores Derivados {#comportamiento-de-operadores-derivados .unnumbered}

> **Teorema (Idempotencia cruzada (NAND/NOR)):**[]{#idemp_cruzada_eng
> label="idemp_cruzada_eng"}
> $$a \uparrow a = \overline{a} \qquad \text{y} \qquad a \downarrow a = \overline{a}$$

> **Teorema (Generación de AND y OR):**[]{#gen_inf_sup_eng
> label="gen_inf_sup_eng"}
> $$a \cdot b = \overline{a \uparrow b} = (a \uparrow b) \uparrow (a \uparrow b) \qquad \text{y} \qquad a + b = \overline{a \downarrow b} = (a \downarrow b) \downarrow (a \downarrow b)$$

> **Teorema (Generación cruzada):**[]{#gen_cruzada_eng
> label="gen_cruzada_eng"}
> $$a + b = \overline{a} \uparrow \overline{b} = (a \uparrow a) \uparrow (b \uparrow b) \qquad \text{y} \qquad a \cdot b = \overline{a} \downarrow \overline{b} = (a \downarrow a) \downarrow (b \downarrow b)$$

> **Teorema (Conmutatividad):**[]{#conmut_deriv_eng
> label="conmut_deriv_eng"}
> $$a \uparrow b = b \uparrow a \qquad \text{y} \qquad a \downarrow b = b \downarrow a$$

> **Teorema (Comportamiento con las
> constantes):**[]{#constantes_deriv_eng label="constantes_deriv_eng"}
> $$\begin{align*}
>     a \uparrow 1 &= \overline{a} \qquad & a \downarrow 0 &= \overline{a} \\
>     a \uparrow 0 &= 1 \qquad & a \downarrow 1 &= 0
> \end{align*}$$

> **Teorema (Ausencia de Asociatividad):**[]{#no_asoc_deriv_eng
> label="no_asoc_deriv_eng"}
> $$(a \uparrow b) \uparrow c \neq a \uparrow (b \uparrow c) \qquad \text{y} \qquad (a \downarrow b) \downarrow c \neq a \downarrow (b \downarrow c)$$

> **Definicion (NAND y NOR de 3 entradas):**[]{#n_entradas_eng
> label="n_entradas_eng"}
> $$\uparrow(a,b,c) = \overline{a \cdot b \cdot c} \qquad \text{y} \qquad \downarrow(a,b,c) = \overline{a + b + c}$$

> **Teorema (NAND/NOR múltiple vs cascada
> binaria):**[]{#multiple_vs_binaria_eng
> label="multiple_vs_binaria_eng"} $$\begin{align*}
>     \uparrow(a,b,c) &\neq (a \uparrow b) \uparrow c \qquad & \uparrow(a,b,c) &\neq a \uparrow (b \uparrow c) \\
>     \downarrow(a,b,c) &\neq (a \downarrow b) \downarrow c \qquad & \downarrow(a,b,c) &\neq a \downarrow (b \downarrow c)
> \end{align*}$$

### Comportamiento de los Operadores XOR y XNOR {#comportamiento-de-los-operadores-xor-y-xnor-1 .unnumbered}

> **Definicion (Definición de XOR y XNOR):**[]{#def_xor_xnor_eng
> label="def_xor_xnor_eng"}
> $$a \oplus b = (a \cdot \overline{b}) + (\overline{a} \cdot b) \qquad \text{y} \qquad a \odot b = \overline{a \oplus b} = (a \cdot b) + (\overline{a} \cdot \overline{b})$$

> **Teorema (Conmutatividad):**[]{#conmut_xor_eng
> label="conmut_xor_eng"}
> $$a \oplus b = b \oplus a \qquad \text{y} \qquad a \odot b = b \odot a$$

> **Teorema (Elementos Neutros e Inversores):**[]{#neutros_xor_eng
> label="neutros_xor_eng"} $$\begin{align*}
>     a \oplus 0 &= a \qquad & a \odot 1 &= a \\
>     a \oplus 1 &= \overline{a} \qquad & a \odot 0 &= \overline{a}
> \end{align*}$$

> **Teorema (Elemento Inverso de sí mismo (Grupo
> Abeliano)):**[]{#idemp_nula_eng label="idemp_nula_eng"}
> $$a \oplus a = 0 \qquad \text{y} \qquad a \odot a = 1$$

> **Teorema (Propiedades de Negación):**[]{#neg_xor_eng
> label="neg_xor_eng"}
> $$\overline{a \oplus b} = \overline{a} \oplus b = a \oplus \overline{b} = a \odot b$$
> $$\overline{a \odot b} = \overline{a} \odot b = a \odot \overline{b} = a \oplus b$$

> **Teorema (Asociatividad y Generalización):**[]{#asoc_gen_xor_eng
> label="asoc_gen_xor_eng"} Ambos operadores son asociativos:
> $$a \oplus (b \oplus c) = (a \oplus b) \oplus c \qquad \text{y} \qquad a \odot (b \odot c) = (a \odot b) \odot c$$
> Lo cual permite su generalización a un número arbitrario $n$ de
> entradas:
> $$\bigoplus_{i=1}^{n} x_i = x_1 \oplus x_2 \oplus \dots \oplus x_n \qquad \text{y} \qquad \bigodot_{i=1}^{n} x_i = x_1 \odot x_2 \odot \dots \odot x_n$$

> **Teorema (Distributividad con el producto y la
> suma):**[]{#dist_xor_eng label="dist_xor_eng"}
> $$a \cdot (b \oplus c) = (a \cdot b) \oplus (a \cdot c) \qquad \text{y} \qquad a + (b \odot c) = (a + b) \odot (a + c)$$

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

# Familias Comerciales y Catálogo (Serie 74xx)

Este anexo sirve como manual técnico de referencia rápida para el
laboratorio de electrónica digital. Tras haber estudiado los límites
teóricos del hardware en el Capítulo
[\[ch:familias\]](#ch:familias){reference-type="ref"
reference="ch:familias"}, aquí abordaremos cómo extraer dicha
información de los manuales oficiales del fabricante y presentaremos la
disposición de pines (pinouts) de los circuitos integrados más
habituales.

## Anatomía de un Datasheet

Un *Datasheet* (Hoja de Características) es el contrato vinculante entre
el fabricante (Texas Instruments, Nexperia, ON Semiconductor, etc.) y el
ingeniero diseñador. Cuando abras el PDF oficial de una puerta (por
ejemplo, el SN74LS00), debes buscar inmediatamente tres tablas críticas:

1.  **Absolute Maximum Ratings (Condiciones Máximas Absolutas):** Estos
    son los límites destructivos. Si superas el voltaje o la temperatura
    indicados aquí, el encapsulado de silicio se fundirá o sufrirá daños
    irreversibles. *Jamás se debe diseñar un circuito operando en esta
    tabla*.

2.  **Recommended Operating Conditions (Condiciones Recomendadas):**
    Esta es la zona segura. Indica los voltajes de alimentación
    nominales (ej. $V_{CC} = 5\text{V} \pm 5\%$) y las temperaturas de
    trabajo donde el fabricante garantiza que la puerta se comportará
    tal y como prometen las matemáticas.

3.  **Electrical Characteristics (Características Eléctricas):** Aquí se
    encuentran los parámetros estudiados previamente
    ($V_{IH}, V_{IL}, I_{OH}, I_{OL}$). Es vital revisar la fila
    denominada *Test Conditions* para saber bajo qué carga de corriente
    o temperatura el fabricante midió esos valores.

## Catálogo de Circuitos Integrados (Serie 74xx)

Los integrados clásicos suelen presentarse en formato *Dual In-line
Package* (DIP), típicamente de 14 o 16 pines. **Regla de oro del
empaquetado DIP:** Posicionando la muesca de plástico en forma de
semicírculo mirando hacia \"arriba\" o \"izquierda\", el Pin 1 es
siempre el primero de la parte inferior izquierda. Se cuenta en sentido
antihorario. Generalmente, el último pin de abajo a la derecha es la
conexión a Tierra (GND), y el pin superior derecho es la alimentación
positiva ($V_{CC}$).

A continuación, se listan integrados fundamentales para montar circuitos
combinacionales.

### Puertas Básicas

**74LS00 / 74HC00: Cuatro puertas NAND de 2 entradas (Quad 2-Input
NAND)** Se trata del chip más famoso de la historia digital. Contiene
cuatro puertas independientes. Pines de alimentación típicos: 7 (GND) y
14 ($V_{CC}$).

**74LS04 / 74HC04: Seis Inversores (Hex Inverter)** Un empaquetado de 14
pines que aloja seis puertas NOT, vital para generar el complemento
matemático de las variables antes de introducirlas a otras etapas
lógicas.

### Circuitos Combinacionales Estándar MSIs

**74LS138 / 74HC138: Decodificador/Demultiplexor 3 a 8** Permite
decodificar 3 bits de dirección ($A, B, C$) para seleccionar una de 8
salidas posibles. Característica fundamental: sus salidas son *activas a
baja* (el cable seleccionado baja a cero voltios, el resto se queda en
uno). Dispone de 3 pines de habilitación (*Enable*) que facilitan
conectar varios chips en cascada para decodificar más bits.

**74HC157: Multiplexor Cuádruple 2 a 1** El opuesto del decodificador.
Selecciona entre dos autobuses de datos de 4 bits ($A$ o $B$) utilizando
un único pin selector común, enviando la información elegida a un bus de
salida único $Y.$

**74HC283: Sumador Completo de 4 bits (4-bit Full Adder)** Realiza la
suma aritmética pura de dos números binarios de 4 bits. Cuenta con
entrada de acarreo ($C_{in}$) y salida de acarreo final ($C_{out}$) para
encadenar aritméticamente múltiples sumadores si se desea procesar
números de 8 o 16 bits en hardware.

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
