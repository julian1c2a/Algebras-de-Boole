# Desarrollo del Álgebra de Boole: Postulados de Huntington

## Notas para el documento:
- **Fase inicial (Signatura de Retículo)**: Utilizaremos los símbolos $\vee$ (supremo/join), $\wedge$ (ínfimo/meet), $\bot$ (elemento mínimo) y $\top$ (elemento máximo) para no llevar a engaño con los símbolos aritméticos habituales.
- **Transición a Notación Digital**: Con el paso de los párrafos, evolucionaremos hacia la notación clásica de sistemas digitales ($+$, $\cdot$, $0$, $1$).
- Introducción a Edward Vermilye Huntington y su formulación de 1904.
    - Los 6 postulados fundamentales (clausura, elemento neutro, conmutatividad, distributividad, complementario, y cardinalidad).

Empezamos pos los pre-axiomas, ¿sobre qué estamos trabajando?
Un conjunto $\mathbb{B}$ junto a un par de operaciones binarias. <!-- Nota a Antigravity: poner alguna clase de nota para indicar que es un conjunto. Usar algo al estilo EsConjunto(\mathbb{B}) -->
Ese conjunto ha de cumplir que tiene dos elementos que llamaremos constantes, tales que $\bot \in \mathbb{B} $ y $\top \in \mathbb{B}$. En principio no decimos nada de la igualdad de esas constantes o no. <!-- Nota a Antigravity: poner una nota para nombrar a estos elementos, es decir, \bot y \top -->
Además vamos a definir dos operaciones binarias internas que denotaremos $\vee, \wedge$ y que satisfacen que son funciones:
$\vee : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ <!-- Nota a Antigravity: poner nota Operación Binaria Interna -->
$\wedge : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ <!-- Nota a Antigravity: poner nota Operación Binaria Interna -->
Esto quiere decir que
$\forall \lang a,b \rang \in \mathbb{B} \times \mathbb{B}$, $\exists! c \in \mathbb{B}, a \vee b = c$ y $\forall \lang a,b\rang \in \mathbb{B} \times \mathbb{B}$, $\exists! d \in \mathbb{B}, a \wedge b = d$.
Para poder usarlo con más seguridad y flexibilidad vamos a poner nombre a cada uno de los conceptos anteriores, para todo par existe imagen en $\mathbb{B}$. <!-- Nota a Antigravity: poner nota de existencia de la imagen, una para \vee y otra para \wedge -->, para un par solo existe una imagen, esto es si $a \vee b = c$ y $a \vee b = d$ entonces $c = d$. <!-- Nota a Antigravity: poner nota de unicidad de la imagen, una para \vee y otra para \wedge -->.

Cada uno de los prerequisitos debería tener un nombre corto con la idea de usarlo en las pruebas.

Texto para LaTeX:

1. \textbf{Elemento neutro $\vee$:} $\forall a \in \mathbb{B}$ se tiene que $a \vee \bot = a$. <!-- Nota a Antigravity: poner nota corta del estilo de $ElemNeu_\vee$ -->
2. \textbf{Elemento neutro $\wedge$:} $\forall a \in \mathbb{B}$ se tiene que $a \wedge \top = a$. <!-- Nota a Antigravity: poner nota corta del estilo de $ElemNeu_\wedge$ -->
3. \textbf{Conmutatividad $\vee$:} $\forall a, b \in \mathbb{B}$ se tiene que $a \vee b = b \vee a$. <!-- Nota a Antigravity: poner nota corta del estilo de $Comm_\vee$ -->
4. \textbf{Conmutatividad $\wedge$:} $\forall a, b \in \mathbb{B}$ se tiene que $a \wedge b = b \wedge a$. <!-- Nota a Antigravity: poner nota corta del estilo de $Comm_\wedge$ -->
5. \textbf{Distributividad $\vee$ sobre $\wedge$:} $\forall a, b, c \in \mathbb{B}$ se tiene que $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$. <!-- Nota a Antigravity: poner nota corta del estilo de $Dist_\vee$ -->
6. \textbf{Distributividad $\wedge$ sobre $\vee$:} $\forall a, b, c \in \mathbb{B}$ se tiene que $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$. <!-- Nota a Antigravity: poner nota corta del estilo de $Dist_\wedge$ -->
7. \textbf{Complementario:} $\forall a \in \mathbb{B} \exists b \in \mathbb{B}$ se tiene que $a \vee b = \top$ <!-- Nota a Antigravity: poner nombre corto como $Comp_\vee$ --> y $a \wedge b = \bot$ <!-- Nota a Antigravity: poner nombre corto como $Comp_\wedge$ -->.

   <!-- Nota a Antigravity: En las pruebas vamos a poner la siguiente estructura , cuando se pueda ir en una línea de cálculo de igualdades de una punta a la otra, la estructura será el nuevo término de la igualdad y el axioma usado en esa transformación por línea -->

- Teoremas principales derivados.

Comenzaremos por Idempotencia.

  $\forall a \in \mathbb{B}, \quad a \vee a = a \quad (Idemp_{\vee})$ <!-- La llamaremos Idemp_∨ -->

  $\forall a \in \mathbb{B}, \quad a \wedge a = a \quad (Idemp_{\wedge})$ <!-- La llamaremos Idemp_∧ -->

Unicidad de los elementos neutros.

  $\exists! e \in \mathbb{B}, \forall a \in \mathbb{B}, a \vee e = a \Rightarrow e = \bot \quad (Unic_e)$ <!-- La llamaremos Unic_e -->

  $\exists! u \in \mathbb{B}, \forall a \in \mathbb{B}, a \wedge u = a \Rightarrow u = \top \quad (Unic_u)$ <!-- La llamaremos Unic_u -->

<!-- Nota a Antigravity: Empezaremos a ver teoremas que se derivan de los axiomas, siempre pondremos el nombre del teorema y los axiomas usados, como los números de las sentencias, por ejemplo: $ElemNeu_∨, Comm_∨ \implies Idemp_∨$ -->
<!-- Vamos a empezar por los más sencillos, aquellos que salen directamente de los axiomas y de los teoremas precedentes.-->
<!-- Necesitamos un par de teoremas para ecuaciones: por ejemplo $x \vee y = x \wedge y \implies x = y$  $(Equa_{\vee,\wedge})$ -->
<!-- Unicidad de los complementos y complemento del complemento, no sé muy bien el orden de estos últimos para que sea lo más simpel posible -->
<!-- Ahora hay otro sobre ecuaciones, usando el hecho de que que la negación (hay definirla previamente) es única. a vee b = a vee c y a vee not b = a vee not c implica b = c. $(Equa\vee\neg)$ -->
<!-- Ahora es el momento de las propiedades de retículo $a \vee b = a \implies a \wedge b = b$ y viceversa, la llamaremos $Prop_{\vee,\wedge}$. -->
<!-- Elementos absorventes \top y \bot para \vee y \wedge respectivamente, su nombre podría ser $Abs_{\vee,\wedge}$ o algo por el estilo -->
<!-- Propiedades de absorción $(Abs_{\vee,\wedge})$-->
<!-- Teoremas de de Morgan $(Mor_{\vee,\wedge})$ -->

Álgebra Trivial:
- Condición de Álgebra Trivial: $\bot = \top \implies \mathbb{B} = \{\top\} = \{\bot\}$
- Complemento idéntico implica Álgebra Trivial: $\exists a \in \mathbb{B}, a' = a \implies \mathbb{B} = \{\top\} = \{\bot\}$
- Conclusiones.

(Ve guardando este archivo, y yo me encargaré de pasarlo a LaTeX)
