# Definición

Se utiliza para resolver problemas de optimización. Este método consiste en dividir el problema original en subproblemas más pequeños (**ramificación**) y utilizar límites (**cotas**) para eliminar (**podar**) subproblemas que no pueden contener una solución mejor que la mejor solución encontrada hasta el momento.

___
# Eficiencia

> Cuando se utiliza la cola de prioridad se da el paso de [Back tracking](../Back%20tracking/Back%20tracking.md) a [Ramificación y poda](Ramificación%20y%20poda.md).

Al igual que en back tracking, las cotas pueden ser tanto estimaciones de valores como valores intermedios calculados mediante otros métodos como los voraces. Estos dan soluciones rápidas y buenas, pero no óptimas. 

El objetivo es establecer restricciones con las cotas y evaluar y podar las ramas en función de si son factibles. Esto se puede hacer comparando los valores de avance con cálculos intermedios. 

Las cotas **reducen el espacio de búsqueda** del algoritmo, lo que permite alcanzar soluciones óptimas de manera eficiente. 

___
# Poda eficiente

Obtener un subconjunto de tamaño m con la suma mínima.

```c++
int ramificacionPodaHelper(const vector<int>& nums, vector<int>& subset, int start, int m, int min_sum) {
    if (subset.size() == m) {
        int current_sum = 0;
        for (int num : subset) {
            current_sum += num;
        }
        return min(current_sum, min_sum);
    }

    for (int i = start; i < nums.size(); ++i) {
        subset.push_back(nums[i]);
        int current_sum = 0;
        for (int num : subset) {
            current_sum += num;
        }
        if (current_sum < min_sum) {
            min_sum = ramificacionPodaHelper(nums, subset, i + 1, m, min_sum);
        }
        subset.pop_back();
    }

    return min_sum;
}

int ramificacionPoda(const vector<int>& nums, int m) {
    vector<int> subset;
    return ramificacionPodaHelper(nums, subset, 0, m, INT_MAX);
}

int main() {
    vector<int> conjunto = {4, 8, 15, 16, 23, 42};
    int tamaño_subconjunto = 2;
    cout << "Suma mínima con poda: " << ramificacionPoda(conjunto, tamaño_subconjunto) << endl;
    return 0;
}
```

Comprueba las sumas parciales con la mínima hasta el momento para realizar o no el avance. 

