RIP - Routing Information Protocol. 

*Encaminamiento dentro de SA (Sistemas autónomos)*
Basado en un algoritmo de vector de distancia - Algoritmo Bellman-Ford.
# RIP v1
Los mensajes RIP con información de las rutas de datos se envían dentro de paquetes UDP
El envío de mensajes RIP a la dirección de broadcast hace que las máquinas que no soportan RIP procesen paquetes hasta la capa de transporte (UDP). 
Para solventar estos problemas se introduce la versión 2 de RIP
# RIP v2
Los mensajes RIP son enviados a la dirección IP **224.0.0.9** (dirección IP de multicast). 

- RIP permite el encaminamiento dinámico en redes de tamaño pequeño (hasta 16 saltos) con una estructura sencilla (inexistencia de muchos bucles). 
- RIP presenta problemas de convergencia lenta ante cambios en la red y posibilidad de que se introduzcan bucles infinitos. Para evitar esto emplea estrategias como temporizadores y un número máximo de saltos.