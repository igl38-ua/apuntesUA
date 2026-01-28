Para el caso:

$$f(n) = n^2 + n + 2$$

$$f(n) \in \Omega(n)$$

$$f(n) \in \Omega(1)$$

Si las dos son "buenas" hay que quedarse con la mayor que acota inferiormente (la más cercana).
Para el caso anterior la más cercana como cota inferior a $n^2$ entre `n` y `1` es `n`.

___
### Notación O - Cota superior - Peor caso

> O(f) -> conjunto de funciones acotadas superiormente por un múltiplo de f.

Funciones $g$, que van de los $N$ a los $R$, tales que existe un número $c>0$, que será el valor que multiplicaremos a la función, y existe un $n_0$, que será el valor a partir del cual lo acotará (solo es necesario saber que existe, no cuál es). La condición es que para todo $n$ > $n_0$ para el cual $0 < g(n) \le cf(n)$
### Notación Ω - Cota inferior - Mejor caso

> Ω(f) -> conjunto de funciones acotadas inferiormente por un múltiplo de f.
### Notación Θ - Coste exacto

> Θ(f) -> conjunto de funciones acotadas superior e inferiormente por un múltiplo de f.

$Θ(f) = O(f)\cupΩ(f)$

