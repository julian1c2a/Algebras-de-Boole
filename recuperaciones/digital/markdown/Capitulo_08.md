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

  -------------------------- ------------------------------------------------------------------
  $$\mathbf{N}$$ variables   Número de funciones distintas: $$2^{(2^{\mathbf{\mathrm{N}}})}$$
  0                          2
  1                          4
  2                          16
  3                          256
  4                          65536
  5                          4294967296
  6                          18446744073709551616
  7                          340282366920938463463374607431768211456
  -------------------------- ------------------------------------------------------------------

2.  1.  El punto anterior es fácil de probar:

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

3.  1.  Como se ve en el punto anterior, el crecimiento es desmesurado
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
