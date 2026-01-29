Análisis de las **características** de las técnicas de multiplexado (FDM, WDM, TDM) y las técnicas de modulación (ASK, PSK, FSK, QPSK y QAM) en términos de **rendimiento**, **velocidad**, y **coste**:
___
## Técnicas de Multiplexado
### 1. Multiplexación por División de Frecuencia (FDM):
- **Rendimiento**:
    - Depende del ancho de banda disponible y la cantidad de bandas asignadas. Es menos eficiente si se requieren bandas de guarda grandes para evitar interferencias.
- **Velocidad**:
    - Moderada; limitada por el ancho de banda físico del medio (ej. cable coaxial o espectro de radio).
- **Coste**:
    - Relativamente bajo, ya que es una técnica establecida y simple, con menor complejidad en los equipos.
### 2. Multiplexación por División de Longitud de Onda (WDM):
- **Rendimiento**:
    - Muy alto, especialmente con **DWDM** que permite densidades extremas de longitudes de onda. Escalable y eficiente.
- **Velocidad**:
    - Altísima; puede alcanzar decenas de terabits por segundo en una sola fibra óptica.
- **Coste**:
    - Alto, debido a la precisión requerida en los multiplexores/demultiplexores y en los transceptores ópticos.
### 3. Multiplexación por División de Tiempo (TDM):
- **Rendimiento**:
    - Síncrona: Eficiencia baja si las fuentes no están transmitiendo continuamente.
    - Estadística: Mucho más eficiente, ya que los intervalos se asignan según demanda.
- **Velocidad**:
    - Moderada; depende de la capacidad del medio físico y de la cantidad de intervalos disponibles.
- **Coste**:
    - Moderado; menos costoso que WDM, pero más complejo que FDM.

___
## Técnicas de Modulación
### 1. Amplitude Shift Keying (ASK):
- **Rendimiento**:
    - Bajo; susceptible a ruidos e interferencias, ya que se basa en cambios de amplitud, que son más fáciles de alterar.
- **Velocidad**:
    - Moderada; limitada por la capacidad del medio y la precisión en la detección de amplitud.
- **Coste**:
    - Bajo; es simple de implementar.
### 2. Frequency Shift Keying (FSK):
- **Rendimiento**:
    - Mejor que ASK, ya que es menos susceptible al ruido al codificar los datos en frecuencias.
- **Velocidad**:
    - Moderada; depende de la separación entre frecuencias utilizadas.
- **Coste**:
    - Moderado; requiere un oscilador para generar múltiples frecuencias.
### 3. Phase Shift Keying (PSK):
- **Rendimiento**:
    - Alto; más resistente al ruido que ASK y FSK, ya que usa cambios en la fase.
- **Velocidad**:
    - Alta; permite transmitir más datos con menos recursos físicos en comparación con ASK y FSK.
- **Coste**:
    - Moderado; más complejo de implementar debido al procesamiento de fase.
### 4. Quadrature Phase Shift Keying (QPSK):
- **Rendimiento**:
    - Muy alto; transmite 2 bits por símbolo al utilizar 4 estados de fase.
- **Velocidad**:
    - Alta; permite mayor eficiencia espectral que PSK.
- **Coste**:
    - Moderado; requiere mayor complejidad en la demodulación.
### 5. Quadrature Amplitude Modulation (QAM):
- **Rendimiento**:
    - Muy alto; combina amplitud y fase para transmitir más bits por símbolo.
    - Ejemplo: **16-QAM** (4 bits/símbolo), **64-QAM** (6 bits/símbolo).
- **Velocidad**:
    - Altísima; excelente eficiencia espectral, ideal para aplicaciones de alta velocidad.
- **Coste**:
    - Alto; la complejidad de implementación aumenta con el número de estados.

___
## Comparación General

| **Técnica**           | **Rendimiento** | **Velocidad** | **Coste** |
| --------------------- | --------------- | ------------- | --------- |
| **FDM**               | Moderado        | Moderada      | Bajo      |
| **WDM**               | Muy alto        | Altísima      | Alto      |
| **TDM (Síncrona)**    | Bajo a Moderado | Moderada      | Moderado  |
| **TDM (Estadística)** | Alto            | Moderada      | Alto      |
| **ASK**               | Bajo            | Moderada      | Bajo      |
| **FSK**               | Moderado        | Moderada      | Moderado  |
| **PSK**               | Alto            | Alta          | Moderado  |
| **QPSK**              | Muy alto        | Alta          | Moderado  |
| **QAM**               | Muy alto        | Altísima      | Alto      |

___
## Conclusión
- **FDM** y **TDM** son más simples y económicas, adecuadas para aplicaciones menos exigentes en cuanto a velocidad.
- **WDM** es ideal para entornos de alta velocidad y capacidad (como fibra óptica).
- Entre las técnicas de modulación, **QAM** ofrece el mejor rendimiento y velocidad, pero a un costo más alto, mientras que **ASK** es la más sencilla y económica, aunque menos eficiente.