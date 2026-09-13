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
                2.   $$\forall{x \in B}{x \leq x}$$

            2.  Antisimétrica:
                $$\forall x,{y \in B}{{x \leq {y \land y}} \leq x}\Rightarrow{x = y}$$

                1.  $$x,{y \in B}{{x \leq {y \land y}} \leq x}$$
                2.  $$x,{y \in B}{{{x \cdot y} = {{y \land x} \cdot y}} = x}$$
                3.  $$x,{y \in B}{x = y}$$

            3.  Transitiva:
                $$\forall x,y,{z \in B}{{x \leq {y \land y}} \leq z}\Rightarrow{x \leq z}$$

                1.   $${x \leq {y \land y}} \leq z$$
                2.  $${{x \cdot y} = {{x \land y} \cdot z}} = y$$
                3.  $${{x \cdot y} \cdot z} = {x \cdot z}$$
                4.  $${x \cdot y} = {x \cdot z}$$
                5.  $$x = {x \cdot z}$$
                6.  $$x \leq z$$

        4.  Definición:$$\forall x,{y \in B}{x \geq y}\Leftrightarrow{{x \cdot y} = y}\Leftrightarrow{{x + y} = x}$$

        5.  $$\left\langle {B, \geq} \right\rangle\text{es un}\mathit{orden}$$.

            1.  Reflexiva: $$\forall{x \in B}{x \geq x}$$

                1.  $$\forall{x \in B}{{x + x} = x}$$
                2.   $$\forall{x \in B}{x \geq x}$$

            2.  Antisimétrica:
                $$\forall x,{y \in B}{{x \geq {y \land y}} \geq x}\Rightarrow{x = y}$$

                1.  $$x,{y \in B}{{x \geq {y \land y}} \geq x}$$
                2.  $$x,{y \in B}{{{x + y} = {{y \land x} + y}} = x}$$
                3.  $$x,{y \in B}{x = y}$$

            3.  Transitiva:
                $$\forall x,y,{z \in B}{{x \geq {y \land y}} \geq z}\Rightarrow{x \geq z}$$

                1.   $${x \geq {y \land y}} \geq z$$
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

        31.  Ahora vamos a construir una función inyectiva del álgebra
            de Boole de las partes de los átomos de B (si este es
            finito) en el álgebra de Boole B. Así cuando menos sa­bremos
            que podemos interpretar este álgebra de las partes de un
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
