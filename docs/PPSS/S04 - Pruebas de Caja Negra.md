# Resumen

- Se asume que el elemento a probar es una **caja negra** en la que solo se conoce la especificación, pero no la implementación interna.
- Los métodos de **caja blanca** solo se aplican a pruebas unitarias, los de **caja negra** se aplican a cualquier tipo de prueba.
- Las pruebas deben de ser un conjunto **EFECTIVO** (deben detectar el máximo número posible de errores) y **EFICIENTE** (con el menor número posible de casos de prueba).
- Las **particiones** representan conjuntos de **posibles comportamientos** de un sistema.
- Para cada _variable de entrada o salida_, se definen **clases válidas** (que cumplen la especificación) y **clases inválidas** (que violan alguna condición).
- Se asigna un **identificador** a cada partición:  A1, A2... para las **válidas** y NA1, NA2... para las **no válidas**.

___
# Pruebas de caja negra
## Diseño de casos de prueba

- **Principio general**: Se asume que el elemento a probar es una "caja negra" en la que solo se conoce la **especificación** (lo que debería hacer), pero no la implementación interna. 
- Esto permite que se puedan encontrar defectos que pertenecen a comportamientos no implementados, a diferencia de los de caja blanca, que se centra en el código implementado. 

![item](../img/ppss/caja%20negra.png)
## Métodos de diseño de caja negra

- Método de particiones equivalentes.
- Método de análisis de valores límite.
- Método de tablas de decisión.
- ...

> Los métodos de **caja blanca** solo se aplican a pruebas unitarias, los de **caja negra** se aplican a cualquier tipo de prueba. 

___
## Método de diseño: Particiones equivalentes

- Con este método se identifica, a partir de la **especificación**, el conjunto de clases de equivalencia para cada entrada y salida del elemento a probar.
- Cada **partición** es un subconjunto de la especificación, separando entradas y salidas. 
	- Cada subconjunto representa un caso de prueba particular y debe tener su **imagen** en una partición de salida (debe tener asociado un subconjunto de salidas).

![item](../img/ppss/subconjuntos%20particiones.png)

No deben quedar subcomportamientos sin clasificar.

- El **objetivo** del método es “**cubrir**” todas las particiones con el **menor número** de casos de prueba. Todas las particiones deben estar probadas, y las particiones no válidas deben de ser probadas una a una (solo una partición no válida por combinación).
### Particiones

- Las **particiones** representan conjuntos de **posibles comportamientos** de un sistema.
- Se identifican en base a **condiciones de entrada/salida** de la unidad a probar. 
- Una **condición de entrada/salida** puede aplicarse a **una única variable** de E/S en una especificación o un **subconjunto** de variables. 
	- `a, b, c > 0` y `a, b, c <= 20` -> partición conjunta a las variables a, b y c.
	- `a > 20` -> partición a la variable `a`. 
	- `b > 20` -> partición a la variable `b`.
	- `c > 20` -> partición a la variable `c`.

> Para cada _variable de entrada o salida_, se definen **clases válidas** (que cumplen la especificación) y **clases inválidas** (que violan alguna condición).

___
## Etiquetado de particiones

- Se asigna un **identificador** a cada partición:  A1, A2... para las **válidas** y NA1, NA2... para las **no válidas**.
### Clases válidas
Se combinan en casos de prueba intentando cubrir el máximo de particiones válidas todavía no cubiertas. 
### Clases no válidas
Cada caso de prueba debe contener **solo una partición inválida** de entrada, para evitar que un error tape a otro. 

___
## Heurísticas de identificación de clases de equivalencia

Clases de equivalencia (**particiones**) para cada entrada/salida (**E/S**):

- Si la E/S indica un **RANGO** de valores de entrada (**1-12**) se definen:
	- **1 partición válida** dentro del rango. `x = 1..12` 
	- **2 particiones no válidas** por debajo y por encima del rango. `x > 12 y x < 1`

- Si la E/S indica un **NÚMERO N** concreto (**número de valores entre 1 y N**):
	- **1 partición válida** con esos valores. `x = 1, 2 o 3` 
	- **2 particiones no válidas** con valores fuera del conjunto. `x = no tiene ningún valor y x tiene más de 3 valores`

- Si la E/S indica un **CONJUNTO** de valores válidos (**{valorA, valorB, valorC}**):
	- **1 partición válida** de valores en el conjunto. `valorA o valorB o valorC`
	- **1 partición no válida** de valores fuera del conjunto. `valorT`

- Si la E/S indica una situación **DEBE SER** (x comenzar por un número):
	- **1 partición válida**. `x empieza con un dígito`
	- **1 partición no válida**. `n No empieza con un dígito`

- Si la E/S tiene condiciones combinadas (una variable depende de otra), se pueden agrupar las entradas en una sola **variable compuesta** para crear particiones más detalladas.

![item](../img/ppss/ejemplo%201%20impresión%20de%20caracteres.png)

![item](../img/ppss/ejemplo%202%20validar%20fecha.png)

![item](../img/ppss/ejemplo%202%20validar%20fecha%201.png)

![item](../img/ppss/ejemplo%202%20validar%20fecha%202.png)

___

Siguiente -> [S05 - Dependencias externas 1 (STUBs)](S05%20-%20Dependencias%20externas%201%20(STUBs).md)