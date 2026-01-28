# Nomenclatura
## Infrastructure BSS
Red inalámbrica con puntos de acceso.
## Independent BSS (IBSS)
[Red inalámbrica ad-hoc](#red-inalambrica-ad-hoc).
# Red inalámbrica ad-hoc
### SSID
**Service Set Identifier**. Identificador de BSS.
### BSSID
**Basic Service Set Identifier**. SSID en redes ad-hoc.
### ESSID 
**Extended Service Set Identifier**. SSID en redes de infraestructura.
# Red inalámbrica de infraestructura
### AP
Access Point. Actúa como un puente entre la LAN de cable y un BSS. 
# Normativas
### IEEE 802.11b
Comunicación inalámbrica empleando una señal portadora de **2.4 GHz**.
### IEEE 802.11n (Wi-Fi 4) 
Permite emplear la portadora de **2.4 GHz** y la de **5 GHz** (19 canales) consiguiendo velocidades de hasta 600 Mbps.
### IEEE 802.11ac (Wi-Fi 5)
Emplea solamente la portadora de **5 GHz** (19 canales) y varias antenas, consiguiendo velocidades de hasta 1.3 Gbps.
### IEEE 802.11ax (Wi-Fi 6) 
Permite emplear la portadora de **2.4 GHz y 5 GHz**, modulación con elevado número de niveles (**QAM**-1024) y varias antenas, consiguiendo velocidades de hasta 10 Gbps.
### IEEE 802.1x.	
WPA–Enterprise
### IEEE 802.11i
WPA2
# Acceso al medio
Las redes LAN 802.11 se caracterizan por una elevada tasa de error en el medio físico. Dos modos de funcionamiento para el uso del medio físico:
## DCF - Función de coordinación distribuida
Mecanismo de reparto **CSMA/CA**. Las estaciones comprueban si el medio físico está libre detectando una señal **CCA** (Estimación de desocupación del canal). 

Para evitar el problema de la estación oculta, la estación que transmite envía un paquete **RTS** que indica a las demás estaciones visibles el tiempo durante el que no pueden transmitir (**NAV** - Vector de reserva de la red).
El receptor confirma con un paquete **CTS** que indica a las demás estaciones visibles el tiempo durante el que no pueden transmitir. 
## PCF - Función de coordinación centralizada
Precisa de la existencia de un **AP**. 
Para que un equipo conozca la existencia de una red inalámbrica el AP envía un paquete denominado trama de baliza o señalización **(beacon frame)** indicando el valor SSID de la red inalámbrica.  
No existen colisiones. 

___
# Seguridad en redes Wi-Fi
Métodos de autenticación y cifrado.
### WEP
Wired Equivalence Privacy.
Basado en el algoritmo de cifrado RC4. 
Su funcionamiento está basado en el conocimiento de una misma clave secreta por parte de la estación y el AP, la **PSK** - Pre-Shared Key.
Clave secreta de 64 a 128 bits.
### WPA
Wifi Protected Access.
Mantiene el mismo cifrado que WEP pero añade el mecanismo **TKIP** (Temporal Key Integrity Protocol).
La solución a los problemas de seguridad y aleatoriedad de WPA se soluciona con **WPA2**.
#### WPA-Personal o WPA-PSK
Clave PSK de al menos 20 caracteres. 
#### WPA-Enterprise
Emplea un servidor de autenticación. 
La base de su funcionamiento es el protocolo de autenticación **EAP** (Extensible Authentication Protocol). Tres mecanismos de autenticación:
- **EAP/TLS**: certificado servidor-cliente. 
- **EAP/TTLS o PEAP**: certificado de servidor RADIUS.
- **LEAP**: Lightweight EAP. Mecanismo CHAP del servidor RADIUS.
Todos tienen el objetivo de proporcionar al usuario la **MK** - Master Key, clave primaria de inicio de TKIP.
### IEEE 802.11i - WPA2
Cifrado **AES** de **128** bits.
### Wi-fi certified WPA3
Cifrado **AES** de **192** bits
