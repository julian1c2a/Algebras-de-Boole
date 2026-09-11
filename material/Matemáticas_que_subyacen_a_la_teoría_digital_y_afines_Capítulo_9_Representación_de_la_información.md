1.  Representación de la información.

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
        $${\{ 0\}} \cup {\{{1 \cdot {\lbrack{\{ 0,1\}}\rbrack}^{\ast}}\}}$$,
        dónde \'$$\cdot$$\' quiere decir seguido o conca­tenado, y
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

2.  1.  Hemos hablado de alfabetos, lenguajes sobre un alfabeto y
        después sobre el orden sobre esas palabras. Si llamamos a las
        reglas que cumplen las palabras de un lenguaje respecto a un
        alfabeto la gramática de ese lenguaje, el último elemento, el
        del orden, o más en general los significados, son la semántica.

    2.  En 3 hablamos de un lenguaje de los números naturales sobre un
        alfabeto $$\mathbf{B}_{\mathbf{\mathrm{2}}}$$. En general: ¿qué
        número significa 1001? ¿y el 1011101?. A qué valor natural
        apunta cada cadena es algo exterior al léxico y su gramática.
        Vamos a construir una semánti­ca: llamamos en una cadena de
        letras del alfabeto
        $$l_{\mathbf{\mathrm{n - 1}}}\ldots l_{\mathbf{\mathrm{1}}}l_{\mathbf{\mathrm{0}}}$$a
        $$l_{\mathbf{\mathrm{0}}}$$el dígito me­nos significativo
        (el$$\mathbf{lsb}$$) y al$$l_{\mathbf{\mathrm{n - 1}}}$$el
        dígito más significativo (el $$\mathbf{\mathrm{msb}}$$). Pri­mero
        asignamos unos valores naturales a los del alfabeto
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

    3.  Aquí es conveniente tener claro cómo pasamos de una base a otra.
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

    4.  Para describir letras, esto es, caracteres alfabéticos de la
        lengua natural, utilizamos generalmente el código ASCII (de 7
        bits el estándar original o de 8 dígitos binarios o bits, el
        extendido de Microsoft). Existen otros códigos, como el EBCDIC
        de IBM, UTF8, UTF16 y Unicode. Permiten sobradamente trasladar
        los lenguajes naturales escritos a un alfabeto binario.

    5.  El conjunto de los naturales es insuficiente para muchas
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
            general$${{\left\{ \mathbf{0} \right\} \vee \left\{ \mathbf{00} \right\}} \vee \left\{ \mathbf{10} \right\}} \vee \left( {{\mathbf{D}_{\mathbf{\mathrm{2}}} \cdot \left( {\mathbf{D}_{\mathbf{\mathrm{n}}} \smallsetminus \left\{ d_{0} \right\}} \right)} \cdot \left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\ast}} \right)$$,
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

                $$\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}:{\mathbf{D}_{\mathbf{\mathrm{n}}}\rightarrow\mathbf{D}_{\mathbf{\mathrm{n}}}}::\delta@\mathbf{\upsilon}\left( {{{n - 1} - \mathbf{\nu}}{(\delta)}} \right)$$$$C_{\mathbf{\mathrm{Β\mathit{m1}}}}:{\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}\rightarrow\left( \mathbf{D}_{\mathbf{\mathrm{n}}} \right)^{\mathbf{\mathrm{\ast}}}}::\delta_{n - 1}\cdots\delta_{1}\delta_{0}{:\rightarrow}\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{n - 1}\cdots\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{1}\mathbf{c}_{\mathbf{\mathrm{Β\mathit{m1}}}}\delta_{0}$$

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
                continuación no tendremos un dígito
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

        4.  La siguiente ampliación es $$\mathbb{Q}$$. Existen de
            entrada dos formas comunes de repre­sentación: en punto fijo
            y en punto flotante.

        5.  En punto fijo tendremos siempre que saber dónde se encuentra
            el punto o coma deci­mal, conociendo cual es la longitud de
            la parte fraccionaria
            ($$\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{(\mathit{r})}$$)
            y cual la de la parte entera
            ($$\mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}{(\mathit{r})}$$).
            Hasta el momento solo hemos utilizado
            $$\mathbf{l}{{(\mathit{r})} = \mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}}{{(\mathit{r})} + \mathbf{l}_{\mathbf{\mathrm{\mathit{ent}}}}}{(\mathit{r})}$$dónde
            $$\mathbf{l}_{\mathbf{\mathrm{\mathit{frac}}}}{{(\mathit{r})} = \mathbf{0}}$$.

        6.  Representaciones de binario natural en punto fijo. Vamos a
            ver, en un primer mo­mento, estas representaciones solo si
            son positivas, esto es, representaciones de
            $$\mathbb{Q}^{\mathbf{\mathrm{+}}}$$en binario natural, que
            será la base para el resto de representaciones más
            com­plejas. En principio la parte entera vendrá dada por una
            expresión del tipo
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
            necesario una vez se conocen la longitudes de las partes
            entera y fraccionaria.

        7.  El siguiente paso es ¿cómo pasamos un número en punto fijo
            de una base a otra?. Para esto lo más sencillo es separar el
            número en punto fijo en dos partes, la entera y la
            fraccionaria. La parte entera, un número natural, seguirá
            siendo entera en cualquier base, por lo que aplicamos las
            reglas de conversión que ya conocemos para n-ario na­tural,
            ya vistas.

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

        8.  Casos en que existe una relación entre
            $$\mathbf{D}_{\mathtt{\mathrm{n}}}$$y
            $$\mathbf{D}_{\mathtt{\mathrm{m}}}$$ tal que
            $$\exists p,{q \in \mathbb{N}}{n^{p} = m}o{n = m^{q}}o{n^{p} = m^{q}}$$.
            Los cambios son idénticos a los realizados para la parte
            entera excepto que los grupos de dígitos se cogen desde el
            punto decimal hacia la derecha, esto es, en sentido inverso
            al que tomábamos para los naturales.

        9.  Caso general. Hemos de utilizar una base intermedia, la
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
                $$({1/3})$$$$=$$$${0.\widehat{3}}_{\mathbf{\mathrm{\mathtt{\mathrm{10}}}}}$$$$=$$$${0.\widehat{01}}_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}}$$$$=$$$$0.1_{\mathbf{\mathrm{\mathtt{\mathrm{3}}}}}$$$$=$$$${0.\widehat{1}}_{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}$$$$=$$$${0.\widehat{13}}_{\mathbf{\mathrm{\mathtt{\mathrm{5}}}}}$$$$=$$$${0.2}_{\mathbf{\mathrm{\mathtt{\mathrm{6}}}}}$$$$=$$$${0.\widehat{2}}_{\mathbf{\mathrm{\mathtt{\mathrm{7}}}}}$$$$=$$$${0.\widehat{25}}_{\mathbf{\mathrm{\mathtt{\mathrm{8}}}}}$$$$=$$$${0.3}_{\mathbf{\mathrm{\mathtt{\mathrm{9}}}}}$$$$= \ldots =$$$${0.4}_{\mathbf{\mathrm{\mathtt{\mathrm{12}}}}}$$$$= \ldots =$$$${0.5}_{\mathbf{\mathrm{\mathtt{\mathrm{15}}}}}$$$$= \ldots =$$$${0.\widehat{5}}_{\mathbf{\mathrm{\mathtt{\mathrm{16}}}}}$$$$= \ldots =$$$${0.9}_{\mathbf{\mathrm{\mathtt{\mathrm{27}}}}}$$$$= \ldots$$.

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
                $$\exists p,{q \in \mathbb{N}}{n^{p} = m}o{n = m^{q}}o{n^{p} = m^{q}}$$,
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
                números enteros en pantalla en $$M\text{\&}S$$.

            6.  Por lo demás es fácil conseguir la representación de la
                parte fraccionaria en $$\mathit{CbB}$$ si ésta es
                negativa. Se realizan las operaciones de la misma forma
                que la hacíamos con la parte entera, solo que allí
                teníamos en cuenta la longi­tud de la representación,
                pero aquí, para la parte fraccionaria el complemento lo
                conseguimos básicamente con el complemento de la parte
                fraccionaria a la unidad
                $$\mathtt{\mathrm{1.0\ldots 0\ldots}}$$.

    6.  El último tipo de representación que vamos a ver es la
        representación en punto flo­tante
        ($$\mathit{floating}\mathit{point}$$, de forma que en C,C++ al
        tipo de números con decimales que habitualmente llamamos reales,
        toman el nombre de su forma de representación :
        $$\mathit{float}$$). Este tipo está estandarizado y tenemos un
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

    8.  Por ejemplo, el código $$\mathtt{{BCD} - {natural}}$$está dentro
        de
        $$\mathtt{\mathrm{L}}^{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}\left( B_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}} \right)$$,
        pero no son idénticos. Enumeraré los valores en una tabla de dos
        columnas:

  $$\mathtt{{BCD} - {natural}}$$   $$\mathtt{\mathrm{L}}^{\mathbf{\mathrm{\mathtt{\mathrm{4}}}}}\left( B_{\mathbf{\mathrm{\mathtt{\mathrm{2}}}}} \right)$$
  -------------------------------- -------------------------------------------------------------------------------------------------------------------------
  0000                             0000
  0001                             0001
  0010                             0010
  0011                             0011
  0100                             0100
  0101                             0101
  0110                             0110
  0111                             0111
  1000                             1000
  1001                             1001
  \-\-\--                          1010
  \-\-\--                          1011
  \-\-\--                          1100
  \-\-\--                          1101
  \-\-\--                          1110
  \-\-\--                          1111

3.  1.  Los códigos$$\mathtt{BCD}$$son códigos de longitud fija, por lo
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

4.  Tratamiento del error en códigos de longitud fija.

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
                poner un límite real­mente permisivo. Así permitimos
                que$$p_{\mathit{error}}{{({1\mathit{bit}})} \in {{\lbrack{0,0,39}\rbrack} \cup {\lbrack{0,61,1}\rbrack}}}$$,
                y por la reducción vista antes tenemos que
                $$p_{\mathit{error}}{{({1\mathit{bit}})} \in {\lbrack{0,0,39}\rbrack}}$$.
                Con un error de $$0,50$$el sistema es plenamente
                aleatorio. No hay absolutamente nada que hacer.
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

            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}\left( \mathtt{\mathrm{a,b}} \right)\overset{\text{def}}{=}\mathit{card}\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$

            En palabras es el número de bits que son diferentes entre
            amabas palabras (posición por posición).

        7.  La función definida anteriormente, formalmente,
            $$d_{\mathtt{\mathrm{H}}}^{\mathtt{\mathrm{n}}}:L^{\mathtt{\mathrm{n}}}{\left( \mathtt{\mathrm{B_{2}}} \right) \times L^{\mathtt{\mathrm{n}}}}{{{\left( \mathtt{\mathrm{B_{2}}} \right)\rightarrow{\lbrack{0,n}\rbrack}} \subset \mathbb{N}} \subset \mathbb{R}}::\left( \mathtt{\mathrm{a,b}} \right)@\mathit{card}\left\{ {{\iota \in {\lbrack{0,{n - 1}}\rbrack}} \mid {l_{\iota}^{a} \neq l_{\iota}^{b}}} \right\}$$es
            una distancia bien definida matemáticamente, la distancia
            entre dos palabras iguales es siempre 0, y si son distintas
            es necesariamente distinta de 0. Siempre es un número mayor
            o igual que 0 como corresponde a un cardinal de un conjunto.
            Además es si­métrica, esto es, la distancia entre dos
            palabras
            $$\mathit{de}\mathtt{\mathrm{a}}a\mathtt{\mathrm{b}}$$ es
            idéntica a la distancia
            $$\mathit{de}\mathtt{\mathrm{b}}a\mathtt{\mathrm{a}}$$. Por
            último se cumple la desigualdad triangular, para tres
            palabras cuales­quiera
            $${\mathtt{\mathrm{a,b,c}} \in \mathtt{\mathrm{L^{n}}}}\left( \mathtt{\mathrm{B_{2}}} \right)$$
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
            $$D_{\min H}\left( C^{n} \right)\overset{\text{def}}{=}\underset{a \neq b}{\overset{{({a,b})} \in {C^{n} \times C^{n}}}{\mathtt{\mathrm{mínimo}}}}\left( {d_{\mathtt{\mathrm{H}}}^{n}\left( \mathtt{\mathrm{a,b}} \right)} \right)$$.
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
                $$d_{\min H}{\left( C^{n} \right) = 1}$$.

            3.  Si$$\#{C^{n} > 2^{n - 1}}$$,
                entonces$$d_{\min H}{\left( C^{n} \right) = 1}$$. Este
                resultado, tipo cota de la dis­tancia mínima en función
                del cardinal del código, se puede extender para
                distancia mínima 2, \... Por
                ejemplo$$d_{\min H}{\left( C^{n} \right) = n}$$entonces$${\# C^{n}} = 2$$.

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
                es el máxima verosimilitud.

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
                Por otra parte, condición necesaria y sufi­ciente para
                que la operación sea inyectiva es que no contenga
                columnas igua­les ni columnas vector 0.

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

$$\begin{matrix}
{{= {\begin{pmatrix}
1 & 0 \\
0 & 1 \\
a & b \\
c & d
\end{pmatrix} \cdot \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1
\end{pmatrix}}} =} \\
{= \begin{pmatrix}
1 & 0 & 1 \\
0 & 1 & 1 \\
a & b & {a \oplus b} \\
c & d & {c \oplus d}
\end{pmatrix}}
\end{matrix}$$

5.  1.  1.  1.  1.  1.  1.  1.  1.  1.  

                La matriz izquierda de la primera fila es la matriz
                generadora de paridades, la de­recha son el código
                original de 4 bits en forma de una palabra por cada
                columna. Por último la matriz inferior son los vectores
                codificados con tres bits de paridad insertos. Solo
                queda ver la transformación inversa correspondiente.
                Para esto vea­mos que si observamos matriz izquierda de
                la primera fila$$\mathtt{\mathrm{H}} = \begin{pmatrix}
                \mathtt{\mathrm{I}_{2 \times 2}} \\
                \mathtt{\mathrm{P}_{2x2}}
                \end{pmatrix}$$. Tomare­mos como matriz decodificadora
                (no necesariamente inyectiva) a

                $$\mathtt{\mathrm{H}}^{\mathbf{\mathrm{\ast}}} = \begin{pmatrix}
                \mathtt{\mathrm{H}_{2 \times 2}} & \mathtt{\mathrm{P}_{2 \times 2}^{\mathrm{T}}}
                \end{pmatrix}$$

                $$\mathtt{\mathrm{H}^{\mathbf{\mathrm{\ast}}}} = \begin{pmatrix}
                1 & 0 & a & c \\
                0 & 1 & b & d
                \end{pmatrix}$$

                Ahora bien, sabemos que:

                $${{\mathtt{\mathrm{H}^{\mathbf{\mathrm{\ast}}}} \cdot \mathtt{\mathrm{H}}} \cdot \mathtt{\mathrm{o}}} = \mathtt{0}$$

                De dónde obtenemos un sistema de ecuaciones, con estos
                resultados (distintos del resultado trivial):

                $$\mathtt{{\mathrm{P}_{2 \times 2}}^{\mathbf{\mathrm{T}}}} = \begin{pmatrix}
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
                \end{pmatrix}} = {}$$

                $${} = \begin{pmatrix}
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

                $$\mathtt{{\mathrm{P}_{2 \times 2}}^{\mathbf{\mathrm{T}}}} = \begin{pmatrix}
                1 & 0 \\
                0 & 1
                \end{pmatrix}$$

                $$\mathtt{\mathrm{H}^{\mathbf{\mathrm{\ast}}}} = \begin{pmatrix}
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

6.  Funciones de Boole de $$n - \mathit{variables}$$ en
    $$1 - \mathit{variable}$$: tablas lineales, 2-dimensiona­les,
    arreglos de tablas 2-dimensionales y otras formas de representación.
    Simplificación en 2 capas de puertas.
