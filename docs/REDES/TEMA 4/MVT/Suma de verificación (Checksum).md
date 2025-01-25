# Suma de verificación (Checksum)
La suma de verificación es un método simple pero efectivo para detectar errores en los datos transmitidos. Consiste en **sumar los valores de los bytes de datos en el emisor**, a menudo utilizando aritmética de **complemento a uno**, y luego enviar el resultado junto con los datos. El receptor realiza la misma suma en los datos recibidos, incluyendo el valor de suma de verificación transmitido, y si el resultado es un valor específico (por ejemplo, 0xFF), los datos se consideran correctos. Si el resultado es diferente, se asume que los datos están corruptos.
## ¿Qué es la suma de verificación?

La suma de verificación es un valor numérico calculado a partir de un bloque de datos antes de su envío. Este valor representa una especie de "resumen" de los datos originales. Al recibir los datos, el receptor recalcula la suma de verificación y la compara con la recibida. Si ambas coinciden, se asume que los datos no han sufrido alteraciones durante la transmisión; si difieren, se detecta que ha ocurrido un error.
## ¿Cómo funciona el mecanismo de suma de verificación?

1. **Cálculo en el emisor:**
   - **Segmentación de datos:** El bloque de datos se divide en segmentos de tamaño fijo (por ejemplo, de 8, 16 o 32 bits).
   - **Suma binaria:** Se suman todos los segmentos utilizando aritmética binaria.
   - **Ajuste de acarreo:** Si la suma excede el tamaño del segmento (se produce un acarreo), este se agrega al resultado sumándolo de nuevo.
   - **Complemento (opcional):** A veces se utiliza el complemento a uno o a dos del resultado para mejorar la detección de errores.
   - **Inserción de la suma de verificación:** El valor final se adjunta al bloque de datos y se envía al receptor.

2. **Verificación en el receptor:**
   - **Recepción de datos y suma de verificación:** Se reciben los datos junto con la suma de verificación calculada por el emisor.
   - **Repetición del cálculo:** El receptor realiza el mismo proceso de suma sobre los datos recibidos.
   - **Comparación:** Se compara la suma calculada con la suma de verificación recibida.
   - **Detección de errores:** Si coinciden, se considera que los datos están íntegros; si no, se detecta un error.
### ¿Qué determina el tamaño de la segmentación de un bloque de datos?

El **tamaño de la segmentación** de un bloque de datos en el cálculo de la suma de verificación (checksum) está determinado por varios factores:

1. **Especificaciones del protocolo:**
   - **Protocolos y estándares:** Algunos protocolos de comunicación y estándares especifican el tamaño del segmento que debe utilizarse. Por ejemplo, en TCP/IP se utiliza un checksum de 16 bits.
   - **Requisitos de compatibilidad:** Para garantizar la interoperabilidad entre diferentes sistemas y dispositivos, es necesario seguir las especificaciones establecidas.

2. **Arquitectura del hardware:**
   - **Ancho de palabra del procesador:** La capacidad de procesamiento del hardware influye en el tamaño óptimo del segmento. Procesadores de 8, 16, 32 o 64 bits pueden procesar más eficientemente segmentos que coincidan con su ancho de palabra.
   - **Limitaciones físicas:** Algunos dispositivos pueden tener limitaciones en cuanto al tamaño de datos que pueden manejar en una sola operación.

3. **Balance entre eficiencia y detección de errores:**
   - **Eficiencia computacional:** Segmentos más grandes pueden reducir el número de operaciones necesarias para calcular la suma, mejorando la eficiencia.
   - **Sensibilidad a errores:** Segmentos más pequeños pueden ser más efectivos en la detección de ciertos tipos de errores, como inversiones de bits individuales.

4. **Consideraciones del software:**
   - **Implementación del algoritmo:** Algunos algoritmos de checksum están diseñados para operar con segmentos de un tamaño específico.
   - **Compatibilidad con sistemas legados:** Sistemas antiguos pueden requerir tamaños de segmento específicos por razones históricas o de compatibilidad.

___
## Ejemplo práctico:

Supongamos que el emisor quiere enviar los siguientes dos segmentos de 8 bits:

- **Segmento 1:** `01010101`
- **Segmento 2:** `00110011`

**Paso 1: Suma los segmentos**

```
  01010101
+ 00110011
------------
  10000110
```

**Paso 2: No hay acarreo más allá de 8 bits, así que no se requiere ajuste.**

**Paso 3: Calcula el complemento a uno (opcional)**

```
Complemento a uno de 10000110 es 01111001
```

**Paso 4: Envía los datos y la suma de verificación**

- Datos: `01010101 00110011`
- Suma de verificación: `01111001`

**En el receptor:**

**Paso 1: Suma los segmentos y la suma de verificación**

```
  01010101
+ 00110011
+ 01111001
------------
  11111111
```

**Paso 2: El resultado es `11111111` (todos unos), lo que indica que no hay errores.**
### Importancia en el nivel de enlace de datos:

En esta capa, los protocolos se encargan de la transferencia directa de datos entre dos nodos conectados físicamente. La suma de verificación es esencial para:

- **Detección de errores de transmisión:** Ruido, interferencias o fallos en el medio físico pueden corromper los datos.
- **Eficiencia en la comunicación:** Al detectar errores tempranamente, se evitan procesos costosos en capas superiores.
- **Simplicidad y rapidez:** Los cálculos de suma de verificación son menos complejos que otros métodos, lo que permite una verificación rápida.
# 3 Limitaciones de la suma de verificación:
- **No es infalible:** Puede no detectar todos los tipos de errores, especialmente si ocurren cambios compensatorios en los datos.
- **No corrige errores:** Solo detecta la presencia de errores; no proporciona información sobre cómo corregirlos.
- **Menos robusta que otros métodos:** Técnicas como el **Chequeo de Redundancia Cíclica (CRC)** ofrecen una detección de errores más confiable y son preferidas en muchas aplicaciones.

___
## Ejemplo práctico con acarreo:

Veamos un ejemplo donde ocurre un **acarreo** durante el cálculo de la suma de verificación usando segmentos de 8 bits.
Supongamos que el emisor quiere enviar los siguientes dos segmentos de 8 bits:

- **Segmento 1:** `11110000` (en decimal, 240)
- **Segmento 2:** `11001100` (en decimal, 204)

En realidad, si no hay errores, la suma de los datos y la suma de verificación debería resultar en todos unos (`11111111` en binario). 

**Paso 1: Suma los segmentos en el emisor**

```
   11110000
+  11001100
-------------
1 10111100
```

- Acarreo: `1`
- Resultado de 8 bits: `10111100`
- Sumamos el acarreo:

```
   10111100
+         1
-------------
   10111101
```

**Paso 2: Calcula el complemento a uno del resultado**

- Complemento a uno de `10111101` es `01000010`

**Paso 3: Envía los datos y la suma de verificación**

- Datos: `11110000 11001100`
- Suma de verificación: `01000010`

En el **receptor**:

**Paso 1: Suma los segmentos y la suma de verificación**

```
   11110000
+  11001100
+  01000010
-------------
1 11111110
```

- Acarreo: `1`
- Resultado de 8 bits: `11111110`
- Sumamos el acarreo:

```
   11111110
+         1
-------------
   11111111
```

**Paso 2: Verificación final**

- El resultado es `11111111` (todos unos), lo que indica que no hay errores en la transmisión.
