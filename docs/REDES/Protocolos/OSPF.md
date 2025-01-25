OSPF - Open Shortest Path First

*Encaminamiento dentro de SA (Sistemas autónomos)*
RIP sólo tiene en cuenta el número de saltos, pero no la velocidad de transferencia, por lo que las rutas con menos saltos no tienen porque ser las más rápidas.

OSPF se fundamenta en el estado del enlace, asignando un coste dependiendo de las características del enlace (alta velocidad, baja velocidad, activado, desactivado, etc.). 
El conjunto de routers de una red que emplean OSPF conforman un grafo, donde se determinan las rutas más cortas entre cualquier par de nodos (router, o en definitiva redes) del grafo (red).

OSPF utiliza varias direcciones [[Multicasting|multicast]] para diferentes tipos de mensajes de enrutamiento. Por ejemplo, en **OSPFv2**, la dirección multicast **IPv4 224.0.0.5** se utiliza para enviar mensajes de estado de enlace (LSU), que contienen información sobre la topología de la red. Esta información incluye detalles sobre los enlaces, como los identificadores de los routers vecinos, los costos de los enlaces y otras métricas.

Además, OSPFv2 también utiliza la dirección multicast **IPv4 224.0.0.6** para enviar mensajes de estado de enlace resumidos (LSAck), que son confirmaciones de los mensajes LSU recibidos.