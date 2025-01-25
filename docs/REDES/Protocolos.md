- OSPF (Open Shortest Path First) -> direccionamiento enlace-estado. Basado en el algoritmo SPF. Para protocolos RIP.

- Para IPv6 e IPv4 las máscaras de red son variables.
- IPv6 simplifica los algoritmos de encaminamiento respecto a IPv4
- Sistema de cabeceras más flexible que IPv4. Soporta monodifusión (anycast)

- BGP no tiene en cuenta los valores de métrica (Border Gateway Protocol)
- Prioridad de paquete IPv6 -> Cabecera propia
- BGP establece políticas de enrutamiento utilizando parámetros de ruta o atributos.
- BGP emplea la capa de transporte para informar de las tablas de encaminamiento del resto de routers.

Se permite el intercambio de paquetes IPv4 a través de redes IPv6
- En el protocolo RIP se informa de todos los destinos conocidos a todos los routers a los que está conectado.
- Para la red 224.0.0.255 los paquetes enviados solo son procesados por ese grupo de multidifusión. 
- Esos routers BGP tienen un conocimiento global de los SA (Sistemas Autónomos) de Internet. 
Los protocolos de encaminamiento OSPF y RIPv2 tienen algunas características comunes, como por ejemplo
- Pueden utilizar la multidifusión para enviar mensajes de información a todos los routers de una red LAN. 

## ARP
El protocolo ARP utiliza las direcciones MAC para identificar los dispositivos en la red local.

La ecuación proporcionada en notación LaTeX es:

$$ s = \sqrt{ \frac{\sum_{i=1}^{n} ( \text{retardo} - \text{retardo}_i )^2}{n-1} } $$
## TCP y UDP
Valores tipos de paquete:
- SYN (1)
- FIN (1)
- ACK (0)
- RST (1)
El protocolo TCP tiene 3 fases, conexión, datos y desconexión.
En la comunicación de dos tramas A y B se intercambian los paquetes:
- Conexión:
	- SYN A-B, para iniciar la conexión.
		- SEQ = 1 (valor del numero de secuencia, generalmente aleatorio).
	- SYN, ACK B-A para la conexión de B y la confirmación de conexión de B.
		- SEQ = 10
		- ACK = 1 + SEQ -> 2
	- ACK A-B, confirmación de conexión de A.
		- SEQ = 2
		- ACK = 1 + SEQ -> 11
- Datos:
	- DATOS (1000B).
		- SEQ = 2 (porque al enviar un ACK no se envían datos, en caso contrario ese valor cambiaria).
		- ACK = 11 (no ha habido más confirmaciones).
	- ACK.
		- SEQ = 11
		- ACK = 2 + 1000 -> 1002
- Fin:
	- FIN.
		- SEQ = 1002
		- ACK = 11 
	- FIN, ACK.
		- SEQ = 11
		- ACK = 1002 +1 -> 1003
	- ACK.
		- SEQ = 1003
		- ACK = 11 + 1 -> 12
### Cabeceras
En una conexión TCP al recibir un paquete TCP, después del proceso de conexión, el paquete necesita tener las cabeceras IP y ETH. Pero no se puede enviar porque en MTU de las redes ethernet es 1500. 
Un paquete TCP tiene que llegar a su destino sin ser fragmentado para que la red no sufre congestión. Se establece el MSS (cantidad máxima de datos de un paquete TCP).
MSS = MTU - IP - TCP
MSS = 1500 - 20 - 20 -> 1460 
Ese será el tamaño máximo de los paquetes TCP.

MSS_datos = min{MSS_A, MSS_B}

En la conexión, si se da el caso de que los paquetes tiene que atravesar una red intermedia el bit DF (don't fragment) debe estar activo a 1. Si estuviera activo, la máquina generaría un mensaje ICMP de error. La máquina sabe el paquete TCP que sufre el error porque en cabecera los 28 bytes, 20 son de la cabecera IP y los 8 restantes son los 8 primeros bytes de la cabecera TCP.
