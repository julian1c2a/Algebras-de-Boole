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

            38. $${\lbrack{{Teorema}1}\rbrack}\forall x,{y \in B}x \oplus {y = y} \oplus x$$

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

            39. $${\lbrack{{Teorema}2}\rbrack}\forall{x \in B}x \oplus {x = 0}$$

                1.  Prueba:
                2.  $${0 = x} \oplus \left( {- x} \right)$$
                3.  $${0 = x} \oplus \left( {\left( {- x} \right) \cdot \left( {- x} \right)} \right)$$
                4.  $${0 = x} \oplus \left( {x \cdot x} \right)$$
                5.  $${0 = x} \oplus x$$

            En el grupo aditivo de un anillo booleano $$B$$ es siempre
            $$\left( {- x} \right) = x$$.

            40. $${\lbrack{{Notación}2}\rbrack}\forall{x \in B}\overline{x}{: = x} \oplus 1$$

            41. $${\lbrack{{Teorema}3}\rbrack}\forall{x \in B}{{x \cdot \overline{x}} = 0}$$

                1.  Prueba:
                2.  $${x \cdot \overline{x}} =$$
                3.  $${= {x \cdot \left( {x \oplus 1} \right)}} =$$
                4.  $${= {x^{2} \oplus {x \cdot 1}}} =$$
                5.  $${= {x \oplus x}} =$$
                6.  $$= 0$$

            42. $${\lbrack{{Notación}3}\rbrack}\forall x,{y \in B}{x + y}{: = \left( {x \oplus y} \right)} \oplus \left( {x \cdot y} \right)$$

            43. $${\lbrack{{Teorema}3}\rbrack}\forall x,{y \in B}{{x \cdot y} = {y \cdot x}}$$

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

            44. $${\lbrack{{Teorema}4}\rbrack}\forall{x \in B}{{x \cdot \overline{x}} = 0}$$

                1.  Prueba:
                2.  $${x \cdot \overline{x}} =$$
                3.  $${= {x \cdot \left( {x \oplus 1} \right)}} =$$
                4.  $${= {x^{2} \oplus {x \cdot 1}}} =$$
                5.  $${= {x \oplus x}} =$$
                6.  $$= 0$$

            45. $${\lbrack{{Teorema}5}\rbrack}\forall{x \in B}x \oplus {\overline{x} = 1}$$

                1.  Prueba:
                2.  $$x \oplus {\overline{x} =}$$
                3.  $${= {x \oplus \left( {x \oplus 1} \right)}} =$$
                4.  $${= \left( {x \oplus x} \right)} \oplus {1 =}$$
                5.  $${= {0 \oplus 1}} =$$
                6.  $$= 1$$

            46. $${\lbrack{{Teorema}6}\rbrack}\forall{x \in B}{{x + \overline{x}} = 1}$$

                1.  Prueba:
                2.  $${x + \overline{x}} =$$
                3.  $${= \left( {x \oplus \overline{x} \oplus \left( {x \cdot \overline{x}} \right)} \right)} =$$
                4.  $${= {1 \oplus 0}} =$$
                5.  $$= 1$$

            47. $${\lbrack{{Teorema}7}\rbrack}\forall{x \in B}{{x + x} = x}$$

                1.  Prueba:
                2.  $${x + x} =$$
                3.  $${= \left( {x \oplus x \oplus \left( {x \cdot x} \right)} \right)} =$$
                4.  $${= {0 \oplus x}} =$$
                5.  $$= x$$

            48. $${\lbrack{{Teorema}8}\rbrack}\forall{x \in B}{{x + 0} = x}$$

                1.  Prueba:
                2.  $${x + x} =$$
                3.  $${= \left( {\left( {x \oplus 0} \right) \oplus \left( {x \cdot 0} \right)} \right)} =$$
                4.  $${= {x \oplus 0}} =$$
                5.  $$= x$$

            49. $${\lbrack{{Teorema}9}\rbrack}\forall x,{y \in B}{{x + y} = {y + x}}$$

                1.  Prueba:
                2.  $${x + y} =$$
                3.  $${= \left( {x \oplus y} \right)} \oplus {\left( {x \cdot y} \right) =}$$
                4.  $${= \left( {y \oplus x} \right)} \oplus {\left( {y \cdot x} \right) =}$$
                5.  $$= {y + x}$$

            50. $${\lbrack{{Teorema}10}\rbrack}\forall x,y,{z \in B}{{\left( {x + y} \right) + z} = {x + \left( {y + z} \right)}}$$

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

            51. $${\lbrack{{Teorema}11}\rbrack}\forall x,y,{z \in B}{{{({x + y})} \cdot z} = {{({x \cdot z})} + {({y \cdot z})}}}$$

                1.  Prueba:
                2.  $${\lbrack A\rbrack}{{{({x + y})} \cdot z} =}$$
                3.  $${{({{({x \oplus y})} \oplus {({x \cdot y})}})} \cdot z} =$$
                4.  $${({{({x \cdot z})} \oplus {({y \cdot z})}})} \oplus {({{x \cdot y} \cdot z})}$$
                5.  $${\lbrack B\rbrack}{}{}{}{{{({x \cdot z})} + {({y \cdot z})}} =}$$
                6.  $${({{({x \cdot z})} \oplus {({y \cdot z})}})} \oplus {({{x \cdot y} \cdot z})}$$
                7.  $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{se obtine la igualdad deseada.}$$

            52. $${\lbrack{{Teorema}12}\rbrack}\forall x,y,{z \in B}{}{}{}{{{({x \cdot y})} + z} = {{({x + z})} \cdot {({y + z})}}}$$

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
