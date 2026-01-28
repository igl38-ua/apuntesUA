# Definición

En back tracking se exploran todas las soluciones posible de manera sistemática para encontrar **una solución** o **todas las soluciones válidas** a un problema. Construye la solución paso a paso y abandona (retrocede) las soluciones parciales que no cumplen las condiciones del problema (las que no dan una solución válida).
# Implementaciones

[[El problema de la mochila (general)]]
[[Permutaciones]]
[[El problema de las n reinas]]
[[Viajante de comercio]]

___
# Podas

En back tracking puro, sin cotas, no importa el orden de los elementos porque se exploran todas las soluciones.

___
# Cotas

## Cota optimista

- Estima, a mejor, el mejor valor alcanzable al expandir un nodo.
- Puede que no exista una solución factible que alcance ese valor
- Si la cota optimista de un nodo es peor que la solución en curso, se puede podar el nodo. 
## Cota pesimista

- Estima, a peor, el mejor valor alcanzable al expandir un nodo. 
- Tiene que asegurar que existe una solución factible con un valor mejor que la cota. 
- Normalmente se obtienen mediante **soluciones voraces** del problema. 
- Se puede eliminar un nodo si su cota optimista es peor que la mejor cota pesimista. 
- Permite la poda aún antes de haber encontrado una solución factible. 

___
# Esquema general recursivo

![item](../Media/vuelta-atras.png)

Utilizar algoritmos voraces en cotas pesimistas permite reducir el espacio de búsqueda del algoritmo. Pueden eliminar ramas del árbol de búsqueda que es probable que no conduzcan a una solución mejor. Esto mejor el rendimiento y la eficiencia (complejidad temporal). 
Los algoritmos voraces suelen encontrar mejores soluciones porque se basan en la estimación del coste mínimo posible de una solución. 

