Objetivo. Mejorar el aprovechamiento del canal de comunicación enviando datos aunque no se reciban los ACK.
- **Lista del emisor**: Secuencias de numeración de los paquetes de datos. Si la numeración es con 3 bits el número de secuencias es 8 (0-1-2-3-4-5-6-7).
- **Lista del receptor**: Secuencias de numeración de los asentimientos de paquetes de datos. Si la numeración es con 3 bits el número de secuencias es 8 (0-1-2-3-4-5-6-7).
Definiciones:
- **Ventana del emisor**: Secuencias de numeración de los paquetes que transmite el emisor y de los que no recibe el ACK correspondiente a cada uno. 
- **Ventana del receptor**: Secuencias de numeración de los paquetes que el receptor espera recibir y de los que envía el ACK. 
- **Tamaño de ventana del emisor ($W_e$)**: Número de secuencias en la ventana del emisor. 
- **Tamaño de ventana del receptor ($W_r$)**: Número de secuencias en la ventana del receptor. 
#### Funcionamiento
![[Temas Redes.pdf#page=120]]

El tamaño de la ventana del *emisor* **VARÍA**, la del *receptor* es **CONSTANTE**.
#### Protocolo de ventana deslizante con numeración de 1 bit
$W_e = 1$, $W_r = 1$.
#### Protocolo de ventana deslizante con repetición no selectiva
$W_r = 1$ SIEMPRE.
#### Protocolo de ventana deslizante con repetición selectiva
$W_r > 1$ SIEMPRE.
Medio full-duplex.
