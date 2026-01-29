# 1.Tipos de redes
## Redes LAN
Redes de difusión. De área local (piso o edificio).
Características:

- Baja tasa de error en el medio físico.
- Alta velocidad de transferencia (10 Mbps - 10 Gbps).
- Coste bajo
- Colisiones en el medio físico.
## Redes MAN
Redes que mezclan difusión y punto a punto (cabe coaxial y fibra óptica).
Extensión de ciudad.
Velocidades altas (100 Mbps - 1 Gbps).
## Redes WAN
Distintas topologías: anillo, estrella, árbol, malla, irregular... Siempre utilizando líneas punto a punto.
Según la forma  en que se establece la comunicación:
### Redes de conmutación de circuitos
Camino fijo y dedicado en un canal físico utilizando conmutadores (switches). Como la RTC en telefonía.
### Redes de conmutación de paquetes
Información fragmentada en paquetes. Cabeceras para el direccionamiento y reconocimiento de paquetes.
#### Circuitos virtuales
Analogía de la conmutación de circuitos. Camino fijo virtual común a todos los paquetes. Más retardos.

- Intercambio fiable de datos.
- Control de los recursos disponibles para la comunicación.
#### Datagramas
Los paquetes tienen información del destino pero no del camino que tienen que seguir. Es posible que los paquetes lleguen a su destino desordenados o que no lleguen, con lo que no es un método muy fiable. (Caso de Red X.25 en España).

Tolerancia a fallos y comunicación no fiable.
La decisión de salto para cada paquete se realiza en cada nodo.

>Un nodo de una red de **conmutación de paquetes** necesita recursos de software y sufre congestión.

>Un nodo de una red de **conmutación de circuitos** tiene una capacidad física determinada y sufre saturación.