# Resumen

- Las **pruebas de integración** permiten **identificar defectos** en las interfaces entre componentes ya verificados de manera individual.
- Se realizan de forma **incremental**, añadiendo componentes uno a uno.
- Hay 4 niveles de pruebas:
	- **Unidad** - Verificación.
	- **Integración** - Verificación.
	- **Sistema** - Verificación.
	- **Aceptación** - Validación.
- El **proceso de integración** es una construcción progresiva del sistema agregando componentes. Asegura que cada nuevo componente no afecte negativamente a los existentes.
- **Estrategias de integración**:
	- **Big Bang**: Integrar todo de golpe, para aplicaciones pequeñas.
	- **Top-Down**: De arriba hacia abajo en nivel de abstracción.
	- **Bottom-Up**: De abajo hacia arriba (menos dobles requeridos).
	- **Sandwich**: Mixta Top + Bottom.
	- **Dirigida por riesgos**: Se integran primero los más propensos a fallar.
	- **Dirigida por funcionalidades**: Basada en casos de uso e historias de usuarios.
- En integración se usa la BD real, no dobles.
- En las **pruebas de regresión** se ejecutan todos los tests después de integrar un nuevo componente. **Evitan** que se **rompan funcionalidades existentes**.
- Las interfaces principales de **DBUnit** son **ITable** y **IDataSet**, que representan a una tabla y muchas tablas respectivamente.
- Para la **automatización con Maven** utilizamos el plugin `sql-maven-plugin`, para ejecutar scripts sql y preparar la base de datos antes de los tests; además del plugin `failsafe` para ejecutar los tests de integración y generar los informes.
- Es habitual dividir los proyectos en **DAO** (Data Access Object) y **BO** (Business Object), para **separar la lógica de negocio del acceso a la base de datos**.

___
# S07 - Integración

Objetivos de las de **pruebas de integración**:

- **Identificar defectos** en las interfaces entre componentes ya probados de forma individual (unidades).
- Realizar un **proceso incremental de integración** asegurando que nuevos componentes no afectan negativamente a los anteriores (**pruebas de regresión**).
## Niveles de pruebas

- Las pruebas se realizan a **diferentes niveles**, durante el proceso de desarrollo. 
- En las pruebas de integración el **orden** en que se integran los componentes es crucial.

| Nivel           | ¿Qué se prueba?               | Tipo                       |
| --------------- | ----------------------------- | -------------------------- |
| **Unidad**      | Código de las unidades        | Verificación (caja blanca) |
| **Integración** | Interacción entre componentes | Verificación               |
| **Sistema**     | Todo el sistema               | Verificación               |
| **Aceptación**  | Producto en su entorno real   | Validación                 |

> Al nivel de pruebas unitarias, el sistema "existe" en forma de "piezas" bajo el control de los programadores. Lo siguiente es "reunir" todas las piezas para construir el sistema completo.

___
## El proceso de integración

Un **sistema** es una colección de **componentes** interconectados de una forma concreta. 

El objetivo de la integración es construir una versión "operativa" del sistema utilizando:

- **Agregación** de forma incremental, de nuevos componentes.
- Asegurándonos de que **añadir nuevos** componentes **no afecta** al funcionamiento de los componentes **existentes** (pruebas de regresión).

___
## Interfaces y errores comunes
### Tipos de interfaces entre componentes

- Interfaz a través de **parámetros** (más común).
- **Memoria compartida**.
- **Procedimientos** (métodos).
- Paso de mensajes.
### Errores más frecuentes en integración

- Mal uso o malinterpretación de la interfaz
- Errores temporales (condiciones específicas, estrés, concurrencia)
### Guías para el diseño de pruebas de integración

- **Valores extremos y punteros nulos** en parámetros.
- Probar explícitamente fallos esperados cunado se invocan componentes con **interfaces procedurales**.
- Pruebas de **estrés** en sistemas con paso de **mensajes**.
- Revisar el orden de uso en memoria compartida (método de diseño de caja negra = particiones equivalentes).

___
## Estrategias de integración
 
- **Big Bang**. Integrar todo de golpe, solo si la aplicación es pequeña.

- **Top-down:** De mayor a menor nivel de abstracción en la integración de componentes.
    
    - Requiere muchos dobles.
    - Ejemplo: sistemas con interfaces gráficas complejas.
    
- **Bottom-up:** Desde infraestructura básica (bases de datos, redes) a componentes funcionales superiores de mayor nivel de abstracción.
    
    - Menos dobles requeridos.
    - Ejemplo: aplicaciones con lógica de negocio compleja.
    
- **Sandwich:** Mezcla de Top-down y Bottom-up.

- **Dirigida por riesgos:** Integrar primero componentes más propensos a fallos.

- **Dirigida por funcionalidades:** Integración basada en casos de uso o historias de usuario. Se ordenan las funcionalidades con algún criterio y se integra siguiendo ese orden.

> Los tests de integración no usarán dobles para la BD, acceden a la base de datos real.

___
## Pruebas de regresión

Las **pruebas de regresión** consisten en repetir la ejecución de todos los tests cuando se integra un nuevo componente.

- **Imprescindibles** en cada paso de integración. AL modificar el software en mantenimiento o añadir funcionalidades o al depurar defectos.
- **Evitan** que nuevos componentes **rompan funcionalidades ya probadas**.

___
## Pruebas de integración con bases de datos (DBUnit)

- **DBUnit** es una extensión de **JUnit**.
- Permite **gestionar el estado** de una base de datos **durante** las pruebas.

___
## Interfaz ITable

- Representa **una tabla concreta** de la base de datos.
- Se suele llamar con el método `getTable("nombre")`, desde un objeto `IDataSet`. 

```java
IDataSet databaseDataSet = connection.createDataSet();  
ITable actualTable = databaseDataSet.getTable("cliente");
```
## Interfaz IDataSet

- Representa **una colección de tablas** de la base de datos.
- Se utiliza para **comparar el estado actual** de la base de datos con el **estado esperado** en fase de pruebas.

Permite cargar datos desde formato xml: 

```java
IDataSet dataSet = new FlatXmlDataFileLoader().load("/cliente-init.xml");
```

___
## Clase FlatXmlDataSet

- Se utiliza para crear **objetos dataset** a partir de documentos xml con los datos de las tablas, y viceversa. 

```xml
<?xml version="1.0" encoding="UTF-8"?>
<dataset>
	<customer id="1"
		firstname="John"
		street="1 Main Street" />
	<user id="1"
		login="John"
		password="John" />
	<user id="2"
		login="Karl"
		password="Karl" />
</dataset>
```

Inserciones en dos tablas `customer` y `user`.

___
## Clase IDataBaseTester

Permite el acceso a la BD mediante conexiones de tipo `IDatabaseConnection`.

```java
// Permite el acceso a la BD, devuelve objetos de tipo IDatabaseConnection
private IDatabaseTester databaseTester;
// Representa la conexión con la BD
private IDatabaseConnection connection; 

// Se establece la cadena de conexión para conectar con la base de datos, el driver mysql, el usuario y contraseña.
String cadena_conexionDB = "jdbc:mysql://localhost:3306/DBUNIT?useSSL=false";
databaseTester = new JdbcDatabaseTester("com.mysql.cj.jdbc.Driver",  
        cadena_conexionDB, "root", "admin");
connection = databaseTester.getConnection();

// Inicializamos la BD desde un fichero xml
IDataSet dataSet = new FlatXmlDataFileLoader().load("/cliente-init.xml");  
databaseTester.setDataSet(dataSet);  
databaseTester.onSetup(); // inserta el contenido del dataSet en la BD

// Recuperamos los datos actuales de la BD después de invocar al SUT  
IDataSet databaseDataSet = connection.createDataSet();  
ITable actualTable = databaseDataSet.getTable("cliente");

// Creamos el dataset con el resultado esperado 
IDataSet expectedDataSet = new FlatXmlDataFileLoader().load("/cliente-esperado.xml"); 
ITable expectedTable = expectedDataSet.getTable("cliente");

// org.dbunit
Assertion.assertEquals(expectedTable, actualTable);
```

___
## DBUnit y pruebas de integración con Maven

```xml
// Librería DbUnit
<dependency>
	<groupId>org.dbunit</groupId>
	<artifactId>dbunit</artifactId>
	<version>3.0.0</version>
	<scope>test</scope>
</dependency>

// Libería para una BD mysql
<dependency>
	<groupId>com.mysql</groupId>
	<artifactId>mysql-connector-j</artifactId>
	<version>9.2.0</version>
	<scope>test</scope>
</dependency>

// Plugin failsafe para ejecutar los tests de integración
<build>
	<plugins>
		<plugin>
			<groupId>org.apache.maven.plugins</groupId>
			<artifactId>maven-failsafe-plugin</artifactId>
			<version>3.5.2</version>
			<executions>
				<execution>
					<goals>
						<goal>integration-test</goal>
						<goal>verify</goal>
					</goals>
				</execution>
			</executions>
		</plugin>
	</plugins>
</build>
```
### Plugin failsafe

- Para todos los métodos `@Test` de las clases `**/IT*.java`, `**/*IT.java`, o `**/*ITCase.java`.
- Informes `/target/failsafe-reports`.

___
## Implementación de drivers

```java
public class ClienteDAO_IT {
	
    private ClienteDAO clienteDAO; // contiene nuestro SUT
    private IDatabaseTester databaseTester; // Necesitamos una instancia de IDatabaseTester para acceder a la BD
    private IDatabaseConnection connection;
	
    @BeforeEach
    public void setUp() throws Exception {
        String cadenaConexionDB = "..."; 
        String claseDriver = "...";
        // Datos para la conexión con la BD
        databaseTester = new JdbcDatabaseTester(claseDriver, cadenaConexionDB, "root", "ppss"); 
        
        // obtenemos la conexión con la BD
        connection = databaseTester.getConnection(); 
        
        // inicializamos el dataset para inicializar la BD
        // Dataset inicial: tabla de clientes VACÍA
        IDataSet dataSet = new FlatXmlDataFileLoader().load("/cliente-init.xml"); 
        
        // inyectamos el dataset
        databaseTester.setDataSet(dataSet);
	
        // inicializamos la BD con el dataset inicial
        // Borra los datos de las tablas del dataset inicial en la BD e inserta en la BD el contenido del dataset inicial
        databaseTester.onSetup(); 
        
        // Instancia que contiene nuestro SUT
        clienteDAO = new ClienteDAO(); 
    }
}
```

___
## Implementación de caso de prueba

```java
@Test
public void testInsert() throws Exception {
    // Datos de entrada del caso de prueba
    Cliente cliente = new Cliente(1, "John", "Smith");
    cliente.setDireccion("1 Main Street");
    cliente.setCiudad("Anycity");
	
    // Resultado ESPERADO
    // creamos el dataset con el resultado esperado
    IDataSet expectedDataSet = new FlatXmlDataFileLoader().load("/cliente-esperado.xml");
    ITable expectedTable = expectedDataSet.getTable("cliente");
    
    // invocamos a nuestro SUT
    clienteDAO.insert(cliente);
    
    // Resultado REAL
    // recuperamos los datos de la BD después de invocar al SUT
    IDataSet databaseDataSet = connection.createDataSet();
    // Recuperamos los datos de la tabla cliente
    ITable actualTable = databaseDataSet.getTable("cliente");
	
    // Comparamos el resultado ESPERADO con el REAL
    Assertion.assertEquals(expectedTable, actualTable);
}
```

___
## Organización de directorios para los ficheros de entrada y resultados esperados

![item](../img/ppss/datos%20de%20entrada%20y%20resultado%20esperado.png)

___
## Plugin sql-maven-plugin

Configuración del pom para inicializar las tablas de la BD antes de ejecutar los tests.

```xml
<plugin>
  // Plugin para ejecutar sentencias SQL
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>sql-maven-plugin</artifactId>
  <version>3.0.0</version>

  // Dependencia del plugin con el driver JDBC para acceder a una base de datos MySQL.
  <dependencies>
    <dependency>
      <groupId>com.mysql</groupId>
      <artifactId>mysql-connector-j</artifactId>
      <version>9.2.0</version>
    </dependency>
  </dependencies>

  // Configuración del driver JDBC
  <configuration>
    <driver>com.mysql.cj.jdbc.Driver</driver>
    <url>jdbc:mysql://localhost:3306/DB?useSSL=false</url>
    <username>root</username>
    <password>ppss</password>
  </configuration>

  <executions>
    <execution>
      // Se ejecuta antes de ejecutar los test de integración
      <id>create-customer-table</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>execute</goal>
      </goals>

      // Script de inicialización de la tabla customer
      <configuration>
        <srcFiles>
          <srcFile>src/test/resources/sql/create_table_customer.sql</srcFile>
        </srcFiles>
      </configuration>
    </execution>
  </executions>
</plugin>
```

___
## Automatización de pruebas de integración con Maven

![item](../img/ppss/proceso%20completo%20automatización.png)

___
## Proyecto Matriculación
### Matriculacion-bo

**BO = Business Object / Business Logic**  
Contiene la lógica de negocio. Es el núcleo del sistema, donde se implementan las reglas y procesos que definen cómo funciona la aplicación.  

**Ejemplo:** `AlumnoBR.java`, `MatriculaBO.java`

---
### Matriculacion-dao

**DAO = Data Access Object**  
Aquí se encapsula el acceso a la base de datos. Es responsable de interactuar con el almacenamiento de datos (por ejemplo, mediante JDBC o JPA).  

**Ejemplo:** `AlumnoDAO.java`, `JDBCMatriculaDAO.java`

---
### Matriculacion-proxy

**Proxy** en este contexto suele hacer referencia a una capa de intermediación, a veces usada para:

- Simular servicios externos (mocking o stubbing)
- Delegar llamadas a otras capas
- Añadir aspectos como logging, seguridad, etc.  

**Ejemplo:** `ProxyDatosEconomicos.java`, que probablemente simula o delega llamadas para obtener datos económicos.

---
### Matriculacion-comun

**Comun = Clases compartidas**  
Contiene elementos reutilizables por todos los módulos: clases auxiliares, objetos de transferencia (TOs o DTOs), constantes, utilidades, etc.  

**Ejemplo:** `AlumnoTO.java`, `AsignaturaTO.java` (TO = Transfer Object)

---
### ¿Cómo se relacionan?

`Matriculacion-bo` depende de `dao`, `proxy` y `comun`, porque necesita acceder a datos (`dao`), comunicarse con servicios externos (`proxy`) y compartir información (`comun`).

![item](../img/ppss/proyecto%20matriculacion.png)

