 Algoritmo de ordenación por partición.

- Se selecciona un **elemento pivote** central que divide el vector dos.
	- En la parte izquierda van los elementos menores que el pivote.
	- En la parte derecha van los elementos mayores que el pivote.
- Mediante llamadas recursivas a ambas partes se ordena el resto del vector. 
# QuickSort (pivote primer elemento)

Criterio librerías STL.

- **first**: primer elemento del vector (incluido).
- **last**: apunta a uno fuera, al siguiente. Al primero que no está en el vector.

```c++
void quicksort( vector<int> tv,	size_t first, size_t last){
	if(last — first < 2 ) return;
	
	size_t p = first, l	= last;
	
	vhile(p+l != 1) {
		if(v[p+1] < v[p]){
			swap(v[p+l], v[p]);
			p++;
		}else{
			l--;
			swap(v[p+l], v[l]);
		}
	}
	quicksort(v, first, p);
	quicksort(v, p+1, las);
}

void quicksort(vector<int> &v) { quicksort(v, 0, v.size()); }
```

Tamaño del problema -> n = last - first

- **Mejor caso**: subproblemas (n/2, n/2).
	Cuando el pivote esta en medio.
$$T(n) \in
	\left\{
		\begin{array}{lr}
			O(1) & n\le1\\
			O(n)+2T(\frac{\large n}{2}) & n>1
		\end{array}
	\right.$$

- **Peor caso**: subproblemas (0, n-1) o (n-1, 0).
	Cuando el pivote se queda a uno de los lados.
$$T(n) \in
	\left\{
		\begin{array}{lr}
			O(1) & n\le1\\
			O(n)+T(n-1) & n>1
		\end{array}
	\right.$$
___
## Mejor caso

![item](../Media/quicksort.png)

$$\frac{n}{2^k}=1 \rightarrow 2^k=n \rightarrow log_2(2^k)=log_{\large 2}\, n \rightarrow k=log_2\,n$$

## Peor caso

![item](../Media/quicksort%201.png)

---
# Quickselect

La principal diferencia respecto al quickSort es que en lugar de hacer dos llamadas recursivas se evalúa si elemento enésimo es menor que el pivote y se hace una única llamada por el lado correspondiente del vector.

```c++
void quickselect( vector<int> tv, size_t first, size_t nth, size_t last){
	if(last — first < 2 ) return;
	
	size_t p = first, l	= last;
	
	vhile(p+l != 1) {
		if(v[p+1] < v[p]){
			swap(v[p+l], v[p]);
			p++;
		}else{
			l--;
			swap(v[p+l], v[l]);
		}
	}
	
	if(nth == p) return;
	if(nth < p)	
		quicksort(v, first, p);
	else
		quicksort(v, p+1, las);
}
```

Tamaño del problema: n = last - first
## Mejor caso

- $nth = p$
- complejidad: $O(n \log(n))$
## Peor caso

- cuando $nth\neq p$ 
- el pivote se queda al principio o al final
$$T(n) =
	\left\{
		\begin{array}{lr}
			1 & n\le1 &\\
			n+T(n-1) & n>1
		\end{array}
	\right. \in O(n^2)$$
## Otro caso especial

- cuando $nth\neq p$
- el pivote se queda en el centro
$$T(n) =
	\left\{
		\begin{array}{lr}
			1 & n\le1 &\\
			n+T(\frac{n}{2}) & n>1
		\end{array}
	\right. \in O(n)$$
