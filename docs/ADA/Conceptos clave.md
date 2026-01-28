# Subestructura óptima o principio de optimalidad

Visto en [Programación dinámica](Programación%20dinámica/Programación%20dinámica.md).

Permite descomponer un problema grande en subproblemas más manejables, asegurando que la combinación de soluciones óptimas de subproblemas conduzca a una solución óptima del problema original.

Este principio establece que una solución óptima de un problema puede construirse de manera óptima a partir de soluciones óptimas de sus subproblemas. En otras palabras, si tenemos una solución óptima para un problema, esta solución incluye soluciones óptimas a los subproblemas que lo componen.
### Ejemplo Clásico: Problema del Camino Mínimo

Consideremos el problema de encontrar el camino mínimo entre dos puntos en un grafo ponderado.

- **Problema Original**: Encontrar el camino mínimo desde el nodo \(A\) hasta el nodo \(B\).
- **Subproblema**: Supongamos que un camino óptimo desde \(A\) hasta \(B\) pasa por un nodo intermedio \(C\). Entonces, el camino mínimo desde \(A\) hasta \(B\) es la combinación del camino mínimo desde \(A\) hasta \(C\) y el camino mínimo desde \(C\) hasta \(B\).

Si $(P_{A,B})$ es el camino óptimo desde $(A)$ hasta $(B)$, y este camino pasa por $(C)$, entonces $(P_{A,B}) = (P_{A,C}) + (P_{C,B})$. Aquí, $(P_{A,C})$ es el camino óptimo desde $(A)$ hasta $(C)$ y $(P_{C,B})$ es el camino óptimo desde $(C)$ hasta $(B)$.
### Ejemplo en Programación Dinámica: Problema de la Mochila

En el problema de la mochila, queremos maximizar el valor total de los ítems seleccionados sin exceder la capacidad de la mochila.
- **Problema Original**: Maximizar el valor total de los ítems seleccionados que no excedan la capacidad de la mochila.
- **Subproblema**: Si consideramos la decisión de incluir o no un ítem en particular, el problema puede dividirse en subproblemas que consisten en maximizar el valor total de los ítems seleccionados para las capacidades reducidas de la mochila.

Si \(K(n, W)\) representa el valor máximo para \(n\) ítems y capacidad \(W\), la relación de recurrencia puede escribirse como:
$K(n, W) = \max \left( K(n-1, W), v_n + K(n-1, W-w_n) \right)$

Aquí:
- $(K(n-1, W))$ es el valor máximo sin incluir el ítem $(n)$.
- $(v_n + K(n-1, W-w_n))$ es el valor máximo al incluir el ítem $(n)$, donde $(v_n)$ es el valor del ítem $(n)$ y $(w_n)$ es su peso.
### Principio de Optimalidad y Algoritmos Voraces

El principio de optimalidad también se aplica en algunos casos de algoritmos voraces, aunque estos generalmente requieren una forma más estricta de subestructura óptima conocida como **propiedad de subproblema de decisión local**.
### Resumen

1. **Principio de Optimalidad**:
   - Una solución óptima para un problema contiene soluciones óptimas para sus subproblemas.
   - Este principio es fundamental para la programación dinámica y ciertos algoritmos voraces.
2. **Aplicaciones**:
   - **Programación Dinámica**: Problema de la mochila, caminos mínimos, cadenas de matrices.
   - **Algoritmos Voraces**: Problema del cambio de monedas, problemas de intervalos.

---
