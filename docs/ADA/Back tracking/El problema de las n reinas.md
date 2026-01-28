> Busca obtener una solución factible, no la solución óptima. 

Se comprueban que no estén en la misma columna y en las diagonales recorriendo todo el vector.
Si llegamos a una hoja se expande el nodo comprobando si es factible. 

![[n-reinas.png]]

Para mostrar solo una solución utilizamos un booleano `found`.

![[n-reinas 1.png]]

