## Teorema de Nyquist
$$Vt_{(max)} = 2·B·\log_2(n)\, bps$$
## Teorema de Shannon
$$Vt_{(max)} = B·\log_2(1+\frac{P_s}{P_n})\, bps$$

$\frac{P_s}{P_n}$ = Proviene de la relación señal - ruido.
$B$ = Ancho de banda
$$s-r=10·\log_{10}(\frac{P_s}{P_n})\, db$$
Si la $V_t > V_m$ hay que aumentar los niveles de tensión.
## Velocidad de modulación

$$V_m = \frac{1}{T_m} = f_m$$
### Modulación digital TDM
Cálculo de frecuencia fundamental y componentes frecuenciales específicas. 
$$\frac{1}{T} \begin{cases} Transmisión\,períodica\,\, T=\frac{\Large{nº\,bits}}{\Large {V_t}} \\\\  Transmisión\,continua\,\, T=\frac{\Large{nº\,pulsos}}{\Large {V_m}} \end{cases} $$
- Ejemplo: 
Período de repetición de 4 bits - secuencia de datos 0001. 4 Niveles de tensión, cada 2 bits -> 1 pulso -> Período es de 2 pulsos.
### Modulación digital PCM
$q$ = número de niveles de cuantización 
$b$ = número de bits de codificación para los niveles q
$$q= 2^b$$
$$V_t = b·2·B\, bps$$



___

## Fibra multimodo de índice de salto 
A mayor distancia, mayor **dispersión intermodal**. Esto obliga a reducir la velocidad de transmisión en el medio.
## Fibra multimodo de índice gradual
Los pulsos tienen limitada su **dispersión intermodal** independientemente de la distancia de la fibra óptica.
Permiten alcanzar velocidades superiores a la Fibra multimodo de índice de salto. 
