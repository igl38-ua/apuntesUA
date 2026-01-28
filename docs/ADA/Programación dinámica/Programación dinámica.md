# Definición

La programación dinámica en contraste con [[Divide y vencerás]] utiliza una matriz que almacena resultados intermedios ya resueltos para evitar recalcular estos resultados, lo que reduce el tiempo de ejecución. 

___
# Implementaciones

[[El problema de la mochila (knapsack problem)]]
[[Coeficiente binomial]]

___
# Casos
### Problemas superpuestos

Es útil cuando los mismos subproblemas se resuelven muchas veces. Almacenando resultados intermedios se evita la redundancia en los cálculos.
### Soluciones

Las construcciones de las soluciones para problemas más grandes se construyen a partir de las soluciones almacenadas de los subproblemas más pequeños. 
### Ejemplo diferencia entre programación dinámica y divide y vencerás
#### Programación Dinámica: Problema de la Mochila

- **Problema**: Dado un conjunto de ítems, cada uno con un peso y un valor, determinar el número de cada ítem que debe incluirse en una colección de modo que el peso total no exceda un límite dado y el valor total sea lo máximo posible.
- **Enfoque**: Utiliza una matriz para almacenar los máximos valores posibles para diferentes capacidades y números de ítems.
#### Divide y Vencerás: Merge Sort

- **Problema**: Ordenar una lista de elementos.
- **Enfoque**: Divide la lista en dos mitades, ordena cada mitad recursivamente y luego combina las dos mitades ordenadas en una lista ordenada completa. No se almacena el resultado intermedio de la ordenación de cada sublista para su reutilización posterior.

