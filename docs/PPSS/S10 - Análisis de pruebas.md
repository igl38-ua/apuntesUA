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
