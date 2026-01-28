Utiliza la función merge, que al recibir dos vectores ordenados los fusiona dando como salida otro vector ordenado.

```c++
void merge(vector<int> tv, size_t first, size_t middel, size_t last) {
	vector<int> v_merged;
	v_merged.reserve(last - first); // to make it faster
	
	size_t l = first, r = middel;
	while(l != middel r != last) {
		if(v[l] < v[r])
			v_merged.push_back(v[l]); ++l;
		else 
			v_merged.push_back(v[r]); ++r;
	}
	for(;l != middel; ++l) v_merged.push_back(v[l]);
	for(;r != last; ++r) v_merged.push_back(v[r]);
	//for( size_t i = first; i < Last; ++i ) 'v [i]	begin (v_merged) , , [first] ) ;
	copy(begin(v_merged), end(v_merged), &v[first]); // faster
}
```

Esta pensado para listas que son consecutivas en la llamada de la función. De manera que desde **first** hasta **middel - 1** forma la primera lista, y desde **middel** hasta **last** (no incluido) forma la segunda.

```c++
void mergesort(vector<int> &v, size_t first, size_t last){ // past-the-end
	if(last - first < 2) // caso base
		return; 
		
	size_t middel = first + (last - first) / 2; 
	
	mergesort(v, first, middel); 
	mergesort(v, middel, last); 
	
	merge(v, first, middel, last);
} 
```

> **No hay mejor y peor caso**.

El tamaño del problema viene dado por $n=last-first$
Ecuación de recurrencia (coste exacto):
$$T(n) =
	\left\{
		\begin{array}{lr}
			1 & n\le1 &\\
			n+2T(\frac{n}{2}) & n>1
		\end{array}
	\right.$$
Complejidad temporal: $O(n\log n)$ (como en el quickSort).
$$T(n) \in
	\left\{
		\begin{array}{lr}
			1 & n\le1 &\\
			n+M(\frac{n}{2}) & n>1
		\end{array}
	\right.$$
Complejidad espacial: $O(n)$

- Como hay una llamada al merge la complejidad espacial no es constante.