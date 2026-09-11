1.  1.  1.  Operadores "nor" y "nand" que representaremos
            respectivamente como $$@$$y $$@$$.

            1.  Definición de "nor":
                $${x@y}{: =}{{\overline{x} \cdot \overline{y}} = \overline{x+y}}$$.
            2.  Definición de "nand":
                $${x@y}{: =}{{\overline{x} + \overline{y}} = \overline{x\cdot y}}$$.

        2.  No asociatividad en general de "nor" y de "nand". Dar algún
            ejemplo en $$B_{2}$$.

        3.  Cualquier expresión de las que hasta ahora se ha podido
            utilizar es expresable con solo funciones "nand" y con solo
            funciones "nor".

            1.  "NOR":

                1.  $${{x + y} = {({x@y})}}@{({x@y})}$$
                2.  $${x \cdot y} = {({{({x@x})}@{({y@y})}})}$$
                3.  $$\overline{x} = {x@x}$$

            2.  "NAND":

                1.  $${{x \cdot y} = {({x@y})}}@{({x@y})}$$
                2.  $${{x + y} = {({x@x})}}@{({y@y})}$$
                3.  $$\overline{x} = {x@x}$$

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
