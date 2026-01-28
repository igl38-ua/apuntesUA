Basado en el tipo abstracto de datos llamado cola de prioridad.

- Estructura de árbol binario completo
- Operaciones:
	- inserción (push). complejidad constante
	- extracción (pop y top). complejidad lineal.
- El árbol se almacena en un vector recorrido por niveles
- cumple siempre la propiedad del heap
	- El valor del padre siempre es mayor que los valores de sus hijos .
	- El valor de la raíz del árbol es el elemento mayor de la estructura.

![item](../../img/ada/inserción.png)

![item](../../img/ada/extracción.png)

___
## Extraer

![item](../../img/ada/sink.png)

___
## Ordenación

![item](../../img/ada/heapsort.png)
### Construcción del heap

Dada la lista inicial se va transformando, extrayendo el elemento máximo e insertándolo en el heap hasta que el montículo esta vacío. Esto da como resultado una lista ordenada.