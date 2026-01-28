# Noción de complejidad

La complejidad algorítmica es fundamental en el estudio de algoritmos, ya que permite cuantificar los recursos necesarios para resolver un problema. Se distingue principalmente entre complejidad temporal y complejidad espacial:

- **Complejidad Temporal**: Se refiere al tiempo que tarda un algoritmo en ejecutarse, el cual depende del tamaño del problema (por ejemplo, el número de elementos en un arreglo). 
	- Se expresa comúnmente en términos de la relación entre el tamaño de entrada del algoritmo y los pasos (o operaciones elementales) que necesita realizar el algoritmo para completar su ejecución.
- **Complejidad Espacial**: Se refiere a la cantidad de memoria que necesita un algoritmo para su ejecución, incluyendo la memoria necesaria para las variables, la información de entrada, y la estructura de control del propio algoritmo.

___
# Estudio del tiempo de ejecución
## Análisis empírico o a posteriori

Ejecutar el algoritmo para distintos valores de entrada y medir el tiempo de ejecución.
## Análisis teórico o a priori

Obtener una función que representa el tiempo de ejecución del algoritmo para cualquier valor de entrada.
## Tiempo de ejecución de un algoritmo

Función T(n) que mide el número de operaciones elementales que realiza el algoritmo de tamaño n.
## Pasos de programa

Agrupación de instrucciones cuyo tiempo de ejecución es cte con el tamaño del problema.

___
# Operaciones elementales para el cálculo de complejidad

1. **Operaciones aritméticas básicas**: Suma, resta, multiplicación y división.
2. **Asignaciones**: La asignación de un valor a una variable.
3. **Comparaciones**: Instrucciones que comparan dos valores, como las operaciones de igualdad, menor que y mayor que.
4. **Accesos a estructuras indexadas**: Acceder a elementos de un arreglo o matriz por medio de índices.
5. **Llamadas a funciones**: Incluidas las llamadas a funciones y el retorno desde ellas, aunque la complejidad de la función llamada se analiza por separado.

>Las instrucciones de declaración no se tienen en cuenta a menos que se trate de inicialización de variables en bucles porque puede afectar si modifica el tamaño del problema.

>Las instrucciones de return se tienen en cuenta si forman parte de la lógica del algoritmo que afecta a como se ejecuta el código en relación con el tamaño de entrada. Como por ejemplo en algoritmos recursivos. 

___
# Cotas de complejidad

Las cotas de complejidad proporcionan una manera de describir el comportamiento de un algoritmo en términos de su eficiencia y son esenciales para predecir el rendimiento de los algoritmos bajo diferentes condiciones:
## Cota Superior

Indica el máximo tiempo de ejecución de un algoritmo para el **peor caso** posible, proporcionando un límite superior en su complejidad temporal.
## Cota Inferior

Proporciona un límite inferior, describiendo el **mejor caso** posible o el mínimo tiempo que puede tomar un algoritmo.
## Cota Exacta

Utilizada cuando un algoritmo tiene el mismo orden de crecimiento tanto en el mejor como en el peor caso, dando una medida exacta de su complejidad. **Caso promedio**.

___
# Notación asintótica

Notación matemática para representar la complejidad cuando el tamaño del problema crece, n tiende a infinito. 
## Notación O - Cota superior - Peor caso

O(f) -> conjunto de funciones acotadas superiormente por un múltiplo de f.
## Notación Ω - Cota inferior - Mejor caso

Ω(f) -> conjunto de funciones acotadas inferiormente por un múltiplo de f.
## Notación Θ - Coste exacto

Θ(f) -> conjunto de funciones acotadas superior e inferiormente por un múltiplo de f.
$Θ(f) = O(f)\cupΩ(f)$

Clases más utilizadas:

![item](../img/ada/jerarquías%20de%20funciones.png)

___
# Cálculo de complejidades

Pasos para obtener las cotas de complejidad:

- **Determinar la talla**: variable que se pretende encontrar, que puede ser el tamaño del problema o un parámetro de la función.
- **Determinar los casos mejor y peor**: instancias para las que el algoritmo tarda más o menos.
- **Obtener las cotas para cada caso**: algoritmos iterativos y recursivos.
## Algoritmos iterativos

> **Sumar elementos**

```c++
int sumar(const vector<int> &v){
	int s = 0;
	for( int i = 0; i < v.size(); i++ ) 
		s += v[i];
	return s;
}
```

| **Línea** | **Pasos** | **C. Asintótica** |
| ----- | ----- | ------------ |
| 2     | 1     | $Θ(1)$       |
| 3, 4  | n     | $Θ(n)$       |
| 5     | 1     | $Θ(1)$       |
| **Suma**      | n+2      | $Θ(n)$             |

Ejemplo 1: Elemento máximo de un vector -> $Θ(n)$
Ejemplo 2: Búsqueda en un vector ordenado -> $Θ(log_2\,n)$

___
## Algoritmos recursivos

Para expresar la complejidad de un algoritmo recursivo se utilizan las relaciones de recurrencia, pero son también aplicables a los algoritmos iterativos.
### Relación de recurrencia

Expresión que relación el valor de una función con uno o más valores de la misma para valores < n.

$$T(n)= 
	\left\{
		\begin{array}{lr}
			a\,f(F(n))+P(n) & n>n_0\\\\
			P'(n) & n\leq n_0
		\end{array}
	\right.$$

- $a\in N$ es una cte.
- $P(n),\,P'(n)$ son funciones de n
- $F(n)<n$

> Si el algoritmo tiene mejor y peor caso puede haber una relación de concurrencia para cada caso.
> Se resuelven mediante el método de sustitución.

___
## QuickSort

Algoritmo de ordenación por partición
### Tipos

Se basa en un elemento pivote, para dividir en dos partes el vector:

- Quicksort primer elemento
- Quicksort central
- Quicksort mediana
### Funcionamiento

- Se elige el pivote
- Se divide el vector en dos partes
	- izquierda, elementos menores
	- derecha, elementos mayores
- Dos llamadas recursivas, una con cada parte del vector

___
## HeapSort

Montículos y algoritmo de ordenación

___
# Programación dinámica

Evita las repeticiones en las iteraciones de las llamadas recursivas en técnicas como divide y vencerás, guardando los resultados de los subproblemas que se evalúan (memoization). Esto puede provocar el aumento de la complejidad espacial, por eso es necesario evaluar la mejor situación. 
## Subestructura óptima (principio de optimalidad)

Es un "caso óptimo" que se puede construir de manera eficiente a partir de las soluciones óptimas de sus subproblemas. Es una condición necesaria para aplicar la programación dinámica. 

Ejemplos:

- Problema de la mochila
- Corte de tubos
- QuickSort
- MergeSort

Hay casos como en el quickSort que no sería óptimo utilizar la programación dinámica ya que no hay, o no suele haber casos repetidos. Esto incrementaría el coste de la complejidad espacial. 
