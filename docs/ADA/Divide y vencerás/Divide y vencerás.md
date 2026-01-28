# Definición

Divide y vencerás divide el problema principal en subproblemas independientes, resuelve cada subproblema por separado y luego combina los resultados para formar la solución del problema original.
# Implementaciones

[[QuickSort|QuickSort]]
[[2 Areas/ADA/Divide y vencerás/HeapSort]]
[[MergeSort]]
# Esquema DyV

Todos los algoritmos implementados mediante esta técnica siguen un esquema general de instanciación.

![[dyv.png]]
## Análisis de eficiencia

De costes log a exponenciales.
### Eficiencia

Depende de:
- N.º subproblemas, h.
- Tamaño de los subproblemas.
### Teorema Maestro

$g(n)=$ tiempo para un tamaño n, sin llamadas recursivas.
b = cte. de división del tamaño de problema.
$$T(n)=h\,T(\frac{n}{b})+g(n)$$
Solución general:
- Suponiendo $g(n)\in O(n^k)$
$$T(n) \in
	\left\{
		\begin{array}{lr}
			\Theta(n^k) & si\,\,h<b^k\\
			\Theta(n^k\,log_{\large b}\,n) & si\,\,h=b^k\\
			\Theta(n^{\Large log_{\Large b}h}) & si\,\, h>b^k
		\end{array}
	\right.$$
### Teorema de reducción

Los mejores resultados en cuanto al coste se consiguen cuando los subproblemas son aprox del mismo tamaño. 
- Caso especial, cumple el teorema de reducción ($b=h=a$).
$g(n) \in O(n^k)$
$$T(n)=a\,T(\frac{n}{a})+g(n)$$
$$ T(n) = \begin{cases} \Theta(n^k) & k > 1 \\ \Theta(n \log n) & k = 1 \\ \Theta(n) & k < 1\end{cases} $$

___
## Paso de Divide y Vencerás a Programación Dinámica

Añade pasos como is_solved() para no repetir pasos de programa.

![[dyv-a-pd.png]]
## Paso a Programación dinámica iterativa

![[dyv-a-pd 1.png]]
