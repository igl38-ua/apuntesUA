Objetivos de la capa de red. Encaminamiento. 
# Protocolo IP. RFC 791
Direccionamiento IP 193.145.20.23
- Máscara de red.
- Valor de 32 bits.
- X.X.X.0 - Dirección de red.
- X.X.X.255 - Dirección de broadcast.
## Tipos de redes
| Clase | Tipo     | Bits                      |
| ----- | -------- | ------------------------- |
| A     | 0...     | Red (7) / Máquina (24)    |
| B     | 10...    | Red (14) / Máquina (16)   |
| C     | 110...   | Red  (21) / Máquina (8)   |
| D     | 1110...  | Multicast (28)            |
| E     | 11110... | Futuras ampliaciones (27) |
## Redes privadas
- 10.0.0.0/8
- 192.168.0.0/16
- 172.16.0.0/12
# Direccionamiento de redes con el protocolo IP
## Protocolo DHCP
Protocolo de configuración de máquina dinámico (RFC 2131).
Parámetros de configuración de un servidor DHCP:
- Rango de direcciones IP disponibles.
- Valor de la máscara de red. 
- Dirección IP de la puerta de enlace por defecto. 
- Direcciones de los servidores DNS. Servidores que traducen el nombre de dominio de una máquina y su dirección IP.
### Mensajes
- **DHCP DISCOVER**: Cliente a MAC de difusión, informando a los servidores DHCP existentes de que necesita una IP.
- **DHCP OFFER**: Servidor al cliente, informando de una configuración disponible. 
- **DHCP REQUEST**: Cliente a MAC de difusión, informando a los servidores DHCP la configuración IP que se solicita. 
- **DHCP ACK**: Servidor a cliente, informando de que se le asigna y reserva por un tiempo la configuración IP. Cuando expira el tiempo de reserva (lease time) el cliente tiene que renovarlo con un paquete DHCP Request y recibir un DHCP ACK.
- **DHCP RELEASE**: Cliente a servidor, informando de que ya no necesita la configuración DHCP para que la libere.
# Congestionamiento en redes IP
## Causas del congestionamiento
- **Routers con insuficiente capacidad de proceso**. Se necesitará aumentar la capacidad de los encaminadores de la red si va a aumentar el flujo de paquetes.
- **Fragmentación de la información con el protocolo IP**. Si el protocolo IP fragmenta los paquetes a gran escala (MTU pequeño en la red), los routers necesitan más tiempo para el encaminamiento que con un MTU más grande, ya que tienen que analizar más cabeceras IP.
## Detección del congestionamiento
- **Routers con insuficiente capacidad de proceso**. Hay que monitorizar cuál es el porcentaje de uso de la CPU de los routers. Si es superior al 60-70% hay que utilizar un router de mayores prestaciones.
- **Fragmentación de la información con el protocolo IP**. Hay que verificar que los MTU de la red estén elegidos adecuadamente y que la fragmentación se evita con mecanismos como la norma RFC 1191. Detectando mensajes ICMP Source Quench o Fragment Reassembly Time Exceeded se conoce si la fragmentación está provocando efectos nocivos en la red.
## Corrección del congestionamiento
La única solución es **reducir el flujo de entrada de paquetes a la red**.
Esta estrategia la utiliza el protocolo TCP, que permite el envío de un número máximo de paquetes sin esperar a los ACK. En caso de que los ACK no lleguen TPC es capaz de reducir su flujo de transmisión.
# Sistemas Autónomos (SA)
**SISTEMA AUTÓNOMO**: Conjunto de redes y routers controlados por una única autoridad administrativa (un único gestor de políticas de encaminamiento). 
**POLÍTICA DE ENCAMINAMIENTO**: Conjunto de estrategias o directrices para decidir los caminos óptimos a seguir en una red. 

Encaminamiento a dos niveles: 
## Encaminamiento entre SA (Sistemas Autónomos):
### [[BGP|Protocolo BGP]]
BGP - Border Gateway Protocol.
- La información de encaminamiento se intercambia utilizando conexiones TCP entre routers frontera.
- **BGP** informa sobre la alcanzabilidad y conectividad entre SA (que redes pertenecen a que sistemas autónomos).
- **BGP** reduce la información intercambiada comunicando una sola vez las redes accesibles a través de un SA y actualiza la información que se modifica. Agrupa destinos en una sola denominación.
- **BGP** soporta autenticación para preservar la validez de la información del encaminamiento. 
#### Mensajes
- **BGP Open**: Primer mensaje entre dos routers frontera que establecen la conexión TCP. Intercambian parámetros como el identificador del SA, intervalos de tiempo de envío de mensajes...
- **BGP Update**: Informa acerca de destinos existentes en el SA y destinos que se han eliminado del SA.
- **BGP Keepalive**: Informa de que un extremo de la comunicación sigue activo ya que TCP no controla que los dos extremos estén activos cuando no intercambian datos.
- **BGP Notification**: Informa sobre errores en la comunicación BGP (mensajes BGP con errores: rutas incorrectas o incongruentes) y permite el control en la comunicación.

![[Temas Redes.pdf#page=214]]
#### Conclusiones
- BGP solo informa de accesibilidad, no de rutas a seguir o de menor coste. 
- BGP establece conexiones entre pares de routers frontera.
- BGP informa sobre destinos existentes y no existentes, evitando la presencia de mensajes ICMP Destination Unreachable entre diferentes ISPs (Internet Service Provider).

En encaminamiento estático en la red no es adecuado, para ello se introduce un mecanismo de configuración y actualización de tablas de encaminamiento automático. 
## Encaminamiento dentro de SA (Sistemas autónomos):
### [[RIP|Protocolo RIP]]
RIP - Routing Information Protocol. 
Basado en un algoritmo de vector de distancia - **Algoritmo Bellman-Ford**.
- Cada router tiene una tabla con información de destinos y una métrica para alcanzarlos.
- Cada router propaga la información de sus rutas conocidas a través de mensajes en la red, y los routers que la reciben actualizan sus tablas si encuentran rutas más cortas a un mismo destino.

- Para cada entrada en la tabla de rutas hay un temporizador (180 segundos). Si la ruta no es informada de nuevo en ese tiempo se elimina.
- Existe un número máximo de saltos para la métrica RIP, **16**. Esto permite llegar a una solución estable. 
#### RIP v1
Los mensajes RIP con información de las rutas de datos se envían dentro de paquetes [[UDP]].
- El envío de mensajes RIP a la dirección de broadcast hace que las máquinas que no soportan RIP procesen paquetes hasta la capa de transporte (UDP). 
Para solventar estos problemas se introduce la versión 2 de RIP.
#### RIP v2
Los mensajes RIP son enviados a la dirección IP **224.0.0.9** (dirección IP de [[Multicasting|multicast]]). 
- RIP permite el encaminamiento dinámico en redes de tamaño pequeño (hasta 16 saltos) con una estructura sencilla (inexistencia de muchos bucles). 
- RIP presenta problemas de convergencia lenta ante cambios en la red y posibilidad de que se introduzcan bucles infinitos. Para evitar esto emplea estrategias como temporizadores y un número máximo de saltos.
#### Conclusiones 
RIP permite el encaminamiento dinámico en redes pequeñas. 
RIP presenta problemas de convergencia lenta ante cambios en la red y posibilidad de que se introduzcan bucles infinitos. Para evitar esto se introducen temporizadores y número máximo de saltos. 
### [[OSPF|Protocolo OSPF]]
OSPF - Open Shortest Path First.
RIP sólo tiene en cuenta el número de saltos, pero no la velocidad de transferencia, por lo que las rutas con menos saltos no tienen porque ser las más rápidas.

OSPF se fundamenta en el estado del enlace, asignando un coste dependiendo de las características del enlace (alta velocidad, baja velocidad, activado, desactivado, etc.). 
OSPF utiliza el algoritmo de Dijkstra para determinar las rutas de menor coste en la red.
El conjunto de routers de una red que emplean OSPF conforman un grafo, donde se determinan las rutas más cortas entre cualquier par de nodos (router, o en definitiva redes) del grafo (red).

OSPF utiliza varias direcciones [[Multicasting|multicast]] para diferentes tipos de mensajes de enrutamiento. 
Los mensajes OSPF se encapsulan en paquetes dirigidos a la dirección de **multicast 224.0.0.5** (todos los routers OSPF) y **224.0.0.6** (routers OSPF designados).
#### Mensajes
- **OSPF Hello**: Permite determinar qué vecinos tiene accesible un router. 
- **OSPF Database description**: Informa de la topología de la red de comunicaciones.
- **OSPF Link status request**: Permite solicitar a los routers vecinos información acerca de los enlace activos. 
- **OSPF Link status update**: Un router informa a sus vecinos del estado de sus enlaces.
# Multicasting
Las **direcciones multicast** son direcciones IP especiales que se utilizan para enviar datos desde un único emisor a múltiples receptores de forma simultánea. 
Una dirección IP normal se utiliza en comunicaciones **punto a punto**, pero una multicast se utilizan para comunicaciones **uno a muchos**.

| *Dirección multicast* | *Denominación del grupo*       |
| --------------------- | ------------------------------ |
| 224.0.0.0             | Reservada                      |
| 224.0.0.1             | Todos los equipos de la subred |
| 224.0.0.2             | Todos los routers en la subred |
| 224.0.0.5             | Routers OSPF                   |
| 224.0.0.6             | Routers OSPF designados        |
| 224.0.0.9             | Routers RIPv2                  |

Existe una restricción, y es que los paquetes dirigidos a grupos de gestión de encaminamiento (desde la dirección **224.0.0.1** a la **224.0.0.255**) no son propagados nunca (para evitar congestionamiento y problemas de convergencia de los algoritmos de encaminamiento).
# IPv6 (RFC 2460)
- IPv6 introduce direcciones IP de 128 frente a las de 32 del IPv4.
- IPv6 no permite la fragmentación de un paquete IP en un router intermedio, solo en el router origen, y es este el que determina el MTU mínimo en el camino de origen a destino. (valor mínimo para redes IPv6, 1280 bytes).
- Es más eficiente que IPv4.
## Cabecera IPv6
Es de 40 bytes. 
Tiene una parte fija, común a todos los paquetes, un conjunto de cabeceras de extensión y la PDU (Protocol Data Unit - Unidad de Datos de un Protocolo) del nivel superior.
### Cabeceras de extensión
- Cabecera de opciones salto a salto. Define las acciones que debe tomar cada router que atraviesa el paquete.
- Cabecera de encaminamiento. Proporciona un encaminamiento adicional, similar al encaminamiento origen en IPv4.
- Cabecera de fragmentación. Fragmentación en el origen, el destinatario se encarga de reensamblar el paquete. 
- Cabecera de opciones para el destino. Información a examinar por el nodo destino. 
- Cabecera de autenticación y encapsulado de seguridad. Cabeceras AH, ESP de IPSEC (cifrado y autenticación de paquetes IP).

El número permitido de saltos es igual que para IPv4.
IPv6 permite tres tipos de dirección IP:
### Direcciones de unidifusión (unicast)
Identifican a una interfaz individual.
### Direcciones de multidifusión (multicast)
Identifican a un conjunto de interfaces que pertenecen a un grupo definido.
### Direcciones de monodifusión (anycast)
Identifican a un conjunto de interfaces que pertenecen a un grupo, pero el paquete solo se entrega a la interfaz más cercana.
## Notación IPv6
En las direcciones Ipv6 hay 8 grupos de 4 dígitos hexadecimales. Los grupos que contienen 0 se sustituyen por un doble : .

Las direcciones MAC normales tienen un valor de 48 bits divididos en dos grupos de 24, de los cuales, los 24 primeros corresponden con el fabricante y el resto son los de la interfaz.
En las MAC para IPv6 los primeros 24 bits corresponden con el proveedor o fabricante, luego se añaden 16 bits a valor fijo y luego los 24 de la interfaz. 
Cualquier dispositivo conectado a una IPv6 tiene un valor **dinámico** pero **único** y **reservado** para su red. 
# Transición IPv4 - IPv6
- Un dispositivo IPv4 solo puede tener conectividad con dispositivos IPv4.
- Cuando la conectividad es entre equipos con la misma versión (IPv4 o IPv6) y deben atravesar una red intermedia con una versión IP distinta, se recurre al procedimiento del túnel. 
## Procedimiento del túnel
Se encapsula un paquete IPv4 (IPv6) como dato dentro de un paquete IPv6 (IPv4) para su transporte a esa red intermedia. 