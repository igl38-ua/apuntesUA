# Mochila 0/1 con pesos discretos

- Se trata de un problema de optimización.
- Los pesos son cantidades discretas, son unidades enteras. A menor sea la unidad más difícil se hace el problema.
- Establece una secuencia de decisiones, los objetos que puedes llevar en la mochila $(x_1,x_2...x_n)$, y si lo puedes coger o no $(x_i\in \{0,1\})$
	- Si el objeto $x_i$ es escogido $x_i=1$, en caso contrario $x_i=0$.

> [!note] Datos
> - $v_i$ son los valores
> - $w_i$ son los pesos
> - $W$ es la capacidad de la mochila

- La secuencia óptima de decisiones maximiza:
$$\sum_{i=1}^{n}x_iv_i$$
Con las restricciones:
$$\sum_{i=1}^{n}x_iv_i \le W$$
$$\forall i:1 \le i \le n, x_i \in \{0,1\}$$

El peso que lleva la mochila debe ser menor o igual que el peso que aguanta la mochila (peso total).

El problema se representa con los objetos 1 hasta k y capacidad C.
- Problema inicial: knapsack(n, W).

___
## Solución recursiva

Las decisiones se toman en orden descendente: $x_n, x_{n-1},...x_1$ 
### Caso base

0 elementos.
$$knapsack(0, W)=0$$
### Recursividad

n elementos.
$$knapsack(n,W)= max
	\left\{
		\begin{array}{lr}
			knapsack(n-1,W)\\
			kanpsack(n-1,W-w_n)+v_n &if W\ge w_n
		\end{array}
	\right.$$
Dos posibilidades, omitiendo el último elemento, o cogiéndolo. 
Al cogerlo se elimina su peso del peso total y se suma el valor del último elemento siempre que sea menor que el peso total.

```c++
#include <limnits>

double knapsack(const vector<double> &v, const vector<unsigned> &w, int n, unsigned W){
	if(n == 0)
		return 0;

	double S1=knapsack(v, w, n-1, W);

	double S2=numeric_limits<double>::lowest();
	if(w[n-1] <= W)
		S2 = v[n-1] + knapsack(v, w, n-1, W-w[n-1]);

	return max(S1, S2);
}
// n = numero de objetos
```
### Complejidad temporal
#### Mejor y peor caso

- **Mejor caso**: Ningún objeto cabe en la mochila, luego $T(n) \in \Omega(n)$
- **Peor caso**: 
$$T(n) =
	\left\{
		\begin{array}{lr}
			1 & n=0 \\
			1+2\,T(n-1) & otro\,caso
		\end{array}
	\right.$$
Término general
$$T(n)=2^k-1+2^k\,T(n-k)$$
Terminará cuando $n-k=0$:
$$T(n)=2^n-1+2^n \in O(2^n)$$
> Solo puede haber nW problemas distintos.

Mediante esta implementación se pueden dar subproblemas repetidos en las llamadas recursivas.

___
## Solución recursiva con almacén

Para evitar repeticiones hay que evaluar si el problema ha sido resuelto para anotarlo o no, y de esa manera resolverlo o utilizar la solución ya anotada. Esta es la solución de **memoization**, recursivo con almacén.

![[pd-almacen.png]]

Utiliza una matriz M, inicializada a un valor centinela (valor imposible de knapsack). Esta matriz almacena las soluciones y los cálculos. De esta manera, antes de calcular otra solución para el problema se comprueba con la matriz si esa solución ya ha sido resuelta. 
Si ha sido resuelta se utiliza ese valor guardado. En caso contrario se resuelve y se anota la solución.
La complejidad por lo tanto será de n * n, que son los accesos a la matriz. $O(nW)$
Matriz n * W.

---
## Solución iterativa
### Una solución

No hace falta centinela pero mantiene una matriz de almacenamiento.

![[sol-iterativa.png]]

___
## Solución iterativa mejor

Almacena los resultados intermedios en la matriz.

![[sol-iterativa-mejor.png]]

![[soluciones-parciales.png]]
### Complejidad temporal

Es la misma que para el caso recursivo con almacén.
$$T(n,W)=1+\sum_{i=1}^n1+\sum_{i=1}^2\sum_{j=1}^W 1=1+n+nW$$
$$T(n,W)\in O(nW)$$
### Complejidad espacial

$$T_s(n,W)\in O(nW)$$

___
## Solución iterativa con extracción de la selección

Almacena en una matriz de booleanos si las posiciones han sido utilizadas o no y extrae la solución en base a esa matriz.

![[sol-iterativa-extraccion.png]]

---
# Subestructura óptima o Principio de Optimalidad

![[principio-de-optimalidad.png]]


