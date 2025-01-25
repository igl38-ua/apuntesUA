Protocolo de nivel de enlace, comunicación virtual horizontal.
## Servicio sin conexión y sin reconocimiento
- Baja tasa de error
- Más importante el retardo que la fiabilidad
- **Ethernet**.
## Servicio sin conexión y con reconocimiento
- Tasa de error considerable. 
- Solo confirmación de envío de información
- **Wi-Fi (IEEE 802.11)**.
## Servicio con conexión y con reconocimiento
- Tasa de error considerable. 
- Control de flujo: ordenación de paquetes y envío correcto.
- **HDLC (fuera de uso)**.
# Funciones del nivel de enlace
## Delimitación de tramas
Identificación del inicio y fin de un paquete.
## Direccionamiento
Identificación de los extremos de la comunicación en un medio físico. 
## Control de errores
Asegura transmisión sin errores debidos al medio físico.
## [[!Mecanismos de verificación de tramas]]
### [[FCS (Frame Check Sequence)]]
### [[Paridad]]
### [[CRC (Cyclic Redundancy Check)]]
### [[Suma de verificación (Checksum)]]
## Control del fujo 
Control del flujo de tramas entre emisor y receptor para evitar congestiones, reenvíos incorrectos, etc.
- Controlar el envío y recepción correcto de los paquetes de nivel enlace.
- Controlar la sincronización del emisor y el receptor.
- Evitar congestiones en el envío de información del emisor al receptor.
### [[Protocolos de parada y espera]]
### [[Protocolos de ventana deslizante]]
# [[Redes LAN 1 - Normas IEEE 802.X]]
# [[Redes LAN 1.1 - IEEE 802.11x LAN Inalámbricas]]
# [[Estándares de redes LAN]]