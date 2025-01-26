Confirmación tras envío de datos por parte del receptor por cada bloque de datos enviado para poder continuar la transmisión. 
#### Tiempo de transmisión ($T_t$)
Tiempo necesario para enviar todos los bits de una trama desde el emisor al receptor. Dado por la longitud de la trama dividida por la velocidad de transmisión del canal .
#### Tiempo de Propagación ($T_p$)
Tiempo que se toma para que un bit viaje desde el emisor al receptor a través del medio de comunicación. 
#### Relación tiempo de transmisión y tiempo de propagación
$$ a=\frac{T_p}{T_t} $$
Si a > 1 el $T_p$ > $T_t$, lo que significa que algunos bits alcanzan al receptor antes de que el emisor termine de transmitir toda la trama. 
Si a < 1 el $T_p$ < $T_t$, lo que significa que el emisor y el receptor están más sincronizados reduciendo el tiempo de espera y aumentando la eficiencia del canal. 
#### Protocolo unilateral de parada y espera. Canal sin errores
Envío de datos - ACK respuesta.
#### Protocolo unilateral de parada y espera. Canal con errores
Desde el envío del paquete en el emisor hasta la llegada del paquete de confirmación (ACK) se define el tiempo de espera de ACK. 
Si el ACK sufre una pérdida, no llega al emisor y este reenvía el paquete, lo que provoca un duplicado en el receptor.
Si hay un retardo en el envío de ACK pueden reenviarse antes los datos y generar duplicados.