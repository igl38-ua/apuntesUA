Su solución voraz toma en cada caso la moneda de mayor valor posible. 
- Busca minimizar el número de monedas 

> [!note] Datos
> $M$ : suma de monedas
> $S$ : secuencia de decisiones (s1, s2, s3...)
> Restricción: $\sum^{n}_{i=1}valor(s_i) = M$

Consiste en formar una suma M con el número mínimo de monedas tomadas (con repetición) de un conjunto C.

Dado $M=65$

|       **C**        |                 **S**                 | **n**  |                               **Solución**                               |
|:------------------:|:-------------------------------------:|:------:|:------------------------------------------------------------------------:|
|   {1, 5, 25, 50}   |             (50, 5, 5, 5)             |   4    |                              óptima y voraz                              |
| {1, 5, 7, 25, 50}  |    (50, 7, 7, 1)<br>(50, 5, 5, 5)     | 4<br>4 |                 óptima y voraz<br>óptima, pero no voraz                  |
| {1, 5, 11, 25, 50} | (50, 11, 1, 1, 1, 1)<br>(50, 5, 5, 5) | 6<br>4 | factible pero no óptima (muchas monedas en uso)<br>óptima, pero no voraz |
|  {5, 11, 25, 50}   |              (50, 11, ?)              |  ???   |                         no se encuentra solución                         |
La solución óptima para el problema del cambio se resuelve con programación dinámica. ya que evita calcular muchas veces las misma solución para el mismo problema.