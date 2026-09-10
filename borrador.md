# Desarrollo del Álgebra de Boole: Postulados de Huntington

## Notas para el documento:
- **Fase inicial (Signatura de Retículo)**: Utilizaremos los símbolos $\vee$ (supremo/join), $\wedge$ (ínfimo/meet), $\bot$ (elemento mínimo) y $\top$ (elemento máximo) para no llevar a engaño con los símbolos aritméticos habituales.
- **Transición a Notación Digital**: Con el paso de los párrafos, evolucionaremos hacia la notación clásica de sistemas digitales ($+$, $\cdot$, $0$, $1$).
- Introducción a Edward Vermilye Huntington y su formulación de 1904.
    - Los 6 postulados fundamentales (clausura, elemento neutro, conmutatividad, distributividad, complementario, y cardinalidad).

Empezamos pos los pre-axiomas, ¿sobre qué estamos trabajando?
Un conjunto $\mathbb{B}$ junto a un par de operaciones binarias. <<Nota: poner alguna clase de nota para indicar que es un conjunto. Usar algo al estilo EsConjunto($\mathbb{B}$)\rangle>
Ese conjunto ha de cumplir que tiene dos elementos que llamaremos constantes, tales que $\bot \in \mathbb{B} $ y $\top \in \mathbb{B}$. En principio no decimos nada de la igualdad de esas constantes o no. <<Nota: poner una nota para nombrar a estos elementos, es decir, $\bot$ y $\top$>>
Además vamos a definir dos operaciones binarias internas que denotaremos $\vee, \wedge$ y que satisfacen que son funciones:
$\vee : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ <<Nota: poner nota Operación Binaria Interna>>
$\wedge : \mathbb{B} \times \mathbb{B} \to \mathbb{B}$ <<Nota: poner nota Operación Binaria Interna>>
Esto quiere decir que
$\forall \lang a,b \rang \in \mathbb{B} \times \mathbb{B}$, $\exists! c \in \mathbb{B}, a \vee b = c$ y $\forall \lang a,b\rang \in \mathbb{B} \times \mathbb{B}$, $\exists! d \in \mathbb{B}, a \wedge b = d$.
Para poder usarlo con más seguridad y flexibilidad vamos a poner nombre a cada uno de los conceptos anteriores, para todo par existe imagen en $\mathbb{B}$. <<Nota: poner nota de existencia de la imagen, una para $\vee$ y otra para $\wedge$>>, para un par solo existe una imagen, esto es si $a \vee b = c$ y $a \vee b = d$ entonces $c = d$. <<Nota: poner nota de unicidad de la imagen, una para $\vee$ y otra para $\wedge$>>.

Cada uno de los prerequisitos debería tener un nombre corto con la idea de usarlo en las pruebas.

Texto para LaTeX:

1. \textbf{Elemento neutro $\vee$:} $\forall a \in \mathbb{B}$ se tiene que $a \vee \bot = a$. <<Nota: poner nota corta del estilo de $ElemNeu_\vee$>>
2. \textbf{Elemento neutro $\wedge$:} $\forall a \in \mathbb{B}$ se tiene que $a \wedge \top = a$. <<Nota: poner nota corta del estilo de $ElemNeu_\wedge$>>
3. \textbf{Conmutatividad $\vee$:} $\forall a, b \in \mathbb{B}$ se tiene que $a \vee b = b \vee a$. <<Nota: poner nota corta del estilo de $Comm_\vee$>>
4. \textbf{Conmutatividad $\wedge$:} $\forall a, b \in \mathbb{B}$ se tiene que $a \wedge b = b \wedge a$. <<Nota: poner nota corta del estilo de $Comm_\wedge$>>
5. \textbf{Distributividad $\vee$ sobre $\wedge$:} $\forall a, b, c \in \mathbb{B}$ se tiene que $a \vee (b \wedge c) = (a \vee b) \wedge (a \vee c)$. <<Nota: poner nota corta del estilo de $Dist_\vee$>>
6. \textbf{Distributividad $\wedge$ sobre $\vee$:} $\forall a, b, c \in \mathbb{B}$ se tiene que $a \wedge (b \vee c) = (a \wedge b) \vee (a \wedge c)$. <<Nota: poner nota corta del estilo de $Dist_\wedge$>>
7. \textbf{Complementario:} $\forall a \in \mathbb{B} \exists b \in \mathbb{B}$ se tiene que $a \vee b = \top$ <<Nota: poner nombre corto como $Comp_\vee$>> y $a \wedge b = \bot$ <<Nota: poner nombre corto como $Comp_\wedge$>>.

- Teoremas principales derivados.
- Conclusiones.

(Ve guardando este archivo, y yo me encargaré de pasarlo a LaTeX)
