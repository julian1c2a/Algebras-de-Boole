$$
\gdef\symdiff{\mathbin{\vartriangle}}
\gdef\llbracket{\lbrack\!\lbrack}
\gdef\rrbracket{\rbrack\!\rbrack}
\gdef\triangleq{\stackrel{\mathrm{def}}{=}}
$$

# Independencia de los axiomas de Huntington de 1904 (Opcional)

Esta sección explora la independencia lógica de los postulados
propuestos por Edward V. Huntington en 1904.[^1]

Para esto demostrar que los axiomas antes dados son independientes entre
sí, primero daremos un modelo consistente y sencillo, en el que haremos
variaciones y obtendremos modelos (ejemplos) de sistemas que cumplan
todos los axiomas excepto uno de ellos. Si se logra quedará claro que no
podemos deducir el axioma fallido del resto de axiomas que sí que se
cumplen: el axioma fallido es lógicamente independiente del resto de
axiomas. Esto es fácil de conseguir, comenzando con modelos de álgebras
con base en un conjunto de dos elementos
${\ensuremath{\mathbb{B}}}_2 = \ensuremath{\{0,1\}}$. En esto copiamos
los modelos dados por Huntington en su artículo de 1904.

## Modelo mínimo de álgebra de Boole.

Definimos: $$\begin{flalign}
{\ensuremath{\mathbb{B}}}_2 &\ensuremath{\stackrel{\mathsf{def}}{{}={}}}\ensuremath{\{0,1\}} = \ensuremath{\{0\}} \cup \ensuremath{\{1\}} \\
0 &\ensuremath{\stackrel{\mathsf{def}}{{}={}}}\emptyset \\
1 &\ensuremath{\stackrel{\mathsf{def}}{{}={}}}\ensuremath{\{\emptyset\}} \cup \ensuremath{\{ \ensuremath{\{ \emptyset \}} \}} = \ensuremath{\{ \emptyset,
\ensuremath{\{ \emptyset \}} \}} \\
0 &\;\in\; 1 \\
0 &\;\subsetneq\; 1 \\
0 &\;\neq\; 1 \\
\end{flalign}$$ $$\begin{flalign}
\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}} &:  {\ensuremath{\mathbb{B}}}_2 \times {\ensuremath{\mathbb{B}}}_2{\qquad}\ensuremath{\longrightarrow}{\qquad} {\ensuremath{\mathbb{B}}}_2\\
\end{flalign}$$ $$\begin{flalign}
\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}} &:: \left({0,0}\right) {\qquad} \mapsto {\qquad} 0\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}} &:: \left({0,1}\right) {\qquad} \mapsto {\qquad} 1\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}} &:: \left({1,0}\right) {\qquad} \mapsto {\qquad} 1\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}} &:: \left({1,1}\right) {\qquad} \mapsto {\qquad} 1
\end{flalign}$$ $$\begin{flalign}
\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}} &:  {\ensuremath{\mathbb{B}}}_2 \times {\ensuremath{\mathbb{B}}}_2{\qquad}\ensuremath{\longrightarrow}{\qquad} {\ensuremath{\mathbb{B}}}_2\\
\end{flalign}$$ $$\begin{flalign}
\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}} &:: \left({0,0}\right) {\qquad} \mapsto {\qquad} 0\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}} &:: \left({0,1}\right) {\qquad} \mapsto {\qquad} 0\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}} &:: \left({1,0}\right) {\qquad} \mapsto {\qquad} 0\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}} &:: \left({1,1}\right) {\qquad} \mapsto {\qquad} 1
\end{flalign}$$ $$\begin{flalign}
\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}} &:  {\ensuremath{\mathbb{B}}}_2 {\qquad} \ensuremath{\longrightarrow}{\qquad} {\ensuremath{\mathbb{B}}}_2
\end{flalign}$$ $$\begin{flalign}
\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}} &:: 0 {\qquad} \mapsto {\qquad} 1\\
\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}} &:: 1 {\qquad} \mapsto {\qquad} 0
\end{flalign}$$

El conjunto ${\ensuremath{\mathbb{B}}}_2$ es conjunto en **ZF**, desde
el momento que la el axioma de unión nos asegura que
${\ensuremath{\mathbb{B}}}_2$ es conjunto unión de dos conjuntos de un
solo elemento,
${\ensuremath{\mathbb{B}}}_2 \ensuremath{\stackrel{\mathsf{def}}{{}={}}}{ \ensuremath{\{0\}} } \cup {
\ensuremath{\{1\}} }$. Los elementos
$0 \ensuremath{\stackrel{\mathsf{def}}{{}={}}}\emptyset$ y
$1 \ensuremath{\stackrel{\mathsf{def}}{{}={}}}\ensuremath{\{
\emptyset, \ensuremath{\{ \emptyset \}} \}}$. De nuevo para definir $1$
como conjunto necesitamos el axioma de unión (o de pares no ordenados)
de **ZF**, siendo
$1 \ensuremath{\stackrel{\mathsf{def}}{{}={}}}\ensuremath{\{0\}}\cup\ensuremath{\{\ensuremath{\{0\}}\}}$.
Podemos ver que $0 \cap 1 =
\emptyset$ por lo que $0 \neq 1$. También $0 \in 1$. Todo este párrafo
constituye la satisfacción de los requerimientos VI[^2].

Tal como hemos definido nuestro modelo de álgebra de Boole, lo primero
que queda claro es que
$\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}$ y
$\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}$ son funciones
binarias bien definidas, y esta última es además biyectiva. Luego los
axiomas Ia[^3] y Ib[^4] quedan satisfechos.

Los axiomas IIa[^5] y IIb[^6] (existencia del elemento neutro) quedan
directamente satisfechos por simple inspección de las tablas.

Para el axioma IIa observamos que
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,0}\right)} = 0$
y
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,1}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({1,0}\right)} = 1$
nos muestra el elemento neutro de la suma, el elemento $0$.

Para el axioma IIb observamos que
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({1,0}\right)} =
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({0,1}\right)} = 0$
y
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({1,1}\right)} = 1$
nos muestra el elemento neutro del producto, el elemento $1$.

Para los axiomas de conmutatividad solo hay que observar en la
definición de las funciones binarias
$\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}},\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}: \ensuremath{\mathbb{B}}_2 \times \ensuremath{\mathbb{B}}_2
\ensuremath{\longrightarrow}\ensuremath{\mathbb{B}}_2$, que
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,1}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({1,0}\right)} = 1$
y se cumple IIIa[^7], que
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({0,1}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({1,0}\right)} = 0$
y se cumple IIIb[^8].

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
columna, la suma
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({ \textsf{b} ,
\textsf{c} }\right)}$, y con las columnas siete y ocho: la ocho es un
producto
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{a},\textsf{c}}\right)}$
y la siete otro
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({
\textsf{a} , \textsf{b} }\right)}$. Las columnas centrales, la cinco y
la seis corresponden a todas las valoraciones posibles (y en el mismo
orden de valor de las variables independientes) de las dos expresiones
que queremos comparar, las afirmadas por el postulado IVb[^9]. Podemos
ver que ambas columnas son idénticas, luego se cumple el citado
postulado.

$$\begin{flalign}
\begin{matrix}
\hline
\textsf{a} & \textsf{b} & \textsf{c} &
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{b},\textsf{c}}\right)} &
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{a},\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{b},\textsf{c}}\right)}}\right)} &
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{a},\textsf{b}}\right)},\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{a},\textsf{c}}\right)}}\right)}
&
{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{a},\textsf{b}}\right)}}
&
{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{a},\textsf{c}}\right)}}
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
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{b},\textsf{c}}\right)} &
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{a},\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\textsf{b},\textsf{c}}\right)}}\right)} &
\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{a},\textsf{b}}\right)},\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{a},\textsf{c}}\right)}}\right)}
&
{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{a},\textsf{b}}\right)}}
&
{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({\textsf{a},\textsf{c}}\right)}}
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

Para el axioma V[^10] observamos que
$\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({0}\right)} = 1$
y
$\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({1}\right)} = 0$
y por inspección en las tablas vemos que
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({0}\right)}}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,1}\right)} = 1$
y que
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({0,\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({0}\right)}}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({0,1}\right)} = 0$
cumpliendo para el elemento $0$ se cumple que
$\exists 1 = \ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({0}\right)} \in \ensuremath{\mathbb{B}}_2$
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({1,\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({1}\right)}}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({1,0}\right)} = 1$,
que coincide con la ecuación segunda (ecuación: 2.15) de postulado V y
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({1,\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({1}\right)}}\right)}=\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({1,0}\right)} = 0$
que coincide con la tercera ecuación (ecuación: 2.16) de postulado V, e
igualmente para el elemento $1$,
$\exists 0 = \ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({1}\right)} \in \ensuremath{\mathbb{B}}_2$
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({0}\right)}}\right)} = \ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{s}}}}\left({0,1}\right)} = 1$
(ecuación: 2.15) y
$\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({0,\ensuremath{\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{c}}}}}\left({0}\right)}}\right)} =\ensuremath{\ensuremath{\ensuremath{\boldsymbol{\mathsf{p}}}}\left({0,1}\right)} = 0$
(ecuación: 2.16) de postulado V.

Como las ecuaciones 2.15 y 2.16 se cumplen para $0$ y $1$, esto es,
$\forall x \in \ensuremath{\mathbb{B}}_2$ como se requiere en la
ecuación 2.14, queda satisfecho el postulado V.

## Independencia de la suma está siempre definida.

Modelo en el que solo falla Ia, esto es, que la operación suma no es
operación interna: no es función, pero en el sentido que $1 + 1 \notin
\ensuremath{\mathbb{B}}$.

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

Al ser $1 + 1 = x$, dónde $x$ es ningún elemento de
$\ensuremath{\mathbb{B}}$, o dicho de otro modo,
$1 + 1 \notin \ensuremath{\mathbb{B}}$, vemos que sigue existiendo el
elemento neutro de la suma, $0$, que la suma sigue siendo conmutativa y
las distributivas siguen valiendo mientras la suma tenga sentido
(mientras no aparezca $x$). El complementario de $0$ es $1$ y el de $1$
es $0$.

## Independencia de la unicidad de la definición de la suma.

Modelo en el que no se cumple Ia, en el sentido que $1 + 1
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

## Independencia de el producto está siempre definido.

Modelo en el que solo falla Ib, esto es, que la operación producto no es
operación interna: no es función. Este es el caso en que
$0 \cdot 0 \notin \ensuremath{\mathbb{B}}$. Ponemos en ese caso
$0 \cdot 0 = x$ pero igualmente podríamos haber dejado en blanco ese
lugar.

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

## Independencia de la unicidad de la definición del producto.

Modelo en el que solo falla Ia, esto es, en el sentido que $0
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

## Independencia de la existencia de elemento neutro de la suma.

Modelo en el que solo falla IIa, esto es, la existencia de elemento
neutro en la operación binaria interna suma.

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
\ensuremath{\mathbb{B}}\quad x + y = 0$.

Segundo, existe el elemento neutro del producto: $0 \cdot 1 = 1 \cdot 0
= 0$ y $1 \cdot 1 = 1$. Luego se cumple IIb[^11].

La conmutatividad se hace patente al ver las diagonales inversas de las
tablas de operación, que muestran un único valor. $0 + 1 = 1 + 0 = 0$ y
$0 \cdot 1 = 1 \cdot 0 = 0$. Se cumplen IIIa y IIIb.

En cuanto a la distribución del producto sobre la suma, veamos si
podemos comprobarla de forma sencilla:
$a \cdot ( b + c ) = (a \cdot b) + (a \cdot
c)$. Sabemos que $b + c = 0$ siempre, y que, pongamos que $a \cdot b = x
\in \ensuremath{\mathbb{B}}$ y que
$a \cdot c = y \in \ensuremath{\mathbb{B}}$. Ahora bien $x + y = 0$. Así
que todo lo que tenemos que probar es que $a \cdot 0 = 0$, pero esto es
claro en la table del producto. Luego se cumple IVb.

Ahora la distribución de la suma sobre el producto. $a + ( b \cdot c )
= (a + b) \cdot (a + c)$. Sabemos que $a + (b \cdot c) = 0$ siempre, y
que, pongamos que $a + b = 0$ y que $a + c = 0$. Ahora bien $0 \cdot
0 = 0$. Luego se cumple IVa[^12].

Nos queda encontrar un complemento para el $0$. Pero encontrar el
complemento solo tiene sentido si existen los dos elementos neutros,
pero en este caso no existe el neutro de la suma: no tiene sentido
buscar el complementario.

## Independencia de la existencia de elemento neutro del producto.

Exponemos un modelo en el que solo falla IIb, esto es, la existencia de
elemento neutro en la operación binaria interna producto.

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

## Independencia de la conmutatividad de la suma.

Modelo en que la conmutatividad de la suma IIIa no se dá, pero si que se
dan el resto de postulados.

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
\cdot z )$ pero como $0 \cdot x = 0$ obtenemos que la distribución IVb
será verdad para $x = 0$ si $0 = 0 + 0$, cosa que es cierta. Si $x = 1$,
la igualdad a verificar quedaría $1 \cdot ( y + z )
= ( 1 \cdot y ) + ( 1 \cdot z )$ y por IIb queda $y + z  =  y
+ z$ que no es más que la identidad lógica de la igualdad. Se satisface
IVb.

Nos preguntamos por la satisfacción de IVa $x + ( y \cdot z
) = ( x + y ) \cdot ( x + z )$ en el actual modelo. Procedemos como en
el párrafo anterior, por casos. Si $x = 0$ entonces
$x + ( y \cdot z ) = ( x
+ y ) \cdot ( x + z )$ $\Longrightarrow$ $0 + ( y \cdot z ) = ( 0 + y )
\cdot ( 0 + z )$ $\Longrightarrow$ $0 = 0 \cdot 0$ lo que es cierto.
Para el caso $x = 1$, obtenemos $x + ( y \cdot z ) = ( x + y ) \cdot ( x
+ z )$ $\Longrightarrow$ $1 + ( y \cdot z ) = ( 1 + y ) \cdot ( 1 + z
)$ $\Longrightarrow$ $1 = 1 \cdot 1$. Por lo tanto también se verifica
IVa.

Queda comprobado que la conmutatividad de la suma IIIa es independiente
del resto de postulados.

## Independencia de la conmutatividad del producto.

Modelo en que la conmutatividad del producto IIIb no se da, pero, si se
satisfacen el resto de postulados.

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

## Independencia de la distribución de la suma sobre el producto.

El postulado del título no se cumple. Existen valores del modelo
$\exists x \in \ensuremath{\mathbb{B}}$ que no cumplen IVa,
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

Este modelo es virtualmente idéntico al cuerpo sobre
$\ensuremath{\mathbb{Z}}$ de restos módulo 2,
$\ensuremath{\mathbb{Z}}/{\mod2}$. Ese es el cambio que se da en la
suma. Ahora $1
+ 1 = 0$.

Se dan por lo tanto todos los teoremas conocidos incluida la
distribución IVb e incluso sabemos que las operaciones son asociativas.

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
  x=1 \wedge y=0 \wedge z=1 &\Longrightarrow \neg\mathrm{IVa}
\end{flalign}$$

De dónde efectivamente este modelo no distribuye la suma sobre un
producto. Y la independencia de IVa queda probada.

## Independencia de la distribución del producto sobre la suma.

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

## Independencia de la existencia del elemento complementario.

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

[^1]: Edward V. Huntington, *Sets of Independent Postulates for the
    Algebra of Logic*, Transactions of the American Mathematical
    Society, Vol. 5, No. 3 (Jul., 1904), pp. 288-309.

[^2]: Postulado VI: Existen al menos dos elementos distintos en la
    clase.

[^3]: Postulado Ia: Clausura bajo la suma.

[^4]: Postulado Ib: Clausura bajo el producto.

[^5]: Postulado IIa: Existencia de elemento neutro para la suma.

[^6]: Postulado IIb: Existencia de elemento neutro para el producto.

[^7]: Postulado IIIa: Conmutatividad de la suma.

[^8]: Postulado IIIb: Conmutatividad del producto.

[^9]: Postulado IVb: Distributividad del producto sobre la suma.

[^10]: Postulado V: Existencia de elemento complementario.

[^11]: Postulado IIb: Existencia de elemento neutro para el producto.

[^12]: Postulado IVa: Distributividad de la suma sobre el producto.
