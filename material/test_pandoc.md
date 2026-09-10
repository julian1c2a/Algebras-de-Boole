1.  Algunos convenios:

    1.  $$0 \notin \mathbb{N}$$. Ante la definición de los naturales
        nosotros adoptamos este convenio.

    2.  $$\widetilde{\mathbb{N}} ≝ \left( {\mathbb{N} \cup \left\{ 0 \right\}} \right)$$.
        Conjunto de los naturales españoles que ya tiene el cero.

    3.  Definición por recurrencia de los conjuntos
        $$\lbrack 0,1\rbrack_{\mathbb{Q}}$$y
        $$\lbrack 0,1\rbrack_{\mathbb{Q}}^{n}$$, dónde
        $${n \in \mathbb{N}}{n > 1}$$:

        1.  1.  $$\lbrack 0,1\rbrack_{\mathbb{Q}}{: = {\lbrack 0,1\rbrack \cap \mathbb{Q}}}$$.
            2.  $${\lbrack 0,1\rbrack_{\mathbb{Q}}}^{1}{: = \lbrack 0,1\rbrack_{\mathbb{Q}}}$$.
            3.  $${\lbrack 0,1\rbrack_{\mathbb{Q}}}^{n}{: = {{\lbrack 0,1\rbrack_{\mathbb{Q}}}^{n - 1} \times {\lbrack 0,1\rbrack_{\mathbb{Q}}}^{1}}}$$.

    4.  Por lo general los elementos de un conjunto se representarán por
        letras minúsculas (alfa­betos griego y latino) con o sin
        suscriptores
        (ejemplo:$$a_{3}$$o$$b$$o$$\gamma_{1547}$$o$$\delta$$) y dí­gitos
        decimales ($$\{{0,1,\ldots,9}\}$$), mientras que los conjuntos
        se representarán por letras mayúsculas (alfabetos griego y
        latino), igualmente con o sin suscriptores. Este convenio será
        válido a excepción que se exprese de forma explícita otro nombre
        para elementos y/o conjuntos.

    5.  En ocasiones aseguraremos que existe un conjunto asociado a un
        elemento: en general serán letras mayúsculas como corresponde a
        un conjunto, pero con un subscriptor que esté escrito
        exactamente como el elemento. La única excepción que se dará es
        un elemento cubierto con la tilde circunflejo, para expresar el
        conjunto de elementos complementa­rios (sea en este instante lo
        que sea ese concepto) con uno dado.

    6.  A veces aparecerá una operación binaria,
        digamos$${\cdot \ast} \cdot$$, dónde los puntos se sustitu­yen
        con los argumentos. Cuando expresemos $$a \ast B$$ , osea, el
        elemento $$a$$operado con un conjunto $$B$$, se trata una
        operación binaria que no es la original. Se interpreta­rá como
        $${a \ast B} = {\{{{a \ast b} \mid \forall{b \in B}}\}}$$ , esto
        es, un conjunto. Igualmente puede ocurrir que esta misma
        operación aparezca entre dos conjuntos:
        $${A \ast B} = {\{{{a \ast b} \mid {\forall{a \in A}\forall{b \in B}}}\}}$$.

    7.  El universo de discurso en el que nos moveremos será$$B$$, por
        lo que para el cuantificador univer­sal (que evitaremos en lo
        posible) no pondremos ningún símbolo de forma que, cuando
        aparezca una variable o conjunto o constante sin haber sido
        cuantificada supondremos que se aplica el cuantificador
        universal a la variable o constante situándolo dentro de $$B$$.
        Si el cuantificador universal debiera aplicarse a una variable
        sobre otro conjunto subconjunto de $$B$$ se omitirá el
        cuantificador universal pero se precederá la sentencia con una
        indicación sobre la pertenencia del elemento. Para cualquier
        elemento en el que no aparezca su pertenencia es porque
        pertenece al universal $$B$$. Al igual, cuando una variable que
        asuma un valor que sea un conjunto este será parte de
        $$\wp{(B)}$$, no aparecerá de forma explícita. Para las variable
        conjunto se repite todo lo anterior con la diferencia de cambiar
        $$B$$ por $$\wp{(B)}$$. De otro lado podemos considerar la clase
        propia de las álgebras de Boole.

2.  Álgebra de Boole.

    1.  Axiomas para un álgebra de Boole
        $$\langle{B,{{\{{0_{B},1_{B}}\}} \subseteq B},{0_{B} \neq 1_{B}},{\mathit{op}{\{{\mathit{bin}:{\{{+ , \cdot}\}}}\}}}}\rangle$$.

        La operación un-aria que se utilizará frecuentemente (la
        complementación), en los axio­mas será introducida como
        definición y no supuesta inicialmente más que como la exis­tencia
        de un conjunto de elementos no vacío asociados a otro que
        cumplen unos requisi­tos. Sin embargo esto último es tan
        importante en las álgebras de Boole que la forma normal de
        escribirse la estructura es
        $$\left\langle {B,{\left\{ {0_{B},1_{B}} \right\} \subseteq B},{0_{B} \neq 1_{B}},{\mathit{op}\left\{ {\mathit{bin}:\left\{ {+ , \cdot} \right\}} \right\},\left\{ {\mathit{una}:\left\{ \overline{} \right\}} \right\}}} \right\rangle$$.

        Los postulados de Huntington (artículos en 1904,1932 -este
        último desarrolla un con­junto de 3 axiomas, uno de ellos llamado
        específicamente Axioma de Huntington, y no es el caso aquí
        expuesto-) definen qué es un álgebra de Boole
        $$\langle{\mathtt{\mathrm{B}},{\{{\mathtt{\mathrm{0}},\mathtt{\mathrm{1}}}\}},{\{{+ , \cdot}\}}}\rangle$$:

        1.  \[Axioma H1\] Existencia del elemento identidad:

            1.  \[H1.1\] Para la suma $$+$$:
                $$\forall{x \in B}{{x + 0} = x}$$
            2.  \[H1.2\] Para la multiplicación $$\cdot$$:
                $$\forall{x \in B}{{x \cdot 1} = x}$$

        2.  \[Axioma H2\] Conmutabilidad:

            1.  \[H2.1\] Para la suma $$+$$:
                $$\forall x,{y \in B}{{x + y} = {y + x}}$$
            2.  \[H2.2\] Para la multiplicación$$\cdot$$:
                $$\forall x,{y \in B}{{x \cdot y} = {y \cdot x}}$$

        3.  \[Axioma H3\] Propiedad distributiva:

            1.  \[H3.1\] Para la suma $$+$$ sobre el
                producto$$\cdot$$:$$\forall x,y,{z \in B}{{x + {({y \cdot z})}} = {{({x + y})} \cdot {({x + z})}}}$$

            2.  \[H3.2\] Para el producto$$\cdot$$sobre la suma $$+$$:

                $$\forall x,y,{z \in B}{{x \cdot {({y + z})}} = {{({x \cdot y})} + {({x \cdot z})}}}$$

        4.  \[Axioma H4\] Existencia de complementario:
            $$\forall{x \in B}\exists{\widehat{x} \subseteq B}{\widehat{x} \neq \varnothing}{{\lbrack{{x + \widehat{x}} = {\{ 1\}}}\rbrack} \land {\lbrack{{x \cdot \widehat{x}} = {\{ 0\}}}\rbrack}}$$

    Como ejemplos que cumplen los anteriores postulados o axiomas vamos
    a desarrollar unos cuántos.

    **\[Ejemplo 1\]** El primero y más sencillo de ver es el álgebra de
    las partes de un conjunto. Dado un conjunto
    cualquiera$$U \neq \varnothing$$,
    $${@U} = {\{{X \mid {X \subseteq U}}\}}$$, esto es,
    $${@U} = {\{{X \mid {{\forall x}\left( {{({x \in X})}\Rightarrow{({x \in U})}} \right)}}\}}$$
    verifica
    que$$\left( {{\varnothing \in @}U} \right) \land \left( {{U \in @}U} \right)$$.
    Ha­remos$$\left( {B{: = @}U} \right),\left( {0{: = \varnothing}} \right)y\left( {1{: = U}} \right)$$,
    como producto lógico pondremos la intersección de
    conjuntos$$\forall X,{Y \in @}U{X \cdot Y}{: = {X \cap Y}}$$, como
    suma lógica pondremos la unión de
    conjuntos$$\forall X,{Y \in @}U{X + Y}{: = {X \cup Y}}$$. Las tres
    primeras (dobles) propiedades son di­rectamente cumplidas por la
    estructura construida y la existencia del complementario es fá­cil de
    ver. Sea
    $$\forall{X \in @}U\Rightarrow\exists Y{: = {U \smallsetminus X}}$$y
    a partir de ahí sabemos que$${Y \in @}U$$puesto
    que$$\forall{x \in Y}{x \in {U \smallsetminus X}}\Rightarrow{x \in U}$$y
    en el caso que$$X = U$$tenemos que
    $${{Y = {U \smallsetminus X}} = {U \smallsetminus U}} = \varnothing$$de
    forma que$${\varnothing \in @}U$$por definición. Ahora sólo se trata
    de ver
    que$${{{{Y \cdot X} = {Y \cap X}} = {{({U \smallsetminus X})} \cap X}} = \varnothing} = 0$$y
    que la propiedad dual a
    cumplir$${{{{Y + X} = {Y \cup X}} = {{({U \smallsetminus X})} \cup X}} = U} = 1$$.
    Ya tenemos
    que$$\forall{X \in @}U\exists{Y \in @}U{Y \in \overline{X}}$$ha­biendo
    tomado$$Y{: = {U \smallsetminus X}}$$.

    **\[Ejemplo 2\]** Un ejemplo interesante fácil de construir es el
    álgebra de Boole de los números que son producto de los primeros
    núme­ros primos (cantidad finita de ellos) y sus divisores.
    Consideramos el conjunto $$P_{n}{: = {\{{2,3,\ldots,p_{n}}\}}}$$,
    con­sideraremos el $$1$$ booleano
    cómo$$1_{B}{: = {\prod\limits_{q \in P_{n}}q}}$$y el $$0$$
    cómo$$0_{B}{: = 1_{\mathbb{N}}}$$. Consideramos a
    $$B_{n}{: = {\{{{k \in \mathbb{N}} \mid {k \mid \left( {\prod P_{n}} \right)}}\}}}$$,
    y las operaciones serán el mínimo común múltiplo como suma booleana
    y el máximo común divisor como producto booleano. El complemento de
    un ele­mento resulta ser
    $$\forall{k \in B_{n}}{{\overline{k} = {1_{B}/k}} = {\prod\limits_{q \in {\{{{{p \in P_{n}} \mid p} \nmid k}\}}}q}}$$.
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
    Es fácil comprobar la validez de esta definición de un álgebra de
    Boole, de manera más concreta, que las operaciones son internas y el
    complemento declarado es también interno y se comporta como
    complemento del nuevo álgebra, esto
    es,$${y \in B_{\geq x}}\Rightarrow y{{' \cdot y} = {x \land y}}{{' + y} = 1}$$
    que$${y \in B_{\leq x}}\Rightarrow y{{' \cdot y} = {0 \land y}}{{' + y} = x}$$.

    **\[Ejemplo 4\]** El álgebra de las proposiciones. Éste es sin duda,
    el primer desarrollo que se hizo del álgebra de Boole, hecha por el
    propio George Boole en mitad del siglo XIX (edición 1851). Lo
    desarrolló como una "Una investigación en las leyes del
    pensamiento". Amigo suyo que lo ayudó a penetrar los ambientes
    académi­cos es Augustus De Morgan. Desde Aristóteles (que funda por
    primera vez la ló­gica como ciencia analítica) en el siglo IV a. C.
    no había habido ningún adelanto sustancial en la lógica. Kant (medio
    siglo antes de Boole) había considerado que la lógica era un cuerpo
    de doctrina cerrado y completo (esto es, no había nada más que decir
    que lo que ya había desarrollado y escrito Aristóteles en sus
    "Tra­tados de Lógica" u "Órganon", hacía ya 2.300 años). Aunque la
    verdadera revolu­ción se da algunos años más tarde con Frege, el
    lógico más importante desde Aristóteles. Si doy estos datos sobre la
    historia de la lógica que todos asociaréis más a la filosofía, que
    parece queda muy lejos del propósito de unos apuntes de matemáticas
    discretas que cubran de la forma más amplia posible los Fundamentos
    de Electró­nica Digital, es porque no queda tan lejos. La idea de
    hacer un len­guaje dónde el razonamiento siguiera unas pautas claras
    de forma que siempre quedara todo tan cierto como en las matemáticas
    era ya antiguo. Aristóteles ya advertía de una cierta indefinición
    insuperable de los términos más importantes de la filosofía (en
    realidad de casi todos los conceptos de la vida ordinaria): "exis­ten
    conceptos o ideas que corresponden con la realidad que no se usan de
    forma equívoca -- esto es, su uso no es equívoco, este mismo
    concepto, palabra o idea que hablamos no se refiere a realidades
    distintas y diferenciadas, de forma que nos llevan a confusión --
    pero tampoco de forma unívoca -- como las definiciones desde axiomas
    en un lenguaje formal matemático, así tenemos que existen con­ceptos
    análogos" (es una glosa de palabras de Aristóteles). En la
    Modernidad, dado que el concepto de analogía lleva aparejado un
    tratamiento difícil que no lleva fácilmente a certeza, se intentan
    buscar criterios de certeza absoluta y unas definiciones que
    aparentemente son unívocas y se tratan como tales. Es significativo
    el nombre (y la estructura interna) de una importante obra de
    Spino­za: "Ética demostrada según el orden geométrico". Será Leibniz
    quién escriba ya cumplidamente sobre la necesidad de establecer un
    léxico completamente unívoco (una tarea mastodonte, o mejor,
    imposible) y un "cálculo" del pensamiento, de forma que "una
    cuestión como la existencia de Dios pueda ser resuelto mediante la
    resolución de unas ecuaciones de pensamiento" (de nuevo es una
    glosa). Se empezaba a buscar con ansiedad una mecanización del
    pensamiento. Esta idea fue muy fructífera, dando un primer paso
    hacia ella George Boole que hace un ál­gebra de las proposiciones.
    Este álgebra no era más amplia que la de Aristóteles, pero permitía
    el cálculo al modo matemático. De aquí a la llegada de Frege, ya,
    Charles Babbage diseña y realiza (sin éxito debido al trabajo de
    mecanizado ex­cesivamente minucioso que requería el diseño) una
    computadora universal me­cánica (mediante engranajes) prácticamente
    similar al modelo de Von Neumann. La condesa de Lovelace (Ada) es el
    matemático que hace los primeros progra­mas en lenguaje ensamblador
    de la máquina de Babbage. La primera programa­dora de la historia.
    Después de Frege siguen los desarrollos con gente como Ber­trand
    Rusell, David Hilbert, y otros hasta los increíbles resultados de
    Gödel que ponen punto final a muchas de las pretensiones de
    mecanización del pensamiento, pero que son ya base de la computación
    moderna, siendo los trabajos definitivos los de Alan Turing. Como
    veis el camino recorrido es largo y complicado, siendo el momento
    crucial para el arranque de la ingeniería digital los trabajos de
    George Boole. No he mencionado el papel de las máquinas de cifrado y
    descifrado de mensajes en la Gran Guerra y la II Guerra Mundial (en
    las que intervinieron muchos de las mentes antes mencionadas).

    De manera un tanto informal podemos ver una proposición (una frase
    que afirma o niega una propiedad de un objeto, una relación entre
    objetos o la existencia del mismo, una frase que ha de ser o
    verdadera, $$1_{B}{{: = V} \equiv \mathbf{\mathit{verdadero}}}$$, o
    falsa, $$0_{B}{{: = F} \equiv \mathbf{\mathit{falso}}}$$, o más
    habitualmente, en inglés,
    $$1_{B}{{: = T} \equiv \mathbf{\mathit{true}}}$$ o
    $$0_{B}{{: = F} \equiv \mathbf{\mathit{false}}}$$) o conjunto de
    proposiciones pueden ser operadas mediante la conjunción 'y', A 'y'
    B es verdadero si A es verdadero y B es verdadero a la vez y falso
    en cualquier otro caso. La disyunción sería la 'o', siendo A 'o' B
    verdadero con que A sea verdadero o lo sea B, siendo falso sólo
    cuando A es falso y B es falso a la vez. La notación más habitual es
    $${{{\cdot + \cdot}{: = {\cdot \vee \cdot}}} \equiv \cdot}\text{or}{\cdot \equiv {{\cdot \mid} \mid \cdot}}$$y$${{{\cdot \mathbf{\cdot} \cdot}{: = {\cdot \land \cdot}}} \equiv \cdot}\text{and}{\cdot \equiv {\cdot \&\& \cdot}}$$.
    Para el 'no' (negación) tenemos
    que$${{\overline{\cdot}{: = {\neg \cdot}}} \equiv \text{not}}{\cdot \equiv {/ \cdot}}$$.
    El conjunto de Boole es el conjunto de proposiciones de la que
    partamos.

    Para ser más exactos, pongamos que $$P$$ es el universo de las
    proposiciones con las que vamos a trabajar, pero en vez de trabajar
    directamente con las proposiciones vamos a trabajar con clases de
    proposiciones. Como en el álgebra de Boole disponemos del signo de
    igualdad, no tiene sentido trabajar con dos proposiciones que son
    equivalentes, esto es, que toman exactamente los mismos valores de
    verdad. Sean $$p,{q \in P}{p \simeq q} ≝ p\Leftrightarrow q$$,
    definimos a partir de aquí
    $${\lbrack p\rbrack} = {\{{{q \in P} \mid p\Leftrightarrow q}\}}$$,
    y el conjunto de los cocientes
    $$\mathtt{\mathrm{P}} ≝ {{{P/} \simeq} \equiv {\{{{\lbrack p\rbrack} \mid {p \in P}}\}}}$$.
    A partir de aquí definimos
    $${\lbrack a\rbrack},{{\lbrack b\rbrack} \in \mathtt{\mathrm{P}}}{{\lbrack a\rbrack} + {\lbrack b\rbrack}} ≝ {\lbrack{a \vee b}\rbrack}$$
    $${\lbrack a\rbrack},{{\lbrack b\rbrack} \in \mathtt{\mathrm{P}}}{{\lbrack a\rbrack} \cdot {\lbrack b\rbrack}} ≝ {\lbrack{a \land b}\rbrack}$$y
    $${{\lbrack a\rbrack} \in \mathtt{\mathrm{P}}}\overline{\lbrack a\rbrack} ≝ {\lbrack{\neg a}\rbrack}$$.

    **\[Ejemplo 5\]** El álgebra de conmutación. Este es el álgebra de
    Boole más sencillo que hay. $$B{{: = B_{2}} \equiv {\{{0,1}\}}}$$.
    Las operaciones las concretaremos en tablas:

    $$\begin{bmatrix}
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

    y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington. Ésta será usada frecuentemente durante el curso. Este
    álgebra está contenido en todo álgebra de Boole.

    **\[Ejemplo 6\]** El álgebra de Boole de 4 elementos. Este es el
    álgebra de Boole generada por un conjunto de 2 elementos. Es
    singular en el sentido que sólo tiene 3 niveles, el más bajo
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
     \cdot & 0 & a & b & 1 \\
    0 & 0 & 0 & 0 & 0 \\
    a & 0 & a & 0 & a \\
    b & 0 & 0 & b & b \\
    1 & 0 & a & b & 1
    \end{bmatrix}\begin{bmatrix}
    \overline{} & 0 & a & b & 1 \\
     & 1 & b & a & 0
    \end{bmatrix}$$

    y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington si cam­biáis $$a$$ por $$\{\alpha\}$$, $$b$$ por
    $$\{\beta\}$$, $$1$$ por $$\{{{\{\alpha\}},{\{\beta\}}}\}$$ y $$0$$
    por el conjunto vacío $$\varnothing$$.

    **\[Ejemplo 7\]** El álgebra de Boole de 8 elementos. Este es el
    álgebra de Boole generada por un conjunto de 3 elementos. Es
    singular en el sentido que sólo tiene 4 niveles, el más bajo
    $$\{ 0\}$$, el de átomos $$\{{a,b,c}\}$$, el de hiper-átomos
    $$\{{A,B,C}\}$$ y el superior $$\{ 1\}$$. Los niveles de átomos y de
    hiper-átomos son especialmente importantes, siendo este álge­bra de
    Boole, el más pequeño que los diferencia. Sería:

    $$B{{: = B_{8}} \equiv {\{{0,a,b,c,A,C,B,1}\}}}$$.

    Las operaciones las concretaremos en tablas:

    $$\begin{bmatrix}
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

    y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington si te­néis en cuenta los cambios aconsejados en el
    cuadro entre llaves, dónde las flechas quieren decir "substituir
    por".

    **\[Ejemplo 8\]** El álgebra de Boole de 16 elementos. Este es el
    álgebra de Boole generada por un conjunto de 4 elementos. Es ya un
    álgebra de Boole completamente regular. Tiene 5 niveles, el más bajo
    el $$\{ 0\}$$, el de átomos $$\{{\alpha,\beta,\gamma,\delta}\}$$, el
    de hiper-átomos $$\{{Α,Β,\Gamma,\Delta}\}$$ , el intermedio
    $$\{{a,b,c,d,e,f}\}$$y finalmente el nivel superior con el
    $$\{ 1\}$$. Sería:

    2.  $$B{{: = B_{16}} \equiv {\{{0,\alpha,\beta,\gamma,\delta,a,b,c,d,e,f,Α,Β,\Gamma,\Delta,1}\}}}$$.

    Las operaciones las concretaremos en tablas:

    $$\begin{bmatrix}
     + & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & Α & Β & \Gamma & \Delta & 1 \\
    0 & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & Α & Β & \Gamma & \Delta & 1 \\
    \alpha & \alpha & \alpha & a & b & c & a & b & c & Α & Β & \Gamma & Α & Β & \Gamma & 1 & 1 \\
    \beta & \beta & a & \beta & d & e & a & Α & Β & d & e & \Delta & Α & Β & 1 & \Delta & 1 \\
    \gamma & \gamma & b & d & \gamma & f & Α & b & Β & \Gamma & \Delta & f & Α & 1 & \Gamma & \Delta & 1 \\
    \delta & \delta & c & e & f & \delta & Β & \Gamma & c & \Delta & e & f & 1 & Β & \Gamma & \Delta & 1 \\
    a & a & a & a & Α & Β & a & Α & Β & Α & \Delta & 1 & Α & Β & 1 & 1 & 1 \\
    b & b & b & Α & b & \Gamma & Α & b & Β & Α & 1 & \Gamma & Α & 1 & \Gamma & 1 & 1 \\
    c & c & c & Β & \Gamma & c & Β & \Gamma & c & 1 & Β & \Gamma & 1 & Β & 1 & \Delta & 1 \\
    d & d & Α & d & d & \Delta & Α & Α & 1 & d & \Delta & \Delta & Α & 1 & 1 & \Delta & 1 \\
    e & e & Β & e & \Delta & e & Β & 1 & Β & \Delta & e & \Delta & 1 & Β & 1 & \Delta & 1 \\
    f & f & \Gamma & \Delta & f & f & 1 & \Gamma & \Gamma & \Delta & \Delta & f & 1 & 1 & \Gamma & \Delta & 1 \\
    Α & Α & Α & Α & Α & 1 & Α & Α & 1 & Α & 1 & 1 & Α & 1 & 1 & 1 & 1 \\
    Β & Β & Β & Β & 1 & Β & Β & 1 & Β & 1 & Β & 1 & 1 & Β & 1 & 1 & 1 \\
    \Gamma & \Gamma & \Gamma & 1 & \Gamma & \Gamma & 1 & \Gamma & \Gamma & 1 & 1 & \Gamma & 1 & 1 & \Gamma & 1 & 1 \\
    \Delta & \Delta & 1 & \Delta & \Delta & \Delta & 1 & 1 & 1 & \Delta & \Delta & \Delta & 1 & 1 & 1 & \Delta & 1 \\
    1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
    \end{bmatrix}$$

$$\begin{bmatrix}
\neg & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & Α & Β & \Gamma & \Delta & 1 \\
 & 1 & \Delta & \Gamma & Β & Α & f & e & d & c & b & a & \delta & \gamma & \beta & \alpha & 0
\end{bmatrix}$$

$$\begin{bmatrix}
 \cdot & 0 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & Α & Β & \Gamma & \Delta & 1 \\
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
Α & Α & \alpha & \beta & \gamma & 0 & a & b & \alpha & d & e & \gamma & Α & a & b & d & Α \\
Β & Β & \alpha & \beta & 0 & \delta & a & \alpha & c & \beta & e & \delta & a & Β & c & d & Β \\
\Gamma & \Gamma & \alpha & 0 & \gamma & \delta & \alpha & b & c & \gamma & \delta & f & b & c & \Gamma & f & \Gamma \\
\Delta & \Delta & 0 & \beta & \gamma & \delta & \beta & \gamma & \delta & d & e & f & d & e & f & \Delta & \Delta \\
1 & 1 & \alpha & \beta & \gamma & \delta & a & b & c & d & e & f & Α & Β & \Gamma & \Delta & 1
\end{bmatrix}$$

3.  y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington, con solo tener en cuenta que todos los elementos se
    pueden poner en función de $$\alpha\beta\gamma\delta$$y sumas de
    ellos. Las sumas de dos de los anteriores elementos son $$abcdef$$y
    las sumas de tres de ellos son $$ΑΒ\Gamma\Delta$$.

    **\[Ejemplo 9\]** El álgebra de Boole de los conjuntos que se pueden
    expresar como **unión dis­junta finita de subintervalos genéricos de
    $$\left\lbrack {0,1} \right\rbrack_{\mathbb{Q}}≝{{\lbrack 0,1\rbrack \cap {\mathbb{Q}}} \equiv \left\{ {x \in {\mathbb{Q}} \mid 0 \leq x \leq 1} \right\}}$$.
    Definimos la notación
    $$\mathbf{\mathrm{I}}_{\mathbb{Q}}≝\left\lbrack {0,1} \right\rbrack_{\mathbb{Q}}$$**.
    Para definir la unión disjunta finita de subintervalos de
    $$\mathbf{\mathrm{I}}_{\mathbb{Q}}$$ haremos abs­tracción de
    cualquier conjunto finito de puntos de
    **$$\mathbf{\mathrm{I}}_{\mathbb{Q}}$$**, esto es, consideraremos
    que dos subconjuntos de $$\mathbf{\mathrm{I}}_{\mathbb{Q}}$$ son
    iguales si su diferencia simétrica (la unión de las diferencias, los
    elementos que no son comunes de ambos conjuntos) es vacía o un
    conjunto finito de puntos. Este álgebra de Boole tiene un cardinal
    infinito numerable (como el cardinal de los números naturales). Lo
    más importante es que no puede desarrollarse de manera semejante a
    como desarrolla­mos el álgebra de las partes de un conjunto. Lo
    formalizaremos del siguiente modo:

    1.  1.  $$a,{b \in \mathbf{\mathrm{I}}_{\mathbb{Q}}}{a < b}\Rightarrow\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}} ≝ {\left\lbrack {a,b} \right\rbrack \cap \mathbb{Q}} ≝ \left\{ {{x \in \mathbf{\mathrm{I}}_{\mathbb{Q}}} \mid {{a \leq x} \leq b}} \right\}$$.

        2.  Si escribimos
            $$\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}}$$ entonces
            $${a < {b \land a}} \neq b$$.

        3.  Sea
            $$\mathbf{II}_{\mathbb{Q}} ≝ \left\{ {\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}} \mid {a,{{{b \in {I_{\mathbb{Q}} \land a}} < {b \land a}} \neq b}}} \right\}$$.

        4.  Sea
            $$\mathbf{III}_{\mathbb{Q}}≝\left\{ {{A \in {\wp\left( I_{\mathbb{Q}} \right)}}\qquad \mid \qquad{{A = \underset{\lambda \in \Lambda}{\mathbf{\cup}}}I_{\lambda}\qquad\forall{\lambda \in \Lambda}\mspace{9mu}{I_{\lambda} \in {\mathbf{II}_{\mathbb{Q}}\mspace{9mu}{{\#(\Lambda)} \in {\mathbb{N}}_{0}}}}}} \right\}$$
            .

        5.  Sea
            $$\mathit{Fin}\left( I_{\mathbb{Q}} \right)\mspace{72mu} ≝\mspace{72mu}\left\{ {{A \in \wp}\left( I_{\mathbb{Q}} \right)\mspace{72mu} \mid \mspace{72mu}\#{(A) \in {\mathbb{N}}_{0}}} \right\}$$.

        6.  $$A,B{\in}{@\left( \mathbf{\mathrm{I}}_{\mathbb{Q}} \right)}{A \approx B} ≝ {\#{\left( {A \bigtriangleup B} \right) \in \widetilde{\mathbb{N}}}}$$.
            Esta relación es de equivalencia.

            1.  Reflexiva
                $$\#{\left( {A\bigtriangleup A} \right) = \#}{(\varnothing) = 0 \in {\mathbb{N}}_{0}}$$.
                Luego $$A \approx A$$.

            2.  Simétrica
                $$A \bigtriangleup {B = B} \bigtriangleup A.\Rightarrow.A \approx B\Leftrightarrow B \approx A$$.

            3.  Transitiva
                $$A \approx {B \land B} \approx C\Rightarrow A \approx C$$.

                1.  $$\#{\left( {A\bigtriangleup B} \right) = n_{1} \in {\overset{\sim}{\mathbb{N}} \land \#}}{\left( {B\bigtriangleup C} \right) = n_{2} \in {\mathbb{N}}_{0}}.\Rightarrow.\#{\left( {A\bigtriangleup C} \right) \leq {n_{1} + n_{2}} \in {\mathbb{N}}_{0}}$$.
                    Y queda de­mostrada la propiedad transitiva.

        7.  A partir de aquí hablaremos de $$⟦A⟧$$para hablar de la
            clase de equivalencia de
            $$A \in \mathbf{\mathrm{III}}_{\mathbb{Q}}$$bajo la relación
            de equivalencia $$\approx$$.

        8.  A partir de aquí hablaremos de nuestro conjunto
            $$\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{GEN}}(0,1) ≝ {}$$
            $$\left\{ {{⟦A⟧} \mid {A \in \mathbf{III}_{\mathbb{Q}}}} \right\}$$

            $${} = {\mathbf{III}_{\mathbb{Q}}/ \approx}$$

        9.  Nuestro conjunto de Boole será
            $$B ≝ {\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}(0,1)}$$.

        10. El $$0_{B}≝{⟦\varnothing ⟧}≝{⟦⟧}$$. El neutro representa
            cualquier cantidad finita de elementos racionales entre
            $$0$$ y $$1$$.

        11. El $$1_{B}≝{⟦\mathbf{\mathrm{I}}_{\mathbb{Q}}⟧}$$.
            Representa el intervalo unidad menos una cantidad finita o
            nula de elementos racionales entre $$0$$ y $$1$$.

        12. Ahora veremos unas operaciones muy cercanas a la unión, la
            intersección y el com­plemento, que nos van a generar un
            álgebra de Boole sobre
            $$\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}$$:

            $$\begin{array}{l}
            {\forall{⟦A⟧},{{⟦B⟧} \in \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{GEN}}}\mspace{72mu}{{⟦A⟧} + {⟦B⟧}}≝{⟦{A \cup B}⟧}} \\
            {\forall{⟦A⟧},{{⟦B⟧} \in \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{GEN}}}\mspace{72mu}{{⟦A⟧} \cdot {⟦B⟧}}≝{⟦{A \cap B}⟧}} \\
            {\forall{{⟦A⟧} \in \mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{GEN}}}\mspace{252mu}\overline{⟦A⟧}≝{⟦{\mathbf{\mathrm{I}}_{\mathbb{Q}} \smallsetminus A}⟧}}
            \end{array}$$

        13. Convenio de
            notación:$${⟦{a,b}⟧} ≝ {⟦\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}}⟧}$$será
            nuestro subintervalo genérico del intervalo unidad genéri­co.

        14. Sea una sucesión finita de un número par $$2 \cdot n$$ de
            elementos de $$\lbrack 0,1\rbrack_{\mathbb{Q}}$$,
            estricta­mente creciente
            $${{{{{{{0_{\mathbb{Q}} \leq a_{1}} < b_{1}} < a_{2}} < b_{2}} < \ldots} < a_{n}} < b_{n}} \leq 1_{\mathbb{Q}}$$
            dispuestos como

            $$⟦{a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}}⟧$$definirán
            los elementos de
            $$\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{\mathrm{GEN}}}$$,
            aparte de
            $${⟦⟧}≝{{⟦\varnothing ⟧} = {⟦{\{ 0\}}⟧} = {⟦{\{ 1\}}⟧} = 0_{\mathbf{\mathrm{I}}_{\mathbb{Q}}^{\mathbf{GEN}}}}$$.

        15. Si escribimos
            $$⟦{a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}}⟧$$,
            significamos ya que
            $${{{{{{{0_{\mathbb{Q}} \leq a_{1}} < b_{1}} < a_{2}} < b_{2}} < \ldots} < a_{n}} < b_{n}} \leq 1_{\mathbb{Q}}$$.

        16. Ahora ya, definimos (notación):

            $$\begin{array}{l}
            {{⟦{a_{1},b_{1},a_{2},b_{2},\ldots,a_{n},b_{n}}⟧}≝{{⟦{\{{{x \in {\lbrack 0,1\rbrack}_{\mathbb{Q}}} \mid \exists{1 \leq k \leq n \in {\mathbb{N}}}\qquad{x \in {\lbrack{a_{k},b_{k}}\rbrack}_{\mathbb{Q}}}}\}}⟧} \equiv}} \\
            {\equiv {⟦{\mathbf{\mathrm{\cup}}_{{k = 1.}..n}{\lbrack{a_{k},b_{k}}\rbrack}}⟧}}
            \end{array}$$.

        17. Ahora tenemos el conjunto de Boole antes encontrado bajo
            otra representación, que será más práctica a la hora de
            hacer cálculos:

            $$\left\lbrack {⟦0,1⟧} \right\rbrack_{\mathbf{\mathrm{I}}} ≝ {\left\{ {{⟦{a_{1,}b_{1,}\ldots,a_{n},b_{n}}⟧} \mid {\exists{n \in \mathbb{N}}{{{{{{0_{\mathbb{Q}} \leq a_{1}} < b_{1}} < \ldots} < a_{n}} < b_{n}} \leq 1_{\mathbb{Q}}}}} \right\} \cup \left\{ {⟦⟧} \right\}}$$.

    Que las uniones, complementos e intersecciones de intervalos
    genéricos finitos siguen siendo intervalos genéricos finitos es
    claro desde el principio. Sin embargo voy a exponer la cabalística,
    hacer las cuentas vamos, para tener una forma de hacer cuentas con
    la última forma de representación. Con todo, este método de cálculo
    habrá de comprobarse que $$B$$ es cerrado bajo las distintas
    operaciones es demasiado laboriosa.

    Las operación de complemento queda de la siguiente manera, y aunque
    aún no podemos comprobar aún su corrección, si queda claro que es un
    operación unaria interna:

    $$\forall{A \in B}\qquad\forall{A \in A}\qquad A^{I}{: = {⟦{\mathbf{\mathrm{I}}_{\mathbb{Q}} \smallsetminus A}⟧}}$$

    $$\text{Sea}A{: = \cup_{{k = 1.}..n}}\left\lbrack {a_{k},b_{k}} \right\rbrack$$

    $$A^{I} \equiv \begin{Bmatrix}
    {⟦{0,a_{1},b_{1},a_{2},\ldots,b_{n - 1},a_{n},b_{n},1}⟧} & \Leftarrow & {a_{1} \neq {0 \land b_{n}} \neq 1} \\
    {⟦{b_{1},a_{2},\ldots,b_{n - 1},a_{n},b_{n},1}⟧} & \Leftarrow & {a_{1} = {0 \land b_{n}} \neq 1} \\
    {⟦{b_{1},a_{2},\ldots,b_{n - 1},a_{n}}⟧} & \Leftarrow & {a_{1} = {0 \land b_{n}} = 1} \\
    {⟦{0,a_{1},b_{1},a_{2},\ldots,b_{n - 1},a_{n}}⟧} & \Leftarrow & {a_{1} \neq {0 \land b_{n}} = 1} \\
    {⟦\varnothing ⟧} & \Leftarrow & {a_{1} = {0 \land b_{1}} = 1} \\
    {⟦0,1⟧} & \Leftarrow & {{\{\varnothing\}} \in A}
    \end{Bmatrix}$$

    De dónde obtenemos$$\forall{A \in B}\exists{A^{I} \in B}$$.

    Tenemos que $${0 \in B}0{{: = {⟦\varnothing ⟧}} \equiv {⟦⟧}}$$y
    $${1 \in B}1{: = {⟦0,1⟧}}$$y $${0^{I} = {1 \land 1^{I}}} = 0$$.
    Además observamos con claridad que
    $$\forall{A \in B}\exists{A^{I} \in B}$$tal
    que$${{A + A^{I}} = {⟦\mathbf{\mathrm{I}}_{\mathbb{Q}}⟧}} = 1$$y
    $${{A \cdot A^{I}} = {⟦⟧}} = 0$$, además de
    $$\forall{A \in B}{{A^{I}}^{I} = A}$$. Así nos queda
    $$A^{I} \equiv \overline{A}$$si se verifican los demás axiomas.

    La suma quedará de la forma antes dada:

    $$\forall A,{B \in \left\lbrack {⟦0,1⟧} \right\rbrack_{\mathbf{\mathrm{I}}}}\exists{\left( {A,B} \right) \subset \left( {A \times B} \right)}{A + B} ≝ {⟦{A \cup B}⟧}$$

    Y el producto seguirá un camino par:

    $$\forall A,{B \in \left\lbrack {⟦0,1⟧} \right\rbrack_{\mathbf{\mathrm{I}}}}\exists{\left( {A,B} \right) \subset \left( {A \times B} \right)}{A \cdot B} ≝ {⟦{A \cap B}⟧}$$

    Sólo queda ver que efectivamente las operaciones son internas (con
    la nueva representación):

    Prueba:

    1.  1.  Ahora vamos a desarrollar la suma por recurrencia:

            $$\forall A,{B \in \left\lbrack {⟦0,1⟧} \right\rbrack_{\mathbf{\mathrm{I}}}}\qquad\exists n,{m \in {\mathbb{N}}_{0}}\mspace{72mu}{B = {⟦{a_{1}^{B},b_{1}^{B},\ldots,a_{n}^{B},b_{n}^{B}}⟧}}\qquad{A = {⟦{a_{1}^{A},b_{1}^{A},\ldots,a_{m}^{A},b_{m}^{A}}⟧}}$$

            Comenzaremos por $$m = 0$$y algunos casos especiales:

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦\varnothing ⟧} & {\Leftarrow} & \begin{Bmatrix}
    {A = {⟦⟧}} \\
    {B = {⟦⟧}}
    \end{Bmatrix} \\
    A & {\Leftarrow} & {B = {⟦\varnothing ⟧}} \\
    B & {\Leftarrow} & {A = {⟦\varnothing ⟧}} \\
    1 & {\Leftarrow} & \begin{Bmatrix}
    {\exists{A \in A}} \\
    {\exists{B \in B}} \\
    {\overline{B} \subseteq A} \\
     \vee \\
    {\overline{A} \subseteq B}
    \end{Bmatrix} \\
    A & {\Leftarrow} & \begin{Bmatrix}
    {\exists{B \in B}} \\
    {\exists{A \in A}} \\
    {B \subseteq A}
    \end{Bmatrix} \\
    B & {\Leftarrow} & \begin{Bmatrix}
    {\exists{A \in A}} \\
    {\exists{B \in B}} \\
    {A \subseteq B}
    \end{Bmatrix}
    \end{Bmatrix}$$

    Distintos casos con $$m = 1$$

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{1}^{A}},{a_{1}^{B},b_{1}^{B}},\ldots,{a_{n}^{B},a_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {b_{1}^{A} \leq a_{1}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{1}^{B}},{a_{2}^{B},b_{2}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {b_{1}^{A} \geq a_{1}^{B}} \\
    {b_{1}^{A} \leq b_{1}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

$${{B + A}{: =}}\begin{Bmatrix}
{⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}},{a_{1}^{B},b_{1}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
{m = 1} \\
{a_{1}^{A} \geq b_{n}^{B}} \\
{b_{1}^{A} \geq b_{n}^{B}}
\end{Bmatrix}
\end{Bmatrix}$$

> 

> $${{B + A}{: =}}\begin{Bmatrix}
> {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{n - 1}^{B},b_{n - 1}^{B}},{a_{n}^{B},b_{1}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
> {m = 1} \\
> {a_{1}^{A} \leq b_{n}^{B}} \\
> {a_{1}^{A} \geq a_{n}^{B}} \\
> {b_{1}^{A} \geq b_{n}^{B}}
> \end{Bmatrix}
> \end{Bmatrix}$$

4.  1.  

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{1}^{A}},{a_{k}^{B},b_{k}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \geq b_{k - 1}^{B}} \\
    {b_{1}^{A} \leq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{k}^{B}},{a_{k + 1}^{B},b_{k + 1}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \geq a_{k}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{k - 1}^{B},b_{k - 1}^{B}},{a_{1}^{A},b_{1}^{A}},{a_{k}^{B},b_{k}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{k < n}} \\
    {a_{1}^{A} \geq b_{k - 1}^{B}} \\
    {a_{1}^{A} \leq a_{k}^{B}} \\
    {b_{1}^{A} \geq b_{k - 1}^{B}} \\
    {b_{1}^{A} \leq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $$\begin{matrix}
    {{B + A}{: =}}
    \end{matrix}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{1}^{A},b_{k}^{B}},{a_{k + 1}^{B},b_{k + 1}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \leq a_{l}^{B}} \\
    {a_{1}^{A} \geq b_{l - 1}^{B}} \\
    {b_{1}^{A} \geq a_{k}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $$\begin{matrix}
    {{B + A}{: =}}
    \end{matrix}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{l}^{B},b_{k}^{B}},{a_{k + l}^{B},b_{k + 1}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \geq a_{l}^{B}} \\
    {a_{1}^{A} \leq b_{l}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}} \\
    {b_{1}^{A} \geq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{l}^{B},b_{1}^{A}},{a_{k + 1}^{B},b_{k + 1}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & {\Leftarrow\begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \geq a_{l}^{B}} \\
    {a_{1}^{A} \leq b_{l}^{B}} \\
    {b_{1}^{A} \geq b_{k}^{B}} \\
    {b_{1}^{A} \leq a_{k + 1}^{B}}
    \end{Bmatrix}}
    \end{Bmatrix}$$

$${{B + A}{: =}}\begin{Bmatrix}
{⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{l}^{B},b_{l}^{B}},{a_{1}^{A},b_{1}^{A}},{a_{k}^{B},b_{k}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & {\Leftarrow\begin{Bmatrix}
{m = 1} \\
{\exists{{l < k} < n}} \\
{a_{1}^{A} \geq b_{l}^{B}} \\
{a_{1}^{A} \leq a_{l + 1}^{B}} \\
{b_{1}^{A} \geq b_{k - 1}^{B}} \\
{b_{1}^{A} \leq a_{k}^{B}}
\end{Bmatrix}}
\end{Bmatrix}$$

5.  $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{l}^{B},b_{l}^{B}},{a_{1}^{A},b_{1}^{A}},{a_{k}^{B},b_{k}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & {\Leftarrow\begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \leq a_{l + 1}^{B}} \\
    {a_{1}^{A} \geq b_{l}^{B}} \\
    {b_{1}^{A} \geq b_{k - 1}^{B}} \\
    {b_{1}^{A} \leq a_{k}^{B}}
    \end{Bmatrix}}
    \end{Bmatrix}$$

    $${{B + A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{l}^{B},b_{k}^{B}},{a_{k + 1}^{B},b_{k + 1}^{B}},\ldots,{a_{n}^{B},b_{n}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \geq a_{l}^{B}} \\
    {a_{1}^{A} \leq b_{l}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}} \\
    {b_{1}^{A} \geq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    Para el caso $$m = 1$$ o $$m = 0$$ y especiales queda demostrado el
    cerramiento de $$B$$bajo esta suma reducida. El caso siguiente se
    construye con facilidad por recurrencia en cualquier número finito
    de pasos. Si hacemos sumas comprobadas ya un número de veces finita,
    queda claro que ya no hay más que demostrar.

    Para cualquier $$m > 1$$:

    $${{B + A}{: =}}\begin{Bmatrix}
    \begin{matrix}
    {B_{1}{: = {B + {⟦{a_{1}^{A},b_{1}^{A}}⟧}}}} \\
    {B_{i}{: = {B_{i - 1} + {⟦{a_{i}^{A},b_{i}^{A}}⟧}}}} \\
     \vdots \\
    {B_{m}{: = {B_{m - 1} + {⟦{a_{m}^{A},b_{m}^{A}}⟧}}}}
    \end{matrix} & {\Leftarrow} & \begin{Bmatrix}
    {{1 \leq i} \leq m} \\
    {A_{0}{: = {⟦\varnothing ⟧}}} \\
    {A_{1}{: = {A_{0} + {⟦{a_{1}^{A},b_{1}^{A}}⟧}}}} \\
    {A_{i + 1}{: = {A_{i} + {⟦{a_{i}^{A},b_{i}^{A}}⟧}}}} \\
    {A{: = A_{m}}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    Queda demostrado que toda suma finita de intervalos genéricos da
    como resultado un intervalos gené­ricos.

    A su vez el producto lo vamos a definir de forma recursiva también,
    comenzando primero con $$A$$ siendo la clase de un solo intervalo
    genérico, o la clase del vacío, además de algu­nos casos especiales.

    $${B \cdot A}{: =}\begin{Bmatrix}
    {⟦\varnothing ⟧} & {\Leftarrow} & \begin{Bmatrix}
    {A = {⟦\varnothing ⟧}} \\
    {B = {⟦\varnothing ⟧}}
    \end{Bmatrix} \\
    A & {\Leftarrow} & {B = 1} \\
    B & {\Leftarrow} & {A = 1} \\
    {⟦\varnothing ⟧} & {\Leftarrow} & \begin{Bmatrix}
    {\exists{B \in B}} \\
    {\exists{A \in A}} \\
    {B \subseteq \overline{A}} \\
     \vee \\
    {A \subseteq \overline{B}}
    \end{Bmatrix} \\
    A & {\Leftarrow} & \begin{Bmatrix}
    {\exists{B \in B}} \\
    {\exists{A \in A}} \\
    {A \subseteq B}
    \end{Bmatrix} \\
    B & {\Leftarrow} & \begin{Bmatrix}
    {\exists{B \in B}} \\
    {\exists{A \in A}} \\
    {B \subseteq A}
    \end{Bmatrix}
    \end{Bmatrix}$$

6.  $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{k - 1}^{B},a_{k - 1}^{B}}}⟧} & {\Leftarrow} & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \geq b_{k - 1}^{B}} \\
    {b_{1}^{A} \leq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{k - 1}^{B},b_{k - 1}^{B}},{a_{k}^{B},b_{1}^{A}}}⟧} & {\Leftarrow} & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \geq a_{k}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{1}^{B}},\ldots,{a_{k - 1}^{B},a_{k - 1}^{B}}}⟧} & {\Leftarrow} & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \geq a_{1}^{B}} \\
    {a_{1}^{A} \leq b_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \geq b_{k - 1}^{B}} \\
    {b_{1}^{A} \leq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{1}^{B}},{a_{2}^{B},b_{2}^{B}},\ldots,{a_{k - 1}^{B},b_{k - 1}^{A}},{a_{k}^{B},b_{k}^{A}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \geq a_{1}^{B}} \\
    {a_{1}^{A} \leq b_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \leq b_{k}^{B}} \\
    {b_{1}^{A} \geq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{B},b_{1}^{B}},\ldots,{a_{k - 1}^{B},b_{k - 1}^{B}},{a_{k}^{B},b_{1}^{A}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {a_{1}^{A} \leq a_{1}^{B}} \\
    {\exists{k < n}} \\
    {b_{1}^{A} \geq a_{k}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},a_{l}^{B}},\ldots,{a_{i}^{B},b_{i}^{B}},\ldots,{a_{k}^{B},b_{1}^{A}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \leq a_{l}^{B}} \\
    {a_{1}^{A} \geq b_{l - 1}^{B}} \\
    {b_{1}^{A} \geq a_{k}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{l}^{B}},\ldots,{a_{i}^{B},b_{i}^{B}},\ldots,{a_{k}^{B},b_{1}^{A}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \geq a_{l}^{B}} \\
    {a_{1}^{A} \leq b_{l}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}} \\
    {b_{1}^{A} \geq a_{k}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {⟦{{a_{1}^{A},b_{l}^{B}},\ldots,{a_{i}^{B},b_{i}^{B}},\ldots,{a_{k - 1}^{B},b_{k - 1}^{B}}}⟧} & \Leftarrow & \begin{Bmatrix}
    {m = 1} \\
    {\exists{{l < k} < n}} \\
    {a_{1}^{A} \geq a_{l}^{B}} \\
    {a_{1}^{A} \leq b_{l}^{B}} \\
    {b_{1}^{A} \leq b_{k}^{B}} \\
    {b_{1}^{A} \geq a_{k - 1}^{B}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    Para el caso $$m = 1$$ o $$m = 0$$ y especiales queda demostrada el
    cerramiento de $$B$$bajo esta suma reducida. El caso siguiente se
    construye con facilidad por recurrencia en cualquier número finito
    de pasos. Si hacemos sumas comprobadas ya un número de veces finita,
    queda claro que ya no hay más que demostrar.

    Para el caso $$m > 1$$:

    $${{B \cdot A}{: =}}\begin{Bmatrix}
    {\sum\limits_{i{: = 1}}^{m}\left( {B \cdot {⟦{a_{i}^{A},b_{i}^{A}}⟧}} \right)} & \Leftarrow & \begin{Bmatrix}
    {{1 < i} \leq m} \\
    {A_{0}{: = {⟦\varnothing ⟧}}} \\
    {A_{1}{: = {A_{0} + {⟦{a_{1}^{A},b_{1}^{A}}⟧}}}} \\
    {A_{i + 1}{: = {A_{i} + {⟦{a_{i}^{A},b_{i}^{A}}⟧}}}} \\
    {A{: = A_{m}}}
    \end{Bmatrix}
    \end{Bmatrix}$$

    Y queda demostrado que la forma del conjunto producto es una clase
    de unión finita de sub-intervalos genéricos. Luego pertenece a
    nuestro álgebra de Boole.

    Este sistema es intuitivamente muy parecido a un álgebra de
    conjuntos sub-álgebra de algún conjunto po­tencia, por lo que es
    fácil determinar que se trata de un álgebra de Boole. Sin embargo su
    cardinalidad es
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
    \end{Bmatrix}} \right)}} \leq$$

    $${{\leq {1 + {\#\left( {\underset{i \in \mathbb{N}}{\mathbf{\mathrm{\cup}}}\underset{j \in \mathbb{N}}{\mathbf{\mathrm{\cup}}}{\mathbb{Q} \times \mathbb{Q}}} \right)}}} = \#}{\left( {{{\mathbb{N} \times \mathbb{N}} \times \mathbb{Q}} \times \mathbb{Q}} \right) = \#}{\mathbb{N} = \aleph_{0}}$$

    En definitiva es un álgebra numerable (del mismo cardinal que los
    números naturales). Luego no existe ningún conjunto para el cual
    esta álgebra de Boole sea semejante a un álgebra de las potencias de
    un conjunto por ser $$\mathbb{N}$$del cardinal infinito más pequeño
    que puede haber, y ningún conjunto finito tiene como potencia uno
    infinito. Este ejemplo será de utilidad más adelante, además de
    darnos un curioso ejemplo de álgebra de Boole nada común.

    **\[Ejemplo 10\]** El álgebra de las funciones de un álgebra de
    Boole sobre otra. Supongamos $$f:{B\rightarrow B}'$$dónde $$f$$ es
    una función. Llamaremos
    $${\mathtt{F}{({B,B'})}} = {\{{f:{B\rightarrow B}' \mid \forall{x \in B}\exists!{y \in B}'f{{(x)} = y}}\}}$$
    a nuestro conjunto de Boole. $$f_{0'}$$ es la función que asigna el
    cero de $$B'$$ a cualquier elemento de $$B$$. Igualmente $$f_{1'}$$
    es la función que asigna el uno de $$B'$$ a cualquier elemento de
    $$B$$. Las operaciones internas a introducir son:

    La suma de funciones:
    $$\forall{x \in B}{\lbrack{f + g}\rbrack}{(x)}{: = f}{{(x)} + g}{(x)}$$dónde
    la segunda suma es la definida en $$B'$$.

    La multiplicación de funciones:
    $$\forall{x \in B}{\lbrack{f \cdot g}\rbrack}{(x)}{: = f}{{(x)} \cdot g}{(x)}$$
    dónde la segunda multiplicación es la definida en $$B'$$.

    La función complemento:
    $$\forall{f \in \mathtt{F}}{({B,B'})}\forall{x \in B}\overline{f}{(x)}{: = \overline{f{(x)}}}$$dónde
    el segundo complemento es el dado anteriormente en $$B'$$.

    De este álgebra podemos entresacar otros conjuntos de funciones
    interesantes, como por ejemplo:

    $${\mathtt{\mathit{Hom}}{({B,B'})}} = \begin{Bmatrix}
    f & : & B & \rightarrow & {B'} & \mathbf{\mid} \\
     & {\forall{x \in B}} & {\exists!{y \in B}'} & {f{{(x)} = y}} & \mathbf{\mathrm{:}} & \\
     & & & & {f{{(0)} = 0}'} & \land \\
     & & & & {f{{(1)} = 1}'} & \land \\
     & & {\forall a,{b \in B}} & & {f{{({a + b})} = f}{{(a)} + f}{(b)}} & \land \\
     & & {\forall a,{b \in B}} & & {f{{({a \cdot b})} = f}{{(a)} \cdot f}{(b)}} & \land \\
     & & {\forall{a \in B}} & & {f{{(\overline{a})} = \overline{f{(a)}}}} & 
    \end{Bmatrix}$$

    y aún otro subconjuntos más pequeños serían las inyecciones de los
    anteriores homomorfismos. Si $${B'} \equiv B$$entonces uno de los
    conjuntos de aplicaciones más interesantes son los endomorfimos o
    isomorfimos en sí mismo.

    Además el kernel de cualquier homomorfismo es un subálgebra de
    $$B$$. Los homomorfismos de las álgebras booleanas tienen
    propiedades interesantes que no veremos aquí.

    4.  Desarrollo de las propiedades generales del álgebra de Boole a
        partir de los axiomas de Huntington.

        1.  Unicidad del
            complementario:$${\forall{a \in B}\forall x,{y \in \widehat{a}}}{x = y}$$

            Prueba:

            $$y{{{{{{= {y \cdot 1}} = {y \cdot {({x + a})}}} = {{({y \cdot x})} + {({y \cdot a})}}} = {{({y \cdot x})} + 0}} = {y \cdot x}} =}$$

            $${{{{{= {x \cdot y}} = {{({x \cdot y})} + 0}} = {{({x \cdot y})} + {({x \cdot a})}}} = {x \cdot {({y + a})}}} = {x \cdot 1}} = x$$

        2.  Definimos **el elemento complementario de otro** , aquel
            elemento de $$B$$
            que$$\forall{a \in B}\exists!{\overline{a} \in B}{\widehat{a} = \left\{ \overline{a} \right\}}$$,
            o dicho de otro modo,

            $$\forall{a \in B}{\left( {{a + \overline{a}} = 1} \right) \land \left( {{a \cdot \overline{a}} = 0} \right)}$$,
            y este elemento es único.

        3.  Distinción necesaria entre un elemento y su complementario:
            $$\forall{a \in B}{a \neq \overline{x}}$$.

            Prueba:

            $${a = \overline{a}}\Rightarrow{{1 = {1 \cdot 1}} = {{({a + a})} \cdot {({a + a})}}}$$

            $$\Rightarrow{1 = {{{{({a \cdot a})} + {({a \cdot a})}} + {({a \cdot a})}} + {({a \cdot a})}}}$$

            $$\Rightarrow{{1 = {{{0 + 0} + 0} + 0}} = 0}$$

            $${1 = 0}\mathit{lo}\mathit{que}\mathit{es}\mathit{absurdo}{- \mathit{es}}\mathit{parte}\mathit{de}\mathit{los}\mathit{postulados}\mathit{que}{\mathbf{1} \neq {\mathbf{0} - ,}}$$

            $$\mathit{luego}{a \neq \overline{a}}$$

        4.  Complementación doble es identidad:
            $$\forall{x \in B}{\overline{\overline{x}} = x}$$

            Prueba:

            $$\forall{x \in B}\exists\mathtt{\mathrm{!}}{\overline{x} \in B}{\left( {{x + \overline{x}} = 1} \right) \land \left( {{x \cdot \overline{x}} = 0} \right)}{\lbrack\mathbf{A}\rbrack}$$

            $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{\exists\mathtt{\mathrm{!}}}{\overline{\overline{x}} \in B}{\left( {{\overline{x} + \overline{\overline{x}}} = 1} \right) \land \left( {{\overline{x} \cdot \overline{\overline{x}}} = 0} \right)}$$

            $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{\exists\mathtt{\mathrm{!}}}{\overline{\overline{x}} \in B}{\left( {{\overline{\overline{x}} + \overline{x}} = 1} \right) \land \left( {{\overline{\overline{x}} \cdot \overline{x}} = 0} \right)}{\lbrack\mathbf{B}\rbrack}$$

            $$\mathit{Comparando}{\lbrack\mathbf{A}\rbrack}y{\lbrack\mathbf{B}\rbrack}y\mathit{por}\mathit{la}\mathit{unicidad}\mathit{del}\mathit{complementario}:$$

            $$\overline{\overline{x}} = x$$

        5.  Para los elementos $$0y1$$:
            $${\overline{0} = 1} \land {\overline{1} = 0}$$

            Prueba:

            $$\begin{matrix}
            {{{0 + 1} = 1}\text{Elemento neutro de la suma.}} \\
            {0{\cdot}1{= 0}\text{Elemento neutro del producto.}}
            \end{matrix}$$

        6.  Leyes de cancelación:

            1.  Para la
                suma:$$\forall x,{y \in B}\left\lbrack {\exists{z \in B}\left\lbrack {\left( {{x + z} = {y + z}} \right) \land \left( {{x + \overline{z}} = {y + \overline{z}}} \right)} \right\rbrack} \right\rbrack\Rightarrow{x = y}$$

                Prueba:

                $${\lbrack\mathit{H1}\rbrack}\exists{z \in B}{{x + z} = {y + z}}$$

                $${\lbrack\mathit{H2}\rbrack}\phantom{\exists{z \in B}}{{x + \overline{z}} = {y + \overline{z}}}$$

                $${\left( {x + z} \right) \cdot \left( {x + \overline{z}} \right)} = {\left( {y + z} \right) \cdot \left( {y + \overline{z}} \right)}$$

                $${x + \left( {z \cdot \overline{z}} \right)} = {y + \left( {z \cdot \overline{z}} \right)}$$

                $${x + 0} = {y + 0}$$

                $$x = y$$

            2.  Para el
                producto:$$\forall x,{y \in B}\left\lbrack {\exists{z \in B}\left\lbrack {\left( {{x \cdot z} = {y \cdot z}} \right) \land \left( {{x \cdot \overline{z}} = {y \cdot \overline{z}}} \right)} \right\rbrack} \right\rbrack\Rightarrow{x = y}$$

                Prueba:

                $${\lbrack\mathit{H1}\rbrack}\exists{z \in B}{{x \cdot z} = {y \cdot z}}$$

                $${\lbrack\mathit{H2}\rbrack}\phantom{\exists{z \in B}}{{x \cdot \overline{z}} = {y \cdot \overline{z}}}$$

                $${\left( {x \cdot z} \right) + \left( {x \cdot \overline{z}} \right)} = {\left( {y \cdot z} \right) + \left( {y \cdot \overline{z}} \right)}$$

                $${x \cdot \left( {z + \overline{z}} \right)} = {y \cdot \left( {z + \overline{z}} \right)}$$

                $${x \cdot 1} = {y \cdot 1}$$

                $$x = y$$

        7.  Unicidad de los neutros:

            1.  Solo hay un $$0$$o elemento neutro de la
                suma:$$\forall{e \in B}{{({\forall{x \in B}{{x + e} = x}})}\Rightarrow{({e = 0})}}$$

                Prueba:

                $$\forall{x \in B}{x + e}{=}x$$

                $$\forall{x \in B}\exists{\overline{x} \in B}{{{\overline{x} \cdot {({x + e})}} = {\overline{x} \cdot x}} = 0}$$

                $$\forall{x \in B}\exists{\overline{x} \in B}{{{{0 = {\overline{x} \cdot {({x + e})}}} = {{\overline{x} \cdot x} + {\overline{x} \cdot e}}} = {0 + {\overline{x} \cdot e}}} = {\overline{x} \cdot e}}$$

                $$x{: = 0}{\overline{x} = 1}{{{0 =} = {1 \cdot e}} = e}$$

                $${\forall{u \in B}\left( {\forall{x \in B}{{x + e} = x}} \right)}\Rightarrow\left( {e = 0} \right)$$

            2.  Solo hay un $$1$$o elemento neutro del
                producto:$$\forall{u \in B}{{({\forall{x \in B}{{x \cdot u} = x}})}\Rightarrow{({u = 1})}}$$

                Prueba:

                $$\forall{x \in B}{x \cdot u}{=}x$$

                $$\forall{x \in B}\exists{\overline{x} \in B}{{{\overline{x} + {({x \cdot u})}} = {\overline{x} + x}} = 1}$$

                $$\forall{x \in B}\exists{\overline{x} \in B}1{{{{= {\overline{x} + {({x \cdot u})}}} = {\overline{x} + x}} = {\overline{x} + u}} = {\overline{x} + u}}$$

                $$x{: = 1}{\overline{x} = 0}{{{1 =} = {0 + u}} = u}$$

                $${\forall{u \in B}\left( {\forall{x \in B}{{x \cdot u} = x}} \right)}\Rightarrow\left( {u = 1} \right)$$

        8.  Propiedad de absorción :

            1.  Para la suma : $$\forall{x \in B}{{x + 1} = 1}$$

                Prueba:

                $$\forall{x \in B}{x \cdot 1}{=}x$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{{{\overline{x} + {({x \cdot 1})}} = {\overline{x} + x}} = 1}$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{{{1 = {\overline{x} + {({x \cdot 1})}}} = {{({\overline{x} + x})} \cdot {({\overline{x} + 1})}}} = {\overline{x} + 1}}$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{1 = {\overline{x} + 1}}$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{\exists\mathtt{\mathrm{!}}}{\overline{\overline{x}} \in B}{1 = {\overline{x} + 1}} \land {1 = {\overline{\overline{x}} + 1}}$$

                $$\forall{x \in B}{1 = {x + 1}}$$

            2.  Para el producto : $$\forall{x \in B}{{x \cdot 0} = 0}$$

                Prueba:

                $$\forall{x \in B}{x + 0}{=}x$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{{{\overline{x} \cdot {({x + 0})}} = {\overline{x} \cdot x}} = 0}$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{{{0 = {\overline{x} \cdot {({x + 1})}}} = {{({\overline{x} \cdot x})} + {({\overline{x} \cdot 0})}}} = {\overline{x} \cdot 0}}$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{0 = {\overline{x} \cdot 0}}$$

                $$\forall{x \in B}{\exists\mathtt{\mathrm{!}}}{\overline{x} \in B}{\exists\mathtt{\mathrm{!}}}{\overline{\overline{x}} \in B}{0 = {\overline{x} \cdot 0}} \land {0 = {\overline{\overline{x}} \cdot 0}}$$

                $$\forall{x \in B}{0 = {x \cdot 0}}$$

        9.  Idempotencia (para retículos en general):

            1.  Para la suma :$$\forall{x \in B}{{x + x} = x}$$

                Prueba:

                $${{{{x = {x + 0}} = {x + {({x \cdot \overline{x}})}}} = {{({x + x})} \cdot {({x + \overline{x}})}}} = {{({x + x})} \cdot 1}} = {x + x}$$

            2.  Para el producto : $$\forall{x \in B}{{x \cdot x} = x}$$

                Prueba:

                $${{{{x = {x \cdot 1}} = {x \cdot {({x + \overline{x}})}}} = {{x \cdot x} + {x \cdot \overline{x}}}} = {{x \cdot x} + 0}} = {x \cdot x}$$

        10. Propiedades de simplificación (para retículos en general):

            1.  $$\forall x,{y \in B}{{x + {({x \cdot y})}} = x}$$

                Prueba:

                $${{{{x + {({x \cdot y})}} = {{({x \cdot 1})} + {({x \cdot y})}}} = {x \cdot {({1 + y})}}} = {x \cdot 1}} = x$$

            2.  $$\forall x,{y \in B}{{x \cdot {({x + y})}} = x}$$

                Prueba:

                $${{{{x \cdot {({x + y})}} = {{({x + 0})} \cdot {({x + y})}}} = {x + {({0 \cdot y})}}} = {x + 0}} = x$$

        11. Una propiedad muy general (para retículos, no sólo para
            álgebras de Boole):

            1.  $$\forall x,{y \in B}{({{x \cdot y} = y})}\Leftrightarrow{({{x + y} = x})}$$

                Prueba:

                $${\lbrack\mathbf{A}\rbrack}{({{x \cdot y} = y})}\Rightarrow{({{({{({x \cdot y})} + x})} = {({y + x})}})}\Rightarrow{({x = {x + y}})}\Rightarrow{({{x + y} = x})}$$

                $${\lbrack\mathbf{B}\rbrack}{({{x + y} = x})}\Rightarrow{({{({{({x + y})} \cdot y})} = {({x \cdot y})}})}\Rightarrow{({y = {x \cdot y}})}\Rightarrow{({{x \cdot y} = y})}$$

                $${{\lbrack\mathbf{A}\rbrack} \land {\lbrack\mathbf{B}\rbrack}}\Rightarrow{({{({{x + y} = x})}\Leftrightarrow{({{x \cdot y} = y})}})}$$

        12. Otra propiedad de simplificación (Shannon):

            1.  $$\forall x,{y \in B}{{{({x + y})} \cdot {({x + \bar{y}})}} = x}$$

                Prueba:

                $${{{{({x + \overline{y}})} \cdot {({x + y})}} = {x + {({\overline{y} \cdot y})}}} = {x + 0}} = x$$

            2.  $$\forall x,{y \in B}{{{({x \cdot y})} + {({x \cdot \bar{y}})}} = x}$$

                Prueba:

                $${{{{({x \cdot \overline{y}})} + {({x \cdot y})}} = {x \cdot {({\overline{y} + y})}}} = {x \cdot 1}} = x$$

        13. Otra propiedad de simplificación (Quine):

            1.  $${{\left( {x \cdot y} \right) + \left( {x \cdot \overline{z}} \right)} + \left( {y \cdot z} \right)} = {\left( {x \cdot \overline{z}} \right) + \left( {y \cdot z} \right)}$$

                Prueba:

                1.  $${{\left( {x \cdot y} \right) + \left( {x \cdot \overline{z}} \right)} + \left( {y \cdot z} \right)} =$$

                    $$= {{\left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{x \cdot y} \cdot \overline{z}} \right)} \right) + \left( {\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {{x \cdot \overline{y}} \cdot \overline{z}} \right)} \right)} + \left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{\overline{x} \cdot y} \cdot z} \right)} \right)}$$

                    $$= {{\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {{x \cdot \overline{y}} \cdot \overline{z}} \right)} \right)} + \left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{\overline{x} \cdot y} \cdot z} \right)} \right)}$$

                    $$= {\left( {\left( {{x \cdot y} \cdot \overline{z}} \right) + \left( {{x \cdot \overline{y}} \cdot \overline{z}} \right)} \right) + \left( {\left( {{x \cdot y} \cdot z} \right) + \left( {{\overline{x} \cdot y} \cdot z} \right)} \right)}$$

                    $$= {\left( {x \cdot \overline{z}} \right) + \left( {y \cdot z} \right)}$$

            2.  $${{\left( {x + y} \right) \cdot \left( {x + \overline{z}} \right)} \cdot \left( {y + z} \right)} = {\left( {x + \overline{z}} \right) \cdot \left( {y + z} \right)}$$

                Prueba:

                1.  $${{\left( {x + y} \right) \cdot \left( {x + \overline{z}} \right)} \cdot \left( {y + z} \right)} =$$

                    $$= {{\left( {\left( {{x + y} + z} \right) \cdot \left( {{x + y} + \overline{z}} \right)} \right) \cdot \left( {\left( {{x + y} + \overline{z}} \right) \cdot \left( {{x + \overline{y}} + \overline{z}} \right)} \right)} \cdot \left( {\left( {{x + y} + z} \right) \cdot \left( {{\overline{x} + y} + z} \right)} \right)}$$

                    $$= {{\left( {{x + y} + \overline{z}} \right) \cdot \left( {\left( {{x + y} + \overline{z}} \right) \cdot \left( {{x + \overline{y}} + \overline{z}} \right)} \right)} \cdot \left( {\left( {{x + y} + z} \right) \cdot \left( {{\overline{x} + y} + z} \right)} \right)}$$

                    $$= {\left( {\left( {{x + y} + \overline{z}} \right) \cdot \left( {{x + \overline{y}} + \overline{z}} \right)} \right) \cdot \left( {\left( {{x + y} + z} \right) \cdot \left( {{\overline{x} + y} + z} \right)} \right)}$$

                    $$= {\left( {x + \overline{z}} \right) \cdot \left( {y + z} \right)}$$

        14. Otra propiedad de simplificación más:

            1.  $$\forall x,{y \in B}{{x + {({\overline{x} \cdot y})}} = {x + y}}$$

                Prueba:

                $${{{x + {({\overline{x} \cdot y})}} = {{({x + \overline{x}})} \cdot {({x + y})}}} = {1 \cdot {({x + y})}}} = {x + y}$$

            2.  $$\forall x,{y \in B}{{x \cdot {({\overline{x} + y})}} = {x \cdot y}}$$

                Prueba:

                $${{{x \cdot {({\overline{x} + y})}} = {{({x \cdot \overline{x}})} + {({x \cdot y})}}} = {0 + {({x \cdot y})}}} = {x \cdot y}$$

        15. Algunos lemas técnicos pre-asociativos bastante útiles:

            1.  Asociatividad cuando dos variables se repiten:

                1.  $$\forall x,{y \in B}{{{x + y} = {x + {({x + y})}}} = {{({x + x})} + y}}$$

                    Prueba:

                    $${}{}{{{{({x + {({x + y})}})} \cdot y} = {{({x \cdot y})} + {({{({x + y})} \cdot y})}}} =}$$

                    $${}{{{= {{({x \cdot y})} + {({{x \cdot y} + {y \cdot y}})}}} = {{({x \cdot y})} + {({{x \cdot y} + y})}}} =}$$

                    $${}{{= {{({x \cdot y})} + y}} = y}{}{}{}\mathit{establece}{\lbrack\mathbf{1}\rbrack}$$

                    $${\lbrack\mathbf{1}\rbrack}{{{({x + {({x + y})}})} \cdot y} = y}$$

                    $${}{}{{{{({x + {({x + y})}})} \cdot x} = {{({x \cdot x})} + {({{({x + y})} \cdot x})}}} =}$$

                    $${}{{{= {{({x \cdot x})} + {({{x \cdot x} + {y \cdot x}})}}} = {{({x \cdot x})} + {({{x \cdot x} + x})}}} =}$$

                    $${}{{= {{({x \cdot x})} + x}} = x}{}{}{}\mathit{establece}{\lbrack\mathbf{2}\rbrack}$$

                    $${\lbrack\mathbf{2}\rbrack}{{{({x + {({x + y})}})} \cdot x} = x}$$

                    $$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}:$$

                    $${{x + y} = {{\lbrack{{({x + {({x + y})}})} \cdot x}\rbrack} + {\lbrack{{({x + {({x + y})}})} \cdot y}\rbrack}}} =$$

                    $${{= {{({x + {({x + y})}})} \cdot {({x + y})}}} = {{({x + {({x + y})}})} \cdot {({{({x + y})} + {({x + y})}})}}} =$$

                    $${= {{({{({x + {({x + y})}})} \cdot {({x + y})}})} + {({{({x + {({x + y})}})} \cdot {({x + y})}})}}} =$$

                    $$= {x + {({x + y})}}$$

                    $${{{({x + x})} + y} = {x + y}} = {x + {({x + y})}}$$

                2.  $$\forall x,{y \in B}{{{x \cdot y} = {x \cdot {({x \cdot y})}}} = {{({x \cdot x})} \cdot y}}$$

                    Prueba:

                    $${}{}{{{{({x \cdot {({x \cdot y})}})} + y} = {{({x + y})} \cdot {({{({x \cdot y})} + y})}}} =}$$

                    $${{= {{({x + y})} \cdot {({{({x + y})} \cdot {({y + y})}})}}} = {{({x + y})} \cdot {({{({x + y})} \cdot y})}}} = {}$$

                    $${{= {{({x + y})} \cdot y}} = y}{}{}{}\mathit{establece}{\lbrack\mathbf{1}\rbrack}$$

                    $${\lbrack\mathbf{1}\rbrack}{{{({x \cdot {({x \cdot y})}})} + y} = y}$$

                    $${}{}{{{{({x \cdot {({x \cdot y})}})} + x} = {{({x + x})} \cdot {({{({x \cdot y})} + x})}}} =}$$

                    $${{= {{({x + x})} \cdot {({{({x + x})} \cdot {({y + x})}})}}} = {{({x + x})} \cdot {({{({x + x})} \cdot {({y + x})}})}}} = {}$$$${{{= {x \cdot {({x \cdot {({y + x})}})}}} = {x \cdot x}} = x}{}{}{}\mathit{establece}{\lbrack\mathbf{2}\rbrack}$$

                    $${\lbrack\mathbf{2}\rbrack}{{{({x \cdot {({x \cdot y})}})} + x} = x}$$

                    $$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}:$$

                    $${{x \cdot y} = {{\lbrack{{({x \cdot {({x \cdot y})}})} + x}\rbrack} \cdot {\lbrack{{({x \cdot {({x \cdot y})}})} + y}\rbrack}}} =$$

                    $${{= {{({x \cdot {({x \cdot y})}})} + {({x \cdot y})}}} = {{({x \cdot {({x \cdot y})}})} + {({{({x \cdot y})} \cdot {({x \cdot y})}})}}} =$$

                    $${= {{({{({x \cdot {({x \cdot y})}})} + {({x \cdot y})}})} \cdot {({{({x \cdot {({x \cdot y})}})} + {({x \cdot y})}})}}} =$$

                    $$= {x \cdot {({x \cdot y})}}$$

                    $${{{({x \cdot x})} \cdot y} = {x \cdot y}} = {x \cdot {({x \cdot y})}}$$

            2.  Asociatividad cuando una de las tres variables es la
                complementaria de otra:

                1.  $${1 = {\overline{x} + {({x + y})}}} = {{({\overline{x} + x})} + y}$$

                    Prueba:

                    $${\lbrack\mathbf{A}\rbrack}{{{{({\overline{x} + {({x + y})}})} \cdot x} = {x + {({x \cdot y})}}} = x}$$

                    $${\lbrack\mathbf{B}\rbrack}{{{{({\overline{x} + {({x + y})}})} \cdot \overline{x}} = {\overline{x} + {({x \cdot y})}}} = \overline{x}}$$

                    $$\mathit{De}{\lbrack\mathbf{A}\rbrack}y\mathit{de}{\lbrack\mathbf{B}\rbrack}\mathit{obtenemos}{\lbrack\mathbf{1}\rbrack}:$$

                    $${\lbrack\mathbf{1}\rbrack}{{{1 = {x + \overline{x}}} = {{({{({\overline{x} + {({x + y})}})} \cdot x})} + {({{({\overline{x} + {({x + y})}})} \cdot \overline{x}})}}} =}$$

                    $${{= {{({\overline{x} + {({x + y})}})} \cdot {({x + \overline{x}})}}} = {{({\overline{x} + {({x + y})}})} \cdot 1}} = {\overline{x} + {({x + y})}}$$

                    $${\lbrack\mathbf{2}\rbrack}{{1 = {1 + y}} = {{({\overline{x} + x})} + y}}$$

                    $$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}:$$

                    $${1 = {\overline{x} + {({x + y})}}} = {{({\overline{x} + x})} + y}$$

                2.  $${0 = {\overline{x} \cdot {({x \cdot y})}}} = {{({\overline{x} \cdot x})} \cdot y}$$

                    Prueba:

                    $${\lbrack\mathbf{A}\rbrack}{{{{({\overline{x} \cdot {({x \cdot y})}})} + x} = {x \cdot {({x + y})}}} = x}$$

                    $${\lbrack\mathbf{B}\rbrack}{{{{({\overline{x} \cdot {({x \cdot y})}})} + \overline{x}} = {\overline{x} \cdot {({x + y})}}} = \overline{x}}$$

                    $$\mathit{De}{\lbrack\mathbf{A}\rbrack}y\mathit{de}{\lbrack\mathbf{B}\rbrack}\mathit{obtenemos}{\lbrack\mathbf{1}\rbrack}:$$

                    $${\lbrack\mathbf{1}\rbrack}{{{0 = {x \cdot \overline{x}}} = {{({{({\overline{x} \cdot {({x \cdot y})}})} + x})} \cdot {({{({\overline{x} \cdot {({x \cdot y})}})} \cdot \overline{x}})}}} =}$$

                    $${{= {{({\overline{x} \cdot {({x \cdot y})}})} + {({x \cdot \overline{x}})}}} = {{({\overline{x} \cdot {({x \cdot y})}})} + 0}} = {\overline{x} \cdot {({x \cdot y})}}$$

                    $${\lbrack\mathbf{2}\rbrack}{{0 = {0 \cdot y}} = {{({\overline{x} \cdot x})} \cdot y}}$$

                    $$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}:$$

                    $${0 = {\overline{x} \cdot {({x \cdot y})}}} = {{({\overline{x} \cdot x})} \cdot y}$$

        16. Leyes de Morgan:

            1.  $$\forall x,{y \in B}{\overline{x+y} = {\overline{x} \cdot \overline{y}}}$$

                Prueba:

                $${{{{{({x + y})} \cdot {({\overline{x} \cdot \overline{y}})}} = {{({x \cdot {({\overline{x} \cdot \overline{y}})}})} + {({y \cdot {({\overline{x} \cdot \overline{y}})}})}}} = {{({x \cdot {({\overline{x} \cdot \overline{y}})}})} + {({y \cdot {({\overline{y} \cdot \overline{x}})}})}}} = {0 + 0}} = 0$$

                $${{{{{({x + y})} + {({\overline{x} \cdot \overline{y}})}} = {{({x + {({\overline{x} \cdot \overline{y}})}})} \cdot {({y + {({\overline{x} \cdot \overline{y}})}})}}} = {{({x + {({\overline{x} \cdot \overline{y}})}})} \cdot {({y + {({\overline{y} \cdot \overline{x}})}})}}} = {1 + 1}} = 1$$

            2.  $$\forall x,{y \in B}{\overline{x\cdot y} = {\overline{x} + \overline{y}}}$$

                Prueba:

                $${{{{{({x \cdot y})} + {({\overline{x} + \overline{y}})}} = {{({x + {({\overline{x} + \overline{y}})}})} \cdot {({y + {({\overline{x} + \overline{y}})}})}}} = {{({x + {({\overline{x} + \overline{y}})}})} \cdot {({y + {({\overline{y} + \overline{x}})}})}}} = {1 \cdot 1}} = 1$$

                $${{{{{({x \cdot y})} \cdot {({\overline{x} + \overline{y}})}} = {{({x \cdot {({\overline{x} + \overline{y}})}})} + {({y \cdot {({\overline{x} + \overline{y}})}})}}} = {{({x \cdot {({\overline{x} + \overline{y}})}})} + {({y \cdot {({\overline{y} + \overline{x}})}})}}} = {0 \cdot 0}} = 0$$

        17. Transformación de la suma y el producto mediante Morgan y
            doble complemento:

            1.  $$\forall x,{y \in B}{{x + y} = \overline{\overline{x}\cdot\overline{y}}}$$

                Prueba:

                $${\{{\overline{x+y} = {\overline{x} \cdot \overline{y}}}\}}\Rightarrow{\{{{x + y} = \overline{\overline{x}\cdot\overline{y}}}\}}$$

            2.  $$\forall x,{y \in B}{{x \cdot y} = \overline{\overline{x}+\overline{y}}}$$

                Prueba:

                $${\{{\overline{({x\cdot y})} = {\overline{x} + \overline{y}}}\}}\Rightarrow{\{{{x \cdot y} = \overline{\overline{x}+\overline{y}}}\}}$$

        18. Asociatividad de las operaciones binarias:

            1.  De la suma:
                $$\forall x,y,{z \in B}{{{({x + y})} + z} = {x + {({y + z})}}}$$

                Prueba:

                $$a{: = {({{({x + y})} + z})}}$$

                $$b{: = {({x + {({y + z})}})}}$$

                $$\overline{b}{= {({\overline{x} \cdot {({\overline{y} \cdot \overline{z}})}})}}$$

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

                $$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}\mathit{que}{\overline{a} = \overline{b}}\Rightarrow{a = b}$$

            2.  De la operación producto:
                $$\forall x,y,{z \in B}{{{({x \cdot y})} \cdot z} = {x \cdot {({y \cdot z})}}}$$

                Prueba:

                $$a{: = {({{({x \cdot y})} \cdot z})}}$$

                $$b{: = {({x \cdot {({y \cdot z})}})}}$$

                $$\overline{b}{= {({\overline{x} + {({\overline{y} + \overline{z}})}})}}$$

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

            3.  $$\mathit{De}{\lbrack\mathbf{1}\rbrack}y\mathit{de}{\lbrack\mathbf{2}\rbrack}\mathit{obtenemos}\mathit{que}{\overline{a} = \overline{b}}\Rightarrow{a = b}$$

        19. Todos los axiomas de los que hemos partido son reducibles al
            siguiente grupo de axiomas:

            1.  Axiomas para un álgebra de Boole con
                solo$$\left\langle {B,@} \right\rangle$$(Sheffer 1933):

                1.  $${\#\left( B \right)} \geq 2$$
                2.  $${{\cdot @} \cdot}:{{B \times B}\rightarrow B}\forall x,{y \in B}\exists!{z \in B}x@{y = z}$$
                3.  $$\forall{x \in B}{({x@x})}@{{({x@x})} = x}$$
                4.  $$\forall x,{y \in B}x@{{({y@{({y@y})}})} = x}@x$$
                5.  $$\forall x,y,{z \in B}{({x@{({y@z})}})}@{{({x@{({y@z})}})} = {({{({y@y})}@x})}}@{({{({z@z})}@x})}$$

            2.  Es muy fácil demostrar que los axiomas de Huntington de
                1903, implican estos 5 axiomas de Sheffer. Los puntos 1
                y 2 son inmediatos, y ya se han definido. También es
                fácil ver que $$x@{x = \overline{x}}$$ (ya se ha visto),
                $$\overline{x}@{{\overline{x} = \overline{\overline{x}}} = x}$$y
                con ello queda probado
                3.$$y@{{({y@y})} = y}@{{{\overline{y} = \overline{({y+\overline{y}})}} = \overline{1}} = 0}$$,
                y de otro lado queda que $$x@{0 = \overline{x}}$$, y el
                punto 4 queda demostrado. El punto 5 lo vamos a reducir
                a expresiones en sumas y productos y negaciones,
                aplicaremos la distributiva y agruparemos de nuevo la
                expresión en la forma deseada. La parte izquierda de la
                igualdad 5 es $${({x@{({y@z})}})}@{({x@{({y@z})}})}$$que
                deshaciendo en sumas y negaciones
                sale$$\overline{\overline{x+\overline{y+z}}}$$donde
                quitando la doble negación y aplicando
                Morgan$$x + {({\overline{y} \cdot \overline{z}})}$$,
                ahora solo aplicamos
                distributiva$${({x + \overline{y}})} \cdot {({x + \overline{z}})}$$
                y ahora aplicamos
                conmutabilidad$${({\overline{y} + x})} \cdot {({\overline{z} + x})}$$y
                reagrupamos en funciones
                "NOR"$$\overline{\overline{\overline{y}+x}+\overline{\overline{z}+x}}$$y
                ya tenemos la igualdad del axioma 5 de Sheffer en su
                parte derecha:$${({{({y@y})}@x})}@{({{({z@z})}@x})}$$.

                Los axiomas de Huntington de 1903 (H03) implican los de
                Sheffer de 1933 (S33). Diremos
                $$\mathit{H03}\Rightarrow\mathit{S33}$$.

            3.  Demostraremos que
                $$\mathit{S33}\Rightarrow\mathit{H03}$$.

                1.  Definición $$x' ≝ x@x$$. Es una aplicación.

                2.  Axioma 3 de Sheffer en una nueva escritura
                    $$x'{' = x}$$.

                3.  Conmutabilidad. $$x@{y = y}@x$$.

                    1.  $$\mathbf{\mathrm{\lbrack{Ax.Sh.5}\rbrack}}{({x@{({y@z})}})}{' = {({y'@x})}}@{({z'@x})}$$
                    2.  $$\mathbf{\mathrm{\lbrack{{{Ax.Sh.5} \land z} = y}\rbrack}}{({x@{({y@y})}})}{' = {({y'@x})}}@{{({y'@x})} = {({y'@x})}}'$$
                    3.  $$\mathbf{\mathrm{\lbrack{{{Ax.Sh.5} \land z} = y}\rbrack}}{({x@{({y'})}})}{' = {({y'@x})}}'$$
                    4.  $$x@{y = {({x@y''})}}'{' = {({y''@x})}}'{' = {y@x}}$$

                4.  Existencia de constante. $$x@x{' = y}@y'$$

                    1.  $${{x@{x'}} = {({x@{x'}})}}'{' =}$$
                    2.  $${= {({x\widehat{+}{x'}})}}'\widehat{+}{{({y\widehat{+}{y'}})} =}$$
                    3.  $${= {({y@{y'}})}}'@{{({x@{x'}})} =}$$
                    4.  $$= {({y@{y'}})}$$

                5.  Definición $$0{: = x}@x'$$. Es una única constante.

                6.  Definición $$1{: = 0}{' = {({x@x'})}}'$$. Es una
                    única constante.

                7.  Definición $${x + y} ≝ {({x@y})}'$$. Es una
                    aplicación.

                8.  Definición $${x \cdot y} ≝ {x'@y'}$$. Es una
                    aplicación.

                9.  Elemento neutro de la suma. $${x + 0} = x$$.

                    1.  $${{x + 0} = {({x@0})}}{' = {({x@0})}}@{{({x@x'})} =}$$
                    2.  $${= {({x@0})}}@{0 = x}'@{0 = x}'{' = x}$$

                10. Elemento neutro del producto. $${x \cdot 1} = x$$.

                    1.  $${{{x \cdot 1} = {x'@0}} = x}'{' = x}$$

                11. Conmutabilidad de la suma: $${x + y} = {y + x}$$.
                    Solo hay que aplicar repetidas veces la
                    conmutabilidad de la "NOR".

                12. Conmutabilidad del producto:
                    $${x \cdot y} = {y \cdot x}$$. Solo hay que aplicar
                    repetidas veces la conmutabilidad de la "NOR".

                13. Distributividad de la suma respecto del producto.

                    $${x + {({y \cdot z})}} = {{({x + y})} \cdot {({x + z})}}$$

                    1.  $${{x + {({y \cdot z})}} = {({x@{({y'@z'})}})}}'{' = {({{({y@x})}@{({z@x})}})}}'{' = {{({x + y})} \cdot {({x + z})}}}$$

                14. Distributividad del producto respecto de la suma.

                    $${x \cdot {({y + z})}} = {{({x \cdot y})} + {({x \cdot z})}}$$

                    1.  $${{x \cdot {({y + z})}} = {({{x'}@{({y@z})}'})}}'{' = {({{({y@z})}@{x'}})}}'{' =}$$
                    2.  $${= {({{({x@y})}@{({x@z})}})}}'{' = {({{({x@y})} + {({x@z})}})}}{' =}$$
                    3.  $${= {({x@y})}}{' \cdot {({x@z})}}{' = {{({x + y})} \cdot {({x + z})}}}$$

                15. Existe elemento complementario.

                    1.  $$\forall x\exists y{{x + y} = 1}$$

                        1.  $$y{: = x}@{x = x}'$$
                        2.  $${x + x}{' = {({x@x'})}}{' = 0}{' = 1}$$

                    2.  $$\forall x\exists y{{x \cdot y} = 0}$$

                        1.  $$y{: = x}@{x = x}'$$
                        2.  $${x \cdot x}{{{' = {x'@x}} = {x@x'}} = 0}$$

                16. Definición: $$\overline{x} ≝ {x@x}{\equiv}x'$$

        20. Todos los axiomas de los que hemos partido son reducibles al
            siguiente grupo de axiomas (nueva interpretación de la
            flecha de Sheffer):

            1.  Axiomas para un álgebra de Boole con
                solo$$\left\langle {B,@} \right\rangle$$(Sheffer 1933):

                1.  $${\#\left( B \right)} \geq 2$$
                2.  $${{\cdot @} \cdot}:{{B \times B}\rightarrow B}\forall x,{y \in B}\exists!{z \in B}x@{y = z}$$
                3.  $$\forall{x \in B}{({x@x})}@{{({x@x})} = x}$$
                4.  $$\forall x,{y \in B}x@{{({y@{({y@y})}})} = x}@x$$
                5.  $$\forall x,y,{z \in B}{({x@{({y@z})}})}@{{({x@{({y@z})}})} = {({{({y@y})}@x})}}@{({{({z@z})}@x})}$$

            2.  Es muy fácil demostrar que los axiomas de Huntington de
                1903, implican estos 5 axiomas de Sheffer. Los puntos 1
                y 2 son inmediatos, y ya se han definido. También es
                fácil ver que $$x@{x = \overline{x}}$$ (ya se ha visto),
                $$\overline{x}@{{\overline{x} = \overline{\overline{x}}} = x}$$y
                con ello queda probado
                3.$$y@{{({y@y})} = y}@{{{\overline{y} = \overline{({y\cdot\overline{y}})}} = \overline{0}} = 1}$$,
                y de otro lado queda que $$x@{1 = \overline{x}}$$, y el
                punto 4 queda demostrado. El punto 5 lo vamos a
                reducirlo a expresiones en sumas y productos y
                negaciones, aplicaremos la distributiva y agruparemos de
                nuevo la expresión en la forma deseada. La parte
                izquierda de la igualdad 5 es
                $${({x@{({y@z})}})}@{({x@{({y@z})}})}$$que deshaciendo
                en sumas y negaciones
                sale$$\overline{\overline{x\cdot\overline{y\cdot z}}}$$donde
                quitando la doble negación y aplicando
                Morgan$$x \cdot {({\overline{y} + \overline{z}})}$$,
                ahora solo aplicamos
                distributiva$${({x \cdot \overline{y}})} + {({x \cdot \overline{z}})}$$
                y ahora aplicamos
                conmutabilidad$${({\overline{y} \cdot x})} + {({\overline{z} \cdot x})}$$y
                reagrupamos en funciones
                "NAND"$$\overline{\overline{\overline{y}\cdot x}\cdot\overline{\overline{z}\cdot x}}$$y
                ya tenemos la igualdad del axioma 5 de Sheffer en su
                parte derecha:$${({{({y@y})}@x})}@{({{({z@z})}@x})}$$.

                Los axiomas de Huntington de 1903 (H03) implican los de
                Sheffer reinterpretados de 1933 (S'33). Diremos
                $$\mathit{H03}\Rightarrow S'33$$.

            3.  Demostraremos que $$S'33\Rightarrow\mathit{H03}$$.

                1.  Definición $$x' ≝ x@x$$. Es una aplicación.

                2.  Axioma 3 de Sheffer en una nueva escritura
                    $$x'{' = x}$$.

                3.  Conmutabilidad. $$x@{y = y}@x$$.

                    1.  $$\mathbf{\lbrack{{Ax.Sh}\mathrm{'}.5}\rbrack}{({x@{({y@z})}})}{' = {({y'@x})}}@{({z'@x})}$$
                    2.  $$\mathbf{\mathrm{\lbrack{{Ax.Sh}'{{.5 \land z} = y}}\rbrack}}{({x@{({y@y})}})}{' = {({y'@x})}}@{{({y'@x})} = {({y'@x})}}'$$
                    3.  $$\mathbf{\mathrm{\lbrack{{Ax.Sh}'{{.5 \land z} = y}}\rbrack}}{({x@{({y'})}})}{' = {({y'@x})}}'$$
                    4.  $$x@{y = {({x@y''})}}'{' = {({y''@x})}}'{' = {y@x}}$$

                4.  Existencia de una expresión constante.
                    $$x@x{' = y}@y'$$

                    1.  $${{x@{x'}} = {({x@{x'}})}}'{' =}$$
                    2.  $${= {({x@{x'}})}}'@{{({y@{y'}})} =}$$
                    3.  $${= {({y@{y'}})}}'@{{({x@{x'}})} =}$$
                    4.  $$= {({y@{y'}})}$$

                5.  Definición $$1{: = x}@x'$$. Es una única constante.

                6.  Definición $$0{: = 1}{' = {({x@x'})}}'$$. Es una
                    única constante.

                7.  Definición $${x \cdot y} ≝ {({x@y})}'$$. Es una
                    aplicación.

                8.  Definición $${x + y} ≝ {x'@y'}$$. Es una aplicación.

                9.  Elemento neutro del producto. $${x \cdot 1} = x$$.

                    1.  $${{x \cdot 1} = {({x@1})}}{' = {({x@1})}}@{{({x@x'})} =}$$
                    2.  $${= {({x@1})}}@{1 = x}'@{1 = x}'{' = x}$$

                10. Elemento neutro de la suma. $${x + 0} = x$$.

                    1.  $${{{x + 0} = {x'@1}} = x}'{' = x}$$

                11. Conmutabilidad del producto:
                    $${x \cdot y} = {y \cdot x}$$. Solo hay que aplicar
                    repetidas veces la conmutabilidad de la "NAND".

                12. Conmutabilidad del producto:
                    $${x \cdot y} = {y \cdot x}$$. Solo hay que aplicar
                    repetidas veces la conmutabilidad de la "NAND".

                13. Distributividad del producto respecto de la suma.

                    $${x \cdot {({y + z})}} = {{({x \cdot y})} + {({x \cdot z})}}$$

                    1.  $${{x \cdot {({y + z})}} = {({x@{({y'@z'})}})}}'{' = {({{({y@x})}@{({z@x})}})}}'{' = {{({x \cdot y})} + {({x \cdot z})}}}$$

                14. Distributividad de la suma respecto del producto.

                    $${x + {({y \cdot z})}} = {{({x + y})} \cdot {({x + z})}}$$

                    1.  $${{x + {({y \cdot z})}} = {({{x'}@{({y@z})}'})}}'{' = {({{({y@z})}@{x'}})}}'{' =}$$
                    2.  $${= {({{({x@y})}@{({x@z})}})}}'{' = {({{({x@y})} + {({x@z})}})}}{' =}$$
                    3.  $${= {({x@y})}}{' + {({x@z})}}{' = {{({x \cdot y})} + {({x \cdot z})}}}$$

                15. Existe elemento complementario.

                    1.  $$\forall x\exists y{{x \cdot y} = 0}$$

                        1.  $$y{: = x}@{x = x}'$$
                        2.  $${x \cdot x}{' = {({x@x'})}}{' = 1}{' = 0}$$

                    2.  $$\forall x\exists y{{x + y} = 1}$$

                        1.  $$y{: = x}@{x = x}'$$
                        2.  $${x + x}{{{' = {x'@x}} = {x@x'}} = 1}$$

                16. Definición: $$\overline{x} ≝ {x@x}{\equiv}x'$$

        21. Lo más habitual es que la flecha de Sheffer se simbolice por
            $$\uparrow$$ cuando es la suma negada, y por
            $$\downarrow$$cuando es el producto negado, tal como lo
            hemos hecho en el anterior texto. Ya que los razonamientos
            hechos con una de las 2 interpretaciones son absolutamente
            simétricos y duales, en vez de hacer referencias a la suma o
            al producto lo hacemos a $${({x \uparrow y})}'$$o a
            $$x' \uparrow y'$$o idénticamente a
            $${({x \downarrow y})}'$$o a $$x' \downarrow y'$$, por lo
            que en vez de diferenciar se usa habitualmente como símbolo
            $$x \mid y$$o "Sheffer's stroke".

        22. Dualidad en el álgebra de Boole.

            1.  Cambiando ***simultáneamente*** todos "0,1,+,\*" por
                (respectivamente) "1,0,\*,+" (más en general, cambiando
                cada valor de un **símbolo constante** de B por su
                complementario, dejando las variables inalteradas,
                aunque la prueba inicial la vamos a hacer permitiendo
                sólo los símbolos "1,0") obtenemos a partir de una
                ex­presión otra con el mismo valor de verdad que la
                primera. A medida que vaya­mos introduciendo nuevos
                operadores veremos como extender esta propiedad de
                dualidad. Se demuestra por inducción sobre cualquier
                expresión bien formada, teniendo en cuenta que todos los
                axiomas son simétricos, duales.

                Prueba:

                Primero hay que construir un lenguaje adecuado para las
                expresiones booleanas (tal como está sirve para hacer un
                programa calculadora de expresiones de Boo­le, aunque no
                programable, ni tampoco se pueden definir variables
                nuevas).

                $$\begin{matrix}
                {{\lbrack\mathbf{\mathit{Constante}}\rbrack}{\mathbf{C}{: =}\mathbf{0}o\mathbf{1}}} \\
                {\mathbf{C}{: =}\mathbf{0}o\mathbf{1}o\mathbf{\Lambda}o\mathbf{\Lambda_{\mathrm{n}}}} \\
                {\mathit{dónde}{\mathbf{n} \in \mathbb{N}}{({\mathit{ha}\mathit{de}\mathit{ser}\mathit{un}\mathit{número}\mathit{concreto}})}y} \\
                {\mathbf{\Lambda},{\mathbf{\Lambda_{\mathrm{n}}} \in {{\{{\alpha,\beta,\gamma,\delta,\epsilon,\theta,\eta,\%,\iota,\chi,\kappa,\lambda,\mu,\nu,\psi,ο,\pi,\rho}\}} \cup}}} \\
                {{\cup {\{{\sigma,\tau,\varepsilon,\varphi,\varsigma,\vartheta,\xi,\upsilon,\zeta,\omega,\varrho,\varpi}\}}}.} \\
                {\mathit{El}\mathit{conjunto}\mathit{de}\mathit{símbolos}\mathit{constantes}\mathit{ha}\mathit{de}\mathit{tener}} \\
                {\mathit{un}\mathit{cardinal}\mathit{menor}o\mathit{igual}\mathit{que}\mathbf{\# B}.} \\
                {\mathit{Estos}\mathit{símbolos}\mathit{tienen}\mathit{un}\mathit{valor}\mathit{concreto}\mathit{booleano}} \\
                {y\mathit{no}\mathit{toman}\mathit{otro}\mathit{valor.}\mathit{Puede}\mathit{haber}\mathit{dos}} \\
                {\mathit{signos}\mathit{constantes}\mathit{distintos}\mathit{con}\mathit{el}\mathit{mismo}} \\
                {\mathit{valor}\mathit{booleano},\mathit{en}\mathit{cuyo}\mathit{caso}\mathit{podemos}\mathit{escribir}\mathit{la}} \\
                {\mathit{igualdad}\mathit{entre}\mathit{los}\mathit{símbolos}\mathit{constantes.}}
                \end{matrix}$$

                $$\begin{matrix}
                {{\lbrack\mathbf{\mathit{Variable}}\rbrack}\mathbf{V}{: =}\mathbf{X}o\mathbf{X_{\mathrm{n}}}} \\
                \mathit{dónde} \\
                {\mathbf{X},{\mathbf{X_{\mathrm{n}}} \in {{\{{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r}\}} \cup}}} \\
                {{\cup {\{{s,t,u,v,w,x,y,z}\}}}\phantom{\{\}}} \\
                {y\mathit{dónde}\mathbf{n}{\in}\mathbf{\mathbb{N}}.}
                \end{matrix}$$

                $$\begin{matrix}
                {\mathit{Lo}\mathit{importante}\mathit{de}\mathit{la}\mathit{variable}\mathbf{X}\mathit{no}\mathit{es}\mathit{que}\mathit{varíe}\mathit{en}\mathit{todo}\mathbf{B},} \\
                {\mathit{sino}\mathit{que}\mathit{varíe}\mathit{en}o\mathit{recorra}{\mathbf{Q_{X}} \subseteq \mathbf{B}},\mathit{tal}\mathit{que}{\mathbf{Q_{X}} \neq \varnothing}.} \\
                {\mathit{Cuando}\mathit{decimos}\mathit{que}\mathit{el}\mathit{dual}\mathit{de}\mathit{una}\mathit{variable}\mathit{es}\mathit{la}\mathit{misma}\mathit{variable},} \\
                {\mathit{no}\mathit{quiere}\mathit{decir}\mathit{que}\mathit{esta}\mathit{variable}\mathit{dual}\mathit{recorra}\mathit{el}\mathit{mismo}\mathit{conjunto}} \\
                {\mathit{de}\mathit{booleanos}\mathit{que}\mathit{la}\mathit{inicial},\mathit{sino}\mathit{que}\mathit{si}\mathit{la}\mathit{inicial}\mathit{tenía}\mathit{elementos},} \\
                {\mathit{la}\mathit{dual}\mathit{también}\mathit{los}\mathit{tiene.}}
                \end{matrix}$$

                $$\begin{matrix}
                {{\lbrack\mathbf{\mathit{Literal}}\rbrack}\mathbf{\mathit{L.p}}{: =}\mathbf{V}o\mathbf{C}} \\
                {\mathbf{L}{: =}\mathbf{\mathit{L.p}}o\overline{\mathbf{\mathit{L.p}}}}
                \end{matrix}$$

                $$\begin{matrix}
                {{\lbrack\mathbf{\mathit{Término}\mathit{Simple}}\rbrack}\mathbf{\mathit{TS.p}}{: =}\mathbf{L}o\left( {{{\cdot \mathbf{L}} \cdot} + {{\cdot \mathbf{L}} \cdot}} \right)o\left( {{{{\cdot \mathbf{L}} \cdot \mathbf{\mathrm{\cdot}}} \cdot \mathbf{L}} \cdot} \right)o\overline{\mathbf{L}}} \\
                {\mathbf{\mathit{TS}}{: =}\mathbf{\mathit{TS.p}}o\mathbf{\overline{\mathit{TS.p}}}} \\
                {\mathit{dónde}\mathit{los}\mathit{signos} \cdot \mathit{débiles}\mathit{significan}\mathit{seguido}ó\mathit{concatenado.}}
                \end{matrix}$$

                $$\begin{matrix}
                {{\lbrack\mathbf{\mathit{Término}}\rbrack}\mathbf{\mathit{T.p}}{: =}\mathbf{\mathit{TS}}o\left( {{{{\cdot \mathbf{\mathit{T.p}}} \cdot \mathbf{+}} \cdot \mathbf{\mathit{TS}}} \cdot} \right)o\left( {{{{\cdot \mathbf{\mathit{T.p}}} \cdot \mathbf{\mathrm{\cdot}}} \cdot \mathbf{\mathit{TS}}} \cdot} \right)} \\
                {{\lbrack\mathbf{\mathit{Término}}\rbrack}\mathbf{T}{: =}\mathbf{\mathit{T.p}}o\overline{\mathbf{\mathit{T.p}}}} \\
                {\mathit{dónde}\mathit{los}\mathit{signos} \cdot \mathit{débiles}\mathit{significan}\mathit{seguido}ó\mathit{concatenado.}}
                \end{matrix}$$

                $${\lbrack\mathbf{\mathit{Expresión}}\rbrack}\mathbf{E}{: =}\mathbf{T{=}T}o\mathbf{T{\neq}T}$$

                Esquema de demostración:

                1.  *Hay que demostrar que para cualquier expresión
                    $$E$$pode­mos encontrar la dual
                    $$\widetilde{E}$$(hasta aquí es sólo formalizar las
                    reglas de los cambios) y que el valor de verdad de
                    $$E$$ y de $$\widetilde{E}$$ son idénticos. Para
                    ello vamos a demos­trarlo primero para igualdades
                    entre literales y des­pués por recursividad para una
                    expresión cualquiera con un literal, y por último
                    para igualdades entre términos cualquiera. El método
                    de demostración será el de induc­ción matemática
                    sobre el número de términos simples en ambos
                    términos de una expresión. Lo haremos
                    indepen­dientemente para el caso de la expresión
                    afirmada y para el caso de la expresión negada.
                    Primero (1) se de­muestra cuando los términos son
                    literales, después (2) se demuestra cuando los
                    términos son términos simples. El siguiente paso (3)
                    es asegurarlo cuando un término es un término simple
                    y el otro un término operado con un término simple,
                    y suponiendo que ya se da la duali­dad sin el añadido
                    (HI), demostrar que se da la duali­dad con el
                    añadidos. El siguiente paso (4) es suponer que si es
                    demostrar cuando los dos son términos supo­niendo
                    dado el caso que un término igual o desigual a un
                    término simple está dado. Por último (5) dado que
                    (HI) implica (3) y (HI) implica (4), suponiendo (2)
                    de­mostramos el caso término operado término simple y
                    tér­mino operado término simple (son 3 casos de
                    operacio­nes) dado (HI). Estamos aprovechando para la
                    demostra­ción la estructura de la gramática
                    construida anterior­mente. En definitiva tendremos
                    los puntos (a.1.cc) , (a.1.cv) , (a.1.vv) ,
                    (a.1.lit.neg) , (a.2.lit.lit) , (a.2.cc+c) ,
                    (a.2.vc+c) , (a.2.vv+c) , (a.2.cc+v) , (a.2.vc+v) ,
                    (a.2.vv+v) , (a.2.cc\*c) , (a.2.vc\*c) , (a.2.vv\*c)
                    , (a.2.cc\*v) , (a.2.vc\*v) , (a.2.vv\*v) ,
                    (a.2.ts.neg) , (a.3.HI.tts+ts) , (a.3.HI.tts\*ts) ,
                    (a.3.HI.tts+ts) , (a.4.HI.ttsts\*) ,
                    (a.5.HI.tts+tts+) , (a.5.HI.tts\*tts\*) ,
                    (a.5.HI.tts+tts\*) , (a.5.HI.t.neg) , y a
                    continuación los puntos dónde se prueba que el dual
                    de una desigual­dad es equivalente a la dual de la
                    misma desigualdad. Habrá que ver previamente que ver
                    cuál es el dual de un recorrido **Q** en **B**, que
                    será el conjunto de los elementos de **B** que son
                    inversos de los elementos de **Q**, ya que para cada
                    constante o valor que tome una variable, el dual
                    será el dual de esa constante o valor, esto es, el
                    complemento de esa constante o valor. Para una
                    variable **a**, el conjunto de valores que recorre
                    es **Q***~***a***~ *. Si necesi­tamos algún conjunto
                    auxiliar lo llamaremos **A** y se de­finirá antes de
                    su uso con la idea que no sea demasiado engorrosa la
                    escritura. Si un conjunto **C** es sin el 1 lo
                    denotaremos por **C***~***\****~ *y si es sin el 0
                    lo denotaremos **C***^***\****^ *y definimos
                    **B***~***2***~***={0,1}** y si un conjunto **C** es
                    sin 0 y sin 1 lo denotamos por **C***^***X***^*.
                    Otro elemento importante son los paréntesis, que
                    permiten una no asociatividad generali­zada entre las
                    diversas operaciones, al no cambiar en absoluto en
                    la expresión dual.*

                2.  Casos en que la expresión $$E$$
                    es$$T_{1} = T_{2}$$afirmativa:

                    ***a.1.cc)*** $$\Lambda_{1} = \Lambda_{2}$$. La
                    expresión dual es
                    $$\overline{\Lambda_{1}} = \overline{\Lambda_{2}}$$.
                    Existe equivalencia cla­ra entre estas 2 expresiones
                    duales.

                    ***a.1.cv)*** $$\Lambda = X$$. El conjunto
                    $$Q_{X{(\Lambda)}} = \left\{ \Lambda \right\}$$ , y
                    así es no vacío. El conjunto dual será
                    $${\widetilde{Q}}_{X{(\Lambda)}} = \left\{ \overline{\Lambda} \right\}$$,
                    que es evidentemente no vacía. La expresión dual es
                    $$\overline{\Lambda} = X$$.

                    ***a.1.vv)*** $$X = Y$$. El conjunto $$Q_{X} = B$$ ,
                    y así es no vacío. El conjunto asociado a $$Y$$ es
                    dependiente de los valores de $$X$$:
                    $$Q_{Y{(X)}} = {B \smallsetminus {\{{\mathit{value}{(X)}}\}}}$$dónde
                    $$\#{\left( \left\{ {\mathit{value}{(X)}} \right\} \right) = 1}$$.
                    De aquí que el con­junto de valores que recorre
                    $$Y$$no es vacío, esto es,
                    $$Q_{Y{(X)}} \neq \varnothing$$. La ex­presión dual
                    será $$\widetilde{X} = \widetilde{Y}$$ que se sigue
                    traduciendo como $$X = Y$$, ya que los conjunto
                    asociados duales que son
                    $${{{\widetilde{Q}}_{X} = \left\{ {{\overline{\alpha} \in B} \mid {\alpha \in B}} \right\}} = B} = Q_{X}$$,
                    y
                    $${\widetilde{Q}}_{Y{(X)}} = {B \smallsetminus \left\{ \overline{\mathit{value}{(X)}} \right\}}$$sigue
                    siendo no vacía. La expresión dual es evi­dentemente
                    equivalente para cada valor de $$X$$.

                    ***a.1.lit.neg)*** Cada literal negado
                    $$\overline{L}$$ es o una variable negada o una
                    cons­tante negada. Cada constante negada no es más
                    que otra constante. Luego si el literal negado es
                    una constante sigue valiendo idénticamente los
                    puntos anteriores. Si el literal negado es una
                    variable digamos $$\overline{X}$$ convertimos
                    $$Q_{X} \neq \varnothing$$ en
                    $$Q_{\overline{X}} = \left\{ {{\overline{x} \in B} \mid {x \in Q_{X}}} \right\}$$
                    que es la misma expresión de
                    $${\widetilde{Q}}_{X}$$, y por lo tanto
                    $$\#{{(Q_{X})} = \#}{{(Q_{\overline{X}})} = \#}{({\widetilde{Q}}_{X})}$$y
                    además
                    $$\#{{({\widetilde{Q}}_{X})} = \#}{{({\widetilde{Q}}_{\overline{X}})} = \#}{{({\widetilde{\widetilde{Q}}}_{X})} = \#}{(Q_{X})}$$.
                    Luego podemos también ver que se trata un caso
                    reducido completamente a los anteriores. Queda
                    demostrado que
                    $${L_{1} = L_{2}}\Leftrightarrow{\widetilde{L_{1}} = \widetilde{L_{2}}}$$
                    .

                    ***a.2.lit.lit)*** Si
                    $$\mathit{TS}_{1} = \mathit{TS}_{2}$$ es tal que
                    $$\mathit{TS}_{1} = L_{1}$$ y
                    $$\mathit{TS}_{2} = L_{2}$$ ya ha queda­do demostrado
                    en el punto (a.1).

                    ***a.2.cc+c)*** El caso
                    $${\Lambda_{1} + \Lambda_{2}} = \Lambda_{3}$$ tiene
                    como expresión dual
                    $${\overline{\Lambda_{1}} \cdot \overline{\Lambda_{2}}} = \overline{\Lambda_{3}}$$que
                    viene justificado por las leyes de De Morgan: ambas
                    expresiones son equivalentes.

                    ***a.2.vc+c)*** El caso $${X + \Lambda} = \Gamma$$
                    tiene como expresión dual
                    $${X \cdot \overline{\Lambda}} = \overline{\Gamma}$$
                    que viene justificado por las leyes de De Morgan,
                    con sólo asegurar que en am­bas expresiones
                    $$X$$recorre un conjunto no vacío. Existen algunas
                    posibili­dades que de inicio sea vacío el recorrido
                    de $$X$$, por ejemplo si $$\Gamma = 0$$ y
                    $$\Lambda = 1$$. En estos casos comprobaremos que
                    $$\widetilde{X}$$ recorre un conjunto
                    $$\varnothing$$. Supongamos que
                    $$\forall{x \in B}{{x + \Lambda} \neq \Gamma}$$y
                    supongamos que
                    $$\exists{y \in B}{{y \cdot \overline{\Lambda}} = \overline{\Gamma}}$$.
                    Y a la inversa: si existe un valor de $$X$$ que haga
                    la ex­presión verdadera entonces existe al menos otro
                    valor de $$\widetilde{X}$$ que hará a la expresión
                    dual igualmente verdadera.

                    Prueba cuando $$X$$ no tiene solución en la
                    expresión:

                    1.  1.  $$\forall{x \in B}{{x + \Lambda} \neq \Gamma}$$$$\land$$$$\exists{y \in B}{{y \cdot \overline{\Lambda}} = \overline{\Gamma}}$$.
                        2.  $${y \cdot \overline{\Lambda}} = \overline{\Gamma}$$
                        3.  $${\left( {y \cdot \overline{\Lambda}} \right) + \left( {x + \Lambda} \right)} = {\overline{\Gamma} + \left( {x + \Lambda} \right)}$$
                        4.  $${\left( {y \cdot \Lambda} \right) + x} = {\overline{\Gamma} + \left( {x + \Lambda} \right)}$$
                        5.  $${{\left( {y + \Lambda} \right) + \overline{\Gamma}} + x} = {\overline{\Gamma} + \left( {x + \Lambda} \right)}$$
                        6.  $${y = 0} = \overline{\Gamma}$$
                        7.  $$\Gamma = 1$$
                        8.  Haciendo $$x = \overline{\Lambda}$$ tenemos
                            que 1. es falso.
                        9.  $$\forall{x \in B}{{x + \Lambda} \neq \Gamma}$$$$\Rightarrow$$$$\forall{x \in B}{{x \cdot \overline{\Lambda}} \neq \overline{\Gamma}}$$.

                    Prueba cuando $$X$$ no tiene solución en la
                    expresión dual:

                    1.  1.  $$\exists{x \in B}{{x + \Lambda} = \Gamma}$$$$\land$$$$\forall{y \in B}{{y \cdot \overline{\Lambda}} \neq \overline{\Gamma}}$$.
                        2.  $${x + \Lambda} = \Gamma$$
                        3.  $${\left( {y \cdot \overline{\Lambda}} \right) + \left( {x + \Lambda} \right)} = {\overline{\Gamma} + \left( {x + \Lambda} \right)}$$
                        4.  $${\left( {x + \overline{\Lambda}} \right) \cdot y} = {\Gamma \cdot \left( {y \cdot \overline{\Lambda}} \right)}$$
                        5.  $${\left( {x + \overline{\Lambda}} \right) \cdot {({y \cdot \Gamma})}} = {\Gamma \cdot \left( {y \cdot \overline{\Lambda}} \right)}$$
                        6.  $$1 = {x \cdot \overline{\Gamma}}$$
                        7.  $$\Gamma = 0$$
                        8.  Haciendo $$y = \Lambda$$ tenemos que 1. es
                            falso.
                        9.  $$\forall{x \in B}{{x \cdot \overline{\Lambda}} \neq \overline{\Gamma}}$$$$\Rightarrow$$$$\forall{x \in B}{{x + \Lambda} \neq \Gamma}$$.

                    Prueba cuando $$X$$ tiene solución en la expresión:

                    1.  1.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\xi + \Lambda} = \Gamma}$$.
                        2.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\overline{\xi} \cdot \overline{\Lambda}} = \overline{\Gamma}}$$
                        3.  $$\exists{\widetilde{Q_{X}} \neq \varnothing}{\widetilde{Q_{X}} \subseteq B}\forall{\xi \in \widetilde{Q_{X}}}{{\xi \cdot \overline{\Lambda}} = \overline{\Gamma}}$$
                        4.  $${X \cdot \overline{\Lambda}} = \overline{\Gamma}$$
                        5.  $${X + \Lambda} = \Gamma$$ $$\Rightarrow$$
                            $${X \cdot \overline{\Lambda}} = \overline{\Gamma}$$

                    Prueba cuando $$X$$ tiene solución en la expresión
                    dual:

                    1.  1.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\xi \cdot \overline{\Lambda}} = \overline{\Gamma}}$$.
                        2.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\overline{\xi} + \Lambda} = \Gamma}$$
                        3.  $$\exists{\widetilde{Q_{X}} \neq \varnothing}{\widetilde{Q_{X}} \subseteq B}\forall{\xi \in \widetilde{Q_{X}}}{{\xi + \Lambda} = \Gamma}$$
                        4.  $${X + \Lambda} = \Gamma$$
                        5.  $${X \cdot \overline{\Lambda}} = \overline{\Gamma}$$
                            $$\Rightarrow$$ $${X + \Lambda} = \Gamma$$

                    ***a.2.vv+c)*** $${X + Y} = \Gamma$$y esta expresión
                    va a ser verdadera. Tenemos que ver su dual
                    $${X + Y} = \overline{\Gamma}$$es también verdadero.
                    Para esto vemos la forma que to­man los conjuntos
                    asociados a las variables $$X\text{e}Y$$. Sea
                    $$Q_{X} = {\{{{\alpha \cdot \Gamma} \mid {\alpha \in B}}\}}$$
                    y
                    $$Q_{Y{(X)}} = {\{{{\overline{\mathit{value}{(X)}} \cdot \Gamma} \mid \mathit{value}{{(X)} \in Q_{X}}}\}}$$.
                    Así en la expresión dual
                    $$\widetilde{Q_{X}} = {\{{{\overline{\alpha} + \overline{\Gamma}} \mid {\alpha \in B}}\}}$$
                    y en
                    $$Q_{Y{(X)}} = {\{{{{\mathit{value}{(X)}} + \overline{\Gamma}} \mid \mathit{value}{{(X)} \in \widetilde{Q_{X}}}}\}}$$,
                    no son vacíos ninguno de los con­juntos asociados,
                    como en la expresión no dual. De hecho a pares
                    tienen el mismo cardinal. Por lo tanto si uno de
                    ellos fuera vacío para una variable también lo sería
                    la en expresión dual, y viceversa.

                    ***a.2.cc+v)*** Veamos el caso
                    $${\Gamma + \Lambda} = X$$. La variable solo puede
                    tomar un va­lor, pero este existe
                    $$Q_{X} = \left\{ {\Gamma + \Lambda} \right\}$$.
                    Luego $$Q_{X}$$no es vacío. La expresión dual
                    $${\overline{\Gamma} \cdot \overline{\Lambda}} = X$$es
                    tal que $$X$$recorre
                    $${{\widetilde{Q}}_{X} = \left\{ {\overline{\alpha} \mid {\alpha \in Q_{X}}} \right\}} = \left\{ {\overline{\Gamma} \cdot \overline{\Lambda}} \right\}$$,
                    que es no vacío, y con el mismo cardinal que
                    $$Q_{X}$$. El camino inverso es similar, probado ya
                    que los cardinales son los mismos.

                    ***a.2.vc+v)*** Este caso corresponde a
                    $${X + \Gamma} = Y$$. Su expresión dual sería
                    $${X \cdot \overline{\Gamma}} = Y$$. Si la expresión
                    es verdadera $${Q_{X} = B} \neq \varnothing$$y
                    $${Q_{Y{(X)}} = \left\{ {\mathit{value}{{(X)} + \Gamma}} \right\}} \neq \varnothing$$.
                    La expresión de los conjuntos asociados a las
                    variables $$X$$ e $$Y$$ en la expresión dual sería
                    $${{\widetilde{Q}}_{X} = B} \neq \varnothing$$, y
                    $${{\widetilde{Q}}_{Y{(X)}} = \left\{ {{\mathit{value}{(X)}} \cdot \overline{\Gamma}} \right\}} \neq \varnothing$$.
                    Al tener los mismos cardinales queda demos­trado lo
                    que queríamos demostrar para el caso afirmativo.
                    Esta expresión y su dual son siempre verdaderas.

                    ***a.2.vv+v)*** El caso $${X + Y} = Z$$ tiene como
                    dual $${X \cdot Y} = Z$$. Solo tenemos que ver los
                    conjuntos asociados $${Q_{X} = B} \neq \varnothing$$
                    , $${Q_{Y} = B} \neq \varnothing$$ ,
                    $${Q_{Z{({X,Y})}} = \left\{ {{\mathit{value}{(X)}} + {\mathit{value}{(Y)}}} \right\}} \neq \varnothing$$
                    , $${{\widetilde{Q}}_{X} = B} \neq \varnothing$$ ,
                    $${{\widetilde{Q}}_{Y} = B} \neq \varnothing$$ ,
                    $${{{\widetilde{Q}}_{Z{({X,Y})}} = {\overline{\mathit{value}{(X)}} \cdot \overline{\mathit{value}{(Y)}}}} = \overline{{\mathit{value}{(X)}}+\overline{\mathit{value}{(Y)}}}} \neq \varnothing$$
                    . Los cardinales de ambos jue­gos de conjuntos
                    asociados, los del original y los del dual son
                    iguales. Esta expresión y su dual son siempre
                    verdaderas.

                    ***a.2.cc\*c)*** El caso
                    $${\Lambda_{1} \cdot \Lambda_{2}} = \Lambda_{3}$$
                    tiene como expresión dual
                    $${\overline{\Lambda_{1}} + \overline{\Lambda_{2}}} = \overline{\Lambda_{3}}$$que
                    viene justificado por las leyes de De Morgan: ambas
                    expresiones son equivalentes.

                    ***a.2.vc\*c)*** El caso
                    $${X \cdot \Lambda} = \Gamma$$ tiene como expresión
                    dual
                    $${X + \overline{\Lambda}} = \overline{\Gamma}$$ que
                    viene justificado por las leyes de De Morgan, con
                    sólo asegurar que en am­bas expresiones $$X$$recorre
                    un conjunto no vacío. Existen algunas posibili­dades
                    que de inicio sea vacío el recorrido de $$X$$, por
                    ejemplo si $$\Gamma = 1$$ y $$\Lambda = 0$$. En
                    estos casos comprobaremos que $$\widetilde{X}$$
                    recorre un conjunto $$\varnothing$$. Supongamos que
                    $$\forall{x \in B}{{x \cdot \Lambda} \neq \Gamma}$$y
                    supongamos que
                    $$\exists{y \in B}{{y + \overline{\Lambda}} = \overline{\Gamma}}$$.
                    Y a la inversa: si existe un valor de $$X$$ que haga
                    la expresión verdadera entonces existe al menos otro
                    valor de $$\widetilde{X}$$ que hará a la expresión
                    dual igualmente verdadera.

                    Prueba cuando $$X$$ no tiene solución en la
                    expresión:

                    1.  1.  $$\forall{x \in B}{{x \cdot \Lambda} \neq \Gamma}$$$$\land$$$$\exists{y \in B}{{y + \overline{\Lambda}} = \overline{\Gamma}}$$.
                        2.  $${y + \overline{\Lambda}} = \overline{\Gamma}$$
                        3.  $${\left( {y + \overline{\Lambda}} \right) + \left( {x \cdot \Lambda} \right)} = {\overline{\Gamma} + \left( {x \cdot \Lambda} \right)}$$
                        4.  $${\left( {y + \overline{\Lambda}} \right) + x} = {\overline{\Gamma} + \left( {x \cdot \Lambda} \right)}$$
                        5.  $${{\left( {y + \overline{\Lambda}} \right) + \overline{\Gamma}} + x} = {\overline{\Gamma} + \left( {x \cdot \Lambda} \right)}$$
                        6.  $${{\left( {y \cdot \Lambda} \right) + {\overline{\Gamma} \cdot \Lambda}} + {x \cdot \Lambda}} = {{\overline{\Gamma} \cdot \Lambda} + \left( {x \cdot \Lambda} \right)}$$
                        7.  $${y \cdot \Lambda} = 0$$
                        8.  $$y = \overline{\Lambda}$$ y de ahí
                            $$\Gamma = \Lambda$$
                        9.  Haciendo $$x = 1$$ tenemos que 1. es falso.
                        10. $$\forall{x \in B}{{x \cdot \Lambda} \neq \Gamma}$$$$\Rightarrow$$$$\forall{y \in B}{{y + \overline{\Lambda}} \neq \overline{\Gamma}}$$.

                    Prueba cuando $$X$$ no tiene solución en la
                    expresión dual:

                    1.  1.  $$\forall{x \in B}{{x + \overline{\Lambda}} \neq \overline{\Gamma}}$$$$\land$$$$\exists{y \in B}{{y \cdot \Lambda} = \Gamma}$$.
                        2.  $${y \cdot \Lambda} = \Gamma$$
                        3.  $${{{({y \cdot \Lambda})} + x} + \overline{\Lambda}} = {{\Gamma + x} + \overline{\Lambda}}$$
                        4.  $${{y + \Lambda} + x} = {{\Gamma + x} + \overline{\Lambda}}$$
                        5.  $${{{\Gamma + y} + \Lambda} + x} = {{\Gamma + x} + \overline{\Lambda}}$$
                        6.  $$y = 0$$
                        7.  $$\Gamma = 0$$
                        8.  $$\forall{x \in B}{{{x + \overline{\Lambda}} \neq \overline{\Gamma}} = 1}$$
                        9.  Haciendo $$x = \Gamma$$ tenemos que 8. es
                            falso y 1. es falso.
                        10. $$\forall{x \in B}{{x + \overline{\Lambda}} \neq \overline{\Gamma}}$$$$\Rightarrow$$$$\forall{y \in B}{{y \cdot \Lambda} \neq \Gamma}$$.

                    Prueba cuando $$X$$ tiene solución en la expresión:

                    1.  1.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\xi \cdot \Lambda} = \Gamma}$$.
                        2.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\overline{\xi} + \overline{\Lambda}} = \overline{\Gamma}}$$
                        3.  $$\exists{\widetilde{Q_{X}} \neq \varnothing}{\widetilde{Q_{X}} \subseteq B}\forall{\xi \in \widetilde{Q_{X}}}{{\xi + \overline{\Lambda}} = \overline{\Gamma}}$$
                        4.  $${X \cdot \overline{\Lambda}} = \overline{\Gamma}$$
                        5.  $${X + \Lambda} = \Gamma$$ $$\Rightarrow$$
                            $${X \cdot \overline{\Lambda}} = \overline{\Gamma}$$

                    Prueba cuando $$X$$ tiene solución en la expresión
                    dual:

                    1.  1.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\xi + \overline{\Lambda}} = \overline{\Gamma}}$$.
                        2.  $$\exists{Q_{X} \neq \varnothing}{Q_{X} \subseteq B}\forall{\xi \in Q_{X}}{{\overline{\xi} \cdot \Lambda} = \Gamma}$$
                        3.  $$\exists{\widetilde{Q_{X}} \neq \varnothing}{\widetilde{Q_{X}} \subseteq B}\forall{\xi \in \widetilde{Q_{X}}}{{\xi \cdot \Lambda} = \Gamma}$$
                        4.  $${X \cdot \Lambda} = \Gamma$$
                        5.  $${X + \overline{\Lambda}} = \overline{\Gamma}$$
                            $$\Rightarrow$$
                            $${X \cdot \Lambda} = \Gamma$$

                    ***a.2.cc\*v)*** Veamos el caso
                    $${\Gamma + \Lambda} = X$$. La variable solo puede
                    tomar un va­lor, pero este existe
                    $$Q_{X} = \left\{ {\Gamma + \Lambda} \right\}$$.
                    Luego $$Q_{X}$$no es vacío. La expresión dual
                    $${\overline{\Gamma} \cdot \overline{\Lambda}} = X$$es
                    tal que $$X$$recorre
                    $${{\widetilde{Q}}_{X} = \left\{ {\overline{\alpha} \mid {\alpha \in Q_{X}}} \right\}} = \left\{ {\overline{\Gamma} \cdot \overline{\Lambda}} \right\}$$,
                    que es no vacío, y con el mismo cardinal que
                    $$Q_{X}$$. El camino inverso es similar, probado ya
                    que los cardinales son los mismos.

                    ***a.2.vc\*v)*** Este caso corresponde a
                    $${X + \Gamma} = Y$$. Su expresión dual sería
                    $${X \cdot \overline{\Gamma}} = Y$$. Si la expresión
                    es verdadera $${Q_{X} = B} \neq \varnothing$$y
                    $${Q_{Y{(X)}} = \left\{ {\mathit{value}{{(X)} + \Gamma}} \right\}} \neq \varnothing$$.
                    La expresión de los conjuntos asociados a las
                    variables $$X$$ e $$Y$$ en la expresión dual sería
                    $${{\widetilde{Q}}_{X} = B} \neq \varnothing$$, y
                    $${{\widetilde{Q}}_{Y{(X)}} = \left\{ {{\mathit{value}{(X)}} \cdot \overline{\Gamma}} \right\}} \neq \varnothing$$.
                    Al tener los mismos cardinales queda demos­trado lo
                    que queríamos demostrar para el caso afirmativo.
                    Esta expresión y su dual son siempre verdaderas.

                    a.2.vv\*c)$${X \cdot Y} = \Gamma$$y esta expresión
                    va a ser verdadera. Tenemos que ver su dual
                    $${X \cdot Y} = \overline{\Gamma}$$es también
                    verdadero. Para esto vemos la forma que toman los
                    conjuntos asociados a las variables $$X\text{e}Y$$.
                    Sea
                    $$Q_{X} = {\{{{\alpha + \Gamma} \mid {\alpha \in B}}\}}$$
                    y
                    $$Q_{Y{(X)}} = {\{{{\overline{\mathit{value}{(X)}} + \Gamma} \mid \mathit{value}{{(X)} \in Q_{X}}}\}}$$.
                    Así en la expresión dual
                    $$\widetilde{Q_{X}} = {\{{{\overline{\alpha} \cdot \overline{\Gamma}} \mid {\alpha \in B}}\}}$$
                    y en
                    $$Q_{Y{(X)}} = {\{{{{\mathit{value}{(X)}} \cdot \overline{\Gamma}} \mid \mathit{value}{{(X)} \in \widetilde{Q_{X}}}}\}}$$,
                    no son vacíos ninguno de los conjuntos asociados,
                    como en la expresión no dual. De hecho a pares
                    tienen el mismo cardinal. Por lo tanto si uno de
                    ellos fuera va­cío para una variable también lo sería
                    la en expresión dual, y viceversa.

                    ***a.2.vv\*v)*** El caso $${X \cdot Y} = Z$$ tiene
                    como dual $${X + Y} = Z$$. Solo tenemos que ver los
                    conjuntos asociados $${Q_{X} = B} \neq \varnothing$$
                    , $${Q_{Y} = B} \neq \varnothing$$ ,
                    $${Q_{Z{({X,Y})}} = \left\{ {{\mathit{value}{(X)}} \cdot {\mathit{value}{(Y)}}} \right\}} \neq \varnothing$$
                    , $${{\widetilde{Q}}_{X} = B} \neq \varnothing$$ ,
                    $${{\widetilde{Q}}_{Y} = B} \neq \varnothing$$ ,
                    $${{{\widetilde{Q}}_{Z{({X,Y})}} = \left\{ {\overline{\mathit{value}{(X)}} + \overline{\mathit{value}{(Y)}}} \right\}} = \left\{ \overline{\left( {{\mathit{value}{(X)}}\cdot{\mathit{value}{(Y)}}} \right)} \right\}} \neq \varnothing$$
                    . Los cardi­nales de ambos juegos de conjuntos
                    asociados, los del original y los del dual son
                    iguales. Esta expresión y su dual son siempre
                    verdaderas.

                    ***a.2.ts.neg)*** El caso
                    $$\mathit{TS} = \overline{\mathit{TS.p}}$$, queda
                    reducido a los casos anteriores ya que
                    $$\mathit{TS.p} = L$$ ,
                    $$\mathit{TS.p} = \left( {L + L} \right)$$ ,
                    $$\mathit{TS.p} = \left( {L \cdot L} \right)$$, que
                    tienen como térmi­nos duales a
                    $${\mathit{TS.p} = \widetilde{L}} = L$$ ,
                    $${\mathit{TS.p} = \left( {\widetilde{L} \cdot \widetilde{L}} \right)} = \left( {L \cdot L} \right)$$
                    ,
                    $${\mathit{TS.p} = \left( {\widetilde{L} + \widetilde{L}} \right)} = \left( {L + L} \right)$$
                    , que son casos todos ellos anteriores.

                    ***a.3.HI.tts+ts)*** La expresión sería una del tipo
                    $${T + \mathit{TS}_{1}} = \mathit{TS}_{2}$$ ,
                    $$T{{{' + \mathit{TS}_{0}} + \mathit{TS}_{1}} = \mathit{TS}_{2}}$$,
                    dónde $$T'$$suponemos (HI) que los valores de ver­dad
                    de $$T_{1}{' = T_{2}}'$$ son idénticos a
                    $$\widetilde{T_{1}}{' = \widetilde{T_{2}}}'$$. Sólo
                    tenemos que de­mostrar que
                    $$T_{1}{{{' + \mathit{TS}_{0}} + \mathit{TS}_{1}} = T_{2}}'$$.
                    Ahora bien $$\mathit{TS}_{0} + \mathit{TS}_{1}$$
                    podemos re­ducirlo finalmente a un literal por
                    evaluación, concretamente a una variable $$X$$ o a
                    una constante $$\Gamma$$. Así nos queda
                    $$T_{1}{{' + L} = T_{2}}{' + 0}$$que entra dentro de
                    la $$\mathit{HI}$$. Así queda demostrado este caso.

                    ***a.3.HI.tts\*ts)*** La expresión sería una del
                    tipo $${T \cdot \mathit{TS}_{1}} = \mathit{TS}_{2}$$
                    ,
                    $$T{{{' \cdot \mathit{TS}_{0}} \cdot \mathit{TS}_{1}} = \mathit{TS}_{2}}$$,
                    dónde $$T'$$suponemos (HI) que los valores de ver­dad
                    de $$T_{1}{' = T_{2}}'$$ son idénticos a
                    $$\widetilde{T_{1}}{' = \widetilde{T_{2}}}'$$. Sólo
                    tenemos que de­mostrar que
                    $$T_{1}{{{' \cdot \mathit{TS}_{0}} \cdot \mathit{TS}_{1}} = T_{2}}'$$.
                    Ahora bien $$\mathit{TS}_{0} \cdot \mathit{TS}_{1}$$
                    podemos reducir­lo finalmente a un literal por
                    evaluación, concretamente a una variable $$X$$ o a
                    una constante $$\Gamma$$. Así nos queda
                    $$T_{1}{{' \cdot L} = T_{2}}{' \cdot 1}$$que entra
                    dentro de la $$\mathit{HI}$$. Así queda demostrado
                    este caso.

                    ***a.5.HI.tts+tts+)*** La expresión sería una del
                    tipo
                    $${T_{1} + \mathit{TS}_{2}} = {T_{2} + \mathit{TS}_{3}}$$
                    ,
                    $$T_{1}{{{' + \mathit{TS}_{0}} + \mathit{TS}_{2}} = T_{2}}{{' + \mathit{TS}_{1}} + \mathit{TS}_{3}}$$,
                    dónde para $$T'$$ suponemos (HI), que los valores de
                    verdad de
                    $$T_{1}{{' + \mathit{TS}_{2}} = T_{2}}{' + \mathit{TS}_{3}}$$
                    son idénticos a los de
                    $$\widetilde{T_{1}}{{' \cdot \widetilde{\mathit{TS}_{2}}} = \widetilde{T_{2}}}{' \cdot \widetilde{\mathit{TS}_{3}}}$$
                    y viceversa. Ahora bien
                    $$\mathit{TS}_{0} + \mathit{TS}_{2}$$ podemos
                    redu­cirlo finalmente a un literal por evaluación,
                    concretamente a una variable $$X$$ o a una constante
                    $$\Gamma$$, e idénticamente para
                    $$\mathit{TS}_{1} + \mathit{TS}_{3}$$. Así nos queda
                    $$T_{1}{{' + L_{1}} = T_{2}}{' + L_{2}}$$que entra
                    dentro de la $$\mathit{HI}$$. Así queda demos­trado
                    este caso.

                    ***a.5.HI.tts\*tts\*)*** La expresión sería una del
                    tipo
                    $${T_{1} \cdot \mathit{TS}_{2}} = {T_{2} \cdot \mathit{TS}_{3}}$$
                    ,
                    $$T_{1}{{{' \cdot \mathit{TS}_{0}} \cdot \mathit{TS}_{2}} = T_{2}}{{' \cdot \mathit{TS}_{1}} \cdot \mathit{TS}_{3}}$$,
                    dónde para $$T'$$ suponemos (HI), que los valores de
                    verdad de
                    $$T_{1}{{' \cdot \mathit{TS}_{2}} = T_{2}}{' \cdot \mathit{TS}_{3}}$$
                    son idénticos a los de
                    $$\widetilde{T_{1}}{{' + \widetilde{\mathit{TS}_{2}}} = \widetilde{T_{2}}}{' + \widetilde{\mathit{TS}_{3}}}$$
                    y viceversa. Ahora bien
                    $$\mathit{TS}_{0} \cdot \mathit{TS}_{2}$$ podemos
                    redu­cirlo finalmente a un literal por evaluación,
                    concretamente a una variable $$X$$ o a una constante
                    $$\Gamma$$, e idénticamente para
                    $$\mathit{TS}_{1} \cdot \mathit{TS}_{3}$$. Así nos
                    que­da
                    $$T_{1}{{' \cdot L_{1}} = T_{2}}{' \cdot L_{2}}$$que
                    entra dentro de la $$\mathit{HI}$$. Así queda
                    demostrado este caso.

                    ***a.5.HI.tts+tts\*)*** La expresión sería una del
                    tipo
                    $${T_{1} \cdot \mathit{TS}_{2}} = {T_{2} \cdot \mathit{TS}_{3}}$$
                    ,
                    $${\left( {T_{1}{' + \mathit{TS}_{0}}} \right) + \mathit{TS}_{2}} = {\left( {T_{2}{' + \mathit{TS}_{1}}} \right) \cdot \mathit{TS}_{3}}$$,
                    dónde para $$T'$$ suponemos (HI), que los valores de
                    verdad de
                    $$T_{1}{{' + \mathit{TS}_{2}} = T_{2}}{' + \mathit{TS}_{3}}$$
                    son idénticos a los de
                    $$\widetilde{T_{1}}{{' \cdot \widetilde{\mathit{TS}_{2}}} = \widetilde{T_{2}}}{' \cdot \widetilde{\mathit{TS}_{3}}}$$
                    y viceversa. Ahora bien
                    $$\mathit{TS}_{0} + \mathit{TS}_{2}$$ podemos
                    redu­cirlo finalmente a un literal por evaluación,
                    concretamente a una variable $$X$$ o a una constante
                    $$\Gamma$$, e idénticamente para
                    $$\mathit{TS}_{1} \cdot \mathit{TS}_{3}$$.
                    $$T_{2}{' \cdot \mathit{TS}_{3}}$$es lo mismo que
                    una $$T_{3}$$ cualquiera (de cualquier longitud).
                    Así nos queda
                    $$T_{1}{{' + L_{1}} = {T_{3} \cdot L_{2}}}$$que ya
                    ha sido demostrado en *a.5.tts+tts+)*. Así queda
                    demostrado este caso.

                    a.5.HI.t.neg) Cualquier T.p negado es susceptible de
                    ser desarrollado (por las leyes de De Morgan) como
                    un T.p y se aplica *a.5.HI.\**.

                3.  Casos en que la expresión $$E$$
                    es$$T_{1} \neq T_{2}$$afirmativa:

                    Estos casos se reduden a que alguna variable siempre
                    es vacía tanto en la ex­presión original como en la
                    dual. Se reducen a los casos anteriores.

        23. Operadores "nor" y "nand" que representaremos
            respectivamente como $$@$$y $$@$$.

            1.  Definición de "nor":
                $${x@y}{: =}{{\overline{x} \cdot \overline{y}} = \overline{x+y}}$$.
            2.  Definición de "nand":
                $${x@y}{: =}{{\overline{x} + \overline{y}} = \overline{x\cdot y}}$$.

        24. No asociatividad en general de "nor" y de "nand". Dar algún
            ejemplo en $$B_{2}$$.

        25. Cualquier expresión de las que hasta ahora se ha podido
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

        26. Ahora podemos establecer el álgebra de Boole en solo función
            de operadores "nor" o sólo de operadores "nand". Los
            postulados de Huntington se establecieron de esta manera,
            aunque con una propiedad que acortaba la longitud total del
            sistema de axiomas. Actualmente se han desarrollado en
            formas cada vez más cortas mediante el postulado de Robinson
            y los de Wolfram más recientemente. (La legibilidad de estos
            sistemas queda definitivamente aniquilada, ya que el sistema
            de pruebas es por lo general un software probador de
            teoremas automático).

        27. Extensión de la dualidad: solo hay que añadir que hay que
            intercambiar todos los operadores "nor" por "nand" y
            viceversa, además de las sustituciones ya enunciadas en
            18.1.

        28. Nuevos operadores "exor" y "exnor".

            1.  Definición del operador "exor":
                $${x \oplus y}{: =}{{{({x \cdot \bar{y}})} + {({\bar{x} \cdot y})}} = {{({x + y})} \cdot {({\bar{x} + \bar{y}})}}}$$
            2.  Definición del operador "exnor":
                $${x \odot y}{: =}{{{({x + \bar{y}})} \cdot {({\bar{x} + y})}} = {{({x \cdot y})} + {({\bar{x} \cdot \bar{y}})}}}$$

        29. Nueva extensión del teorema de dualidad: solo hay que
            intercambiar "exor" por "ex­nor " y viceversa, además de
            todos los intercambios que anteriormente se han des­crito en
            22.

        30. Propiedad de elemento inverso (el inverso de cada elemento
            existe y es él mismo):

            1.  Para la operación "exor" :
                $$\forall{x \in B}x \oplus {x = 0}$$

                Prueba:

                $$x \oplus {{{x = {{({x \cdot \overline{x}})} + {({\overline{x} \cdot x})}}} = {0 + 0}} = 0}$$

            2.  Para la operación "exnor":
                $$\forall{x \in B}x \odot {x = 1}$$

                Prueba:

                $$x \odot {{{x = {{({x + \overline{x}})} \cdot {({\overline{x} + x})}}} = {1 \cdot 1}} = 1}$$

        31. Valor para un elemento operado con su complementario:

            1.  $$\forall{x \in B}x \oplus {\bar{x} = 1}$$

                Prueba:

                $$x \oplus {{{{\bar{x} = {{({x \cdot \overline{\overline{x}}})} + {({\overline{x} \cdot \overline{x}})}}} = {({{({x \cdot x})} + \overline{x}})}} = {x + \overline{x}}} = 1}$$

            2.  $$\forall{x \in B}x \odot {\bar{x} = 0}$$

                Prueba:

                $$x \odot {{{{\overline{x} = {{({x + \overline{\overline{x}}})} \cdot {({\overline{x} + \overline{x}})}}} = {({{({x + x})} \cdot \overline{x}})}} = {x \cdot \overline{x}}} = 0}$$

        32. Más valores de estas operaciones:

            1.  $$\forall{x \in B}x \oplus {1 = \bar{x}}$$

                Prueba:

                $$x \oplus {{{{1 = {{({\overline{x} \cdot 1})} + {({x \cdot \overline{1}})}}} = {\overline{x} + {({x \cdot 0})}}} = {\overline{x} + 0}} = \overline{x}}$$

            2.  $$\forall{x \in B}x \odot {0 = \bar{x}}$$

                Prueba:

                $$x \odot {{{{0 = {{({\overline{x} + 0})} \cdot {({x + \overline{0}})}}} = {\overline{x} \cdot {({x + 1})}}} = {\overline{x} + 1}} = \overline{x}}$$

        33. Elementos neutros:

            1.  $$\forall{x \in B}x \oplus {0 = x}$$

                Prueba:

                $$x \oplus {{{0 = {{({\overline{x} \cdot 0})} + {({x \cdot \overline{0}})}}} = {0 + {({x \cdot 1})}}} = x}$$

            2.  $$\forall{x \in B}x \odot {1 = x}$$

                Prueba:

                $$x \odot {{{1 = {{({\overline{x} + 1})} \cdot {({x + \overline{1}})}}} = {1 \cdot {({x + 0})}}} = x}$$

        34. Una propiedad de simetría:

            1.  $$\forall a,{b \in B}a \oplus {b = \bar{a}} \oplus \bar{b}$$

                Prueba:

                $$a \oplus {{{b = {{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}}} = {{\lbrack{{({\overline{a} \cdot b})} + a}\rbrack} \cdot {\lbrack{{({\overline{a} \cdot b})} + \overline{b}}\rbrack}}} = {{\lbrack{a + b}\rbrack} \cdot {\lbrack{\overline{a} + \overline{b}}\rbrack}}}$$

                $$\overline{a} \oplus {{{{\overline{b} = {{\lbrack{\overline{a} + \overline{b}}\rbrack} \cdot {\lbrack{\overline{\overline{a}} + \overline{\overline{b}}}\rbrack}}} = {{\lbrack{\overline{a} + \overline{b}}\rbrack} \cdot {\lbrack{a + b}\rbrack}}} = {{\lbrack{a + b}\rbrack} \cdot {\lbrack{\overline{a} + \overline{b}}\rbrack}}} = a} \oplus b$$

            2.  $$\forall a,{b \in B}a \odot {b = \bar{a}} \odot \bar{b}$$

                Prueba:

                $$a \odot {{{b = {{({\overline{a} + b})} \cdot {({a + \overline{b}})}}} = {{\lbrack{{({\overline{a} + b})} \cdot a}\rbrack} + {\lbrack{{({\overline{a} + b})} \cdot \overline{b}}\rbrack}}} = {{\lbrack{a \cdot b}\rbrack} + {\lbrack{\overline{a} \cdot \overline{b}}\rbrack}}}$$

                $$\overline{a} \odot {{{{\overline{b} = {{\lbrack{\overline{a} \cdot \overline{b}}\rbrack} + {\lbrack{\overline{\overline{a}} \cdot \overline{\overline{b}}}\rbrack}}} = {{\lbrack{\overline{a} \cdot \overline{b}}\rbrack} + {\lbrack{a \cdot b}\rbrack}}} = {{\lbrack{a \cdot b}\rbrack} + {\lbrack{\overline{a} \cdot \overline{b}}\rbrack}}} = a} \odot b$$

        35. Los operadores negados "nexor" y "nexnor" coinciden
            respectivamente con "exnor" y "exor" (y así no se producen
            nuevos operadores):

            1.  $$\forall a,{b \in B}{{\bar{a\oplus b} \equiv \overline{a\oplus b}} = \overline{a}} \oplus {b = a} \oplus {\overline{b} = a} \odot b$$
            2.  $$\forall a,{b \in B}{{\bar{a\odot b} \equiv \overline{a\odot b}} = \overline{a}} \odot {b = a} \odot {\overline{b} = a} \oplus b$$

        36. Asociatividad de los nuevos operadores "exor" y "exnor":

            1.  $$\forall a,b,{c \in B}{({a \oplus b})} \oplus {c = a} \oplus {({b \oplus c})}$$

                Prueba:

                $${({a \oplus b})} \oplus {c =}$$

                $${= {({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})}} \oplus {c =}$$

                $${= {{({\overline{({{({\overline{a}\cdot b})}+{({a\cdot\overline{b}})}})} \cdot c})} + {({{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot \overline{c}})}}} =$$

                $${= {{({\overline{({{({\overline{a}\cdot b})}+{({a\cdot\overline{b}})}})} \cdot c})} + {({{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot \overline{c}})}}} =$$

                $${= {{{({{({\overline{({\overline{a}\cdot b})} \cdot \overline{({a\cdot\overline{b}})}})} \cdot c})} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                $${= {{{({{({{({a + \overline{b}})} \cdot {({\overline{a} + b})}})} \cdot c})} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                $${= {{{{({{a \cdot b} \cdot c})} + {({{\overline{a} \cdot \overline{b}} \cdot c})}} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                $${= {{({a \cdot {({{({b \cdot c})} + {({\overline{b} \cdot \overline{c}})}})}})} + {({\overline{a} \cdot {({{({\overline{b} \cdot c})} + {({b + \overline{c}})}})}})}}} =$$

                $${= {{({a \cdot {({b \odot c})}})} + {({\overline{a} \cdot {({b \oplus c})}})}}} =$$

                $${= {{({a \cdot \overline{({b\oplus c})}})} + {({\overline{a} \cdot {({b \oplus c})}})}}} =$$

                $${= a} \oplus {({b \oplus c})}$$

            2.  $$\forall a,b,{c \in B}{({a \odot b})} \odot {c = a} \odot {({b \odot c})}$$

                Prueba:

                $${({a \odot b})} \odot {c =}$$

                $${= {({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})}} \odot {c =}$$

                $${= {{({\overline{({{({\overline{a}+b})}\cdot{({a+\overline{b}})}})} + c})} \cdot {({{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + \overline{c}})}}} =$$

                $${= {{({\overline{({{({\overline{a}+b})}\cdot{({a+\overline{b}})}})} + c})} \cdot {({{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + \overline{c}})}}} =$$

                $${= {{{({{({\overline{({\overline{a}+b})} + \overline{({a+\overline{b}})}})} + c})} \cdot {({{\overline{a} + b} + \overline{c}})}} \cdot {({{a + \overline{b}} + \overline{c}})}}} =$$

                $${= {{{({{({{({a \cdot \overline{b}})} + {({\overline{a} \cdot b})}})} + c})} \cdot {({{\overline{a} + b} + \overline{c}})}} \cdot {({{a + \overline{b}} + \overline{c}})}}} =$$

                $${= {{{{({{a \cdot b} \cdot c})} + {({{\overline{a} \cdot \overline{b}} \cdot c})}} + {({{\overline{a} \cdot b} \cdot \overline{c}})}} + {({{a \cdot \overline{b}} \cdot \overline{c}})}}} =$$

                $${= {{({a \cdot {({{({b \cdot c})} + {({\overline{b} \cdot \overline{c}})}})}})} + {({\overline{a} \cdot {({{({\overline{b} \cdot c})} + {({b + \overline{c}})}})}})}}} =$$

                $${= {{({a + {({b \oplus c})}})} \cdot {({\overline{a} + {({b \odot c})}})}}} =$$

                $${= {{({a \cdot \overline{({b\oplus c})}})} + {({\overline{a} \cdot {({b \oplus c})}})}}} =$$

                $${= a} \odot {({b \odot c})}$$

        37. Distributividad de "$$\oplus$$" respecto del producto lógico
            "$$\cdot$$" y de "$$\odot$$" res­pecto de la suma lógica
            "$$+$$":

            1.  $$\forall x,y,{z \in B}{{x \cdot {({y \oplus z})}} = {({x \cdot y})}} \oplus {({x \cdot z})}$$

                Prueba:

                $${{x \cdot {({y \oplus z})}} = {({x \cdot y})}} \oplus {({x \cdot z})}$$

                $${\lbrack\mathbf{A}\rbrack}{{{({x \cdot {({y \oplus z})}})} \cdot \overline{({{({x\cdot y})}\oplus{({x\cdot z})}})}} =}$$

                $${= {{({x \cdot {({y \oplus z})}})} \cdot {({{({x \cdot y})} \odot {({x \cdot z})}})}}} =$$

                $${= {{({x \cdot {({y \oplus z})}})} \cdot {({\overline{({x\cdot y})} \oplus {({x \cdot z})}})}}} =$$

                $${= {{({x \cdot {({{({\overline{y} \cdot z})} + {({y \cdot \overline{z}})}})}})} \cdot {({{({{({x \cdot y})} \cdot {({x \cdot z})}})} + {({\overline{({x\cdot y})} \cdot \overline{({x\cdot z})}})}})}}} =$$

                $${= {{{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({{x \cdot y} \cdot z})}} + {{{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({\overline{x} + \overline{y}})}} \cdot {({\overline{x} + \overline{z}})}}}} =$$

                $${= {{{{({x\overline{y}z})} \cdot {({xyz})}} + {{({xy\overline{z}})} \cdot {({xyz})}}} + {{({{({x\overline{y}z})} + {({xy\overline{z}})}})} \cdot {({{\overline{x} + \overline{x}}{\overline{z} + \overline{x}}{\overline{y} + \overline{y}}\overline{z}})}}}} =$$
                $${= {{0 + 0} + {{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({\overline{x} + {\overline{y} \cdot \overline{z}}})}}}} =$$

                $${= {{{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot \overline{x}} + {{({{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}})} \cdot {({\overline{y} \cdot \overline{z}})}}}} =$$

                $${= {{{{x \cdot {({{\overline{y} \cdot z} + {y \cdot \overline{z}}})}} \cdot \overline{x}} + {{({{x \cdot \overline{y}} \cdot z})} \cdot {({\overline{y} \cdot \overline{z}})}}} + {{({{x \cdot y} \cdot \overline{z}})} \cdot {({\overline{y} \cdot \overline{z}})}}}} =$$

                $${= {{0 + 0} + 0}} = 0$$

                $${\lbrack\mathbf{B}\rbrack}{{{({x \cdot {({y \oplus z})}})} + \overline{({{({x\cdot y})}\oplus{({x\cdot z})}})}} =}$$

                $${= {{({x \cdot {({y \oplus z})}})} + {({{({x \cdot y})} \odot {({x \cdot z})}})}}} =$$

                $${= {{({x \cdot {({y \oplus z})}})} + {({\overline{({x\cdot y})} \oplus {({x \cdot z})}})}}} =$$

                $${= {{({x \cdot {({{({\overline{y} \cdot z})} + {({y \cdot \overline{z}})}})}})} + {({{({{({x \cdot y})} \cdot {({x \cdot z})}})} + {({\overline{({x\cdot y})} \cdot \overline{({x\cdot z})}})}})}}} =$$

                $${= {{{{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}} + {({{x \cdot y} \cdot z})}} + {({{({\overline{x} + \overline{y}})} \cdot {({\overline{x} + \overline{z}})}})}}} =$$

                $${= {{{{({{x \cdot \overline{y}} \cdot z})} + {({{x \cdot y} \cdot \overline{z}})}} + {({{x \cdot y} \cdot z})}} + {({\overline{x} + {\overline{y} \cdot \overline{z}}})}}} =$$

                $${= {{{{{{x \cdot \overline{y}} \cdot z} + {{x \cdot y} \cdot \overline{z}}} + {{x \cdot y} \cdot z}} + \overline{x}} + {\overline{y} \cdot \overline{z}}}} =$$

                $${= {{{{{{{{{{x \cdot \overline{y}} \cdot z} + {{x \cdot y} \cdot \overline{z}}} + {{x \cdot y} \cdot z}} + {{\overline{x} \cdot y} \cdot z}} + {{\overline{x} \cdot y} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot z}} + {{x \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot \overline{z}}}} =$$
                $${= {{{{{{{{{x \cdot \overline{y}} \cdot z} + {{x \cdot y} \cdot \overline{z}}} + {{x \cdot y} \cdot z}} + {{x \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot y} \cdot z}} + {{\overline{x} \cdot y} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot \overline{z}}} + {{\overline{x} \cdot \overline{y}} \cdot z}}} =$$

                $${= {{x \cdot {({{{{\overline{y} \cdot z} + {y \cdot \overline{z}}} + {y \cdot z}} + {\overline{y} \cdot \overline{z}}})}} + {\overline{x} \cdot {({{{{y \cdot z} + {y \cdot \overline{z}}} + {\overline{y} \cdot \overline{z}}} + {\overline{y} \cdot z}})}}}} =$$

                $${= {{{{\overline{y} \cdot z} + {y \cdot \overline{z}}} + {y \cdot z}} + {\overline{y} \cdot \overline{z}}}} =$$

                $${= {{\overline{y} \cdot {({z + \overline{z}})}} + {y \cdot {({z + \overline{z}})}}}} =$$

                $${= {z + \overline{z}}} = 1$$

                $$\text{De}{\lbrack\mathbf{A}\rbrack}\text{y de}{\lbrack\mathbf{B}\rbrack}\text{se obtiene que}{\overline{({x\cdot{({y\oplus z})}})} = \overline{({{({x\cdot y})}\oplus{({x\cdot z})}})}}$$

                $$\text{Y de aquí, por la unicidad del complementario obtenemos}$$

                $${{x \cdot {({y \oplus z})}} = {({x \cdot y})}} \oplus {({x \cdot z})}$$

                Es seguro que la prueba anterior puede ser acortada
                drásticamente, así que si al­guno encuentra una forma
                (quizás más directa) la pondremos en su lugar.

            2.  $$\forall x,y,{z \in B}{{x + {({y \odot z})}} = {({x + y})}} \odot {({x + z})}$$Se
                prueba como en el caso anterior, sólo que cambiando los
                operadores duales, y las dos constantes $$\{{0,1}\}$$
                entre sí y obtenemos el resultado que hemos enunciado.

                Prueba:

                $${{x + {({y \odot z})}} = {({x + y})}} \odot {({x + z})}$$

                $${\lbrack\mathbf{A}\rbrack}{{{({x + {({y \odot z})}})} + \overline{({{({x+y})}\odot{({x+z})}})}} =}$$

                $${= {{({x + {({y \odot z})}})} + {({{({x + y})} \oplus {({x + z})}})}}} =$$

                $${= {{({x + {({y \odot z})}})} + {({\overline{({x+y})} \odot {({x + z})}})}}} =$$

                $${= {{({x + {({{({\overline{y} + z})} \cdot {({y + \overline{z}})}})}})} + {({{({{({x + y})} + {({x + z})}})} \cdot {({\overline{({x+y})} + \overline{({x+z})}})}})}}} =$$

                $${= {{{{({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})} + {{({{x + y} + z})} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}}} + {({\overline{x} \cdot \overline{y}})}} + {({\overline{x} \cdot \overline{z}})}}} =$$

                $$= {{{{({{x + \overline{y}} + z})} + {{({{x + y} + z})} \cdot {({{x + y} + \overline{z}})}}} + {{({{x + y} + z})} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}}} +}$$

                $${+ {({{{{\overline{x} \cdot \overline{x}} + {\overline{z} \cdot \overline{x}}} + {\overline{y} \cdot \overline{y}}} + \overline{z}})}} =$$

                $${= {{{1 \cdot 1} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}} + {({{\overline{x} \cdot \overline{y}} + \overline{z}})}}} =$$

                $${= {{{({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})} + {\overline{x} \cdot {({{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}})}}} + {({\overline{y} + \overline{z}})}}} =$$

                $${= {{{{x + {({{\overline{y} + {z \cdot y}} + \overline{z}})}} + {\overline{x} \cdot {({{x + \overline{y}} + z})}}} + {{({\overline{y} + \overline{z}})} \cdot {({{x + y} + \overline{z}})}}} + {({\overline{y} + \overline{z}})}}} =$$

                $${= {{1 \cdot 1} \cdot 1}} = 1$$

                $${\lbrack\mathbf{B}\rbrack}{{{({x + {({y \odot z})}})} \cdot \overline{({{({x+y})}\odot{({x+z})}})}} =}$$

                $${= {{({x + {({y \odot z})}})} \cdot {({{({x + y})} \oplus {({x + z})}})}}} =$$

                $${= {{({x + {({y \odot z})}})} \cdot {({\overline{({x+y})} \odot {({x + z})}})}}} =$$

                $${= {{({x + {({{({\overline{y} + z})} \cdot {({y + \overline{z}})}})}})} \cdot {({{({{({x + y})} + {({x + z})}})} \cdot {({\overline{({x+y})} + \overline{({x+z})}})}})}}} =$$

                $${= {{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot \left( {\left( {\overline{x} \cdot \overline{y}} \right) + \left( {\overline{x} \cdot \overline{z}} \right)} \right)}} =$$

                $${= {{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot {({\overline{x} \cdot {({\overline{y} + \overline{z}})}})}}} =$$

                $$= {{{{{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot {({{\overline{x} + y} + z})}} \cdot {({{\overline{x} + y} + \overline{z}})}} \cdot {({{\overline{x} + \overline{y}} + \overline{z}})}} \cdot}$$

                $${{{\cdot {({{\overline{x} + \overline{y}} + z})}} \cdot {({{x + \overline{y}} + \overline{z}})}} \cdot {({{\overline{x} + \overline{y}} + \overline{z}})}} =$$

                $$= {{{{{{{({{x + \overline{y}} + z})} \cdot {({{x + y} + \overline{z}})}} \cdot {({{x + y} + z})}} \cdot {({{x + \overline{y}} + \overline{z}})}} \cdot {({{\overline{x} + y} + z})}} \cdot {({{\overline{x} + y} + \overline{z}})}} \cdot}$$

                $${{\cdot {({{\overline{x} + \overline{y}} + \overline{z}})}} \cdot {({{\overline{x} + \overline{y}} + z})}} =$$

                $${= {{({x + {({{{{({\overline{y} + z})} \cdot {({y + \overline{z}})}} \cdot {({y + z})}} \cdot {({\overline{y} + \overline{z}})}})}})} \cdot {({\overline{x} + {({{{{({y + z})} \cdot {({y + \overline{z}})}} \cdot {({\overline{y} + \overline{z}})}} \cdot {({\overline{y} + z})}})}})}}} =$$

                $${= {{{{({\overline{y} + z})} \cdot {({y + \overline{z}})}} \cdot {({y + z})}} \cdot {({\overline{y} + \overline{z}})}}} =$$

                $${= {{({\overline{y} + {({z \cdot \overline{z}})}})} \cdot {({y + {({z \cdot \overline{z}})}})}}} =$$

                $${= {z \cdot \overline{z}}} = 0$$

                $$\text{De}{\lbrack\mathbf{A}\rbrack}\text{y de}{\lbrack\mathbf{B}\rbrack}\text{se obtiene que}{\overline{({x+{({y\odot z})}})} = \overline{({{({x+y})}\odot{({x+z})}})}}$$

                $$\text{Y de aquí, por la unicidad del complementario obtenemos}$$

                $${{x + {({y \odot z})}} = {({x + y})}} \odot {({x + z})}$$

        38. Estructuras de anillo conmutativo con elemento unidad (es
            claro desde todas las pro­piedades anteriormente
            demostradas):

            1.  La más normal sería:
                $$({B,{{\{ 0,1\}} \subseteq B},{0 \neq 1}, \oplus , \cdot})$$
            2.  Su forma dual es
                :$$({B,{{\{ 0,1\}} \subseteq B},{0 \neq 1}, \odot , +})$$

        39. Estructuras respectivas a 38 de bimódulo
            de$$({B^{n}, \oplus})$$sobre el anillo
            $$({B, \oplus , \cdot})$$ y el dual, de
            $$({B^{n}, \odot})$$sobre el anillo $$({B, \odot , +})$$.

        A continuación hablaremos sobre como son en general las álgebras
        de Boole, funda­mentalmente las finitas, y veremos que
        efectivamente podemos llegar a teoremas que nos dicen de forma
        muy concreta cuales son estas álgebras de Boole. Vamos a ver
        for­mas de generarlas y cuestiones parecidas.

        40. En el caso que el cardinal de $$B$$sea finito,
            $$2 \mid {({\# B})}$$. Para demostrarlo solo hay que darse
            cuenta que $${B = \cup_{x \in B}}{\{{x,\overline{x}}\}}$$,
            que
            $${({{x \neq {y \land \overline{x}}} \neq y})}\Rightarrow{({{{\{{x,\overline{x}}\}} \cap {\{{y,\overline{y}}\}}} = \varnothing})}$$
            y que $$\forall{x \in B}\#{{\{{x,\overline{x}}\}} = 2}$$ y
            así cuando$$B$$sea finito, su cardinal será un múlti­plo de
            2.

        41. Definición:

            $$\forall x,{y \in B}{x \leq y}\Leftrightarrow{{x \cdot y} = x}\Leftrightarrow{{x + y} = y}$$

        42. $$\left\langle {B, \leq} \right\rangle\text{es un}\mathit{orden}$$.

            1.  Reflexiva: $$\forall{x \in B}{x \leq x}$$.

                1.  $$\forall{x \in B}{{x \cdot x} = x}$$
                2.   $$\forall{x \in B}{x \leq x}$$

            2.  Antisimétrica:
                $$\forall x,{y \in B}{{x \leq {y \land y}} \leq x}\Rightarrow{x = y}$$

                1.  $$x,{y \in B}{{x \leq {y \land y}} \leq x}$$.
                2.  $$x,{y \in B}{{{x \cdot y} = {{y \land x} \cdot y}} = x}$$.
                3.  $$x,{y \in B}{x = y}$$.

            3.  Transitiva:
                $$\forall x,y,{z \in B}{{x \leq {y \land y}} \leq z}\Rightarrow{x \leq z}$$

                1.  $${x \leq {y \land y}} \leq z$$
                2.  $${{x \cdot y} = {{x \land y} \cdot z}} = y$$
                3.  $${{x \cdot y} \cdot z} = {x \cdot z}$$
                4.  $${x \cdot y} = {x \cdot z}$$
                5.  $$x = {x \cdot z}$$
                6.  $$x \leq z$$

        43. Definición:

            $$\forall x,{y \in B}{x \geq y}\Leftrightarrow{{x \cdot y} = y}\Leftrightarrow{{x + y} = x}$$

        44. $$\left\langle {B, \geq} \right\rangle\text{es un}\mathit{orden}$$.

            1.  Reflexiva: $$\forall{x \in B}{x \geq x}$$.

                1.  $$\forall{x \in B}{{x + x} = x}$$
                2.   $$\forall{x \in B}{x \geq x}$$

            2.  Antisimétrica:
                $$\forall x,{y \in B}{{x \geq {y \land y}} \geq x}\Rightarrow{x = y}$$

                1.  $$x,{y \in B}{{x \geq {y \land y}} \geq x}$$.
                2.  $$x,{y \in B}{{{x + y} = {{y \land x} + y}} = x}$$.
                3.  $$x,{y \in B}{x = y}$$.

            3.  Transitiva:
                $$\forall x,y,{z \in B}{{x \geq {y \land y}} \geq z}\Rightarrow{x \geq z}$$

                1.  $${x \geq {y \land y}} \geq z$$
                2.  $${{x + y} = {{x \land y} + z}} = y$$
                3.  $${{x + y} + z} = {x + z}$$
                4.  $${x + y} = {x + z}$$
                5.  $$x = {x + z}$$
                6.  $$x \geq z$$

        45. Definición:

            $$\mathsf{\mathit{atom}}_{B}{(x)}\Leftrightarrow_{\text{def}}{\left\lbrack {x \in \lbrack 1,0)_{B}} \right\rbrack \land \left\lbrack {\forall{y \in \lbrack 1,0)_{B}}\left( {\left( {{x \cdot y} = x} \right) \vee \left( {{x \cdot y} = 0} \right)} \right)} \right\rbrack}$$.

        46. $$\forall x,{y \in B}\mathsf{\mathit{atom}}_{B}{{(x)} \land \mathsf{\mathit{atom}}_{B}}{{(y)} \land {({x \neq y})}}\Rightarrow{{x \cdot y} = 0}$$.

        47. Definición:

            $$\mathsf{\mathit{htom}}_{B}{(x)}\Leftrightarrow_{\text{def}}{\left\lbrack {x \in (1,0\rbrack_{B}} \right\rbrack \land \left\lbrack {\forall{y \in (1,0\rbrack_{B}}\left( {\left( {{x + y} = x} \right) \vee \left( {{x + y} = 1} \right)} \right)} \right\rbrack}$$.

        48. $$\forall x,{y \in B}\mathsf{\mathit{htom}}_{B}{{(x)} \land \mathsf{\mathit{htom}}_{B}}{{(y)} \land {({x \neq y})}}\Rightarrow{{x + y} = 1}$$.

        49. Definición*$${x \in B}\Rightarrow{\lbrack{x,0}\rbrack}_{B}{: = {\{{{y \in B} \mid {y \leq x}}\}}}$$*.

        50. $$\#{{\lbrack{x,0}\rbrack}_{B} = 1}\Leftrightarrow{{\lbrack{x,0}\rbrack}_{B} = {\{ 0\}}}\Leftrightarrow{x = 0}$$.

        51. Definición*$${x \in B}\Rightarrow{\lbrack{1,x}\rbrack}_{B}{: = {\{{{y \in B} \mid {y \geq x}}\}}}$$*.

        52. $$\#{{\lbrack{1,x}\rbrack}_{B} = 1}\Leftrightarrow{{\lbrack{1,x}\rbrack}_{B} = {\{ 1\}}}\Leftrightarrow{x = 1}$$.

        53. Definición*$$x,{y \in B}{x \geq y}\Rightarrow\left\lbrack {x,y} \right\rbrack_{B}{: = {\{{{z \in B} \mid {{y \leq {z \land x}} \geq z}}\}}}$$*.

        54. Definición*$$x,{y \in B}{x \geq y}\Rightarrow\left\lbrack {x,y} \right)_{B}{: = {\{{{z \in B} \mid {{{y \leq {z \land x}} \geq {z \land z}} \neq y}}\}}}$$*.

        55. Definición*$$x,{y \in B}{x \geq y}\Rightarrow\left( {x,y} \right\rbrack_{B}{: = {\{{{z \in B} \mid {{{y \leq {z \land x}} \geq {z \land z}} \neq x}}\}}}$$*.

        56. Definición*$$x,{y \in B}{x \geq y}\Rightarrow\left( {x,y} \right)_{B}{: = {\{{{z \in B} \mid {{{{y \leq {z \land x}} \geq {z \land z}} \neq {x \land z}} \neq y}}\}}}$$*.

        57. *$${x \in B}\Rightarrow{{{\lbrack{x,0}\rbrack}_{B} \cap {\lbrack{1,x}\rbrack}_{B}} = {\{ x\}}}$$*.

        58. *$${x \in B}\Rightarrow{{{\lbrack{x,0}\rbrack}_{B} \cap {\lbrack{\overline{x},0}\rbrack}_{B}} = {\{ 0\}}}$$*.

        59. *$${x \in B}\Rightarrow{{{\lbrack{1,x}\rbrack}_{B} \cap {\lbrack{1,\overline{x}}\rbrack}_{B}} = {\{ 1\}}}$$*.

        60. *$$\forall{x \in B}\forall{y \in \left( {x,0} \right\rbrack_{B}}{{({{\lbrack{y,0}\rbrack}_{B} \subset {\lbrack{x,0}\rbrack}_{B}})} \land {({{\lbrack{y,0}\rbrack}_{B} \neq {\lbrack{x,0}\rbrack}_{B}})}}$$*.

        61. *$$\forall{x \in B}\forall{y \in \left\lbrack {1,x} \right)_{B}}{{({{\lbrack{1,y}\rbrack}_{B} \subset {\lbrack{1,x}\rbrack}_{B}})} \land {({{\lbrack{1,y}\rbrack}_{B} \neq {\lbrack{1,x}\rbrack}_{B}})}}$$*.

        62. Definición*$$\mathit{Atom}B{: = {\{{{x \in \lbrack 1,0)_{B}} \mid \mathsf{\mathit{atom}}_{B}{(x)}}\}}}$$*.

        63. Definición*$$\mathit{Htom}B{: = {\{{{x \in (1,0\rbrack_{B}} \mid \mathsf{\mathit{htom}}_{B}{(x)}}\}}}$$*.

        64. *$$\mathit{Atom}{{(B_{2})} = {{\{ 1\}} \land \mathit{Htom}}}{{(B_{2})} = {\{ 0\}}}$$*.

        65. Definición
            *$$\left\lbrack B \right){: = {\{{{A \subset B} \mid \exists{x \in B}{\left\lbrack {A = \left\lbrack {x,0} \right)_{B}} \right\rbrack \land \left\lbrack {\left( {x,0} \right)_{B} \neq \varnothing} \right\rbrack}}\}}}$$*.

        66. *$$\left\lbrack B \right) \neq \varnothing$$*. Pues es un
            álgebra de cardinal mayor o igual que 2 y existe al menos
            $$\{ 1\}$$.

        67. *$${\langle{\left\lbrack B \right), \supseteq}\rangle}\mathit{es}\mathit{un}\mathit{orden}$$*.

        68. *$$B\mathit{finito}\forall{P \subset \left\lbrack B \right)}{\langle{P, \supseteq}\rangle}\mathit{orden}\mathit{total}\Rightarrow\exists!{x \in \underset{X \in P}{\cap}}X\mathsf{\mathit{atom}}_{B}{(x)}$$*.

            Prueba:

            1.  $${\langle{P, \supseteq}\rangle}\mathit{es}\mathit{un}\mathit{orden}\mathit{total}$$
            2.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{{X \supset {Y \vee Y}} \supset X}$$
            3.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{\left( {\left( {Y \supset X} \right) \vee \left( {Y \supset X} \right)} \right) \land \left( {\left( {{Y \cap X} = X} \right) \vee \left( {{Y \cap X} = Y} \right)} \right)}$$
            4.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{\left( {\left( {{Y \cap X} = X} \right) \vee \left( {{Y \cap X} = Y} \right)} \right) \land \left( {{X \neq {{\{ 0\}} \land Y}} \neq {\{ 0\}}} \right)}$$
            5.  $$\forall X,{Y \in P}\left( {X \neq Y} \right)\Rightarrow\left( {{Y \cap X} \neq {\{ 0\}}} \right)$$
            6.  $$\underset{X \in P}{\cap}{X \neq {{\{ 0\}} \land \underset{X \in P}{\cap}}}{X \supset {\{ 0\}}}$$
            7.  $$\underset{Y \in P}{\cap}Y \supsetneq {\{ 0\}}$$
            8.  $$\underset{Y \in P}{\cap}{Y \supseteq {\{{0,x}\}}}$$
            9.  $$\underset{Y \in P}{\cap}{Y \supseteq {\lbrack{x,0}\rbrack}_{B}}$$
            10. $$\underset{Y \in P}{\cap}{{Y \supseteq {\lbrack{x,0}\rbrack}_{B}} \supseteq {\{{0,x}\}}}$$
            11. $${\lbrack{x,0}\rbrack}_{B} \in P$$
            12. $$\exists{X \in P}\exists{x \in X}{\underset{Y \in P}{\cap}{Y = {\lbrack{x,0}\rbrack}_{B}}}$$
            13. $$\exists!{x \in B}{\underset{Y \in P}{\cap}{Y = {\lbrack{x,0}\rbrack}_{B}}}$$
            14. $$\exists{x \in {\underset{Y \in P}{\cap}Y{{\lbrack{x,0}\rbrack}_{B} = {\{{0,x}\}}}}}$$
            15. $$\exists{x \in {\underset{Y \in P}{\cap}Y\forall{X \in P}{{X \supseteq {\lbrack{x,0}\rbrack}_{B}} = {\{{0,x}\}}}}}$$
            16. $$\forall{P \subset \left\lbrack B \right)}{\langle{P, \supseteq}\rangle}\mathit{orden}\mathit{total}\Rightarrow\exists!{x \in \underset{X \in P}{\cap}}X\mathsf{\mathit{atom}}_{B}{(x)}$$

        69. 
            $$B\mathit{finito}\Rightarrow\mathit{Atom}{B \neq \varnothing}$$.
            Desde 68 es inmediato.

        70. Todo $$B ≝ {{\{{s,i}\}} \simeq B_{2}}$$(no hace falta
            construir el isomorfismo realmente desde que se pueden
            representar sus elementos por una caracterización única).

            Prueba:

            1.  $$\varphi:{B\rightarrow B_{2}}::{x\rightarrow\begin{Bmatrix}
                {0\Leftarrow{x = s}} \\
                {1\Leftarrow{x = i}}
                \end{Bmatrix}}$$

            2.  $$\varphi$$es una biyección que respeta el $$1/s$$ y el
                $$0/i$$.

            3.  $$\varphi$$Respeta la adición booleana:

                1.  $$\varphi{{{({x + y})} = \begin{Bmatrix}
                    {1\Leftarrow{{({x,y})} = {({s,s})}}} \\
                    {1\Leftarrow{{({x,y})} = {({s,i})}}} \\
                    {0\Leftarrow{{({x,y})} = {({i,i})}}} \\
                    {1\Leftarrow{{({x,y})} = {({i,s})}}}
                    \end{Bmatrix}} =}$$
                2.  $${= \begin{Bmatrix}
                    {{1 + 1}\Leftarrow{{({x,y})} = {({s,s})}}} \\
                    {{1 + 0}\Leftarrow{{({x,y})} = {({s,i})}}} \\
                    {{0 + 0}\Leftarrow{{({x,y})} = {({i,i})}}} \\
                    {{0 + 1}\Leftarrow{{({x,y})} = {({i,s})}}}
                    \end{Bmatrix}} =$$
                3.  $${{= \begin{Bmatrix}
                    {\varphi{{(s)} + \varphi}{(s)}\Leftarrow{{({x,y})} = {({s,s})}}} \\
                    {\varphi{{(s)} + \varphi}{(i)}\Leftarrow{{({x,y})} = {({s,i})}}} \\
                    {\varphi{{(i)} + \varphi}{(i)}\Leftarrow{{({x,y})} = {({i,i})}}} \\
                    {\varphi{{(i)} + \varphi}{(s)}\Leftarrow{{({x,y})} = {({i,s})}}}
                    \end{Bmatrix}} = \varphi}{{(x)} + \varphi}{(y)}$$

            4.  $$\varphi$$Respeta el producto booleano:

                1.  $$\varphi{{{({x \cdot y})} = \begin{Bmatrix}
                    {1\Leftarrow{{({x,y})} = {({s,s})}}} \\
                    {0\Leftarrow{{({x,y})} = {({s,i})}}} \\
                    {0\Leftarrow{{({x,y})} = {({i,i})}}} \\
                    {0\Leftarrow{{({x,y})} = {({i,s})}}}
                    \end{Bmatrix}} =}$$
                2.  $${= \begin{Bmatrix}
                    {{1 \cdot 1}\Leftarrow{{({x,y})} = {({s,s})}}} \\
                    {{1 \cdot 0}\Leftarrow{{({x,y})} = {({s,i})}}} \\
                    {{0 \cdot 0}\Leftarrow{{({x,y})} = {({i,i})}}} \\
                    {{0 \cdot 1}\Leftarrow{{({x,y})} = {({i,s})}}}
                    \end{Bmatrix}} =$$
                3.  $${{= \begin{Bmatrix}
                    {\varphi{{(s)} \cdot \varphi}{(s)}\Leftarrow{{({x,y})} = {({s,s})}}} \\
                    {\varphi{{(s)} \cdot \varphi}{(i)}\Leftarrow{{({x,y})} = {({s,i})}}} \\
                    {\varphi{{(i)} \cdot \varphi}{(i)}\Leftarrow{{({x,y})} = {({i,i})}}} \\
                    {\varphi{{(i)} \cdot \varphi}{(s)}\Leftarrow{{({x,y})} = {({i,s})}}}
                    \end{Bmatrix}} = \varphi}{{(x)} \cdot \varphi}{(y)}$$

            5.  $$\varphi$$Respeta el complementario:

                1.  $$\varphi{{{(\overline{x})} = \begin{Bmatrix}
                    {1\Leftarrow{x = i}} \\
                    {0\Leftarrow{x = s}}
                    \end{Bmatrix}} =}$$
                2.  $${= \begin{Bmatrix}
                    {\overline{0}\Leftarrow{x = i}} \\
                    {\overline{1}\Leftarrow{x = s}}
                    \end{Bmatrix}} =$$
                3.  $${= \begin{Bmatrix}
                    {\overline{\varphi{(i)}}\Leftarrow{x = i}} \\
                    {\overline{\varphi{(s)}}\Leftarrow{x = s}}
                    \end{Bmatrix}} = \overline{\varphi{(x)}}$$

        71. Caracterización de $$B_{2}$$. Las siguientes afirmaciones
            son equivalentes:

            1.  $$\#{B = 2}$$
            2.  $${1 \in \mathit{Atom}}{(B)}$$
            3.  $${0 \in \mathit{Htom}}{(B)}$$
            4.  $$\exists{\mathit{xy} \in {\mathit{Atom}{{(B)} \times \mathit{Htom}}{(B)}}}{{x \neq {y \land x}} > y}$$
            5.  $$B = B_{2}$$

        72. Definición
            $$y\mathsf{\mathit{minimal}}x\Leftrightarrow_{\text{def}}\mathsf{\mathit{atom}}_{B}{{{{(y)} \land x} \cdot y} = y}\Leftrightarrow\mathsf{\mathit{atom}}_{B}{{{(y)} \land y} \leq x}$$

        73. Ahora veremos que para cada elemento $$x$$ no atómico de
            $$B^{\ast}$$ con $$B \neq B_{2}$$ existe algún elemento
            atómico $$y$$ tal que $$y \leq x$$. Más formalmente

            1.  $$\forall{x \in B^{\ast}}\exists{y \in B}y\mathsf{\mathit{minimal}}x$$.

                Prueba:

            2.  $$\left\lbrack {x,0} \right\rbrack_{B}\text{es un álgebra de Boole}$$

                Tiene igual o más de 2 elementos.

            3.  $${{{\lbrack{x,0}\rbrack}_{B} \supseteq {{\{{x,0}\}} \land x}} \neq 0}\Rightarrow\#{{({\lbrack{x,0}\rbrack})} \geq 2}$$

                El producto tal cual es interno.

            4.  $$\forall{\mathit{yz} \in \left\lbrack {x,0} \right\rbrack_{B}}{{{{{y \cdot z} \leq y} \leq {{x \land y} \cdot z}} \leq z} \leq x}$$

            5.  $$\forall{\mathit{yz} \in \left\lbrack {x,0} \right\rbrack_{B}}{{y \cdot z} \in \left\lbrack {x,0} \right\rbrack_{B}}$$

                La suma tal cual es interna.

            6.  $$\forall{\mathit{yz} \in \left\lbrack {x,0} \right\rbrack_{B}}{{{{({y + z})} \cdot x} = {{({y \cdot x})} + {({z \cdot x})}}} = {y + z}}$$

            7.  $$\forall{\mathit{yz} \in \left\lbrack {x,0} \right\rbrack_{B}}{{y + z} \leq x}$$

            8.  $$\forall{\mathit{yz} \in \left\lbrack {x,0} \right\rbrack_{B}}{{y + z} \in \left\lbrack {x,0} \right\rbrack_{B}}$$

                $$x$$es la unidad.

            9.  $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{z \leq x}$$

            10. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{z \cdot x} = z}$$

                $$0$$ es el cero.

            11. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{0 + z} = z}$$

                Definimos un nuevo complementario.

            12. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{z'} ≝ {x \cdot \overline{z}}}$$

                Es interno.

            13. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{z'} \leq x}$$

            14. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{z'} \in \left\lbrack {x,0} \right\rbrack_{B}}$$

                Hace lo que tiene que hacer un complementario.

            15. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{{{{z'} + z} = {{x \cdot \overline{z}} + z}} = {x + z}} = x}$$

            16. $$\forall{z \in \left\lbrack {x,0} \right\rbrack_{B}}{{{{z'} \cdot z} = {{x \cdot \overline{z}} \cdot z}} = 0}$$

                Aplicamos la existencia de elementos átomos y que $$x$$
                no lo es.

            17. $$\mathsf{\mathit{atom}}_{B}{(x)}\Rightarrow{\left( {x,0} \right)_{B} \neq \varnothing}$$

            18. $$\exists{y \in \mathit{Atom}}{(\left\lbrack {x,0} \right\rbrack_{B})}$$

            19. $$y < x$$

        74. Definición
            *$$\left( B \right\rbrack{: = {\{{{A \subset B} \mid \exists{x \in B}{\left\lbrack {A = \left\lbrack {1,x} \right)_{B}} \right\rbrack \land \left\lbrack {\left( {1,x} \right)_{B} \neq \varnothing} \right\rbrack}}\}}}$$*.

        75. *$$\left( B \right\rbrack \neq \varnothing$$*. Pues es un
            álgebra de cardinal mayor o igual que 2 y existe al menos
            $$\{ 0\}$$.

        76. *$${\langle{\left( B \right\rbrack, \subseteq}\rangle}\mathit{es}\mathit{un}\mathit{orden}$$*.

        77. *$$B\mathit{finito}\forall{P \subset \left( B \right\rbrack}{\langle{P, \subseteq}\rangle}\mathit{orden}\mathit{total}\Rightarrow\exists!{x \in \underset{X \in P}{\cap}}X\mathsf{\mathit{atom}}_{B}{(x)}$$*.

            Prueba:

            1.  $${\langle{P, \subseteq}\rangle}\mathit{es}\mathit{un}\mathit{orden}\mathit{total}$$
            2.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{{X \subset {Y \vee Y}} \subset X}$$
            3.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{\left( {\left( {Y \subset X} \right) \vee \left( {Y \subset X} \right)} \right) \land \left( {\left( {{Y \cap X} = X} \right) \vee \left( {{Y \cap X} = Y} \right)} \right)}$$
            4.  $$\forall X,{Y \in P}{X \neq Y}\Rightarrow{\left( {\left( {{Y \cap X} = X} \right) \vee \left( {{Y \cap X} = Y} \right)} \right) \land \left( {{X \neq {{\{ 1\}} \land Y}} \neq {\{ 1\}}} \right)}$$
            5.  $$\forall X,{Y \in P}\left( {X \neq Y} \right)\Rightarrow\left( {{Y \cap X} \neq {\{ 1\}}} \right)$$
            6.  $$\underset{X \in P}{\cap}{X \neq {{\{ 1\}} \land \underset{X \in P}{\cap}}}{X \supset {\{ 1\}}}$$
            7.  $$\underset{Y \in P}{\cap}Y \supsetneq {\{ 1\}}$$
            8.  $$\underset{Y \in P}{\cap}{Y \supseteq {\{{1,x}\}}}$$
            9.  $$\underset{Y \in P}{\cap}{Y \supseteq {\lbrack{1,x}\rbrack}_{B}}$$
            10. $$\underset{Y \in P}{\cap}{{Y \supseteq {\lbrack{1,x}\rbrack}_{B}} \supseteq {\{{0,x}\}}}$$
            11. $${\lbrack{1,x}\rbrack}_{B} \in P$$
            12. $$\exists{X \in P}\exists{x \in X}{\underset{Y \in P}{\cap}{Y = {\lbrack{1,x}\rbrack}_{B}}}$$
            13. $$\exists!{x \in B}{\underset{Y \in P}{\cap}{Y = {\lbrack{1,x}\rbrack}_{B}}}$$
            14. $$\exists{x \in {\underset{Y \in P}{\cap}Y{{\lbrack{1,x}\rbrack}_{B} = {\{{1,x}\}}}}}$$
            15. $$\exists{x \in {\underset{Y \in P}{\cap}Y\forall{X \in P}{{X \supseteq {\lbrack{1,x}\rbrack}_{B}} = {\{{1,x}\}}}}}$$
            16. $$\forall{P \subset \left( B \right\rbrack}{\langle{P, \subseteq}\rangle}\mathit{orden}\mathit{total}\Rightarrow\exists!{x \in \underset{X \in P}{\cap}}X\mathsf{\mathit{htom}}_{B}{(x)}$$

        78. 
            $$B\mathit{finito}\Rightarrow\mathit{Htom}{{(B)} \neq \varnothing}$$.
            Desde 74 es inmediato.

        79. Definición
            $$y\mathsf{\mathit{maximal}}x\Leftrightarrow_{\text{def}}\mathsf{\mathit{htom}}_{B}{{{{(y)} \land x} \cdot y} = y}\Leftrightarrow\mathsf{\mathit{htom}}_{B}{{{(y)} \land y} \leq x}$$

        80.  Ahora veremos que para cada elemento $$x$$ de $$B_{\ast}$$
            con $$B \neq B_{2}$$ existe algún elemento atómico $$y$$ tal
            que $$y \geq x$$. Más formalmente

            1.  $$\forall{x \in B_{\ast}}\exists{y \in B}y\mathsf{\mathit{maximal}}x$$.

                Prueba:

            2.  $$\left\lbrack {1,x} \right\rbrack_{B}\text{es un álgebra de Boole}$$

                Tiene 2 elementos o más.

            3.  $${{x \neq {1 \land {\{{1,x}\}}}} \subseteq \left\lbrack {1,x} \right\rbrack_{B}}\Rightarrow\#{\left\lbrack {1,x} \right\rbrack_{B} \geq 2}$$

                El producto tal cual es interno.

            4.  $$\forall{\mathit{yz} \in \left\lbrack {1,x} \right\rbrack_{B}}{{{{{y + z} \geq y} \geq {{x \land y} + z}} \geq z} \geq x}$$

            5.  $$\forall{\mathit{yz} \in \left\lbrack {1,x} \right\rbrack_{B}}{{y + z} \in \left\lbrack {1,x} \right\rbrack_{B}}$$

                La suma tal cual es interna.

            6.  $$\forall{\mathit{yz} \in \left\lbrack {1,x} \right\rbrack_{B}}{{{{({y \cdot z})} + x} = {{({y + x})} \cdot {({z + x})}}} = {y + z}}$$

            7.  $$\forall{\mathit{yz} \in \left\lbrack {1,x} \right\rbrack_{B}}{{y \cdot z} \geq x}$$

            8.  $$\forall{\mathit{yz} \in \left\lbrack {1,x} \right\rbrack_{B}}{{y \cdot z} \in \left\lbrack {1,x} \right\rbrack_{B}}$$

                $$x$$es el cero.

            9.  $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{z \geq x}$$

            10. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{z + x} = z}$$

                $$1$$ es el uno.

            11. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{1 \cdot z} = z}$$

                Definimos un nuevo complementario.

            12. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{z'} ≝ {x + \overline{z}}}$$

                Es interno.

            13. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{z'} \geq x}$$

            14. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{z'} \in \left\lbrack {1,x} \right\rbrack_{B}}$$

                Hace lo que tiene que hacer un complementario.

            15. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{{{{{z'} \cdot z} = {{({x + \overline{z}})} \cdot z}} = {{({x \cdot z})} + {({\overline{z} \cdot z})}}} = {x \cdot z}} = x}$$

            16. $$\forall{z \in \left\lbrack {1,x} \right\rbrack_{B}}{{{{{z'} + z} = {{x + \overline{z}} + z}} = {x + 1}} = 1}$$

                Aplicamos la existencia de elementos hiperátomos y que
                $$x$$ no lo es.

            17. $${x \notin \mathit{Htom}}{(B)}\Rightarrow{\left( {1,x} \right)_{B} \neq \varnothing}$$

            18. $$\exists{y \in \mathit{Htom}}{(\left\lbrack {1,x} \right\rbrack_{B})}$$

            19. $$y \geq x$$

        81. Vamos a ver ahora que, si $${\#{(B)}} > 4$$ para cada $$x$$
            no átomo ni $$0$$ no solo encontramos un $$y$$ minimal de
            $$x$$(como ya hemos demostrado) sino que podemos encontrar
            al menos otro átomo $$z$$ minimal de $$x$$, $$z \neq y$$.
            Así para cada $$x$$ no átomo encontramos dos elementos
            átomos minimales distintos entre sí.

            Prueba:

            1.  $$x \neq y$$.

            2.  $${{{{x \cdot \overline{y}} \neq {{x \land x} \cdot \overline{y}}} \neq {y \land x}} \neq {{\overline{y} \land x} \cdot \overline{y}}} \neq 0$$

                1.  Supongamos $${x \cdot \overline{y}} = y$$.

                    1.  $${{{({x \cdot \overline{y}})} \cdot y} = {y \cdot y}} = y$$.
                    2.  $$0 = y$$. Absurdo. Habíamos asumido que
                        $${y \in {B^{\ast} \land 0}} \notin B^{\ast}$$.

                2.  Supongamos $${x \cdot \overline{y}} = x$$.

                    1.  $${{({x \cdot \overline{y}})} \cdot y} = {x \cdot y}$$
                    2.  $$0 = y$$. Absurdo. Habíamos asumido que
                        $${y \in {B^{\ast} \land 0}} \notin B^{\ast}$$.

                3.  Supongamos $$x = \overline{y}$$.

                    1.  $${x \cdot y} = 0$$
                    2.  $$0 = y$$. Absurdo. Habíamos asumido que
                        $${y \in {B^{\ast} \land 0}} \notin B^{\ast}$$.

                4.  Supongamos $${x \cdot \overline{y}} = 0$$.

                    1.  $${y + \overline{y}} = 1$$
                    2.  $${{x \cdot {({y + \overline{y}})}} = {x \cdot 1}} = x$$
                    3.  $${{x = {{({x \cdot y})} + {({x \cdot \overline{y}})}}} = {{({x \cdot y})} + 0}} = y$$
                    4.  $$x = y$$. Absurdo. Habíamos asumido que
                        $${y \in \mathit{Atom}}{{{(B)} \land x} \notin \mathit{Atom}}{(B)}$$.

            3.  $${{({x \cdot \overline{y}})} \cdot x} = {({x \cdot \overline{y}})}$$

            4.  $$\exists{z \in \mathit{Atom}}{(B)}{{z \cdot {({x \cdot \overline{y}})}} = z}$$

            5.  $$z \neq y$$

                1.  Supongamos $$z = y$$.
                2.  $${y = z} = {{({x \cdot \overline{y}})} \cdot z}$$
                3.  $${{{y = {{({{({x \cdot \overline{y}})} \cdot z})} \cdot y}} = {{({x \cdot z})} \cdot {({\overline{y} \cdot y})}}} = {{({x \cdot z})} \cdot 0}} = 0$$
                4.  $$0 = y$$. Absurdo. Habíamos asumido que
                    $${y \in {B^{\ast} \land 0}} \notin B^{\ast}$$.

            6.  $$\exists{z \in {B \smallsetminus {\{ y\}}}}z\mathsf{\mathit{minimal}}x$$.

            7.  $$\exists{\mathit{yz} \in B}{{\left\lbrack {y\mathsf{\mathit{minimal}}x} \right\rbrack \land \left\lbrack {z\mathsf{\mathit{minimal}}x} \right\rbrack} \land \left\lbrack {y \neq x} \right\rbrack}$$.

            8.  $$\forall{x \in B^{\ast}}\exists{\mathit{yz} \in B}{{\left\lbrack {y\mathsf{\mathit{minimal}}x} \right\rbrack \land \left\lbrack {z\mathsf{\mathit{minimal}}x} \right\rbrack} \land \left\lbrack {y \neq x} \right\rbrack}$$.

        82. Vamos a ver ahora que, si $${\#{(B)}} > 4$$ para cada $$x$$
            no hiperátomo ni $$1$$ no solo encontramos un $$y$$ maximal
            de $$x$$(como ya hemos demostrado) sino que podemos
            encontrar al menos otro átomo $$z$$ maximal de $$x$$,
            $$z \neq y$$. Así para cada $$x$$ no hiperátomo encontramos
            dos elementos hiperátomos maximales distintos entre sí.

            Prueba:

            1.  $$x \neq y$$.

            2.  $${{{{x + \overline{y}} \neq {x + {x \cdot \overline{y}}}} \neq {y \land x}} \neq {{\overline{y} \land x} + \overline{y}}} \neq 1$$

                1.  Supongamos $${x + \overline{y}} = y$$.

                    1.  $${{{({x + \overline{y}})} \cdot y} = {y + y}} = y$$.
                    2.  $$1 = y$$. Absurdo. Habíamos asumido que
                        $${y \in {B_{\ast} \land 1}} \notin B_{\ast}$$.

                2.  Supongamos $${x + \overline{y}} = x$$.

                    1.  $${{({x + \overline{y}})} + y} = {x + y}$$
                    2.  $$1 = y$$. Absurdo. Habíamos asumido que
                        $${y \in {B_{\ast} \land 1}} \notin B_{\ast}$$.

                3.  Supongamos $$x = \overline{y}$$.

                    1.  $${x + y} = 1$$
                    2.  $$1 = y$$. Absurdo. Habíamos asumido que
                        $${y \in {B_{\ast} \land 1}} \notin B_{\ast}$$.

                4.  Supongamos $${x + \overline{y}} = 1$$.

                    1.  $${y \cdot \overline{y}} = 0$$
                    2.  $${{x + {({y \cdot \overline{y}})}} = {x + 0}} = x$$
                    3.  $${{x = {{({x + y})} \cdot {({x + \overline{y}})}}} = {{({x + y})} \cdot 1}} = y$$
                    4.  $$x = y$$. Absurdo. Habíamos asumido que
                        $${y \in \mathit{Htom}}{{{(B)} \land x} \notin \mathit{Htom}}{(B)}$$.

            3.  $${{({x + \overline{y}})} + x} = {({x + \overline{y}})}$$

            4.  $$\exists{z \in \mathit{Htom}}{(B)}{{z + {({x + \overline{y}})}} = z}$$

            5.  $$z \neq y$$

                1.  Supongamos $$z = y$$.
                2.  $${y = z} = {{({x + \overline{y}})} + z}$$
                3.  $${{{y = {{({{({x + \overline{y}})} + z})} + y}} = {{({x + z})} + {({\overline{y} + y})}}} = {{({x + z})} + 1}} = 1$$
                4.  $$1 = y$$. Absurdo. Habíamos asumido que
                    $${y \in {B_{\ast} \land 1}} \notin B_{\ast}$$.

            6.  $$\exists{z \in {B \smallsetminus {\{ y\}}}}z\mathsf{\mathit{maximal}}x$$.

            7.  $$\exists{\mathit{yz} \in B}{{\left\lbrack {y\mathsf{\mathit{maximal}}x} \right\rbrack \land \left\lbrack {z\mathsf{\mathit{maximal}}x} \right\rbrack} \land \left\lbrack {y \neq x} \right\rbrack}$$.

            8.  $$\forall{x \in B_{\ast}}\exists{\mathit{yz} \in B}{{\left\lbrack {y\mathsf{\mathit{maximal}}x} \right\rbrack \land \left\lbrack {z\mathsf{\mathit{maximal}}x} \right\rbrack} \land \left\lbrack {y \neq x} \right\rbrack}$$.

        Hemos determinado algunas propiedades importantes de los
        elementos átomos y minimales de otros y de los elementos
        hiperátomos y maximales de otros. Para $$B_{2}$$ todo ha quedado
        claro (está todo completamente determinado a este respecto).
        Para avanzar algo más hemos de determinar propiedades únicas de
        los siguientes (solo dos) álgebras finitas, y así determinarlas
        en sus excentricidades.

        83. $$\left\lbrack {\exists{\left( {x,\overline{x}} \right) \in \mathit{Atom}}{{(B)} \times \mathit{Atom}}{(B)}} \right\rbrack\Rightarrow\left\lbrack {B = B_{4}} \right\rbrack$$.

            Prueba:

            1.  Supongamos
                $$\exists{y \in \mathit{Atom}}{(B)}{{x \neq {y \land \overline{x}}} \neq y}$$

                1.  $${{y \cdot x} = {{0 \land y} \cdot \overline{x}}} = 0$$
                2.  $${{{({y \cdot x})} + {({y \cdot \overline{x}})}} = {0 + 0}} = 0$$
                3.  $${{y = 0} \in \mathit{Atom}}{(B)}\mathit{ABSURDO}$$

            2.  Luego $$\mathit{Atom}{{(B)} = {\{{x,\overline{x}}\}}}$$.

            3.  Supongamos
                $$\exists{y \in B}{y \notin {B \smallsetminus {\mathit{Atom}{(B)}}}}$$

                1.  $$\exists{x \in B}x\mathsf{\mathit{minimal}}y$$

                2.  $${x \in \mathit{Atom}}{{{(B)} \land y} \notin \mathit{Atom}}{(B)}\Rightarrow{x \neq y}$$

                    1.  Supongamos
                        $$\overline{x}\mathsf{\mathit{minimal}}y$$

                        1.  $${\overline{x} \cdot y} = \overline{x}$$
                        2.  $${{y = {{\overline{x} \cdot y} + {x \cdot y}}} = {\overline{x} + x}} = 1$$

                    2.  Supongamos$$y \neq 1$$

                        1.  $$\neg{({\overline{x}{\mathsf{\mathit{minimal}}y}})}$$
                        2.  $${\overline{x} \cdot y} = 0$$
                        3.  $${x + \overline{y}} = 1$$
                        4.  $$\overline{x}\mathsf{\mathit{minimal}}\overline{y}$$

            4.  $$\forall{y \in B_{\ast}}$$

                $$\left\lbrack {{{\left\lbrack {x\mathsf{\mathit{minimal}}y} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{minimal}}\overline{y}} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{minimal}}\overline{y}})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{minimal}}y})}} \right\rbrack} \right\rbrack \vee$$

                $$\vee \left\lbrack {{{\left\lbrack {x\mathsf{\mathit{minimal}}\overline{y}} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{minimal}}y} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{minimal}}y})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{minimal}}\overline{y}})}} \right\rbrack} \right\rbrack$$

            5.  Pongamos sin pérdida de generalidad

                $$\forall{{\{{y,\overline{y}}\}} \subset B_{\ast}^{\ast}}$$

                $$\left\lbrack {{{\left\lbrack {x\mathsf{\mathit{minimal}}y} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{minimal}}\overline{y}} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{minimal}}\overline{y}})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{minimal}}y})}} \right\rbrack} \right\rbrack \land$$

                $$\land \left\lbrack {{{\left\lbrack {x\mathsf{\mathit{minimal}}y} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{minimal}}\overline{y}} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{minimal}}\overline{y}})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{minimal}}y})}} \right\rbrack} \right\rbrack$$

            6.  $$\forall{{\{{y,\overline{y}}\}} \subset B_{\ast}^{\ast}}{{{y \cdot \overline{x}} = {{0 \land y} + \overline{x}}} = 1}$$

            7.  $$\forall{{\{{y,\overline{y}}\}} \subset B_{\ast}^{\ast}}{{y = {x \land \overline{y}}} = \overline{x}}$$

            8.  $${B_{\ast}^{\ast} = {{\{ 1,0\}} \cup \mathit{Atom}}}{{{(B)} = {\{{1,0,x,\overline{x}}\}}} = B_{4}}$$

        84. $$\left\lbrack {\exists{x \in \mathit{Atom}}{(B)}{\overline{x} \in \mathit{Atom}}{(B)}} \right\rbrack\Leftrightarrow\left\lbrack {B = B_{4}} \right\rbrack$$

        85. $$\left\lbrack {\exists{x \in \mathit{Htom}}{(B)}{\overline{x} \in \mathit{Htom}}{(B)}} \right\rbrack\Rightarrow\left\lbrack {B = B_{4}} \right\rbrack$$.

            Prueba:

            1.  Supongamos
                $$\exists{y \in \mathit{Htom}}{(B)}{{x \neq {y \land \overline{x}}} \neq y}$$

                1.  $${{y + x} = {{1 \land y} + \overline{x}}} = 1$$
                2.  $${{{({y + x})} \cdot {({y + \overline{x}})}} = {1 \cdot 1}} = 1$$
                3.  $${{y = 1} \in \mathit{Htom}}{(B)}\mathit{ABSURDO}$$

            2.  Luego $$\mathit{Htom}{{(B)} = {\{{x,\overline{x}}\}}}$$.

            3.  Supongamos
                $$\exists{y \in B}{y \notin {B \smallsetminus {\mathit{Htom}{(B)}}}}$$

                1.  $$\exists{x \in B}x\mathsf{\mathit{maximal}}y$$

                2.  $${x \in \mathit{Htom}}{{{(B)} \land y} \notin \mathit{Htom}}{(B)}\Rightarrow{x \neq y}$$

                    1.  Supongamos
                        $$\overline{x}\mathsf{\mathit{maximal}}y$$

                        1.  $${\overline{x} + y} = \overline{x}$$
                        2.  $${{y = {{({\overline{x} + y})} \cdot {({x + y})}}} = {\overline{x} \cdot x}} = 0$$

                    2.  Supongamos$$y \neq 0$$

                        1.  $$\neg{({\overline{x}{\mathsf{\mathit{maximal}}y}})}$$
                        2.  $${\overline{x} + y} = 1$$
                        3.  $${x \cdot \overline{y}} = 0$$
                        4.  $$\overline{x}\mathsf{\mathit{maximal}}\overline{y}$$

            4.  $$\forall{y \in B_{\ast}}$$

                $$\left\lbrack {{{\left\lbrack {x\mathsf{\mathit{maximal}}y} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{maximal}}\overline{y}} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{maximal}}\overline{y}})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{maximal}}y})}} \right\rbrack} \right\rbrack \vee$$

                $$\vee \left\lbrack {{{\left\lbrack {x\mathsf{\mathit{maximal}}\overline{y}} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{maximal}}y} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{maximal}}y})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{maximal}}\overline{y}})}} \right\rbrack} \right\rbrack$$

            5.  Pongamos sin pérdida de generalidad

                $$\forall{{\{{y,\overline{y}}\}} \subset B_{\ast}^{\ast}}$$

                $$\left\lbrack {{{\left\lbrack {x\mathsf{\mathit{maximal}}y} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{maximal}}\overline{y}} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{maximal}}\overline{y}})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{maximal}}y})}} \right\rbrack} \right\rbrack \land$$

                $$\land \left\lbrack {{{\left\lbrack {x\mathsf{\mathit{maximal}}y} \right\rbrack \land \left\lbrack {\overline{x}\mathsf{\mathit{maximal}}\overline{y}} \right\rbrack} \land \left\lbrack {\neg{({x\mathsf{\mathit{maximal}}\overline{y}})}} \right\rbrack} \land \left\lbrack {\neg{({\overline{x}\mathsf{\mathit{maximal}}y})}} \right\rbrack} \right\rbrack$$

            6.  $$\forall{{\{{y,\overline{y}}\}} \subset B_{\ast}^{\ast}}{{{y + \overline{x}} = {{1 \land y} \cdot \overline{x}}} = 0}$$

            7.  $$\forall{{\{{y,\overline{y}}\}} \subset B_{\ast}^{\ast}}{{y = {x \land \overline{y}}} = \overline{x}}$$

            8.  $${B_{\ast}^{\ast} = {{\{ 1,0\}} \cup \mathit{Htom}}}{{{(B)} = {\{{1,0,x,\overline{x}}\}}} = B_{4}}$$

        86. $$\left\lbrack {\exists{x \in \mathit{Htom}}{(B)}{\overline{x} \in \mathit{Htom}}{(B)}} \right\rbrack\Leftrightarrow\left\lbrack {B = B_{4}} \right\rbrack$$

        87. $$\left\lbrack {\mathit{Htom}{{(B)} \cap \mathit{Atom}}{{(B)} \neq \varnothing}} \right\rbrack\Rightarrow\left\lbrack {B = B_{4}} \right\rbrack$$

            Prueba:

            1.  $$\exists{x \in B}\forall{y \in B}{\left\lbrack {{{y \cdot x} = {x \vee {y \cdot x}}} = 0} \right\rbrack \land \left\lbrack {{{y + x} = {{x \vee y} + x}} = 1} \right\rbrack}$$

            2.  Caso 1 $${{y \cdot x} = {{x \land y} + x}} = x$$

                1.  $${{1 = {{({y \cdot x})} + {({\overline{y} \cdot \overline{x}})}}} = y} \odot x$$
                2.  $$y = x$$
                3.  $$y \in {\{{x,\overline{x}}\}}$$

            3.  Caso 2 $${{y \cdot x} = {{x \land y} + x}} = 1$$

                1.  $${{1 = {y + x}} = {y + {({y \cdot x})}}} = y$$
                2.  $$y = 1$$
                3.  $$y \in {\{ 1,0\}}$$

            4.  Caso 3 $${{y \cdot x} = {{0 \land y} + x}} = x$$

                1.  $${{0 = {y \cdot x}} = {y \cdot {({y + x})}}} = y$$
                2.  $$y = 0$$
                3.  $$y \in {\{ 1,0\}}$$

            5.  Caso 4 $${{y \cdot x} = {{0 \land y} + x}} = 1$$

                1.  $$y = \overline{x}$$
                2.  $$y \in {\{{x,\overline{x}}\}}$$

            6.  Como
                $$\mathit{Atom}{{(B_{2})} \cap \mathit{Htom}}{{(B_{2})} = \varnothing}\Rightarrow\forall{y \in B_{\ast}^{\ast}}{y \in {\{{x,\overline{x}}\}}}$$

            7.  $$\mathit{Atom}{{(B)} \cup \mathit{Htom}}{{{{(B)} \cup {\{ 1,0\}}} = {{\{{x,\overline{x}}\}} \cup {\{ 1,0\}}}} = {\{{1,x,\overline{x},0}\}}}$$

            8.  $$\forall{y \in B^{\ast}}{{y \cdot \overline{x}} \in {\{{\overline{x},0}\}}}$$

            9.  $$\mathit{Atom}{{(B)} = {\{{x,\overline{x}}\}}}$$

            10. $$\forall{y \in B_{\ast}}{{y + \overline{x}} \in {\{{1,\overline{x}}\}}}$$

            11. $$\mathit{Htom}{{(B)} = {\{{x,\overline{x}}\}}}$$

            12. $${{B = {\{{1,x,\overline{x},0}\}}} = {{\{ 1,0\}} \cup \mathit{Atom}}}{{(B)} = {{\{ 1,0\}} \cup \mathit{Htom}}}{(B)}$$

            13. $$\mathit{Atom}{{(B)} = \mathit{Htom}}{(B)}$$

            14. $$B = B_{4}$$

        88. $$\left\lbrack {\mathit{Htom}{{(B)} \cap \mathit{Atom}}{{(B)} \neq \varnothing}} \right\rbrack\Leftrightarrow\left\lbrack {B = B_{4}} \right\rbrack$$

            1.  Todos las álgebras de Boole finitas de cardinal 4 son
                isomorfas entre sí. Por lo visto hasta ahora, queda
                $${B = \underset{B_{2}}{\underbrace{\{ 0,1\}}}}@\underset{\mathit{Atom}{{(B)} = \mathit{Htom}}{(B)}}{\underbrace{\{{a,\overline{a}}\}}}$$y
                si tenemos un segundo conjunto de Boole talque

                $$B{' = \underset{B'_{2}}{\underbrace{\{{0',1'}\}}}}@\underset{\mathit{Atom}{{({B'})} = \mathit{Htom}}{({B'})}}{\underbrace{\{{a',\overline{a'}}\}}}$$basta
                con construir el siguiente isomorfismo:

                $$\varphi:{B\rightarrow B}'::x\mapsto\varphi{(x)} ≔ \begin{Bmatrix}
                {0'\Leftarrow{x = 0}} \\
                {1'\Leftarrow{x = 1}} \\
                {a'\Leftarrow{x = a}} \\
                {\overline{a'}\Leftarrow{x = \overline{a}}}
                \end{Bmatrix}$$

        89. Las siguientes condiciones son equivalentes entre sí:

            1.  $$\exists{x \in B}{{\{{x,\overline{x}}\}} \subseteq {\mathit{Atom}{(B)}}}$$
            2.  $$\exists{x \in B}{{\{{x,\overline{x}}\}} \subseteq {\mathit{Htom}{(B)}}}$$
            3.  $$\mathit{Atom}{{(B)} \cap \mathit{Htom}}{{(B)} \neq \varnothing}$$
            4.  $$\#{B = 4}$$
            5.  $$B = B_{4}$$

        90. Los siguientes conjuntos no pueden dotarse de la estructura
            de álgebra de Boole.

            $$\left\lbrack {{\#{(B)}} \in {\{{0,1,3,5,7}\}}} \right\rbrack\Rightarrow$$

            $$\Rightarrow{\neg\left\lbrack {\forall + , \cdot :{{B \times B}\rightarrow B}{\langle{B, + , \cdot}\rangle}\mathit{de}\mathit{Boole}} \right\rbrack}$$

        91. $${{\#{(B)}} = 6}\Rightarrow{\neg\left\lbrack {\forall + , \cdot :{{B \times B}\rightarrow B}{\langle{B, + , \cdot}\rangle}\mathit{de}\mathit{Boole}} \right\rbrack}$$

            Prueba:

            1.  Suponemos$$B = {\{{1,0,x,y,\overline{x},\overline{y}}\}}$$se
                puede dotar de estructura de álgebra de Boole.

            2.  Ponemos$$\mathit{Atom}{{(B)} \supseteq {\{{x,y}\}}}$$
                sin pérdida de generalidad.

                Entonces:

                1.  $$\mathit{Htom}{{(B)} \supseteq {\{{\overline{x},\overline{y}}\}}}$$

                2.  $${x + y} \neq 1$$

                3.  Ponemos sin pérdida de generalidad

                    $${x + y} = \overline{x}$$

                4.  $${{{{0 = {x + \overline{x}}} = {x + {({x + y})}}} = {{({x + x})} + y}} = {x + y}} = \overline{x}$$

                5.  $$1 = x$$

                6.  $${6 = \#}{B = 2}\mathit{ABSURDO}$$

            3.  $$\forall{{\{{x,y}\}} \in \wp}{(B)}{{\{{x,y}\}} \nsubseteq B}\mathit{ABSURDO}$$

        92. Vamos a dar una caracterización de $$B_{8}$$ que es el
            último de las álgebras de Boole pequeñas que tienen
            excentricidades en su comportamiento. La única de $$B_{8}$$
            es que no tiene elementos fuera de
            $$B_{2}\biguplus{\mathit{Atom}{(B)}}\biguplus{\mathit{Htom}{(B)}}$$.
            Todos sus elementos son los caracterizados como especiales
            hasta ahora. Al decir $$B_{8}$$ quiero decir en realidad un
            álgebra de Boole de 8 elementos. Adelanto que será igual a
            la de los primeros ejemplos en todo lo que importa (es
            isomorfa a aquella). Pero por el momento no sabemos si hay
            solo una o varias diferentes, con operaciones esencialmente
            diferentes. La caracterización que daremos es

            $$\left\lbrack {\#{{(B)} = 8}} \right\rbrack\Leftrightarrow\left\lbrack {\exists{\mathit{xy} \in \mathit{Atom}}{(B)}{\left\lbrack {x \neq y} \right\rbrack \land \left\lbrack {x,y,{\overline{x+y} \in \mathit{Atom}}{(B)}} \right\rbrack}} \right\rbrack$$

            Prueba:

            $$\left\lbrack {\#{{(B)} = 8}} \right\rbrack\Rightarrow\left\lbrack {\exists{\mathit{xy} \in \mathit{Atom}}{(B)}{\left\lbrack {x \neq y} \right\rbrack \land \left\lbrack {\overline{x+y},x,{y \in \mathit{Atom}}{(B)}} \right\rbrack}} \right\rbrack$$

            1.  Sea $${\mathit{xy} \in \mathit{Atom}}{(B)}$$ (su
                existencia ya ha sido demostrada).

            2.  $${{x + y} \notin \mathit{Atom}}{(B)}$$

                1.  $$x \leq {x + y}$$

                2.  $$x \neq {x + y}$$

                    1.  Supongamos que$$x = {x + y}$$

                        1.  $${{x \cdot y} = {{({x + y})} \cdot y}} = y$$
                        2.  $$\mathit{hip.}{y \neq {x \land \mathit{sup.}}}\mathsf{\mathit{atom}_{B}}{{(x)} \land \mathit{sup.}}\mathsf{\mathit{atom}_{B}}{{{(y)} \land y} < x}\mathit{ABSURDO}$$

            3.  $${a \in \mathit{Htom}}{(B)}\Rightarrow{\overline{a} \in \mathit{Atom}}{(B)}$$

                1.  Caso 1 $${z + a} = a$$

                    1.  $${z + a} = a$$

                        1.  $${{{({z + a})} \cdot \overline{a}} = {a \cdot \overline{a}}} = 0$$
                        2.  $${z \cdot \overline{a}} = 0$$

                    2.  Caso 2 $${z + a} = 1$$

                        1.  $${{{({z + a})} \cdot \overline{a}} = {1 \cdot \overline{a}}} = \overline{a}$$
                        2.  $${z \cdot \overline{a}} = \overline{a}$$

            4.  $${a \in \mathit{Atom}}{(B)}\Rightarrow{\overline{a} \in \mathit{Htom}}{(B)}$$

                1.  $$a \in {\{{x,y}\}}$$

                    1.  Caso 1 $${z \cdot a} = a$$

                        1.  $${z \cdot a} = a$$

                            1.  $${{{({z \cdot a})} + \overline{a}} = {a + \overline{a}}} = 1$$
                            2.  $${z + \overline{a}} = 1$$

                        2.  Caso 2 $${z \cdot a} = 0$$

                            1.  $${{{({z \cdot a})} + \overline{a}} = {0 + \overline{a}}} = \overline{a}$$
                            2.  $${z + \overline{a}} = \overline{a}$$

            5.  $${{\{{\overline{x},\overline{y}}\}} \subseteq \mathit{Htom}}{{{(B)} \land \overline{x}} \neq \overline{y}}$$

            6.  $${a \in \mathit{Atom}}{(B)}\Leftrightarrow{\overline{a} \in \mathit{Htom}}{(B)}$$

            7.  $$\exists{z \in \mathit{Atom}}{(B)}{{\lbrack{z \neq x}\rbrack} \land {\lbrack{z \neq y}\rbrack}}$$

                1.  $$\mathit{Atom}'{{(B)} = {\{{x,y}\}}}$$

                2.  $$\mathit{Htom}'{{(B)} = {\{{\overline{x},\overline{y}}\}}}$$

                3.  $$\exists{{\{{z,\overline{z}}\}} \subset B}{B = B_{2}}\biguplus{\mathit{Atom}'{(B)}}\biguplus{\mathit{Htom}'{(B)}}\biguplus{\{{z,\overline{z}}\}}$$

                4.  Pongamos $$z = {\overline{x} \cdot \overline{y}}$$ y
                    de
                    aquí$${{z \neq {\overline{x} \land z}} \neq {\overline{y} \land z}} \neq 1$$

                    1.  $${z \cdot x} = 0$$

                    2.  $${z \cdot y} = 0$$

                    3.  $${z \cdot {({x + y})}} = 0$$

                    4.  $${z \cdot \overline{z}} = 0$$

                    5.  $${z \cdot z} = z$$

                    6.  $${z \cdot \overline{x}} = z$$ y de aquí
                        $$z \neq x$$

                    7.  $${z \cdot \overline{y}} = z$$y de aquí
                        $$z \neq y$$

                    8.  $${z \cdot 1} = z$$

                    9.  $${z \cdot 0} = 0$$

                    10. $$z \neq 0$$

                        1.  Supongamos
                            $${z = {\overline{x} \cdot \overline{y}}} = 0$$
                        2.  $${z = \overline{x+y}} = 0$$
                        3.  $${\overline{z} = {x + y}} = 1$$
                        4.  $${x \cdot y} = 0$$
                        5.  $${x = {\overline{y} \land y}} = \overline{x}$$
                        6.  $${{\{{x,y}\}} \subseteq \mathit{Atom}}{{(B)} \cap \mathit{Htom}}{(B)}$$
                        7.  $$\mathit{Atom}{{(B)} \cap \mathit{Htom}}{{(B)} \neq \varnothing}$$
                        8.  $${B \simeq {B_{4} \land \#}}{{(B)} = 8}\mathit{ABSURDO}$$

                    11. $${z \in \mathit{Atom}}{(B)}$$

                    12. $${\overline{x+y} \in \mathit{Atom}}{(B)}$$

                    13. $${{x + y} \in \mathit{Htom}}{(B)}$$

                5.  $$\mathit{Atom}{{(B)} = {{\{{x,y,{x + y}}\}} \land \mathit{Htom}}}{{(B)} = {\{{\overline{x},\overline{y},{\overline{x} \cdot \overline{y}}}\}}}$$

                6.  $${B = \mathit{Atom}}{(B)}\biguplus\mathit{Htom}{(B)}\biguplus B_{2}$$

            $$\left\lbrack {\left\lbrack {x \neq y} \right\rbrack \land \left\lbrack {\overline{x+y},x,{y \in \mathit{Atom}}{(B)}} \right\rbrack} \right\rbrack\Rightarrow\left\lbrack {\#{{(B)} = 8}} \right\rbrack$$

            8.  $$\forall{z \in \mathit{Atom}}{{(B)} \smallsetminus {\{{x,y}\}}}{z = {\overline{x} \cdot \overline{y}}}$$

                1.  Supongamos que no:

                    $$\exists{z \in \mathit{Atom}}{{(B)} \smallsetminus {\{{x,y}\}}}{z \neq {\overline{x} \cdot \overline{y}}}$$

                2.  $${{({x + y})} \cdot z} = 0$$

                    1.  $${{{({x \cdot z})} + {({y \cdot z})}} = {0 + 0}} = 0$$

                3.  $${\overline{x+y} \cdot z} = 0$$

                    1.  $$\overline{x+y},{z \in \mathit{Atom}}{{{(B)} \land \overline{x+y}} \neq z}$$

                4.  $${z = 0}\mathit{ABSURDO}$$

            9.  $$\mathit{Atom}{{(B)} = {\{{x,y,\overline{x+y}}\}}}$$

            10. $$\mathit{Htom}{{(B)} = {\{{\overline{x},\overline{y},{x + y}}\}}}$$

            11. $$\mathsf{\mathit{Ker}}B ≝ {\{{x,y,\overline{x},\overline{y},{x + y},{\overline{x} \cdot \overline{y}},1,0}\}}$$

            12. $$\mathsf{\mathit{Nil}}B ≝ {B \smallsetminus {\mathsf{\mathit{Ker}}B}}$$

            13. Supongamos $$\exists{z \in {\mathsf{\mathrm{Nil}}B}}$$

                1.  Casos al multiplicar por átomos.

                    1.  Caso 1.
                        $${{z \cdot x} = {{x \land z} \cdot y}} = 0$$:

                        1.  $${{z \cdot \overline{x}} = {{0 \land z} \cdot \overline{y}}} = z$$
                        2.  $${{{z \cdot \overline{x+y}} = {{({z \cdot \overline{x}})} \cdot {({z \cdot \overline{y}})}}} = {0 + z}} = z$$
                        3.  $${z < \overline{x+y}}\mathit{ABSURDO}$$

                    2.  Caso 2.
                        $${{z \cdot x} = {{0 \land z} \cdot y}} = y$$:

                        1.  $${{z \cdot \overline{x}} = {{z \land z} \cdot \overline{y}}} = 0$$
                        2.  $${{{z \cdot \overline{x+y}} = {{({z \cdot \overline{x}})} \cdot {({z \cdot \overline{y}})}}} = {z + 0}} = z$$
                        3.  $${z < \overline{x+y}}\mathit{ABSURDO}$$

                    3.  Caso
                        3.$${{z \cdot x} = {{x \land z} \cdot y}} = y$$:

                        1.  $${{z \cdot {({x + y})}} = {{({z \cdot x})} + {({z \cdot y})}}} = {x + y}$$
                        2.  $${x + y} \leq z$$
                        3.  $${{z \geq {x + y}} \in \mathit{Htom}}{(B)}$$
                        4.  $${z \neq 1}\Rightarrow{z \in \mathit{Htom}}{(B)}$$
                        5.  $${\overline{z} \in \mathit{Atom}}{(B)}\mathit{ABSURDO}$$

                    4.  Caso
                        4.$${{z \cdot x} = {{0 \land z} \cdot y}} = 0$$:

                        1.  $${{{z \cdot {({x + y})}} = {{({z \cdot x})} + {({z \cdot y})}}} = {0 + 0}} = 0$$
                        2.  $${{({x + y})} + z} = 1$$
                        3.  $${z = \overline{x+y}}\mathit{ABSURDO}$$
                        4.  $$\forall{z \in B}{z \in {({B_{2}@{\mathit{Atom}{(B)}}@{\mathit{Htom}{(B)}}})}}$$
                        5.  $$\#{{(B)} = 8}$$

            14. Todos las álgebras de Boole finitas de cardinal 8 son
                isomorfas entre sí. Por lo visto hasta ahora, queda
                $${B = \underset{B_{2}}{\underbrace{\{ 0,1\}}}}@\underset{\mathit{Atom}{(B)}}{\underbrace{\{{a,b,\overline{a+b}}\}}}@\underset{\mathit{Htom}{(B)}}{\underbrace{\{{\overline{a},\overline{b},{a + b}}\}}}$$y
                si tenemos un segundo conjunto de Boole talque

                $$B{' = \underset{B'_{2}}{\underbrace{\{{0',1'}\}}}}@\underset{\mathit{Atom}{({B'})}}{\underbrace{\{{a',b',\overline{a'+_{2}b'}}\}}}@\underset{\mathit{Htom}{({B'})}}{\underbrace{\{{\overline{a},\overline{b},{a +_{2}b}}\}}}$$basta
                con construir el siguiente isomorfismo:

                $$\varphi:{B\rightarrow B}'::x\mapsto\varphi{(x)} ≝ \begin{Bmatrix}
                {0'\Leftarrow{x = 0}} \\
                {1'\Leftarrow{x = 1}} \\
                {a'\Leftarrow{x = a}} \\
                {b'\Leftarrow{x = b}} \\
                {\overline{a'+_{2}b'}\Leftarrow{x = \overline{a+b}}} \\
                {\overline{a'}\Leftarrow{x = \overline{a}}} \\
                {\overline{b'}\Leftarrow{x = \overline{b}}} \\
                {\overline{a'+_{2}b'}\Leftarrow{x = {a + b}}}
                \end{Bmatrix}$$

        93.  Vamos a ver que si $$z,y$$ son minimales de $$x$$,
            distintos entre sí, obtenemos que o bien
            $${x = {y + z}}{\land}\forall{w \in \mathit{Atom}}{(\left\lbrack {x,0} \right\rbrack_{B})}{{w \cdot x} = 0}$$
            o bien existe otro elemento minimal átomo $$w$$ de $$x$$,
            esto es, $${w \cdot x} = w$$. Esto nos dará un método
            inductivo que funcionará recursivamente hasta encontrar un
            conjunto de átomos cuya suma sea $$x$$.

            Prueba:

            1.  $$\exists{\mathit{yz} \in \mathit{Atom}}{(B)}{x = {y + z}}$$.
                Existencia demostrada en el anterior lema.
            2.  $$\forall{w \in \mathit{Atom}}{(B)}{w \notin {\{{x,y}\}}}$$.
                Sino existiese este elemento habríamos completado el
                conjunto $$\mathit{Atom}{(B)}$$.
            3.  $${{{{x \cdot w} = {{({y + z})} \cdot w}} = {{({y \cdot w})} + {({z \cdot w})}}} = {0 + 0}} = 0$$.
                Ningún otro átomo está relacionado con $$x$$.
            4.  $$x \neq {y + z}$$. Veamos que pasa cuando los dos
                átomos que nos han asegurado su existencia a partir de
                $$x$$ no son suficientes para $$x = {y + z}$$.
            5.  $$\forall{x \in {B^{\ast} \smallsetminus {\mathit{Atom}{(B)}}}}\exists{\mathit{yz} \in \mathit{Atom}}{(B)}{{{{x \cdot y} = {{y \land x} \cdot z}} = {{z \land y} \cdot z}} = 0}$$.
            6.  $${{x \cdot {({y + z})}} = {{({x \cdot y})} + {({x \cdot z})}}} = {y + z}$$
            7.  $${\overline{y+z} \notin \mathit{Atom}}{(B)}$$
            8.  Supongamos $${\overline{y+z} \in \mathit{Atom}}{(B)}$$
            9.  Supongamos$$\mathit{Atom}{{(B)} = {\{{y,z,\overline{y+z}}\}}}$$
            10. $${B = {\{{0,y,z,\overline{y+z},{y + z},{y + \overline{z}},{z + \overline{y}},1}\}}} = B_{8}$$
            11. $${\overline{y+z} \cdot {({y + \overline{z}})}} = {{\overline{y} \cdot \overline{z}} \cdot {({y + \overline{z}})}}$$
            12. 
            13. Supongamos $$\#{{({\mathit{Atom}B})} > 3}$$
            14. Supongamos$${{y + z} + w} \neq \overline{y+z}$$
            15. $${{y + z} + w} \neq {\overline{y} \cdot \overline{z}}$$
            16. $$\exists{w \in \mathit{Atom}}{(B)}{{\overline{y+z} \cdot w} = w}$$

        94.  Ahora vamos a construir una función inyectiva del álgebra
            de Boole de las partes de los átomos de B (si este es
            finito) en el álgebra de Boole B. Así cuando menos sa­bremos
            que podemos interpretar este álgebra de las partes de un
            conjunto de los áto­mos de B como un sub-álgebra de la que
            estamos estudiando.

            La función $$\varphi$$que vamos a definir va a quedar
            completamente definida en la fór­mula que sigue. Tendremos
            que mostrar que está bien definida, que es inyectiva, que
            $$\varphi{{({x \cup y})} = \varphi}{{(x)} + \varphi}{(y)}$$,
            esto es que respeta la suma booleana en $$B$$que viene como
            unión de conjuntos desde
            $$@\left( {\mathit{Atom}{(B)}} \right)$$, que
            $$\varphi{{({x \cap y})} = \varphi}{{(x)} \cdot \varphi}{(y)}$$,
            esto es que respeta el producto booleano en $$B$$que viene
            como intersección de conjun­tos desde
            $$@\left( {\mathit{Atom}{(B)}} \right)$$ , y aunque ya no
            sería necesario, también veremos que
            $$\varphi{\left( {\mathit{Atom}{{(B)} \smallsetminus x}} \right) = \overline{\varphi(x)}}$$
            . Así quedará clara la relación entre ambas álgebras.

            1.  $$\begin{matrix}
                {n{: = \#}\left( {\mathit{Atom}B} \right)} \\
                {{n \leq m}{: = \#}\left( B \right)} \\
                {\left\lbrack {1,n} \right\rbrack_{\mathbb{N}}{: = {\{{1,2,\ldots,n}\}}}} \\
                {\varphi:@{\left( {\mathit{Atom}\left( B \right)} \right)\rightarrow B}} \\
                {{\varphi{(x)}}{: =}\begin{Bmatrix}
                0 & \Leftarrow & {{x = \varnothing} = {\{\}}} \\
                {x_{1}'} & \Leftarrow & {x = {\{{x_{1}'}\}}} \\
                {{\sum\limits_{\substack{k \in I \\ I \subset {\lbrack{1,n}\rbrack}_{\mathbb{N}}}}x_{k}}'} & \Leftarrow & {x = {\{{{x_{i}'} \mid {{i \in I} \subset \left\lbrack {1,n} \right\rbrack_{\mathbb{N}}}}\}}} \\
                {x_{1}{{' + \ldots} + x_{i - 1}}{' + x_{i}}{{' + \ldots} + x_{n}}'} & \Leftarrow & {{x = \mathit{Atom}}{{(B)} \smallsetminus {\{{x_{i}'}\}}}} \\
                1 & \Leftarrow & {{x = \mathit{Atom}}{(B)}}
                \end{Bmatrix}}
                \end{matrix}$$.

        95. $$\#{B_{a} = \#}{B_{b} = 2}\Rightarrow{B_{a} \simeq B_{b}}$$.
            Con la misma $$\varphi$$ anterior.

        96. $$\#{B_{a} = \#}{B_{b} = 4}\Rightarrow{B_{a} \simeq B_{b}}$$.
            Con la misma $$\varphi$$ anterior.

        97. $$\#{B > 4}\Rightarrow\mathit{Atom}{B \cap \mathit{Htom}}{B = \varnothing}$$.
            Lo mejor sería demostrar que cualquier cadena completa
            saturada de 1 a 0 tiene una longitud (número de elementos)
            siempre igual al $$\#\mathit{Atom}{(B)}$$. De ahí se sigue
            que si el cardinal es el dicho, tendríamos más de 3 niveles,
            diferenciándose siempre los átomos y los hiperátomos.

        98. Para cada uno de los cardinales de $$B$$, cuando son
            finitos, existe una estructura no solo de anillo conmutativo
            con unidad como en 34, sino otra estructura asociada de
            dominio de integridad / cuerpo. La po­demos encontrar
            explícitamente en el álgebra de las partes de un conjunto
            finito. Sólo nos queda ver que $$\varphi$$es sobreyectivo.
            Tenemos que
            $$\varphi{\left( {\mathit{Atom}{(B)}} \right) = B}$$. Así
            $$\varphi$$pasa a ser un isomorfimo de álgebras de Boole:
            esto es, en lo que a la estructu­ra de álgebra de Boole se
            refiere, haciendo abstracción de las operaciones $$+$$ y
            $$\cdot$$concretas y los elementos concretos,
            $${\langle{B,0,1, + , \cdot}\rangle} \cong {\langle{@\left( {\mathit{Atom}{(B)}} \right),\varnothing,\mathit{Atom}\left( B \right), \cup , \cap}\rangle}$$.

        99. De 74 se deduce que si $$B$$es un conjunto finito,
            $$\exists{n \in \mathbb{N}}\#{B = 2^{\mathbf{\mathrm{n}}}}$$.

        100. Estructuras respectivas a 35 de espacio vectorial
             de$$({B^{n}, \oplus})$$sobre el cuerpo
             $$({B, \oplus , \cdot})$$ y el dual de
             $$({B^{n}, \odot})$$sobre el cuerpo dual
             $$({B, \odot , +})$$. Éste último es el caso cuando
             $${B = B_{2}} = {\{ 0,1\}}$$. Esto tendrá utilidad
             inmediata en los códigos de Hamming.

        101. Para calcular los inversos en los cuerpos finitos de
             cardinal $$2^{\mathbf{\mathrm{n}}}$$ construidos sobre las
             álgebras de Boole correspondientes hay que re­solver algunas
             ecuaciones sobre igualdades polinómicas. El producto del
             cuerpo fi­nito asociado (en número de elementos) a nuestro
             álgebra de Boole no es en general igual al producto del
             ani­llo booleano asociado, o bien la unidad del anillo
             booleano natural es distinta de la unidad del cuerpo.

             Estos cuerpos finitos son habitualmente llamados cuerpos de
             Galois. El cuerpo de Galois no es un anillo de Boole si no
             es $$B_{2}$$. Los cuerpos de Galois correspondientes a las
             álgebras de Boole son $$\mathit{GF}{(2^{n})}$$para cada
             $$B_{2^{n}}$$. Estos cuerpos y los polinomios mencionados
             son de gran utilidad en teoría de codificación.

        102. Existen formulas sencillas para poner la suma "$$+$$", el
             producto "$$\cdot$$" en fun­ción de las funciones
             "$$\oplus$$" y "$$\cdot$$", y de "$$\odot$$" y "$$+$$":

             1.  $${{a + b} = {({a \oplus b})}} \oplus {({a \cdot b})}$$

                 Prueba:

                 $${({a \oplus b})} \oplus {{({a \cdot b})} =}$$

                 $${= {({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})}} \oplus {{({a \cdot b})} =}$$

                 $${= {{\lbrack{\overline{({{({\overline{a}\cdot b})}+{({a\cdot\overline{b}})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot \overline{({a\cdot b})}}\rbrack}}} =$$

                 $${= {{\lbrack{{({\overline{({\overline{a}\cdot b})} \cdot \overline{({a\cdot\overline{b}})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot {({\overline{a} + \overline{b}})}}\rbrack}}} =$$

                 $${= {{\lbrack{{({{({a + \overline{b}})} \cdot {({\overline{a} + b})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot {({\overline{a} + \overline{b}})}}\rbrack}}} =$$

                 $${= {{\lbrack{({a \cdot b})}\rbrack} + {\lbrack{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})}\rbrack}}} =$$

                 $${= {{{({a \cdot b})} + {({\overline{a} \cdot b})}} + {({a \cdot \overline{b}})}}} =$$

                 $${= {{\lbrack{{({a \cdot b})} + {({\overline{a} \cdot b})}}\rbrack} + {\lbrack{{({a \cdot b})} + {({a \cdot \overline{b}})}}\rbrack}}} =$$

                 $${= {{\lbrack b\rbrack} + {\lbrack a\rbrack}}} =$$

                 $$= {a + b}$$

             2.  $${{a \cdot b} = {({a \odot b})}} \odot {({a + b})}$$

                 Prueba:

                 $${({a \odot b})} \odot {{({a + b})} =}$$

                 $${= {({{({\overline{a} + b})} \cdot {({a \cdot \overline{b}})}})}} \odot {{({a + b})} =}$$

                 $${= {{\lbrack{\overline{({{({\overline{a}+b})}\cdot{({a+\overline{b}})}})} + {({a + b})}}\rbrack} \cdot {\lbrack{{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + \overline{({a+b})}}\rbrack}}} =$$

                 $${= {{\lbrack{{({\overline{({\overline{a}+b})} + \overline{({a+\overline{b}})}})} + {({a + b})}}\rbrack} \cdot {\lbrack{{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})} + {({\overline{a} \cdot \overline{b}})}}\rbrack}}} =$$

                 $${= {{\lbrack{{({{({a + \overline{b}})} \cdot {({\overline{a} + b})}})} \cdot {({a \cdot b})}}\rbrack} + {\lbrack{{({{({\overline{a} \cdot b})} + {({a \cdot \overline{b}})}})} \cdot {({\overline{a} + \overline{b}})}}\rbrack}}} =$$

                 $${= {{\lbrack{({a + b})}\rbrack} \cdot {\lbrack{({{({\overline{a} + b})} \cdot {({a + \overline{b}})}})}\rbrack}}} =$$

                 $${= {{{({a + b})} \cdot {({\overline{a} + b})}} \cdot {({a + \overline{b}})}}} =$$

                 $${= {{\lbrack{{({a + b})} \cdot {({\overline{a} + b})}}\rbrack} \cdot {\lbrack{{({a + b})} \cdot {({a + \overline{b}})}}\rbrack}}} =$$

                 $${= {{\lbrack b\rbrack} \cdot {\lbrack a\rbrack}}} =$$

                 $$= {a \cdot b}$$

        103. Si un anillo $$({B,0,1, \oplus , \cdot})$$ es tal que
             $$\forall{x \in B}{{x \cdot x} = x}$$, define de manera
             unívoca un álgebra de Boole (la estructura de la que
             hablamos se llama un anillo de Boole). Esta proposición,
             con ser matemáticamente importante, la vemos aquí como sólo
             una curiosidad. En el anillo no exigimos que sea
             conmutativo. La conmutabilidad de la suma está asegurada
             para todo anillo, y la del producto está asegurada con la
             con­dición de idempotencia impuesta a todos los elementos
             del anillo. Que la inversa de un elemento bajo la suma es
             el mismo elemento se deduce fácilmente de la idempotencia
             del producto. La suma lógica la establecemos
             $${{x + y} = x} \oplus y \oplus {({x \cdot y})}$$(como en
             40.1, solo que aquí no su­ponemos nada sobre álgebras de
             Boole), mientras que el producto lógico lo pone­mos como
             idéntico al producto del anillo (idénticamente a lo
             anteriormente dicho). Nota: es importante darse cuenta que
             este anillo tendrá siempre divisores de cero, esto es,
             habrá para cada elemento otro, distintos ambos de cero, que
             al multiplicarse dan cero, lo que impide que este anillo de
             Boole sea un dominio de integridad y por lo tanto también
             impide que sea cuerpo. El complementario, siguiendo la
             misma tó­nica que en 40.1, se define como
             $${\overline{x} = x} \oplus 1$$. Por la idempotencia de la
             suma, la asociatividad de la suma y la existencia y
             unicidad de la suma tenemos que la doble negación es igual
             a la identidad. Sólo quedaría ver las distributividades.
             Cómo hasta ahora las demostraciones son cálculos que
             verifican la aserción. Así tenemos una forma de ir de cada
             álgebra de Boole a cada anillo de Boole, y un camino
             (exacta­mente el inverso), que nos llevaría de cada anillo
             de Boole a cada álgebra de Boole. Las álgebras de Boole y
             los anillos de Boole son categorías equivalentes. A los
             ca­minos los llamamos funtores. Daré solo un comienzo de
             estos teoremas:

             \[Axioma R0\]
             **$$\forall{\left( {x,y} \right) \in {B \times B}}\exists\mathtt{\mathrm{!}}{z \in B}x \oplus {y = z}$$

             \[Axioma R1\]
             $$\forall x,y,{z \in B}\left( {x \oplus y} \right) \oplus {z = x} \oplus \left( {y \oplus z} \right)$$

             \[Axioma R2\]
             $$\exists{0 \in B}\forall{x \in B}0 \oplus {x = x}$$

             \[Axioma R3\]
             $$\forall{x \in B}\exists{y_{x} \in B}y_{x} \oplus {x = 0}$$

             \[Axioma R4\]
             $$\forall x,{y \in B}\exists\mathtt{\mathrm{!}}{z \in B}{{x \cdot y} = z}$$

             \[Axioma R5\]
             $$\forall x,y,{z \in B}{{\left( {x \cdot y} \right) \cdot z} = {x \cdot \left( {y \cdot z} \right)}}$$

             \[Axioma R6\]
             $$\exists{1 \in B}\forall{x \in B}{{1 \cdot x} = x}$$

             \[Axioma R7\]
             $$\exists 1{' \in B}\forall{x \in B}{x \cdot 1}{' = x}$$

             \[Axioma R8\]
             $${\left\{ 0,1 \right\} \subseteq {B \land 0}} \neq 1$$

             \[Axioma R9\]
             $$\forall x,y,{z \in B}{{\left( {x \oplus y} \right) \cdot z} = \left( {x \cdot z} \right)} \oplus \left( {y \cdot z} \right)$$

             \[Axioma
             R10\]$$\forall x,y,{z \in B}{{x \cdot \left( {y \oplus z} \right)} = \left( {x \cdot y} \right)} \oplus \left( {x \cdot z} \right)$$

             \[Axioma BR\]$$\forall{x \in B}{{x \cdot x} = x}$$

             $$\left\lbrack {{Lema}1} \right\rbrack\forall x,{y_{x} \in B}{}{}{}\left\lbrack {\left( {y_{x} \oplus x} \right) = 0} \right\rbrack\Rightarrow\left\lbrack {\left( {x \oplus y_{x}} \right) \oplus {\left( {x \oplus y_{x}} \right) = \left( {x \oplus y_{x}} \right)}} \right\rbrack$$

             Prueba:

             $$\left( {x \oplus y_{x}} \right) \oplus {\left( {x \oplus y_{x}} \right) =}$$

             $${= \left( {x \oplus \left( {y_{x} \oplus \left( {x \oplus y_{x}} \right)} \right)} \right)} =$$

             $${= \left( {x \oplus \left( {\left( {y_{x} \oplus x} \right) \oplus y_{x}} \right)} \right)} =$$

             $${= \left( {x \oplus \left( {0 \oplus y_{x}} \right)} \right)} =$$

             $$= \left( {x \oplus y_{x}} \right)$$

             $$\left\lbrack {{Lema}2} \right\rbrack\forall x,{y_{x} \in B}{\left( {y_{x} \oplus x} \right) = 0}\Rightarrow{\left( {x \oplus y_{x}} \right) = 0}$$

             Prueba:

             $$\forall x,{y_{x} \in B}\exists{u_{x + y_{x}} \in B}{{u_{x + y_{x}} \oplus \left( {x \oplus y_{x}} \right)} = 0}$$

             $$\left( {u_{x \oplus y_{x}} \oplus \left( {x \oplus y_{x}} \right)} \right) \oplus {\left( {x \oplus y_{x}} \right) = 0} \oplus \left( {x \oplus y_{x}} \right)$$

             $$u_{x \oplus y_{x}} \oplus {\left( {\left( {x \oplus y_{x}} \right) \oplus \left( {x \oplus y_{x}} \right)} \right) = \left( {x \oplus y_{x}} \right)}$$

             $$u_{x \oplus y_{x}} \oplus {\left( {x \oplus y_{x}} \right) = \left( {x \oplus y_{x}} \right)}$$

             $$0 = \left( {x \oplus y_{x}} \right)$$

             $$\left\lbrack {{Lema}3} \right\rbrack\forall{x \in B}0 \oplus {x = x}$$

             Prueba:

             $$\forall{x \in B}0 \oplus {x =}$$

             $$\forall{x \in B}\exists{y_{x} \in B}{= \left( {x \oplus y_{x}} \right)} \oplus {x =}$$

             $$\forall{x \in B}\exists{y_{x} \in B}{= x} \oplus {\left( {y_{x} \oplus x} \right) =}$$

             $$\forall{x \in B}{= x} \oplus {0 = 0}$$

             $$\left\lbrack {{Lema}4} \right\rbrack\forall{e \in B}\left( {\forall{x \in B}x \oplus {e = x}} \right)\Rightarrow\left( {e = 0} \right)$$

             Prueba:

             $$\forall{x \in B}x \oplus {e = x}$$

             $$\forall{x \in B}\exists{y_{x} \in B}y_{x} \oplus {x = 0}$$

             $$\forall{x \in B}\exists{y_{x} \in B}y_{r} \oplus {\left( {x \oplus e} \right) = y_{r}} \oplus x$$

             $$\forall{x \in B}\exists{y_{x} \in B}y_{r} \oplus {\left( {x \oplus e} \right) = 0}$$

             $$\forall{x \in B}\exists{y_{x} \in B}\left( {y_{r} \oplus x} \right) \oplus {e = y_{r}} \oplus {x = 0}$$

             $$\forall{x \in B}\left( {y_{r} \oplus x} \right) \oplus {e = 0}$$

             $$\forall{x \in B}0 \oplus {e = 0}$$

             $$\forall{x \in B}{e = 0}$$

             $$\left\lbrack {{Lema}5} \right\rbrack\forall{x \in B}\forall y_{x},{z_{x} \in B}\left\lbrack {{{x + y_{r}} = {{0 \land x} + z_{r}}} = 0} \right\rbrack\Rightarrow\left\lbrack {y_{x} = z_{r}} \right\rbrack$$

             Prueba:

             $$y_{r} \oplus {\left( {x \oplus z_{r}} \right) = y_{r}} \oplus 0$$

             $$\left( {y_{r} \oplus x} \right) \oplus {z_{r} = y_{r}}$$

             $$0 \oplus {z_{r} = y_{r}}$$

             $$z_{r} = y_{r}$$

             $${\lbrack{{Notación}1}\rbrack}{{{y_{x} + x} = {{0 \vee x} + y_{x}}} = 0}\Rightarrow\left( {- x} \right){: = y_{x}}$$

             $$\left\lbrack {{Lema}6} \right\rbrack\forall x,y,{z \in B}\left\lbrack {x \oplus {y = x} \oplus z} \right\rbrack\Rightarrow\left\lbrack {y = z} \right\rbrack$$

             Prueba:

             $$x \oplus {y_{r} = {0 \land x}} \oplus {z_{r} = 0}$$

             $${({- x})} \oplus {{({x \oplus y})} = {({- x})}} \oplus {({x \oplus z})}$$

             $$\left( {{({- x})} \oplus x} \right) \oplus {y = \left( {{({- x})} \oplus x} \right)} \oplus z$$

             $$0 \oplus {y = 0} \oplus z$$

             $$y = z$$

             $$\left\lbrack {{Lema}7} \right\rbrack\forall x,y,{z \in B}\left\lbrack {{y + x} = {z + x}} \right\rbrack\Rightarrow\left\lbrack {y = z} \right\rbrack$$

             Prueba:

             $$y \oplus {x = z} \oplus x$$

             $${({- x})} \oplus {{({x \oplus y})} = {({- x})}} \oplus {({x \oplus z})}$$

             $$\left( {{({- x})} \oplus x} \right) \oplus {y = \left( {{({- x})} \oplus x} \right)} \oplus z$$

             $$y \oplus {0 = z} \oplus 0$$

             $$y = z$$

             $$\left\lbrack {{Lema}8} \right\rbrack\forall x,{y \in B}\exists\mathtt{\mathrm{!}}{z \in B}x \oplus {z = y}$$

             Prueba:

             $$z{: = \left( {- x} \right)} \oplus y$$

             $$x \oplus {z = x} \oplus \left( {\left( {- x} \right) \oplus y} \right)$$

             $$x \oplus {z = \left( {x \oplus \left( {- x} \right)} \right)} \oplus y$$

             $$x \oplus {z = 0} \oplus y$$

             $$x \oplus {z = y}$$

             $$\left\lbrack {{Lema}9} \right\rbrack\forall x,{y \in B}\exists\mathtt{\mathrm{!}}{z \in B}z \oplus {x = y}$$

             Prueba:

             $$z{: = y} \oplus \left( {- x} \right)$$

             $$z \oplus {x = \left( {y \oplus \left( {- x} \right)} \right)} \oplus x$$

             $$z \oplus {x = y} \oplus \left( {\left( {- x} \right) \oplus x} \right)$$

             $$z \oplus {x = y} \oplus 0$$

             $$z \oplus {x = y}$$

             $$\left\lbrack {{Lema}10} \right\rbrack\forall{x \in B}{\left( {- \left( {- x} \right)} \right) = x}$$

             Prueba:

             $$x \oplus {\left( {- x} \right) = 0}$$

             $$\left( {- x} \right) \oplus {x = 0}$$

             $$x \oplus {\left( {- x} \right) = 0}$$

             $$x = \left( {- \left( {- x} \right)} \right)$$

             $$\left\lbrack {{Lema}11} \right\rbrack{\left( {- 0} \right) = 0}$$

             Prueba:

             $$\left( {- 0} \right) \oplus {0 = 0}$$

             $$\left( {- 0} \right) \oplus {0 = \left( {- 0} \right)}$$

             $$0 = \left( {- 0} \right)$$

             $$\left\lbrack {{Lema}12} \right\rbrack\forall{x \in B}{{0 \cdot x} = 0}$$

             Prueba:

             $$x \oplus {\left( {0 \cdot x} \right) =}$$

             $${= \left( {1 \cdot x} \right)} \oplus {\left( {0 \cdot x} \right) =}$$

             $${= {\left( {1 \oplus 0} \right) \cdot x}} =$$

             $${= {1 \cdot x}} =$$

             $$= x$$

             $$x \oplus {{\left( {0 \cdot x} \right) = x} = x} \oplus 0$$

             $$\left( {0 \cdot x} \right) = 0$$

             $$\left\lbrack {{Lema}13} \right\rbrack\forall{x \in B}{{x \cdot 0} = 0}$$

             Prueba:

             $$\left( {x \cdot 0} \right) \oplus {x =}$$

             $${= \left( {x \cdot 0} \right)} \oplus {\left( {x \cdot 1} \right) =}$$

             $${= {x \cdot \left( {0 \oplus 1} \right)}} =$$

             $${= {x \cdot 1}} =$$

             $$= x$$

             $$\left( {x \cdot 0} \right) \oplus {{0 = x} = 0} \oplus x$$

             $$\left( {x \cdot 0} \right) = 0$$

             $$\left\lbrack {{Lema}14} \right\rbrack\forall x,{y \in B}{\left( {- \left( {x \cdot y} \right)} \right) = {\left( {- x} \right) \cdot y}}$$

             Prueba:

             $$\left( {x \cdot y} \right) \oplus {\left( {\left( {- x} \right) \cdot y} \right) =}$$

             $${\left( {(x) \oplus \left( {- x} \right)} \right) \cdot y} =$$

             $${= {0 \cdot y}} =$$

             $$= 0$$

             $$\left\lbrack {{Lema}15} \right\rbrack\forall x,{y \in B}{\left( {- \left( {x \cdot y} \right)} \right) = {x \cdot \left( {- y} \right)}}$$

             Prueba:

             $$\left( {x \cdot y} \right) \oplus {\left( {x \cdot \left( {- y} \right)} \right) =}$$

             $${= {x \cdot \left( {y \oplus \left( {- y} \right)} \right)}} =$$

             $${= {x \cdot 0}} =$$

             $$= 0$$

             $${\lbrack{{Lema}16}\rbrack}\forall x,{y \in B}{{x \cdot y} = {\left( {- x} \right) \cdot \left( {- y} \right)}}$$

             Prueba:

             $$\left( {- \left( {x \cdot y} \right)} \right) \oplus {\left( {\left( {- x} \right) \cdot \left( {- y} \right)} \right) =}$$

             $${= \left( {\left( {- x} \right) \cdot y} \right)} \oplus {\left( {\left( {- x} \right) \cdot \left( {- y} \right)} \right) =}$$

             $${= {\left( {- x} \right) \cdot \left( {y \oplus \left( {- y} \right)} \right)}} =$$

             $${= \left( {- \left( {x \cdot 0} \right)} \right)} =$$

             $${= \left( {- 0} \right)} =$$

             $$= 0$$

             $$\left\lbrack {{Lema}17} \right\rbrack\forall{x \in B}{{\left( {- 1} \right) \cdot x} = \left( {- x} \right)}$$

             Prueba:

             $$\left( {\left( {- 1} \right) \cdot x} \right) \oplus {x =}$$

             $${= \left( {\left( {- 1} \right) \cdot x} \right)} \oplus {\left( {1 \cdot x} \right) =}$$

             $${= {\left( {\left( {- 1} \right) \oplus 1} \right) \cdot x}} =$$

             $${= {0 \cdot x}} =$$

             $$= 0$$

             $$\left\lbrack {{Lema}18} \right\rbrack\forall{x \in B}1{' = 1}$$

             Prueba:

             $$\left\{ {\left\lbrack {{Axioma}{BR6}} \right\rbrack \land \left\{ {x{: = 1}'} \right\}} \right\}\Rightarrow\left\{ {{1 \cdot 1}{' = 1}'} \right\}$$

             $$\left\{ {\left\lbrack {{Axioma}{BR7}} \right\rbrack \land \left\{ {x{: = 1}} \right\}} \right\}\Rightarrow\left\{ {{1 \cdot 1}{' = 1}} \right\}$$

             $$1{' = {1 \cdot 1}}{' = 1}$$

             $$\left\lbrack {{Lema}19} \right\rbrack\forall{x \in B}{{x \cdot 1} = x}$$

             $${\lbrack{{Notación}1}\rbrack}\text{En adelante no usaremos}1'\text{sino solamente}1\text{.}$$

             $${\lbrack{{Lema}20}\rbrack}\forall{x \in B}{{x \cdot \left( {- 1} \right)} = \left( {- x} \right)}$$

             Prueba:

             $${x \cdot \left( {- 1} \right)} =$$

             $${= \left( {- \left( {x \cdot 1} \right)} \right)} =$$

             $$= \left( {- x} \right)$$

             $${\lbrack{{Lema}21}\rbrack}\forall{e \in B}\left( {\left( {\forall{x \in B}{{e \cdot x} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

             Prueba:

             $$\left( {\left( {\forall{x \in B}{{e \cdot x} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

             $$\left( {x{: = 1}} \right)\left( {{e \cdot 1} = 1} \right)$$

             $${e \cdot 1} = e$$

             $$e = 1$$

             $${\lbrack{{Lema}22}\rbrack}\forall{e \in B}\left( {\left( {\forall{x \in B}{{x \cdot e} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

             Prueba:

             $$\left( {\left( {\forall{x \in B}{{x \cdot e} = x}} \right)\Rightarrow\left( {e = 1} \right)} \right)$$

             $$\left( {x{: = 1}} \right)\left( {{1 \cdot e} = 1} \right)$$

             $${1 \cdot e} = e$$

             $$e = 1$$

             $${\lbrack{{Lema}23}\rbrack}\forall x,{y \in B}{\left( {- \left( {x \oplus y} \right)} \right) = \left( {- y} \right)} \oplus \left( {- x} \right)$$

             Prueba:

             $$\left( {x \oplus y} \right) \oplus {\left( {\left( {- y} \right) \oplus \left( {- x} \right)} \right) =}$$

             $${= \left( {x \oplus \left( {\left( {y \oplus \left( {- y} \right)} \right) \oplus \left( {- x} \right)} \right)} \right)} =$$

             $${= \left( {x \oplus \left( {0 \oplus \left( {- x} \right)} \right)} \right)} =$$

             $${= \left( {x \oplus \left( {- x} \right)} \right)} =$$

             $$= 0$$

             Esta fórmula que acabamos de exponer es la fórmula
             universal para el inverso en cualquier grupo, o in­cluso,
             para cualquier operación con neutro asociativa, siempre que
             existan los inversos, tanto el total como los individuales.

             $${\lbrack{{Teorema}1}\rbrack}\forall x,{y \in B}x \oplus {y = y} \oplus x$$

             Prueba:

             $$\left( {- \left( {x \oplus y} \right)} \right) =$$

             $${= {\left( {- 1} \right) \cdot \left( {x \oplus y} \right)}} =$$

             $${= \left( {\left( {- 1} \right) \cdot x} \right)} \oplus {\left( {\left( {- 1} \right) \cdot y} \right) =}$$

             $${= \left( {- x} \right)} \oplus \left( {- y} \right)$$

             $$= \left( {- \left( {y \oplus x} \right)} \right)$$

             $${- \left( {x \oplus y} \right)} = {- \left( {y \oplus x} \right)}$$

             $$\left( {{- \left( {x \oplus y} \right)} = {- \left( {y \oplus x} \right)}} \right)\Rightarrow\left( {x \oplus {y = y} \oplus x} \right)$$

             $$x \oplus {y = y} \oplus x$$

             El grupo aditivo de un anillo con unidad multiplicativa por
             ambos lados es siempre un grupo abeliano.

             $${\lbrack{{Teorema}2}\rbrack}\forall{x \in B}x \oplus {x = 0}$$

             Prueba:

             $${0 = x} \oplus \left( {- x} \right)$$

             $${0 = x} \oplus \left( {\left( {- x} \right) \cdot \left( {- x} \right)} \right)$$

             $${0 = x} \oplus \left( {x \cdot x} \right)$$

             $${0 = x} \oplus x$$

             **En el grupo aditivo de un anillo booleano** *$$B$$* **es
             siempre** *$$\left( {- x} \right) = x$$*.

             $${\lbrack{{Notación}2}\rbrack}\forall{x \in B}\overline{x}{: = x} \oplus 1$$

             $${\lbrack{{Teorema}3}\rbrack}\forall{x \in B}{{x \cdot \overline{x}} = 0}$$

             Prueba:

             $${x \cdot \overline{x}} =$$

             $${= {x \cdot \left( {x \oplus 1} \right)}} =$$

             $${= {x^{2} \oplus {x \cdot 1}}} =$$

             $${= {x \oplus x}} =$$

             $$= 0$$

             $${\lbrack{{Notación}3}\rbrack}\forall x,{y \in B}{x + y}{: = \left( {x \oplus y} \right)} \oplus \left( {x \cdot y} \right)$$

             $${\lbrack{{Teorema}3}\rbrack}\forall x,{y \in B}{{x \cdot y} = {y \cdot x}}$$

             Prueba:

             $${\lbrack A\rbrack}{{\left( {x + y} \right)^{2} = {{{x^{2} + {x \cdot y}} + {y \cdot x}} + y^{2}}} = {{{x + {x \cdot y}} + {y \cdot x}} + y}}$$

             $${\lbrack B\rbrack}{\left( {x + y} \right)^{2} = {x + y}}$$

             $$\mathit{De}{\lbrack A\rbrack}y{\lbrack B\rbrack}:$$

             $${x + y} = {{{x + {x \cdot y}} + {y \cdot x}} + y}$$

             $$0 = {{x \cdot y} + {y \cdot x}}$$

             $${x \cdot y} = {{- y} \cdot x}$$

             $${x \cdot y} = {y \cdot x}$$

             **La operación multiplicativa de un anillo de Boole $$B$$
             es siempre abeliana. Un anillo de Boole es una categoría
             anidada dentro de la categoría de los anillos
             conmutativos.**

             $${\lbrack{{Teorema}4}\rbrack}\forall{x \in B}{{x \cdot \overline{x}} = 0}$$

             Prueba:

             $${x \cdot \overline{x}} =$$

             $${= {x \cdot \left( {x \oplus 1} \right)}} =$$

             $${= {x^{2} \oplus {x \cdot 1}}} =$$

             $${= {x \oplus x}} =$$

             $$= 0$$

             $${\lbrack{{Teorema}5}\rbrack}\forall{x \in B}x \oplus {\overline{x} = 1}$$

             Prueba:

             $$x \oplus {\overline{x} =}$$

             $${= {x \oplus \left( {x \oplus 1} \right)}} =$$

             $${= \left( {x \oplus x} \right)} \oplus {1 =}$$

             $${= {0 \oplus 1}} =$$

             $$= 1$$

             $${\lbrack{{Teorema}6}\rbrack}\forall{x \in B}{{x + \overline{x}} = 1}$$

             Prueba:

             $${x + \overline{x}} =$$

             $${= \left( {x \oplus \overline{x} \oplus \left( {x \cdot \overline{x}} \right)} \right)} =$$

             $${= {1 \oplus 0}} =$$

             $$= 1$$

             $${\lbrack{{Teorema}7}\rbrack}\forall{x \in B}{{x + x} = x}$$

             Prueba:

             $${x + x} =$$

             $${= \left( {x \oplus x \oplus \left( {x \cdot x} \right)} \right)} =$$

             $${= {0 \oplus x}} =$$

             $$= x$$

             $${\lbrack{{Teorema}8}\rbrack}\forall{x \in B}{{x + 0} = x}$$

             Prueba:

             $${x + x} =$$

             $${= \left( {\left( {x \oplus 0} \right) \oplus \left( {x \cdot 0} \right)} \right)} =$$

             $${= {x \oplus 0}} =$$

             $$= x$$

             $${\lbrack{{Teorema}9}\rbrack}\forall x,{y \in B}{{x + y} = {y + x}}$$

             Prueba:

             $${x + y} =$$

             $${= \left( {x \oplus y} \right)} \oplus {\left( {x \cdot y} \right) =}$$

             $${= \left( {y \oplus x} \right)} \oplus {\left( {y \cdot x} \right) =}$$

             $$= {y + x}$$

             $${\lbrack{{Teorema}10}\rbrack}\forall x,y,{z \in B}{{\left( {x + y} \right) + z} = {x + \left( {y + z} \right)}}$$

             Prueba:

             $${\lbrack A\rbrack}{{{({x + y})} + z} =}$$

             $${{({{({x \oplus y})} \oplus {({x \cdot y})}})} + z} =$$

             $${= {({{({x \oplus y})} \oplus {({x \cdot y})}})}} \oplus z \oplus {{({{({{({x \oplus y})} \oplus {({x \cdot y})}})} \cdot z})} =}$$

             $${= x} \oplus y \oplus {({x \cdot y})} \oplus z \oplus {({x \cdot z})} \oplus {({y \cdot z})} \oplus {({{x \cdot y} \cdot z})}$$

             $${\lbrack B\rbrack}{{x + {({y + z})}} =}$$

             $${= x} \oplus {({y + z})} \oplus {{({x \cdot {({y + z})}})} =}$$

             $${= x} \oplus {({y \oplus z \oplus {({y \cdot z})}})} \oplus {{({x \cdot {({y \oplus z \oplus {({y \cdot z})}})}})} =}$$

             $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{obtenemos:}$$

             $${= x} \oplus y \oplus z \oplus {({y \cdot z})} \oplus {({x \cdot y})} \oplus {({x \cdot z})} \oplus {({{x \cdot y} \cdot z})}$$

             $${\left( {{({x + y})} + z} \right) + \left( {x + {({y + z})}} \right)} = 0$$

             $${\lbrack{{Teorema}11}\rbrack}\forall x,y,{z \in B}{{{({x + y})} \cdot z} = {{({x \cdot z})} + {({y \cdot z})}}}$$

             Prueba:

             $${\lbrack A\rbrack}{{{({x + y})} \cdot z} =}$$

             $${{({{({x \oplus y})} \oplus {({x \cdot y})}})} \cdot z} =$$

             $${({{({x \cdot z})} \oplus {({y \cdot z})}})} \oplus {({{x \cdot y} \cdot z})}$$

             $${\lbrack B\rbrack}{{{({x \cdot z})} + {({y \cdot z})}} =}$$

             $${({{({x \cdot z})} \oplus {({y \cdot z})}})} \oplus {({{x \cdot y} \cdot z})}$$

             $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{se obtiene la igualdad deseada.}$$

             $${\lbrack{{Teorema}12}\rbrack}\forall x,y,{z \in B}{{{({x \cdot y})} + z} = {{({x + z})} \cdot {({y + z})}}}$$

             Prueba:

             $${\lbrack A\rbrack}{{{({x \cdot y})} + z} =}$$

             $${= {{({x \cdot y})} + z}} =$$

             $${= {({{({x \cdot y})} \oplus z})}} \oplus {{({{({x \cdot y})} \cdot z})} =}$$

             $${= {({x \cdot y})}} \oplus z \oplus {({{x \cdot y} \cdot z})}$$

             $${\lbrack B\rbrack}{{{({x + z})} \cdot {({y + z})}} =}$$

             $${= {{({{({x \oplus z})} \oplus {({x \cdot z})}})} \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}}} =$$

             $${= {({{x \cdot {({y \oplus z})}} \oplus {x \cdot {({y \cdot z})}}})}} \oplus {({{z \cdot {({y \oplus z})}} \oplus {z \cdot {({y \cdot z})}}})} \oplus {{({{{x \cdot z} \cdot {({y \oplus z})}} \oplus {{x \cdot z} \cdot {({y \cdot z})}}})} =}$$

             $${= {x \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}}} \oplus {z \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}} \oplus {{{x \cdot z} \cdot {({{({y \oplus z})} \oplus {({y \cdot z})}})}} =}$$

             $${= {({{({{x \cdot y} \oplus {x \cdot z}})} \oplus {({{x \cdot y} \cdot z})}})}} \oplus {({{({{z \cdot y} \oplus {z \cdot z}})} \oplus {({{z \cdot y} \cdot z})}})} \oplus {{({{({{{x \cdot z} \cdot y} \oplus {{x \cdot z} \cdot z}})} \oplus {({{{x \cdot z} \cdot y} \cdot z})}})} =}$$

             $${= {x \cdot y}} \oplus {x \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {z \cdot y} \oplus {z \cdot z} \oplus {{z \cdot y} \cdot z} \oplus {{x \cdot z} \cdot y} \oplus {{x \cdot z} \cdot z} \oplus {{{{x \cdot z} \cdot y} \cdot z} =}$$

             $${= {x \cdot y}} \oplus {x \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {y \cdot z} \oplus z \oplus {y \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {x \cdot z} \oplus {{{x \cdot y} \cdot z} =}$$

             $${= {x \cdot y}} \oplus {{x \cdot y} \cdot z} \oplus {y \cdot z} \oplus z \oplus {y \cdot z} \oplus {{x \cdot y} \cdot z} \oplus {{{x \cdot y} \cdot z} =}$$

             $${= {x \cdot y}} \oplus {y \cdot z} \oplus z \oplus {y \cdot z} \oplus {{{x \cdot y} \cdot z} =}$$

             $${= {x \cdot y}} \oplus z \oplus {{{x \cdot y} \cdot z} =}$$

             $${= \left( {x \cdot y} \right)} \oplus z \oplus \left( {{x \cdot y} \cdot z} \right)$$

             $$\text{De}{\lbrack A\rbrack}\text{y}{\lbrack B\rbrack}\text{se obtine la igualdad deseada.}$$

    5.  Estudio de las funciones booleanas, sobre álgebras de Boole
        finitas.

        1.  Estudiaremos sólo las funciones $$f:{B^{n}\rightarrow B}$$
            dónde $${B = B_{2}} = {\{ 0,1\}}$$. Esto es
            $$f:{{B_{2}}^{n}\rightarrow B_{2}}$$.
        2.  Formas normales. Toda función
            $$f:{{B_{2}}^{n}\rightarrow B_{2}}$$ se puede poner en la
            forma
            $$f{{({x_{1,}x_{2,...},x_{n}})} = {\sum\limits_{k = 1}^{m < 2^{n}}{\prod\limits_{l = 1}^{n}x_{l}}}}$$.
        3.  En general, el número de funciones de un conjunto $$C$$de
            cardinal $$n_{C} \in \mathbb{N}$$ en un conjunto $$D$$de
            cardinal $$n_{D} \in \mathbb{N}$$será $${n_{D}}^{n_{C}}$$.
            Así una función de $$n$$ variables ordenadas en $$C$$con
            valores en $$D$$será $${n_{D}}^{({n_{C}}^{n})}$$. Para el
            caso en que $${C = D} = B_{2}$$que toma como argumento$$n$$
            variables, obtenemos que el número de funciones será de
            $$2^{(2^{\mathbf{\mathrm{n}}})}$$. En una pequeña tabla
            vemos como crece esta cantidad:

+--------------------------+-------------------------------------------+
| $$\mathbf{N}$$ variables | > Número de funciones distintas:          |
|                          | > $$2^{(2^{\mathbf{\mathrm{N}}})}$$       |
+--------------------------+-------------------------------------------+
| > 0                      | > 2                                       |
+--------------------------+-------------------------------------------+
| > 1                      | > 4                                       |
+--------------------------+-------------------------------------------+
| > 2                      | > 16                                      |
+--------------------------+-------------------------------------------+
| > 3                      | > 256                                     |
+--------------------------+-------------------------------------------+
| > 4                      | > 65536                                   |
+--------------------------+-------------------------------------------+
| > 5                      | > 4294967296                              |
+--------------------------+-------------------------------------------+
| > 6                      | > 18446744073709551616                    |
+--------------------------+-------------------------------------------+
| > 7                      | > 340282366920938463463374607431768211456 |
+--------------------------+-------------------------------------------+

7.  1.  El punto anterior es fácil de probar:

        1.  Para el caso de $$N = 0$$ y de $$N = 1$$ es fácil probar
            (por enumeración) la vali­dez de la fórmula. Más tarde
            mostraremos tablas de todas las funciones hasta $$N = 2$$
            inclusive.

        2.  Para el caso general, la ***Hipótesis de Inducción*** será
            :$${\lbrack\mathbf{\mathit{HI}}\rbrack}\forall{N \in {({\mathbb{N} \cup {\{ 0\}}})}}{{0 \leq N} \leq {n - 1}}\Rightarrow 2^{(2^{\mathbf{\mathrm{N}}})}\mathit{es}\mathit{el}\mathit{cardinal}\mathit{buscado.}$$

        3.  Veremos si para el caso $$N = n$$ se sigue cumpliendo la
            fórmula anterior. Pero esto es claro: al añadir una variable
            en el argumento tendremos todas las funcio­nes del caso
            $$N = {n - 1}$$ $$(2^{n - 1})$$ para el valor $$0$$ de la
            nueva variable y otros $$(2^{n - 1})$$ para el valor $$1$$
            de la nueva variable, y no quedan otros casos. Las funciones
            totales para $$N = n$$ serán :

            $$\mathit{card}{{({{\{{f:{{B_{\mathbf{\mathrm{2}}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}} \times {\{{f:{B_{\mathbf{\mathrm{2}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}}})} =}$$

            $${= {{({\mathit{card}{({\{{f:{B_{\mathbf{\mathrm{2}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}})}})} \cdot {({\mathit{card}{({\{{f:{B_{\mathbf{\mathrm{2}}}^{\mathbf{\mathrm{n - 1}}}\rightarrow B_{\mathbf{\mathrm{2}}}}{\mid}f\mathit{es}\mathit{función}}\}})}})}}} =$$
            $${{{= {{(2^{(2^{\mathbf{\mathrm{n - 1}}})})} \cdot {(2^{(2^{\mathbf{\mathrm{n - 1}}})})}}} = {(2^{{(2^{\mathbf{\mathrm{n - 1}}})} + {(2^{\mathbf{\mathrm{n - 1}}})}})}} = {(2^{2 \cdot {(2^{\mathbf{\mathrm{n - 1}}})}})}} = {(2^{(2^{\mathbf{\mathrm{n}}})})}$$.

            Y así queda establecida la fórmula.

    2.  Como se ve en el punto anterior, el crecimiento es desmesurado
        al compararlo al crecimiento lineal de los argumentos. En un
        futuro, cuan­do intentemos hacer reducciones de expresiones
        booleanas, este crecimiento nos im­pedirá construir métodos
        eficaces para resolver las minimizaciones.

    3.  Aunque hemos visto que podemos poner las expresiones booleanas
        en los conjuntos de operadores
        ![](./ObjectReplacements/Object 112){width="6.246cm"
        height="0.492cm"}, por comprensibilidad y para una lectura
        normal se utilizan frecuentemente los dos primeros conjuntos
        unidos, pu­diendo variarse bien el orden de los operadores
        binarios: ![](./ObjectReplacements/Object 113){width="3.692cm"
        height="0.508cm"}. El primer conjunto
        *![](./ObjectReplacements/Object 114){width="1.718cm"
        height="0.506cm"}*será el que estudiemos por defecto, el segundo
        se tratará con una simetría de dualidad (hay que tener algunos
        cuidados). El conjunto elegido de operaciones se llamará
        ***desarrollo en sumas de productos de términos simples (una
        variable, o su negada, o una constante)***. También se llamará
        desarrollo por **minitérminos** o ***SOP (inglés)*** o
        ***SdP***. El segundo será el ***desarrollo en producto de sumas
        de términos simples (una variable, o su negada, o una
        constante)***. También se llamará desarrollo por
        **maxitérminos** o ***POS (inglés)*** o ***PdS***.

    4.  En el desarrollo por ***minitérminos*** expresamos sólo los
        términos de la expresión en que la función tiene como valor
        $$\mathbf{1}$$. Veamos:

        1.  $${f_{B_{\mathbf{\mathrm{2}}}}{({x_{1,}x_{2,...},x_{n}})}} = {\sum\limits_{{({i_{1,}i_{2...,}i_{n}})} = {({0,...,0})}}^{{({1,...,1})}\text{All Combinations}}{({\sigma_{1}^{({i_{1,}i_{2...,}i_{n}})}{{(i_{1})} \cdot \sigma_{2}^{({i_{1,}i_{2...,}i_{n}})}}{{(i_{2})} \cdot}...{\cdot \sigma_{n}^{({i_{1,}i_{2...,}i_{n}})}}{(i_{n})}})}}$$

            $$\mathit{dónde}\sigma_{k}^{({i_{1,}i_{2...,}i_{n}})}{{(i_{k})} \in {\{{i_{k},\overline{i_{k}}}\}}}y{\{{{0 \leq k} \leq n}\}}$$

        2.  Para más sencillez:

            $${{{{f_{B_{\mathbf{\mathrm{2}}}}{(x)}} = {f_{B_{2}}{({x_{1,}x_{2,...},x_{n}})}}} = {\sum\limits_{\iota \in {B_{\mathbf{\mathrm{2}}}}^{\mathbf{\mathrm{n}}}}{({\sigma_{1}^{\iota}{{(\iota_{1})} \cdot \sigma_{2}^{\iota}}{{(\iota_{2})} \cdot}...{\cdot \sigma_{n}^{\iota}}{{(\iota_{n})} \cdot {f_{B_{2}}{(\iota)}}}})}}} = \sum\limits_{\iota \in {B_{\mathbf{\mathrm{2}}}}^{\mathbf{\mathrm{n}}}}}{({\sigma^{\iota} \cdot {f_{B_{2}}{(\iota)}}})}$$$$\mathit{dónde}\sigma_{k}^{\iota}{{(\iota_{k})} \in {\{{\iota_{k},\overline{\iota_{k}}}\}}}y{{0 \leq k} \leq n}y\sigma^{\iota}\mathit{es}\mathit{un}\mathit{minitérmino}$$

        3.  Cuándo la sigma (el minitérmino) es en todos los casos (para
            todas las iotas) completo (es un producto de
            ***$$\mathbf{{n - \mathit{términos}}\mathit{simples}}$$***),
            el valor de la función en esa iota concreta indica si el
            minitérmino aparece o no.

    5.  En el desarrollo por maxitérminos de una función de
        ***$$\mathbf{n}$$*** variables, los
        ***$$\mathbf{\mathit{maxitérminos}}$$*** son sumatorios de
        ***$$\mathbf{{n - \mathit{términos}}\mathit{simples}}$$***. Así
        termina consis­tiendo la función en un producto de maxitérminos.
        Los maxitérminos indican un ***$$\mathbf{0}$$*** de la función.

    6.  Además de expresar las funciones por cadenas de símbolos que
        constituyen un térmi­no, existe una posibilidad de expresar estas
        funciones por tablas lineales o por cua­dros (tablas
        bidimensionales). Para cada combinación de valores booleanos a
        la en­trada de una función obtenemos un valor booleano de salida.

    7.  Para que las funciones booleanas representen algo de interés
        para la ingeniería, lo primero que debemos tener es una forma de
        representar la información que queremos procesar. ¿Cómo
        representamos un número?. ¿Cómo una letra?. Haremos un alto en
        la exposición de funciones booleanas, para detallar más esta
        pregunta, poder respon­derla y así ver para qué estamos viendo
        las álgebras de Boole.

8.  Representación de la información.

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
        $${\{ 0\}} \cup {\{{1 \cdot {\lbrack{\{ 0,1\}}\rbrack}^{\ast}}\}}$$*,
        dónde \'$$\cdot$$\'* quiere decir seguido o conca­tenado, y
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
        autocom­plementario Aitken), códigos con distancias sucesivas 1
        (para longitud fija) (códigos continuos), códigos continuos con
        distancia 1 entre el primer elemento y el último elemento o
        circulares. Códigos especulares. Si son circulares y especulares
        se llaman códigos Gray (de una determinada longitud fija).
        Códigos con redundancia de infor­mación, entre los que destacan
        los códigos Hamming.

        Podéis ver que en los códigos antes explicitados y sus
        propiedades hacen referencia necesaria a algo más que al
        conjunto de las palabras de un lenguaje, que se puede re­sumir en
        un orden en las palabras. Esto viene dado normalmente por el
        significado de las palabras.

    5.  Hemos hablado de alfabetos, lenguajes sobre un alfabeto y
        después sobre el orden sobre esas palabras. Si llamamos a las
        reglas que cumplen las palabras de un lenguaje respecto a un
        alfabeto la gramática de ese lenguaje, el último elemento, el
        del orden, o más en general los significados, son la semántica.

    6.  En 3 hablamos de un lenguaje de los números naturales sobre un
        alfabeto $$\mathbf{B}_{\mathbf{\mathrm{2}}}$$. En general: ¿qué
        número significa 1001? ¿y el 1011101?. A qué valor natural
        apunta cada cadena es algo exterior al léxico y su gramática.
        Vamos a construir una semánti­ca: llamamos en una cadena de
        letras del alfabeto
        $$l_{\mathbf{\mathrm{n - 1}}}\ldots l_{\mathbf{\mathrm{1}}}l_{\mathbf{\mathrm{0}}}$$a
        $$l_{\mathbf{\mathrm{0}}}$$el dígito me­nos significativo
        (el**$$\mathbf{lsb}$$**) y al$$l_{\mathbf{\mathrm{n - 1}}}$$el
        dígito más significativo (el **$$\mathbf{\mathrm{msb}}$$**).
        Pri­mero asignamos unos valores naturales a los del alfabeto
        $$\nu:{B_{\mathbf{\mathrm{2}}}\rightarrow\mathbf{\mathbb{N}}}::\begin{Bmatrix}
        {\mathbf{0_{\mathrm{2}}}@0} \\
        {\mathbf{1_{\mathrm{2}}}@1}
        \end{Bmatrix}$$, y según el subíndice $$\mathbf{n}$$ de la letra
        $$l_{\mathbf{\mathrm{n}}}$$ obtenemos el valor
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
        \end{matrix}$$, el valor de una palabra del lenguaje (código)
        $$r \in {d_{i \neq 0} \cdot {\lbrack\mathbf{D}_{\mathbf{\mathrm{n}}}\rbrack}^{\ast}}$$
        será
        $$\nu{(r)}{=}{\sum\limits_{\iota = 0}^{l{{(r)} - 1}}{({\nu{{(d_{\mathbf{\mathrm{\iota}}})} \cdot {(n^{\mathbf{\mathrm{\iota}}})}}})}}$$,
        y $$l{(r)}$$ es la longitud de la representación $$r$$. Este
        tipo de representación es la más usada en el ámbito de los
        números desde hace seiscientos o setecientos años más o menos en
        Occidente, sólo que para base 10 (diez dígitos distintos).
        Nosotros usaremos también bastante la base 2, código que
        llamamos habitualmente binario natural.

    7.  Aquí es conveniente tener claro cómo pasamos de una base a otra.
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

    8.  Para describir letras, esto es, caracteres alfabéticos de la
        lengua natural, utilizamos generalmente el código ASCII (de 7
        bits el estándar original o de 8 dígitos binarios o bits, el
        extendido de Microsoft). Existen otros códigos, como el EBCDIC
        de IBM, UTF8, UTF16 y Unicode. Permiten sobradamente trasladar
        los lenguajes naturales escritos a un alfabeto binario.

    9.  El conjunto de los naturales es insuficiente para muchas
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
            general*$${{\left\{ \mathbf{0} \right\} \vee \left\{ \mathbf{00} \right\}} \vee \left\{ \mathbf{10} \right\}} \vee \left( {{\mathbf{D}_{\mathbf{\mathrm{2}}} \cdot \left( {\mathbf{D}_{\mathbf{\mathrm{n}}} \smallsetminus \left\{ d_{0} \right\}} \right)} \cdot \left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\ast}} \right)$$*,
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

                $$\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}:{\mathbf{D}_{\mathbf{\mathrm{n}}}\rightarrow\mathbf{D}_{\mathbf{\mathrm{n}}}}::\delta@\mathbf{\upsilon}\left( {{{n - 1} - \mathbf{\nu}}{(\delta)}} \right)$$*$$C_{\mathbf{\mathrm{Β\mathit{m1}}}}:{\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}\rightarrow\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}}::\delta_{n - 1}\cdots\delta_{1}\delta_{0}{:\rightarrow}\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{n - 1}\cdots\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{1}\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{0}$$*

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

            2.  Ahora ya podemos saber como interpretar los números
                negativos en represen­tación CbB. El
                $$\mathbf{\mathit{msb}}$$será $$\mathbf{1}$$, a
                continuación ***no*** tendremos un dígito
                $$\mathbf{d}_{\mathbf{\mathrm{n - 1}}}$$, sino cualquier
                otro, y una ristra finita cualquiera de dígitos sobre el
                alfabeto $$\mathbf{D}_{\mathbf{\mathrm{n}}}$$. Para
                cualquier palabra sobre el alfabeto dicho definimos el
                valor en Complemento a la base B con 1 y con 0.

                $$\forall{\mathit{r} \in \left\{ \left\lbrack \mathbf{D}_{\mathbf{\mathrm{n}}} \right\rbrack^{\mathbf{\mathrm{\ast}}} \right\}}\mathit{definimos}\mathit{el}\mathit{valor}\mathit{entero}$$

                $$\mathbf{\nu_{Β,1}}{(\mathit{r})}{: =}{\mathbf{n}^{\mathbf{\mathrm{l}}{(\mathit{r})}} - {\sum\limits_{\mathbf{\mathrm{\iota = 0}}}^{{\mathbf{\mathrm{l}}{(\mathit{r})}} - \mathbf{\mathrm{1}}}{({\mathbf{\nu}{{(\mathit{r}_{\mathbf{\mathrm{\iota}}})} \cdot \mathbf{n}^{\mathbf{\mathrm{\iota}}}}})}}}$$

                $$y$$

                $$\mathbf{\nu_{Β,0}}{(\mathit{r})}{: =}{\sum\limits_{\mathbf{\mathrm{\iota = 0}}}^{{\mathbf{\mathrm{l}}{(\mathit{r})}} - \mathbf{\mathrm{1}}}{({\mathbf{\nu}{{(\mathit{r}_{\mathbf{\mathrm{\iota}}})} \cdot \mathbf{n}^{\mathbf{\mathrm{\iota}}}}})}}$$

            3.  Ahora nos disponemos a representar el lenguaje de las
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

    10. La siguiente ampliación es $$\mathbb{Q}$$. Existen de entrada
        dos formas comunes de repre­sentación: en punto fijo y en punto
        flotante.

    11. En punto fijo tendremos siempre que saber dónde se encuentra el
        punto o coma deci­mal, conociendo cual es la longitud de la parte
        fraccionaria
        ($$\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{(\mathit{r})}$$)
        y cual la de la parte entera
        ($$\mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}{(\mathit{r})}$$).
        Hasta el momento solo hemos utilizado
        $$\mathbf{l}{{(\mathit{r})} = \mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}}{{(\mathit{r})} + \mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}}{(\mathit{r})}$$dónde
        $$\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{{(\mathit{r})} = \mathbf{0}}$$.

    12. Representaciones de binario natural en punto fijo. Vamos a ver,
        en un primer mo­mento, estas representaciones solo si son
        positivas, esto es, representaciones de
        $$\mathbb{Q}^{\mathbf{\mathrm{+}}}$$en binario natural, que será
        la base para el resto de representaciones más com­plejas. En
        principio la parte entera vendrá dada por una expresión del tipo
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
        necesario una vez se conocen la longitudes de las partes entera
        y fraccionaria.

    13. El siguiente paso es ¿cómo pasamos un número en punto fijo de
        una base a otra?. Para esto lo más sencillo es separar el número
        en punto fijo en dos partes, la entera y la fraccionaria. La
        parte entera, un número natural, seguirá siendo entera en
        cualquier base, por lo que aplicamos las reglas de conversión
        que ya conocemos para n-ario na­tural, ya vistas.

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
            *$$\exists p,{q \in \mathbb{N}}{n^{p} = m}o{n = m^{q}}o{n^{p} = m^{q}}$$*.
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
                *$$({1/3})$$$$=$$$${0.\widehat{3}}_{\mathbf{\mathrm{\mathtt{\mathrm{10}}}}}$$$$=$$$${0.\widehat{01}}_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}}$$$$=$$$$0.1_{\mathbf{\mathrm{\mathtt{\mathrm{3}}}}}$$$$=$$$${0.\widehat{1}}_{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}$$$$=$$$${0.\widehat{13}}_{\mathbf{\mathrm{\mathtt{\mathrm{5}}}}}$$$$=$$$${0.2}_{\mathbf{\mathrm{\mathtt{\mathrm{6}}}}}$$$$=$$$${0.\widehat{2}}_{\mathbf{\mathrm{\mathtt{\mathrm{7}}}}}$$$$=$$$${0.\widehat{25}}_{\mathbf{\mathrm{\mathtt{\mathrm{8}}}}}$$$$=$$*$${0.3}_{\mathbf{\mathrm{\mathtt{\mathrm{9}}}}}$$$$= \ldots =$$$${0.4}_{\mathbf{\mathrm{\mathtt{\mathrm{12}}}}}$$$$= \ldots =$$$${0.5}_{\mathbf{\mathrm{\mathtt{\mathrm{15}}}}}$$$$= \ldots =$$$${0.\widehat{5}}_{\mathbf{\mathrm{\mathtt{\mathrm{16}}}}}$$$$= \ldots =$$$${0.9}_{\mathbf{\mathrm{\mathtt{\mathrm{27}}}}}$$$$= \ldots$$.

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
                *$$\exists p,{q \in \mathbb{N}}{n^{p} = m}o{n = m^{q}}o{n^{p} = m^{q}}$$*,
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
                números enteros en pantalla en $$M\text{\&}S$$(y en
                cualquier base incluida la base 10).

            6.  Por lo demás es fácil conseguir la representación de la
                parte fraccionaria en $$\mathit{CbB}$$ si ésta es
                negativa. Se realizan las operaciones de la misma forma
                que la hacíamos con la parte entera, solo que allí
                teníamos en cuenta la longi­tud de la representación,
                pero aquí, para la parte fraccionaria el complemento lo
                conseguimos básicamente con el complemento de la parte
                fraccionaria a la unidad
                $$\mathtt{\mathrm{1.0\ldots 0\ldots}}$$.

    14. El último tipo de representación que vamos a ver es la
        representación en punto flo­tante
        ($$\mathit{floating}\mathit{point}$$, de forma que en C,C++ al
        tipo de números con decimales que habitualmente llamamos reales,
        toman el nombre de su forma de representación :
        $$\mathit{float}$$). Este tipo está estandarizado (IEEE-754) y
        tenemos un documento que lo detalla bastante bien. Este tipo
        tiene ventajas (relativas) con respecto al punto fijo porque
        amplía bastante el rango de valores a representar con el mismo
        número de dígitos, y porque se controla el error de
        representación en forma proporcional al valor absoluto del
        número, esto es, trabajamos con errores relativos, mientras en
        punto fijo se trabaja con errores absolutos que son fijos en
        todo el rango de representaciones. Como parte negativa hay que
        decir que los circuitos para trabajar con punto flotante son más
        complejos y voluminosos que los que teníamos para punto fijo,
        que eran los mismos circuitos que teníamos para trabajar con
        enteros.

    15. Siguiendo con los códigos que utilizamos en Electrónica Digital,
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

    16. Por ejemplo, el código $$\mathtt{{BCD} - {natural}}$$está dentro
        de
        $$\mathtt{\mathrm{L}}^{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}\left( B_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}} \right)$$,
        pero no son idénticos. Enumeraré los valores en una tabla de dos
        columnas:

+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| > $$\mathtt{{BCD} - {natural}}$$ | > $$\mathtt{\mathrm{L}}^{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}\left( B_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}} \right)$$ |
+==================================+===========================================================================================================================+
| 0000                             | 0000                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0001                             | 0001                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0010                             | 0010                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0011                             | 0011                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0100                             | 0100                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0101                             | 0101                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0110                             | 0110                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 0111                             | 0111                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 1000                             | 1000                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| 1001                             | 1001                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| \-\-\--                          | 1010                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| \-\-\--                          | 1011                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| \-\-\--                          | 1100                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| \-\-\--                          | 1101                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| \-\-\--                          | 1110                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| \-\-\--                          | 1111                                                                                                                      |
+----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

9.  1.  Los códigos$$\mathtt{BCD}$$son códigos de longitud fija, por lo
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
        $$\mathtt{{dígito}{BCD}}$$, y es apropiado para tratamiento muy
        rápido de la in­formación mediante registros de desplazamientos y
        otros dispositivos:

        $$\{{({00000,0})},{({00001,1})},{({00011,2})},{({00111,3})},{({01111,4})},$$

        $${({11111,5})},{({11110,6})},{({11100,7})},{({11000,8})},{({10000,9})}\}$$

10. Tratamiento del error en códigos de longitud fija.

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
            cambien unos símbolos del alfabeto por otros, obteniendo así
            una palabra del código válida o no. Si la palabra re­cibida
            en el Emisor es recibida con cambios que no la convierten en
            una palabra prohibida (no del código común), el error pasará
            desapercibido. Por otra parte si per­cibimos una palabra
            errónea del Receptor, bien podremos corregirlo, bien no.

        4.  Suposiciones varias que hacen el tratamiento de errores
            manejable (suposiciones ra­zonables).

            1.  La longitud de la palabra enviada permanece inalterable.
                No se pierden bits por el trayecto: se transmutarán en
                otros pero no seguirá siendo un $$n - \mathit{código}$$.
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
                poner un límite real­mente permisivo). Así permitimos
                que$$p_{\mathit{error}}{{({1\mathit{bit}})} \in {{\lbrack{0,0,39}\rbrack} \cup {\lbrack{0,61,1}\rbrack}}}$$,
                y por la reducción vista antes tenemos que
                $$p_{\mathit{error}}{{({1\mathit{bit}})} \in {\lbrack{0,0,78}\rbrack}}$$con
                su media en $$0,39$$. Con un error de $$0,50$$el sistema
                es plenamente aleatorio. No hay absolutamente nada que
                hacer.
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
            $$\mathtt{\mathrm{n}} - \mathit{código}$$, la distancia
            Hamming en­tre dos palabras de longitud
            $$\mathtt{\mathrm{n}}$$ sobre un alfabeto
            $$\mathtt{\mathrm{A}}$$, digamos
            $$\mathtt{\mathrm{a}}{: = l_{n - 1}^{a}}\ldots l_{1}^{a}l_{0}^{a}$$y
            $$\mathtt{\mathrm{b}}{: = l_{n - 1}^{b}}\ldots l_{1}^{b}l_{0}^{b}$$,
            definimos:

            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}\left( \mathtt{\mathrm{a,b}} \right) ≝ \#\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$

            En palabras, es el número de bits que son diferentes entre
            ambas palabras (posición por posición).

        7.  La función definida anteriormente, formalmente,
            *$$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}:L^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{B_{2}}} \right) \times L^{\mathtt{\mathrm{n}}}}{{{\left( \mathtt{\mathrm{B_{2}}} \right)\rightarrow{\lbrack{0,n}\rbrack}} \subset \mathbb{N}} \subset \mathbb{R}}::\left( \mathtt{\mathrm{a,b}} \right)@\#\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$*es
            una distancia bien definida matemáticamente, la distancia
            entre dos palabras iguales es siempre 0, y si son distintas
            es necesariamente distinta de 0. Siempre es un número mayor
            o igual que 0 como corresponde a un cardinal de un conjunto.
            Además es si­métrica, esto es, la distancia entre dos
            palabras
            $$\mathit{de}\mathtt{\mathrm{a}}a\mathtt{\mathrm{b}}$$ es
            idéntica a la distancia
            $$\mathit{de}\mathtt{\mathrm{b}}a\mathtt{\mathrm{a}}$$. Por
            último se cumple la desigualdad triangular, esto es, para
            tres palabras cuales­quiera
            $$\forall{\mathtt{\mathrm{a,b,c}} \in \mathtt{\mathrm{L^{n}}}}\left( \mathtt{\mathrm{B_{2}}} \right)$$
            la distancia Hamming cumple
            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{a,b}} \right) \leq {d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{a,c}} \right) + d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}}\left( \mathtt{\mathrm{c,b}} \right)}}$$.
            Estas tres propiedades pueden verse que normales entre las
            distancias euclídeas normales. De hecho esta distancia nos
            habilita para ver una geometría
            en$$\mathtt{\mathrm{L^{n}}}{\left( \mathtt{\mathrm{B_{2}}} \right) \equiv B_{2}^{n}}$$,
            dónde podemos poner como puntos los
            $$\mathit{minitérminos}$$o bien los
            $$\mathit{maxitérminos}$$, en general, a estos, vistos desde
            el pris­ma geométrico, se les llama $$n - \mathit{cubos}$$.

        8.  Para un código cualquiera de longitud fija definimos ahora
            el concepto de
            $$\mathit{distancia}\mathit{mínima}\text{de un}{\mathtt{\mathrm{n}} - \mathit{código}}$$,
            que es, dado
            $$C^{\mathtt{\mathrm{n}}} \subseteq B_{2}^{\mathtt{\mathrm{n}}}$$,
            $$D_{\min H}\left( C^{n} \right) ≝ \underset{a \neq b}{\overset{{({a,b})} \in {C^{n} \times C^{n}}}{\mathtt{\mathrm{mínimo}}}}\left( {d_{\mathtt{\mathrm{H}}}^{n}\left( \mathtt{\mathrm{a,b}} \right)} \right)$$.
            Para el lenguaje completo
            $$\mathtt{\mathrm{L}}{\left( B_{2} \right) \equiv B_{2}^{\mathtt{\mathrm{n}}}}$$,
            esta distancia mínima es 1. La idea que sigue es muy
            intuitiva: si la distancia entre dos palabras es 0, entonces
            las dos palabras son en realidad la misma, son el mismo
            pun­to-palabra del espacio-código de longitud fija. Si las
            palabras son de longitud 24, 24 es la distancia más alejada
            entre dos palabras y así.

            Para determinar la distancia mínima de un
            $$\mathtt{\mathrm{n}} - \mathit{código}$$hay algunos trucos
            que nos ayudarán:

            1.  Con la primera distancia 1 que encontremos podemos dejar
                de comprobar. La distancia mínima de ese código es 1.

            2.  $$D_{\min H}{\left( B_{2}^{n} \right) = 1}$$.
                Si$$\#{C^{n} = 2^{n}}$$, entonces
                $$D_{\min H}{\left( C^{n} \right) = 1}$$.

            3.  Si $${2^{n - 1} < \#}{C^{n} \leq 2^{n}}$$ entonces
                $${0 < D_{\min H}}{\left( C^{n} \right) \leq 1}$$. Este
                resultado, tipo cota del cardinal del código en función
                de la distancia mínima del código, se puede extender
                para otras distancias mínimas. Por
                ejemplo,$${{n - 1} < D_{\min H}}{\left( C^{n} \right) \leq n}$$solo
                si $${0 < {\# C^{n}}} \leq 2$$.
                Seguimos:$${{n - 2} < D_{\min H}}{\left( C^{n} \right) \leq {n - 1}}$$solo
                si$${2 < {\# C^{n}}} \leq 2²$$. En general
                $${2^{{n - k} - 1} < \#}{C^{\mathtt{\mathrm{n}}} \leq 2^{n - k}}$$
                solo si
                $${{k - 1} < D_{\min H}}{\left( C^{n} \right) \leq k}$$
                con $${1 \leq k} \leq n$$.

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
                es el máxima verosimilitud (esperanza matemática).

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
                $$\mathtt{\mathrm{n}} - \mathit{código}$$ original, en
                un$$\left( \mathtt{\mathrm{n + l}} \right) - \mathit{código}$$.
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
                Por otra parte, **condición necesaria y sufi­ciente para
                que la operación sea inyectiva es que no contenga
                columnas igua­les ni columnas vector 0.**

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

> $$\begin{matrix}
> {{= {\begin{pmatrix}
> 1 & 0 \\
> 0 & 1 \\
> a & b \\
> c & d
> \end{pmatrix} \cdot \begin{pmatrix}
> 1 & 0 & 1 \\
> 0 & 1 & 1
> \end{pmatrix}}} =} \\
> {= \begin{pmatrix}
> 1 & 0 & 1 \\
> 0 & 1 & 1 \\
> a & b & {a \oplus b} \\
> c & d & {c \oplus d}
> \end{pmatrix}}
> \end{matrix}$$

11. 1.  1.  1.  

                La matriz izquierda de la primera fila es la matriz
                generadora de paridades, la de­recha son el código
                original de 4 bits en forma de una palabra por cada
                columna. Por último la matriz inferior son los vectores
                codificados con tres bits de paridad insertos. Solo
                queda ver la transformación inversa correspondiente.
                Para esto vea­mos que si observamos matriz izquierda de
                la primera fila$$\mathtt{\mathrm{H}} = \begin{pmatrix}
                \mathtt{\mathrm{I_{2 \times 2}}} \\
                \mathtt{\mathrm{P_{2x2}}}
                \end{pmatrix}$$. Tomare­mos como matriz decodificadora
                (no necesariamente inyectiva) a

                $$\mathtt{\mathrm{H}}^{\mathbf{\mathrm{\ast}}} = \begin{pmatrix}
                \mathtt{\mathrm{H_{2 \times 2}}} & \mathtt{\mathrm{P_{2 \times 2}^{T}}}
                \end{pmatrix}$$

                $$\mathtt{\mathrm{H^{\mathtt{\mathbf{\mathrm{\ast}}}}}} = \begin{pmatrix}
                1 & 0 & a & c \\
                0 & 1 & b & d
                \end{pmatrix}$$

                Ahora bien, sabemos que:

                $${{\mathtt{\mathrm{H^{\mathbf{\mathrm{\ast}}}}} \cdot \mathtt{\mathrm{H}}} \cdot \mathtt{\mathrm{o}}} = \mathtt{\mathrm{0}}$$

                De dónde obtenemos un sistema de ecuaciones, con estos
                resultados (distintos del resultado trivial):

                $$\mathtt{\mathrm{{P_{2 \times 2}}^{\mathtt{\mathbf{\mathrm{T}}}}}} = \begin{pmatrix}
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
                \end{pmatrix}} =$$

                $$= \begin{pmatrix}
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

                $$\mathtt{\mathrm{{P_{2 \times 2}}^{\mathtt{\mathbf{\mathrm{T}}}}}} = \begin{pmatrix}
                1 & 0 \\
                0 & 1
                \end{pmatrix}$$

                $$\mathtt{\mathrm{H^{\mathtt{\mathbf{\mathrm{\ast}}}}}} = \begin{pmatrix}
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

12. Funciones de Boole de $$n - \mathit{variables}$$ en
    $$1 - \mathit{variable}$$: tablas lineales, 2-dimensiona­les,
    arreglos de tablas 2-dimensionales y otras formas de representación.
    Simplificación en 2 capas de puertas.

    1.  1.  1.   Se trata de hacer lo más pequeño posible un circuito
                lógico, en este caso combinacional. Es equivalente a
                tener el mínimo de puertas posibles (manteniendo la
                estructura 1ª capa INV 2ª capa OR 3ª capa AND). Esto es
                equivalente a tener un número de minitérminos en la
                expresión de la función booleana mínimo. Es claro que si
                no mantenemos la estructura de capas antes dicha, podría
                haber minimizaciones mejores, pero aún así la
                minimización en dos capas es el instrumento adecuado
                para alcanzar otros tipos de minimizaciones.

                El problema de la minimización es NP-Completo. Esto
                quiere decir que es un problema que al intentar
                resolverlo con un algoritmo presenta las siguientes
                características. Primero: los algoritmos conocidos hasta
                ahora crecen en tiempo de realización exponencialmente
                con un incremento lineal del número de variables.
                Segundo: si alguien encontrase un algoritmo que
                solucionara el problema en tiempo polinómico y no
                exponencial, acabaría de demostrar que todo problema se
                puede poner en forma polinómica. Ganaría \$1.000.000.

                Fuera de este curioso asunto hay que decir que los
                métodos por tablas de Karnough tienen un alcance muy
                corto. Podemos ver bien tablas de Karnough de 3, 4, 5 y
                hasta 6 variables de entrada. Para 1, 2 o 3 variables de
                entrada es casi preferible un método de manipulación
                algebraica de la fórmula. Ampliar más allá de las 6
                variables este método es complicado además de que
                tenderemos a equivocarnos con facilidad.

                El método (algoritmo) que extrae lo que hacemos en las
                tablas de Karnough y lo implementa computacionalmente
                para un número cualquiera de variables de entrada es el
                método desarrollado por Quine (el filósofo Willard Van
                Orman Quine) y McCluskey (Edward J. McCluskey). Este
                método que explicaremos en breve, tiene la virtud que
                puede obtener todas las soluciones minimales (ya que
                mínimas pueden no existir), y la desventaja que requiere
                hacer tablas (en memoria) de hasta $$2^{({n - 1})}$$
                minitérminos, la posterior comparación de unos términos
                con otros, por poner un ejemplo, hasta
                $${({n - 1})}{({{(2^{({n - 1})})}/n})}^{2}$$comparaciones
                de minitérminos, sin contar las comparaciones anidadas
                que serían cada vez menores. Después hay otra etapa que
                no es tan gastosa pero que hay que tener en cuenta.
                Estos últimos números hacen que este método no sea el
                indicado cuando el número de variables es demasiado alta
                (depende del ordenador que se utilice, pero piénsese en
                64 bits de entrada: el número de comparaciones
                sería$${{{63 \cdot {({2^{126}/64^{2}})}} \approx {2^{126}/64}} = {2^{126}/2^{6}}} = 2^{120}$$que
                es una cifra más que astronómica). Sin embargo para 16
                bits el cálculo de tiempo máximo nos daría
                aproximadamente
                $${{{15 \cdot {({2^{30}/16^{2}})}} \approx {2^{30}/16}} = {2^{30}/2^{4}}} = 2^{26}$$que
                es una cantidad de cálculos asumible en un computador de
                sobremesa actual.

                Así que aunque el problema sigue siendo de un gran
                volumen se ha desarrollado técnicas que no pretenden
                sacar soluciones minimales, y que solo aspiran a
                soluciones "buenas", con la suerte que habitualmente son
                minimales o casi minimales. Este método no lo
                explicaremos aquí pero diremos que el más utilizado es
                el Espresso II.

                1.  1.   Comenzaremos por ver los métodos de Tablas de
                        Karnough. Para éstas utilizamos códigos Gray de
                        los bits necesarios.

13. Esta tabla nos dice los códigos Gray a utilizar para cada número de
    variables:

  -------------------- ------------- ------------- ------------- ------------- -------------
  Tablas de Karnough   2 variables   3 variables   4 variables   5 variables   6 variables
  Eje X                Gray 1 bit    Gray 1 bit    Gray 2 bits   Gray 1 bit    Gray 2 bits
  Eje Y                Gray 1 bit    Gray 2 bits   Gray 2 bits   Gray 2 bits   Gray 2 bits
  Eje Z                                                          Gray 2 bits   Gray 2 bits
  -------------------- ------------- ------------- ------------- ------------- -------------

> Tablas de Karnough para 2 variables:

> $$\begin{matrix}
> {F{({a,b})}b} & 0 & 1 \\
> a & & \\
> 0 & {F{(0,0)}} & {F{(0,1)}} \\
> 1 & {F{(1,0)}} & {F{(1,1)}}
> \end{matrix}$$

> Significado para el desarrollo por minitérminos:

> $$\begin{matrix}
> {\mathit{Si}F{{({a,b})} = 1}b} & 0 & 1 \\
> a & & \\
> 0 & {\bar{a} \cdot \bar{b}} & {a \cdot \bar{b}} \\
> 1 & {\bar{a} \cdot b} & {a \cdot b}
> \end{matrix}$$

> Significado para el desarrollo por maxitérminos:

> $$\begin{matrix}
> {\mathit{Si}F{{({a,b})} = 0}b} & 0 & 1 \\
> a & & \\
> 0 & {a + b} & {\bar{a} + b} \\
> 1 & {a + \bar{b}} & {\bar{a} + \bar{b}}
> \end{matrix}$$

> Tablas de Karnough para 3 variables:

> $$\begin{matrix}
> {F{({a,b,c})}c} & 0 & 1 \\
> \mathit{ab} & & \\
> 00 & {F{({0,0,0})}} & {F{({0,0,1})}} \\
> 01 & {F{({0,1,0})}} & {F{({0,1,1})}} \\
> 11 & {F{({1,1,0})}} & {F{({1,1,1})}} \\
> 10 & {F{({1,0,0})}} & {F{({1,0,1})}}
> \end{matrix}$$

> Significado para el desarrollo por minitérminos:

> $$\begin{matrix}
> {\mathit{Si}F{{({a,b,c})} = 1}c} & 0 & 1 \\
> \mathit{ab} & & \\
> 00 & {{\bar{a} \cdot \bar{b}} \cdot \bar{c}} & {{\bar{a} \cdot \bar{b}} \cdot c} \\
> 01 & {{\bar{a} \cdot b} \cdot \bar{c}} & {{\bar{a} \cdot b} \cdot c} \\
> 11 & {{a \cdot b} \cdot \bar{c}} & {{a \cdot b} \cdot c} \\
> 10 & {{a \cdot \bar{b}} \cdot \bar{c}} & {{a \cdot \bar{b}} \cdot c}
> \end{matrix}$$

> Significado para el desarrollo por maxitérminos:

> $$\begin{matrix}
> {\mathit{Si}F{{({a,b,c})} = 0}c} & 0 & 1 \\
> \mathit{ab} & & \\
> 00 & {{a + b} + c} & {{a + b} + \bar{c}} \\
> 01 & {{a + \bar{b}} + c} & {{a + \bar{b}} + \bar{c}} \\
> 11 & {{\bar{a} + \bar{b}} + c} & {{\bar{a} + \bar{b}} + \bar{c}} \\
> 10 & {{\bar{a} + b} + c} & {{\bar{a} + b} + \bar{c}}
> \end{matrix}$$

> Tablas de Karnough para 4 variables:

> $$\begin{matrix}
> {F{({a,b,c,d})}\mathit{cd}} & 00 & 01 & 11 & 10 \\
> \mathit{ab} & & & & \\
> 00 & {F{({0,0,0,0})}} & {F{({0,0,0,1})}} & {F{({0,0,1,1})}} & {F{({0,0,1,0})}} \\
> 01 & {F{({0,1,0,0})}} & {F{({0,1,0,1})}} & {F{({0,1,1,1})}} & {F{({0,1,1,0})}} \\
> 11 & {F{({1,1,0,0})}} & {F{({1,1,0,1})}} & {F{({1,1,1,1})}} & {F{({1,1,1,0})}} \\
> 10 & {F{({1,0,0,0})}} & {F{({1,0,0,1})}} & {F{({1,0,1,1})}} & {F{({1,0,1,0})}}
> \end{matrix}$$

> Significado para el desarrollo por minitérminos:

> $$\begin{matrix}
> {\mathit{Si}F{{({a,b,c,d})} = 1}\mathit{cd}} & 00 & 01 & 11 & 10 \\
> \mathit{ab} & & & & \\
> 00 & {{{\bar{a} \cdot \bar{b}} \cdot \bar{c}} \cdot \bar{d}} & {{{\bar{a} \cdot \bar{b}} \cdot \bar{c}} \cdot d} & {{{\bar{a} \cdot \bar{b}} \cdot c} \cdot d} & {{{\bar{a} \cdot \bar{b}} \cdot c} \cdot \bar{d}} \\
> 01 & {{{\bar{a} \cdot b} \cdot \bar{c}} \cdot \bar{d}} & {{{\bar{a} \cdot b} \cdot \bar{c}} \cdot d} & {{{\bar{a} \cdot b} \cdot c} \cdot d} & {{{\bar{a} \cdot b} \cdot c} \cdot \bar{d}} \\
> 11 & {{{a \cdot b} \cdot \bar{c}} \cdot \bar{d}} & {{{a \cdot b} \cdot \bar{c}} \cdot d} & {{{a \cdot b} \cdot c} \cdot d} & {{{a \cdot b} \cdot c} \cdot \bar{d}} \\
> 10 & {{{a \cdot \bar{b}} \cdot \bar{c}} \cdot \bar{d}} & {{{a \cdot \bar{b}} \cdot \bar{c}} \cdot d} & {{{a \cdot \bar{b}} \cdot c} \cdot d} & {{{a \cdot \bar{b}} \cdot c} \cdot \bar{d}}
> \end{matrix}$$

> Significado para el desarrollo por maxitérminos:

> $$\begin{matrix}
> {\mathit{Si}F{{({a,b,c,d})} = 0}\mathit{cd}} & 00 & 01 & 11 & 10 \\
> \mathit{ab} & & & & \\
> 00 & {{{a + b} + c} + d} & {{{a + b} + c} + \bar{d}} & {{{a + b} + \bar{c}} + \bar{d}} & {{{a + b} + \bar{c}} + d} \\
> 01 & {{{a + \bar{b}} + c} + d} & {{{a + \bar{b}} + c} + \bar{d}} & {{{a + \bar{b}} + \bar{c}} + \bar{d}} & {{{a + \bar{b}} + \bar{c}} + d} \\
> 11 & {{{\bar{a} + \bar{b}} + c} + d} & {{{\bar{a} + \bar{b}} + c} + \bar{d}} & {{{\bar{a} + \bar{b}} + \bar{c}} + \bar{d}} & {{{\bar{a} + \bar{b}} + \bar{c}} + d} \\
> 10 & {{{\bar{a} + b} + c} + d} & {{{\bar{a} + b} + c} + \bar{d}} & {{{\bar{a} + b} + \bar{c}} + \bar{d}} & {{{\bar{a} + b} + \bar{c}} + d}
> \end{matrix}$$

> Tablas de Karnough para 5 variables:

> $$\begin{matrix}
>  & {F{({a,b,c,d,e})}\mathit{cd}} & 00 & 01 & 11 & 10 \\
> e & \mathit{ab} & & & & \\
>  & 00 & {F{({0,0,0,0,0})}} & {F{({0,0,0,1,0})}} & {F{({0,0,1,1,0})}} & {F{({0,0,1,0,0})}} \\
> 0 & 01 & {F{({0,1,0,0,0})}} & {F{({0,1,0,1,0})}} & {F{({0,1,1,1,0})}} & {F{({0,1,1,0,0})}} \\
>  & 11 & {F{({1,1,0,0,0})}} & {F{({1,1,0,1,0})}} & {F{({1,1,1,1,0})}} & {F{({1,1,1,0,0})}} \\
>  & 10 & {F{({1,0,0,0,0})}} & {F{({1,0,0,1,0})}} & {F{({1,0,1,1,0})}} & {F{({1,0,1,0,0})}} \\
>  & {\mathit{cd}} & 00 & 01 & 11 & 10 \\
> e & \mathit{ab} & & & & \\
>  & 00 & {F{({0,0,0,0,1})}} & {F{({0,0,0,1,1})}} & {F{({0,0,1,1,1})}} & {F{({0,0,1,0,1})}} \\
> 1 & 01 & {F{({0,1,0,0,1})}} & {F{({0,1,0,1,1})}} & {F{({0,1,1,1,1})}} & {F{({0,1,1,0,1})}} \\
>  & 11 & {F{({1,1,0,0,1})}} & {F{({1,1,0,1,1})}} & {F{({1,1,1,1,1})}} & {F{({1,1,1,0,1})}} \\
>  & 10 & {F{({1,0,0,0,1})}} & {F{({1,0,0,1,1})}} & {F{({1,0,1,1,1})}} & {F{({1,0,1,0,1})}}
> \end{matrix}$$

> Tablas de Karnough para 6 variables:

> $$\begin{matrix}
>  & {{F{({a,b,c,d,e,f})}}\mathit{cd}} & 00 & 01 & 11 & 10 & & {\mathit{cd}} & 00 & 01 & 11 & 10 \\
> \mathit{ef} & \mathit{ab} & & & & & {\mathit{ef}} & \mathit{ab} & & & & \\
>  & 00 & {F{({0,0,0,0,0,0})}} & {F{({0,0,0,1,0,0})}} & {F{({0,0,1,1,0,0})}} & {F{({0,0,1,0,0,0})}} & & 00 & {F{({0,0,0,0,0,1})}} & {F{({0,0,0,1,0,1})}} & {F{({0,0,1,1,0,1})}} & {F{({0,0,1,0,0,1})}} \\
> 00 & 01 & {F{({0,1,0,0,0,0})}} & {F{({0,1,0,1,0,0})}} & {F{({0,1,1,1,0,0})}} & {F{({0,1,1,0,0,0})}} & {01} & 01 & {F{({0,1,0,0,0,1})}} & {F{({0,1,0,1,0,1})}} & {F{({0,1,1,1,0,1})}} & {F{({0,1,1,0,0,1})}} \\
>  & 11 & {F{({1,1,0,0,0,0})}} & {F{({1,1,0,1,0,0})}} & {F{({1,1,1,1,0,0})}} & {F{({1,1,1,0,0,0})}} & & 11 & {F{({1,1,0,0,0,1})}} & {F{({1,1,0,1,0,1})}} & {F{({1,1,1,1,0,1})}} & {F{({1,1,1,0,0,1})}} \\
>  & 10 & {F{({1,0,0,0,0,0})}} & {F{({1,0,0,1,0,0})}} & {F{({1,0,1,1,0,0})}} & {F{({1,0,1,0,0,0})}} & & 10 & {F{({1,0,0,0,0,1})}} & {F{({1,0,0,1,0,1})}} & {F{({1,0,1,1,0,1})}} & {F{({1,0,1,0,0,1})}} \\
>  & {\mathit{cd}} & 00 & 01 & 11 & 10 & & {\mathit{cd}} & 00 & 01 & 11 & 10 \\
> \mathit{ef} & \mathit{ab} & & & & & {\mathit{ef}} & \mathit{ab} & & & & \\
>  & 00 & {F{({0,0,0,0,1,0})}} & {F{({0,0,0,1,1,0})}} & {F{({0,0,1,1,1,0})}} & {F{({0,0,1,0,1,0})}} & & 00 & {F{({0,0,0,0,1,1})}} & {F{({0,0,0,1,1,1})}} & {F{({0,0,1,1,1,1})}} & {F{({0,0,1,0,1,1})}} \\
> 10 & 01 & {F{({0,1,0,0,1,0})}} & {F{({0,1,0,1,1,0})}} & {F{({0,1,1,1,1,0})}} & {F{({0,1,1,0,1,0})}} & {11} & 01 & {F{({0,1,0,0,1,1})}} & {F{({0,1,0,1,1,1})}} & {F{({0,1,1,1,1,1})}} & {F{({0,1,1,0,1,1})}} \\
>  & 11 & {F{({1,1,0,0,1,0})}} & {F{({1,1,0,1,1,0})}} & {F{({1,1,1,1,1,0})}} & {F{({1,1,1,0,1,0})}} & & 11 & {F{({1,1,0,0,1,1})}} & {F{({1,1,0,1,1,1})}} & {F{({1,1,1,1,1,1})}} & {F{({1,1,1,0,1,1})}} \\
>  & 10 & {F{({1,0,0,0,1,0})}} & {F{({1,0,0,1,1,0})}} & {F{({1,0,1,1,1,0})}} & {F{({1,0,1,0,1,0})}} & & 10 & {F{({1,0,0,0,1,1})}} & {F{({1,0,0,1,1,1})}} & {F{({1,0,1,1,1,1})}} & {F{({1,0,1,0,1,1})}}
> \end{matrix}$$

> 

> 
