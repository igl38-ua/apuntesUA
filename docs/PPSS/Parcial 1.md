Las pruebas deben de ser un conjunto **EFECTIVO** (deben detectar el máximo número posible de errores) y **EFICIENTE** (con el menor número posible de casos de prueba). ^R1

___
## Ubicaciones directorios

Para la clase `Cosa.java`.

```sql
project-home/                    --> Carpeta raíz que contiene el proyecto Maven
├── src/                         --> Ficheros
│   ├── main/
│   │   ├── java/                --> Código fuente en Java
│   │   │   └── paquete/         --> Paquete raíz del proyecto
│   │   │       ├── excepciones/
│   │   │       │   └── CosaException.java  --> Manejo de excepciones
│   │   │       └── Cosa.java               --> Clase principal
│   │   └── resources/           --> Archivos adicionales usados por el código fuente
│   └── test/                    --> Pruebas
│       ├── java/                --> Código fuente de las pruebas en Java
│       │   └── paquete/         --> Paquete raíz de pruebas
│       │       ├── CosaTest.java          --> Clase de prueba
│       │       ├── CosaTestable.java      --> Clase para la inyección de dependencias
│       │       └── CosaStub.java          --> STUB para pruebas
│       └── resources/           --> Archivos adicionales para pruebas
│
├── target/                      --> Generado automáticamente por Maven (build)
│   ├── classes/                 --> Archivos compilados del código fuente
│   ├── test-classes/            --> Archivos compilados del código de prueba
│   ├── surefire-reports/        --> Reportes de ejecución de pruebas unitarias
│   │   ├── paquete.CosaTest.txt
│   │   └── TEST-paquete.CosaTest.xml
│   ├── failsafe-reports/        --> Reportes de pruebas de integración
│   ├── generated-sources/       --> Código fuente generado automáticamente
│   ├── generated-test-sources/  --> Código de prueba generado automáticamente
│   ├── maven-status/            --> Información del estado de compilación
│   ├── site/                    --> Documentación del proyecto generada con `mvn site`
│   ├── dependency/              --> Dependencias copiadas localmente (si se configura)
│   └── [nombre].jar             --> Archivo JAR final generado (si aplica)
│
└── pom.xml                      --> Archivo de configuración del proyecto (POM)

```

___
