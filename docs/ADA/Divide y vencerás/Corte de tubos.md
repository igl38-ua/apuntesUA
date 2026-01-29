# Corte de tubos
Tubos de longitud n que son cortados en trozos más pequeños para su venta, de manera que a más pequeños mayor es el precio por unidad.
El número total de formas distintas de cortar el tubo es de $2^{n-1}$, porque entre cada trozo posible del tubo, de 1 a 2, 2 a 3... puedes elegir cortar o no cortar (0 o 1).
# Solución por divide y vencerás

Se busca la descomposición en k número de elementos mediante la que se pueda obtener el precio máximo. i son las formas posibles de cortar.

$$n=i_1+i_2+···+i_k$$

Precio: 

$$r_n=p_{i_1}+p_{i_2}+···+p_{i_k}$$

Se va cortando el tubo haciendo llamadas recursivas después de guardar los valores para cada caso posible de n, reduciendo el número de elementos en cada iteración.

```c++
int tube_cut(const vector<int> &p, const int l){ //p tabla precios, l longitud del tubo 
	if(l == 0)
		return 0;

	int 1 = numeric_limits<int>::lowest();
	for(int i = 1; i <= l; i++)
		q = max(q, p[i] + tube_cut(p, l-i));
	return q;
}
```

___
## Complejidad

![item](../../img/ada/complejidad-solu-recursiva.png)

___
# Solución recursiva con almacén (memoization)

Guarda los resultados de los subproblemas en un vector de almacén.

```c++
const int SENTINEL = -1;

int tube_cut(vector<int> &M, const vector<int> &p, int l){ // M almacen de subproblemas 
	if(M[l] != SENTINEL) return M[l];

	if(l == 0) return M[0];

	int q = numeric_limits<int>::lowest();
	for(int i = 1; i <= l; i++)
		q = max(q, p[i] + tube_cut(M, p, l-i));

	return M[l] = 1; // guardar la solucion y devolver valor
}

int tube_cut(const vector<int> &p, int l){
	vector<int> M(l+1, SENTINEL); // inicializacion
	return tube_cut(M, p, l);
}
```

**Complejidad temporal**: $O(n)$
**Complejidad espacial**: $O(n^2)$

___
# Solución iterativa (directa)

```c++
int tube_cut(const vector<int> &p, int n){
	vector<int> M(n+1); // almacen de subproblemas

	for(int l = 0; l <= n; l++){
		if(l == 0){ // caso base
			M[0] = 0;
			continue;
		}

		int q = mumeric_limits<int>::lowest();
		for(int i = 1; i <= l; i++)
			q = max(q, p[i] + M[l-i]);
		M[l] = q; // guarda la solucion
	}
	return M[n];
}
```

**Complejidad temporal**: $O(n)$
**Complejidad espacial**: $O(n^2)$

