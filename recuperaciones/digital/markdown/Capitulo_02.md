Desarrollo de las propiedades generales del álgebra de Boole a partir de
los axiomas de Huntington.

Teoremas de Idempotencia:

Para la suma: $$\forall{x \in B}{{x + x} = x}$$

Prueba:

$${x = {x + 0}} =$$

Elemento neutro de la suma.

$$\forall{y \in \widehat{x}}{{= {x + {({x \cdot y})}}} =}$$

Propiedad del complementario que produce 0.

$$\forall{y \in \widehat{x}}{{= {{({x + x})} \cdot {({x + y})}}} =}$$

Distributiva izquierda de la suma respecto al producto.

$${= {{({x + x})} \cdot 1}} = {}$$

Propiedad del complementario que suma 1.

$$= {x + x}$$

Elemento neutro del producto.

Para el producto: $$\forall{x \in B}{{x \cdot x} = x}$$

Prueba:

$${x = {x \cdot 1}} =$$

Elemento neutro de la suma.

$$\forall{y \in \widehat{x}}{{= {x \cdot {({x + y})}}} =}$$

Propiedad del complementario que produce 0.

$$\forall{y \in \widehat{x}}{{= {{({x \cdot x})} + {({x \cdot y})}}} =}$$

Distributiva izquierda de la suma respecto al producto.

$${= {{({x \cdot x})} + 0}} = {}$$

Propiedad del complementario que suma 1.

$$= {x \cdot x}$$

Elemento neutro del producto.

Teoremas de Absorción:

Para el $$1$$: $$\forall{x \in B}{{x + 1} = 1}$$

Prueba:

$$\forall{y \in \widehat{x}}{{1 = {x + y}} =}$$

Propiedad de sumar $$1$$ de un elemento al sumar con uno de sus
complementarios.

$$\forall{y \in \widehat{x}}{{= {x + {({y \cdot 1})}}} =}$$

Elemento neutro de la multiplicación.

$$\forall{y \in \widehat{x}}{{= {{({x + y})} \cdot {({x + 1})}}} =}$$

Distributividad izquierda de la suma respecto al producto.

$${= {1 \cdot {({x + 1})}}} = {}$$

Propiedad de sumar $$1$$de un elemento con cualquiera de sus
complementarios.

$$= {x + 1}$$

Elemento neutro del producto.

Para el $$0$$: $$\forall{x \in B}{{x \cdot 0} = 0}$$

Prueba:

$$\forall{y \in \widehat{x}}{{0 = {x \cdot y}} =}$$

Propiedad de resultar $$0$$ de un elemento al multiplicar con uno de sus
complementarios.

$$\forall{y \in \widehat{x}}{{= {x \cdot {({y + 0})}}} =}$$

Elemento neutro de la suma.

$$\forall{y \in \widehat{x}}{{= {{({x \cdot y})} + {({x \cdot 0})}}} =}$$

Distributividad izquierda del producto respecto a la suma.

$${= {0 + {({x \cdot 0})}}} = {}$$

Propiedad de resultar $$0$$ de un elemento al multiplicar con uno de sus
complementarios.

$$= {x \cdot 0}$$

Elemento neutro de la suma.

Condición necesaria y suficiente particular para que haya un solo
elemento en el conjunto de Boole:
$$\left( {0_{B} = 1_{B}} \right)\Rightarrow\left( {\text{\#}{B = 1}} \right)$$.

Prueba:

$$$$

Propiedad de absorción de la multiplicación con el $$0$$.

$$$$

Sustituimos el $$0$$ por el $$1$$ gracias a la hipótesis.

$$$$

Elemento neutro de la multiplicación, el $$1$$.

$$B = \left\{ 0 \right\}$$

Desde el punto (1) y (3), mediante la transitividad de la igualdad
equivale.

$${B = \left\{ 0 \right\}} = \left\{ 1 \right\}$$

Por la hipótesis.

Condición necesaria y suficiente general para que haya un solo elemento
en el conjunto de Boole:

$$\left( {0_{B} = 1_{B}} \right)\Rightarrow\left( {\text{\#}{B = 1}} \right)$$.

Prueba:

$$\forall{y \in \widehat{x}}{{1 = {x + y}} =}$$

Axioma de sumar $$1$$ un elemento y su complementario.

$$\exists{x \in \widehat{x}}{}{{= {x + x}} =}$$

Particularización de la fórmula (2) con usando la hipótesis.

$$= x$$

Teorema de Idempotencia de la suma.

$${1 =} = x$$

Fórmulas (1) y (3) aplicando la transitividad de la igualdad.

$$\forall{y \in \widehat{x}}{{0 = {x \cdot y}} =}$$

Axioma de multiplicar $$0$$ un elemento y su complementario.

$$\exists{x \in \widehat{x}}{}{{= {x \cdot x}} =}$$

Particularización de la fórmula (5) con usando la hipótesis.

$${= x}{}$$

Teorema de Idempotencia del producto.

$${0 =} = x$$

Fórmulas (5) y (7) aplicando la transitividad de la igualdad.

$$\left( {{({0 = x})} \land {({1 = x})}} \right)\Rightarrow{({0 = 1})}$$

Fórmulas (4) y (8) y transitividad de la igualdad.

$$0 = 1$$

Puesto que se da la hipótesis de (9) en (4) y (8).

$${B = \left\{ 0 \right\}} = \left\{ 1 \right\}$$

Por el teorema (4) (anterior).

Unicidad del
complementario:$${\forall{a \in B}\forall{\mathit{xy} \in \widehat{a}}}{}{}{}{x = y}$$

Prueba:

$$\forall{x \in B}\forall{a \in \widehat{x}}{1 = {x + a}}$$

Axioma de sumar $$1$$ cualquier elemento y su complementario.

$$y{{= {y \cdot 1}} =}$$

Elemento neutro del producto.

$${= {y \cdot {({x + a})}}} =$$

Particularización de la fórmula (1) (axioma).

$${= {{({y \cdot x})} + {({y \cdot a})}}} =$$

Distributiva izquierda del producto respecto de la suma.

$${= {{({y \cdot x})} + 0}} =$$

Propiedad de los complementarios por la que multiplican $$0$$.

$${= {y \cdot x}} =$$

Propiedad del elemento neutro de la suma.

$${= {x \cdot y}} =$$

Propiedad conmutativa del producto

$${= {{({x \cdot y})} + 0}} =$$

Propiedad del elemento neutro de la suma.

$${= {{({x \cdot y})} + {({x \cdot a})}}} =$$

Propiedad complementaria de $$x\text{y}a$$que multiplican $$0$$

$${= {x \cdot {({y + a})}}} =$$

Distributiva izquierda del producto respecto de la suma.

$${= {x \cdot 1}} =$$

Propiedad complementaria de $$x\text{y}a$$que suma $$1$$

$$= x$$

Elemento neutro del producto

Definimos el elemento complementario de otro, aquel elemento de $$B$$
que
$$\forall{a \in B}\exists!{\overline{a} \in B}{\widehat{a} = \left\{ \overline{a} \right\}}$$,
o dicho de otro modo,
$$\forall{a \in B}\exists!{\overline{a} \in B}{\left( {{a + \overline{a}} = 1} \right) \land \left( {{a \cdot \overline{a}} = 0} \right)}$$,
y este elemento es único.

Complementación doble es identidad:
$$\forall{x \in B}{\overline{\overline{x}} = x}$$.

Prueba:

$$\forall{x \in B}{}{}{}\exists\mathtt{\mathrm{!}}{\overline{x} \in B}{}{}{}{\left( {{x + \overline{x}} = 1} \right) \land \left( {{x \cdot \overline{x}} = 0} \right)}$$

Versión del axioma de complementarios con el teorema (6) y la definición
(7).

$${}{}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{}{}{}{\exists\mathtt{\mathrm{!}}}{\overline{\overline{x}} \in B}{}{}{}{\left( {{\overline{x} + \overline{\overline{x}}} = 1} \right) \land \left( {{\overline{x} \cdot \overline{\overline{x}}} = 0} \right)}$$

Aplicamos particularización de (1) sustituyendo $$x$$ por
$$\overline{x}$$y $$\overline{x}$$ por $$\overline{\overline{x}}$$.

$${}{}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{}{}{}{\exists\mathtt{\mathrm{!}}}{\overline{\overline{x}} \in B}{}{}{}{\left( {{\overline{\overline{x}} + \overline{x}} = 1} \right) \land \left( {{\overline{\overline{x}} \cdot \overline{x}} = 0} \right)}$$

Aplicamos los axiomas de conmutatividad de la suma y el producto a las
fórmulas de (2).

$$\forall{x \in B}\exists!{\overline{x} \in B}\exists!{\overline{\overline{x}} \in B}{\left\{ {x,\overline{\overline{x}}} \right\} \subseteq \widehat{\overline{x}}}$$

De las fórmulas (1) y (3) y del axioma de complementarios se deriva lo
anterior.

$$\overline{\overline{x}} = x$$

Por el teorema (6) de unicidad del complementario.

Unicidad de los neutros:

El neutro para la suma es único
$$\forall{e \in B}\left\lbrack {\left\lbrack {\forall{x \in B}{{x + e} = x}} \right\rbrack\Rightarrow\left\lbrack {e = 0} \right\rbrack} \right\rbrack$$

Prueba:

$$\forall{x \in B}{{x + e} = x}$$

Hipótesis.

$${0 + e} = 0$$

Particularización de (1) con el neutro de la suma.

$${e + 0} = 0$$

Axioma de conmutatividad para la suma.

$$0 = {e + 0}$$

Simetría de la igualdad.

$${e + 0} = e$$

Axioma del elemento neutro de la suma.

$${0 =} = e$$

Transitividad de la igualdad en las fórmulas (4) y (5).

El neutro para el producto es único
$$\forall{u \in B}\left\lbrack {\left\lbrack {\forall{x \in B}{{x \cdot u} = x}} \right\rbrack\Rightarrow\left\lbrack {u = 1} \right\rbrack} \right\rbrack$$

Prueba:

$$\forall{x \in B}{{x \cdot u} = x}$$

Hipótesis.

$${1 \cdot u} = 1$$

Particularización de (1) con el neutro del producto.

$${u \cdot 1} = 1$$

Axioma de conmutatividad para el producto.

$$1 = {u \cdot 1}$$

Simetría de la igualdad.

$${u \cdot 1} = u$$

Axioma del elemento neutro del producto.

$${1 =} = u$$

Transitividad de la igualdad en las fórmulas (4) y (5).

Para los elementos $$0y1$$:
$${\overline{0} = 1} \land {\overline{1} = 0}$$

Prueba:

$${{0 + 1} = 1}\text{Elemento neutro de la suma.}$$

$$0{\cdot}1{= 0}\text{Elemento neutro del producto.}$$

Leyes de cancelación:

Para la suma:

$$\forall x,{y \in B}\left\lbrack {\exists{z \in B}\left\lbrack {\left( {{x + z} = {y + z}} \right) \land \left( {{x + \overline{z}} = {y + \overline{z}}} \right)} \right\rbrack} \right\rbrack\Rightarrow{x = y}$$

Prueba:

$${}{}{}\exists{z \in B}{}{}{}{{x + z} = {y + z}}$$

Hipótesis (1).

$${}{}{}\phantom{\exists{z \in B}}{}{}{}{{x + \overline{z}} = {y + \overline{z}}}$$

Hipótesis (2).

$${\left( {x + z} \right) \cdot \left( {x + \overline{z}} \right)} = {\left( {y + z} \right) \cdot \left( {y + \overline{z}} \right)}$$

Por ser el producto aplicación, el multiplicar las expresiones derechas
de las igualdades entre sí y las izquierdas entre sí, no altera la
igualdad.

$${x + \left( {z \cdot \overline{z}} \right)} = {y + \left( {z \cdot \overline{z}} \right)}$$

Por el axioma de distributividad de la suma respecto al producto por la
izquierda.

$${x + 0} = {y + 0}$$

Por la propiedad de resultar $$0$$la multiplicación de un elemento y su
complementario en el axioma de complementarios.

$$x = y$$

Por el axioma del elemento neutro de la suma.

Para el
producto:$$\forall x,{y \in B}\left\lbrack {\exists{z \in B}\left\lbrack {\left( {{x \cdot z} = {y \cdot z}} \right) \land \left( {{x \cdot \overline{z}} = {y \cdot \overline{z}}} \right)} \right\rbrack} \right\rbrack\Rightarrow{x = y}$$

Prueba:

$${}{}{}\exists{z \in B}{}{}{}{{x \cdot z} = {y \cdot z}}$$

Hipótesis (1).

$${}{}{}\phantom{\exists{z \in B}}{}{}{}{{x \cdot \overline{z}} = {y \cdot \overline{z}}}$$

Hipótesis (2).

$${\left( {x \cdot z} \right) + \left( {x \cdot \overline{z}} \right)} = {\left( {y \cdot z} \right) + \left( {y \cdot \overline{z}} \right)}$$

Por ser la suma aplicación, el sumar las expresiones derechas de las
igualdades entre sí y las izquierdas entre sí, no altera la igualdad.

$${x \cdot \left( {z + \overline{z}} \right)} = {y \cdot \left( {z + \overline{z}} \right)}$$

Por el axioma de distributividad del producto respecto de la suma por la
izquierda.

$${x \cdot 1} = {y \cdot 1}$$

Por la propiedad de resultar $$1$$la suma de un elemento y su
complementario en el axioma de complementarios.

$$x = y$$

Por el axioma del elemento neutro de la multiplicación.

Propiedades de simplificación (para retículos en general):

$$\forall x,{y \in B}{{x + {({x \cdot y})}} = x}$$

Prueba:

$${x + {({x \cdot y})}} = {}$$

$${= {{({x \cdot 1})} + {({x \cdot y})}}} =$$

Por ser el $$1$$ el elemento neutro del producto (Axioma).

$${= {x \cdot {({1 + y})}}} =$$

Por el axioma de distributividad del producto respecto de la suma por la
izquierda.

$${= {x \cdot 1}} =$$

Por ser el $$1$$ elemento absorbente en la suma \[Teorema (2.1)\].

$$= x$$

Por ser el $$1$$el elemento neutro del producto (Axioma).

$$\forall x,{y \in B}{{x \cdot {({x + y})}} = x}$$

Prueba:

$${x \cdot {({x + y})}} = {}$$

$${= {{({x + 0})} \cdot {({x + y})}}} =$$

Por ser el $$0$$ el elemento neutro de la suma (Axioma).

$${= {x + {({0 \cdot y})}}} =$$

Por el axioma de distributividad de la suma respecto del producto por la
izquierda.

$${= {x \cdot 1}} =$$

Por ser el $$0$$ elemento absorbente en el producto \[Teorema (2.2)\].

$$= x$$

Por ser el $$0$$el elemento neutro de la suma (Axioma).

Una propiedad muy general (para retículos no sólo para álgebras de
Boole):

$$\forall x,{y \in B}{}{}{}{({{x \cdot y} = y})}\Leftrightarrow{({{x + y} = x})}$$

Prueba:

$${x \cdot y} = y$$

Hipótesis.

$$x = x$$

Verdad universal para la igualdad.

$${{({x \cdot y})} + x} = {y + x}$$

Como la suma es una aplicación, al sumar las expresiones izquierdas
entre si, e idénticamente con las derechas, la igualdad se mantiene.

$${{({y \cdot x})} + x} = {y + x}$$

Propiedad conmutativa del producto (axioma).

$$x = {y + x}$$

Propiedad de simplificación del teorema anterior (11.2).

$${y + x} = x$$

Simetría de la igualdad.

$${x + y} = x$$

Propiedad conmutativa de la suma (axioma).

$${({{x \cdot y} = y})}\Rightarrow{({{x + y} = x})}$$

De (1) hemos derivado (7).

$${x + y} = x$$

Hipótesis.

$$y = y$$

Verdad universal de la igualdad.

$${{({x + y})} \cdot y} = {x \cdot y}$$

Como el producto es aplicación, el multiplicar los términos izquierdos
de las igualdades (9) y (10) entre sí y los derechos de (9) y (10)
idénticamente, se mantiene la igualdad.

$$y = {x \cdot y}$$

Teorema de simplificación inmediatamente anterior (11.1).

$${x \cdot y} = y$$

Por la simetría de la igualdad.

$${({{x + y} = x})}\Rightarrow{({{x \cdot y} = y})}$$

De (9) hemos derivado (13).

$$\begin{matrix}
{{\left( {{({{x + y} = x})}\Rightarrow{({{x \cdot y} = y})}} \right) \land \left( {{({{x \cdot y} = y})}\Rightarrow{({{x + y} = x})}} \right)} ≝} \\
{{≝ {({{x + y} = x})}}\Leftrightarrow{({{x \cdot y} = y})}}
\end{matrix}$$

\(11\) y (14) significan exactamente la definición del "si y solo si".

Otra propiedad de simplificación (Shannon):

$$\forall x,{y \in B}{{{({x + y})} \cdot {({x + \bar{y}})}} = x}$$

Prueba:

$${x = {x + 0}} = {}$$

Por el axioma de elemento neutro de la suma.

$${= {x + {({\overline{y} \cdot y})}}} =$$

Por el axioma de complementarios en su afirmación del producto de
complementarios.

$$= {{({x + \overline{y}})} \cdot {({x + y})}}$$

Por la distributividad de la suma respecto al producto por la izquierda.

$$\forall x,{y \in B}{{{({x \cdot y})} + {({x \cdot \bar{y}})}} = x}$$

Prueba:

$${x = {x + 0}} = {}$$

Por el axioma de elemento neutro de la suma.

$${= {x + {({\overline{y} \cdot y})}}} =$$

Por el axioma de complementarios en su afirmación del producto de
complementarios.

$$= {{({x + \overline{y}})} \cdot {({x + y})}}$$

Por la distributividad de la suma respecto al producto por la izquierda.

Otra propiedad de simplificación más:

Para la suma respecto del producto:
$$\forall x,{y \in B}{}{}{}{{x + {({\overline{x} \cdot y})}} = {x + y}}$$

Prueba:

$${{x + {({\overline{x} \cdot y})}} = {{({x + \overline{x}})} \cdot {({x + y})}}} = {}$$

Por el axioma de distributividad de la suma respecto al producto.

$${= {1 \cdot {({x + y})}}} =$$

Por la propiedad de sumar 1 los complementarios en el axioma de
complementarios.

$$= {x + y}$$

Por el axioma del elemento neutro de la suma.

Para el producto respecto de la
suma:$$\forall x,{y \in B}{}{}{}{{x + {({\overline{x} \cdot y})}} = {x + y}}$$

Prueba:

$${{x \cdot {({\overline{x} + y})}} = {{({x \cdot \overline{x}})} + {({x \cdot y})}}} = {}$$

Por el axioma de distributividad del producto respecto de la suma.

$${= {0 + {({x \cdot y})}}} =$$

Por la propiedad de multiplicar $$0$$ los complementarios en el axioma
de complementarios.

$$= {x \cdot y}$$

Por el axioma del elemento neutro del producto.

Algunos lemas técnicos pre-asociativos útiles:

Asociatividad cuando dos variables se repiten:

Para la
suma:$$\forall{\mathit{xy} \in B}{}{}{}{{{x + y} = {x + {({x + y})}}} = {{({x + x})} + y}}$$

Prueba:

$${{({x + {({x + y})}})} \cdot y} = {}$$

Ponemos una expresión izquierda de una igualdad.

$${= {y \cdot {({x + {({x + y})}})}}} =$$

Por el axioma de conmutatividad del producto.

$${= {{({y \cdot x})} + {({y \cdot {({x + y})}})}}} =$$

Distributividad del producto respecto a la suma por la izquierda.

$${= {{({y \cdot x})} + {({{({y \cdot x})} + {({y \cdot y})}})}}} =$$

Distributividad del producto respecto a la suma por la izquierda.

$${= {{({y \cdot x})} + {({{({y \cdot x})} + y})}}} =$$

Por el teorema de idempotencia del producto.

$${= {{({{({y \cdot x})} + y})} + {({y \cdot x})}}} =$$

Por axioma de conmutatividad de la suma.

$${= {{({y + {({y \cdot x})}})} + {({y \cdot x})}}} =$$

Por axioma de conmutatividad de la suma.

$${= {{({{({y \cdot x})} + y})} + {({y \cdot x})}}} =$$

Por axioma de conmutatividad de la suma.

$${= {{({{({x \cdot y})} + y})} + {({y \cdot x})}}} =$$

Por axioma de conmutatividad del producto.

$${= {y + {({y \cdot x})}}} =$$

Por el teorema de simplificación de la suma respecto al producto.

$${= {{({y \cdot x})} + y}} =$$

Por axioma de conmutatividad de la suma.

$${= {{({x \cdot y})} + y}} =$$

Por axioma de conmutatividad del producto.

$$= y$$

Por el teorema de simplificación de la suma respecto al producto.

$${{({x + {({x + y})}})} \cdot y} = y$$

Fórmulas (1) y (13) por la transitividad de la igualdad.

$${{({x + {({x + y})}})} \cdot x} = {}$$

Ponemos una expresión izquierda de una igualdad.

$${= {{({x \cdot x})} + {({{({x + y})} \cdot x})}}} =$$

Por el axioma de distributividad del producto respecto de la suma.

$${= {{({x \cdot x})} + {({{({y + x})} \cdot x})}}} =$$

Por el axioma de conmutatividad de la suma.

$${= {{({x \cdot x})} + x}} =$$

Teorema de simplificación del producto respecto de la suma.

$$= x$$

Teorema de simplificación del producto respecto de la suma.

$${{({x + {({x + y})}})} \cdot x} = x$$

Fórmulas (15) y (19) y transitividad de la igualdad.

$${}{{x + y} =}$$

$${= {{\lbrack{{({x + {({x + y})}})} \cdot x}\rbrack} + {\lbrack{{({x + {({x + y})}})} \cdot y}\rbrack}}} =$$

Fórmulas (14) y (20) y simetría de la igualdad. De otro lado está que al
ser la suma una aplicación, se puede sumar lado derecho de una igualdad
con el lado derecho de otra y e igualmente sus lados izquierdos, y el
resultado sigue siendo una igualdad.

$${= {{\lbrack{x \cdot {({x + {({x + y})}})}}\rbrack} + {\lbrack{y \cdot {({x + {({x + y})}})}}\rbrack}}} =$$

Axioma de conmutatividad del producto.

$${= {{({x + y})} \cdot {({x + {({x + y})}})}}} =$$

Por el axioma de distributividad por la izquierda del producto respecto
de la suma.

$${= {\left( {{({x + y})} + {({x + y})}} \right) \cdot {({x + {({x + y})}})}}} =$$

Por el teorema de idempotencia de la suma.

$${= {\left( {x + {({x + y})}} \right) \cdot \left( {{({x + y})} + {({x + y})}} \right)}} =$$

Por el axioma de conmutabilidad del producto.

$${= {\left( {{({x + y})} + x} \right) \cdot \left( {{({x + y})} + {({x + y})}} \right)}} =$$

Por el axioma de conmutatividad de la suma.

$${= {{({x + y})} + {({x \cdot {({x + y})}})}}} =$$

Por el axioma de distributividad de la suma respecto al producto.

$${= {{({x + y})} + {({{({x + y})} \cdot x})}}} =$$

Axioma de conmutatividad del producto.

$${= {{({x + y})} + {({{({y + x})} \cdot x})}}} =$$

Axioma de conmutatividad de la suma.

$${= {{({x + y})} + x}} =$$

Teorema de simplificación del producto respecto de la suma.

$$= {x + {({x + y})}}$$

Por el axioma de conmutatividad de la suma.

$${x + y} = {x + {({x + y})}}$$

De las fórmulas (21) y (32) y la transitividad de la igualdad.

$${\left( {x + x} \right) = x}{}$$

Teorema de idempotencia de la suma.

$$y = y$$

Propiedad fundamental de la igualdad.

$${{({x + x})} + y} = {x + y}$$

Al ser la suma una aplicación y sumar los lados derechos de las
igualdades y los lados izquierdos permanece la igualdad.

$${}{{{{({x + x})} + y} = {x + y}} = {x + {({x + y})}}}$$

Concatenación de las fórmulas (36) y (33) por transitividad de la
igualdad.

Para el
producto:$$\forall x,{y \in B}{{{x \cdot y} = {x \cdot {({x \cdot y})}}} = {{({x \cdot x})} \cdot y}}$$

Prueba:

$${{({x \cdot {({x \cdot y})}})} + y} = {}$$

Ponemos una expresión izquierda bien formada de una igualdad.

$${= {y + {({x \cdot {({x \cdot y})}})}}} =$$

Por el axioma de conmutatividad de la suma.

$${= {{({y + x})} \cdot {({y + {({x \cdot y})}})}}} =$$

Distributividad de la suma respecto al producto por la izquierda.

$${= {{({y + x})} \cdot {({{({y + x})} \cdot {({y + y})}})}}} =$$

Distributividad de la suma respecto al producto por la izquierda.

$${= {{({y + x})} \cdot {({{({y + x})} \cdot y})}}} =$$

Por el teorema de idempotencia de la suma.

$${= {{({{({y + x})} \cdot y})} \cdot {({y + x})}}} =$$

Por axioma de conmutatividad del producto.

$${= {{({y \cdot {({y + x})}})} \cdot {({y + x})}}} =$$

Por axioma de conmutatividad del producto.

$${= {{({{({y + x})} \cdot y})} \cdot {({y + x})}}} =$$

Por axioma de conmutatividad del producto.

$${= {{({{({x + y})} \cdot y})} \cdot {({y + x})}}} =$$

Por axioma de conmutatividad de la suma.

$${= {y \cdot {({y + x})}}} =$$

Por el teorema de simplificación del producto respecto a la suma.

$${= {{({y + x})} \cdot y}} =$$

Por axioma de conmutatividad del producto.

$${= {{({x + y})} \cdot y}} =$$

Por axioma de conmutatividad de la suma.

$$= y$$

Por el teorema de simplificación del producto respecto a la suma.

$${{({x \cdot {({x \cdot y})}})} + y} = y$$

Fórmulas (1) y (13) por la transitividad de la igualdad.

$${{({x \cdot {({x \cdot y})}})} + x} = {}$$

Ponemos una expresión izquierda de una igualdad.

$${= {{({x + x})} \cdot {({{({x \cdot y})} + x})}}} =$$

Por el axioma de distributividad de la suma respecto del producto.

$${= {{({x + x})} \cdot {({{({y \cdot x})} + x})}}} =$$

Por el axioma de conmutatividad del producto.

$${= {{({x + x})} \cdot x}} =$$

Teorema de simplificación de la suma respecto del producto.

$$= x$$

Teorema de simplificación del producto respecto de la suma.

$${{({x \cdot {({x \cdot y})}})} + x} = x$$

Fórmulas (15) y (19) y transitividad de la igualdad.

$${}{{x \cdot y} =}$$

$${= {{\lbrack{{({x \cdot {({x \cdot y})}})} + x}\rbrack} \cdot {\lbrack{{({x \cdot {({x \cdot y})}})} + y}\rbrack}}} =$$

Fórmulas (14) y (20) y simetría de la igualdad. De otro lado está que al
ser el producto una aplicación, se puede multiplicar lado derecho de una
igualdad con el lado derecho de otra y e igualmente sus lados
izquierdos, y el resultado sigue siendo una igualdad.

$${= {{\lbrack{x + {({x \cdot {({x \cdot y})}})}}\rbrack} \cdot {\lbrack{y + {({x \cdot {({x \cdot y})}})}}\rbrack}}} =$$

Axioma de conmutatividad de la suma.

$${= {{({x \cdot y})} + {({x \cdot {({x \cdot y})}})}}} =$$

Por el axioma de distributividad por la izquierda de la suma respecto
del producto.

$${= {\left( {{({x \cdot y})} \cdot {({x \cdot y})}} \right) + {({x \cdot {({x \cdot y})}})}}} =$$

Por el teorema de idempotencia del producto.

$${= {\left( {x \cdot {({x \cdot y})}} \right) + \left( {{({x \cdot y})} \cdot {({x \cdot y})}} \right)}} =$$

Por el axioma de conmutabilidad de la suma.

$${= {\left( {{({x \cdot y})} \cdot x} \right) + \left( {{({x \cdot y})} \cdot {({x \cdot y})}} \right)}} =$$

Por el axioma de conmutatividad del producto.

$${= {{({x \cdot y})} \cdot {({x + {({x \cdot y})}})}}} =$$

Por el axioma de distributividad del producto respecto a la suma.

$${= {{({x \cdot y})} \cdot {({{({x \cdot y})} + x})}}} =$$

Axioma de conmutatividad de la suma.

$${= {{({x \cdot y})} \cdot {({{({y \cdot x})} + x})}}} =$$

Axioma de conmutatividad del producto.

$${= {{({x \cdot y})} \cdot x}} =$$

Teorema de simplificación de la suma respecto del producto.

$$= {x \cdot {({x \cdot y})}}$$

Por el axioma de conmutatividad del producto.

$${x \cdot y} = {x \cdot {({x \cdot y})}}$$

De las fórmulas (21) y (32) y la transitividad de la igualdad.

$${\left( {x \cdot x} \right) = x}{}$$

Teorema de idempotencia del producto.

$$y = y$$

Propiedad fundamental de la igualdad.

$${{({x \cdot x})} \cdot y} = {x \cdot y}$$

Al ser el producto una aplicación y multiplicar los lados derechos de
las igualdades y los lados izquierdos permanece la igualdad.

$${}{{{{({x \cdot x})} \cdot y} = {x \cdot y}} = {x \cdot {({x \cdot y})}}}$$

Concatenación de las fórmulas (36) y (33) por transitividad de la
igualdad.

Asociatividad cuando una de las tres variables es la complementaria de
otra:

Para la
suma:$${1 = {\overline{x} + {({x + y})}}} = {{({\overline{x} + x})} + y}$$

Prueba:

$${{({\overline{x} + {({x + y})}})} \cdot x} = {}$$

$$= {{({\overline{x} \cdot x})} + {({{({x + y})} \cdot x})}}$$

$$= {{({\overline{x} \cdot x})} + {({{({x + y})} \cdot x})}}$$

$${= {({{({x + y})} \cdot x})}} =$$

$${= {{({y + x})} \cdot x}} =$$

$$= x$$

$${{({\overline{x} + {({x + y})}})} \cdot x} = {}$$

$${{({\overline{x} + {({x + y})}})} \cdot \overline{x}} = {}$$

$${= {\overline{x} + {({x \cdot y})}}} = {}$$

$$= \overline{x}$$

$${{{({\overline{x} + {({x + y})}})} \cdot \overline{x}} = \overline{x}}{}$$

$${1 = {x + \overline{x}}} = {}$$

$${= {\left\lbrack {\left( {\overline{x} + \left( {x + y} \right)} \right) \cdot x} \right\rbrack \cdot \left\lbrack {\left( {\overline{x} + \left( {x + y} \right)} \right) \cdot \overline{x}} \right\rbrack}} =$$

$${= {\left\lbrack {\left( {\left( {x + y} \right) + \overline{x}} \right) \cdot x} \right\rbrack \cdot \left\lbrack {\left( {\left( {x + y} \right) + \overline{x}} \right) \cdot \overline{x}} \right\rbrack}} =$$

$${= {{({\overline{x} + {({x + y})}})} \cdot {({x + \overline{x}})}}} =$$

$${= {{({\overline{x} + {({x + y})}})} \cdot 1}} =$$

$$= {\overline{x} + {({x + y})}}$$

$${1 = {1 + y}} = {}$$

$$= {{({\overline{x} + x})} + y}$$

$${1 = {\overline{x} + {({x + y})}}} = {}$$

$$= {{({\overline{x} + x})} + y}$$

$${1 = {\overline{x} + {({x + y})}}} = {{({\overline{x} + x})} + y}$$

Para el
producto:$${0 = {\overline{x} \cdot {({x \cdot y})}}} = {{({\overline{x} \cdot x})} \cdot y}$$

Prueba:

$${{({\overline{x} \cdot {({x \cdot y})}})} + x} = {}$$

$${= {x \cdot {({x + y})}}} =$$

$$= x$$

$${{{({\overline{x} \cdot {({x \cdot y})}})} + x} = x}{}$$

$${{({\overline{x} + {({x + y})}})} \cdot \overline{x}} = {}$$

$${= {\overline{x} + {({x \cdot y})}}} = {}$$

$$= \overline{x}$$

$${{{({\overline{x} + {({x + y})}})} \cdot \overline{x}} = \overline{x}}{}$$

$${1 = {x + \overline{x}}} = {}$$

$${= {{({{({\overline{x} + {({x + y})}})} \cdot x})} + {({{({\overline{x} + {({x + y})}})} \cdot \overline{x}})}}} =$$

$${= {{({\overline{x} + {({x + y})}})} \cdot {({x + \overline{x}})}}} =$$

$${= {{({\overline{x} + {({x + y})}})} \cdot 1}} =$$

$$= {\overline{x} + {({x + y})}}$$

$${1 = {1 + y}} = {}$$

$$= {{({\overline{x} + x})} + y}$$

$${1 = {\overline{x} + {({x + y})}}} = {}$$

$$= {{({\overline{x} + x})} + y}$$

$${1 = {\overline{x} + {({x + y})}}} = {{({\overline{x} + x})} + y}$$

Leyes de Morgan:

De la suma en
producto:$$\forall x,{y \in B}{\overline{x+y} = {\overline{x} \cdot \overline{y}}}$$

Prueba:

$${{{{{({x + y})} \cdot {({\overline{x} \cdot \overline{y}})}} = {{({x \cdot {({\overline{x} \cdot \overline{y}})}})} + {({y \cdot {({\overline{x} \cdot \overline{y}})}})}}} = {{({x \cdot {({\overline{x} \cdot \overline{y}})}})} + {({y \cdot {({\overline{y} \cdot \overline{x}})}})}}} = {0 + 0}} = 0$$

$${{{{{({x + y})} + {({\overline{x} \cdot \overline{y}})}} = {{({x + {({\overline{x} \cdot \overline{y}})}})} \cdot {({y + {({\overline{x} \cdot \overline{y}})}})}}} = {{({x + {({\overline{x} \cdot \overline{y}})}})} \cdot {({y + {({\overline{y} \cdot \overline{x}})}})}}} = {1 \cdot 1}} = 1$$

Del producto en
suma:$$\forall x,{y \in B}{}{}{}{\overline{x\cdot y} = {\overline{x} + \overline{y}}}$$

Prueba:

$${{{{{({x \cdot y})} + {({\overline{x} + \overline{y}})}} = {{({x + {({\overline{x} + \overline{y}})}})} \cdot {({y + {({\overline{x} + \overline{y}})}})}}} = {{({x + {({\overline{x} + \overline{y}})}})} \cdot {({y + {({\overline{y} + \overline{x}})}})}}} = {1 \cdot 1}} = 1$$

$${{{{{({x \cdot y})} \cdot {({\overline{x} + \overline{y}})}} = {{({x \cdot {({\overline{x} + \overline{y}})}})} + {({y \cdot {({\overline{x} + \overline{y}})}})}}} = {{({x \cdot {({\overline{x} + \overline{y}})}})} + {({y \cdot {({\overline{y} + \overline{x}})}})}}} = {0 \cdot 0}} = 0$$

Transformación de la suma y el producto mediante Morgan y doble
complemento:

De la suma en
producto:$$\forall x,{y \in B}{}{}{}{{x + y} = \overline{\overline{x}\cdot\overline{y}}}$$

Prueba:

$${\{{\overline{x+y} = {\overline{x} \cdot \overline{y}}}\}}\Rightarrow{\{{{x + y} = \overline{\overline{x}\cdot\overline{y}}}\}}$$

Del producto en
suma:$$\forall x,{y \in B}{}{}{}{{x \cdot y} = \overline{\overline{x}+\overline{y}}}$$

Prueba:

$${\{{\overline{({x\cdot y})} = {\overline{x} + \overline{y}}}\}}\Rightarrow{\{{{x \cdot y} = \overline{\overline{x}+\overline{y}}}\}}$$

Asociatividad de las operaciones binarias:

De la suma:
$$\forall x,y,{z \in B}{}{}{}{{{({x + y})} + z} = {x + {({y + z})}}}$$

Prueba:

$$a{: = {({{({x + y})} + z})}}$$

$$b{: = {({x + {({y + z})}})}}$$

$$\overline{b}{}{}{}{= {({\overline{x} \cdot {({\overline{y} \cdot \overline{z}})}})}}$$

$${\lbrack\mathbf{1}\rbrack}{{a + \overline{b}} =}$$

$${= {{({a + \overline{x}})} \cdot {({{({a + \overline{y}})} \cdot {({a + \overline{z}})}})}}} =$$

$${= {{({{({{({x + y})} + z})} + \overline{x}})} \cdot {({{({{({{({x + y})} + z})} + \overline{y}})} \cdot {({{({{({x + y})} + z})} + \overline{z}})}})}}} =$$

$${= {{({{({{({x + y})} + z})} + \overline{x}})} \cdot {({{({{({{({x + y})} + z})} + \overline{y}})} \cdot 1})}}} =$$

$${= {{({{({{({x + y})} + z})} + \overline{x}})} \cdot {({{({{({x + y})} + z})} + \overline{y}})}}} =$$

$${= {{({{({x + y})} + z})} + {({\overline{x} \cdot \overline{y}})}}} =$$

$${= {{({{({x + y})} + z})} + \overline{({x+y})}}} =$$

$${= {\overline{({x+y})} + {({{({x + y})} + z})}}} =$$

$$= 1$$

$${\lbrack\mathbf{2}\rbrack}{{a \cdot \overline{b}} =}$$

$${= {{({a \cdot \overline{x}})} + {({{({a \cdot \overline{y}})} + {({a \cdot \overline{z}})}})}}} =$$

$${= {{({{({{({x \cdot y})} \cdot z})} \cdot \overline{x}})} + {({{({{({{({x \cdot y})} \cdot z})} \cdot \overline{y}})} + {({{({{({x \cdot y})} \cdot z})} \cdot \overline{z}})}})}}} =$$

$${= {{({{({{({x \cdot y})} \cdot z})} \cdot \overline{x}})} + {({{({{({{({x \cdot y})} \cdot z})} \cdot \overline{y}})} + 0})}}} =$$

$${= {{({{({{({x \cdot y})} \cdot z})} \cdot \overline{x}})} + {({{({{({x \cdot y})} \cdot z})} \cdot \overline{y}})}}} =$$

$${= {{({{({x \cdot y})} \cdot z})} \cdot {({\overline{x} + \overline{y}})}}} =$$

$${= {{({{({x \cdot y})} \cdot z})} \cdot \overline{({x\cdot y})}}} =$$

$${= {\overline{({x\cdot y})} \cdot {({{({x \cdot y})} \cdot z})}}} =$$

$$= 0$$

$$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}\mathit{que}{}{}{}{\overline{a} = \overline{b}}{}\Rightarrow{}{a = b}$$

De la operación producto:
$$\forall x,y,{z \in B}{}{}{}{{{({x \cdot y})} \cdot z} = {x \cdot {({y \cdot z})}}}$$

Prueba:

$$a{: = {({{({x \cdot y})} \cdot z})}}$$

$$b{: = {({x \cdot {({y \cdot z})}})}}$$

$$\overline{b}{}{}{}{= {({\overline{x} + {({\overline{y} + \overline{z}})}})}}$$

$${\lbrack\mathbf{1}\rbrack}{{a \cdot \overline{b}} =}$$

$${= {{({a \cdot \overline{x}})} + {({{({a \cdot \overline{y}})} + {({a \cdot \overline{z}})}})}}} =$$

$${= {{({{({{({x \cdot y})} \cdot z})} \cdot \overline{x}})} + {({{({{({{({x \cdot y})} \cdot z})} \cdot \overline{y}})} + {({{({{({x \cdot y})} \cdot z})} \cdot \overline{z}})}})}}} =$$

$${= {{({{({{({x \cdot y})} \cdot z})} \cdot \overline{x}})} + {({{({{({{({x \cdot y})} \cdot z})} \cdot \overline{y}})} + 0})}}} =$$

$${= {{({{({{({x \cdot y})} \cdot z})} \cdot \overline{x}})} + {({{({{({x \cdot y})} \cdot z})} \cdot \overline{y}})}}} =$$

$${= {{({{({x \cdot y})} \cdot z})} \cdot {({\overline{x} + \overline{y}})}}} =$$

$${= {{({{({x \cdot y})} \cdot z})} \cdot \overline{({x\cdot y})}}} =$$

$${= {\overline{({x\cdot y})} \cdot {({{({x \cdot y})} \cdot z})}}} =$$

$$= 0$$

$${\lbrack\mathbf{2}\rbrack}{{a + \overline{b}} =}$$

$${= {{({a + \overline{x}})} \cdot {({{({a + \overline{y}})} \cdot {({a + \overline{z}})}})}}} =$$

$${= {{({{({{({x + y})} + z})} + \overline{x}})} \cdot {({{({{({{({x + y})} + z})} + \overline{y}})} \cdot {({{({{({x + y})} + z})} + \overline{z}})}})}}} =$$

$${= {{({{({{({x + y})} + z})} + \overline{x}})} \cdot {({{({{({{({x + y})} + z})} + \overline{y}})} \cdot 1})}}} =$$

$${= {{({{({{({x + y})} + z})} + \overline{x}})} \cdot {({{({{({x + y})} + z})} + \overline{y}})}}} =$$

$${= {{({{({x + y})} + z})} + {({\overline{x} \cdot \overline{y}})}}} =$$

$${= {{({{({x + y})} + z})} + \overline{({x+y})}}} =$$

$${= {\overline{({x+y})} + {({{({x + y})} + z})}}} =$$

$$= 1$$

$$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}\mathit{que}{}{}{}{\overline{a} = \overline{b}}{}\Rightarrow{}{a = b}$$

Propiedad de simplificación de Quine:

$${{\left( {x \cdot y} \right) + \left( {x \cdot \overline{z}} \right)} + \left( {y \cdot z} \right)} = {\left( {x \cdot \overline{z}} \right) + \left( {y \cdot z} \right)}$$

Prueba:

$${{\left( {x \cdot y} \right) + \left( {x \cdot \overline{z}} \right)} + \left( {y \cdot z} \right)} =$$

$${} = {{\left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{x \cdot y} \cdot \overline{z}} \right)} \right) + \left( {\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {{x \cdot \overline{y}} \cdot \overline{z}} \right)} \right)} + \left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{\overline{x} \cdot y} \cdot z} \right)} \right)}$$

$${} = {{\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {{x \cdot \overline{y}} \cdot \overline{z}} \right)} \right)} + \left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{\overline{x} \cdot y} \cdot z} \right)} \right)}$$

$${} = {\left( {\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {{x \cdot \overline{y}} \cdot \overline{z}} \right)} \right) + \left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{\overline{x} \cdot y} \cdot z} \right)} \right)}$$

$${} = {\left( {x \cdot \overline{z}} \right) + \left( {y \cdot z} \right)}$$

$${{\left( {x + y} \right) \cdot \left( {x + \overline{z}} \right)} \cdot \left( {y + z} \right)} = {\left( {x + \overline{z}} \right) \cdot \left( {y + z} \right)}$$

Prueba:

$${{\left( {x + y} \right) \cdot \left( {x + \overline{z}} \right)} \cdot \left( {y + z} \right)} =$$

$${} = {{\left( {\left( {{x + y} + z} \right) \cdot \left( {{x + y} + \overline{z}} \right)} \right) \cdot \left( {\left( {{x + y} + \overline{z}} \right) \cdot \left( {{x + \overline{y}} + \overline{z}} \right)} \right)} \cdot \left( {\left( {{x + y} + z} \right) \cdot \left( {{\overline{x} + y} + z} \right)} \right)}$$

$${} = {{\left( {{x + y} + \overline{z}} \right) \cdot \left( {\left( {{x + y} + \overline{z}} \right) \cdot \left( {{x + \overline{y}} + \overline{z}} \right)} \right)} \cdot \left( {\left( {{x + y} + z} \right) \cdot \left( {{\overline{x} + y} + z} \right)} \right)}$$

$${} = {\left( {\left( {{x + y} + \overline{z}} \right) \cdot \left( {{x + \overline{y}} + \overline{z}} \right)} \right) \cdot \left( {\left( {{x + y} + z} \right) \cdot \left( {{\overline{x} + y} + z} \right)} \right)}$$

$${} = {\left( {x + \overline{z}} \right) \cdot \left( {y + z} \right)}$$
