> Programación dinámica
# Identidad de Pascal

![[identidad-de-pascal.png]]

___
## Ecuación de recurrencia
### Suponiendo $T(n-1,r)\le T(n-1,r-1)$

![[sol-recursiva-ineficiente.png]]

Se reduce a un término que si que sabes resolver $2g(n-1,r)$ ya que r es cte. Por lo tanto la complejidad se reduce a $O(2^{n-r})$.
### Suponiendo $T(n-1,r)\ge T(n-1,r-1)$

![[sol-recursiva-ineficiente 1.png]]

Se reduce a un término que si que sabes resolver $2g(n-1,r-1)$ ya que r es cte. Por lo tanto la complejidad se reduce a $O(2^r)$. Pero no es una solución recursiva aceptable.

Esta solución genera muchos subproblemas repetidos en la recursión. Para solventar esto se implementa una solución recursiva mejorada.

Establece un centinela y almacena los valores intermedios. **Memoization**.

![[memoization.png]]

