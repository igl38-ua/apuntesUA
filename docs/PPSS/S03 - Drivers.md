# Resumen

- Los **drivers** son fragmentos de código que implementamos para ejecutar los tests de manera automática. 
- **SUT = System Under Test**, código a probar.
- Las **pruebas unitarias** se centran en unidades de programa: **métodos java**.
- En cada driver hay tres fases. **Arrange**, preparar los datos; **Act**, invocar la SUT; y **Assert**, comparar resultados.
- En **JUnit** los drivers son métodos **sin parámetros**, tipo **void** y anotado con `@Test`.
- JUnit tiene métodos como `assertEquals`, `assertTrue`, `assertThrows`, para verificar los resultados. Todos se pueden agrupar en sentencias `assertAll`.
- Los **tests parametrizados** permiten ejecutar un mismo método de prueba con parámetros distintos. Puede utilizarse `@ValueSource` o `@MethodSource`.
- El plugin **maven-surefire-plugin** gestiona la ejecución de los tests invocando a la librería `junit-jupiter`.
- Podemos incluir **filtros** en los comandos maven para **excluir** tests o ejecutar tests **específicos**.
- Los informes se guardan en `target/surefire-reports` en formatos de texto. Pueden presentarse como **pass**, **failure** o **error**. 
- El **ciclo de vida por defecto** de maven tiene tres fases: **compile**, **test-compile** y **test**.

___
# Drivers
## Automatización de las pruebas

Se trata de implementar código, **drivers**, para ejecutar los tests de forma automática.

El código de pruebas tendrá que:
1. Proporcionar **datos de entrada** + **resultado esperado** al código a probar (**SUT**)
2. Obtener el resultado real.
3. Comparar el resultado esperado con el real.
4. Emitir un informe que verifica que no haya bugs en el código.

**SUT = System Under Test** -> El código a probar.

___
## Pruebas unitarias

- Las **pruebas unitarias** se centran en _unidades de programa_ (en este caso, cada **unidad** se define como un _método Java_).
- El **objetivo** es aislar cada método y **detectar** posibles defectos.
- Creamos un test, por cada unidad de programa presente.
### Pruebas de Unidad Dinámicas: Drivers

- Un **driver** es un _código conductor_ para ejecutar un caso de prueba **de forma automatizada**.
- Cada driver se encarga de:
    1. Preparar los datos de entrada (**Arrange**).
    2. Invocar el método a probar (**Act**).
    3. Comparar resultado real vs. esperado (**Assert**).
    4. Emitir un informe.
- Así, cada _caso de prueba_ tendrá un _driver_, y ese driver llamará a la **SUT (System Under Test)**, que en pruebas unitarias se corresponde con **un único método**.
- Cada unidad es un **método java**. 

___
## Implementación de drivers con JUnit 5

### JUnit 5

- **JUnit 5** es una librería Java para _implementar y ejecutar_ tests.
### Cómo identificamos un driver (test) con JUnit 5?

- Cada _driver_ se define como un **método** sin parámetros, con valor de retorno `void` y anotado con `@Test`.
- La **clase de prueba** debe estar en el **mismo paquete** que la clase a probar y que su nombre sea igual añadiendo `Test`, `TrianguloTest`.

```java
class TrianguloTest {
    @Test
    void C1_testTipoEquilatero() {
        // 1. Arrange
        int a = 1, b = 1, c = 1;
        String esperado = "Equilatero";
        Triangulo tri = new Triangulo();
		
        // 2. Act
        String real = tri.tipo_triangulo(a,b,c);
		
        // 3. Assert
        assertEquals(esperado, real);
    }
}
```

___
### Patrón AAA (Arrange-Act-Assert)

- **Arrange**: Preparar datos de entrada, instanciar la SUT y definir precondiciones.
- **Act**: Invocar el método SUT con los datos preparados.
- **Assert**: Comprobar la coincidencia entre resultado real y esperado usando aserciones de JUnit (por ejemplo, `assertEquals`).

Los **nombres de los drivers** seguirán el formato: ``ID_MethodName_ExpectedResult_When_Conditions``.
### Sentencias de aserción (Assert)

- JUnit provee métodos estáticos (`assertEquals`, `assertTrue`, `assertThrows`) para verificar la validez de los resultados.
- El **orden** de parámetros es `assertEquals(esperado, real)`.
- Cuando un `assert` falla, lanza una excepción (`AssertionFailedError`), marcando el test como _Failure_.
- Para **varias** comprobaciones en un mismo test, hay que usar `assertAll`, que ejecuta todas las aserciones (si una falla, igualmente se registra el fallo, pero se reportan todas las discrepancias).

Agrupando las excepciones:

```java
@Test
public void C3_add_should_not_add_element_when_dataArray_is_full() {
	int[] arrayEsperado = {1,2,3,4,5,6,7,8,9,10};
	int numElemEsperado = 10;
	int[] arrayEstadoInicial = Arrays.copyOf(arrayEsperado, arrayEsperado.length);
	DataArray coleccion = new DataArray(arrayEstadoInicial, 10);
	
	coleccion.add(11);
	
	//Agrupamos las aserciones. SE EJECUTAN TODAS siempre
	assertAll("C3_dataArray no debe cambiar",
		()-> assertArrayEquals(arrayEsperado, coleccion.getColeccion()),
		()-> assertEquals(numElemEsperado, coleccion.size())
	); //Se muestran todos los "fallos" producidos
}
```

No las agrupamos:

```java
@Test
public void C3_add_should_not_add_element_when_dataArray_is_full() {
	...
	//No agrupamos las excepciones. Si falla la primera, la segunda NO se ejecuta
	assertArrayEquals(arrayEsperado, coleccion.getColeccion());
	assertEquals(numElemEsperado, coleccion.size());
}
```

___
### Pruebas de excepciones
#### assertThrows
**Incluye** las excepciones heredadas de la excepción a capturar.

- Si se **espera** que la SUT lance una excepción, se usa `assertThrows(...)`.
- Si se **espera** que _no_ se lance ninguna excepción, se puede usar `assertDoesNotThrow(...)`.

En un `assertThrows(...)` si al ejecutar `sut()` no se lanza la excepción de tipo `ExpectedException` la ejecución del test fallará. Pasa lo mismo en `assertDoesNotThrow(...)` pero cuando no se lanza la excepción.

```java
@Test
void excepcionLanzadaTest() {
    ArithmeticException exception = assertThrows(
	    ArithmeticException.class, () -> sut.metodoDividir(10,0)
    );
    assertEquals("/ by zero", exception.getMessage());
}
```
#### assertThrowsExactly
**No incluye** las excepciones heredadas de la excepción a capturar.

___
### Anotaciones @BeforeEach, @AfterEach, @BeforeAll, @AfterAll

- Permiten **inicializar** y **finalizar** el estado antes/después de cada test o de _todos_ los tests, para _reducir código repetido_.
- Ejemplo:
    - `@BeforeEach` se ejecuta antes de **cada** test, por ejemplo para inicializar una variable común.
    - `@AfterEach` justo después de **cada** test, por ejemplo para cerrar ficheros o conexiones.
    - `@BeforeAll` y `@AfterAll` (métodos `static`) se ejecutan una vez al inicio y final de la clase de prueba. Para acciones previas antes de **TODOS** los tests.

> No debemos asumir nunca el orden de ejecución de los tests. No se deben implementar **NUNCA** tests cuya ejecución dependa del resultado de ejecutar otro test.

![item](../img/ppss/Anotaciones%20metodos%20java.png)

___
### Tests parametrizados

- JUnit 5 permite la **ejecución repetida** de un mismo método de prueba con diferentes parámetros, usando anotaciones como `@ParameterizedTest`, `@ValueSource`, `@MethodSource`, etc.
#### Con `@ValueSource`

```java
@ParameterizedTest
@ValueSource(strings = {"racecar", "radar", "able was I ere I saw elba"})
void testPalindromes(String candidate) {
    assertTrue(miClase.isPalindrome(candidate));
}
```

```
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running ppss.MiPruebaTest
  -> testPalindromos(String) with argument [racecar] PASSED
  -> testPalindromos(String) with argument [radar] PASSED
  -> testPalindromos(String) with argument [able was I ere I saw elba] PASSED

Results:
Tests run: 3, Failures: 0, Errors: 0, Skipped: 0

-------------------------------------------------------
BUILD SUCCESS
-------------------------------------------------------

```
#### Con `@MethodSource`

Admite pasar **múltiples parámetros** simultáneamente.

```java
@DisplayName("Calculadora_")
@ParameterizedTest(name = "[{index}]: se espera {0} para ({1}, {2})")
@MethodSource("casosDePrueba")
void testSuma(int resultadoEsperado, int a, int b) {
    int resultadoReal = Calculadora.sumar(a, b); // SUT
    Assertions.assertEquals(resultadoEsperado, resultadoReal);
}

// SIEMPRE privado, estático, sin parámetros y tipo Stream<Arguments> 
private static Stream<Arguments> casosDePrueba() {
    return Stream.of(
        Arguments.of(5, 2, 3),    // Queremos que funcione
        Arguments.of(0, 0, 0),    // Queremos que falle, imaginemos que la SUT retorna 1
        Arguments.of(-1, -2, 1),  // Queremos que falle
        Arguments.of(7, 3, 4),    // Queremos que funcione
        Arguments.of(10, 9, 1)    // Queremos que funcione
    );
}
```

- `name` en `@ParameterizedTest` representa una línea personalizada de salida la ejecución de cada test. Se muestra independientemente de si los tests pasan o fallan.
- `@MethodSource` indica el método `Stream<Arguments>` del que se obtienen los parámetros de los tests. 
	- Los argumentos **deben estar en el mismo orden** que en el driver original. 
	- El método **SIEMPRE debe ser privado, estático, no debe tener parámetros y debe ser de tipo `Stream<Arguments>`**.
- Opcionalmente se puede incluir el nombre personalizado para el test con `@DisplayName`. 

```
-------------------------------------------------------
 T E S T S
-------------------------------------------------------
Running ppss.CalculadoraTest

+-- [OK] Calculadora_[1]: se espera 5 para (2, 3) - 0.001s
+-- [FAIL] Calculadora_[2]: se espera 0 para (0, 0) - 0.001s
			   org.opentest4j.AssertionFailedError:
			   expected: <0> but was: <1>
			       at org.junit.jupiter.api.AssertionUtils.fail(AssertionUtils.java:55)
			       at org.junit.jupiter.api.Assertions.fail(Assertions.java:114)
			       at org.junit.jupiter.api.Assertions.assertEquals(Assertions.java:638)
			       ...
+-- [FAIL] Calculadora_[3]: se espera -1 para (-2, 1) - 0.001s
			   org.opentest4j.AssertionFailedError:
			   expected: <-1> but was: <0>
				   ...
+-- [OK] Calculadora_[4]: se espera 7 para (3, 4) - 0.001s
+-- [OK] Calculadora_[5]: se espera 10 para (9, 1) - 0.001s

Results:
Tests run: 5,  Failures: 2,  Errors: 0,  Skipped: 0

-------------------------------------------------------
BUILD SUCCESS
-------------------------------------------------------
```

___
## JUnit 5 y Maven

### Dependencia en el pom.xml

Para compilar y ejecutar pruebas con JUnit 5, se añade la dependencia "junit-jupiter", lo que da acceso a las clases del paquete `org.junit.jupiter.api` y `org.junit.jupiter.params`. 

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.11.4</version>
    <scope>test</scope>
</dependency>
```

- `<scope>test</scope>` significa que solo se usa en la fase de pruebas, sin incluirse en el _runtime_ normal de la aplicación. Para ejecutar los tests.

> No usamos la librería de forma explícita porque maven la invoca a través de la goal `surefire:test`.

___
### Plugin surefire

- **maven-surefire-plugin** gestiona la _ejecución_ de los tests en la fase `test`.
- Se puede **sobrescribir** la versión por defecto en el `pom.xml`:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.2</version>
</plugin>
```

- Su comando principal `mvn test` busca y ejecuta las clases cuyo nombre coincida con los patrones `**/Test*.java`, `**/*Test.java`, `**/*TestCase.java`, que estén anotados con `@Test` o `@ParameterizedTest`.
- La goal por defecto de de `mvn test` es `surefire:test`.
- Tiene empaquetado `jar` por defecto.
- Si un test falla, se produce `BUILD FAILURE`.

___
### Filtros

- `mvn test -Dgroups=rapidos` ejecuta solo los tests con el tag "rapidos".
- `mvn test -Dgroups=etiqueta1,etiqueta2 -DexcludedGroups=excluidos` ejecuta los tests con los tags "etiqueta1" y "etiqueta2" y que no estén anotados con el tag "excluidos".

___
### Informes

- Maven genera por defecto **informes** en `target/surefire-reports` en formatos txt y xml.
- Los resultados pueden presentarse:
    - **Pass**: el resultado real coincide con el esperado.
    - **Failure**: las aserciones de JUnit fallan (AssertionFailedError).
    - **Error**: excepciones ajenas a las aserciones (NullPointerException).
- Maven los muestra en el terminal tras la ejecución de la fase `test`, pero los genera JUnit.

___
## Maven y pruebas unitarias

El ciclo de vida **por defecto** incluye:
### 1. **compile**

- Compila código en `src/main/java`.
- Goal por defecto: `compiler:compile`.
### 2. **test-compile**

- Compila código de prueba en `src/test/java`.
- Goal por defecto `compiler:testCompile`.
### 3. **test** 

- Ejecuta las clases de prueba (drivers) mediante la goal por defecto `surefire:test`.
- Si algún test falla, se detiene el proceso de construcción.

___

Siguiente -> [S04 - Pruebas de Caja Negra](S04%20-%20Pruebas%20de%20Caja%20Negra.md)