1.  **Algunos convenios**:

<!-- -->

1.  1.  $$0 \notin {\mathbb{N}}$$Ante la definición de los naturales
        nosotros adoptamos este convenio.

    2.  $${\mathbb{N}}_{0}{\qquad ≝ \qquad}{{\mathbb{N}} \cup \left\{ 0 \right\}}$$Conjunto
        de los naturales extendidos que ya tiene el cero.

    3.  Definición recurrente de los
        conjuntos$$\lbrack 0,1\rbrack_{\mathbb{Q}}$$y$$\lbrack 0,1\rbrack_{\mathbb{Q}}^{n}$$,
        dónde $${n \in {\mathbb{N}}}\qquad{n > 1}$$:

        1.  1.  $$\lbrack 0,1\rbrack_{\mathbb{Q}}{\qquad ≝ \qquad}{\lbrack 0,1\rbrack \cap {\mathbb{Q}}}$$
            2.  $$\phantom{{\forall{n \in {{\mathbb{N}} \smallsetminus \left\{ 0,1 \right\}}}}\mspace{144mu}}\lbrack 0,1\rbrack_{\mathbb{Q}}^{1}{\qquad ≝ \qquad}\lbrack 0,1\rbrack_{\mathbb{Q}}$$
            3.  $$\phantom{{\forall{n \in {{\mathbb{N}} \smallsetminus \left\{ 0,1 \right\}}}}\mspace{144mu}}{{{\lbrack 0,1\rbrack_{\mathbb{Q}}}^{n}{: = {{\lbrack 0,1\rbrack_{\mathbb{Q}}}^{n - 1} \times {\lbrack 0,1\rbrack_{\mathbb{Q}}}^{1}}}}{\mspace{72mu}\forall{n \in {{\mathbb{N}} \smallsetminus {\{ 0,1\}}}}}}$$

    4.  Por lo general los elementos de un conjunto se representarán por
        letras minúsculas (alfa­betos griego y latino) con o sin
        suscriptores
        (ejemplo:$$a_{3}$$o![](./ObjectReplacements/Object 1513){width="0.425cm"
        height="0.467cm"}o![](./ObjectReplacements/Object 1514){width="0.982cm"
        height="0.374cm"}o![](./ObjectReplacements/Object 1515){width="0.422cm"
        height="0.344cm"}) y dí­gitos decimales ($$\{{0,1,\ldots,9}\}$$),
        mientras que los conjuntos se representarán por letras
        mayúsculas (alfabetos griego y latino), igualmente con o sin
        suscriptores. Este convenio será válido a excepción que se
        exprese de forma explícita otro nombre para elementos y/o
        conjuntos.

    5.  En ocasiones aseguraremos que existe un conjunto asociado a un
        elemento: en general serán letras mayúsculas como corresponde a
        un conjunto, pero con un subscriptor que estará escrito
        exactamente como el elemento. La única excepción que se dará es
        un elemento cubierto con la tilde circunfleja, para expresar el
        conjunto de elementos complementa­rios con uno dado.

    6.  A veces aparecerá una operación binaria,
        digamos![](./ObjectReplacements/Object 1573){width="0.859cm"
        height="0.467cm"}, dónde los puntos se sustitu­yen con los
        argumentos. Cuando expresemos$$a \ast B$$, o sea, el elemento
        $$a$$operado con un conjunto$$B$$, se trata una operación
        binaria que no es la original. Se interpreta­rá
        como$${a \ast B} = {\{{{a \ast b}{\qquad \mid \qquad}{b \in B}}\}}$$,
        esto es, un conjunto. Igualmente, puede ocurrir que esta misma
        operación aparezca entre dos
        conjuntos:$${A \ast B} = {\{{{a \ast b}{\qquad \mid \qquad}{{a \in A},{b \in B}}}\}}$$.

    7.  El universo en el que nos moveremos
        será![](./ObjectReplacements/Object 1579){width="0.51cm"
        height="0.563cm"}, por lo que para el cuantificador univer­sal
        (que evitaremos en lo posible) no pondremos ningún símbolo, de
        forma que, cuando aparezca una variable de elementos o de
        conjuntos sin haber sido cuantificada, supondremos que se aplica
        el cuantificador universal a la variable situándola dentro
        de![](./ObjectReplacements/Object 1580){width="0.51cm"
        height="0.563cm"}. Si el cuantificador universal debiera
        aplicarse a una variable sobre otro conjunto subconjunto
        de![](./ObjectReplacements/Object 1581){width="0.51cm"
        height="0.563cm"}, se intentará omitir el cuantificador
        universal, pero se precederá la sentencia con una indicación
        sobre la pertenencia del elemento al conjunto. Para cualquier
        elemento en el que no aparezca su pertenencia es porque
        pertenece al
        universal![](./ObjectReplacements/Object 1582){width="0.51cm"
        height="0.563cm"}. Al igual, cuando una variable que asume un
        valor que es un conjunto, éste será parte
        de![](./ObjectReplacements/Object 1583){width="1.829cm"
        height="0.624cm"}, que no aparecerá de forma explícita. Para las
        variables conjunto se repite todo lo anterior con la diferencia
        de que se
        cambia![](./ObjectReplacements/Object 1585){width="0.51cm"
        height="0.563cm"}por
        ![](./ObjectReplacements/Object 1321){width="1.829cm"
        height="0.624cm"}.

2.  Álgebra de Boole.

    1.  Axiomas para un álgebra de
        Boole![](./ObjectReplacements/Object 1){width="7.008cm"
        height="0.667cm"}.

        La operación uno-aria que se utilizará frecuentemente (la
        complementación), en los axiomas será introducida como
        definición y no supuesta inicialmente más que como la existencia
        de un conjunto de elementos no vacío asociados a otro que
        cumplen unos requisi­tos. Sin embargo esta operación es tan
        importante en las álgebras de Boole que la forma normal de
        escribirse la estructura es
        $$\left\langle {,{\left\{ {0_{},1_{}} \right\} \subseteq},{0_{} \neq 1_{}},{\mathit{op}\left\{ {\mathit{bin}:\left\{ {+ , \cdot} \right\}} \right\},\left\{ {\mathit{una}:\left\{ \overline{\phantom{A}} \right\}} \right\}}} \right\rangle$$.

        Además, la distinción entre los dos neutros no siempre se
        requiere. Esto tiene poco impacto, ya que el único álgebra de
        Boole dónde los dos neutros son iguales coincide con el álgebra
        de Boole con un solo elemento, que es el álgebra de Boole
        trivial.

        Los postulados de Huntington (artículos en 1904,1932 -este
        último desarrolla un con­junto de 3 axiomas, uno de ellos llamado
        específicamente Axioma de Huntington, y no es el caso aquí
        expuesto, en esta primera formalización-) definen qué sea un
        álgebra de Boole
        ![](./ObjectReplacements/Object 1094){width="3.173cm"
        height="0.572cm"}:

        1.  **\[Axioma H0\]** De
            ser![](./ObjectReplacements/Object 1323){width="0.51cm"
            height="0.563cm"}un conjunto, las operaciones binarias
            funciones y de la existencia
            de![](./ObjectReplacements/Object 613){width="0.422cm"
            height="0.467cm"}y![](./ObjectReplacements/Object 1072){width="0.411cm"
            height="0.467cm"}en$$$$:

            1.  **\[H0.0.0\]**
                ![](./ObjectReplacements/Object 1316){width="0.51cm"
                height="0.563cm"}es un conjunto (por ejemplo en la
                axiomatización de Zermelo-Fraenkel-Skolem o más
                brevemente, **ZFS**, o digamos la más extensa
                Neumann-Gödel-Bernays, abreviadamente, **NGB**).
            2.  **\[H0.0.1\]** Para la suma
                ![](./ObjectReplacements/Object 1073){width="0.492cm"
                height="0.467cm"}:$$0 \in$$
            3.  **\[H0.0.2\]** Para el producto
                ![](./ObjectReplacements/Object 1092){width="0.445cm"
                height="0.467cm"}:![](./ObjectReplacements/Object 1074){width="1.053cm"
                height="0.563cm"}
            4.  **\[H0.1\]** Para la suma
                ![](./ObjectReplacements/Object 499){width="0.492cm"
                height="0.467cm"}:![](./ObjectReplacements/Object 2){width="5.819cm"
                height="0.577cm"}
            5.  **\[H0.2\]** Para la multiplicación
                ![](./ObjectReplacements/Object 18){width="0.445cm"
                height="0.467cm"}:![](./ObjectReplacements/Object 3){width="5.666cm"
                height="0.577cm"}

        2.  **\[Axioma H1\]** Existencia del elemento identidad o
            neutro:

            1.  **\[H1.1\]** Para la suma
                ![](./ObjectReplacements/Object 210){width="0.492cm"
                height="0.467cm"}:
                ![](./ObjectReplacements/Object 500){width="3.006cm"
                height="0.563cm"}
            2.  **\[H1.2\]** Para la multiplicación
                ![](./ObjectReplacements/Object 197){width="0.445cm"
                height="0.467cm"}:
                ![](./ObjectReplacements/Object 198){width="2.842cm"
                height="0.563cm"}

        3.  **\[Axioma H2\]** Conmutabilidad:

            1.  **\[H2.1\]** Para la suma
                ![](./ObjectReplacements/Object 501){width="0.492cm"
                height="0.467cm"}:
                ![](./ObjectReplacements/Object 4){width="5.022cm"
                height="0.577cm"}
            2.  **\[H2.2\]** Para la multiplicación
                ![](./ObjectReplacements/Object 19){width="0.445cm"
                height="0.467cm"}:
                ![](./ObjectReplacements/Object 5){width="4.715cm"
                height="0.577cm"}

        4.  **\[Axioma H3\]** Propiedad distributiva:

            1.  **\[H3.1\]** De la
                suma![](./ObjectReplacements/Object 502){width="0.492cm"
                height="0.467cm"}sobre el
                producto![](./ObjectReplacements/Object 523){width="0.445cm"
                height="0.467cm"}(o, inversamente, **sacar sumando
                común**):

                ![](./ObjectReplacements/Object 6){width="8.181cm"
                height="0.577cm"}

            2.  **\[H3.2\]** Del
                producto![](./ObjectReplacements/Object 524){width="0.445cm"
                height="0.467cm"}sobre la suma
                ![](./ObjectReplacements/Object 503){width="0.492cm"
                height="0.467cm"}(o, inversamente, **sacar factor
                común**):

                ![](./ObjectReplacements/Object 7){width="8.027cm"
                height="0.577cm"}

        5.  **\[Axioma H4\]** Existencia de complementario:

            1.  **\[H4\]**![](./ObjectReplacements/Object 8){width="4.253cm"
                height="0.563cm"} tal que
                ![](./ObjectReplacements/Object 1324){width="1.464cm"
                height="0.467cm"}se cumplen las dos sub-fórmulas
                siguientes:

                1.  **\[H4.1\]**$${x + y} = 1$$
                2.  **\[H4.2\]**$$x{\mspace{9mu} \cdot \mspace{9mu}}{y = 0}$$

    Como ejemplos que cumplen los anteriores postulados o axiomas (a los
    que llamaremos propiamente modelos de la teoría de Álgebras de Boole
    axiomatizada según los anteriores axiomas) vamos a desarrollar unos
    cuántos de ellos.

    **\[Ejemplo 1\]** **El álgebra de las partes de un
    conjunto**![](./ObjectReplacements/Object 1317){width="0.527cm"
    height="0.469cm"}.

    El ejemplo primero y más sencillo de ver es el álgebra de las partes
    de un conjunto. Dado que para un conjunto
    cualquiera![](./ObjectReplacements/Object 83){width="0.529cm"
    height="0.467cm"},![](./ObjectReplacements/Object 1046){width="3.371cm"
    height="0.58cm"}es también un conjunto en cualquiera de los dos
    sistemas axiomáticos de teoría de conjuntos mencionados.

    Además![](./ObjectReplacements/Object 1051){width="6.479cm"
    height="0.58cm"}, dónde se verifica
    que![](./ObjectReplacements/Object 1068){width="4.544cm"
    height="0.64cm"}.

    Definiremos![](./ObjectReplacements/Object 1050){width="1.907cm"
    height="0.58cm"},
    ![](./ObjectReplacements/Object 1325){width="1.145cm"
    height="0.467cm"}y
    ![](./ObjectReplacements/Object 1326){width="1.094cm"
    height="0.467cm"}. Como producto lógico pondremos la intersección de
    conjuntos![](./ObjectReplacements/Object 1052){width="4.644cm"
    height="0.58cm"}y como suma lógica pondremos la unión de
    conjuntos![](./ObjectReplacements/Object 1053){width="4.798cm"
    height="0.58cm"}.

    Las conmutabilidades de la suma y el producto se intercambian
    directamente por la conmutabilidad de la unión y la intersección.

    El elemento neutro de la suma es trivialmente
    el![](./ObjectReplacements/Object 1327){width="0.422cm"
    height="0.467cm"}ya que
    ![](./ObjectReplacements/Object 1328){width="0.57cm"
    height="0.385cm"}es neutro para la unión. Igualmente el neutro del
    producto es el![](./ObjectReplacements/Object 1329){width="0.411cm"
    height="0.467cm"}por ser
    ![](./ObjectReplacements/Object 1330){width="0.549cm"
    height="0.467cm"}el neutro de la intersección en
    ![](./ObjectReplacements/Object 1331){width="1.261cm"
    height="0.58cm"}.

    Las distributividades recaen directamente en las de la unión sobre
    la intersección y de la intersección sobre la unión.

    Sea ![](./ObjectReplacements/Object 1054){width="6.387cm"
    height="0.612cm"}y a partir de ahí sabemos
    que![](./ObjectReplacements/Object 82){width="2.069cm"
    height="0.612cm"}puesto
    que![](./ObjectReplacements/Object 1055){width="4.688cm"
    height="0.531cm"}y en el caso
    que![](./ObjectReplacements/Object 1056){width="1.21cm"
    height="0.467cm"}tenemos que
    ![](./ObjectReplacements/Object 1057){width="3.983cm"
    height="0.531cm"}de forma
    que![](./ObjectReplacements/Object 1058){width="2.736cm"
    height="0.612cm"}por la definición. Ahora sólo se trata de darse
    cuenta
    que$${Y_{X} \cdot X} = {Y_{X} \cap X} = {{({U \smallsetminus X})} \cap X} = \varnothing \equiv 0$$y
    que![](./ObjectReplacements/Object 1065){width="6.334cm"
    height="0.54cm"}, y ya tenemos
    que![](./ObjectReplacements/Object 1066){width="5.978cm"
    height="0.612cm"}habiendo
    tomado![](./ObjectReplacements/Object 1067){width="1.976cm"
    height="0.531cm"}.

    **\[Ejemplo 2\]** **El álgebra de los números que son producto de
    los![](./ObjectReplacements/Object 1318){width="0.422cm"
    height="0.467cm"}primeros números primos.**

    Un ejemplo interesante fácil de construir es el álgebra de Boole de
    los números que son producto de los primeros núme­ros primos
    (cantidad finita de ellos) y sus divisores. Consideramos el
    conjunto![](./ObjectReplacements/Object 184){width="3.097cm"
    height="0.531cm"}, con­sideraremos
    el![](./ObjectReplacements/Object 1626){width="0.411cm"
    height="0.467cm"}booleano cómo
    ![](./ObjectReplacements/Object 185){width="1.852cm"
    height="0.896cm"}y
    el![](./ObjectReplacements/Object 1627){width="0.423cm"
    height="0.467cm"}cómo![](./ObjectReplacements/Object 200){width="1.371cm"
    height="0.587cm"}. Consideramos
    a![](./ObjectReplacements/Object 1069){width="3.822cm"
    height="0.656cm"}, y las operaciones serán el mínimo común múltiplo
    (![](./ObjectReplacements/Object 1319){width="3.621cm"
    height="0.506cm"}) como suma booleana y el máximo común divisor a
    (![](./ObjectReplacements/Object 1320){width="3.353cm"
    height="0.506cm"}) como producto booleano. El complemento de un
    elemento resulta
    ser![](./ObjectReplacements/Object 1070){width="6.731cm"
    height="0.915cm"}. Éste es un modelo fácil de desarrollar para poner
    ejemplos.

    **\[Ejemplo 3\]** Partimos de un álgebra de Boole
    ![](./ObjectReplacements/Object 1312){width="0.51cm"
    height="0.563cm"}cualquiera y un elemento $$x$$
    no![](./ObjectReplacements/Object 1076){width="0.609cm"
    height="0.587cm"}ni$$1_{}$$cualquiera tal
    que![](./ObjectReplacements/Object 1077){width="2.641cm"
    height="0.669cm"}(luego este álgebra de Boole no puede ser el
    trivial ni uno de dos elementos). Definimos ahora un
    conjunto![](./ObjectReplacements/Object 1078){width="3.997cm"
    height="0.61cm"}y![](./ObjectReplacements/Object 1079){width="4.126cm"
    height="0.61cm"}. Las álgebras de Boole nuevas a considerar son
    ![](./ObjectReplacements/Object 1082){width="10.156cm"
    height="0.695cm"}y![](./ObjectReplacements/Object 1083){width="10.146cm"
    height="0.695cm"}. Consideramos el mismo producto booleano que en el
    conjunto inicial e idéntica­mente con la suma booleana (solo que
    restringidos al subconjunto elegido). Sólo varía el complemento, de
    la siguiente
    forma![](./ObjectReplacements/Object 1080){width="3.872cm"
    height="0.612cm"}y![](./ObjectReplacements/Object 1081){width="3.715cm"
    height="0.61cm"}. Es fácil comprobar la validez de esta definición
    de un álgebra de Boole, de manera más concreta, que las operaciones
    son internas y el complemento declarado es también interno y se
    comporta como complemento del nuevo álgebra, esto
    es,![](./ObjectReplacements/Object 1084){width="5.189cm"
    height="0.61cm"}
    que![](./ObjectReplacements/Object 1085){width="5.2cm"
    height="0.61cm"}.

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
    "Tra­tados de Lógica" u "Órganon", hacía ya 2.100 años). Aunque la
    verdadera revolu­ción se da algunos años más tarde con Frege, el
    lógico más importante desde Aristóteles. Si doy estos datos sobre la
    historia de la lógica que todos asociaréis más a la filosofía, que
    parece queda muy lejos del propósito de unos apuntes de matemáticas
    discretas que cubran de la forma más amplia posible los Fundamentos
    de Electrónica en su parte Digital, es porque en realidad no queda
    tan lejos. La idea de hacer un lenguaje dónde el razonamiento
    siguiera unas pautas claras de forma que siempre quedara todo tan
    cierto como en las matemáticas era ya antigua. Aristóteles ya
    advertía de una cierta indefinición insuperable de los términos más
    importantes de la filosofía (en realidad de casi todos los conceptos
    de la vida ordinaria): "existen conceptos o ideas que corresponden
    con la realidad que no se usan de forma equívoca -- esto es, su uso
    no es equívoco, este mismo concepto, palabra o idea que hablamos no
    se refiere a realidades distintas y diferenciadas, de forma que nos
    llevan a confusión -- pero tampoco de forma unívoca -- como las
    definiciones desde axiomas en un lenguaje formal matemático, así
    tenemos que existen conceptos análogos" (es una glosa de palabras de
    Aristóteles). En la Modernidad, dado que el concepto de analogía
    lleva aparejado un tratamiento difícil que no lleva fácilmente a
    certeza, se intentan buscar criterios de certeza absoluta y unas
    definiciones que aparentemente son unívocas y se tratan como tales.
    Es significativo el nombre (y la estructura interna) de una
    importante obra de Spino­za: "Ética demostrada según el orden
    geométrico". Será Leibniz quién escriba ya cumplidamente sobre la
    necesidad de establecer un léxico completamente unívoco (una tarea
    mastodonte, o mejor, imposible) y un "cálculo" del pensamiento, de
    forma que "una cuestión como la existencia de Dios pueda ser
    resuelta mediante la resolución de unas ecuaciones de pensamiento"
    (de nuevo es una glosa). Se empezaba a buscar con ansiedad una
    mecanización del pensamiento. Este motivo fue muy fructífero, dando
    un primer paso hacia él, George Boole que hace un ál­gebra de las
    proposiciones. Esta álgebra no era más amplia que la de Aristóteles
    (de hecho, era solo un subconjunto de la lógica aristotélica), pero
    permitía el cálculo al modo algebraico. De aquí a la llegada de
    Frege, ya, Charles Babbage diseña y realiza (sin éxito debido al
    trabajo de mecanizado ex­cesivamente minucioso que requería el
    diseño) una computadora universal me­cánica (mediante engranajes)
    prácticamente similar al modelo de Von Neumann. La condesa de
    Lovelace (Ada) es la matemática que hace los primeros progra­mas en
    lenguaje ensamblador de la máquina de Babbage. La primera
    programa­dora de la historia. Después viene Frege, al que debemos el
    invento de la Lógica-Matemática, o lógica extensional en aquel
    nacer. Ampliaba inmensamente la lógica aristotélica pues la
    estructura de la proposición no seguía ya el esquema
    sujeto-predicado que se mostraba insuficiente por lo que adopta el
    esquema función-argumentos, además de introducir los cuantificadores
    ("existe al menos un"
    ![](./ObjectReplacements/Object 1266){width="0.476cm"
    height="0.333cm"}y "para todo"
    ![](./ObjectReplacements/Object 1293){width="0.591cm"
    height="0.358cm"}). Después de Frege siguen los desarrollos con
    gente como Ber­trand Rusell, David Hilbert y otros, hasta los
    increíbles resultados de Gödel (y posteriormente Turing) que ponen
    punto final a muchas de las pretensiones de mecanización del
    pensamiento, pero que son ya la base de la computación moderna,
    siendo los trabajos definitivos los de Alan Turing. Como veis el
    camino recorrido es largo y complicado, siendo el momento crucial
    para el arranque de la ingeniería digital los trabajos de George
    Boole. No he mencionado intentos de mecanización más antiguos como
    los del mallorquín Raimundo Lulio, ni la calculadora binaria de
    Leibniz, ni mecanismos remotos como el mecanismo de Anticitera, así
    como el papel fundamental que jugó la crisis de las matemáticas de
    finales del siglo XIX y principios del XX ni el papel de las
    máquinas de cifrado y descifrado de mensajes en la Gran Guerra y la
    II Guerra Mundial (en las que intervinieron muchas de las mentes
    antes mencionadas).

    De manera un tanto informal podemos ver una proposición (una frase
    que afirma o niega una propiedad de un objeto, una relación entre
    objetos o la existencia del mismo, una frase que ha de ser o
    verdadero,![](./ObjectReplacements/Object 1086){width="3.002cm"
    height="0.587cm"}, o
    falso,![](./ObjectReplacements/Object 1087){width="3.129cm"
    height="0.587cm"}). Este conjunto de proposiciones pueden ser
    operadas mediante la conjunción
    'y'(![](./ObjectReplacements/Object 1295){width="0.554cm"
    height="0.467cm"}),
    ![](./ObjectReplacements/Object 1297){width="1.164cm"
    height="0.467cm"}es verdadero
    si![](./ObjectReplacements/Object 1298){width="0.526cm"
    height="0.467cm"}es verdadero
    y![](./ObjectReplacements/Object 1299){width="0.487cm"
    height="0.467cm"}es verdadero a la vez y falso en cualquier otro
    caso. La disyunción sería la
    'o'(![](./ObjectReplacements/Object 1300){width="0.554cm"
    height="0.467cm"}),
    siendo![](./ObjectReplacements/Object 1301){width="1.164cm"
    height="0.467cm"}verdadero con
    que![](./ObjectReplacements/Object 1302){width="0.526cm"
    height="0.467cm"}sea verdadero o lo
    sea![](./ObjectReplacements/Object 1303){width="0.487cm"
    height="0.467cm"}, siendo falso sólo
    cuando![](./ObjectReplacements/Object 1304){width="0.526cm"
    height="0.467cm"}es falso
    y![](./ObjectReplacements/Object 1305){width="0.487cm"
    height="0.467cm"}es falso a la vez. La notación más habitual es
    ![](./ObjectReplacements/Object 1088){width="2.506cm"
    height="0.489cm"}y![](./ObjectReplacements/Object 1089){width="3.29cm"
    height="0.467cm"}. Para el 'no'
    (negación,![](./ObjectReplacements/Object 1306){width="0.482cm"
    height="0.467cm"}) tenemos
    ![](./ObjectReplacements/Object 1090){width="3.628cm"
    height="0.467cm"}. El conjunto de Boole es el conjunto de las
    proposiciones de la que partamos.

    De manera más formal se considera un elemento del álgebra de Boole
    de la lógica a las clases de equivalencia de las proposiciones
    equivalentes lógicamente (en su valor de verdad o falsedad) entre
    sí.

    **\[Ejemplo 5\]** El álgebra de conmutación (Shannon). Esta es el
    álgebra de Boole más sencilla que
    hay:![](./ObjectReplacements/Object 1071){width="2.612cm"
    height="0.61cm"}. Las operaciones las concretaremos en tablas:

    ![](./ObjectReplacements/Object 1091){width="5.78cm"
    height="1.623cm"}

    y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington. Ésta será usada frecuentemente durante el curso. Esta
    álgebra está contenida en todo álgebra de Boole.

    Como diagrama de Hasse (dónde se hace patente un orden en el
    álgebra) tiene

![](Pictures/200000170000011100000D6AF113C5679B46B21D.svm){width="0.273cm"
height="3.434cm"}

3.  **\[Ejemplo 6\]** El álgebra de Boole de 4 elementos. Este es el
    álgebra de Boole generada por un conjunto de 2 elementos. Es
    singular en el sentido que sólo tiene 3 niveles, el más
    bajo$$\{{0 ≝ {\{\}} \equiv \varnothing}\}$$, el
    intermedio![](./ObjectReplacements/Object 1200){width="1.842cm"
    height="0.492cm"}, y el
    superior![](./ObjectReplacements/Object 1202){width="2.111cm"
    height="0.492cm"}.
    ![](./ObjectReplacements/Object 1095){width="3.471cm"
    height="0.61cm"}. Las operaciones las concretaremos en tablas:

    ![](./ObjectReplacements/Object 1096){width="9.488cm"
    height="2.732cm"}y podréis comprobar fácilmente que se cumplen todos
    los postulados de Huntington si
    cam­biáis![](./ObjectReplacements/Object 1203){width="0.441cm"
    height="0.467cm"}por![](./ObjectReplacements/Object 1204){width="0.811cm"
    height="0.48cm"},![](./ObjectReplacements/Object 1205){width="0.425cm"
    height="0.467cm"}por![](./ObjectReplacements/Object 1206){width="0.757cm"
    height="0.48cm"},![](./ObjectReplacements/Object 1744){width="0.411cm"
    height="0.467cm"}por![](./ObjectReplacements/Object 1207){width="1.842cm"
    height="0.492cm"}y![](./ObjectReplacements/Object 1745){width="0.423cm"
    height="0.467cm"}por el conjunto
    vacío![](./ObjectReplacements/Object 1208){width="0.57cm"
    height="0.385cm"}. Su diagrama de Hasse es:

![](Pictures/2000003600000B0600000D019F08206D3B15AC87.svm){width="2.822cm"
height="3.328cm"}

4.  **\[Ejemplo 7\]** El álgebra de Boole de 8 elementos. Este es el
    álgebra de Boole generada por un conjunto de 3 elementos. Es
    singular en el sentido que sólo tiene 4 niveles, el más
    bajo$$\{ 0\}$$, el de
    átomos![](./ObjectReplacements/Object 1209){width="1.64cm"
    height="0.492cm"}, el de
    hiperátomos![](./ObjectReplacements/Object 1210){width="1.884cm"
    height="0.492cm"}y el superior$$\{ 1\}$$. Los niveles de átomos y de
    hiperátomos son especialmente importantes, siendo esta álge­bra de
    Boole, la más pequeña que los diferencia. Sería:

    ![](./ObjectReplacements/Object 1097){width="5.38cm"
    height="0.61cm"}

    Las operaciones las concretaremos en tablas:

    ![](./ObjectReplacements/Object 1629){width="12.206cm"
    height="4.948cm"}

    ![](./ObjectReplacements/Object 1630){width="15.085cm"
    height="3.577cm"}

    y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington si te­néis en cuenta los cambios aconsejados en el
    cuadro entre llaves, dónde las flechas quieren decir "substituir
    por".

    El diagrama de Hasse correspondiente sería:

![](Pictures/2000003200000D9600001219FA1521857C60DA85.svm){width="3.478cm"
height="4.634cm"}

5.  **\[Ejemplo 8\]** El álgebra de Boole de 16 elementos. Este es el
    álgebra de Boole generada por un conjunto de 4 elementos. Es ya un
    álgebra de Boole completamente regular. Tiene 5 niveles, el más bajo
    el$$\{ 0\}$$, el de
    átomos![](./ObjectReplacements/Object 1101){width="2.124cm"
    height="0.492cm"}, el de hiperátomos$$\{{Α,Β,\Gamma,\Delta}\}$$, el
    intermedio![](./ObjectReplacements/Object 1103){width="2.833cm"
    height="0.492cm"}y finalmente el nivel superior con el$$\{ 1\}$$.
    Sería:

    ![](./ObjectReplacements/Object 1099){width="9.453cm"
    height="0.61cm"}

    Las operaciones las concretaremos en tablas:

    ![](./ObjectReplacements/Object 1100){width="12.06cm"
    height="9.444cm"}

>  ![](./ObjectReplacements/Object 1105){width="11.18cm"
> height="1.102cm"}

>  ![](./ObjectReplacements/Object 1628){width="11.728cm"
> height="9.604cm"}

6.  y podréis comprobar fácilmente que se cumplen todos los postulados
    de Huntington, con solo tener en cuenta que todos los elementos se
    pueden poner en función de
    ![](./ObjectReplacements/Object 1509){width="1.958cm"
    height="0.483cm"}y sumas de ellos. Las sumas de dos de los
    anteriores elementos son
    ![](./ObjectReplacements/Object 1510){width="2.94cm"
    height="0.467cm"}y las sumas de tres de ellos
    son![](./ObjectReplacements/Object 1511){width="2.168cm"
    height="0.467cm"}.

    Como diagrama de Hasse tiene:

![](Pictures/200000D100001BD7000014EC91BF966ED9304A6C.svm){width="7.128cm"
height="5.355cm"}

7.  **\[Ejemplo 9\]** El álgebra de Boole de los conjuntos que se pueden
    expresar como unión disyunta finita de sub-intervalos genéricos
    de![](./ObjectReplacements/Object 1250){width="1.639cm"
    height="0.517cm"}. Definimos por conveniencia
    ![](./ObjectReplacements/Object 1631){width="2.006cm"
    height="0.54cm"}. Para esto haremos abstracción de cualquier
    conjunto finito de puntos de
    ![](./ObjectReplacements/Object 1098){width="0.58cm"
    height="0.515cm"}, esto es, consideraremos que dos conjuntos son
    equivalentes si su diferencia simétrica (la unión de las
    diferencias, los elementos que no son comunes de ambos conjuntos) es
    vacía o es un conjunto finito de puntos. Esta álgebra de Boole tiene
    un cardinal infinito numerable (como el cardinal de los números
    naturales). Lo más importante es que no puede desarrollarse de
    manera semejante a como desarrolla­mos el álgebra de las partes de un
    conjunto. Lo formalizaremos del siguiente modo:

    3.  ![](./ObjectReplacements/Object 1259){width="9.567cm"
        height="0.723cm"}

        Si
        escribimos![](./ObjectReplacements/Object 1260){width="1.304cm"
        height="0.54cm"}entonces
        ![](./ObjectReplacements/Object 1261){width="2.127cm"
        height="0.467cm"}

        1.  Sea![](./ObjectReplacements/Object 1632){width="6.415cm"
            height="0.753cm"}

        2.  Sea![](./ObjectReplacements/Object 1634){width="12.719cm"
            height="0.69cm"}

        3.  Sea![](./ObjectReplacements/Object 1633){width="6.976cm"
            height="0.766cm"}

        4.  ![](./ObjectReplacements/Object 1252){width="7.354cm"
            height="0.67cm"}Esta relación es de equivalencia.

            1.  Reflexiva
                ![](./ObjectReplacements/Object 1262){width="4.24cm"
                height="0.556cm"}Luego![](./ObjectReplacements/Object 1263){width="1.177cm"
                height="0.467cm"}

            2.  Simétrica![](./ObjectReplacements/Object 1264){width="10.195cm"
                height="0.519cm"}

            3.  Transitiva![](./ObjectReplacements/Object 1265){width="3.946cm"
                height="0.467cm"}

                1.  ![](./ObjectReplacements/Object 20){width="11.404cm"
                    height="0.556cm"}Y queda de­mostrada la propiedad
                    transitiva.

        5.  A partir de aquí hablaremos de
            ![](./ObjectReplacements/Object 1254){width="0.847cm"
            height="0.482cm"}para hablar de la clase de equivalencia de
            ![](./ObjectReplacements/Object 1268){width="1.542cm"
            height="0.515cm"}bajo la relación de
            equivalencia![](./ObjectReplacements/Object 1636){width="0.579cm"
            height="0.467cm"}.

        6.  A partir de aquí hablaremos de nuestro conjunto de
            Boole![](./ObjectReplacements/Object 1635){width="4.553cm"
            height="0.601cm"}.

        7.  Nuestro conjunto de Boole será
            ![](./ObjectReplacements/Object 1269){width="2.431cm"
            height="0.594cm"}.

        8.  El![](./ObjectReplacements/Object 1270){width="1.483cm"
            height="0.482cm"}

        9.  El![](./ObjectReplacements/Object 1271){width="1.665cm"
            height="0.587cm"}

        10. Ahora veremos unas operaciones muy cercanas a la unión, la
            intersección y el com­plemento, que realmente nos dan un
            álgebra de Boole sobre
            ![](./ObjectReplacements/Object 1637){width="0.945cm"
            height="0.575cm"}:

            ![](./ObjectReplacements/Object 1272){width="3.201cm"
            height="2.108cm"}

        11. Convenio de
            notación:$${⟦{a,b}⟧} ≝ {⟦\left\lbrack {a,b} \right\rbrack_{\mathbb{Q}}⟧}$$.
            Estos conjuntos serán nuestros sub-intervalos genéricos del
            intervalo-unidad genéri­co.

        12. Sea una sucesión finita de un número
            par![](./ObjectReplacements/Object 1218){width="0.794cm"
            height="0.467cm"}de elementos
            de![](./ObjectReplacements/Object 1217){width="1.155cm"
            height="0.54cm"}, estricta­mente
            creciente![](./ObjectReplacements/Object 1219){width="6.034cm"
            height="0.531cm"}dispuestos como

            ![](./ObjectReplacements/Object 1220){width="4.41cm"
            height="0.531cm"}definirán los elementos
            de![](./ObjectReplacements/Object 1221){width="0.945cm"
            height="0.575cm"}, aparte de
            ![](./ObjectReplacements/Object 1222){width="5.011cm"
            height="0.639cm"}

        13. Si
            escribimos![](./ObjectReplacements/Object 1277){width="4.41cm"
            height="0.531cm"}, significamos ya (suponemos que es un
            hecho
            que)![](./ObjectReplacements/Object 1278){width="6.034cm"
            height="0.531cm"}

        14. Ahora ya definimos (notación):
            ![](./ObjectReplacements/Object 1279){width="12.515cm"
            height="1.141cm"}

        15. Ahora ya tenemos el conjunto de Boole que buscábamos:

            ![](./ObjectReplacements/Object 1224){width="12.248cm"
            height="0.586cm"}

    Que las uniones, complementos e intersecciones de intervalos
    genéricos finitos siguen siendo intervalos genéricos finitos es
    claro desde el principio. Sin embargo voy a exponer la cabalística,
    hacer las cuentas vamos, para que no quede lugar a dudas. Toda esta
    comprobación (o redefinición) de
    que![](./ObjectReplacements/Object 1273){width="0.51cm"
    height="0.563cm"}es cerrado bajo las distintas operaciones es quizás
    demasiado laboriosa, enojosa, pero quiero dejar claro este ejemplo
    de un álgebra de Boole no atómica, que por otra parte es la única
    vez que veremos.

    La operación de complemento queda de la siguiente manera, y aunque
    aún no podemos comprobar su corrección, si queda claro que es un
    operación un-aria interna:

    ![](./ObjectReplacements/Object 1226){width="9.992cm"
    height="5.239cm"}

    De dónde
    obtenemos![](./ObjectReplacements/Object 1229){width="3.311cm"
    height="0.563cm"}.

    Tenemos que ![](./ObjectReplacements/Object 1230){width="3.471cm"
    height="0.667cm"}y![](./ObjectReplacements/Object 1231){width="2.942cm"
    height="0.667cm"}y![](./ObjectReplacements/Object 1274){width="2.26cm"
    height="0.517cm"}Además observamos con claridad
    que![](./ObjectReplacements/Object 1276){width="2.932cm"
    height="0.563cm"}tal
    que![](./ObjectReplacements/Object 1638){width="2.783cm"
    height="0.564cm"}y![](./ObjectReplacements/Object 1639){width="2.265cm"
    height="0.529cm"}, además
    de![](./ObjectReplacements/Object 1275){width="2.912cm"
    height="0.563cm"}. Así nos queda
    ![](./ObjectReplacements/Object 1640){width="1.221cm"
    height="0.517cm"} si se verifican los demás axiomas.

    La suma quedará de la siguiente forma:

    ![](./ObjectReplacements/Object 1286){width="9.246cm"
    height="0.552cm"}

    El producto seguirá un camino par:

    ![](./ObjectReplacements/Object 1287){width="9.093cm"
    height="0.552cm"}

    Sólo queda ver que efectivamente las operaciones son internas:

    Prueba:

    1.  1.  Ahora vamos a desarrollar la suma de forma recurrente:

            ![](./ObjectReplacements/Object 1289){width="10.832cm"
            height="0.591cm"}

            Comenzaremos por
            ![](./ObjectReplacements/Object 1288){width="1.101cm"
            height="0.467cm"} y algunos casos especiales:

    ![](./ObjectReplacements/Object 1234){width="12.935cm"
    height="8.5cm"}

    Distintos casos con
    ![](./ObjectReplacements/Object 1232){width="1.087cm"
    height="0.467cm"}

    ![](./ObjectReplacements/Object 1247){width="9.23cm"
    height="2.05cm"}![](./ObjectReplacements/Object 1216){width="9.215cm"
    height="2.789cm"}
    ![](./ObjectReplacements/Object 1283){width="9.2cm"
    height="2.05cm"}![](./ObjectReplacements/Object 1225){width="9.809cm"
    height="2.789cm"}![](./ObjectReplacements/Object 1235){width="9.486cm"
    height="3.378cm"}![](./ObjectReplacements/Object 1236){width="9.744cm"
    height="3.378cm"}![](./ObjectReplacements/Object 1282){width="13.213cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1238){width="11.913cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1237){width="11.88cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1239){width="11.578cm"
    height="4.119cm"}
    ![](./ObjectReplacements/Object 1285){width="12.305cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1281){width="12.305cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1240){width="11.915cm"
    height="4.119cm"}

    Para el caso![](./ObjectReplacements/Object 1644){width="1.087cm"
    height="0.467cm"}o![](./ObjectReplacements/Object 1645){width="1.101cm"
    height="0.467cm"}y especiales queda demostrada el cerramiento de
    ![](./ObjectReplacements/Object 1646){width="0.51cm"
    height="0.563cm"}bajo esta suma reducida. El caso siguiente se
    construye con facilidad por recurrencia en cualquier número finito
    de pasos. Si hacemos sumas comprobadas ya un número de veces finita,
    queda claro que ya no hay más que demostrar.

    Para cualquier![](./ObjectReplacements/Object 1284){width="1.027cm"
    height="0.467cm"}:

    ![](./ObjectReplacements/Object 1241){width="12.37cm"
    height="3.38cm"}

    Queda demostrado que toda suma da como resultado un conjunto finito
    de intervalos gené­ricos.

    A su vez el producto lo vamos a definir de forma recursiva también,
    comenzando primero
    con![](./ObjectReplacements/Object 1228){width="0.499cm"
    height="0.467cm"}siendo la clase de un solo intervalo genérico, o la
    clase del vacío, además de algu­nos casos especiales.

    ![](./ObjectReplacements/Object 1242){width="12.913cm"
    height="8.468cm"}![](./ObjectReplacements/Object 1243){width="11.264cm"
    height="3.378cm"}![](./ObjectReplacements/Object 1244){width="11.728cm"
    height="3.378cm"}![](./ObjectReplacements/Object 1290){width="11.262cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1292){width="10.927cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1291){width="9.67cm"
    height="3.378cm"}![](./ObjectReplacements/Object 1245){width="9.987cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1246){width="9.971cm"
    height="4.119cm"}![](./ObjectReplacements/Object 1248){width="10.582cm"
    height="4.119cm"}

    Para el caso![](./ObjectReplacements/Object 1641){width="1.087cm"
    height="0.467cm"}o![](./ObjectReplacements/Object 1642){width="1.101cm"
    height="0.467cm"}y especiales queda demostrada el cerramiento de
    ![](./ObjectReplacements/Object 1643){width="0.51cm"
    height="0.563cm"}bajo esta suma reducida. El caso siguiente se
    construye con facilidad por recurrencia en cualquier número finito
    de pasos. Si hacemos sumas comprobadas ya un número de veces finita,
    queda claro que ya no hay más que demostrar.

    Para el caso ![](./ObjectReplacements/Object 1280){width="1.027cm"
    height="0.467cm"}:

    ![](./ObjectReplacements/Object 1233){width="9.313cm"
    height="3.38cm"}

    Y queda demostrado que la forma del conjunto producto es una clase
    de unión finita de sub-intervalos genéricos. Luego pertenece a
    nuestro álgebra de Boole.

    Este sistema es muy parecido a un álgebra de conjuntos subálgebra de
    algún conjunto po­tencia, por lo que es fácil determinar que se trata
    de un álgebra de Boole. Sin embargo su cardinal
    es![](./ObjectReplacements/Object 1249){width="4.77cm"
    height="0.476cm"}. Veámoslo:

    ![](./ObjectReplacements/Object 1647){width="13.457cm"
    height="4.768cm"}![](./ObjectReplacements/Object 1648){width="10.114cm"
    height="1.683cm"}

    En definitiva es un álgebra numerable (del mismo cardinal que los
    números naturales). Puesto que el cardinal de los números naturales
    ![](./ObjectReplacements/Object 1227){width="0.533cm"
    height="0.385cm"} no es conmensurable con el de la potencia de
    ningún conjunto (es del cardinal infinito más pequeño posible y
    ningún conjunto finito tiene como potencia uno infinito), no existe
    ningún conjunto para el cual esta álgebra de Boole sea semejante
    (isomorfa) a un álgebra de las potencias de un conjunto. Este
    ejemplo será de utilidad más adelante, además de darnos un curioso
    ejemplo de álgebra de Boole nada común.

    **\[Ejemplo 10\]** El álgebra de las funciones de un álgebra de
    Boole sobre otra. Supongamos
    ![](./ObjectReplacements/Object 1612){width="1.88cm"
    height="0.563cm"}dónde![](./ObjectReplacements/Object 1613){width="0.515cm"
    height="0.467cm"}es una función. Llamaremos
    ![](./ObjectReplacements/Object 1614){width="9.442cm"
    height="0.577cm"}a nuestro conjunto de Boole.
    ![](./ObjectReplacements/Object 1617){width="0.811cm"
    height="0.601cm"}es la función que asigna el cero
    de![](./ObjectReplacements/Object 1616){width="0.683cm"
    height="0.563cm"}a cualquier elemento
    de![](./ObjectReplacements/Object 1615){width="0.51cm"
    height="0.563cm"}. Igualmente
    ![](./ObjectReplacements/Object 1618){width="0.803cm"
    height="0.601cm"}es la función que asigna el uno
    de![](./ObjectReplacements/Object 1623){width="0.683cm"
    height="0.563cm"}a cualquier elemento
    de![](./ObjectReplacements/Object 1624){width="0.51cm"
    height="0.563cm"}. Las operaciones internas a introducir son:

    La suma de
    funciones:![](./ObjectReplacements/Object 1625){width="5.898cm"
    height="0.577cm"}

    La multiplicación de
    funciones:![](./ObjectReplacements/Object 1739){width="5.592cm"
    height="0.577cm"}

    La función
    complemento:![](./ObjectReplacements/Object 1740){width="7.542cm"
    height="0.577cm"}

    De esta álgebra podemos entresacar otros conjuntos de funciones
    interesantes, como. Por ejemplo:

    ![](./ObjectReplacements/Object 1741){width="14.418cm"
    height="4.537cm"}

    y aún otros subconjuntos más pequeños serían las inyecciones de los
    anteriores homomorfismos. Si
    ![](./ObjectReplacements/Object 1743){width="1.344cm"
    height="0.563cm"}entonces uno de los conjuntos de aplicaciones más
    interesantes son los endomorfimos o isomorfimos en sí mismo.

    Además el kernel de cualquier homomorfismo es un subálgebra
    de![](./ObjectReplacements/Object 1742){width="0.51cm"
    height="0.563cm"}. Los homomorfismos de las álgebras booleanas
    tienen propiedades interesantes que no veremos aquí.

    2.  Desarrollo de las propiedades generales del álgebra de Boole a
        partir de los axiomas de Huntington.

        1.  Teoremas de Idempotencia:

            1.  Para la suma:
                ![](./ObjectReplacements/Object 1782){width="3.644cm"
                height="0.563cm"}

> Prueba:

8.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1784){width="3.794cm"
                    height="0.467cm"}

>  Elemento neutro de la suma.

9.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1785){width="4.524cm"
                    height="0.506cm"}

>  Propiedad del complementario que produce 0.

10. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1786){width="5.35cm"
                    height="0.506cm"}

>  Distributiva izquierda de la suma respecto al producto.

11. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1787){width="4.503cm"
                    height="0.506cm"}

>  Propiedad del complementario que suma 1.

12. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1788){width="3.512cm"
                    height="0.467cm"}

                    Elemento neutro del producto.

        2.  Para el producto:
            ![](./ObjectReplacements/Object 1790){width="3.491cm"
            height="0.563cm"}

> Prueba:

13. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1791){width="3.628cm"
                    height="0.467cm"}

>  Elemento neutro de la suma.

14. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1792){width="4.524cm"
                    height="0.506cm"}

>  Propiedad del complementario que produce 0.

15. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1793){width="5.195cm"
                    height="0.506cm"}

>  Distributiva izquierda de la suma respecto al producto.

16. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1794){width="4.517cm"
                    height="0.506cm"}

>  Propiedad del complementario que suma 1.

17. 1.  1.  1.  1.  ![](./ObjectReplacements/Object 1789){width="3.358cm"
                    height="0.467cm"}

> Elemento neutro del producto.

18. 1.  1.  1.  Teoremas de Absorción:

                1.  Para
                    el![](./ObjectReplacements/Object 1807){width="0.411cm"
                    height="0.467cm"}:![](./ObjectReplacements/Object 1796){width="3.581cm"
                    height="0.563cm"}

> Prueba:

19. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1797){width="3.939cm"
                        height="0.467cm"}

>  Propiedad de
> sumar![](./ObjectReplacements/Object 546){width="0.411cm"
> height="0.467cm"}de un elemento al sumar con uno de sus
> complementarios.

20. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1798){width="4.493cm"
                        height="0.506cm"}

>  Elemento neutro de la multiplicación.

21. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1799){width="5.316cm"
                        height="0.506cm"}

>  Distributividad izquierda de la suma respecto al producto.

22. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1800){width="4.471cm"
                        height="0.506cm"}

>  Propiedad de sumar
> ![](./ObjectReplacements/Object 547){width="0.411cm"
> height="0.467cm"}de un elemento con cualquiera de sus complementarios.

23. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1801){width="3.48cm"
                        height="0.467cm"}

>  Elemento neutro del producto.

24. 1.  1.  1.  1.  Para
                    el![](./ObjectReplacements/Object 1802){width="0.423cm"
                    height="0.467cm"}:![](./ObjectReplacements/Object 1803){width="3.454cm"
                    height="0.563cm"}

> Prueba:

25. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1804){width="3.798cm"
                        height="0.467cm"}

> Propiedad de
> resultar![](./ObjectReplacements/Object 548){width="0.423cm"
> height="0.467cm"}de un elemento al multiplicar con uno de sus
> complementarios.

26. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1805){width="4.505cm"
                        height="0.506cm"}

> Elemento neutro de la suma.

27. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1806){width="5.175cm"
                        height="0.506cm"}

> Distributividad izquierda del producto respecto a la suma.

28. 1.  1.  1.  1.  1.  ![](./ObjectReplacements/Object 1808){width="4.498cm"
                        height="0.506cm"}

> Propiedad de
> resultar![](./ObjectReplacements/Object 549){width="0.423cm"
> height="0.467cm"}de un elemento al multiplicar con uno de sus
> complementarios.

29. 1.  1.  1.  1.  1.  $$\mspace{468mu} = {x \cdot 0}$$

> Elemento neutro de la suma.

30. 1.  1.  Condición necesaria y suficiente particular para que haya un
            solo elemento en el conjunto de
            Boole:![](./ObjectReplacements/Object 1809){width="3.487cm"
            height="0.73cm"}.

> Prueba:

31. 1.  1.  1.  ![](./ObjectReplacements/Object 1810){width="1.709cm"
                height="0.587cm"}

> Propiedad de absorción de la multiplicación con
> el![](./ObjectReplacements/Object 550){width="0.423cm"
> height="0.467cm"}

32. 1.  1.  1.  ![](./ObjectReplacements/Object 1811){width="1.693cm"
                height="0.587cm"}

> Sustituimos el![](./ObjectReplacements/Object 1746){width="0.423cm"
> height="0.467cm"}por
> el![](./ObjectReplacements/Object 1747){width="0.411cm"
> height="0.467cm"}gracias a la hipótesis.

33. 1.  1.  1.  ![](./ObjectReplacements/Object 1812){width="1.681cm"
                height="0.587cm"}

> Elemento neutro de la multiplicación,
> el![](./ObjectReplacements/Object 1748){width="0.411cm"
> height="0.467cm"}.

34. 1.  1.  1.  ![](./ObjectReplacements/Object 1813){width="0.796cm"
                height="0.467cm"}
            2.  ![](./ObjectReplacements/Object 1126){width="1.349cm"
                height="0.573cm"}

> Desde el punto (1) y (3), mediante la transitividad de la igualdad
> equivale.

35. 1.  1.  1.  ![](./ObjectReplacements/Object 1814){width="2.159cm"
                height="0.573cm"}

> Por la hipótesis.

36. 1.  1.  Condición necesaria y suficiente general para que haya un
            solo elemento en el conjunto de
            Boole:![](./ObjectReplacements/Object 1816){width="3.545cm"
            height="0.73cm"}.

            Prueba:

            1.  ![](./ObjectReplacements/Object 1818){width="4.274cm"
                height="0.467cm"}

                Axioma de
                sumar![](./ObjectReplacements/Object 1751){width="0.411cm"
                height="0.467cm"}un elemento y su complementario.

            2.  ![](./ObjectReplacements/Object 1819){width="4.281cm"
                height="0.467cm"}

                Particularización de la fórmula (2) usando la hipótesis.

            3.  ![](./ObjectReplacements/Object 1822){width="4.533cm"
                height="0.467cm"}

                Teorema de Idempotencia de la suma.

            4.  ![](./ObjectReplacements/Object 1749){width="4.509cm"
                height="0.467cm"}

                Fórmulas (1) y (3) aplicando la transitividad de la
                igualdad.

            5.  ![](./ObjectReplacements/Object 1820){width="4.217cm"
                height="0.467cm"}

                Axioma de
                multiplicar![](./ObjectReplacements/Object 1750){width="0.423cm"
                height="0.467cm"}un elemento y su complementario.

            6.  ![](./ObjectReplacements/Object 1821){width="4.21cm"
                height="0.467cm"}

                Particularización de la fórmula (5) con usando la
                hipótesis.

            7.  ![](./ObjectReplacements/Object 1815){width="4.533cm"
                height="0.467cm"}

                Teorema de Idempotencia del producto.

            8.  ![](./ObjectReplacements/Object 1823){width="4.479cm"
                height="0.467cm"}

                Fórmulas (5) y (7) aplicando la transitividad de la
                igualdad.

            9.  ![](./ObjectReplacements/Object 1825){width="4.531cm"
                height="0.563cm"}

                Fórmulas (4) y (8) y transitividad de la igualdad.

            10. ![](./ObjectReplacements/Object 1826){width="0.988cm"
                height="0.467cm"}

                Puesto que se da la hipótesis de (9) en (4) y (8).

            11. ![](./ObjectReplacements/Object 1827){width="2.159cm"
                height="0.573cm"}

                Por el teorema (4) (anterior).

        2.  Unicidad del
            complementario:![](./ObjectReplacements/Object 9){width="4.106cm"
            height="0.563cm"}

            Prueba:

            1.  ![](./ObjectReplacements/Object 545){width="4.881cm"
                height="0.563cm"}

                Axioma de
                sumar![](./ObjectReplacements/Object 1753){width="0.411cm"
                height="0.467cm"}cualquier elemento y su complementario.

            2.  ![](./ObjectReplacements/Object 1752){width="1.827cm"
                height="0.467cm"}

                Elemento neutro del producto.

            3.  ![](./ObjectReplacements/Object 1764){width="2.644cm"
                height="0.506cm"}

                Particularización de la fórmula (1) (axioma).

            4.  ![](./ObjectReplacements/Object 1765){width="3.334cm"
                height="0.506cm"}

                Distributiva izquierda del producto respecto de la suma.

            5.  ![](./ObjectReplacements/Object 1766){width="2.626cm"
                height="0.506cm"}

                Propiedad de los complementarios por la que
                multiplican![](./ObjectReplacements/Object 1776){width="0.423cm"
                height="0.467cm"}.

            6.  ![](./ObjectReplacements/Object 1767){width="1.82cm"
                height="0.467cm"}

                Propiedad del elemento neutro de la suma.

            7.  ![](./ObjectReplacements/Object 122){width="1.813cm"
                height="0.467cm"}

                Propiedad conmutativa del producto

            8.  ![](./ObjectReplacements/Object 1768){width="2.626cm"
                height="0.506cm"}

                Propiedad del elemento neutro de la suma.

            9.  ![](./ObjectReplacements/Object 1769){width="3.314cm"
                height="0.506cm"}

                Propiedad complementaria de
                ![](./ObjectReplacements/Object 1777){width="1.018cm"
                height="0.467cm"}que multiplican
                ![](./ObjectReplacements/Object 1778){width="0.423cm"
                height="0.467cm"}

            10. ![](./ObjectReplacements/Object 1770){width="2.644cm"
                height="0.506cm"}

                Distributiva izquierda del producto respecto de la suma.

            11. ![](./ObjectReplacements/Object 1771){width="1.769cm"
                height="0.467cm"}

                Propiedad complementaria de
                ![](./ObjectReplacements/Object 1779){width="1.018cm"
                height="0.467cm"}que suma
                ![](./ObjectReplacements/Object 1780){width="0.411cm"
                height="0.467cm"}

            12. ![](./ObjectReplacements/Object 1772){width="1.071cm"
                height="0.467cm"}

                Elemento neutro del producto

        3.  Definimos el elemento complementario de otro, aquel elemento
            de![](./ObjectReplacements/Object 1373){width="0.51cm"
            height="0.563cm"}que![](./ObjectReplacements/Object 1371){width="4.385cm"
            height="0.573cm"}, o dicho de otro
            modo,$$\forall{a \in}\qquad\exists!{\overline{a} \in}\mspace{72mu}{\left( {{a + \overline{a}} = 1} \right) \land \left( {{a \cdot \overline{a}} = 0} \right)}$$,
            y este elemento es único.

        4.  Complementación doble es
            identidad:$$\forall{x \in}{}{}{}{\overline{\overline{x}} = x}$$.

            Prueba:

            1.  ![](./ObjectReplacements/Object 123){width="8.216cm"
                height="0.573cm"}

                Versión del axioma de complementarios con el teorema (6)
                y la definición (7).

            2.  ![](./ObjectReplacements/Object 551){width="8.264cm"
                height="0.573cm"}

                Aplicamos particularización de (1)
                sustituyendo![](./ObjectReplacements/Object 1755){width="0.443cm"
                height="0.467cm"}por$$\overline{x}$$y![](./ObjectReplacements/Object 1774){width="0.443cm"
                height="0.467cm"}por![](./ObjectReplacements/Object 1773){width="0.443cm"
                height="0.467cm"}.

            3.  ![](./ObjectReplacements/Object 552){width="8.264cm"
                height="0.573cm"}

                Aplicamos los axiomas de conmutabilidad de la suma y el
                producto a las fórmulas de (2).

            4.  ![](./ObjectReplacements/Object 553){width="6.736cm"
                height="0.573cm"}

                De las fórmulas (1) y (3) y del axioma de
                complementarios se deriva lo anterior.

            5.  ![](./ObjectReplacements/Object 627){width="5.595cm"
                height="0.467cm"}

                Por el teorema (6) de unicidad del complementario.

        5.  Unicidad de los neutros:

            1.  El neutro para la suma es único
                ![](./ObjectReplacements/Object 14){width="6.773cm"
                height="0.681cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1781){width="3.612cm"
                    height="0.563cm"}

                    Hipótesis.

                2.  ![](./ObjectReplacements/Object 1783){width="3.56cm"
                    height="0.467cm"}

                    Particularización de (1) con el neutro de la suma.

                3.  ![](./ObjectReplacements/Object 1817){width="3.56cm"
                    height="0.467cm"}

                    Axioma de conmutabilidad para la suma.

                4.  ![](./ObjectReplacements/Object 1828){width="3.56cm"
                    height="0.467cm"}

                    Simetría de la igualdad.

                5.  ![](./ObjectReplacements/Object 1824){width="4.135cm"
                    height="0.467cm"}

                    Axioma del elemento neutro de la suma.

                6.  ![](./ObjectReplacements/Object 1829){width="4.152cm"
                    height="0.467cm"}

                    Transitividad de la igualdad en las fórmulas (4) y
                    (5).

            2.  El neutro para el producto es único
                ![](./ObjectReplacements/Object 1775){width="6.678cm"
                height="0.681cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1830){width="3.484cm"
                    height="0.563cm"}

                    Hipótesis.

                2.  ![](./ObjectReplacements/Object 1831){width="3.403cm"
                    height="0.467cm"}

                    Particularización de (1) con el neutro del producto.

                3.  ![](./ObjectReplacements/Object 1832){width="3.403cm"
                    height="0.467cm"}

                    Axioma de conmutatividad para el producto.

                4.  ![](./ObjectReplacements/Object 1833){width="3.403cm"
                    height="0.467cm"}

                    Simetría de la igualdad.

                5.  ![](./ObjectReplacements/Object 1834){width="4.015cm"
                    height="0.467cm"}

                    Axioma del elemento neutro del producto.

                6.  ![](./ObjectReplacements/Object 1835){width="4.165cm"
                    height="0.467cm"}

                    Transitividad de la igualdad en las fórmulas (4) y
                    (5).

        6.  Para los elementos
            ![](./ObjectReplacements/Object 1047){width="0.982cm"
            height="0.467cm"}:
            ![](./ObjectReplacements/Object 1048){width="2.124cm"
            height="0.467cm"}

            Prueba:

            1.  ![](./ObjectReplacements/Object 1757){width="1.489cm"
                height="0.467cm"}

                Axioma de elemento neutro de la suma.

            2.  ![](./ObjectReplacements/Object 1049){width="1.595cm"
                height="0.467cm"}

                Axioma de elemento neutro del producto.

        7.  Leyes de cancelación:

            1.  Para la suma:

                ![](./ObjectReplacements/Object 1003){width="9.881cm"
                height="0.658cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1060){width="3.496cm"
                    height="0.563cm"}

                    Hipótesis (1).

                2.  ![](./ObjectReplacements/Object 1061){width="3.498cm"
                    height="0.563cm"}

                    Hipótesis (2).

                3.  ![](./ObjectReplacements/Object 1062){width="4.789cm"
                    height="0.519cm"}

                    Por ser el producto aplicación, el multiplicar las
                    expresiones derechas de las igualdades entre sí y
                    las izquierdas entre sí, no altera la igualdad.

                4.  ![](./ObjectReplacements/Object 1063){width="3.219cm"
                    height="0.519cm"}

                    Por el axioma de distributividad de la suma respecto
                    al producto por la izquierda.

                5.  ![](./ObjectReplacements/Object 1064){width="2.074cm"
                    height="0.467cm"}

                    Por la propiedad de resultar
                    ![](./ObjectReplacements/Object 1836){width="0.423cm"
                    height="0.467cm"}la multiplicación de un elemento y
                    su complementario en el axioma de complementarios.

                6.  ![](./ObjectReplacements/Object 1005){width="1.05cm"
                    height="0.467cm"}

                    Por el axioma del elemento neutro de la suma.

            2.  Para el
                producto:![](./ObjectReplacements/Object 1026){width="9.266cm"
                height="0.658cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1837){width="3.187cm"
                    height="0.563cm"}

                    Hipótesis (1).

                2.  ![](./ObjectReplacements/Object 1838){width="3.191cm"
                    height="0.563cm"}

                    Hipótesis (2).

                3.  ![](./ObjectReplacements/Object 1007){width="4.48cm"
                    height="0.519cm"}

                    Por ser la suma aplicación, el sumar las expresiones
                    derechas de las igualdades entre sí y las izquierdas
                    entre sí, no altera la igualdad.

                4.  ![](./ObjectReplacements/Object 1008){width="3.219cm"
                    height="0.519cm"}

                    Por el axioma de distributividad del producto
                    respecto de la suma por la izquierda.

                5.  ![](./ObjectReplacements/Object 1839){width="1.744cm"
                    height="0.467cm"}

                    Por la propiedad de resultar
                    ![](./ObjectReplacements/Object 1842){width="0.411cm"
                    height="0.467cm"}la suma de un elemento y su
                    complementario en el axioma de complementarios.

                6.  ![](./ObjectReplacements/Object 1843){width="1.05cm"
                    height="0.467cm"}

                    Por el axioma del elemento neutro de la
                    multiplicación.

        8.  Propiedades de simplificación (para retículos en general):

            1.  ![](./ObjectReplacements/Object 12){width="4.173cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 133){width="2cm"
                    height="0.506cm"}

                2.  ![](./ObjectReplacements/Object 41){width="4.48cm"
                    height="0.506cm"}

                    Por ser
                    el![](./ObjectReplacements/Object 86){width="0.411cm"
                    height="0.467cm"}el elemento neutro del producto
                    (Axioma).

                3.  ![](./ObjectReplacements/Object 42){width="3.81cm"
                    height="0.506cm"}

                    Por el axioma de distributividad del producto
                    respecto de la suma por la izquierda.

                4.  ![](./ObjectReplacements/Object 84){width="2.967cm"
                    height="0.467cm"}

                    Por ser
                    el![](./ObjectReplacements/Object 87){width="0.411cm"
                    height="0.467cm"}elemento absorbente en la suma
                    \[Teorema (2.1)\].

                5.  $$\mspace{306mu}{= x}$$

                    Por ser
                    el![](./ObjectReplacements/Object 124){width="0.411cm"
                    height="0.467cm"}el elemento neutro del producto
                    (Axioma).

            2.  ![](./ObjectReplacements/Object 13){width="4.173cm"
                height="0.577cm"}

                1.  Prueba:

                2.  ![](./ObjectReplacements/Object 128){width="2cm"
                    height="0.506cm"}

                3.  ![](./ObjectReplacements/Object 130){width="4.648cm"
                    height="0.506cm"}

                    Por ser
                    el![](./ObjectReplacements/Object 131){width="0.423cm"
                    height="0.467cm"}el elemento neutro de la suma
                    (Axioma).

                4.  ![](./ObjectReplacements/Object 132){width="3.822cm"
                    height="0.506cm"}

                    Por el axioma de distributividad de la suma respecto
                    del producto por la izquierda.

                5.  ![](./ObjectReplacements/Object 134){width="2.967cm"
                    height="0.467cm"}

                    Por ser
                    el![](./ObjectReplacements/Object 241){width="0.423cm"
                    height="0.467cm"}elemento absorbente en el producto
                    \[Teorema (2.2)\].

                6.  ![](./ObjectReplacements/Object 242){width="2.267cm"
                    height="0.467cm"}

                    Por ser
                    el![](./ObjectReplacements/Object 127){width="0.423cm"
                    height="0.467cm"}el elemento neutro de la suma
                    (Axioma).

        9.  Una propiedad muy general (para retículos no sólo para
            álgebras de Boole):

            1.  ![](./ObjectReplacements/Object 203){width="5.83cm"
                height="0.577cm"}

                Prueba:

                1.  1.  ![](./ObjectReplacements/Object 125){width="1.452cm"
                        height="0.467cm"}

                        Hipótesis.

                    2.  ![](./ObjectReplacements/Object 244){width="1.416cm"
                        height="0.467cm"}

                        Verdad universal para la igualdad.

                    3.  ![](./ObjectReplacements/Object 245){width="2.828cm"
                        height="0.506cm"}

                        Como la suma es una aplicación, al sumar las
                        expresiones izquierdas entre si, e idénticamente
                        con las derechas, la igualdad se mantiene.

                    4.  ![](./ObjectReplacements/Object 246){width="2.828cm"
                        height="0.506cm"}

                        Propiedad conmutativa del producto (axioma).

                    5.  ![](./ObjectReplacements/Object 247){width="1.589cm"
                        height="0.467cm"}

                        Propiedad de simplificación del teorema anterior
                        (11.2).

                    6.  ![](./ObjectReplacements/Object 248){width="1.589cm"
                        height="0.467cm"}

                        Simetría de la igualdad.

                    7.  ![](./ObjectReplacements/Object 249){width="1.589cm"
                        height="0.467cm"}

                        Propiedad conmutativa de la suma (axioma).

                    8.  ![](./ObjectReplacements/Object 126){width="3.856cm"
                        height="0.506cm"}

                        De (1) hemos derivado (7).

                    9.  ![](./ObjectReplacements/Object 555){width="1.572cm"
                        height="0.467cm"}

                        Hipótesis.

                    10. ![](./ObjectReplacements/Object 556){width="1.453cm"
                        height="0.467cm"}

                        Verdad universal de la igualdad.

                    11. ![](./ObjectReplacements/Object 557){width="2.693cm"
                        height="0.506cm"}

                        Como el producto es aplicación, el multiplicar
                        los términos izquierdos de las igualdades (9)
                        y (10) entre sí y los derechos de (9) y (10)
                        idénticamente, se mantiene la igualdad.

                    12. ![](./ObjectReplacements/Object 558){width="1.455cm"
                        height="0.467cm"}

                        Teorema de simplificación inmediatamente
                        anterior (11.1).

                    13. ![](./ObjectReplacements/Object 559){width="1.455cm"
                        height="0.467cm"}

                        Por la simetría de la igualdad.

                    14. ![](./ObjectReplacements/Object 243){width="3.856cm"
                        height="0.506cm"}

                        De (9) hemos derivado (13).

                    15. ![](./ObjectReplacements/Object 628){width="8.675cm"
                        height="1.09cm"}

                        \(11\) y (14) significan exactamente la
                        definición del "si y solo si".

        10. Otra propiedad de simplificación (Shannon):

            1.  ![](./ObjectReplacements/Object 15){width="5.022cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 250){width="1.905cm"
                    height="0.467cm"}

                    Por el axioma de elemento neutro de la suma.

                2.  ![](./ObjectReplacements/Object 554){width="2.686cm"
                    height="0.506cm"}

                    Por el axioma de complementarios en su afirmación
                    del producto de complementarios.

                3.  ![](./ObjectReplacements/Object 560){width="3.171cm"
                    height="0.506cm"}

                    Por la distributividad de la suma respecto al
                    producto por la izquierda.

            2.  ![](./ObjectReplacements/Object 16){width="4.867cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 135){width="1.905cm"
                    height="0.467cm"}

                    Por el axioma de elemento neutro de la suma.

                2.  ![](./ObjectReplacements/Object 136){width="2.686cm"
                    height="0.506cm"}

                    Por el axioma de complementarios en su afirmación
                    del producto de complementarios.

                3.  ![](./ObjectReplacements/Object 561){width="3.171cm"
                    height="0.506cm"}

                    Por la distributividad de la suma respecto al
                    producto por la izquierda.

        11. Otra propiedad de simplificación más:

            1.  Para la suma respecto del producto:
                ![](./ObjectReplacements/Object 28){width="4.731cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 137){width="4.618cm"
                    height="0.506cm"}

                    Por el axioma de distributividad de la suma respecto
                    al producto.

                2.  ![](./ObjectReplacements/Object 1591){width="3.81cm"
                    height="0.506cm"}

                    Por la propiedad de sumar 1 los complementarios en
                    el axioma de complementarios.

                3.  ![](./ObjectReplacements/Object 11){width="2.812cm"
                    height="0.467cm"}

                    Por el axioma del elemento neutro de la suma.

            2.  Para el producto respecto de la
                suma:![](./ObjectReplacements/Object 138){width="4.731cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1593){width="4.463cm"
                    height="0.506cm"}

                    Por el axioma de distributividad del producto
                    respecto de la suma.

                2.  ![](./ObjectReplacements/Object 1594){width="3.822cm"
                    height="0.506cm"}

                    Por la propiedad de multiplicar
                    ![](./ObjectReplacements/Object 1595){width="0.423cm"
                    height="0.467cm"} los complementarios en el axioma
                    de complementarios.

                3.  ![](./ObjectReplacements/Object 1592){width="2.656cm"
                    height="0.467cm"}

                    Por el axioma del elemento neutro del producto.

        12. Algunos lemas técnicos pre-asociativos útiles:

            1.  Asociatividad cuando dos variables se repiten:

                1.  Para la
                    suma:![](./ObjectReplacements/Object 118){width="6.565cm"
                    height="0.577cm"}

                    Prueba:

                    1.  ![](./ObjectReplacements/Object 129){width="2.865cm"
                        height="0.506cm"}

                        Ponemos una expresión izquierda de una igualdad.

                    2.  ![](./ObjectReplacements/Object 1596){width="5.526cm"
                        height="0.506cm"}

                        Por el axioma de conmutatividad del producto.

                    3.  ![](./ObjectReplacements/Object 1853){width="6.216cm"
                        height="0.506cm"}

                        Distributividad del producto respecto a la suma
                        por la izquierda.

                    4.  ![](./ObjectReplacements/Object 1758){width="6.906cm"
                        height="0.506cm"}

                        Distributividad del producto respecto a la suma
                        por la izquierda.

                    5.  ![](./ObjectReplacements/Object 1759){width="6.216cm"
                        height="0.506cm"}

                        Por el teorema de idempotencia del producto.

                    6.  ![](./ObjectReplacements/Object 1854){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad de la suma.

                    7.  ![](./ObjectReplacements/Object 1855){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad de la suma.

                    8.  ![](./ObjectReplacements/Object 1858){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad de la suma.

                    9.  ![](./ObjectReplacements/Object 1859){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad del producto.

                    10. ![](./ObjectReplacements/Object 1840){width="4.701cm"
                        height="0.506cm"}

                        Por el teorema de simplificación de la suma
                        respecto al producto.

                    11. ![](./ObjectReplacements/Object 1856){width="4.701cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad de la suma.

                    12. ![](./ObjectReplacements/Object 1857){width="4.701cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad del producto.

                    13. ![](./ObjectReplacements/Object 1841){width="6.316cm"
                        height="0.467cm"}

                        Por el teorema de simplificación de la suma
                        respecto al producto.

                    14. ![](./ObjectReplacements/Object 202){width="3.129cm"
                        height="0.506cm"}

                        Fórmulas (1) y (13) por la transitividad de la
                        igualdad.

                    15. ![](./ObjectReplacements/Object 564){width="2.829cm"
                        height="0.506cm"}

                        Ponemos una expresión izquierda de una igualdad.

                    16. ![](./ObjectReplacements/Object 565){width="6.177cm"
                        height="0.506cm"}

                        Por el axioma de distributividad del producto
                        respecto de la suma.

                    17. ![](./ObjectReplacements/Object 1848){width="6.177cm"
                        height="0.506cm"}

                        Por el axioma de conmutatividad de la suma.

                    18. ![](./ObjectReplacements/Object 1844){width="4.664cm"
                        height="0.506cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    19. ![](./ObjectReplacements/Object 1847){width="6.339cm"
                        height="0.467cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    20. ![](./ObjectReplacements/Object 10){width="3.06cm"
                        height="0.506cm"}

                        Fórmulas (15) y (19) y transitividad de la
                        igualdad.

                    21. ![](./ObjectReplacements/Object 567){width="1.385cm"
                        height="0.467cm"}

                    22. ![](./ObjectReplacements/Object 1860){width="7.227cm"
                        height="0.506cm"}

                        Fórmulas (14) y (20) y simetría de la igualdad.
                        De otro lado está que al ser la suma una
                        aplicación, se puede sumar lado derecho de una
                        igualdad con el lado derecho de otra y e
                        igualmente sus lados izquierdos, y el resultado
                        sigue siendo una igualdad.

                    23. ![](./ObjectReplacements/Object 1861){width="7.227cm"
                        height="0.506cm"}

                        Axioma de conmutatividad del producto.

                    24. ![](./ObjectReplacements/Object 568){width="4.898cm"
                        height="0.506cm"}

                        Por el axioma de distributividad por la
                        izquierda del producto respecto de la suma.

                    25. ![](./ObjectReplacements/Object 1862){width="6.521cm"
                        height="0.563cm"}

                        Por el teorema de idempotencia de la suma.

                    26. ![](./ObjectReplacements/Object 566){width="6.482cm"
                        height="0.563cm"}

                        Por el axioma de conmutabilidad del producto.

                    27. ![](./ObjectReplacements/Object 1863){width="6.482cm"
                        height="0.563cm"}

                        Por el axioma de conmutatividad de la suma.

                    28. ![](./ObjectReplacements/Object 569){width="4.898cm"
                        height="0.506cm"}

                        Por el axioma de distributividad de la suma
                        respecto al producto.

                    29. ![](./ObjectReplacements/Object 1846){width="4.898cm"
                        height="0.506cm"}

                        Axioma de conmutatividad del producto.

                    30. ![](./ObjectReplacements/Object 1864){width="4.898cm"
                        height="0.506cm"}

                        Axioma de conmutatividad de la suma.

                    31. ![](./ObjectReplacements/Object 1849){width="3.39cm"
                        height="0.506cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    32. ![](./ObjectReplacements/Object 570){width="7.922cm"
                        height="0.506cm"}

                        Por el axioma de conmutatividad de la suma.

                    33. ![](./ObjectReplacements/Object 1845){width="2.979cm"
                        height="0.506cm"}

                        De las fórmulas (21) y (32) y la transitividad
                        de la igualdad.

                    34. ![](./ObjectReplacements/Object 1865){width="1.863cm"
                        height="0.519cm"}

                        Teorema de idempotencia de la suma.

                    35. ![](./ObjectReplacements/Object 1866){width="1.076cm"
                        height="0.467cm"}

                        Propiedad fundamental de la igualdad.

                    36. ![](./ObjectReplacements/Object 1867){width="2.983cm"
                        height="0.506cm"}

                        Al ser la suma una aplicación y sumar los lados
                        derechos de las igualdades y los lados
                        izquierdos permanece la igualdad.

                    37. ![](./ObjectReplacements/Object 212){width="4.951cm"
                        height="0.506cm"}

                        Concatenación de las fórmulas (36) y (33) por
                        transitividad de la igualdad.

                2.  Para el
                    producto:![](./ObjectReplacements/Object 119){width="6.068cm"
                    height="0.577cm"}

                    Prueba:

                    1.  ![](./ObjectReplacements/Object 88){width="2.709cm"
                        height="0.506cm"}

                        Ponemos una expresión izquierda bien formada de
                        una igualdad.

                    2.  ![](./ObjectReplacements/Object 211){width="5.373cm"
                        height="0.506cm"}

                        Por el axioma de conmutatividad de la suma.

                    3.  ![](./ObjectReplacements/Object 213){width="6.216cm"
                        height="0.506cm"}

                        Distributividad de la suma respecto al producto
                        por la izquierda.

                    4.  ![](./ObjectReplacements/Object 214){width="7.061cm"
                        height="0.506cm"}

                        Distributividad de la suma respecto al producto
                        por la izquierda.

                    5.  ![](./ObjectReplacements/Object 215){width="6.216cm"
                        height="0.506cm"}

                        Por el teorema de idempotencia de la suma.

                    6.  ![](./ObjectReplacements/Object 571){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad del producto.

                    7.  ![](./ObjectReplacements/Object 572){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad del producto.

                    8.  ![](./ObjectReplacements/Object 573){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad del producto.

                    9.  ![](./ObjectReplacements/Object 574){width="6.216cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad de la suma.

                    10. ![](./ObjectReplacements/Object 575){width="4.701cm"
                        height="0.506cm"}

                        Por el teorema de simplificación del producto
                        respecto a la suma.

                    11. ![](./ObjectReplacements/Object 576){width="4.701cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad del producto.

                    12. ![](./ObjectReplacements/Object 1850){width="4.701cm"
                        height="0.506cm"}

                        Por axioma de conmutatividad de la suma.

                    13. ![](./ObjectReplacements/Object 1868){width="6.316cm"
                        height="0.467cm"}

                        Por el teorema de simplificación del producto
                        respecto a la suma.

                    14. ![](./ObjectReplacements/Object 1869){width="2.976cm"
                        height="0.506cm"}

                        Fórmulas (1) y (13) por la transitividad de la
                        igualdad.

                    15. ![](./ObjectReplacements/Object 1870){width="2.676cm"
                        height="0.506cm"}

                        Ponemos una expresión izquierda de una igualdad.

                    16. ![](./ObjectReplacements/Object 1871){width="6.177cm"
                        height="0.506cm"}

                        Por el axioma de distributividad de la suma
                        respecto del producto.

                    17. ![](./ObjectReplacements/Object 1872){width="6.177cm"
                        height="0.506cm"}

                        Por el axioma de conmutatividad del producto.

                    18. ![](./ObjectReplacements/Object 1873){width="4.664cm"
                        height="0.506cm"}

                        Teorema de simplificación de la suma respecto
                        del producto.

                    19. ![](./ObjectReplacements/Object 1874){width="6.339cm"
                        height="0.467cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    20. $${{({x \cdot {({x \cdot y})}})} + x} = x$$

                        Fórmulas (15) y (19) y transitividad de la
                        igualdad.

                    21. ![](./ObjectReplacements/Object 1876){width="1.229cm"
                        height="0.467cm"}

                        Expresión bien formada en la parte izquierda de
                        la igualdad.

                    22. ![](./ObjectReplacements/Object 1877){width="6.765cm"
                        height="0.506cm"}

                        Fórmulas (14) y (20) y simetría de la igualdad.
                        De otro lado está que al ser el producto una
                        aplicación, se puede multiplicar lado derecho de
                        una igualdad con el lado derecho de otra y e
                        igualmente sus lados izquierdos, y el resultado
                        sigue siendo una igualdad.

                    23. ![](./ObjectReplacements/Object 1878){width="6.765cm"
                        height="0.506cm"}

                        Axioma de conmutatividad de la suma.

                    24. ![](./ObjectReplacements/Object 1879){width="4.59cm"
                        height="0.506cm"}

                        Por el axioma de distributividad por la
                        izquierda de la suma respecto del producto.

                    25. ![](./ObjectReplacements/Object 1880){width="5.906cm"
                        height="0.563cm"}

                        Por el teorema de idempotencia del producto.

                    26. ![](./ObjectReplacements/Object 1881){width="5.867cm"
                        height="0.563cm"}

                        Por el axioma de conmutabilidad de la suma.

                    27. ![](./ObjectReplacements/Object 1882){width="5.867cm"
                        height="0.563cm"}

                        Por el axioma de conmutatividad del producto.

                    28. ![](./ObjectReplacements/Object 1883){width="4.59cm"
                        height="0.506cm"}

                        Por el axioma de distributividad del producto
                        respecto a la suma.

                    29. ![](./ObjectReplacements/Object 1884){width="4.59cm"
                        height="0.506cm"}

                        Axioma de conmutatividad de la suma.

                    30. ![](./ObjectReplacements/Object 1885){width="4.59cm"
                        height="0.506cm"}

                        Axioma de conmutatividad del producto.

                    31. ![](./ObjectReplacements/Object 1886){width="3.082cm"
                        height="0.506cm"}

                        Teorema de simplificación de la suma respecto
                        del producto.

                    32. ![](./ObjectReplacements/Object 1887){width="7.615cm"
                        height="0.506cm"}

                        Por el axioma de conmutatividad del producto.

                    33. ![](./ObjectReplacements/Object 1888){width="2.519cm"
                        height="0.506cm"}

                        De las fórmulas (21) y (32) y la transitividad
                        de la igualdad.

                    34. ![](./ObjectReplacements/Object 1889){width="1.707cm"
                        height="0.519cm"}

                        Teorema de idempotencia del producto.

                    35. ![](./ObjectReplacements/Object 1890){width="1.076cm"
                        height="0.467cm"}

                        Propiedad fundamental de la igualdad.

                    36. ![](./ObjectReplacements/Object 1891){width="2.521cm"
                        height="0.506cm"}

                        Al ser el producto una aplicación y multiplicar
                        los lados derechos de las igualdades y los lados
                        izquierdos permanece la igualdad.

                    37. ![](./ObjectReplacements/Object 1892){width="4.182cm"
                        height="0.506cm"}

                        Concatenación de las fórmulas (36) y (33) por
                        transitividad de la igualdad.

            2.  Asociatividad cuando una de las tres variables es la
                complementaria de otra:

                1.  Para la
                    suma:![](./ObjectReplacements/Object 120){width="4.322cm"
                    height="0.506cm"}

                    Prueba:

                    1.  ![](./ObjectReplacements/Object 577){width="2.831cm"
                        height="0.506cm"}

                        Expresión derecha de la igualdad.

                    2.  ![](./ObjectReplacements/Object 1923){width="5.592cm"
                        height="0.506cm"}

                        Axioma de conmutatividad del producto.

                    3.  ![](./ObjectReplacements/Object 1893){width="6.262cm"
                        height="0.506cm"}

                        Axioma de distributividad del producto del
                        producto respecto de la suma.

                    4.  ![](./ObjectReplacements/Object 1914){width="5.572cm"
                        height="0.506cm"}

                        Propiedad de
                        multiplicar![](./ObjectReplacements/Object 1925){width="0.423cm"
                        height="0.467cm"}los complementarios por el
                        axioma de complementarios.

                    5.  ![](./ObjectReplacements/Object 1915){width="4.766cm"
                        height="0.506cm"}

                        Axioma de elemento neutro de la suma.

                    6.  ![](./ObjectReplacements/Object 1924){width="4.766cm"
                        height="0.506cm"}

                        Axioma de conmutatividad del producto.

                    7.  ![](./ObjectReplacements/Object 1916){width="4.766cm"
                        height="0.506cm"}

                        Axioma de conmutatividad de la suma.

                    8.  ![](./ObjectReplacements/Object 1894){width="6.634cm"
                        height="0.467cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    9.  ![](./ObjectReplacements/Object 1895){width="2.831cm"
                        height="0.506cm"}

                        Transitividad de la igualdad desde la
                        fórmula (1) a la (8).

                    10. ![](./ObjectReplacements/Object 578){width="2.833cm"
                        height="0.506cm"}

                        Expresión derecha de la igualdad.

                    11. ![](./ObjectReplacements/Object 1917){width="5.48cm"
                        height="0.506cm"}

                        Axioma de conmutatividad de la suma.

                    12. ![](./ObjectReplacements/Object 1918){width="6.623cm"
                        height="0.467cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    13. ![](./ObjectReplacements/Object 1898){width="3.106cm"
                        height="0.506cm"}

                        Transitividad de la igualdad des la fórmula (10)
                        hasta la (12).

                    14. ![](./ObjectReplacements/Object 580){width="0.764cm"
                        height="0.467cm"}

                        Expresión bien formada como lado izquierdo de la
                        igualdad.

                    15. ![](./ObjectReplacements/Object 1930){width="3.046cm"
                        height="0.467cm"}

                        Propiedad de sumar
                        ![](./ObjectReplacements/Object 1926){width="0.411cm"
                        height="0.467cm"}los complementarios en el
                        axioma de existencia de complementarios.

                    16. ![](./ObjectReplacements/Object 579){width="7.504cm"
                        height="0.631cm"}

                        Sustitución de los lados derechos de las
                        igualdades (9) y (13) por sus lados izquierdos.

                    17. ![](./ObjectReplacements/Object 581){width="5.369cm"
                        height="0.506cm"}

                        Axioma de distributividad izquierda del producto
                        respecto de la suma.

                    18. ![](./ObjectReplacements/Object 1899){width="4.551cm"
                        height="0.506cm"}

                        Propiedad de
                        sumar![](./ObjectReplacements/Object 1927){width="0.411cm"
                        height="0.467cm"}los complementarios del axioma
                        de existencia de complementario.

                    19. ![](./ObjectReplacements/Object 1900){width="7.939cm"
                        height="0.506cm"}

                        Axioma de elemento neutro del producto.

                    20. ![](./ObjectReplacements/Object 1896){width="2.395cm"
                        height="0.506cm"}

                        Transitividad de la igualdad desde la
                        fórmula (14) hasta la (19).

                    21. ![](./ObjectReplacements/Object 582){width="0.764cm"
                        height="0.467cm"}

                        Expresión bien formada en lado izquierdo de la
                        igualdad.

                    22. ![](./ObjectReplacements/Object 1929){width="1.967cm"
                        height="0.467cm"}

                        Teorema del elemento absorbente de la suma.

                    23. ![](./ObjectReplacements/Object 583){width="7.927cm"
                        height="0.506cm"}

                        Propiedad de
                        sumar![](./ObjectReplacements/Object 1928){width="0.411cm"
                        height="0.467cm"}los complementarios en el
                        axioma de existencias de complementarios.

                    24. ![](./ObjectReplacements/Object 584){width="2.365cm"
                        height="0.506cm"}

                        Transitividad de la igualdad desde la
                        fórmula (21) hasta la (23).

                    25. ![](./ObjectReplacements/Object 1902){width="4.355cm"
                        height="0.506cm"}

                        Transitividad de la igualdad y simetría de la
                        misma en las fórmulas (20) y (24).

                2.  Para el
                    producto:![](./ObjectReplacements/Object 121){width="3.717cm"
                    height="0.506cm"}

                    Prueba:

                    1.  ![](./ObjectReplacements/Object 585){width="2.678cm"
                        height="0.506cm"}

                        Expresión bien formada como lado izquierdo de la
                        igualdad.

                    2.  ![](./ObjectReplacements/Object 1931){width="5.073cm"
                        height="0.506cm"}

                        Axioma de conmutatividad de la suma.

                    3.  ![](./ObjectReplacements/Object 586){width="5.837cm"
                        height="0.575cm"}

                        Axioma de distributividad izquierda de la suma
                        respecto al producto.

                    4.  ![](./ObjectReplacements/Object 1912){width="5.837cm"
                        height="0.575cm"}

                        Axioma de conmutatividad del producto.

                    5.  ![](./ObjectReplacements/Object 1913){width="5.027cm"
                        height="0.575cm"}

                        Propiedad de
                        sumar![](./ObjectReplacements/Object 1933){width="0.411cm"
                        height="0.467cm"}los complementarios del axioma
                        de existencia de complementarios.

                    6.  ![](./ObjectReplacements/Object 1932){width="4.424cm"
                        height="0.519cm"}

                        Axioma de elemento neutro del producto.

                    7.  ![](./ObjectReplacements/Object 1901){width="4.424cm"
                        height="0.519cm"}

                        Axioma de conmutatividad de la suma.

                    8.  ![](./ObjectReplacements/Object 1919){width="4.424cm"
                        height="0.519cm"}

                        Axioma de conmutatividad del producto.

                    9.  ![](./ObjectReplacements/Object 587){width="4.955cm"
                        height="0.467cm"}

                        Teorema de simplificación de la suma respecto al
                        producto.

                    10. ![](./ObjectReplacements/Object 588){width="2.951cm"
                        height="0.506cm"}

                        Transitividad de la igualdad desde la
                        fórmula (1) a la (9).

                    11. ![](./ObjectReplacements/Object 589){width="2.586cm"
                        height="0.575cm"}

                        Expresión bien formada como lado izquierdo de la
                        igualdad.

                    12. ![](./ObjectReplacements/Object 1920){width="5.59cm"
                        height="0.575cm"}

                        Axioma de distributividad izquierda de la suma
                        respecto al producto.

                    13. ![](./ObjectReplacements/Object 590){width="4.822cm"
                        height="0.575cm"}

                        Teorema de idempotencia de la suma.

                    14. ![](./ObjectReplacements/Object 1921){width="4.822cm"
                        height="0.575cm"}

                        Axioma de conmutatividad del producto.

                    15. ![](./ObjectReplacements/Object 591){width="5.877cm"
                        height="0.467cm"}

                        Teorema de simplificación del producto respecto
                        de la suma.

                    16. ![](./ObjectReplacements/Object 1903){width="2.861cm"
                        height="0.575cm"}

                        Transitividad de la igualdad desde la
                        fórmula (11) hasta la (15).

                    17. ![](./ObjectReplacements/Object 1904){width="0.774cm"
                        height="0.467cm"}

                        Expresión bien formada como lado izquierdo de la
                        igualdad.

                    18. ![](./ObjectReplacements/Object 1934){width="2.829cm"
                        height="0.467cm"}

                        Propiedad de multiplicar 0 los complementarios
                        del axioma de existencia de complementarios.

                    19. ![](./ObjectReplacements/Object 1905){width="6.959cm"
                        height="0.631cm"}

                        Sustitución de los lados izquierdos de las
                        fórmulas (10) y (16) por sus lados derechos.

                    20. ![](./ObjectReplacements/Object 1906){width="4.978cm"
                        height="0.506cm"}

                        Axioma de distributividad izquierda de la suma
                        respecto al producto.

                    21. ![](./ObjectReplacements/Object 1907){width="4.327cm"
                        height="0.506cm"}

                        Propiedad de
                        multiplicar![](./ObjectReplacements/Object 1936){width="0.423cm"
                        height="0.467cm"}los complementarios del axioma
                        de existencia de complementarios.

                    22. ![](./ObjectReplacements/Object 1908){width="6.175cm"
                        height="0.506cm"}

                        Axioma de elemento neutro de la suma.

                    23. ![](./ObjectReplacements/Object 1897){width="2.101cm"
                        height="0.506cm"}

                        Transitividad de la igualdad desde la
                        fórmula (17) hasta la (22).

                    24. ![](./ObjectReplacements/Object 1909){width="0.774cm"
                        height="0.467cm"}

                        Expresión bien formada en lado izquierdo de la
                        igualdad.

                    25. ![](./ObjectReplacements/Object 1935){width="2.746cm"
                        height="0.467cm"}

                        Teorema de elemento absorbente de la
                        multiplicación.

                    26. ![](./ObjectReplacements/Object 1910){width="3.436cm"
                        height="0.506cm"}

                        Propiedad de
                        multiplicar![](./ObjectReplacements/Object 1937){width="0.423cm"
                        height="0.467cm"}los complementarios del axioma
                        de existencia de complementarios.

                    27. ![](./ObjectReplacements/Object 1922){width="4.763cm"
                        height="0.506cm"}

                        Axioma de conmutatividad del producto.

                    28. ![](./ObjectReplacements/Object 1911){width="2.069cm"
                        height="0.506cm"}

                        Transitividad de la igualdad desde la
                        fórmula (24) a la (27).

                    29. ![](./ObjectReplacements/Object 139){width="3.752cm"
                        height="0.506cm"}

                        Transitividad y simetría de la igualdad con las
                        fórmulas (23) y (28).

        13. Leyes de Morgan:

            1.  De la suma en
                producto:![](./ObjectReplacements/Object 23){width="3.918cm"
                height="0.563cm"}

                Prueba:

                Informal:

                ![](./ObjectReplacements/Object 140){width="11.723cm"
                height="0.506cm"}

                ![](./ObjectReplacements/Object 141){width="11.998cm"
                height="0.506cm"}

                Formal:

                1.  ![](./ObjectReplacements/Object 1938){width="2.713cm"
                    height="0.506cm"}

                    Expresión bien formada en lado izquierdo de la
                    igualdad.

                2.  ![](./ObjectReplacements/Object 1955){width="5.276cm"
                    height="0.506cm"}

                    Axioma de conmutatividad del producto.

                3.  ![](./ObjectReplacements/Object 1956){width="6.632cm"
                    height="0.506cm"}

                    Axioma de distributividad izquierda del producto
                    respecto de la suma.

                4.  ![](./ObjectReplacements/Object 1939){width="6.632cm"
                    height="0.506cm"}

                    Axioma de conmutatividad del producto.

                5.  ![](./ObjectReplacements/Object 1940){width="6.63cm"
                    height="0.506cm"}

                    Lema de asociatividad del producto cuando uno de los
                    tres operandos es negado de otro.

                6.  ![](./ObjectReplacements/Object 1976){width="5.96cm"
                    height="0.506cm"}

                    Propiedad de
                    multiplicar![](./ObjectReplacements/Object 1942){width="0.423cm"
                    height="0.467cm"}los complementarios del axioma de
                    existencia de complementarios.

                7.  ![](./ObjectReplacements/Object 1977){width="5.265cm"
                    height="0.506cm"}

                    Teorema de elemento absorbente del producto.

                8.  ![](./ObjectReplacements/Object 1941){width="4.461cm"
                    height="0.506cm"}

                    Axioma del elemento neutro de la suma.

                9.  ![](./ObjectReplacements/Object 1978){width="4.463cm"
                    height="0.506cm"}

                    Teorema de la doble negación.

                10. ![](./ObjectReplacements/Object 1943){width="6.865cm"
                    height="0.467cm"}

                    Lema de asociatividad del producto cuando uno de los
                    tres operandos es negado de otro.

                11. ![](./ObjectReplacements/Object 1944){width="2.976cm"
                    height="0.506cm"}

                    Transitividad de la igualdad desde la fórmula (1)
                    hasta la (10).

                12. ![](./ObjectReplacements/Object 1945){width="2.866cm"
                    height="0.506cm"}

                    Expresión bien formada en lado izquierdo de la
                    igualdad.

                13. ![](./ObjectReplacements/Object 1946){width="7.093cm"
                    height="0.506cm"}

                    Axioma de distributividad izquierda de la suma
                    respecto al producto.

                14. ![](./ObjectReplacements/Object 1947){width="7.093cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                15. ![](./ObjectReplacements/Object 1979){width="7.093cm"
                    height="0.506cm"}

                    Teorema de la doble negación.

                16. ![](./ObjectReplacements/Object 1952){width="7.093cm"
                    height="0.506cm"}

                    Axioma de asociatividad del producto cuando uno de
                    los elementos es negado de otro.

                17. ![](./ObjectReplacements/Object 1953){width="5.352cm"
                    height="0.506cm"}

                    Propiedad de sumar 1 los complementarios del axioma
                    de existencia de complementarios.

                18. ![](./ObjectReplacements/Object 1948){width="5.352cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                19. ![](./ObjectReplacements/Object 1949){width="3.69cm"
                    height="0.467cm"}

                    Teorema del elemento absorbente de la suma.

                20. ![](./ObjectReplacements/Object 1950){width="6.854cm"
                    height="0.467cm"}

                    Axioma del elemento neutro del producto.

                21. ![](./ObjectReplacements/Object 1951){width="3.119cm"
                    height="0.506cm"}

                    Transitividad de la igualdad desde la fórmula (12)
                    hasta la (21).

                22. ![](./ObjectReplacements/Object 1954){width="6.653cm"
                    height="0.559cm"}

                    Fórmulas (11) y (21).

                23. ![](./ObjectReplacements/Object 1981){width="2.598cm"
                    height="0.63cm"}

                    Implicado por el axioma de existencia de
                    complementarios.

                24. ![](./ObjectReplacements/Object 1980){width="2.619cm"
                    height="0.563cm"}

                    Por el teorema de unicidad del complementario.

            2.  Del producto en
                suma:![](./ObjectReplacements/Object 24){width="3.918cm"
                height="0.563cm"}

                Prueba:

                Informal:

                ![](./ObjectReplacements/Object 592){width="12.614cm"
                height="0.506cm"}

                ![](./ObjectReplacements/Object 142){width="12.185cm"
                height="0.506cm"}

                Formal:

                1.  ![](./ObjectReplacements/Object 1958){width="2.713cm"
                    height="0.506cm"}

                    Expresión bien formada como parte izquierda de la
                    igualdad.

                2.  ![](./ObjectReplacements/Object 1959){width="6.63cm"
                    height="0.506cm"}

                    Axioma de distribución del producto respecto de la
                    suma.

                3.  ![](./ObjectReplacements/Object 1982){width="5.232cm"
                    height="0.506cm"}

                    Lema de asociatividad del producto cuando uno de los
                    factores es complementario de otro.

                4.  ![](./ObjectReplacements/Object 1960){width="4.427cm"
                    height="0.506cm"}

                    Axioma del elemento neutro de la suma.

                5.  ![](./ObjectReplacements/Object 1961){width="4.427cm"
                    height="0.506cm"}

                    Axioma de conmutatividad del producto.

                6.  ![](./ObjectReplacements/Object 1965){width="6.865cm"
                    height="0.467cm"}

                    Axioma de asociatividad del producto cuando uno de
                    los operandos es complementario de otro.

                7.  ![](./ObjectReplacements/Object 1966){width="2.976cm"
                    height="0.506cm"}

                    Transitividad de la igualdad desde la fórmula (1) a
                    la (6).

                8.  ![](./ObjectReplacements/Object 1962){width="2.866cm"
                    height="0.506cm"}

                    Expresión de lado izquierdo de la igualdad bien
                    formada.

                9.  ![](./ObjectReplacements/Object 1968){width="5.514cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                10. ![](./ObjectReplacements/Object 1963){width="7.177cm"
                    height="0.506cm"}

                    Axioma de distribución izquierda de la suma respecto
                    del producto.

                11. ![](./ObjectReplacements/Object 1964){width="7.177cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                12. ![](./ObjectReplacements/Object 1967){width="5.493cm"
                    height="0.506cm"}

                    Lema asociativo de la suma cuando un operando es
                    complementario de otro.

                13. ![](./ObjectReplacements/Object 1969){width="4.854cm"
                    height="0.506cm"}

                    Axioma de elemento neutro del producto.

                14. $$\mspace{486mu}{= {{({\overline{x} + \overline{y}})} + \overline{\overline{y}}} =}$$

                    Teorema de la doble negación.

                15. ![](./ObjectReplacements/Object 1975){width="6.854cm"
                    height="0.467cm"}

                    Lema de asociatividad de la suma cuando un operando
                    es complementario de otro.

                16. ![](./ObjectReplacements/Object 1957){width="2.965cm"
                    height="0.506cm"}

                    Transitividad de la igualdad desde la fórmula (8)
                    hasta la (15).

                17. ![](./ObjectReplacements/Object 1970){width="6.653cm"
                    height="0.559cm"}

                    Fórmulas (7) y (16).

                18. ![](./ObjectReplacements/Object 1971){width="2.598cm"
                    height="0.63cm"}

                    Derivación por el axioma de existencia de
                    complementarios.

                19. $${{({\overline{x} \cdot \overline{y}})} = \overline{({x+y})}}{}$$

                    Por el teorema de unicidad del complementario.

        14. Transformación de la suma y el producto mediante Morgan y
            doble complemento:

            1.  De la suma en
                producto:![](./ObjectReplacements/Object 27){width="3.918cm"
                height="0.563cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1974){width="1.341cm"
                    height="0.467cm"}

                    Expresión bien formada en la parte izquierda de la
                    igualdad.

                2.  ![](./ObjectReplacements/Object 1983){width="2.738cm"
                    height="0.573cm"}

                    Por el teorema de la doble negación es identidad.

                3.  ![](./ObjectReplacements/Object 1984){width="3.369cm"
                    height="0.573cm"}

                    Por el teorema de Morgan sobre la negación de una
                    suma.

                4.  ![](./ObjectReplacements/Object 143){width="2.224cm"
                    height="0.573cm"}

                    Por la transitividad de la igualdad desde la
                    fórmula (1) a la (3).

            2.  Del producto en
                suma:![](./ObjectReplacements/Object 26){width="3.918cm"
                height="0.563cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 1985){width="1.187cm"
                    height="0.467cm"}

                    Expresión bien formada en la parte izquierda de la
                    igualdad.

                2.  ![](./ObjectReplacements/Object 1986){width="2.582cm"
                    height="0.573cm"}

                    Por el teorema de doble negación es identidad.

                3.  ![](./ObjectReplacements/Object 1987){width="3.522cm"
                    height="0.573cm"}

                    Por el teorema de Morgan de la negación del
                    producto.

                4.  ![](./ObjectReplacements/Object 144){width="2.224cm"
                    height="0.573cm"}

                    Transitividad de la igualdad desde la fórmula (1) a
                    la (3).

        15. Asociatividad de las operaciones binarias:

            1.  De la suma:
                ![](./ObjectReplacements/Object 22){width="6.061cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 157){width="2.658cm"
                    height="0.506cm"}

                    Definición dónde la parte derecha de la igualdad
                    está bien formada.

                2.  ![](./ObjectReplacements/Object 158){width="2.658cm"
                    height="0.506cm"}

                    Definición dónde la parte derecha de la igualdad
                    está bien formada.

                3.  ![](./ObjectReplacements/Object 205){width="0.778cm"
                    height="0.467cm"}

                    Expresión bien formada en la parte izquierda de la
                    igualdad.

                4.  ![](./ObjectReplacements/Object 1991){width="3.09cm"
                    height="0.63cm"}

                    Fórmula derivada de (2) por aplicación de una
                    operación unaria unívoca sobre ambos lados de la
                    igualdad.

                5.  ![](./ObjectReplacements/Object 1988){width="2.949cm"
                    height="0.637cm"}

                    Teorema de Morgan de la negación de la suma.

                6.  ![](./ObjectReplacements/Object 1989){width="4.45cm"
                    height="0.575cm"}

                    Teorema de Morgan de la negación de la suma.

                7.  ![](./ObjectReplacements/Object 1990){width="2.281cm"
                    height="0.575cm"}

                    Transitividad de la igualdad desde la fórmula (3) a
                    la (6).

                8.  ![](./ObjectReplacements/Object 206){width="1.293cm"
                    height="0.467cm"}

                    Expresión bien formada en el lado izquierdo de la
                    igualdad.

                9.  ![](./ObjectReplacements/Object 1992){width="3.974cm"
                    height="0.575cm"}

                    Sustitución de un término de la fórmula (8) por el
                    lado derecho de la igualdad (7).

                10. ![](./ObjectReplacements/Object 1993){width="4.246cm"
                    height="0.575cm"}

                    Axioma de distribución del producto respecto de la
                    suma.

                11. ![](./ObjectReplacements/Object 1994){width="5.368cm"
                    height="0.575cm"}

                    Axioma de distribución del producto respecto de la
                    suma.

                12. ![](./ObjectReplacements/Object 209){width="10.409cm"
                    height="0.506cm"}

                    Sustitución de un término de la fórmula (11) por el
                    lado derecho de la igualdad definición (1).

                13. ![](./ObjectReplacements/Object 504){width="7.962cm"
                    height="0.506cm"}

                    Lema de asociatividad de la suma cuando un término
                    es complementario de otro.

                14. ![](./ObjectReplacements/Object 505){width="7.324cm"
                    height="0.506cm"}

                    Axioma de elemento neutro del producto.

                15. ![](./ObjectReplacements/Object 506){width="4.874cm"
                    height="0.506cm"}

                    Axioma de distribución del producto respecto de la
                    suma.

                16. ![](./ObjectReplacements/Object 507){width="5.027cm"
                    height="0.563cm"}

                    Teorema de Morgan de la negación de la suma.

                17. ![](./ObjectReplacements/Object 208){width="5.027cm"
                    height="0.563cm"}

                    Axioma de conmutatividad de la suma.

                18. ![](./ObjectReplacements/Object 509){width="9.206cm"
                    height="0.467cm"}

                    Lema de asociatividad de la suma cuando un término
                    es complemento de otro.

                19. ![](./ObjectReplacements/Object 2004){width="1.519cm"
                    height="0.467cm"}

                    Transitividad de la igualdad desde la fórmula (8) a
                    la (18).

                20. ![](./ObjectReplacements/Object 510){width="1.139cm"
                    height="0.467cm"}

                    Expresión bien formada en el lado izquierdo de la
                    igualdad.

                21. ![](./ObjectReplacements/Object 508){width="3.821cm"
                    height="0.575cm"}

                    Sustitución de un término de la fórmula (21) por el
                    lado derecho de la igualdad (7).

                22. ![](./ObjectReplacements/Object 511){width="5.018cm"
                    height="0.575cm"}

                    Sustitución de un término de la fórmula (21) por el
                    lado derecho de la igualdad definición (1).

                23. ![](./ObjectReplacements/Object 512){width="7.177cm"
                    height="0.506cm"}

                    Axioma de distribución del producto respecto de la
                    suma.

                24. ![](./ObjectReplacements/Object 1995){width="7.177cm"
                    height="0.506cm"}

                    Axioma de conmutatividad del producto.

                25. $$\mspace{144mu}{= {{({x \cdot {({\overline{x} \cdot {({\overline{y} \cdot \overline{z}})}})}})} + {({{({\overline{x} \cdot \overline{({y+z})}})} \cdot {({y + z})}})}} =}$$

                    Teorema de Morgan de la negación de la suma.

                26. ![](./ObjectReplacements/Object 1997){width="7.624cm"
                    height="0.617cm"}

                    Teorema de doble negación es identidad.

                27. ![](./ObjectReplacements/Object 1998){width="4.355cm"
                    height="0.506cm"}

                    Lema de asociatividad del producto cuando un término
                    es complemento de otro.

                28. ![](./ObjectReplacements/Object 1999){width="3.551cm"
                    height="0.506cm"}

                    Axioma de elemento neutro de la suma.

                29. ![](./ObjectReplacements/Object 2000){width="3.551cm"
                    height="0.506cm"}

                    Axioma de conmutatividad del producto.

                30. ![](./ObjectReplacements/Object 2001){width="3.551cm"
                    height="0.506cm"}

                    Axioma de conmutatividad del producto.

                31. ![](./ObjectReplacements/Object 2002){width="3.844cm"
                    height="0.563cm"}

                    Teorema de doble negación es identidad.

                32. ![](./ObjectReplacements/Object 2003){width="10.225cm"
                    height="0.467cm"}

                    Lema de asociatividad del producto cuando un término
                    es complemento de otro.

                33. ![](./ObjectReplacements/Object 2005){width="1.378cm"
                    height="0.467cm"}

                    Transitividad del la igualdad desde la fórmula (20)
                    a la (32).

                34. ![](./ObjectReplacements/Object 519){width="0.982cm"
                    height="0.467cm"}

                    De (33) y (19) por el axioma de existencia de
                    elemento complementario.

                35. ![](./ObjectReplacements/Object 513){width="1.002cm"
                    height="0.467cm"}

                    Teorema de unicidad del complementario.

                36. ![](./ObjectReplacements/Object 514){width="1.002cm"
                    height="0.467cm"}

                    Simetría de la igualdad.

                37. ![](./ObjectReplacements/Object 515){width="1.002cm"
                    height="0.517cm"}

                    Por el teorema de unicidad del complementario la
                    igualdad permanece.

                38. ![](./ObjectReplacements/Object 2006){width="1.018cm"
                    height="0.467cm"}

                    Teorema doble negación es identidad.

                39. ![](./ObjectReplacements/Object 2007){width="3.651cm"
                    height="0.519cm"}

                    Sustitución en (38) de
                    ![](./ObjectReplacements/Object 516){width="0.441cm"
                    height="0.467cm"}por el lado derecho de (1) y de
                    ![](./ObjectReplacements/Object 517){width="0.425cm"
                    height="0.467cm"}por el lado izquierdo de (2).

            2.  De la operación producto:
                ![](./ObjectReplacements/Object 520){width="5.445cm"
                height="0.577cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 528){width="2.351cm"
                    height="0.506cm"}

                    Definición dónde la parte derecha de la igualdad
                    está bien formada.

                2.  ![](./ObjectReplacements/Object 529){width="2.351cm"
                    height="0.506cm"}

                    Definición dónde la parte derecha de la igualdad
                    está bien formada.

                3.  ![](./ObjectReplacements/Object 530){width="0.778cm"
                    height="0.467cm"}

                    Expresión bien formada en la parte izquierda de la
                    igualdad.

                4.  ![](./ObjectReplacements/Object 531){width="2.616cm"
                    height="0.63cm"}

                    Fórmula derivada de (2) por aplicación de una
                    operación unaria unívoca sobre ambos lados de la
                    igualdad.

                5.  ![](./ObjectReplacements/Object 532){width="2.782cm"
                    height="0.637cm"}

                    Teorema de Morgan de la negación del producto.

                6.  ![](./ObjectReplacements/Object 533){width="4.759cm"
                    height="0.575cm"}

                    Teorema de Morgan de la negación del producto.

                7.  ![](./ObjectReplacements/Object 534){width="2.589cm"
                    height="0.575cm"}

                    Transitividad de la igualdad desde la fórmula (3) a
                    la (6).

                8.  ![](./ObjectReplacements/Object 535){width="1.139cm"
                    height="0.467cm"}

                    Expresión bien formada en el lado izquierdo de la
                    igualdad.

                9.  ![](./ObjectReplacements/Object 536){width="3.455cm"
                    height="0.575cm"}

                    Sustitución de un término de la fórmula (8) por el
                    lado derecho de la igualdad (7).

                10. ![](./ObjectReplacements/Object 537){width="4.076cm"
                    height="0.575cm"}

                    Axioma de distribución de la suma respecto del
                    producto.

                11. ![](./ObjectReplacements/Object 538){width="5.046cm"
                    height="0.575cm"}

                    Axioma de distribución de la suma respecto del
                    producto.

                12. ![](./ObjectReplacements/Object 539){width="9.163cm"
                    height="0.506cm"}

                    Sustitución de un término de la fórmula (11) por el
                    lado derecho de la igualdad definición (1).

                13. ![](./ObjectReplacements/Object 540){width="7.19cm"
                    height="0.506cm"}

                    Lema de asociatividad del producto cuando un término
                    es complementario de otro.

                14. ![](./ObjectReplacements/Object 541){width="6.385cm"
                    height="0.506cm"}

                    Axioma de elemento neutro de la suma.

                15. ![](./ObjectReplacements/Object 542){width="4.397cm"
                    height="0.506cm"}

                    Axioma de distribución de la suma respecto del
                    producto.

                16. ![](./ObjectReplacements/Object 543){width="4.242cm"
                    height="0.563cm"}

                    Teorema de Morgan de la negación del producto.

                17. ![](./ObjectReplacements/Object 2008){width="4.242cm"
                    height="0.563cm"}

                    Axioma de conmutatividad del producto.

                18. ![](./ObjectReplacements/Object 2009){width="2.104cm"
                    height="0.467cm"}

                    Lema de asociatividad del producto cuando un término
                    es complemento de otro.

                19. ![](./ObjectReplacements/Object 2010){width="1.378cm"
                    height="0.467cm"}

                    Transitividad de la igualdad desde la fórmula (8) a
                    la (18).

                20. ![](./ObjectReplacements/Object 2011){width="1.293cm"
                    height="0.467cm"}

                    Expresión bien formada en el lado izquierdo de la
                    igualdad.

                21. ![](./ObjectReplacements/Object 2012){width="3.149cm"
                    height="0.575cm"}

                    Sustitución de un término de la fórmula (21) por el
                    lado derecho de la igualdad (7).

                22. ![](./ObjectReplacements/Object 2013){width="5.173cm"
                    height="0.575cm"}

                    Sustitución de un término de la fórmula (21) por el
                    lado derecho de la igualdad definición (1).

                23. ![](./ObjectReplacements/Object 2014){width="7.795cm"
                    height="0.506cm"}

                    Axioma de distribución de la suma respecto del
                    producto.

                24. ![](./ObjectReplacements/Object 2015){width="7.795cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                25. ![](./ObjectReplacements/Object 2016){width="7.639cm"
                    height="0.563cm"}

                    Teorema de Morgan de la negación del producto.

                26. ![](./ObjectReplacements/Object 2017){width="7.932cm"
                    height="0.617cm"}

                    Teorema de doble negación es identidad.

                27. ![](./ObjectReplacements/Object 2018){width="4.651cm"
                    height="0.506cm"}

                    Lema de asociatividad de la suma cuando un término
                    es complemento de otro.

                28. ![](./ObjectReplacements/Object 2019){width="4.013cm"
                    height="0.506cm"}

                    Axioma de elemento neutro del producto.

                29. ![](./ObjectReplacements/Object 2020){width="4.013cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                30. ![](./ObjectReplacements/Object 2021){width="4.013cm"
                    height="0.506cm"}

                    Axioma de conmutatividad de la suma.

                31. ![](./ObjectReplacements/Object 2022){width="4.306cm"
                    height="0.563cm"}

                    Teorema de doble negación es identidad.

                32. ![](./ObjectReplacements/Object 2023){width="10.55cm"
                    height="0.467cm"}

                    Lema de asociatividad de la suma cuando un término
                    es complemento de otro.

                33. ![](./ObjectReplacements/Object 2024){width="1.519cm"
                    height="0.467cm"}

                    Transitividad del la igualdad desde la fórmula (20)
                    a la (32).

                34. ![](./ObjectReplacements/Object 2025){width="0.982cm"
                    height="0.467cm"}

                    De (33) y (19) por el axioma de existencia de
                    elemento complementario.

                35. ![](./ObjectReplacements/Object 2026){width="1.002cm"
                    height="0.467cm"}

                    Teorema de unicidad del complementario.

                36. $$\overline{a} = \overline{b}$$

                    Simetría de la igualdad.

                37. ![](./ObjectReplacements/Object 2028){width="1.002cm"
                    height="0.517cm"}

                    Por el teorema de unicidad del complementario la
                    igualdad permanece.

                38. ![](./ObjectReplacements/Object 2029){width="1.018cm"
                    height="0.467cm"}

                    Teorema doble negación es identidad.

                39. ![](./ObjectReplacements/Object 2030){width="3.036cm"
                    height="0.519cm"}

                    Sustitución en (38) de
                    ![](./ObjectReplacements/Object 21){width="0.441cm"
                    height="0.467cm"}por el lado derecho de (1) y de
                    ![](./ObjectReplacements/Object 518){width="0.425cm"
                    height="0.467cm"}por el lado izquierdo de (2).

        16. Propiedad de simplificación de Quine:

            1.  ![](./ObjectReplacements/Object 563){width="5.967cm"
                height="0.575cm"}

                Prueba:

                1.  ![](./ObjectReplacements/Object 521){width="3.946cm"
                    height="0.575cm"}
                2.  ![](./ObjectReplacements/Object 522){width="3.519cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 525){width="3.812cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 526){width="5.293cm"
                    height="0.506cm"}
                5.  ![](./ObjectReplacements/Object 527){width="5.293cm"
                    height="0.506cm"}
                6.  ![](./ObjectReplacements/Object 1006){width="6.93cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 1009){width="6.93cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 1012){width="5.299cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 2031){width="4.658cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 2032){width="4.658cm"
                    height="0.506cm"}
                11. ![](./ObjectReplacements/Object 2033){width="3.022cm"
                    height="0.506cm"}
                12. ![](./ObjectReplacements/Object 2034){width="3.022cm"
                    height="0.506cm"}
                13. ![](./ObjectReplacements/Object 2035){width="3.717cm"
                    height="0.506cm"}
                14. ![](./ObjectReplacements/Object 2036){width="3.717cm"
                    height="0.506cm"}
                15. ![](./ObjectReplacements/Object 2040){width="2.683cm"
                    height="0.506cm"}
                16. ![](./ObjectReplacements/Object 2041){width="6.073cm"
                    height="0.575cm"}

            2.  ![](./ObjectReplacements/Object 1296){width="6.017cm"
                height="0.519cm"}

Prueba:

37. 1.  1.  1.  1.  $${\left( {\left( {x + y} \right) \cdot \left( {x + \overline{z}} \right)} \right) \cdot \left( {y + z} \right)} = {}$$
                2.  ![](./ObjectReplacements/Object 1294){width="3.812cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 1587){width="3.812cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 1588){width="5.293cm"
                    height="0.506cm"}
                5.  ![](./ObjectReplacements/Object 1589){width="5.293cm"
                    height="0.506cm"}
                6.  ![](./ObjectReplacements/Object 1590){width="6.622cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 2037){width="6.623cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 2038){width="5.309cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 2039){width="4.505cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 2042){width="4.505cm"
                    height="0.506cm"}
                11. $${} = {{({{({y + z})} \cdot x})} + y} = {}$$
                12. ![](./ObjectReplacements/Object 2044){width="3.177cm"
                    height="0.506cm"}
                13. ![](./ObjectReplacements/Object 2045){width="4.023cm"
                    height="0.506cm"}
                14. ![](./ObjectReplacements/Object 2046){width="4.023cm"
                    height="0.506cm"}
                15. ![](./ObjectReplacements/Object 2047){width="2.836cm"
                    height="0.506cm"}
                16. ![](./ObjectReplacements/Object 562){width="6.073cm"
                    height="0.575cm"}

        2.  Todos los axiomas de los que hemos partido son reducibles al
            siguiente grupo de axiomas:

            1.  Axiomas para un álgebra de Boole con
                solo![](./ObjectReplacements/Object 152){width="1.224cm"
                height="0.621cm"}(Sheffer 1933):

                1.  ![](./ObjectReplacements/Object 1649){width="1.663cm"
                    height="0.624cm"}
                2.  ![](./ObjectReplacements/Object 145){width="7.848cm"
                    height="0.563cm"}
                3.  ![](./ObjectReplacements/Object 147){width="6.292cm"
                    height="0.577cm"}
                4.  ![](./ObjectReplacements/Object 149){width="6.851cm"
                    height="0.577cm"}
                5.  ![](./ObjectReplacements/Object 148){width="11.654cm"
                    height="0.577cm"}

            2.  Es muy fácil demostrar que los axiomas de Huntington de
                1904, implican estos 5 axiomas de Sheffer. Los puntos 1
                y 2 son inmediatos, y ya se han definido. También es
                fácil ver
                que![](./ObjectReplacements/Object 146){width="1.566cm"
                height="0.467cm"}(ya se ha visto),
                $$\overline{x}@{\overline{x} = \overline{\overline{x}} = x}$$y
                con ello queda probado
                3.![](./ObjectReplacements/Object 151){width="5.611cm"
                height="0.563cm"}, y de otro lado queda
                que![](./ObjectReplacements/Object 1620){width="1.549cm"
                height="0.467cm"}, y el punto 4 queda demostrado. El
                punto 5 vamos a reducirlo a expresiones en sumas y
                productos y negaciones, aplicaremos la distributiva y
                agruparemos de nuevo la expresión en la forma deseada.
                La parte izquierda de la igualdad 5 es
                ![](./ObjectReplacements/Object 1651){width="4.277cm"
                height="0.506cm"}que deshaciendo en sumas y negaciones
                sale![](./ObjectReplacements/Object 1650){width="1.506cm"
                height="0.503cm"}donde quitando la doble negación y
                aplicando
                Morgan![](./ObjectReplacements/Object 1652){width="1.658cm"
                height="0.506cm"}, ahora solo aplicamos
                distributiva![](./ObjectReplacements/Object 1653){width="2.498cm"
                height="0.506cm"} y ahora aplicamos
                conmutabilidad![](./ObjectReplacements/Object 1621){width="2.498cm"
                height="0.506cm"}y reagrupamos en funciones
                "NOR"![](./ObjectReplacements/Object 1654){width="2.043cm"
                height="0.467cm"}y ya tenemos la igualdad del axioma 5
                de Sheffer en su parte
                derecha:![](./ObjectReplacements/Object 1655){width="4.277cm"
                height="0.506cm"}.

        3.  Los axiomas de Huntington de 1903 (H03) implican los de
            Sheffer de 1933 (S33).

            Diremos![](./ObjectReplacements/Object 1656){width="2.223cm"
            height="0.467cm"}.

            1.  Demostraremos
                que![](./ObjectReplacements/Object 1657){width="2.223cm"
                height="0.467cm"}.

                1.  Definición![](./ObjectReplacements/Object 154){width="2.18cm"
                    height="0.467cm"}. Es una aplicación.

                2.  Axioma 3 de Sheffer en una nueva
                    escritura![](./ObjectReplacements/Object 1619){width="1.386cm"
                    height="0.467cm"}.

                3.  Conmutabilidad.
                    ![](./ObjectReplacements/Object 150){width="2.134cm"
                    height="0.467cm"}.

                    1.  ![](./ObjectReplacements/Object 153){width="7.308cm"
                        height="0.506cm"}
                    2.  ![](./ObjectReplacements/Object 155){width="10.338cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 156){width="6.812cm"
                        height="0.506cm"}
                    4.  ![](./ObjectReplacements/Object 1611){width="6.396cm"
                        height="0.506cm"}

                4.  Existencia de constante.
                    ![](./ObjectReplacements/Object 1622){width="2.482cm"
                    height="0.467cm"}

                    1.  ![](./ObjectReplacements/Object 1658){width="3.438cm"
                        height="0.506cm"}
                    2.  ![](./ObjectReplacements/Object 1659){width="4.15cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 1660){width="3.881cm"
                        height="0.506cm"}
                    4.  ![](./ObjectReplacements/Object 1661){width="1.842cm"
                        height="0.506cm"}

                5.  Definición![](./ObjectReplacements/Object 1662){width="1.723cm"
                    height="0.467cm"}. Es una única constante.

                6.  Definición![](./ObjectReplacements/Object 1663){width="2.926cm"
                    height="0.506cm"}. Es una única constante.

                7.  Definición![](./ObjectReplacements/Object 1664){width="2.623cm"
                    height="0.506cm"}. Es una aplicación.

                8.  Definición![](./ObjectReplacements/Object 1665){width="2.351cm"
                    height="0.467cm"}. Es una aplicación.

                9.  Elemento neutro de la suma.
                    ![](./ObjectReplacements/Object 1666){width="1.552cm"
                    height="0.467cm"}.

                    1.  Prueba:
                    2.  ![](./ObjectReplacements/Object 1667){width="5.801cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 1668){width="4.925cm"
                        height="0.506cm"}

                10. Elemento neutro del producto.
                    ![](./ObjectReplacements/Object 1670){width="1.385cm"
                    height="0.467cm"}.

                    1.  ![](./ObjectReplacements/Object 1671){width="3.607cm"
                        height="0.467cm"}

                11. Conmutabilidad de la
                    suma:![](./ObjectReplacements/Object 1669){width="2.141cm"
                    height="0.467cm"}. Solo hay que aplicar repetidas
                    veces la conmutabilidad de la "NOR".

                12. Conmutabilidad del
                    producto:![](./ObjectReplacements/Object 1672){width="1.834cm"
                    height="0.467cm"}. Solo hay que aplicar repetidas
                    veces la conmutabilidad de la "NAND".

                13. Distributividad de la suma respecto del producto.
                    ![](./ObjectReplacements/Object 1673){width="4.277cm"
                    height="0.506cm"}

                    1.  $${{x + {({y \cdot z})}} = {({x@{({y'@z'})}})}}'{' = {({{({y@x})}@{({z@x})}})}}'{' = {{({x + y})} \cdot {({x + z})}}}$$

                14. Distributividad del producto respecto de la
                    suma.![](./ObjectReplacements/Object 1676){width="4.124cm"
                    height="0.506cm"}

                    1.  ![](./ObjectReplacements/Object 1675){width="7.684cm"
                        height="0.506cm"}
                    2.  ![](./ObjectReplacements/Object 1677){width="7.19cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 1678){width="5.796cm"
                        height="0.506cm"}

                15. Existe elemento complementario.

                    1.  ![](./ObjectReplacements/Object 1679){width="3.263cm"
                        height="0.467cm"}

                        1.  ![](./ObjectReplacements/Object 1680){width="2.514cm"
                            height="0.467cm"}
                        2.  ![](./ObjectReplacements/Object 1681){width="4.226cm"
                            height="0.506cm"}

                    2.  ![](./ObjectReplacements/Object 1683){width="3.124cm"
                        height="0.467cm"}

                        1.  ![](./ObjectReplacements/Object 1684){width="2.514cm"
                            height="0.467cm"}
                        2.  ![](./ObjectReplacements/Object 1682){width="4.168cm"
                            height="0.467cm"}

                16. Definición:![](./ObjectReplacements/Object 1597){width="3.194cm"
                    height="0.467cm"}

        4.  Todos los axiomas de los que hemos partido son reducibles al
            siguiente grupo de axiomas (nueva interpretación de la
            flecha de Sheffer):

            1.  Axiomas para un álgebra de Boole con
                solo![](./ObjectReplacements/Object 1686){width="1.224cm"
                height="0.621cm"}(Sheffer 1933):

                1.  ![](./ObjectReplacements/Object 1687){width="1.663cm"
                    height="0.624cm"}
                2.  ![](./ObjectReplacements/Object 1688){width="7.848cm"
                    height="0.563cm"}
                3.  ![](./ObjectReplacements/Object 1689){width="4.778cm"
                    height="0.577cm"}
                4.  ![](./ObjectReplacements/Object 1690){width="5.844cm"
                    height="0.577cm"}
                5.  $$\forall x,y,{z \in}{({x@{({y@z})}})}@{{({x@{({y@z})}})} = {({{({y@y})}@x})}}@{({{({z@z})}@x})}$$

        5.  Es muy fácil demostrar que los axiomas de Huntington de
            1903, implican estos 5 axiomas de Sheffer. Los puntos 1 y 2
            son inmediatos, y ya se han definido. También es fácil ver
            que![](./ObjectReplacements/Object 1692){width="1.566cm"
            height="0.467cm"}(ya se ha visto),
            ![](./ObjectReplacements/Object 1693){width="2.163cm"
            height="0.467cm"}y con ello queda probado
            3.![](./ObjectReplacements/Object 1694){width="5.457cm"
            height="0.563cm"}, y de otro lado queda
            que$$x@{1 = \overline{x}}$$, y el punto 4 queda demostrado.
            El punto 5 lo vamos a reducirlo a expresiones en sumas y
            productos y negaciones, aplicaremos la distributiva y
            agruparemos de nuevo la expresión en la forma deseada. La
            parte izquierda de la igualdad 5 es
            $${({x@{({y@z})}})}@{({x@{({y@z})}})}$$que deshaciendo en
            sumas y negaciones
            sale$$\overline{\overline{x\cdot\overline{y\cdot z}}}$$donde
            quitando la doble negación y aplicando Morgan
            queda$$x \cdot {({\overline{y} + \overline{z}})}$$, ahora
            solo aplicamos
            distributiva$${({x \cdot \overline{y}})} + {({x \cdot \overline{z}})}$$
            y ahora aplicamos
            conmutabilidad![](./ObjectReplacements/Object 1700){width="2.344cm"
            height="0.506cm"}y reagrupamos en funciones
            "NAND"![](./ObjectReplacements/Object 1701){width="1.58cm"
            height="0.467cm"}y ya tenemos la igualdad del axioma (5) de
            Sheffer en su parte
            derecha:![](./ObjectReplacements/Object 1702){width="4.277cm"
            height="0.506cm"}.

        6.  Los axiomas de Huntington de 1903 (H03) implican los de
            Sheffer re-interpretados de 1933 (S'33).
            Diremos![](./ObjectReplacements/Object 1703){width="2.397cm"
            height="0.467cm"}.

            1.  Demostraremos
                que![](./ObjectReplacements/Object 1704){width="2.397cm"
                height="0.467cm"}.

                1.  Definición![](./ObjectReplacements/Object 1705){width="2.18cm"
                    height="0.467cm"}. Es una aplicación.

                2.  Axioma 3 de Sheffer en una nueva
                    escritura![](./ObjectReplacements/Object 1706){width="1.386cm"
                    height="0.467cm"}.

                3.  Conmutabilidad.
                    ![](./ObjectReplacements/Object 1707){width="2.134cm"
                    height="0.467cm"}.

                    1.  ![](./ObjectReplacements/Object 1708){width="7.308cm"
                        height="0.506cm"}
                    2.  ![](./ObjectReplacements/Object 1709){width="10.497cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 1710){width="6.971cm"
                        height="0.506cm"}
                    4.  ![](./ObjectReplacements/Object 1711){width="6.396cm"
                        height="0.506cm"}

                4.  Existencia de una expresión constante.
                    ![](./ObjectReplacements/Object 1712){width="2.482cm"
                    height="0.467cm"}

                    1.  ![](./ObjectReplacements/Object 1713){width="3.438cm"
                        height="0.506cm"}
                    2.  ![](./ObjectReplacements/Object 1714){width="3.881cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 1715){width="3.881cm"
                        height="0.506cm"}
                    4.  ![](./ObjectReplacements/Object 1716){width="1.842cm"
                        height="0.506cm"}

                5.  Definición![](./ObjectReplacements/Object 1717){width="1.729cm"
                    height="0.467cm"}. Es una única constante.

                6.  Definición![](./ObjectReplacements/Object 1718){width="2.944cm"
                    height="0.506cm"}. Es una única constante.

                7.  Definición![](./ObjectReplacements/Object 1719){width="2.469cm"
                    height="0.506cm"}. Es una aplicación.

                8.  Definición![](./ObjectReplacements/Object 1720){width="2.505cm"
                    height="0.467cm"}. Es una aplicación.

                9.  Elemento neutro del producto.
                    ![](./ObjectReplacements/Object 1721){width="1.385cm"
                    height="0.467cm"}.

                    1.  ![](./ObjectReplacements/Object 1722){width="5.609cm"
                        height="0.506cm"}
                    2.  ![](./ObjectReplacements/Object 1723){width="4.886cm"
                        height="0.506cm"}

                10. Elemento neutro de la suma.
                    ![](./ObjectReplacements/Object 1724){width="1.552cm"
                    height="0.467cm"}.

                    1.  ![](./ObjectReplacements/Object 1725){width="3.761cm"
                        height="0.467cm"}

                11. Conmutabilidad del
                    producto:![](./ObjectReplacements/Object 1726){width="1.834cm"
                    height="0.467cm"}. Solo hay que aplicar repetidas
                    veces la conmutabilidad de la "NAND".

                12. Conmutabilidad del
                    producto:![](./ObjectReplacements/Object 1727){width="1.834cm"
                    height="0.467cm"}. Solo hay que aplicar repetidas
                    veces la conmutabilidad de la "NOR".

                13. Distributividad del producto respecto de la suma:
                    ![](./ObjectReplacements/Object 1728){width="4.124cm"
                    height="0.506cm"}

                    1.  ![](./ObjectReplacements/Object 1729){width="10.456cm"
                        height="0.506cm"}

                14. Distributividad de la suma respecto del producto:
                    $${x + {({y \cdot z})}} = {{({x + y})} \cdot {({x + z})}}$$

                    1.  $${{x + {({y \cdot z})}} = {({{x'}@{({y@z})}'})}}'{' = {({{({y@z})}@{x'}})}}'{' =}$$
                    2.  ![](./ObjectReplacements/Object 1732){width="7.19cm"
                        height="0.506cm"}
                    3.  ![](./ObjectReplacements/Object 1733){width="5.681cm"
                        height="0.506cm"}

                15. Existe elemento complementario.

                    1.  ![](./ObjectReplacements/Object 1734){width="3.124cm"
                        height="0.467cm"}

                        1.  ![](./ObjectReplacements/Object 1735){width="2.514cm"
                            height="0.467cm"}
                        2.  ![](./ObjectReplacements/Object 1736){width="4.073cm"
                            height="0.506cm"}

                    2.  ![](./ObjectReplacements/Object 1737){width="3.263cm"
                        height="0.467cm"}

                        1.  ![](./ObjectReplacements/Object 1738){width="2.514cm"
                            height="0.467cm"}
                        2.  $${x + x}{' = {x'@x} = {x@x'} = 1}$$

                16. Definición:
                    ![](./ObjectReplacements/Object 1598){width="3.194cm"
                    height="0.467cm"}

        7.  Lo más habitual es que la flecha de Sheffer se simbolice
            por![](./ObjectReplacements/Object 1599){width="0.402cm"
            height="0.325cm"}cuando es la suma negada, y por
            ![](./ObjectReplacements/Object 1600){width="0.402cm"
            height="0.325cm"}cuando es el producto negado, tal como lo
            hemos hecho en el anterior texto. Ya que los razonamientos
            hechos con una de las 2 interpretaciones son absolutamente
            simétricos y duales, en vez de hacer referencias a la suma o
            al producto lo hacemos a
            ![](./ObjectReplacements/Object 1601){width="1.473cm"
            height="0.506cm"}o a
            ![](./ObjectReplacements/Object 1602){width="1.339cm"
            height="0.467cm"}o idénticamente a
            ![](./ObjectReplacements/Object 1603){width="1.473cm"
            height="0.506cm"}o
            a![](./ObjectReplacements/Object 1604){width="1.339cm"
            height="0.467cm"}, por lo que en vez de diferenciar se usa
            habitualmente como símbolo
            ![](./ObjectReplacements/Object 1605){width="0.852cm"
            height="0.489cm"}o "Sheffer's stroke".

        8.  Dualidad en el álgebra de Boole. \[Metateorema\]

            1.  Cambiando simultáneamente todas las ocurrencias entre
                "0,1,+,\*" por (respectivamente) las de "1,0,\*,+"
                obtenemos a partir de una ex­presión otra con el mismo
                valor de verdad que la primera. A medida que vaya­mos
                introduciendo nuevos operadores veremos como extender
                esta propiedad de dualidad. Se demuestra por inducción
                sobre cualquier expresión bien formada, teniendo en
                cuenta que todos los axiomas son simétricos, duales.

Prueba:

Primero hay que construir un lenguaje adecuado para las expresiones
booleanas (tal como está sirve para hacer un programa calculadora de
expresiones de Boo­le, aunque no programable, esto es, no podemos
introducir símbolos nuevos con su definición, por ejemplo funciones
booleanas nuevas, ni tampoco se pueden asignar valores a variables).

Partimos de un lenguaje lógico-formal de 1^er^ orden (lógica de
predicados) con igualdad y pertenencia definida a través de una teoría
de conjuntos con 3 tipos dónde la única primitiva es la pertenencia a un
conjunto y la igualdad de elementos de tipo 0. No vamos a definir esta
parte, sino que la emplearemos de forma transparente, y enumeraremos las
transformaciones válidas. La igualdad para los restantes tipos es la
bi-inclusión clásica.

El lenguaje siguiente no da la probabilidad de hacer definiciones, con
todo es bastante expresivo:

![](./ObjectReplacements/Object 2066){width="10.294cm" height="3.223cm"}

![](./ObjectReplacements/Object 216){width="14.067cm" height="2.695cm"}

![](./ObjectReplacements/Object 2051){width="14.545cm" height="2.21cm"}

![](./ObjectReplacements/Object 2050){width="16.291cm" height="2.332cm"}

![](./ObjectReplacements/Object 2049){width="16.274cm" height="2.461cm"}

![](./ObjectReplacements/Object 217){width="12.929cm" height="1.625cm"}

![](./ObjectReplacements/Object 2048){width="12.931cm" height="1.685cm"}

![](./ObjectReplacements/Object 220){width="12.931cm"
height="1.804cm"}![](./ObjectReplacements/Object 1184){width="13.099cm"
height="1.933cm"}

![](./ObjectReplacements/Object 2068){width="15.946cm"
height="10.809cm"}

![](./ObjectReplacements/Object 218){width="7.713cm" height="2.736cm"}

![](./ObjectReplacements/Object 219){width="12.813cm" height="1.265cm"}

![](./ObjectReplacements/Object 2073){width="11.578cm" height="0.676cm"}

![](./ObjectReplacements/Object 2074){width="12.084cm" height="0.676cm"}

![](./ObjectReplacements/Object 2075){width="12.247cm" height="0.676cm"}

![](./ObjectReplacements/Object 2072){width="14.757cm" height="3.286cm"}

![](./ObjectReplacements/Object 2076){width="13.665cm" height="3.286cm"}

![](./ObjectReplacements/Object 2077){width="14.002cm" height="3.286cm"}

![](./ObjectReplacements/Object 2078){width="14.259cm" height="2.184cm"}

![](./ObjectReplacements/Object 2065){width="8.631cm" height="1.813cm"}

![](./ObjectReplacements/Object 2079){width="11.735cm" height="3.406cm"}

![](./ObjectReplacements/Object 2080){width="13.571cm" height="2.916cm"}

![](./ObjectReplacements/Object 2067){width="13.601cm" height="2.916cm"}

![](./ObjectReplacements/Object 2081){width="13.615cm" height="2.916cm"}

![](./ObjectReplacements/Object 191){width="11.414cm" height="3.933cm"}

![](./ObjectReplacements/Object 2071){width="11.478cm" height="4.353cm"}

![](./ObjectReplacements/Object 2070){width="12.181cm" height="4.353cm"}

![](./ObjectReplacements/Object 2069){width="12.898cm" height="4.353cm"}

![](./ObjectReplacements/Object 17){width="5.978cm" height="2.471cm"}

38. 1.  1.  Operadores "nor" y "nand" que representaremos
            respectivamente
            como![](./ObjectReplacements/Object 32){width="0.402cm"
            height="0.325cm"}y![](./ObjectReplacements/Object 1606){width="0.402cm"
            height="0.325cm"}.

            1.  Definición de
                "nor":![](./ObjectReplacements/Object 33){width="3.616cm"
                height="0.467cm"}.
            2.  Definición de
                "nand":![](./ObjectReplacements/Object 34){width="3.616cm"
                height="0.467cm"}.

        2.  No asociatividad en general de "nor" y de "nand". Dar algún
            ejemplo
            en![](./ObjectReplacements/Object 199){width="0.637cm"
            height="0.61cm"}.

        3.  Cualquier expresión de las que hasta ahora se ha podido
            utilizar es expresable con solo funciones "nand" y con solo
            funciones "nor".

            1.  "NOR":

                1.  ![](./ObjectReplacements/Object 35){width="3.791cm"
                    height="0.506cm"}
                2.  ![](./ObjectReplacements/Object 36){width="3.928cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 37){width="1.535cm"
                    height="0.467cm"}

            2.  "NAND":

                1.  ![](./ObjectReplacements/Object 39){width="3.637cm"
                    height="0.506cm"}
                2.  ![](./ObjectReplacements/Object 40){width="3.791cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 38){width="1.535cm"
                    height="0.467cm"}

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
                ![](./ObjectReplacements/Object 43){width="6.726cm"
                height="0.506cm"}
            2.  Definición del operador "exnor":
                ![](./ObjectReplacements/Object 44){width="6.727cm"
                height="0.506cm"}

        7.  Nueva extensión del teorema de dualidad: solo hay que
            intercambiar "exor" por "ex­nor " y viceversa, además de
            todos los intercambios que anteriormente se han des­crito en
            22.

        8.  Propiedad de elemento inverso (el inverso de cada elemento
            existe y es él mismo):

            1.  Para la operación "exor" :
                ![](./ObjectReplacements/Object 57){width="3.087cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 159){width="5.122cm"
                    height="0.506cm"}

            2.  Para la operación "exnor":
                ![](./ObjectReplacements/Object 58){width="3.076cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 160){width="5.091cm"
                    height="0.506cm"}

        9.  Valor para un elemento operado con su complementario:

            1.  ![](./ObjectReplacements/Object 59){width="3.074cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 161){width="7.191cm"
                    height="0.506cm"}

            2.  ![](./ObjectReplacements/Object 60){width="3.087cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 162){width="7.205cm"
                    height="0.506cm"}

        10. Más valores de estas operaciones:

            1.  ![](./ObjectReplacements/Object 61){width="3.074cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 163){width="6.837cm"
                    height="0.506cm"}

            2.  ![](./ObjectReplacements/Object 56){width="3.087cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 164){width="7.004cm"
                    height="0.506cm"}

        11. Elementos neutros:

            1.  ![](./ObjectReplacements/Object 165){width="3.087cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 166){width="5.75cm"
                    height="0.506cm"}

            2.  ![](./ObjectReplacements/Object 168){width="3.076cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 167){width="5.872cm"
                    height="0.506cm"}

        12. Una propiedad de simetría:

            1.  ![](./ObjectReplacements/Object 70){width="4.085cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 207){width="9.765cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 169){width="9.74cm"
                    height="0.529cm"}

            2.  ![](./ObjectReplacements/Object 71){width="4.087cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 544){width="9.92cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 170){width="9.28cm"
                    height="0.529cm"}

        13. Los operadores negados "nexor" y "nexnor" coinciden
            respectivamente con "exnor" y "exor" (y así no se producen
            nuevos operadores):

            1.  ![](./ObjectReplacements/Object 68){width="7.602cm"
                height="0.563cm"}
            2.  $$\forall a,{b \in}{}{}{}{\overline{a\odot b} \equiv \overline{a\odot b} = \overline{a}}\odot{b = a}\odot{\overline{b} = a}\oplus b$$

        14. Asociatividad de los nuevos operadores "exor" y "exnor":

            1.  ![](./ObjectReplacements/Object 171){width="6.258cm"
                height="0.577cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 370){width="2.263cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 371){width="5.537cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 372){width="8.864cm"
                    height="0.563cm"}
                5.  ![](./ObjectReplacements/Object 373){width="8.864cm"
                    height="0.563cm"}
                6.  ![](./ObjectReplacements/Object 374){width="8.475cm"
                    height="0.563cm"}
                7.  ![](./ObjectReplacements/Object 375){width="8.782cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 376){width="8.393cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 377){width="8.992cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 378){width="6.412cm"
                    height="0.506cm"}
                11. ![](./ObjectReplacements/Object 379){width="6.412cm"
                    height="0.563cm"}
                12. ![](./ObjectReplacements/Object 172){width="3.971cm"
                    height="0.506cm"}

            2.  ![](./ObjectReplacements/Object 174){width="6.262cm"
                height="0.577cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 380){width="2.265cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 381){width="5.69cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 382){width="9.326cm"
                    height="0.563cm"}
                5.  ![](./ObjectReplacements/Object 383){width="9.326cm"
                    height="0.563cm"}
                6.  ![](./ObjectReplacements/Object 384){width="9.4cm"
                    height="0.563cm"}
                7.  ![](./ObjectReplacements/Object 385){width="9.089cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 386){width="8.393cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 387){width="8.992cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 388){width="6.565cm"
                    height="0.506cm"}
                11. ![](./ObjectReplacements/Object 389){width="6.412cm"
                    height="0.563cm"}
                12. ![](./ObjectReplacements/Object 173){width="3.972cm"
                    height="0.506cm"}

        15. Distributividad de
            "![](./ObjectReplacements/Object 175){width="0.572cm"
            height="0.467cm"}" respecto del producto lógico
            "![](./ObjectReplacements/Object 176){width="0.445cm"
            height="0.467cm"}" y de
            "![](./ObjectReplacements/Object 177){width="0.573cm"
            height="0.467cm"}" res­pecto de la suma lógica
            "![](./ObjectReplacements/Object 178){width="0.492cm"
            height="0.467cm"}":

            1.  ![](./ObjectReplacements/Object 179){width="8.186cm"
                height="0.577cm"}

                1.  Prueba:

                2.  ![](./ObjectReplacements/Object 221){width="4.23cm"
                    height="0.506cm"}

                3.  ![](./ObjectReplacements/Object 390){width="5.722cm"
                    height="0.563cm"}

                4.  ![](./ObjectReplacements/Object 391){width="5.292cm"
                    height="0.506cm"}

                5.  ![](./ObjectReplacements/Object 392){width="5.292cm"
                    height="0.563cm"}

                6.  ![](./ObjectReplacements/Object 393){width="9.11cm"
                    height="0.563cm"}

                7.  ![](./ObjectReplacements/Object 394){width="11.217cm"
                    height="0.506cm"}

                8.  ![](./ObjectReplacements/Object 395){width="11.896cm"
                    height="0.506cm"}

                9.  ![](./ObjectReplacements/Object 396){width="6.611cm"
                    height="0.506cm"}

                10. ![](./ObjectReplacements/Object 397){width="8.842cm"
                    height="0.506cm"}

                11. ![](./ObjectReplacements/Object 398){width="8.638cm"
                    height="0.506cm"}

                12. ![](./ObjectReplacements/Object 399){width="2.417cm"
                    height="0.467cm"}

                13. ![](./ObjectReplacements/Object 222){width="5.86cm"
                    height="0.563cm"}

                14. ![](./ObjectReplacements/Object 400){width="5.445cm"
                    height="0.506cm"}

                15. ![](./ObjectReplacements/Object 401){width="5.445cm"
                    height="0.563cm"}

                16. ![](./ObjectReplacements/Object 402){width="9.264cm"
                    height="0.563cm"}

                17. ![](./ObjectReplacements/Object 403){width="8.114cm"
                    height="0.506cm"}

                18. ![](./ObjectReplacements/Object 404){width="7.006cm"
                    height="0.506cm"}

                19. ![](./ObjectReplacements/Object 405){width="5.838cm"
                    height="0.467cm"}

                20. ![](./ObjectReplacements/Object 406){width="12.024cm"
                    height="0.467cm"}

                21. ![](./ObjectReplacements/Object 407){width="10.756cm"
                    height="0.467cm"}

                22. ![](./ObjectReplacements/Object 408){width="9.128cm"
                    height="0.506cm"}

                23. ![](./ObjectReplacements/Object 409){width="4.212cm"
                    height="0.467cm"}

                24. ![](./ObjectReplacements/Object 410){width="3.992cm"
                    height="0.506cm"}

                25. ![](./ObjectReplacements/Object 411){width="1.819cm"
                    height="0.467cm"}

                    ![](./ObjectReplacements/Object 223){width="10.414cm"
                    height="0.563cm"}

                    ![](./ObjectReplacements/Object 412){width="10.091cm"
                    height="0.467cm"}

                26. ![](./ObjectReplacements/Object 413){width="4.23cm"
                    height="0.506cm"}

                Es seguro que la prueba anterior puede ser acortada
                drásticamente, así que si al­guno encuentra una forma
                (quizás más directa) la pondremos en su lugar.

            2.  ![](./ObjectReplacements/Object 180){width="8.652cm"
                height="0.577cm"}Se prueba como en el caso anterior,
                sólo que cambiando los operadores duales, y las dos
                constantes
                ![](./ObjectReplacements/Object 192){width="1.161cm"
                height="0.492cm"} entre sí y obtenemos el resultado que
                hemos enunciado.

                1.  Prueba:

                2.  ![](./ObjectReplacements/Object 414){width="4.694cm"
                    height="0.506cm"}

                3.  ![](./ObjectReplacements/Object 415){width="6.339cm"
                    height="0.563cm"}

                4.  ![](./ObjectReplacements/Object 416){width="5.907cm"
                    height="0.506cm"}

                5.  ![](./ObjectReplacements/Object 417){width="5.909cm"
                    height="0.563cm"}

                6.  ![](./ObjectReplacements/Object 418){width="10.342cm"
                    height="0.563cm"}

                7.  ![](./ObjectReplacements/Object 419){width="12.448cm"
                    height="0.506cm"}

                8.  ![](./ObjectReplacements/Object 594){width="11.583cm"
                    height="0.506cm"}

                9.  ![](./ObjectReplacements/Object 420){width="4.147cm"
                    height="0.506cm"}

                10. ![](./ObjectReplacements/Object 421){width="6.897cm"
                    height="0.506cm"}

                11. ![](./ObjectReplacements/Object 422){width="10.075cm"
                    height="0.506cm"}

                12. ![](./ObjectReplacements/Object 423){width="10.022cm"
                    height="0.506cm"}

                13. ![](./ObjectReplacements/Object 424){width="2.064cm"
                    height="0.467cm"}

                14. ![](./ObjectReplacements/Object 425){width="6.168cm"
                    height="0.563cm"}

                15. ![](./ObjectReplacements/Object 426){width="5.754cm"
                    height="0.506cm"}

                16. ![](./ObjectReplacements/Object 427){width="5.756cm"
                    height="0.563cm"}

                17. ![](./ObjectReplacements/Object 428){width="10.188cm"
                    height="0.563cm"}

                18. ![](./ObjectReplacements/Object 429){width="8.29cm"
                    height="0.575cm"}

                19. ![](./ObjectReplacements/Object 430){width="7.761cm"
                    height="0.506cm"}

                20. ![](./ObjectReplacements/Object 431){width="10.888cm"
                    height="0.506cm"}![](./ObjectReplacements/Object 432){width="5.955cm"
                    height="0.506cm"}

                21. ![](./ObjectReplacements/Object 593){width="10.888cm"
                    height="0.506cm"}![](./ObjectReplacements/Object 433){width="4.24cm"
                    height="0.506cm"}

                22. ![](./ObjectReplacements/Object 434){width="12.511cm"
                    height="0.506cm"}

                23. ![](./ObjectReplacements/Object 435){width="5.533cm"
                    height="0.506cm"}

                24. ![](./ObjectReplacements/Object 436){width="4.42cm"
                    height="0.506cm"}

                25. ![](./ObjectReplacements/Object 437){width="1.676cm"
                    height="0.467cm"}

                    ![](./ObjectReplacements/Object 438){width="10.876cm"
                    height="0.563cm"}

                    ![](./ObjectReplacements/Object 439){width="10.091cm"
                    height="0.467cm"}

                26. ![](./ObjectReplacements/Object 181){width="4.694cm"
                    height="0.506cm"}

        16. Estructuras de anillo conmutativo con elemento unidad (es
            claro desde todas las pro­piedades anteriormente
            demostradas):

            1.  La más normal sería:
                ![](./ObjectReplacements/Object 45){width="4.314cm"
                height="0.577cm"}
            2.  Su forma dual es
                :![](./ObjectReplacements/Object 46){width="4.47cm"
                height="0.577cm"}

        17. Estructuras respectivas a 33 de bimódulo
            de![](./ObjectReplacements/Object 72){width="1.445cm"
            height="0.577cm"}sobre el anillo
            ![](./ObjectReplacements/Object 73){width="1.647cm"
            height="0.577cm"} y el dual, de
            ![](./ObjectReplacements/Object 74){width="1.445cm"
            height="0.577cm"}sobre el anillo
            ![](./ObjectReplacements/Object 75){width="1.803cm"
            height="0.577cm"}.

        A continuación hablaremos sobre como son en general las álgebras
        de Boole, funda­mentalmente las finitas, y veremos que
        efectivamente podemos llegar a teoremas que nos dicen de forma
        muy concreta cuales son estas álgebras de Boole. Vamos a ver
        for­mas de generarlas y cuestiones parecidas.

        18. En el caso que el cardinal
            de![](./ObjectReplacements/Object 47){width="0.51cm"
            height="0.563cm"}sea
            finito,![](./ObjectReplacements/Object 48){width="1.431cm"
            height="0.577cm"}. Para demostrarlo solo hay que darse
            cuenta
            que![](./ObjectReplacements/Object 182){width="2.706cm"
            height="0.667cm"}, que
            ![](./ObjectReplacements/Object 183){width="6.339cm"
            height="0.506cm"}y
            que![](./ObjectReplacements/Object 186){width="3.508cm"
            height="0.572cm"}y así
            cuando![](./ObjectReplacements/Object 187){width="0.51cm"
            height="0.563cm"}sea finito, su cardinal será un múlti­plo de
            2.

        19. Definición:

            ![](./ObjectReplacements/Object 1142){width="6.683cm"
            height="0.563cm"}

        20. ![](./ObjectReplacements/Object 1144){width="3.575cm"
            height="0.621cm"}

            1.  Reflexiva:
                ![](./ObjectReplacements/Object 1164){width="2.609cm"
                height="0.563cm"}

                1.  ![](./ObjectReplacements/Object 1145){width="2.986cm"
                    height="0.563cm"}
                2.  
                    ![](./ObjectReplacements/Object 1158){width="2.609cm"
                    height="0.563cm"}

            2.  Antisimétrica:
                ![](./ObjectReplacements/Object 1147){width="5.759cm"
                height="0.563cm"}

                1.  ![](./ObjectReplacements/Object 1146){width="3.881cm"
                    height="0.563cm"}
                2.  ![](./ObjectReplacements/Object 1148){width="4.658cm"
                    height="0.563cm"}
                3.  ![](./ObjectReplacements/Object 1149){width="2.672cm"
                    height="0.563cm"}

            3.  Transitiva:
                ![](./ObjectReplacements/Object 1150){width="6.133cm"
                height="0.563cm"}

                1.  
                    ![](./ObjectReplacements/Object 1151){width="2.244cm"
                    height="0.467cm"}
                2.  ![](./ObjectReplacements/Object 1152){width="3.022cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 1153){width="2.15cm"
                    height="0.467cm"}
                4.  ![](./ObjectReplacements/Object 1154){width="1.794cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 1155){width="1.395cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 1156){width="1.016cm"
                    height="0.467cm"}

        21. Definición:![](./ObjectReplacements/Object 1143){width="6.683cm"
            height="0.612cm"}

        22. ![](./ObjectReplacements/Object 1177){width="3.575cm"
            height="0.621cm"}

            1.  Reflexiva:
                ![](./ObjectReplacements/Object 1180){width="2.609cm"
                height="0.563cm"}

                1.  ![](./ObjectReplacements/Object 1182){width="3.141cm"
                    height="0.563cm"}
                2.  
                    ![](./ObjectReplacements/Object 1183){width="2.609cm"
                    height="0.563cm"}

            2.  Antisimétrica:
                ![](./ObjectReplacements/Object 1186){width="5.759cm"
                height="0.563cm"}

                1.  ![](./ObjectReplacements/Object 1187){width="3.881cm"
                    height="0.563cm"}
                2.  ![](./ObjectReplacements/Object 1188){width="4.965cm"
                    height="0.563cm"}
                3.  ![](./ObjectReplacements/Object 1189){width="2.672cm"
                    height="0.563cm"}

            3.  Transitiva:
                ![](./ObjectReplacements/Object 1190){width="6.133cm"
                height="0.563cm"}

                1.  
                    ![](./ObjectReplacements/Object 1191){width="2.244cm"
                    height="0.467cm"}
                2.  ![](./ObjectReplacements/Object 1192){width="3.328cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 1193){width="2.612cm"
                    height="0.467cm"}
                4.  ![](./ObjectReplacements/Object 1194){width="2.101cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 1195){width="1.549cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 1170){width="1.016cm"
                    height="0.467cm"}

        23. Definición:![](./ObjectReplacements/Object 1136){width="10.456cm"
            height="0.9cm"}

        24. ![](./ObjectReplacements/Object 1138){width="7.08cm"
            height="0.577cm"}.

        25. Definición:![](./ObjectReplacements/Object 1137){width="12.307cm"
            height="0.834cm"}

        26. ![](./ObjectReplacements/Object 1157){width="7.641cm"
            height="0.577cm"}

        27. Definición![](./ObjectReplacements/Object 1159){width="5.756cm"
            height="0.667cm"}

        28. ![](./ObjectReplacements/Object 1173){width="5.8cm"
            height="0.587cm"}

        29. Definición![](./ObjectReplacements/Object 1160){width="5.794cm"
            height="0.667cm"}

        30. ![](./ObjectReplacements/Object 1174){width="5.856cm"
            height="0.587cm"}

        31. Definición![](./ObjectReplacements/Object 1199){width="8.594cm"
            height="0.651cm"}

        32. Definición$$x,{y \in}\mspace{72mu}{x \geq y}\qquad\Rightarrow\qquad\left\lbrack {x,y} \right)_{}{: = {\{{{z \in} \mid {y \leq {z \land x} \geq {z \land z} \neq y}}\}}}$$

        33. Definición![](./ObjectReplacements/Object 1197){width="9.744cm"
            height="0.651cm"}

        34. Definición![](./ObjectReplacements/Object 1198){width="10.926cm"
            height="0.661cm"}

        35. ![](./ObjectReplacements/Object 1168){width="5.341cm"
            height="0.667cm"}

        36. ![](./ObjectReplacements/Object 1169){width="5.343cm"
            height="0.667cm"}

        37. ![](./ObjectReplacements/Object 1104){width="5.36cm"
            height="0.667cm"}

        38. ![](./ObjectReplacements/Object 1171){width="9.825cm"
            height="0.667cm"}

        39. ![](./ObjectReplacements/Object 1172){width="10.021cm"
            height="0.667cm"}

        40. Definición![](./ObjectReplacements/Object 1161){width="5.463cm"
            height="0.661cm"}

        41. Definición![](./ObjectReplacements/Object 1162){width="5.911cm"
            height="0.661cm"}

        42. ![](./ObjectReplacements/Object 1163){width="4.934cm"
            height="0.61cm"}

        43. Definición
            ![](./ObjectReplacements/Object 1175){width="5.914cm"
            height="0.681cm"}

        44. ![](./ObjectReplacements/Object 1178){width="1.496cm"
            height="0.624cm"}Pues es un álgebra de cardinal mayor o
            igual que
            ![](./ObjectReplacements/Object 1307){width="0.413cm"
            height="0.467cm"} y existe al
            menos![](./ObjectReplacements/Object 1141){width="0.743cm"
            height="0.492cm"}.

        45. ![](./ObjectReplacements/Object 1176){width="3.574cm"
            height="0.624cm"}

        46. ![](./ObjectReplacements/Object 1117){width="11.675cm"
            height="0.905cm"}

            1.  Prueba:
            2.  ![](./ObjectReplacements/Object 1179){width="4.128cm"
                height="0.487cm"}
            3.  ![](./ObjectReplacements/Object 1185){width="6.025cm"
                height="0.467cm"}
            4.  ![](./ObjectReplacements/Object 1181){width="11.499cm"
                height="0.575cm"}
            5.  ![](./ObjectReplacements/Object 1106){width="11.411cm"
                height="0.575cm"}
            6.  ![](./ObjectReplacements/Object 1107){width="6.064cm"
                height="0.547cm"}
            7.  ![](./ObjectReplacements/Object 1108){width="4.207cm"
                height="0.905cm"}
            8.  ![](./ObjectReplacements/Object 1109){width="2.023cm"
                height="0.905cm"}
            9.  ![](./ObjectReplacements/Object 1110){width="2.42cm"
                height="0.905cm"}
            10. ![](./ObjectReplacements/Object 1111){width="2.498cm"
                height="0.905cm"}
            11. ![](./ObjectReplacements/Object 1118){width="3.833cm"
                height="0.905cm"}
            12. ![](./ObjectReplacements/Object 1112){width="1.894cm"
                height="0.587cm"}
            13. ![](./ObjectReplacements/Object 1113){width="5.63cm"
                height="0.905cm"}
            14. ![](./ObjectReplacements/Object 1114){width="4.283cm"
                height="0.905cm"}
            15. ![](./ObjectReplacements/Object 1115){width="4.785cm"
                height="0.905cm"}
            16. ![](./ObjectReplacements/Object 1119){width="7.093cm"
                height="0.905cm"}
            17. ![](./ObjectReplacements/Object 1116){width="9.987cm"
                height="0.905cm"}

        47. ![](./ObjectReplacements/Object 1120){width="4.657cm"
            height="0.563cm"} Desde 57 es inmediato.

        48.  Ahora vamos a construir una función inyectiva del álgebra
            de Boole de las partes de los átomos de
            ![](./ObjectReplacements/Object 1308){width="0.51cm"
            height="0.563cm"} (si este es finito) en el álgebra de Boole
            ![](./ObjectReplacements/Object 1309){width="0.51cm"
            height="0.563cm"}. Así cuando menos sa­bremos que podemos
            interpretar esta álgebra de las partes de un conjunto de los
            áto­mos de
            ![](./ObjectReplacements/Object 1310){width="0.51cm"
            height="0.563cm"} como un subálgebra de la que estamos
            estudiando.

            La función
            ![](./ObjectReplacements/Object 1121){width="0.471cm"
            height="0.319cm"}que vamos a definir va a quedar
            completamente definida en la fór­mula que sigue. Tendremos
            que mostrar que está bien definida, que es inyectiva, que
            ![](./ObjectReplacements/Object 1122){width="4.032cm"
            height="0.506cm"}, esto es que respeta la suma booleana en
            ![](./ObjectReplacements/Object 1123){width="0.51cm"
            height="0.563cm"}que viene como unión de conjuntos
            desde![](./ObjectReplacements/Object 1124){width="2.538cm"
            height="0.639cm"},
            que![](./ObjectReplacements/Object 1125){width="3.879cm"
            height="0.506cm"}, esto es que respeta el producto booleano
            en![](./ObjectReplacements/Object 195){width="0.51cm"
            height="0.563cm"}que viene como intersección de conjun­tos
            desde![](./ObjectReplacements/Object 1127){width="2.538cm"
            height="0.639cm"}, y aunque ya no sería necesario, también
            veremos
            que![](./ObjectReplacements/Object 1128){width="4.038cm"
            height="0.639cm"}. Así quedará clara la relación entre ambas
            álgebras.

            1.  ![](./ObjectReplacements/Object 1093){width="11.557cm"
                height="6.468cm"}.

        49. ![](./ObjectReplacements/Object 1166){width="4.281cm"
            height="0.61cm"}Con la
            misma![](./ObjectReplacements/Object 1129){width="0.471cm"
            height="0.319cm"}anterior.

        50. ![](./ObjectReplacements/Object 1167){width="4.307cm"
            height="0.61cm"}Con la misma$$\varphi$$anterior.

        51. ![](./ObjectReplacements/Object 1165){width="5.662cm"
            height="0.563cm"}Lo mejor sería demostrar que cualquier
            cadena completa saturada de 1 a 0 tiene una longitud (número
            de elementos) siempre igual
            al![](./ObjectReplacements/Object 1131){width="2.103cm"
            height="0.577cm"}. De ahí se sigue que si el cardinal es el
            dicho, tendríamos más de 3 niveles, diferenciándose siempre
            los átomos y los hiperátomos.

        52. Para cada uno de los cardinales de
            ![](./ObjectReplacements/Object 49){width="0.51cm"
            height="0.563cm"}, cuando son finitos, existe una estructura
            no solo de anillo conmutativo con unidad como en 34, sino
            también de cuerpo. La po­demos encontrar explícitamente en el
            álgebra de las partes de un conjunto finito. Sólo nos queda
            ver que
            ![](./ObjectReplacements/Object 1132){width="0.471cm"
            height="0.319cm"}es sobreyectivo. Tenemos
            que![](./ObjectReplacements/Object 1133){width="3.027cm"
            height="0.639cm"}. Así
            ![](./ObjectReplacements/Object 1134){width="0.471cm"
            height="0.319cm"}pasa a ser un isomorfismo de álgebras de
            Boole: esto es, en lo que a la estructu­ra de álgebra de
            Boole se refiere, haciendo abstracción de las
            operaciones![](./ObjectReplacements/Object 1139){width="0.492cm"
            height="0.467cm"}y
            ![](./ObjectReplacements/Object 1135){width="0.445cm"
            height="0.467cm"}concretas y los elementos
            concretos,![](./ObjectReplacements/Object 1140){width="8.954cm"
            height="0.637cm"}.

        53. De 74 se deduce que si
            ![](./ObjectReplacements/Object 1607){width="0.51cm"
            height="0.563cm"}es un conjunto
            finito,![](./ObjectReplacements/Object 1608){width="3.004cm"
            height="0.563cm"}.

        54. Estructuras respectivas a 35 de espacio vectorial
            de![](./ObjectReplacements/Object 76){width="1.445cm"
            height="0.577cm"}sobre el cuerpo
            ![](./ObjectReplacements/Object 77){width="1.647cm"
            height="0.577cm"}y el dual de
            ![](./ObjectReplacements/Object 78){width="1.445cm"
            height="0.577cm"}sobre el cuerpo
            dual![](./ObjectReplacements/Object 79){width="1.803cm"
            height="0.577cm"}. Éste último es el caso
            cuando![](./ObjectReplacements/Object 188){width="2.514cm"
            height="0.61cm"}. Esto tendrá utilidad inmediata en los
            códigos de Hamming.

        55. Para calcular los inversos en los cuerpos finitos de
            cardinal![](./ObjectReplacements/Object 1609){width="0.577cm"
            height="0.527cm"}correspondientes hay que re­solver algunas
            ecuaciones sobre igualdades polinómicas. El producto del
            cuerpo fi­nito asociado (en número de elementos) a nuestro
            álgebra de Boole no es en general igual al producto del
            ani­llo booleano asociado. Tiene que ver con los cuerpos de
            Galois![](./ObjectReplacements/Object 50){width="1.48cm"
            height="0.557cm"}. Estos cuerpos y los polinomios
            mencionados son de gran utilidad en teoría de codificación.

        56. Existen formulas sencillas para poner la suma
            "![](./ObjectReplacements/Object 51){width="0.492cm"
            height="0.467cm"}", el producto
            "![](./ObjectReplacements/Object 52){width="0.445cm"
            height="0.467cm"}" en fun­ción de las funciones
            "![](./ObjectReplacements/Object 53){width="0.572cm"
            height="0.467cm"}" y
            "![](./ObjectReplacements/Object 54){width="0.445cm"
            height="0.467cm"}", y de
            "![](./ObjectReplacements/Object 55){width="0.573cm"
            height="0.467cm"}" y
            "![](./ObjectReplacements/Object 62){width="0.492cm"
            height="0.467cm"}":

            1.  ![](./ObjectReplacements/Object 63){width="3.665cm"
                height="0.506cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 251){width="2.928cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 252){width="6.833cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 253){width="10.791cm"
                    height="0.563cm"}
                5.  ![](./ObjectReplacements/Object 254){width="10.791cm"
                    height="0.563cm"}
                6.  ![](./ObjectReplacements/Object 255){width="11.098cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 256){width="7.303cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 257){width="6.461cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 258){width="8.177cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 259){width="4.537cm"
                    height="0.482cm"}
                11. ![](./ObjectReplacements/Object 193){width="3.635cm"
                    height="0.467cm"}

            2.  ![](./ObjectReplacements/Object 64){width="3.667cm"
                height="0.506cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 260){width="3.083cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 261){width="7.2cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 262){width="11.772cm"
                    height="0.563cm"}
                5.  ![](./ObjectReplacements/Object 263){width="11.772cm"
                    height="0.563cm"}
                6.  ![](./ObjectReplacements/Object 264){width="11.308cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 265){width="7.668cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 266){width="6.826cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 267){width="8.543cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 268){width="4.593cm"
                    height="0.482cm"}
                11. ![](./ObjectReplacements/Object 194){width="3.692cm"
                    height="0.467cm"}

        57. Si un
            anillo![](./ObjectReplacements/Object 190){width="2.379cm"
            height="0.577cm"}es tal
            que![](./ObjectReplacements/Object 189){width="2.863cm"
            height="0.563cm"}, define de manera unívoca un álgebra de
            Boole (la estructura de la que hablamos se llama un anillo
            de Boole). Esta proposición, con ser matemáticamente
            importante, la vemos aquí como sólo una curiosidad. En el
            anillo no exigimos que sea conmutativo. La conmutatividad de
            la suma está asegurada para todo anillo, y la del producto
            está asegurada con la con­dición de idempotencia impuesta a
            todos los elementos del anillo. La idempotencia de la suma
            también se deduce fácilmente de la idempotencia del
            producto. La suma lógica la establecemos
            ![](./ObjectReplacements/Object 224){width="3.517cm"
            height="0.506cm"}(como en 40.1, solo que aquí no su­ponemos
            nada sobre álgebras de Boole), mientras que el producto
            lógico lo pone­mos como idéntico al producto del anillo
            (idénticamente a lo anteriormente dicho). Nota: es
            importante darse cuenta que este anillo tendrá siempre
            divisores de cero, esto es habrá para cada elemento otro,
            distintos ambos de cero, que al multiplicarse dan cero, lo
            que impide que este anillo de Boole sea un dominio de
            integridad y por lo tanto también impide que sea cuerpo. El
            complementario, siguiendo la misma tó­nica que en 40.1, se
            define
            como![](./ObjectReplacements/Object 225){width="1.598cm"
            height="0.467cm"}. Por la idempotencia de la suma, la
            asociatividad de la suma y la existencia y unicidad de la
            suma tenemos que la doble negación es igual a la identidad.
            Sólo quedaría ver las distributividades. Cómo hasta ahora
            las demostraciones son cálculos que verifican la aserción.
            Así tenemos una forma de ir de cada álgebra de Boole a cada
            anillo de Boole, y un camino (exacta­mente el inverso), que
            nos llevaría de cada anillo de Boole a cada álgebra de
            Boole. Las álgebras de Boole y los anillos de Boole son
            categorías equivalentes. A los ca­minos los llamamos
            funtores. Daré solo un comienzo de estos teoremas:

            1.  \[Axioma R0\]
                ![](./ObjectReplacements/Object 656){width="5.964cm"
                height="0.573cm"}

            2.  \[Axioma R1\]
                ![](./ObjectReplacements/Object 655){width="6.274cm"
                height="0.573cm"}

            3.  \[Axioma R2\]
                ![](./ObjectReplacements/Object 654){width="4.429cm"
                height="0.563cm"}

            4.  \[Axioma R3\]
                ![](./ObjectReplacements/Object 653){width="4.784cm"
                height="0.61cm"}

            5.  \[Axioma R4\]
                ![](./ObjectReplacements/Object 699){width="4.955cm"
                height="0.563cm"}

            6.  \[Axioma R5\]
                ![](./ObjectReplacements/Object 700){width="5.339cm"
                height="0.573cm"}

            7.  \[Axioma R6\]
                ![](./ObjectReplacements/Object 701){width="4.173cm"
                height="0.563cm"}

            8.  \[Axioma R7\]
                ![](./ObjectReplacements/Object 765){width="4.494cm"
                height="0.563cm"}

            9.  \[Axioma R8\]
                ![](./ObjectReplacements/Object 702){width="2.778cm"
                height="0.573cm"}

            10. \[Axioma R9\]
                ![](./ObjectReplacements/Object 703){width="6.392cm"
                height="0.573cm"}

            11. \[Axioma
                R10\]![](./ObjectReplacements/Object 704){width="6.419cm"
                height="0.573cm"}

            12. \[Axioma
                BR\]![](./ObjectReplacements/Object 759){width="2.863cm"
                height="0.563cm"}

            13. ![](./ObjectReplacements/Object 648){width="11.095cm"
                height="0.669cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 657){width="3.464cm"
                    height="0.589cm"}
                3.  ![](./ObjectReplacements/Object 619){width="4.113cm"
                    height="0.721cm"}
                4.  ![](./ObjectReplacements/Object 639){width="4.113cm"
                    height="0.721cm"}
                5.  ![](./ObjectReplacements/Object 640){width="3.039cm"
                    height="0.653cm"}
                6.  ![](./ObjectReplacements/Object 641){width="1.826cm"
                    height="0.589cm"}

            14. ![](./ObjectReplacements/Object 642){width="7.895cm"
                height="0.639cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 643){width="7.151cm"
                    height="0.647cm"}
                3.  ![](./ObjectReplacements/Object 644){width="6.798cm"
                    height="0.66cm"}
                4.  ![](./ObjectReplacements/Object 645){width="6.193cm"
                    height="0.653cm"}
                5.  ![](./ObjectReplacements/Object 646){width="4.283cm"
                    height="0.596cm"}
                6.  ![](./ObjectReplacements/Object 647){width="2.048cm"
                    height="0.589cm"}

            15. ![](./ObjectReplacements/Object 649){width="4.606cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 651){width="2.856cm"
                    height="0.563cm"}
                3.  ![](./ObjectReplacements/Object 652){width="5.777cm"
                    height="0.639cm"}
                4.  ![](./ObjectReplacements/Object 658){width="5.777cm"
                    height="0.639cm"}
                5.  ![](./ObjectReplacements/Object 659){width="3.471cm"
                    height="0.563cm"}

            16. ![](./ObjectReplacements/Object 650){width="7.782cm"
                height="0.624cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 661){width="3.073cm"
                    height="0.563cm"}
                3.  ![](./ObjectReplacements/Object 662){width="4.784cm"
                    height="0.61cm"}
                4.  ![](./ObjectReplacements/Object 663){width="6.339cm"
                    height="0.61cm"}
                5.  ![](./ObjectReplacements/Object 668){width="5.579cm"
                    height="0.61cm"}
                6.  ![](./ObjectReplacements/Object 664){width="6.93cm"
                    height="0.639cm"}
                7.  ![](./ObjectReplacements/Object 665){width="4.073cm"
                    height="0.639cm"}
                8.  ![](./ObjectReplacements/Object 666){width="3.052cm"
                    height="0.563cm"}
                9.  ![](./ObjectReplacements/Object 667){width="2.461cm"
                    height="0.563cm"}

            17. ![](./ObjectReplacements/Object 660){width="10.62cm"
                height="0.637cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 670){width="3.455cm"
                    height="0.589cm"}
                3.  ![](./ObjectReplacements/Object 671){width="2.872cm"
                    height="0.589cm"}
                4.  ![](./ObjectReplacements/Object 672){width="1.843cm"
                    height="0.531cm"}
                5.  ![](./ObjectReplacements/Object 673){width="1.252cm"
                    height="0.531cm"}

            18. ![](./ObjectReplacements/Object 686){width="7.811cm"
                height="0.556cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 1761){width="7.183cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 1760){width="4.576cm"
                    height="0.577cm"}

            19. ![](./ObjectReplacements/Object 675){width="7.8cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 676){width="3.604cm"
                    height="0.531cm"}
                3.  ![](./ObjectReplacements/Object 677){width="5.265cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 678){width="5.166cm"
                    height="0.563cm"}
                5.  ![](./ObjectReplacements/Object 679){width="2.208cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 674){width="1.025cm"
                    height="0.467cm"}

            20. ![](./ObjectReplacements/Object 681){width="7.638cm"
                height="0.572cm"}

                1.  1.  1.  Prueba:
                        2.  ![](./ObjectReplacements/Object 682){width="2.228cm"
                            height="0.467cm"}
                        3.  ![](./ObjectReplacements/Object 683){width="5.265cm"
                            height="0.506cm"}
                        4.  ![](./ObjectReplacements/Object 684){width="5.166cm"
                            height="0.563cm"}
                        5.  ![](./ObjectReplacements/Object 685){width="2.208cm"
                            height="0.467cm"}
                        6.  ![](./ObjectReplacements/Object 680){width="1.025cm"
                            height="0.467cm"}

            21. ![](./ObjectReplacements/Object 687){width="6.712cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 689){width="2.348cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 690){width="3.655cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 691){width="3.649cm"
                    height="0.575cm"}
                5.  ![](./ObjectReplacements/Object 692){width="2.217cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 688){width="1.626cm"
                    height="0.467cm"}

            22. ![](./ObjectReplacements/Object 694){width="6.712cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 695){width="2.351cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 696){width="3.649cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 697){width="3.655cm"
                    height="0.575cm"}
                5.  ![](./ObjectReplacements/Object 698){width="2.217cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 693){width="1.626cm"
                    height="0.467cm"}

            23. ![](./ObjectReplacements/Object 714){width="5.36cm"
                height="0.601cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 716){width="2.171cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 717){width="2.175cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 715){width="2.171cm"
                    height="0.519cm"}
                5.  ![](./ObjectReplacements/Object 718){width="2.159cm"
                    height="0.575cm"}

            24. ![](./ObjectReplacements/Object 669){width="3.267cm"
                height="0.519cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 706){width="2.155cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 707){width="2.722cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 708){width="1.563cm"
                    height="0.519cm"}

            25. ![](./ObjectReplacements/Object 720){width="4.565cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 721){width="1.99cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 722){width="2.933cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 723){width="2.321cm"
                    height="0.519cm"}
                5.  ![](./ObjectReplacements/Object 724){width="1.485cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 725){width="0.785cm"
                    height="0.467cm"}
                7.  ![](./ObjectReplacements/Object 726){width="3.395cm"
                    height="0.519cm"}
                8.  ![](./ObjectReplacements/Object 727){width="1.612cm"
                    height="0.519cm"}

            26. ![](./ObjectReplacements/Object 719){width="4.57cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 729){width="1.993cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 730){width="2.933cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 731){width="2.321cm"
                    height="0.519cm"}
                5.  ![](./ObjectReplacements/Object 732){width="1.485cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 733){width="0.785cm"
                    height="0.467cm"}
                7.  ![](./ObjectReplacements/Object 734){width="3.39cm"
                    height="0.519cm"}
                8.  ![](./ObjectReplacements/Object 728){width="1.612cm"
                    height="0.519cm"}

            27. ![](./ObjectReplacements/Object 741){width="6.881cm"
                height="0.601cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 742){width="3.258cm"
                    height="0.575cm"}
                3.  ![](./ObjectReplacements/Object 751){width="2.859cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 744){width="1.529cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 745){width="0.774cm"
                    height="0.467cm"}

            28. ![](./ObjectReplacements/Object 746){width="6.876cm"
                height="0.601cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 747){width="3.258cm"
                    height="0.575cm"}
                3.  ![](./ObjectReplacements/Object 748){width="2.995cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 749){width="1.496cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 750){width="0.774cm"
                    height="0.467cm"}

            29. ![](./ObjectReplacements/Object 743){width="6.676cm"
                height="0.573cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 752){width="4.399cm"
                    height="0.575cm"}
                3.  ![](./ObjectReplacements/Object 754){width="4.745cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 753){width="3.558cm"
                    height="0.575cm"}
                5.  ![](./ObjectReplacements/Object 756){width="2.314cm"
                    height="0.575cm"}
                6.  ![](./ObjectReplacements/Object 757){width="1.692cm"
                    height="0.519cm"}
                7.  ![](./ObjectReplacements/Object 758){width="0.774cm"
                    height="0.467cm"}

            30. ![](./ObjectReplacements/Object 705){width="5.703cm"
                height="0.573cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 709){width="2.559cm"
                    height="0.575cm"}
                3.  ![](./ObjectReplacements/Object 710){width="3.498cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 711){width="2.886cm"
                    height="0.575cm"}
                5.  ![](./ObjectReplacements/Object 712){width="1.496cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 713){width="0.774cm"
                    height="0.467cm"}

            31. ![](./ObjectReplacements/Object 735){width="4.341cm"
                height="0.572cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 737){width="6.817cm"
                    height="0.573cm"}
                3.  ![](./ObjectReplacements/Object 738){width="6.495cm"
                    height="0.573cm"}
                4.  ![](./ObjectReplacements/Object 739){width="2.205cm"
                    height="0.467cm"}

            32. ![](./ObjectReplacements/Object 760){width="4.568cm"
                height="0.572cm"}

            33. ![](./ObjectReplacements/Object 793){width="10.278cm"
                height="0.482cm"}

            34. ![](./ObjectReplacements/Object 736){width="5.754cm"
                height="0.573cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 740){width="1.695cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 766){width="2.304cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 767){width="1.351cm"
                    height="0.519cm"}

            35. ![](./ObjectReplacements/Object 755){width="8.066cm"
                height="0.693cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 768){width="4.847cm"
                    height="0.693cm"}
                3.  ![](./ObjectReplacements/Object 769){width="2.939cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 770){width="1.316cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 771){width="0.97cm"
                    height="0.467cm"}

            36. ![](./ObjectReplacements/Object 773){width="8.066cm"
                height="0.693cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 774){width="4.847cm"
                    height="0.693cm"}
                3.  ![](./ObjectReplacements/Object 775){width="1.535cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 1762){width="1.321cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 1763){width="1.669cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 776){width="1.316cm"
                    height="0.467cm"}
                7.  ![](./ObjectReplacements/Object 772){width="0.97cm"
                    height="0.467cm"}

            37. ![](./ObjectReplacements/Object 867){width="7.96cm"
                height="0.601cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 877){width="4.29cm"
                    height="0.575cm"}
                3.  ![](./ObjectReplacements/Object 878){width="4.949cm"
                    height="0.704cm"}
                4.  ![](./ObjectReplacements/Object 879){width="3.42cm"
                    height="0.637cm"}
                5.  ![](./ObjectReplacements/Object 880){width="2.559cm"
                    height="0.575cm"}
                6.  ![](./ObjectReplacements/Object 881){width="0.774cm"
                    height="0.467cm"}

            Esta fórmula que acabamos de exponer es la fórmula universal
            para el inverso en cualquier grupo, o in­cluso, para
            cualquier operación con neutro asociativa, siempre que
            existan los inversos, tanto el total como los individuales.

            38. ![](./ObjectReplacements/Object 761){width="6.308cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 762){width="2.247cm"
                    height="0.575cm"}
                3.  ![](./ObjectReplacements/Object 763){width="2.928cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 764){width="4.106cm"
                    height="0.575cm"}
                5.  ![](./ObjectReplacements/Object 777){width="2.551cm"
                    height="0.519cm"}
                6.  ![](./ObjectReplacements/Object 778){width="2.245cm"
                    height="0.575cm"}
                7.  ![](./ObjectReplacements/Object 788){width="3.441cm"
                    height="0.519cm"}
                8.  ![](./ObjectReplacements/Object 789){width="6.431cm"
                    height="0.575cm"}
                9.  ![](./ObjectReplacements/Object 779){width="2.288cm"
                    height="0.467cm"}

            El grupo aditivo de un anillo con unidad multiplicativa por
            ambos lados es siempre un grupo abeliano.

            39. ![](./ObjectReplacements/Object 780){width="5.166cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 781){width="2.175cm"
                    height="0.519cm"}
                3.  ![](./ObjectReplacements/Object 782){width="3.364cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 783){width="2.223cm"
                    height="0.519cm"}
                5.  ![](./ObjectReplacements/Object 784){width="1.609cm"
                    height="0.467cm"}

            En el grupo aditivo de un anillo booleano
            ![](./ObjectReplacements/Object 786){width="0.51cm"
            height="0.563cm"} es siempre
            ![](./ObjectReplacements/Object 785){width="1.582cm"
            height="0.519cm"}.

            40. ![](./ObjectReplacements/Object 799){width="5.387cm"
                height="0.563cm"}

            41. ![](./ObjectReplacements/Object 787){width="4.937cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 802){width="1.154cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 803){width="2.332cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 804){width="2.215cm"
                    height="0.527cm"}
                5.  ![](./ObjectReplacements/Object 805){width="1.739cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 806){width="0.774cm"
                    height="0.467cm"}

            42. ![](./ObjectReplacements/Object 800){width="7.832cm"
                height="0.573cm"}

            43. ![](./ObjectReplacements/Object 790){width="5.846cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 791){width="8.243cm"
                    height="0.57cm"}
                3.  ![](./ObjectReplacements/Object 792){width="3.113cm"
                    height="0.57cm"}
                4.  ![](./ObjectReplacements/Object 794){width="2.441cm"
                    height="0.482cm"}
                5.  ![](./ObjectReplacements/Object 795){width="3.976cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 796){width="2.332cm"
                    height="0.467cm"}
                7.  ![](./ObjectReplacements/Object 797){width="2.14cm"
                    height="0.467cm"}
                8.  ![](./ObjectReplacements/Object 798){width="1.82cm"
                    height="0.467cm"}

            La operación multiplicativa de un anillo de Boole
            ![](./ObjectReplacements/Object 801){width="0.51cm"
            height="0.563cm"} es siempre abeliana. Un anillo de Boole es
            una subcategoría de la categoría de los anillos
            conmutativos.

            44. ![](./ObjectReplacements/Object 808){width="4.958cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 809){width="1.154cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 810){width="2.332cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 811){width="2.215cm"
                    height="0.527cm"}
                5.  ![](./ObjectReplacements/Object 812){width="1.739cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 813){width="0.774cm"
                    height="0.467cm"}

            45. ![](./ObjectReplacements/Object 816){width="5.159cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 817){width="1.388cm"
                    height="0.467cm"}
                3.  $${} = {x\oplus\left( {x\oplus 1} \right)} = {}$$
                4.  ![](./ObjectReplacements/Object 819){width="2.565cm"
                    height="0.519cm"}
                5.  ![](./ObjectReplacements/Object 820){width="1.709cm"
                    height="0.467cm"}
                6.  ![](./ObjectReplacements/Object 815){width="0.764cm"
                    height="0.467cm"}

            46. ![](./ObjectReplacements/Object 822){width="5.085cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 823){width="1.309cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 825){width="3.212cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 828){width="1.709cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 821){width="0.764cm"
                    height="0.467cm"}

            47. ![](./ObjectReplacements/Object 827){width="5.105cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 829){width="1.307cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 831){width="3.21cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 832){width="1.73cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 826){width="0.785cm"
                    height="0.467cm"}

            48. ![](./ObjectReplacements/Object 830){width="5.096cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 833){width="1.307cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 834){width="3.434cm"
                    height="0.575cm"}
                4.  ![](./ObjectReplacements/Object 835){width="1.73cm"
                    height="0.467cm"}
                5.  ![](./ObjectReplacements/Object 824){width="0.785cm"
                    height="0.467cm"}

            49. ![](./ObjectReplacements/Object 836){width="6.16cm"
                height="0.563cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 837){width="1.341cm"
                    height="0.467cm"}
                3.  ![](./ObjectReplacements/Object 838){width="3.267cm"
                    height="0.519cm"}
                4.  ![](./ObjectReplacements/Object 839){width="3.267cm"
                    height="0.519cm"}
                5.  ![](./ObjectReplacements/Object 840){width="1.341cm"
                    height="0.467cm"}

            50. ![](./ObjectReplacements/Object 842){width="8.25cm"
                height="0.573cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 846){width="2.909cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 847){width="3.812cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 848){width="7.982cm"
                    height="0.506cm"}
                5.  ![](./ObjectReplacements/Object 849){width="7.451cm"
                    height="0.506cm"}
                6.  ![](./ObjectReplacements/Object 850){width="2.872cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 851){width="4.646cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 852){width="7.347cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 853){width="4.65cm"
                    height="0.482cm"}
                10. ![](./ObjectReplacements/Object 854){width="7.451cm"
                    height="0.506cm"}
                11. ![](./ObjectReplacements/Object 855){width="4.727cm"
                    height="0.563cm"}

            51. ![](./ObjectReplacements/Object 843){width="8.661cm"
                height="0.577cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 845){width="2.755cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 856){width="3.658cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 857){width="4.293cm"
                    height="0.506cm"}
                5.  ![](./ObjectReplacements/Object 858){width="3.351cm"
                    height="0.506cm"}
                6.  ![](./ObjectReplacements/Object 859){width="4.293cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 860){width="7.731cm"
                    height="0.482cm"}

            52. ![](./ObjectReplacements/Object 844){width="8.83cm"
                height="0.577cm"}

                1.  Prueba:
                2.  ![](./ObjectReplacements/Object 861){width="2.755cm"
                    height="0.506cm"}
                3.  ![](./ObjectReplacements/Object 863){width="2.328cm"
                    height="0.506cm"}
                4.  ![](./ObjectReplacements/Object 864){width="4.63cm"
                    height="0.506cm"}
                5.  ![](./ObjectReplacements/Object 865){width="3.706cm"
                    height="0.506cm"}
                6.  ![](./ObjectReplacements/Object 866){width="3.505cm"
                    height="0.506cm"}
                7.  ![](./ObjectReplacements/Object 862){width="6.366cm"
                    height="0.506cm"}
                8.  ![](./ObjectReplacements/Object 868){width="12.575cm"
                    height="0.506cm"}
                9.  ![](./ObjectReplacements/Object 869){width="11.155cm"
                    height="0.506cm"}
                10. ![](./ObjectReplacements/Object 870){width="13.995cm"
                    height="0.506cm"}
                11. ![](./ObjectReplacements/Object 871){width="11.367cm"
                    height="0.467cm"}
                12. ![](./ObjectReplacements/Object 872){width="9.998cm"
                    height="0.467cm"}
                13. ![](./ObjectReplacements/Object 873){width="8.11cm"
                    height="0.467cm"}
                14. ![](./ObjectReplacements/Object 876){width="5.419cm"
                    height="0.467cm"}
                15. ![](./ObjectReplacements/Object 874){width="3.463cm"
                    height="0.467cm"}
                16. ![](./ObjectReplacements/Object 875){width="3.6cm"
                    height="0.519cm"}
                17. ![](./ObjectReplacements/Object 841){width="7.731cm"
                    height="0.482cm"}

    2.  Estudio de las funciones booleanas, sobre álgebras de Boole
        finitas.

        1.  Estudiaremos sólo las
            funciones![](./ObjectReplacements/Object 65){width="1.729cm"
            height="0.563cm"}dónde![](./ObjectReplacements/Object 66){width="2.514cm"
            height="0.61cm"}. Esto
            es![](./ObjectReplacements/Object 67){width="1.984cm"
            height="0.61cm"}.
        2.  Formas normales. Toda
            función![](./ObjectReplacements/Object 80){width="1.984cm"
            height="0.61cm"}se puede poner en la
            forma![](./ObjectReplacements/Object 81){width="6.232cm"
            height="1.177cm"}dónde
            ![](./ObjectReplacements/Object 1313){width="3.175cm"
            height="0.506cm"}.
        3.  En general, el número de funciones de un
            conjunto![](./ObjectReplacements/Object 29){width="0.506cm"
            height="0.467cm"}de
            cardinal![](./ObjectReplacements/Object 30){width="1.272cm"
            height="0.531cm"}en un
            conjunto![](./ObjectReplacements/Object 31){width="0.547cm"
            height="0.467cm"}de
            cardinal![](./ObjectReplacements/Object 89){width="1.295cm"
            height="0.531cm"}será![](./ObjectReplacements/Object 90){width="0.87cm"
            height="0.598cm"}. Así una función
            de![](./ObjectReplacements/Object 95){width="0.422cm"
            height="0.467cm"}variables en
            ![](./ObjectReplacements/Object 91){width="0.506cm"
            height="0.467cm"}con valores en
            ![](./ObjectReplacements/Object 92){width="0.547cm"
            height="0.467cm"}será![](./ObjectReplacements/Object 93){width="1.131cm"
            height="0.633cm"}. Para el caso en
            que![](./ObjectReplacements/Object 94){width="1.993cm"
            height="0.61cm"}que toma como
            argumento![](./ObjectReplacements/Object 96){width="0.422cm"
            height="0.467cm"} variables, obtenemos que el número de
            funciones será
            de![](./ObjectReplacements/Object 97){width="0.944cm"
            height="0.676cm"}. En una pequeña tabla vemos como crece
            esta cantidad:

  --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------
  ![](./ObjectReplacements/Object 99){width="0.564cm" height="0.467cm"} variables   Número de funciones distintas: ![](./ObjectReplacements/Object 98){width="0.967cm" height="0.656cm"}
  0                                                                                 2
  1                                                                                 4
  2                                                                                 16
  3                                                                                 256
  4                                                                                 65536
  5                                                                                 4294967296
  6                                                                                 18446744073709551616
  7                                                                                 340282366920938463463374607431768211456
  --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------

39. 1.  1.  El punto anterior es fácil de probar:

            1.  Para el caso
                de![](./ObjectReplacements/Object 100){width="1.122cm"
                height="0.467cm"}y
                de![](./ObjectReplacements/Object 101){width="1.109cm"
                height="0.467cm"}es fácil probar (por enumeración) la
                vali­dez de la fórmula. Más tarde mostraremos tablas de
                todas las funciones hasta
                ![](./ObjectReplacements/Object 102){width="1.111cm"
                height="0.467cm"}inclusive.

            2.  Para el caso general, la Hipótesis de Inducción será
                :![](./ObjectReplacements/Object 103){width="12.017cm"
                height="0.686cm"}

            3.  Veremos si para el
                caso![](./ObjectReplacements/Object 104){width="1.12cm"
                height="0.467cm"}se sigue cumpliendo la fórmula
                anterior. Pero esto es claro: al añadir una variable en
                el argumento tendremos todas las funcio­nes del
                caso![](./ObjectReplacements/Object 106){width="1.683cm"
                height="0.467cm"}:![](./ObjectReplacements/Object 107){width="1.205cm"
                height="0.557cm"}para el
                valor![](./ObjectReplacements/Object 108){width="0.422cm"
                height="0.467cm"}de la nueva variable y
                otros![](./ObjectReplacements/Object 109){width="1.205cm"
                height="0.557cm"}para el
                valor![](./ObjectReplacements/Object 110){width="0.411cm"
                height="0.467cm"}de la nueva variable, y no quedan otros
                casos. Las funciones totales
                para![](./ObjectReplacements/Object 111){width="1.12cm"
                height="0.467cm"}serán :

                1.  ![](./ObjectReplacements/Object 440){width="12.033cm"
                    height="0.7cm"}
                2.  ![](./ObjectReplacements/Object 441){width="13.714cm"
                    height="0.7cm"}
                3.  ![](./ObjectReplacements/Object 442){width="9.216cm"
                    height="0.686cm"}

Y así queda establecida la fórmula.

40. 1.  1.  Como se ve en el punto anterior, el crecimiento es
            desmesurado al compararlo al crecimiento lineal de los
            argumentos. En un futuro, cuan­do intentemos hacer
            reducciones de expresiones booleanas, este crecimiento nos
            im­pedirá construir métodos eficaces para resolver las
            minimizaciones.

        2.  Aunque hemos visto que podemos poner las expresiones
            booleanas en los conjuntos de
            operadores![](./ObjectReplacements/Object 112){width="6.078cm"
            height="0.492cm"}, por comprensibilidad y para una lectura
            normal se utilizan frecuentemente los dos primeros conjuntos
            unidos, pu­diendo variarse bien el orden de los operadores
            binarios:![](./ObjectReplacements/Object 113){width="3.551cm"
            height="0.506cm"}. El primer conjunto
            ![](./ObjectReplacements/Object 114){width="1.647cm"
            height="0.506cm"}será el que estudiemos por defecto, el
            segundo se tratará con una simetría de dualidad (hay que
            tener algunos cuidados). El conjunto elegido de operaciones
            se llamará desarrollo en sumas de productos de términos
            simples (una variable, o su negada, o una constante).
            También se llamará desarrollo por minitérminos o SOP
            (inglés) o SdP. El segundo será el desarrollo en producto de
            sumas de términos simples (una variable, o su negada, o una
            constante). También se llamará desarrollo por maxitérminos o
            POS (inglés) o PdS.

        3.  En el desarrollo por minitérminos expresamos sólo los
            términos de la expresión en que la función tiene como
            valor![](./ObjectReplacements/Object 115){width="0.411cm"
            height="0.467cm"}. Veamos:

        4.  ![](./ObjectReplacements/Object 116){width="12.857cm"
            height="1.207cm"}

            ![](./ObjectReplacements/Object 226){width="6.817cm"
            height="0.603cm"}

        5.  Para más sencillez:

            ![](./ObjectReplacements/Object 117){width="13.78cm"
            height="1.125cm"}![](./ObjectReplacements/Object 227){width="10.149cm"
            height="0.54cm"}

        6.  Cuándo la sigma (el minitérmino) es en todos los casos (para
            todas las iotas) completo (es un producto
            de![](./ObjectReplacements/Object 807){width="3.708cm"
            height="0.467cm"}), el valor de la función en esa iota
            concreta indica si el minitérmino aparece o no.

        7.  En el desarrollo por maxitérminos de una función
            de![](./ObjectReplacements/Object 883){width="0.448cm"
            height="0.467cm"}variables, los
            ![](./ObjectReplacements/Object 882){width="2.612cm"
            height="0.467cm"}son sumatorios
            de![](./ObjectReplacements/Object 814){width="3.708cm"
            height="0.467cm"}. Así termina consis­tiendo la función en un
            producto de maxitérminos. Los maxitérminos indican un
            ![](./ObjectReplacements/Object 884){width="0.422cm"
            height="0.467cm"}de la función.

        8.  Además de expresar las funciones por cadenas de símbolos que
            constituyen un térmi­no, existe una posibilidad de expresar
            estas funciones por tablas lineales o por cua­dros (tablas
            bidimensionales). Para cada combinación de valores booleanos
            a la en­trada de una función obtenemos un valor booleano de
            salida.

        9.  Para que las funciones booleanas representen algo de interés
            para la ingeniería, lo primero que debemos tener es una
            forma de representar la información que queremos procesar.
            ¿Cómo representamos un número?. ¿Cómo una letra?. Haremos un
            alto en la exposición de funciones booleanas, para detallar
            más esta pregunta, poder respon­derla y así ver para qué
            estamos viendo las álgebras de Boole.

41. Representación de la información.

    1.  Un alfabeto es un conjunto de valores diferentes que podemos
        aplicar para represen­tar información. En el sentido que nosotros
        lo utilizamos el alfabeto de la escritura en español no solo se
        compone de las letras del abecedario, digamos en minúsculas,
        sino además, de otro conjunto similar pero en mayúsculas. A esto
        hay que añadir todos los signos de puntuación en párrafos.
        Además hay que añadir todas las vocales que son susceptibles de
        tener tilde o diéresis, además, el guion para separar las
        palabras en dos y por último un elemento muy frecuente que suele
        pasar desapercibido: el espa­cio en blanco. Por último los
        guarismos de los números del 0 al 9. Si consideramos los números
        naturales estos guarismos son un alfabeto de los números
        naturales. Como vemos los alfabetos tienen la común propiedad de
        ser finitos. Para los núme­ros naturales (como para cualquier
        otra cosa que representar) basta con
        ![](./ObjectReplacements/Object 201){width="1.984cm"
        height="0.681cm"} .
    2.  Para nosotros un lenguaje sobre un alfabeto será un conjunto,
        donde los elementos serán ristras de letras de ese alfabeto. Una
        ristra de letras (una ristra finita) de ese al­fabeto no tiene
        porqué pertenecer al lenguaje. Por ejemplo, podemos establecer
        un lenguaje de los números naturales sobre un alfabeto
        cualquiera. Si es sobre el
        alfabe­to![](./ObjectReplacements/Object 228){width="0.672cm"
        height="0.681cm"}, de cardinal 2, diremos que una palabra de
        nuestro lenguaje es bien un 0 o bien un 1 seguido de una ristra
        finita cualquiera de 0s y 1s (formalmente se suele re­presentar
        como![](./ObjectReplacements/Object 229){width="3.055cm"
        height="0.593cm"}, dónde
        \'![](./ObjectReplacements/Object 230){width="0.445cm"
        height="0.467cm"}\' quiere decir seguido o conca­tenado, y
        \'\'![](./ObjectReplacements/Object 231){width="0.975cm"
        height="0.542cm"}\'\' quiere decir una ristra de letras de
        dentro del paréntesis, con la única condición que sea finita, y
        que puede ser vacía).
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
        auto-complementario Aitken), códigos con distancias sucesivas 1
        (para longitud fija) (códigos continuos), códigos continuos con
        distancia 1 entre el primer elemento y el último elemento o
        circulares. Códigos especulares. Si son circulares y especulares
        se llaman códigos Gray (de una determinada longitud fija).
        Códigos con redundancia de infor­mación, entre los que destacan
        los códigos Hamming.

Podéis ver que en los códigos antes explicitados y sus propiedades hacen
referencia necesaria a algo más que al conjunto de las palabras de un
lenguaje, que se puede re­sumir en un orden en las palabras. Esto viene
dado normalmente por el significado de las palabras.

42. 1.  Hemos hablado de alfabetos, lenguajes sobre un alfabeto y
        después sobre el orden sobre esas palabras. Si llamamos a las
        reglas que cumplen las palabras de un lenguaje respecto a un
        alfabeto la gramática de ese lenguaje, el último elemento, el
        del orden, o más en general los significados, son la semántica.

    2.  En 3 hablamos de un lenguaje de los números naturales sobre un
        alfabeto![](./ObjectReplacements/Object 232){width="0.672cm"
        height="0.681cm"}. En general: ¿qué número significa 1001? ¿y el
        1011101?. A qué valor natural apunta cada cadena es algo
        exterior al léxico y su gramática. Vamos a construir una
        semánti­ca: llamamos en una cadena de letras del alfabeto
        ![](./ObjectReplacements/Object 233){width="2.018cm"
        height="0.601cm"}a
        ![](./ObjectReplacements/Object 234){width="0.496cm"
        height="0.601cm"}el dígito me­nos significativo
        (el![](./ObjectReplacements/Object 351){width="0.734cm"
        height="0.467cm"}) y
        al![](./ObjectReplacements/Object 235){width="0.938cm"
        height="0.601cm"}el dígito más significativo
        (el![](./ObjectReplacements/Object 885){width="0.965cm"
        height="0.467cm"}). Pri­mero asignamos unos valores naturales a
        los del
        alfabeto![](./ObjectReplacements/Object 236){width="4.036cm"
        height="1.348cm"}, y según el
        subíndice![](./ObjectReplacements/Object 238){width="0.448cm"
        height="0.467cm"}de la
        letra![](./ObjectReplacements/Object 239){width="0.515cm"
        height="0.601cm"}obtenemos el
        valor![](./ObjectReplacements/Object 237){width="1.935cm"
        height="0.7cm"}para esa letra en ese lugar concreto. Así el
        valor de una palabra de nuestro código
        será![](./ObjectReplacements/Object 240){width="2.639cm"
        height="1.139cm"}. Más en general si
        ![](./ObjectReplacements/Object 269){width="0.711cm"
        height="0.617cm"}es un alfabeto de
        cardinal![](./ObjectReplacements/Object 270){width="0.448cm"
        height="0.467cm"}, esto es, desde los dígitos
        ![](./ObjectReplacements/Object 271){width="3.96cm"
        height="0.663cm"}y establecemos la
        función![](./ObjectReplacements/Object 272){width="3.542cm"
        height="0.617cm"}, el valor de una palabra del lenguaje
        (código)![](./ObjectReplacements/Object 273){width="2.522cm"
        height="0.7cm"}será![](./ObjectReplacements/Object 274){width="4.551cm"
        height="1.162cm"}, y
        ![](./ObjectReplacements/Object 275){width="0.868cm"
        height="0.506cm"}es la longitud de la
        representación![](./ObjectReplacements/Object 276){width="0.392cm"
        height="0.467cm"}. Este tipo de representación es la más usada
        en el ámbito de los números desde hace seiscientos o setecientos
        años más o menos en Occidente, sólo que para base 10 (diez
        dígitos distintos). Nosotros usaremos también bastante la base
        2, código que llamamos habitualmente binario natural.

    3.  Aquí es conveniente tener claro cómo pasamos de una base a otra.
        En general lo ha­cemos por pasos:

        1.  Paso de una
            base![](./ObjectReplacements/Object 277){width="0.487cm"
            height="0.467cm"}a
            base![](./ObjectReplacements/Object 278){width="0.628cm"
            height="0.467cm"}. Esto lo hacemos por aplicación directa de
            la fórmula expresada anteriormente en 2.6.

        2.  Paso de
            base![](./ObjectReplacements/Object 280){width="0.628cm"
            height="0.467cm"}a una
            base![](./ObjectReplacements/Object 279){width="0.487cm"
            height="0.467cm"}. Esto se hace por el proceso inverso al
            ante­rior, dividimos sucesivamente por
            ![](./ObjectReplacements/Object 311){width="0.487cm"
            height="0.467cm"}los cocientes y nos vamos quedando con los
            restos, dónde los primeros son los dígitos de más bajo peso,
            y los últimos los de más alto. El proceso termina
            naturalmente cuando el cociente a dividir es más pequeño que
            la base![](./ObjectReplacements/Object 312){width="0.487cm"
            height="0.467cm"}, cociente que pasa a ser el dígito
            ![](./ObjectReplacements/Object 313){width="0.926cm"
            height="0.467cm"}de la conver­sión.

        3.  Paso de una
            base![](./ObjectReplacements/Object 281){width="0.614cm"
            height="0.531cm"}a una base
            ![](./ObjectReplacements/Object 282){width="0.616cm"
            height="0.531cm"}:

            1.  Caso
                que![](./ObjectReplacements/Object 283){width="1.96cm"
                height="0.591cm"}. Cada dígito
                de![](./ObjectReplacements/Object 284){width="0.614cm"
                height="0.531cm"}lo desarrollamos como su
                co­rrespondiente
                en![](./ObjectReplacements/Object 285){width="0.466cm"
                height="0.467cm"}dígitos de
                base![](./ObjectReplacements/Object 286){width="0.616cm"
                height="0.531cm"}(sin ahorrar los 0 a la izquierda). Así
                hemos terminado.
            2.  Caso
                que![](./ObjectReplacements/Object 287){width="1.939cm"
                height="0.591cm"}. Comenzando por el
                ![](./ObjectReplacements/Object 288){width="0.714cm"
                height="0.467cm"}(el más a la derecha) agrupamos los
                dígitos
                de![](./ObjectReplacements/Object 290){width="1.155cm"
                height="0.467cm"}dígitos
                de![](./ObjectReplacements/Object 289){width="0.614cm"
                height="0.531cm"}. Cada grupo
                de![](./ObjectReplacements/Object 291){width="0.43cm"
                height="0.467cm"}dí­gitos
                de![](./ObjectReplacements/Object 292){width="0.614cm"
                height="0.531cm"}es exactamente un dígito
                de![](./ObjectReplacements/Object 293){width="0.616cm"
                height="0.531cm"}, hacemos así la sustitución predicha y
                hemos terminado. El único posible problema es el grupo
                de![](./ObjectReplacements/Object 296){width="0.43cm"
                height="0.467cm"}dígitos más alto, en el caso que tenga
                entre![](./ObjectReplacements/Object 294){width="0.411cm"
                height="0.467cm"}y![](./ObjectReplacements/Object 295){width="0.993cm"
                height="0.467cm"}dígitos. Ese grupo se rellena
                con![](./ObjectReplacements/Object 297){width="0.573cm"
                height="0.531cm"}(el que representa
                a![](./ObjectReplacements/Object 298){width="0.422cm"
                height="0.467cm"}) por la izquierda hasta completar la
                longitud![](./ObjectReplacements/Object 299){width="0.43cm"
                height="0.467cm"}.
            3.  Caso
                que![](./ObjectReplacements/Object 300){width="4.688cm"
                height="0.591cm"}. Lo dividimos en dos pasos: pasamos
                primero![](./ObjectReplacements/Object 301){width="0.614cm"
                height="0.531cm"}a![](./ObjectReplacements/Object 302){width="0.624cm"
                height="0.591cm"}y entonces
                de![](./ObjectReplacements/Object 303){width="1.842cm"
                height="0.591cm"}a![](./ObjectReplacements/Object 304){width="0.616cm"
                height="0.531cm"}.
            4.  Caso en que no hay una relación
                entre![](./ObjectReplacements/Object 310){width="0.614cm"
                height="0.531cm"}y![](./ObjectReplacements/Object 309){width="0.616cm"
                height="0.531cm"}de las anteriores. Enton­ces pasamos de
                base![](./ObjectReplacements/Object 308){width="0.614cm"
                height="0.531cm"}a
                base![](./ObjectReplacements/Object 307){width="0.628cm"
                height="0.467cm"}, y entonces de
                base![](./ObjectReplacements/Object 306){width="0.628cm"
                height="0.467cm"}a![](./ObjectReplacements/Object 305){width="0.616cm"
                height="0.531cm"}. Este método es general, pero el
                anterior es más eficiente para los casos espe­cificados.

    4.  Para describir letras, esto es, caracteres alfabéticos de la
        lengua natural, utilizamos generalmente el código ASCII (de 7
        bits el estándar original o de 8 dígitos binarios o bits, el
        extendido de Microsoft). Existen otros códigos, como el EBCDIC
        de IBM y las implementaciones UTF8, UTF16 y UTF32 de Unicode.
        Permiten sobradamente trasladar los lenguajes naturales escritos
        a un alfabeto binario.

    5.  El conjunto de los naturales es insuficiente para muchas
        aplicaciones. La primera ampliación es el
        conjunto![](./ObjectReplacements/Object 314){width="0.559cm"
        height="0.385cm"}de los enteros. Las formas de representar
        números enteros es variada pero la vamos a resumir en tres
        formas:

        1.  Magnitud y Signo
            (![](./ObjectReplacements/Object 629){width="1.291cm"
            height="0.467cm"}). Representamos el valor absoluto del
            número como un número en binario natural y le añadimos
            un![](./ObjectReplacements/Object 318){width="0.422cm"
            height="0.467cm"}o
            un![](./ObjectReplacements/Object 319){width="0.411cm"
            height="0.467cm"}en
            el![](./ObjectReplacements/Object 317){width="0.926cm"
            height="0.467cm"}, dónde
            el![](./ObjectReplacements/Object 320){width="0.422cm"
            height="0.467cm"}representa el signo
            "![](./ObjectReplacements/Object 316){width="0.554cm"
            height="0.467cm"}" y
            el![](./ObjectReplacements/Object 321){width="0.411cm"
            height="0.467cm"}representa el signo
            "![](./ObjectReplacements/Object 315){width="0.492cm"
            height="0.467cm"}". Este lenguaje sería en
            general![](./ObjectReplacements/Object 633){width="6.932cm"
            height="0.84cm"}, habida cuenta
            que![](./ObjectReplacements/Object 323){width="1.55cm"
            height="0.617cm"}. Esta es una traducción directa de lo que
            hacemos cuando escribimos un número entero con signo. En
            general tenemos 2 representa­ciones para el número 0.

        2.  En Complemento a la base
            ![](./ObjectReplacements/Object 1314){width="0.487cm"
            height="0.467cm"}(![](./ObjectReplacements/Object 630){width="0.963cm"
            height="0.467cm"}). En este método de representación tene­mos
            una forma de representar los números positivos y otra los
            negativos. Los nú­meros positivos (incluido el
            ![](./ObjectReplacements/Object 324){width="0.607cm"
            height="0.601cm"}de
            valor![](./ObjectReplacements/Object 325){width="0.422cm"
            height="0.467cm"}) se representan de forma idéntica a como
            se hace
            en![](./ObjectReplacements/Object 204){width="1.291cm"
            height="0.467cm"}. La novedad está en los números negativos,
            cuyo ![](./ObjectReplacements/Object 326){width="0.926cm"
            height="0.467cm"}es![](./ObjectReplacements/Object 327){width="0.411cm"
            height="0.467cm"}, seguido de un dígito cualquiera distinto
            del más alto
            ![](./ObjectReplacements/Object 328){width="1.438cm"
            height="0.601cm"}y seguido de una ristra finita cualquiera
            de dígitos.

            1.  Primero introduciremos una operación, la complementación
                de dígitos que designaremos como un operador
                prefijo![](./ObjectReplacements/Object 329){width="1.207cm"
                height="0.601cm"}, de forma que dada una ris­tra
                cualquiera sobre un
                alfabeto![](./ObjectReplacements/Object 330){width="0.711cm"
                height="0.617cm"}, formalmente el
                lenguaje![](./ObjectReplacements/Object 331){width="1.549cm"
                height="0.838cm"}, que definimos como:

                ![](./ObjectReplacements/Object 322){width="8.211cm"
                height="0.665cm"}

                ![](./ObjectReplacements/Object 631){width="8.243cm"
                height="0.72cm"}

                ![](./ObjectReplacements/Object 632){width="6.608cm"
                height="0.639cm"}![](./ObjectReplacements/Object 634){width="12.95cm"
                height="0.723cm"}

            Otra forma de llamar a esta operación es complemento a la
            base menos uno. Permite hacer operaciones sin ningún tipo de
            acarreo, dígito a dígito sin de­pendencias de la posición.
            Algunas propiedades de esta operación son:

            ![](./ObjectReplacements/Object 333){width="6.156cm"
            height="0.723cm"}

            ![](./ObjectReplacements/Object 334){width="10.312cm"
            height="0.734cm"}

            Esta operación es interesante porque nos va a permitir
            definir la complementa­ción a la base
            ![](./ObjectReplacements/Object 335){width="0.496cm"
            height="0.321cm"} de forma sencilla:

            ![](./ObjectReplacements/Object 336){width="8.885cm"
            height="0.762cm"}

            Las propiedades de esta complementación son:

            ![](./ObjectReplacements/Object 338){width="4.731cm"
            height="0.617cm"}

            ![](./ObjectReplacements/Object 337){width="9.28cm"
            height="0.734cm"}

            2.  Ahora ya podemos saber como interpretar los números
                negativos en represen­tación
                ![](./ObjectReplacements/Object 196){width="0.963cm"
                height="0.467cm"}. El
                ![](./ObjectReplacements/Object 339){width="0.926cm"
                height="0.467cm"}será![](./ObjectReplacements/Object 340){width="0.411cm"
                height="0.467cm"}, a continuación no tendremos un
                dígito![](./ObjectReplacements/Object 341){width="1.064cm"
                height="0.601cm"}, sino cualquier otro, y una ristra
                finita cualquiera de dígitos sobre el
                alfabeto![](./ObjectReplacements/Object 342){width="0.711cm"
                height="0.617cm"}. Para cualquier palabra sobre el
                alfabeto dicho definimos el valor en Complemento a la
                base![](./ObjectReplacements/Object 1315){width="0.487cm"
                height="0.467cm"}con 1 y con 0.

                ![](./ObjectReplacements/Object 332){width="7.461cm"
                height="0.838cm"}

                ![](./ObjectReplacements/Object 635){width="6.137cm"
                height="1.309cm"}

                ![](./ObjectReplacements/Object 636){width="0.466cm"
                height="0.467cm"}

                ![](./ObjectReplacements/Object 637){width="5.046cm"
                height="1.309cm"}

            3.  Ahora nos disponemos a representar el lenguaje de las
                representaciones ente­ras
                en![](./ObjectReplacements/Object 886){width="0.979cm"
                height="0.467cm"}, y podemos ver bien que valores
                tienen:

            ![](./ObjectReplacements/Object 344){width="9.342cm"
            height="0.85cm"}

            ![](./ObjectReplacements/Object 345){width="8.821cm"
            height="0.85cm"}

            ![](./ObjectReplacements/Object 346){width="5.796cm"
            height="0.661cm"}

            ![](./ObjectReplacements/Object 347){width="10.051cm"
            height="1.566cm"}

            Y así queda definido el lenguaje de las representaciones en
            complemento a una base y su semántica de valores
            en![](./ObjectReplacements/Object 348){width="0.557cm"
            height="0.385cm"}.

        3.  Exceso a![](./ObjectReplacements/Object 349){width="0.422cm"
            height="0.467cm"}. Este tipo de representación no necesita
            signo siendo, el valor de la representación su valor en
            binario natural
            menos![](./ObjectReplacements/Object 350){width="0.422cm"
            height="0.467cm"}. La representación
            ![](./ObjectReplacements/Object 352){width="0.422cm"
            height="0.467cm"}tiene como
            valor![](./ObjectReplacements/Object 353){width="0.774cm"
            height="0.467cm"}. En general el valor de la
            representación![](./ObjectReplacements/Object 355){width="0.392cm"
            height="0.467cm"}en Exceso a
            ![](./ObjectReplacements/Object 354){width="0.422cm"
            height="0.467cm"}será![](./ObjectReplacements/Object 356){width="1.549cm"
            height="0.506cm"}, siendo la
            función![](./ObjectReplacements/Object 887){width="1.706cm"
            height="0.467cm"}la correspondiente al bina­rio natural.

        4.  La siguiente ampliación
            es![](./ObjectReplacements/Object 357){width="0.52cm"
            height="0.385cm"}. Existen de entrada dos formas comunes de
            repre­sentación: en punto fijo y en punto flotante.

        5.  En punto fijo tendremos siempre que saber dónde se encuentra
            el punto o coma deci­mal, conociendo cual es la longitud de
            la parte fraccionaria
            (![](./ObjectReplacements/Object 358){width="1.219cm"
            height="0.697cm"}) y cual la de la parte entera
            (![](./ObjectReplacements/Object 359){width="1.325cm"
            height="0.61cm"}). Hasta el momento solo hemos utilizado
            ![](./ObjectReplacements/Object 360){width="3.256cm"
            height="0.829cm"}dónde![](./ObjectReplacements/Object 361){width="1.563cm"
            height="0.697cm"}.

        6.  Representaciones de binario natural en punto fijo. Vamos a
            ver, en un primer mo­mento, estas representaciones solo si
            son positivas, esto es, representaciones de
            ![](./ObjectReplacements/Object 362){width="0.741cm"
            height="0.568cm"}en binario natural, que será la base para
            el resto de representaciones más com­plejas. En principio la
            parte entera vendrá dada por una expresión del
            tipo![](./ObjectReplacements/Object 363){width="3.604cm"
            height="0.76cm"},![](./ObjectReplacements/Object 365){width="3.313cm"
            height="0.61cm"},![](./ObjectReplacements/Object 364){width="3.244cm"
            height="0.887cm"},![](./ObjectReplacements/Object 366){width="0.824cm"
            height="0.467cm"},![](./ObjectReplacements/Object 368){width="7.832cm"
            height="0.887cm"}y![](./ObjectReplacements/Object 367){width="3.256cm"
            height="0.829cm"}. Para evaluar el valor de la
            representación la fórmula es la
            clásica![](./ObjectReplacements/Object 369){width="3.874cm"
            height="1.307cm"}. En general aunque ponemos explícita­mente
            el punto, no es necesario una vez se conocen las longitudes
            de las partes entera y fraccionaria.

        7.  El siguiente paso es ¿cómo pasamos un número en punto fijo
            de una base a otra?. Para esto lo más sencillo es separar el
            número en punto fijo en dos partes, la entera y la
            fraccionaria. La parte entera, un número natural, seguirá
            siendo entera en cualquier base, por lo que aplicamos las
            reglas de conversión que ya conocemos para n-ario na­tural,
            ya vistas.

        ¿Y la parte fraccionaria?. También sigue siendo un número
        ![](./ObjectReplacements/Object 105){width="1.499cm"
        height="0.538cm"}para cualquier base, y en cualquier base sigue
        representándose como una cadena de­trás del punto fijo. A partir
        de ahora la
        representación![](./ObjectReplacements/Object 443){width="0.392cm"
        height="0.467cm"}, representará siempre la parte fraccionaria,
        esto es![](./ObjectReplacements/Object 444){width="2.351cm"
        height="0.506cm"}, y su representación será siempre tal que
        confundiremos
        ![](./ObjectReplacements/Object 445){width="0.392cm"
        height="0.467cm"}con
        ![](./ObjectReplacements/Object 446){width="0.803cm"
        height="0.467cm"}y![](./ObjectReplacements/Object 447){width="3.748cm"
        height="0.663cm"}. Veremos los distintos ca­sos:

        8.  Casos en que existe una relación
            entre![](./ObjectReplacements/Object 448){width="0.714cm"
            height="0.635cm"}y![](./ObjectReplacements/Object 450){width="0.716cm"
            height="0.635cm"}tal
            que![](./ObjectReplacements/Object 449){width="7.322cm"
            height="0.568cm"}. Los cambios son idénticos a los
            realizados para la parte entera excepto que los grupos de
            dígitos se cogen desde el punto decimal hacia la derecha,
            esto es, en sentido inverso al que tomábamos para los
            naturales.

        9.  Caso general. Hemos de utilizar una base intermedia, la
            habitual base
            10![](./ObjectReplacements/Object 451){width="0.905cm"
            height="0.635cm"}. El método es el mismo explicado en su
            momento para números naturales en
            ![](./ObjectReplacements/Object 343){width="2.798cm"
            height="0.467cm"}. Solo que da pues ver como pasamos de
            base![](./ObjectReplacements/Object 452){width="0.905cm"
            height="0.635cm"}a![](./ObjectReplacements/Object 453){width="0.714cm"
            height="0.635cm"}y viceversa.

            1.  El caso inmediato
                es![](./ObjectReplacements/Object 454){width="1.794cm"
                height="0.635cm"}. Utilizamos la siguiente
                fórmula:![](./ObjectReplacements/Object 457){width="4.621cm"
                height="1.319cm"}.

            2.  El caso inmediato
                es![](./ObjectReplacements/Object 455){width="1.794cm"
                height="0.635cm"}. Se trata del proceso inverso al
                anterior, esto es, como las potencias son negativas
                realizamos, en el caso anterior divi­siones sucesivas
                por![](./ObjectReplacements/Object 456){width="0.453cm"
                height="0.492cm"}, el cardinal de la base. Pro lo tanto
                el proceso que nos atañe será el de multiplicar
                sucesivamente por la
                base![](./ObjectReplacements/Object 458){width="0.453cm"
                height="0.492cm"}, el número
                fraccionario![](./ObjectReplacements/Object 459){width="1.011cm"
                height="0.492cm"}. En cada multiplicación por la base la
                parte entera será un dígito de la nueva base, y los
                obtenemos desde el primer lugar a la derecha del punto
                decimal hacia la derecha. En cada multiplicación nos
                quedamos con el resto, esto es, la parte fraccionaria
                del resultado (la parte entera ya ha sido incorporada al
                resultado final).

            3.  Podemos observar fácilmente que en los dos casos
                anteriores el procedimien­to de colocar decimales en la
                nueva base no tiene por qué ser un proceso que termine,
                esto es, finito. Es
                claro![](./ObjectReplacements/Object 460){width="0.811cm"
                height="0.467cm"}en base
                ![](./ObjectReplacements/Object 461){width="0.686cm"
                height="0.617cm"}tiene una representa­ción
                finita![](./ObjectReplacements/Object 462){width="2.193cm"
                height="0.628cm"}, pero en
                base![](./ObjectReplacements/Object 463){width="0.684cm"
                height="0.617cm"}, en binario, y en base
                ![](./ObjectReplacements/Object 464){width="0.707cm"
                height="0.492cm"}y en otras bases tenemos
                que![](./ObjectReplacements/Object 466){width="1.131cm"
                height="0.506cm"}![](./ObjectReplacements/Object 467){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 468){width="1.162cm"
                height="0.667cm"}![](./ObjectReplacements/Object 469){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 470){width="1.182cm"
                height="0.669cm"}![](./ObjectReplacements/Object 471){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 472){width="0.923cm"
                height="0.619cm"}![](./ObjectReplacements/Object 473){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 474){width="0.967cm"
                height="0.667cm"}![](./ObjectReplacements/Object 475){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 476){width="1.182cm"
                height="0.667cm"}![](./ObjectReplacements/Object 477){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 478){width="0.967cm"
                height="0.619cm"}![](./ObjectReplacements/Object 479){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 480){width="0.967cm"
                height="0.667cm"}![](./ObjectReplacements/Object 481){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 482){width="1.184cm"
                height="0.667cm"}![](./ObjectReplacements/Object 483){width="0.554cm"
                height="0.467cm"}![](./ObjectReplacements/Object 484){width="0.972cm"
                height="0.619cm"}![](./ObjectReplacements/Object 465){width="1.362cm"
                height="0.467cm"}![](./ObjectReplacements/Object 607){width="1.184cm"
                height="0.619cm"}![](./ObjectReplacements/Object 608){width="1.362cm"
                height="0.467cm"}![](./ObjectReplacements/Object 609){width="1.161cm"
                height="0.619cm"}![](./ObjectReplacements/Object 610){width="1.362cm"
                height="0.467cm"}![](./ObjectReplacements/Object 602){width="1.161cm"
                height="0.663cm"}![](./ObjectReplacements/Object 603){width="1.362cm"
                height="0.467cm"}![](./ObjectReplacements/Object 600){width="1.168cm"
                height="0.619cm"}![](./ObjectReplacements/Object 601){width="1.009cm"
                height="0.467cm"}.

                Una vez hemos utilizado la representación en binario,
                las de base 4 y la octal (base 8) son inmediatas por
                reagrupamientos. Igualmente la representación en base 3
                es inmediata ya
                que![](./ObjectReplacements/Object 485){width="2.369cm"
                height="0.631cm"}, que corresponde
                a![](./ObjectReplacements/Object 486){width="5.482cm"
                height="0.704cm"}, y confundiremos
                habitualmente![](./ObjectReplacements/Object 488){width="0.644cm"
                height="0.635cm"}con
                ![](./ObjectReplacements/Object 487){width="0.453cm"
                height="0.492cm"}y queda claro que para cualquier otra
                posición tenemos
                que![](./ObjectReplacements/Object 489){width="5.733cm"
                height="0.683cm"}. Igualmente tenemos por reagrupamien­to
                la representación para base 9.

            4.  Es importante darnos cuenta que en el caso de pasos
                entre
                ![](./ObjectReplacements/Object 496){width="0.714cm"
                height="0.635cm"}y![](./ObjectReplacements/Object 497){width="0.716cm"
                height="0.635cm"}tal que
                ![](./ObjectReplacements/Object 498){width="7.322cm"
                height="0.568cm"}, si la representación fuente es finita
                la destino también los será, y si la fuente es infinita
                con un periodo, el destino también lo será. En general
                si pasamos un número de
                base![](./ObjectReplacements/Object 604){width="0.714cm"
                height="0.635cm"}a
                base![](./ObjectReplacements/Object 605){width="1.007cm"
                height="0.635cm"}la representación seguirá guardando su
                carácter finito no periódi­co si así ocurre en
                ![](./ObjectReplacements/Object 606){width="0.714cm"
                height="0.635cm"}(como vemos al pasar de base 3 a base
                6).

            5.  Habitualmente utilizaremos el guarismo confundido con el
                dígito![](./ObjectReplacements/Object 490){width="1.046cm"
                height="0.496cm"}![](./ObjectReplacements/Object 491){width="1.487cm"
                height="0.467cm"}![](./ObjectReplacements/Object 492){width="1.55cm"
                height="0.492cm"}. Para dígitos superiores, si los
                hubiera, hay varias es­trategias. En Electrónica Digital
                se suele utilizar el alfabeto latino, sin dife­renciar
                mayúsculas de minúsculas, lo más habitual para trabajar
                en base 16
                (hexadecimal),![](./ObjectReplacements/Object 493){width="9.68cm"
                height="0.7cm"}y en general podemos utilizar más letras,
                y más letras aún de otros abecedarios (y aún distinguir
                entre mayúsculas y minúsculas, acentuarlas de diferentes
                formas e inventarnos nuevas letras-gráficos, pero en
                general no es solución general del problema). Una
                solución general es utilizar cadenas que conten­gan el
                índice del dígito correspondiente en base 10
                (comprensible para todos) en una cadena que exprese la
                base en la que nos encontramos
                con![](./ObjectReplacements/Object 494){width="6.535cm"
                height="0.639cm"}, que es la solución que hemos adop­tado
                en el
                programa![](./ObjectReplacements/Object 495){width="1.87cm"
                height="0.467cm"}que podéis disponer para hacer
                conversio­nes etc en cualquier base. En este programa (en
                realidad un conjunto de clases del lenguaje de
                programación C++), además de representar y operar con
                dígi­tos de cualquier base, podemos representar y operar
                con números naturales en cualquier base
                (representación![](./ObjectReplacements/Object 599){width="2.798cm"
                height="0.467cm"}) y con números enteros de cualquier
                base (representación interna
                en![](./ObjectReplacements/Object 597){width="0.963cm"
                height="0.467cm"}). Los naturales los repre­sentamos
                como![](./ObjectReplacements/Object 595){width="10.236cm"
                height="0.67cm"}y los enteros por defecto entran y salen
                como
                en![](./ObjectReplacements/Object 596){width="0.963cm"
                height="0.467cm"}. Hay algunas facili­dades para sacar
                los números enteros en pantalla
                en![](./ObjectReplacements/Object 598){width="1.291cm"
                height="0.467cm"}.

            6.  Por lo demás es fácil conseguir la representación de la
                parte fraccionaria
                en![](./ObjectReplacements/Object 611){width="0.963cm"
                height="0.467cm"}si ésta es negativa. Se realizan las
                operaciones de la misma forma que la hacíamos con la
                parte entera, solo que allí teníamos en cuenta la
                longi­tud de la representación, pero aquí, para la parte
                fraccionaria el complemento lo conseguimos básicamente
                con el complemento de la parte fraccionaria a la
                unidad![](./ObjectReplacements/Object 612){width="2.185cm"
                height="0.492cm"}.

    6.  El último tipo de representación que vamos a ver es la
        representación en punto flo­tante
        (![](./ObjectReplacements/Object 888){width="2.524cm"
        height="0.467cm"}, de forma que en C, C++ al tipo de números con
        decimales que habitualmente llamamos reales, toman el nombre de
        su forma de representación :
        ![](./ObjectReplacements/Object 889){width="1.021cm"
        height="0.467cm"}). Este tipo está estandarizado y tenemos un
        documento que lo detalla bastante bien. Este tipo tiene ventajas
        (relativas) con respecto al punto fijo porque amplía bastante el
        rango de valores a representar con el mismo número de dígitos, y
        porque se controla el error de representación en forma
        proporcional al valor absoluto del número, esto es, trabajamos
        con errores relativos, mientras en punto fijo se trabaja con
        errores absolutos que son fijos en todo el rango de
        representaciones. Como parte negativa hay que decir que los
        circuitos para trabajar con punto flotante son más complejos y
        voluminosos que los que teníamos para punto fijo, que eran los
        mismos circuitos que teníamos para trabajar con enteros.

    7.  Siguiendo con los códigos que utilizamos en Electrónica Digital,
        los más comunes son los códigos o lenguajes que tienen una
        longitud fija. Por ver un poco la noción de longitud, ésta
        determina básicamente la cantidad de valores de diferentes, de
        palabras diferentes que puede tener el lenguaje. Si trabajamos
        con el
        lenguaje![](./ObjectReplacements/Object 617){width="0.457cm"
        height="0.492cm"}sobre el
        alfabeto![](./ObjectReplacements/Object 616){width="0.482cm"
        height="0.492cm"}, definiremos:

        ![](./ObjectReplacements/Object 615){width="3.607cm"
        height="0.603cm"}

        ![](./ObjectReplacements/Object 618){width="4.263cm"
        height="0.603cm"}

        ![](./ObjectReplacements/Object 638){width="7.336cm"
        height="0.61cm"}

        ![](./ObjectReplacements/Object 614){width="7.176cm"
        height="0.61cm"}

        ![](./ObjectReplacements/Object 620){width="9.938cm"
        height="0.64cm"}

        A este último lo suelo llamar código saturado de
        longitud![](./ObjectReplacements/Object 621){width="0.453cm"
        height="0.492cm"}sobre el
        alfabeto![](./ObjectReplacements/Object 622){width="0.482cm"
        height="0.492cm"}, y será la referencia para los distintos
        códigos de longitud fija. Para un código de este tipo el número
        de palabras máximo permitido
        será![](./ObjectReplacements/Object 623){width="1.235cm"
        height="0.633cm"}. Si trabajamos en binario natural de longitud
        fija![](./ObjectReplacements/Object 624){width="0.453cm"
        height="0.492cm"}, representaremos desde
        el![](./ObjectReplacements/Object 626){width="0.453cm"
        height="0.492cm"}al![](./ObjectReplacements/Object 625){width="1.251cm"
        height="0.594cm"}.

    8.  Por ejemplo, el código
        ![](./ObjectReplacements/Object 890){width="3.092cm"
        height="0.492cm"}está dentro
        de![](./ObjectReplacements/Object 891){width="1.505cm"
        height="0.774cm"}, pero no son idénticos. Enumeraré los valores
        en una tabla de dos columnas:

  ![](./ObjectReplacements/Object 892){width="3.092cm" height="0.492cm"}   ![](./ObjectReplacements/Object 893){width="1.505cm" height="0.774cm"}
  ------------------------------------------------------------------------ ------------------------------------------------------------------------
  0000                                                                     0000
  0001                                                                     0001
  0010                                                                     0010
  0011                                                                     0011
  0100                                                                     0100
  0101                                                                     0101
  0110                                                                     0110
  0111                                                                     0111
  1000                                                                     1000
  1001                                                                     1001
  \-\-\--                                                                  1010
  \-\-\--                                                                  1011
  \-\-\--                                                                  1100
  \-\-\--                                                                  1101
  \-\-\--                                                                  1110
  \-\-\--                                                                  1111

43. 1.  Los códigos![](./ObjectReplacements/Object 894){width="0.961cm"
        height="0.492cm"}son códigos de longitud fija, por lo general 4,
        pero lo fundamen­tal es que remedan en binario el
        alfabeto![](./ObjectReplacements/Object 895){width="2.503cm"
        height="0.635cm"}. Dependiendo de la finali­dad hay varios: el
        más sencillo el que acabamos de dar.
        El![](./ObjectReplacements/Object 896){width="3.739cm"
        height="0.492cm"}, es de longitud 4, pero con el 0 en 0011 y el
        9 en 1100. Comprobaréis fácilmente que es un código dónde el
        ![](./ObjectReplacements/Object 897){width="1.946cm"
        height="0.676cm"}coincide con la negación lógica bit a bit. Esto
        fa­cilita el hacer operaciones directamente
        en![](./ObjectReplacements/Object 898){width="0.905cm"
        height="0.635cm"}. El
        código![](./ObjectReplacements/Object 899){width="2.85cm"
        height="0.492cm"}, es un código auto-complementario como el
        anterior pero además mantiene un sistema de pesos 2-4-2-1, en
        orden con su valores decimales sería:

        ![](./ObjectReplacements/Object 900){width="11.098cm"
        height="1.048cm"}

    2.  Otro tipo de códigos son los códigos continuos y los cíclicos.
        Decimos que un código es continuo si entre una palabra y la
        siguiente en el orden propio (valor semántico o significado)
        solo varía un dígito. Además es cíclico si entre la primera
        palabra y la última varía a su vez un solo bit. Para casos con
        más de dos valores en el alfabeto ha­bría que afinar la
        definición, pero para el caso que nos ocupa, que es el código
        Gray de ![](./ObjectReplacements/Object 901){width="1.397cm"
        height="0.467cm"}basta con lo dicho y los ejemplos que a
        continuación se van a dar. Estos códigos son además códigos
        reflejados, esto es, se obtienen por un sistema especular. Para
        un solo bit sería:

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

        ![](./ObjectReplacements/Object 902){width="2.469cm"
        height="3.995cm"}

        Para 4 bits sería:

        ![](./ObjectReplacements/Object 903){width="3.101cm"
        height="8.027cm"}

        Y así sucesivamente.

    3.  Los códigos biquinarios (el 2 entre 5 en concreto, entre los
        muchos biquinarios que de hecho se han utilizado), es un código
        que mantiene el número de 1s en cada pala­bra del código que
        tiene longitud constante 5. Además proviene de un código
        ponde­rado, pero tal como lo ponemos aquí ya no lo es:

        ![](./ObjectReplacements/Object 904){width="10.142cm"
        height="0.506cm"}

        ![](./ObjectReplacements/Object 905){width="10.098cm"
        height="0.506cm"}

        Proviene del siguiente, que es ponderado, de 7 bits de longitud,
        y ponderación
        ![](./ObjectReplacements/Object 908){width="3.854cm"
        height="0.467cm"}:

        ![](./ObjectReplacements/Object 907){width="12.137cm"
        height="0.506cm"}

        ![](./ObjectReplacements/Object 906){width="12.365cm"
        height="0.506cm"}

    4.  El siguiente y último código es el Johnson (Johnson-Möbius) de 5
        bits de longitud, que es un código continuo y progresivo, pero
        que puede ser de longitud fija
        de![](./ObjectReplacements/Object 913){width="0.453cm"
        height="0.492cm"}, con una capacidad de
        ![](./ObjectReplacements/Object 914){width="0.843cm"
        height="0.492cm"}valores distintos, así el de 5 bits es
        apropiado para re­presentar
        un![](./ObjectReplacements/Object 915){width="2.738cm"
        height="0.492cm"}, y es apropiado para tratamiento muy rápido de
        la in­formación mediante registros de desplazamientos y otros
        dispositivos:

        ![](./ObjectReplacements/Object 909){width="10.072cm"
        height="0.506cm"}

        ![](./ObjectReplacements/Object 911){width="9.97cm"
        height="0.506cm"}

44. Tratamiento del error en códigos de longitud fija.

    1.  Utilizaremos en principio varios métodos para esta finalidad:
        códigos Reed-Solomon, códigos lineales de grupo (dentro de estos
        se encuentran los códigos Hamming), códi­gos Golay, distintos
        bits de paridad, códigos de
        repetición![](./ObjectReplacements/Object 1001){width="1.48cm"
        height="0.519cm"}u otros, códigos CRC, y de suma igual. En
        general: en unos detectamos un error y devolvemos una peti­ción
        de reenvío o similar, en otros cubrimos los casos más
        importantes y probables y la detección y corrección ha de ser
        autónoma por el receptor. Es importante saber que es lo que
        suele pasar cuando hay una comunicación de tramas de bits:

        1.  Tenemos un Emisor y un Receptor de mensaje, que comparten un
            protocolo común de actuación además del alfabeto básico y el
            código a utilizar.

        2.  Entre el Emisor y el Receptor tenemos un Medio: una Línea de
            transmisión, sea esta cableada o no.

        3.  El Medio/Línea es ruidoso: existe la probabilidad que se
            cambien uno símbolos de alfabeto por otros, obteniendo así
            una palabra del código válida o no. Si la palabra re­cibida
            en el Emisor es recibida con cambios que no la convierten en
            una palabra prohibida (no del código común), el error pasará
            desapercibido. Por otra parte si per­cibimos como Receptor un
            error podremos bien corregirlo, bien no.

        4.  Suposiciones varias que hacen el tratamiento de errores
            manejable (suposiciones ra­zonables).

            1.  La longitud de la palabra enviada permanece inalterable.
                No se pierden bits por el trayecto: se transmutarán en
                otros pero no seguirá siendo
                un![](./ObjectReplacements/Object 916){width="1.939cm"
                height="0.467cm"}.
            2.  La probabilidad de error será pequeña, esto
                es![](./ObjectReplacements/Object 917){width="3.918cm"
                height="0.54cm"}, aunque de hecho no importaría esta
                otra
                situación![](./ObjectReplacements/Object 918){width="3.907cm"
                height="0.54cm"}, caso en que cambiamos 1s por 0s y
                viceversa, y cambiamos la probabilidad
                por![](./ObjectReplacements/Object 919){width="4.48cm"
                height="0.54cm"}. El problema grave aparece
                cuando![](./ObjectReplacements/Object 920){width="5.36cm"
                height="0.556cm"}con
                ![](./ObjectReplacements/Object 921){width="2.17cm"
                height="0.482cm"}(por poner un límite real­mente
                permisivo. Así permitimos
                que![](./ObjectReplacements/Object 922){width="5.639cm"
                height="0.54cm"}, y por la reducción vista antes tenemos
                que![](./ObjectReplacements/Object 923){width="3.859cm"
                height="0.54cm"}. Con un error de
                ![](./ObjectReplacements/Object 924){width="0.951cm"
                height="0.467cm"}el sistema es plenamente aleatorio. No
                hay absolutamente nada que hacer.
            3.  El error en un bit ha de ser independiente de los que
                hay alrededor. Esto es a ve­ces claramente no realista.
                La idea es que en una palabra
                recibida,![](./ObjectReplacements/Object 925){width="2.76cm"
                height="0.531cm"}dados
                ![](./ObjectReplacements/Object 926){width="8.594cm"
                height="0.54cm"}.
            4.  Por la suposición 2 y 3, dada la palabra que se
                envía![](./ObjectReplacements/Object 927){width="2.76cm"
                height="0.531cm"}, tene­mos entonces
                que![](./ObjectReplacements/Object 928){width="2.574cm"
                height="0.482cm"}, tal que
                para![](./ObjectReplacements/Object 929){width="3.298cm"
                height="0.467cm"}entonces![](./ObjectReplacements/Object 930){width="2.709cm"
                height="0.54cm"}, y
                así![](./ObjectReplacements/Object 931){width="6.115cm"
                height="0.591cm"}. En
                general![](./ObjectReplacements/Object 932){width="4.637cm"
                height="0.591cm"}.
            5.  La probabilidad de error sobre un valor 0 o un valor 1
                ha de ser muy parecida, de forma que la asimetría sea
                inapreciable.

        5.  Hay varios conceptos importantes en cuanto a los errores: el
            de distancia Hamming y el de paridad.

        6.  En un código de longitud fija, digamos
            un![](./ObjectReplacements/Object 933){width="1.972cm"
            height="0.492cm"}, la distancia Hamming en­tre dos palabras
            de
            longitud![](./ObjectReplacements/Object 934){width="0.453cm"
            height="0.492cm"}sobre un
            alfabeto![](./ObjectReplacements/Object 935){width="0.482cm"
            height="0.492cm"}, digamos
            ![](./ObjectReplacements/Object 936){width="2.589cm"
            height="0.591cm"}y
            ![](./ObjectReplacements/Object 937){width="2.591cm"
            height="0.591cm"}, definimos:

            ![](./ObjectReplacements/Object 938){width="6.473cm"
            height="0.826cm"}

            En palabras es el número de bits que son diferentes entre
            amabas palabras (posición por posición).

        7.  La función definida anteriormente, formalmente,
            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}:L^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{}_{2}} \right) \times L^{\mathtt{\mathrm{n}}}}{\left( \mathtt{\mathrm{}_{2}} \right)\rightarrow{\lbrack{0,n}\rbrack} \subset {\mathbb{N}} \subset {\mathbb{R}}}::\left( \mathtt{\mathrm{a}\mathrm{,}\mathrm{b}} \right)@\mathit{card}\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$es
            una distancia bien definida matemáticamente, la distancia
            entre dos palabras iguales es siempre 0, y si son distintas
            es necesariamente distinta de 0. Siempre es un número mayor
            o igual que 0 como corresponde a un cardinal de un conjunto.
            Además es si­métrica, esto es, la distancia entre dos
            palabras
            ![](./ObjectReplacements/Object 940){width="1.478cm"
            height="0.492cm"} es idéntica a la distancia
            ![](./ObjectReplacements/Object 941){width="1.478cm"
            height="0.492cm"}. Por último se cumple la desigualdad
            triangular, para tres palabras
            cuales­quiera![](./ObjectReplacements/Object 942){width="3.179cm"
            height="0.693cm"}la distancia Hamming
            cumple![](./ObjectReplacements/Object 943){width="5.442cm"
            height="0.616cm"}. Estas tres propiedades pueden verse que
            normales entre las distancias euclidianas normales. De hecho
            esta distancia nos habilita para ver una geometría
            en![](./ObjectReplacements/Object 944){width="2.198cm"
            height="0.693cm"}, dónde podemos poner como puntos
            los![](./ObjectReplacements/Object 945){width="2.441cm"
            height="0.467cm"}o bien
            los![](./ObjectReplacements/Object 946){width="2.512cm"
            height="0.467cm"}, en general, a estos, vistos desde el
            pris­ma geométrico, se les
            llama![](./ObjectReplacements/Object 947){width="1.792cm"
            height="0.467cm"}.

        8.  Para un código cualquiera de longitud fija definimos ahora
            el concepto
            de![](./ObjectReplacements/Object 948){width="6.096cm"
            height="0.492cm"}, que es,
            dado![](./ObjectReplacements/Object 949){width="1.473cm"
            height="0.61cm"},![](./ObjectReplacements/Object 952){width="6.137cm"
            height="1.147cm"}. Para el lenguaje
            completo![](./ObjectReplacements/Object 950){width="2.027cm"
            height="0.676cm"}, esta distancia mínima es 1. La idea que
            sigue es muy intuitiva: si la distancia entre dos palabras
            es 0, entonces las dos palabras son en realidad la misma,
            son el mismo pun­to-palabra del espacio-código de longitud
            fija. Si las palabras son de longitud 24, 24 es la distancia
            más alejada entre dos palabras y así.

            Para determinar la distancia mínima de un
            ![](./ObjectReplacements/Object 951){width="1.972cm"
            height="0.492cm"}hay algunos trucos que nos ayudarán:

            1.  Con la primera distancia 1 que encontremos podemos dejar
                de comprobar. La distancia mínima de ese código es 1.

            2.  ![](./ObjectReplacements/Object 953){width="2.499cm"
                height="0.676cm"}.
                Si![](./ObjectReplacements/Object 954){width="1.665cm"
                height="0.527cm"}, entonces
                ![](./ObjectReplacements/Object 955){width="2.385cm"
                height="0.619cm"}.

            3.  Si![](./ObjectReplacements/Object 956){width="1.944cm"
                height="0.527cm"},
                entonces![](./ObjectReplacements/Object 957){width="2.385cm"
                height="0.619cm"}. Este resultado, tipo cota de la
                dis­tancia mínima en función del cardinal del código, se
                puede extender para distancia mínima 2, \... Por
                ejemplo![](./ObjectReplacements/Object 958){width="2.395cm"
                height="0.619cm"}entonces![](./ObjectReplacements/Object 959){width="1.522cm"
                height="0.527cm"}.

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
                ![](./ObjectReplacements/Object 960){width="3.427cm"
                height="0.676cm"}y el bit de paridad lo ponemos
                (añadimos) en la posición
                ![](./ObjectReplacements/Object 961){width="0.453cm"
                height="0.492cm"}, la fórmula
                ![](./ObjectReplacements/Object 962){width="4.819cm"
                height="0.944cm"} nos da el valor del bit de paridad
                par. El de paridad impar es exactamente el inverso del
                formulado. La ra­zón por la que la fórmula funciona es
                sencilla, si recordamos
                que![](./ObjectReplacements/Object 963){width="1.628cm"
                height="0.467cm"}y
                que![](./ObjectReplacements/Object 964){width="1.628cm"
                height="0.467cm"}. Así, para un código de un solo bit,
                el de paridad sería simple­mente la repetición del bit
                (el bit de paridad par sería simplemente del mismo va­lor
                que el ya existente). De esta forma los dos bits son
                iguales y el número de 1s será o 0 o 2, esto es, siempre
                par. Si fuese el código original de 2 bits de longitud,
                el bit de paridad debería valer 1 si solo uno de los dos
                (no los dos) valiese 1. Esto vuelve a ser la suma
                exclusiva. Y así sucesivamente.

            5.  Podemos realizar un bit de paridad par sobre los 0s de
                una palabra. Esto tiene mayor interés cuando la longitud
                de la palabra es impar. Solo hay que negar cada bit y
                utilizar la misma fórmula
                anterior:![](./ObjectReplacements/Object 965){width="4.821cm"
                height="0.944cm"}. Si la lon­gitud de la palabra es par
                podéis comprobar que es lo mismo poner que no poner
                todas las negaciones.

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
                ![](./ObjectReplacements/Object 966){width="1.155cm"
                height="0.467cm"}necesitaremos que el código sea de
                distancia
                mínima![](./ObjectReplacements/Object 967){width="0.99cm"
                height="0.467cm"}. El razonamiento es igual al expre­sado
                para errores de 1 bit. Si la distancia mínima del código
                es ![](./ObjectReplacements/Object 968){width="0.99cm"
                height="0.467cm"}entonces, en el peor caso,
                ![](./ObjectReplacements/Object 969){width="1.76cm"
                height="0.467cm"}pueden dejarnos la palabra a distancia
                1 (como míni­mo) de cualquier palabra válida del código.
                Luego podemos detectar que la pala­bra recibida no está
                en el código.

            8.  Podemos dar un paso más e intentar no solo detectar sino
                corregir el bit equivo­cado. Para esto necesitamos que la
                palabra con el bit equivocado quede de forma tal que sea
                claro desde cual palabra del código correcto se ha
                producido el error. No podremos tener dos palabras
                distintas del código a distancia mínima de la pa­labra
                equivocada, sino solamente una. La corrección
                consistiría en cambiar la pa­labra equivocada por la
                única más cercana del código. El principio de corrección
                es el máxima verosimilitud.

            9.  Para poder
                corregir![](./ObjectReplacements/Object 970){width="1.76cm"
                height="0.467cm"}necesitamos una distancia
                mínima![](./ObjectReplacements/Object 971){width="1.351cm"
                height="0.467cm"}. Para corregir un solo bit necesitamos
                una distancia mínima de tres. Esto es claro. Si la
                distancia fuera dos, al producirse el error, quedaría a
                distancia uno de más de una palabra del código. Sin
                embargo si la distancia mínima es tres, al producirse un
                error quedará a distancia 2 como mínimo de todas las
                demás palabras del códi­go. En general desde una
                palabra![](./ObjectReplacements/Object 1020){width="0.665cm"
                height="0.635cm"}se ha producido con error la
                palabra![](./ObjectReplacements/Object 1021){width="0.534cm"
                height="0.492cm"}tal
                que![](./ObjectReplacements/Object 1022){width="2.559cm"
                height="0.854cm"}. Podemos decir que la palabra errónea
                está dentro del radio de la esfera que rodea
                a![](./ObjectReplacements/Object 1023){width="0.665cm"
                height="0.635cm"}. La pregunta que surge es ¿puede
                existir una palabra
                ![](./ObjectReplacements/Object 1024){width="0.665cm"
                height="0.635cm"}con
                $$\mathtt{\mathrm{i} \neq \mathrm{j}}$$tal que
                ![](./ObjectReplacements/Object 1027){width="2.559cm"
                height="0.854cm"}?. Sabemos
                que![](./ObjectReplacements/Object 1028){width="5.803cm"
                height="0.854cm"}. Esto quiere decir, que:

                ![](./ObjectReplacements/Object 1029){width="9.851cm"
                height="0.854cm"}

                ![](./ObjectReplacements/Object 1030){width="13.591cm"
                height="1.037cm"}

                ![](./ObjectReplacements/Object 1031){width="10.557cm"
                height="0.938cm"}

                ![](./ObjectReplacements/Object 1032){width="6.433cm"
                height="0.938cm"}

                ![](./ObjectReplacements/Object 1033){width="5.528cm"
                height="0.938cm"}

                ![](./ObjectReplacements/Object 1034){width="8.163cm"
                height="0.938cm"}

                ![](./ObjectReplacements/Object 1035){width="6.428cm"
                height="0.938cm"}

                Luego la corrección será
                ![](./ObjectReplacements/Object 1036){width="1.349cm"
                height="0.635cm"}necesariamente. Siempre habrá una sola
                pala­bra de nuestro código que esté a distancia menor o
                igual
                que![](./ObjectReplacements/Object 1037){width="0.466cm"
                height="0.467cm"}, estando las de­más palabras del código
                a distancia mayor o igual
                que![](./ObjectReplacements/Object 1038){width="0.967cm"
                height="0.467cm"}.

            10. El método de construcción de detectores/correctores de
                error de Hamming es en principio el más fácil de usar,
                es el método lineal de codificación por grupo. Se trata
                de utilizar una matriz (de 0s y 1s) para convertir
                el![](./ObjectReplacements/Object 972){width="1.97cm"
                height="0.492cm"}original, en
                un![](./ObjectReplacements/Object 973){width="2.769cm"
                height="0.547cm"}. La condición principal es que la
                transformación sea inyecti­va
                y![](./ObjectReplacements/Object 988){width="5.075cm"
                height="0.746cm"}. Para esto lo fundamental es que la
                matriz de codificación (de
                dimensión![](./ObjectReplacements/Object 974){width="1.859cm"
                height="0.547cm"}) mantenga el original (con
                ![](./ObjectReplacements/Object 975){width="0.43cm"
                height="0.467cm"}colum­nas dónde el único 1 está en la
                posición
                ![](./ObjectReplacements/Object 977){width="0.944cm"
                height="0.519cm"}con![](./ObjectReplacements/Object 976){width="1.625cm"
                height="0.482cm"}), esto es, siendo un bloque matricial
                completo la matriz
                identidad![](./ObjectReplacements/Object 989){width="0.97cm"
                height="0.563cm"}, uno de los dos bloques de
                construcción de la
                matriz![](./ObjectReplacements/Object 990){width="0.453cm"
                height="0.492cm"}de codificación Hamming. El otro bloque
                lo de­notaremos
                por![](./ObjectReplacements/Object 991){width="0.974cm"
                height="0.563cm"}. Esto además lo conseguiremos si la
                matriz de decodifica­ción
                ![](./ObjectReplacements/Object 992){width="0.674cm"
                height="0.603cm"}de dimensión
                ![](./ObjectReplacements/Object 993){width="1.85cm"
                height="0.531cm"}es tal que
                ![](./ObjectReplacements/Object 994){width="3.865cm"
                height="0.908cm"}. Si el resultado de la primera
                decodificación no es cero es que hay error. Entonces, si
                llamamos
                ![](./ObjectReplacements/Object 995){width="0.534cm"
                height="0.48cm"}a la palabra recibida y
                ![](./ObjectReplacements/Object 996){width="0.466cm"
                height="0.48cm"}a la palabra enviada (siempre correcta),
                ha de existir un vector
                columna![](./ObjectReplacements/Object 997){width="1.73cm"
                height="0.515cm"}, con un único uno
                en![](./ObjectReplacements/Object 998){width="0.349cm"
                height="0.235cm"}, tal
                que![](./ObjectReplacements/Object 999){width="4.487cm"
                height="0.612cm"}. Por otra parte, condición necesaria y
                sufi­ciente para que la operación sea inyectiva es que no
                contenga columnas igua­les ni columnas vector 0.

                Ejemplo:

                Supongamos que nos llega un código de 2 bits cuyos bits
                llamaremos![](./ObjectReplacements/Object 978){width="0.954cm"
                height="0.531cm"}, a su vez los bits codificados por la
                matriz generadora
                serán![](./ObjectReplacements/Object 979){width="1.593cm"
                height="0.531cm"}. En general para poder corregir un bit
                necesitamos distancia 3: ¿cuántos bits habrá que
                añadir?. En general si queremos corregir códigos, hemos
                de añadir un número
                ![](./ObjectReplacements/Object 1039){width="0.33cm"
                height="0.467cm"}de bits a
                los![](./ObjectReplacements/Object 1040){width="0.422cm"
                height="0.467cm"}originales tal que la distancia sea
                mayor o igual
                que![](./ObjectReplacements/Object 980){width="0.418cm"
                height="0.467cm"}, y probando, tenemos
                que![](./ObjectReplacements/Object 983){width="1.094cm"
                height="0.467cm"}ya cumple. Así que la matriz de
                codificación de grupo será de
                dimensión![](./ObjectReplacements/Object 984){width="1.012cm"
                height="0.467cm"}.

                ![](./ObjectReplacements/Object 1010){width="3.33cm"
                height="0.586cm"}

$$\begin{array}{l}
{= {\begin{pmatrix}
1 & 0 \\
0 & 1 \\
a & b \\
c & d
\end{pmatrix} \cdot \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1
\end{pmatrix}} =} \\
{= \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
a & b & {a\oplus b} \\
c & d & {c\oplus d}
\end{pmatrix}}
\end{array}$$

45. 1.  1.  1.  1.  1.  1.  1.  1.  1.  

                La matriz izquierda de la primera fila es la matriz
                generadora de paridades, la de­recha son el código
                original de 4 bits en forma de una palabra por cada
                columna. Por último la matriz inferior son los vectores
                codificados con tres bits de paridad insertos. Solo
                queda ver la transformación inversa correspondiente.
                Para esto vea­mos que si observamos matriz izquierda de
                la primera
                fila![](./ObjectReplacements/Object 986){width="1.974cm"
                height="1.265cm"}. Tomare­mos como matriz decodificadora
                (no necesariamente inyectiva) a

                1.  1.  ![](./ObjectReplacements/Object 987){width="3.223cm"
                        height="0.67cm"}

                        ![](./ObjectReplacements/Object 1000){width="3.514cm"
                        height="1.074cm"}

                Ahora bien, sabemos que:

                ![](./ObjectReplacements/Object 1002){width="2.094cm"
                height="0.593cm"}

                De dónde obtenemos un sistema de ecuaciones, con estos
                resultados (distintos del resultado trivial):

                ![](./ObjectReplacements/Object 1004){width="2.872cm"
                height="1.074cm"}

                Que hace
                que$$\mathtt{\mathrm{H}} \cdot \mathtt{\mathrm{o}}$$quede
                como:

                $$\begin{pmatrix}
                1 & 0 & 1 \\
                0 & 1 & 1
                \end{pmatrix}\rightarrow\begin{pmatrix}
                1 & 0 & 1 \\
                0 & 1 & 1 \\
                a & b & {a\oplus b} \\
                c & d & {c\oplus d}
                \end{pmatrix}$$

                El sistema de ecuaciones se genera como se ve a
                continuación:

                ![](./ObjectReplacements/Object 1018){width="5.547cm"
                height="2.18cm"}

                ![](./ObjectReplacements/Object 982){width="8.916cm"
                height="1.159cm"}

                ![](./ObjectReplacements/Object 985){width="8.551cm"
                height="1.155cm"}

                $$\begin{bmatrix}
                {c = \overline{a}} & {{a \cdot b} = {\overline{a} \cdot d}} & {1\oplus{a \cdot \overline{b}}\oplus{c \cdot \overline{d}}} \\
                {{a \cdot b} = {\overline{a} \cdot d}} & {d = \overline{b}} & {1\oplus{b \cdot \overline{a}}\oplus{d \cdot \overline{c}}}
                \end{bmatrix}$$

                ![](./ObjectReplacements/Object 1017){width="6.523cm"
                height="1.067cm"}

                ![](./ObjectReplacements/Object 1019){width="5.92cm"
                height="1.124cm"}

                ![](./ObjectReplacements/Object 1041){width="6.07cm"
                height="1.067cm"}

                ![](./ObjectReplacements/Object 1042){width="7.664cm"
                height="1.556cm"}

                ![](./ObjectReplacements/Object 1043){width="2.805cm"
                height="1.074cm"}

                ![](./ObjectReplacements/Object 1044){width="3.45cm"
                height="1.074cm"}

                ![](./ObjectReplacements/Object 1045){width="2.027cm"
                height="2.18cm"}

                ![](./ObjectReplacements/Object 981){width="5.419cm"
                height="2.18cm"}

46. Funciones de Boole
    de![](./ObjectReplacements/Object 910){width="2.367cm"
    height="0.467cm"}en
    ![](./ObjectReplacements/Object 912){width="2.198cm"
    height="0.467cm"}: tablas lineales, 2-dimensiona­les, arreglos de
    tablas 2-dimensionales y otras formas de representación.
    Simplificación en 2 capas de puertas.
