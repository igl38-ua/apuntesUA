Dado un Grafo ponderado $g = (V, E)$ con pesos no negativos hay que encontrar un ciclo hamiltoniano de coste mínimo. 

![item](../Media/viajante-de-comercio.png)

La función **round** calcula la longitud de un camino, dado un grafo y el vector de su posible solución.

___
## Función solve

**k** es la ciudad por la cual se rellena
**x** es la solución parcial. 
**shortest** longitud del camino más corto hasta el momento.

Guarda el mínimo entre el shortest actual y el nuevo calculado.
Hace las permutaciones pertinentes con el swap para probar el resto de ciudades.

![item](../Media/viajante-de-comercio%201.png)

shortest se inicializa al máximo porque queremos minimizarlo.

No es viable por la complejidad $O(n^n)$ porque en cada casilla del vector podemos poner desde 1 hasta n.

Una cota optimista podría ser, dada un solución parcial sin ocupar todos los nodos, 
finalizar desde el último nodo calculado. Es una mejor solución, pero no es la óptima.

___
# Mejoras

- Cálculo incremental de la vuelta. 
- **Cota optimista**: 
	- Restricciones: 
		- el camino tiene que pasar por todas las ciudades.
		- el camino tiene que ser continuo.
	- Relajaciones:
		- no pasar por todas las ciudades -> saltar de la última a la primera.
		- ir saltando de una ciudad a otra -> árbol de recubrimiento mínimo.
- Poda basada en la mejor solución hasta el momento (cota pesimista).
	- buscar una solución subóptima
		- algoritmo voraz.

## Las n mejores soluciones

![item](../Media/n-mejores-soluciones.png)

Utiliza un cola de prioridad que siempre está ordenada.
Cada vez que tenemos una hoja, sacamos la longitud y comprobamos si merece la pena meterla entre las n mejores. Para eso comprobamos la peor de las que tenemos guardadas ( el top, por la manera en la que la cola de prioridad está ordenada de mayor a menor). 
