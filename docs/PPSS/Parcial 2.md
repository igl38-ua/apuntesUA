# Proyecto Matriculación Multimódulo

## Matriculacion-bo

**BO = Business Object / Business Logic**  
Contiene la lógica de negocio. Es el núcleo del sistema, donde se implementan las reglas y procesos que definen cómo funciona la aplicación.  

**Ejemplo:** `AlumnoBR.java`, `MatriculaBO.java`

## Matriculacion-dao

**DAO = Data Access Object**  
Aquí se encapsula el acceso a la base de datos. Es responsable de interactuar con el almacenamiento de datos (por ejemplo, mediante JDBC o JPA).  

**Ejemplo:** `AlumnoDAO.java`, `JDBCMatriculaDAO.java`

## Matriculacion-proxy

**Proxy** en este contexto suele hacer referencia a una capa de intermediación, a veces usada para:

- Simular servicios externos (mocking o stubbing)
- Delegar llamadas a otras capas
- Añadir aspectos como logging, seguridad, etc.  

**Ejemplo:** `ProxyDatosEconomicos.java`, que probablemente simula o delega llamadas para obtener datos económicos.

## Matriculacion-comun

**Comun = Clases compartidas**  
Contiene elementos reutilizables por todos los módulos: clases auxiliares, objetos de transferencia (TOs o DTOs), constantes, utilidades, etc.  

**Ejemplo:** `AlumnoTO.java`, `AsignaturaTO.java` (TO = Transfer Object)

## Como se relacionan

`Matriculacion-bo` depende de `dao`, `proxy` y `comun`, porque necesita acceder a datos (`dao`), comunicarse con servicios externos (`proxy`) y compartir información (`comun`).

![item](../img/ppss/proyecto%20matriculacion.png)

___
# Implementación de drivers para pruebas de integración con dbunit

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
# Configuraciones pom.xml
## Maven Surefire Plugin (para JUnit-5 / tests unitarios)

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-surefire-plugin</artifactId>
  <version>3.5.2</version>
  <!-- Opcional: incluir/excluir tests -->
  <configuration>
	<!-- Por defecto ejecuta clases *Test.java, Test*.java y *Tests.java -->
	<!-- <includes><include>**/*Test.java</include></includes> -->
	<!-- <excludes><exclude>**/IT_*.java</exclude></excludes> -->
  </configuration>
</plugin>
```

- **Usos**:
	- Ejecutar los **unit-tests** en la fase `test`.
	- Detecta automáticamente tests JUnit 5 (JUnitPlatform).
	- Permite filtros `<includes>`/`<excludes>` para naming conventions.

___
## Maven Compiler Plugin

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <version>3.13.0</version>
  <configuration>
	<source>21</source>
	<target>21</target>
	<encoding>UTF-8</encoding>
  </configuration>
</plugin>
```

- **Usos**:
	- Compilar el código Java de `src/main/java` (fase `compile`).
	- Compilar tests de `src/test/java` (fase `test-compile`).
	- Ajustar nivel de lenguaje (`source`/`target`) y codificación.

___
## Maven Failsafe Plugin (para tests de integración)

```xml
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-failsafe-plugin</artifactId>
  <version>3.5.2</version>
  <executions>
	<execution>
	  <id>integration-tests</id>
	  <goals>
		<goal>integration-test</goal>  <!-- corre ITs -->
		<goal>verify</goal>
	  </goals>
	  <configuration>
		<includes>
		  <include>**/*IT.java</include>
		  <include>**/IT_*.java</include>
		</includes>
	  </configuration>
	</execution>
  </executions>
</plugin>
```

- **Usos**:
	- Ejecutar tests que sigan el patrón `*IT.java` o `IT_*.java` en la fase `integration-test`.
	- Realizar el `verify` tras las ITs, deteniendo el build si fallan.

___
## SQL Maven Plugin + MySQL Connector + configuración JDBC

```xml
<plugin>
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>sql-maven-plugin</artifactId>
  <version>3.0.0</version>
  <dependencies>
	<dependency>
	  <groupId>mysql</groupId>
	  <artifactId>mysql-connector-java</artifactId>
	  <version>8.0.33</version>
	</dependency>
  </dependencies>
  <configuration>
	<driver>com.mysql.cj.jdbc.Driver</driver>
	<url>jdbc:mysql://localhost:3306/DBUNIT?useSSL=false</url>
	<username>root</username>
	<password>admin</password>
  </configuration>
  <executions>
	<execution>
	  <id>create-customer-table</id>
	  <phase>pre-integration-test</phase>
	  <goals><goal>execute</goal></goals>
	  <configuration>
		<srcFiles>
		  <srcFile>src/test/resources/sql/create_table_customer.sql</srcFile>
		</srcFiles>
	  </configuration>
	</execution>
  </executions>
</plugin>
```

- **Usos**:
	- Ejecutar scripts SQL (creación de esquemas/tablas, carga de datos) antes o después de ciertas fases (ej. `pre-integration-test`).
	- Importa el driver MySQL para que el plugin pueda cargar `com.mysql.cj.jdbc.Driver`.

___
## Dependencia Selenium Java (para tests de aceptación / E2E)

```xml
<dependency>
  <groupId>org.seleniumhq.selenium</groupId>
  <artifactId>selenium-java</artifactId>
  <version>4.14.0</version>
  <scope>test</scope>
</dependency>
```

- **Usos**:
	- Escribir pruebas de interfaz de usuario que controlen navegadores (ChromeDriver, GeckoDriver, etc.).
	- Con JUnit/TestNG pueden ejecutarse junto a tu suite de tests unitarios o de integración.

___
## JaCoCo Maven Plugin (instrumentación y checks)

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.13</version>
  <executions>
	<!-- 1. Instrumentación para unit-tests -->
	<execution>
	  <id>default-prepare-agent</id>
	  <goals><goal>prepare-agent</goal></goals>
	</execution>
	<!-- 2. Informe tras unit-tests (fase test→verify) -->
	<execution>
	  <id>default-report</id>
	  <goals><goal>report</goal></goals>
	</execution>
	<!-- 3. Instrumentación para integration-tests -->
	<execution>
	  <id>prepare-agent-integration</id>
	  <phase>pre-integration-test</phase>
	  <goals><goal>prepare-agent-integration</goal></goals>
	  <configuration>
		<destFile>${project.build.directory}/jacoco-it.exec</destFile>
	  </configuration>
	</execution>
	<!-- 4. Informe tras integration-tests -->
	<execution>
	  <id>report-integration</id>
	  <phase>verify</phase>
	  <goals><goal>report-integration</goal></goals>
	  <configuration>
		<dataFile>${project.build.directory}/jacoco-it.exec</dataFile>
		<outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
	  </configuration>
	</execution>
	<!-- 5. Check de umbrales globales y por clase -->
	<execution>  
		<id>default-check</id>  
		<goals>        
			<goal>check</goal>  
		</goals>    
		<configuration>
			<!-- EJEMPLOS -->     
			<rules>    
				<!-- A NIVEL DE PROYECTO -->  
				<rule>  
					<element>BUNDLE</element>  
					<limits>                    
						<limit>                        
							<counter>COMPLEXITY</counter>  
							<value>COVEREDRATIO</value>  
							<minimum>0.82</minimum>  
						</limit>                    
						<limit>                        
							<counter>INSTRUCTION</counter>  
							<value>COVEREDRATIO</value>  
							<minimum>0.90</minimum>  
						</limit>                    
						<limit>                        
							<counter>CLASS</counter>  
							<value>COVEREDRATIO</value>  
							<minimum>1.00</minimum>  
						</limit>                
					</limits>            
				</rule>            
				<!-- A NIVEL DE CADA CLASE -->  
				<rule>  
					<element>CLASS</element>  
					<limits>                    
						<limit>                        
							<counter>LINE</counter>  
							<value>COVEREDRATIO</value>  
							<minimum>0.75</minimum>  
						</limit>                    
						<limit>                        
							<counter>METHOD</counter>  
							<value>COVEREDRATIO</value>  
							<minimum>0.60</minimum>  
						</limit>                
					</limits>            
				</rule>        
			</rules>    
		</configuration>
	</execution>
  </executions>
</plugin>
```

- **Orden de ejecución** en un `mvn clean verify`:
	1. `prepare-agent` (unit)
	2. `test` → JaCoCo recoge datos (`jacoco.exec`)
	3. `report` (informe unit)
	4. `pre-integration-test` → `prepare-agent-integration` (IT)
	5. `integration-test` → JaCoCo recoge datos IT (`jacoco-it.exec`)
	6. `report-integration` (informe IT)
	7. `check` (comprueba umbrales, puede fallar el build)

___
# Ejecución de fases en maven

Ciclo de vida completo con **todas** las fases y los goals que hemos visto:

| **Fase**                 | **Plugin:Goal**                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| validate                 |                                                                                               |
| ==initialize==           | ==jacoco:prepare-agent==                                                                      |
| generate-sources         |                                                                                               |
| process-sources          |                                                                                               |
| generate-resources       |                                                                                               |
| process-resources        | resources:resources                                                                           |
| ==compile==              | ==compiler:compile==                                                                          |
| process-classes          |                                                                                               |
| generate-test-sources    |                                                                                               |
| process-test-sources     |                                                                                               |
| generate-test-resources  |                                                                                               |
| process-test-resources   | resources:testResources                                                                       |
| ==test-compile==         | ==compiler:testCompile==                                                                      |
| process-test-classes     |                                                                                               |
| ==test==                 | ==surefire:test==                                                                             |
| prepare-package          |                                                                                               |
| ==package==              | ==jar:jar==                                                                                   |
| ==pre-integration-test== | ==sql:execute==<br>==jacoco:prepare-agent-integration==                                       |
| ==integration-test==     | ==failsafe:integration-test==                                                                 |
| post-integration-test    |                                                                                               |
| ==verify==               | ==failsafe:verify==<br>==jacoco:report==<br>==jacoco:report-integration==<br>==jacoco:check== |
| install                  | install:install                                                                               |
| deploy                   | deploy:deploy                                                                                 |

- **resources:resources** -> copia `src/main/resources` en **process-resources**
- **compiler:compile** -> compila `src/main/java` en **compile**
- **resources:testResources** -> copia `src/test/resources` en **process-test-resources**
- **compiler:testCompile** -> compila `src/test/java` en **test-compile**
- **surefire:test** -> ejecuta unit‐tests en **test**
- **jar: jar** -> empaqueta en **package**
- **sql:execute** -> corre scripts SQL en **pre-integration-test**
- **jacoco:prepare-agent** / **jacoco:prepare-agent-integration** -> instrumentan coverage para unit/IT en **initialize** y **pre-integration-test**
- **failsafe:integration-test** -> ejecuta ITs en **integration-test**
- **failsafe:verify** -> verifica ITs en **verify**
- **jacoco:report** / **report-integration** / **check** -> generan informes y comprueban umbrales en **verify**
- **install:install**, **deploy:deploy** -> instalan/despliegan en **install** y **deploy** respectivamente

___
# Jmeter

(Ejemplo ejercicio 2 práctica 9)

**GRUPO DE HILOS** -> Envuelve a todos los samplers y controladores de la sesión. Controla la ejecución y establece los Threads (usuarios activos simultáneos), el Ramp-up period (sec) y las iteraciones.

- **HTTP REQUEST (SAMPLER)** -> Suele incluir un Response Assertion, que pueden visualizarse con el listener Assertion Results.
- **HTTP REQUEST DEFAULTS** -> `localhost:8080`. Configuración default para todos los samplers.
- **HTTP COOKIE MANAGER** -> Almacena cookies recibidas para todos los samplers.
- **RESPONSE ASSERTION** -> Validación de datos de un sampler.
- **INTERLEAVE CONTROLLER** -> Ejecuta un sampler por iteración. Alterna la ejecución de uno de los hijos que envuelve por iteración. 
- **UNIFORM RANDOM TIMER**
- **GRAPH RESULTS** -> Gráfico en tiempo real del avance de las pruebas.
- **VIEW RESULTS TREE** -> Muestra las peticiones y respuestas de todos los samplers.
- **ASSERTIONS RESULT** -> Muestra el resultado de cada assertion en cada sampler.
- **AGGREGATE REPORT** -> Da un resumen general. Agrupa los samplers por label y calcula estadísticas acumuladas de progreso.
- **VIEW RESULTS IN TABLE** -> Muestra en forma de tabla, una fila por sampler (TIEMPO, BYTES, RESULTADO)
- **SIMPLE DATA WRITER** -> Guarda en un csv los cálculos jmeter. Con en comando `jmeter -g data.csv reports/`. Se pueden visualizar las gráficas de Response Over Time para comprobar los Threads activos por ejecución (si cuadran con los especificados en el Thread Group). 

___
# Page Object y Page Factory
## Sin Page Object

Se buscan los campos con `driver.findElement(By.)` y se ejecutan las acciones de manera directa en el mismo driver.
	
```java
private WebDriver driver;  
// Mis credenciales del test de creación  
private static final String EXISTING_EMAIL = "iguijarrolillo2@mail.com";  
private static final String EXISTING_PASSWORD = "...........";  
  
@BeforeEach  
public void setup() {  
    driver = new ChromeDriver();  
    WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));  
    driver.get("http://demo.magento.recolize.com");  
    Dimension dimension = new Dimension(1500, 1000);  
    driver.manage().window().setSize(dimension);  
}

@Tag("R2R3")  
public void R2_requirement_loginOK_should_login_with_success_when_user_account_exists() throws InterruptedException {  
    // 1. Verificar título de la home  
    assertEquals("Madison Island", driver.getTitle());  
  
    // 2. Abrir menú Account → Login  
    driver.findElement(By.cssSelector("#header > div > div.skip-links > div > a")).click();  
    driver.findElement(By.cssSelector("#header-account > div > ul > li.last > a")).click();  
	  
    // 3. Verificar título de la página de login  
    assertEquals("Customer Login", driver.getTitle());  
	  
    // 4. Rellenar el email y enviar sin password  
    driver.findElement(By.id("email")).sendKeys(EXISTING_EMAIL);  
    Thread.sleep(500);  
    driver.findElement(By.cssSelector("button[title='Login']")).click();  
	  
    // 5. Verificar mensaje de campo requerido en contraseña  
    WebElement errorPass = driver.findElement(  
            By.cssSelector("#advice-required-entry-pass")  
    );  
    assertEquals("This is a required field.", errorPass.getText());  
	  
    // 6. Rellenar la contraseña y volver a enviar  
    driver.findElement(By.id("pass")).sendKeys(EXISTING_PASSWORD);  
    Thread.sleep(500);  
    driver.findElement(By.cssSelector("button[title='Login']")).click();  
    Thread.sleep(500);  
	
    // 7. Verificar que estamos en "My Account" y mensaje de bienvenida  
    assertEquals("My Account", driver.getTitle());  
    WebElement welcome = driver.findElement(By.cssSelector("p.hello"));  
    assertTrue(  
            welcome.getText().startsWith("Hello,"),  
            "Debe mostrar mensaje de bienvenida con 'Hello,'"  
    );  
}
```

___
## Page Object

El método **Page Object** se basa en delegar y separar la creación de objetos y acceso a los campos de la web, a clases que representan una página completa de la web.
Este acceso se realiza mediante funciones que llaman a los selectores correspondientes.

```java
@Test  
public void R4_requierement_PO_loginOK_should_login_with_success_when_user_account_exists() {  
    HomePage home = new HomePage(driver);  
    home.clickAccount();  
    CustomerLoginPage login = home.clickLogin();  
  
    // Paso 4: solo email  
    login.enterEmail(EXISTING_EMAIL);  
    // Paso 6: contraseña y submit  
    login.enterPassword(EXISTING_PASSWORD);  
    MyAccountPage account = login.clickLoginButton();  
  
    // Paso 7: verificaciones  
    assertEquals("My Account", account.getTitle());  
}
```

```java
public class HomePage {  
    private final WebDriver driver;  
    private final By accountMenu = By.cssSelector("#header > div > div.skip-links > div > a");  
    private final By loginLink = By.cssSelector("#header-account > div > ul > li.last > a");  
  
    public HomePage(WebDriver driver) {  
        this.driver = driver;  
    }  
  
    // Abre el menú “Account”  
    public void clickAccount() {  
        driver.findElement(accountMenu).click();  
    }  
  
    // Hace click en “Log In” y devuelve la página de login  
    public CustomerLoginPage clickLogin() {  
        driver.findElement(loginLink).click();  
        return new CustomerLoginPage(driver);  
    }  
}
```

___
## Page Object + Page Factory

Con el patrón Page Factory, en lugar de instanciar los objetos Page Object directamente se delega a la Page Factory usando una función `PageFactory.initElements(driver, Clase.class);` 
De esta manera se crea el objeto Page Object y se inicializan los `@FindBy` para no tener que instanciarlos con `.findElements()`. Pero es obligatorio que en la clase instanciada se defina un constructor por defecto:

```java
public MyAccountPage(WebDriver driver) {  
	this.driver = driver;
}  
```

Esto inicializa los `@FindBy` y prepara el Page Object para ejecutar las acciones sobre la página.

```java
@Test  
public void R6_requirement_PO_compareShoes_should_clear_comparison_when_TwoShoes_are_compared_and_cleared() {  
	// 1. MyAccountPage  
	MyAccountPage acct = PageFactory.initElements(driver, MyAccountPage.class);  
	assertEquals("My Account", acct.getTitle());  
	
	// 2–3. Hover Accessories -> Shoes  
	ShoesPage shoes = acct.goToShoes();  
	assertEquals("Shoes - Accessories", shoes.getTitle());  
	
	// 4. Seleccionamos los dos últimos zapatos  
	shoes.selectShoeToCompare(5);  
	shoes.selectShoeToCompare(6);  
	
	// 5–6. Pulsar COMPARE y cambio a ventana hija  
	ProductComparisonPage comp = shoes.clickCompare();  
	assertTrue(comp.getTitle().contains("Products Comparison List"));  
	
	// 7–8. Cerrar ventana comparativa y volver a ShoesPage  
	shoes = comp.closeComparison();  
	assertEquals("Shoes - Accessories", shoes.getTitle());  
	
	// 9. Clear All y leer alerta  
	String alertText = shoes.clearComparisonAlert();  
	assertEquals(  
			"Do you like to remove all products from your comparison?",  
			alertText  
	);  
	
	// 10. Mensaje final  
	String clearedMsg = shoes.getClearedMessage();  
	assertTrue(  
			clearedMsg.contains("the comparison list was cleared"),  
			"Debe mostrar mensaje de lista vaciada"  
	);  
}  
```

```java
public class MyAccountPage {  
    private final WebDriver driver;  
	  
    @FindBy(xpath = "//a[normalize-space()='Accessories']") WebElement accessoriesMenu;  
	  
    public MyAccountPage(WebDriver driver) {  
        this.driver = driver;
    }  
	  
    /** Título de la página */  
    public String getTitle() {  
        return driver.getTitle();  
    }  
	  
    /** Hover → devuelve la PO de Shoes */  
    public ShoesPage goToShoes() {  
        new Actions(driver).moveToElement(accessoriesMenu).perform(); 
        return PageFactory.initElements(driver, ShoesPage.class);  
    }  
}
```

Lo normal es utilizar métodos como el `goToShoes()` en los que se ejecutan las acciones sobre el driver y luego se redirige a la siguiente página instanciando el `PageFactory.initElements()`. 