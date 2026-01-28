Se trata de reducir el tamaño del problema por piso para simplificar por paso la pirámide que hay que resolver, utilizando como pivote el palo intermedio.

![item](../Media/hanoi.png)

- Primero desde n-1 para resolver la sub pirámide sobre el palo intermedio, B.
- Se mueve el último disco al destino, C.
- Se aplica de nuevo desde n-1 sobre el destino, C.

La talla del problema es n-1.
## Complejidad

![item](../Media/hanoi%201.png)

Para la primera parte de la resolución (verde) se trata de una progresión geométrica como la de la página 3 de [am](../am.pdf):

$$\sum_{i=0}^{n} 2^i=2^{n+1}-1$$

Luego la ecuación de recurrencia y la complejidad:  
$$T(n)=
	\left\{
		\begin{array}{lr}
			1 & n=1 &\\
			1+2\,T(n-1) & n>1
		\end{array}
	\right.$$

$$T(n)=2^n-1 \in O(2^{\large n})$$
