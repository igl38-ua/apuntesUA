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
## [Mecanismos de verificación de tramas](MVT/!MVT.md)
### [FCS (Frame Check Sequence)](MVT/FCS%20(Frame%20Check%20Sequence).md)
### [Paridad](MVT/Paridad.md)
### [CRC (Cyclic Redundancy Check)](MVT/CRC%20(Cyclic%20Redundancy%20Check).md)
### [Suma de verificación (Checksum)](MVT/Suma%20de%20verificación%20(Checksum).md)
## Control del fujo 
Control del flujo de tramas entre emisor y receptor para evitar congestiones, reenvíos incorrectos, etc.
- Controlar el envío y recepción correcto de los paquetes de nivel enlace.
- Controlar la sincronización del emisor y el receptor.
- Evitar congestiones en el envío de información del emisor al receptor.
### Protocolos de parada y espera 
[Parada y espera](Protocolos de parada y espera.md)
### Protocolos de ventana deslizante
[Ventana deslizante](Protocolos de ventana deslizante.md)
# [Redes LAN 1 - Normas IEEE 802.X](Redes LAN 1 - Normas IEEE 802.X.md)
# [Redes LAN 1.1 - IEEE 802.11x LAN Inalámbricas](Redes LAN 1.1 - IEEE 802.11x LAN Inalámbricas.md)
# [Estándares de redes LAN](Estándares de redes LAN.md)