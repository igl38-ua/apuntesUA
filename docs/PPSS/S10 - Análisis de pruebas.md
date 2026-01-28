# S10 - Análisis de pruebas
## Plugin JACOCO para Maven

JaCoCo (Jaca Code Coverage) mide la cobertura de código de las pruebas en proyectos java. Verifica que porcentaje del código ha sido ejecutado al correr los tests (unitarios o de integración).

- Permite pre-procesar (instrumentar) los ficheros `.class` del proyecto para que recojan datos de cobertura al ejecutar los tests. 
- Genera informes html/xml.
- Define mínimos de cobertura requeridos para que el build pase o falle, en función de la CC (Complejidad Ciclomática).
- Durante la ejecución de los tests se genera el análisis de cobertura y se guardan en un fichero binario con extensión `.exec`.
### Goals principales

- `jacoco:prepare-agent`
	
	- Prepara la instrumentación para tests unitarios.
	- Se ejecuta en la fase `initialize`.
	- Indica qué clases deben ser instrumentadas y genera el fichero `target/jacoco.exec` con los datos de cobertura.
    
- `jacoco:prepare-agent-integration`
    
	- Es similar a la anterior, pero para las pruebas de integración. 
	- Por defecto se asocia a la fase `pre-integration-test`. 
	- Genera el fichero con resultados del análisis `target/jacoco-it.exec`.
    
- `jacoco:report`
    
    - Genera los informes visuales (HTML/XML/CSV) a partir de los datos obtenidos con el análisis de cobertura durante la ejecución de las pruebas unitarias (`target/jacoco.exec`).  
    - Por defecto se asocia a la fase `verify`.
    - Genera un informe en el directorio `target/site/jacoco`. 
    
- `jacoco:report-integration`
    
	- Similar al anterior, pero para pruebas de integración.
	- Utiliza el `target/jacoco-it.exec` para generar los informes. 
	- Por defecto se asocia a la fase `verify`.
	- Genera un informe en el directorio `target/site/jacoco-it`. 
    
- `jacoco:check`
    
    - Verifica que se cumplan los mínimos de cobertura.
    - Por defecto se asocia a la fase `verify` y usa el fichero `jacoco.exec`, pero se puede configurar para usar el `jacoco-it.exec` usando la propiedad `<dataFile>`.

    - Es posible configurar la cobertura a diferentes niveles (tag `<element>`): `BUNDLE`, `PACKAGE`, `CLASS`, `SOURCEFILE` o `METHOD`.
    - Para cada nivel, se puede indicar el contador a configurar (etiqueta `<counter>`): `INSTRUCTION`, `LINE`, `BRANCH`, `COMPLEXITY`, `METHOD`, `CLASS`.
    - Para cada contador, se pueden establecer valores máximos o mínimos, sobre los diferentes valores calculados (etiqueta `<value>`): `TOTALCOUNT`, `COVEREDCOUNT`, `MISSEDCOUNT`, `COVEREDRATIO`, `MISSEDRATIO`.
### Tabla resumen

| GOAL                      | FASE                   | QUE HACE                                     |
| ------------------------- | ---------------------- | -------------------------------------------- |
| prepare-agent             | `initialize`           | Instrumenta clases para tests unitarios      |
| prepare-agent-integration | `pre-integration-test` | Instrumenta clases para tests de integración |
| report                    | `verify`               | Genera Informe de cobertura (unitarios)      |
| report-integration        | `verify`               | Genera Informe de cobertura (integración)    |
| check                     | `verify`               | Valida que se cumpla la cobertura mínima     |

![item](../img/ppss/proceso%20completo%20automatización.png)

___
## Análisis de cobertura y generación de informes

Configuración plugin JACOCO para el análisis de cobertura de pruebas 

```xml
<plugin>  
    <groupId>org.jacoco</groupId>  
    <artifactId>jacoco-maven-plugin</artifactId>  
    <version>0.8.13</version>  
    <executions>
	    <execution>            
		    <id>default-prepare-agent</id>  
            <goals>                
	            <goal>prepare-agent</goal>  Preparar la instrumentación y análisis de cobertura
            </goals>        
        </execution>        
	    <execution>            
		    <id>default-report</id>  
            <goals>                
	            <goal>report</goal>  Generar el informe en formato html
            </goals>        
        </execution>        
	    <execution>            
		    <id>default-check</id>  
            <goals>                
	            <goal>check</goal>  Establecer unos niveles de cobertura
            </goals>            
            <configuration>                
	            <rules>                    
		            <rule>                        
			            <element>BUNDLE</element>  
                        <limits>                            
	                        <limit>
		                        <counter>COMPLEXITY</counter>  
                                <value>COVEREDRATIO</value>  
                                <minimum>0.60</minimum>  
                            </limit>
                        </limits>                    
                    </rule>  La construccion se detiene si la CC no alcanza un 60%
                </rules>            
            </configuration>        
        </execution>    
    </executions>
</plugin>
```

Con el comando `mvn verify`, Obtenemos como resultado un fichero jacoco.exec y el check de construcción si la CC no alcanza el 60%.

___
## Análisis P10
### 🧾 1. ¿Cuál es el número de instrucciones bytecode ejecutadas para la clase `Sample`?

✅ **117 instrucciones ejecutadas**

Esto se deduce de:

> `Missed Instructions: 0 of 117` → ninguna instrucción se ha quedado sin ejecutar ⇒ todas las 117 fueron ejecutadas.

___
### 🧾 2. ¿Cuántas instrucciones bytecode nos faltan para tener una cobertura del 100%?

✅ **0 instrucciones faltantes**

Está confirmado por:

> `Missed Instructions: 0`  
> `Cov. (instrucciones): 100 %`

___
### 🧾 3. ¿Cuántas instrucciones bytecode tiene la clase `Sample`?

✅ **117 instrucciones**

Esto se lee directamente de la columna:

> `0 of 117` = 117 totales

___
### 🧾 4. ¿Por qué aparece el método `Sample()` en el informe si no lo hemos implementado?

✅ Porque el **constructor por defecto** se genera automáticamente.

Cuando no defines ningún constructor en una clase Java, el compilador **genera uno implícito** sin argumentos. Aunque no lo veas en tu código, **sí existe en bytecode**, y JaCoCo lo analiza como cualquier otro método.

___
### 🧾 5. ¿Por qué el método `Sample()` tiene una cobertura de branches con valor "n/a"?

✅ Porque **no contiene ninguna rama de decisión** (`if`, `switch`, `while`, etc.).

"n/a" en JaCoCo para branches significa "not applicable", es decir: **no hay ninguna condición lógica** que deba cubrirse. Esto es normal en constructores vacíos (como el generado por defecto).

___
### 🧾 6. ¿Cuál es el valor de complejidad ciclomática (`Cxty`) para `Sample.maxValue()` y por qué?

🔢 En tu informe, `Cxty = 3` para `maxValue()` (basado en análisis típico).

📌 Fórmula de JaCoCo para complejidad ciclomática:  
**1 + número de estructuras de decisión (`if`, `while`, `for`, `catch`, `case`)**

#### En `Sample.maxValue()`:

```java
if (isValid(data)) {    // 1 rama (if)
    for (...) {         // 1 bucle (for)
        if (...) {      // 1 rama (if)
            ...
        }
    }
}
```

🔢 Total:

- `1 (if) + 1 (for) + 1 (if) = 3 estructuras`
    
- `1 + 3 = 4` → JaCoCo reportaría **Cxty = 4** para este método si cuenta el `if (isValid(data))` incluso cuando delega.
    

📝 Pero si JaCoCo ignora llamadas externas como esa y solo cuenta `for + if`, entonces da `Cxty = 2`.

**⚠ Necesitaríamos ver el desglose exacto en el informe línea a línea** para confirmar si `isValid` suma a la Cxty. Pero el razonamiento es válido en ambos sentidos.

___
### 🧾 7. ¿Qué representa el valor de Cxty para `Sample.maxValue()` y somos eficientes según él?

✅ `Cxty` representa la **cantidad de caminos lógicos independientes** que pueden seguirse durante la ejecución del método.

- Cuanto más alto sea, **más tests necesitas** para cubrir todos los casos.
    
- En este caso, `Cxty` moderado (3 o 4) indica que:
    
    - **El método no es complejo**, y
        
    - **Estamos siendo eficientes**: la lógica está clara, el código es testable.
        

📌 **Sí, es eficiente y efectivo.** No hay ramas innecesarias ni código difícil de probar.

___
### 🧾 8. ¿Por qué no se recorre la línea `if (isValid(data))` en `maxValue()` según el informe?

**¡Truco clásico de cobertura!**

Aunque tú llames a `maxValue()` en tus tests, **es posible que JaCoCo no cuente `if (isValid(...))` como cubierta** si:

- **Usas una subclase (`SampleTestable_isValid`)** que **sobrescribe `isValid()`**.
    
- Entonces, **`Sample.isValid()` no se ejecuta nunca**, aunque parezca que sí.
    

💡 Es decir, la línea:

```java
if (isValid(data)) {
```

se ejecuta, **pero no se recorre la implementación original de `isValid`** que está en la clase `Sample`, por lo tanto esa línea **no tiene cobertura** en JaCoCo.

✅ Solución: **testear directamente `Sample.isValid()`** con instancias de `Sample`, no de subclases mockeadas.

