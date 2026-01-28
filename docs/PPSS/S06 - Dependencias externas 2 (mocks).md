# Resumen

- En la **verificación basada en el estado (STUB)** se comprueba el estado resultante de la SUT, en la **verificación basada en el comportamiento (MOCKS)** se comprueba la interacción con las dependencias externas. 
- Hay **cuatro pasos** para automatizar las pruebas:
	- **Identificar** las dependencias externas.
	- Asegurarse de la que SUT es **testable**.
	- **Implementar** el doble (**MOCK**).
	- **Implementar** el **driver**. 
- El framework **EasyMock** permite **crear automáticamente objetos** de las clases que contienen a nuestros dobles.
- Con **EasyMock** se pueden implementar tanto **STUBS** como **MOCKS** cada uno con criterios diferenciados.
- Los métodos principales son:
	- `expect(...)` para las **expectativas**.
	- `andStubReturn(...)` si devuelve **valor**, o `expectedLastCall(...)` si es **void**.
	- `replay(...)` para **activar** el doble.
	- `verify(...)` para **verificar que la SUT invoca los mocks**.
	- `andReturn(...).times(...)` times opcional, o `andThrow(...)` para excepciones.

___
# Dependencias externas
## Verificación y pruebas unitarias

Dos enfoques de verificación en las pruebas unitarias. 

1. **Basada en el estado**. Se comprueba el estado resultante del SUT.
2. **Basada en el comportamiento**. Se comprueba la interacción con las dependencias externas (como y cuantas veces se llaman).

En ambos casos el objetivo es detectar defectos durante las pruebas unitarias.

___
## Proceso para automatizar las pruebas unitarias (recordatorio S05)

1. **Identificar** dependencias externas.
2. Asegurarse de que la SUT es **testable**.
3. Proporcionar **dobles** (stubs o **mocks**) para reemplazar las dependencias. Mocks en esta sesión.
4. Implementar los **drivers** y definir el tipo de verificación (estado o comportamiento).

___
## Frameworks para implementar dobles

Para el desarrollo de los dobles (**mocks**) lo mejor es utilizar frameworks dedicados. 
Los frameworks generan un implementación configurable trabajando "**sobre la marcha**", generando el bytecode necesario.  
 
- Facilitan la creación de dobles de forma **dinámica**. 
- Permiten **configurar las expectativas sobre los métodos invocados**. 

___
# EasyMock

EasyMock crea de forma **automática** un **objeto** de la clase que contiene nuestro doble.

```java
EasyMock.niceMock(Clase.class) 
// devuelve un OBJETO que extiende/implementa la clase/interfaz "Clase.class"
```

El OBJETO tiene las siguientes características: 

- El **orden** en que se realizan las invocaciones de los métodos **NO** se **chequea**.
- Por defecto se permiten las invocaciones a **TODOS** los métodos del OBJETO. **Si no hemos programado las expectativas del algún método** se devuelven los valores correspondientes por defecto: **0, null, o false (tipo primitivo, objeto o bool)**.
- Todas las **invocaciones esperadas** a métodos del doble se tienen que hacer con los **argumentos que se especifican**.

> Una vez se crea el doble, hay que programar sus expectativas para que controle las entradas indirectas a la SUT (STUB). Si no las controla se devuelven los valores por defecto que define EasyMock. 

___
## EasyMock: Implementación de STUBS

1. Creamos el **doble** con `niceMock(Clase.class)`. (**El objeto que contiene el STUB**).

```java
import org.easymock.EasyMock;
...
Dependencia1 dep1 = EasyMock.niceMock(Dependencia1.class); 
// Dependencia1.class es la clase que contiene la dependencia externa

//dep1 no chequea el orden de invocaciones
//se permiten invocaciones no programadas, en ese caso se
//devolverán los valores por defecto 0, null o falso
```

2. **Programamos las expectativas** con `EasyMock.expect(...).andStubReturn(...)` o `.andStubThrow(...)` para excepciones.

```java
//metodo1() devolverá 9 si es invocado por nuestro SUT
//independientemente de cuándo o cuántas veces sea invocado

//y con qué valores de parámetros sea invocado
EasyMock.expect(dep1.metodo1(anyString(),anyInt())).andStubReturn(9);

//metodo2() devolverá una excepción cuando se invoque desde SUT
EasyMock.expect(dep1.metodo2(anyObject())).andStubThrow(new MyException("message"));

dep1.metodo3(anyInt()); //metodo3 es un método que devuelve void
EasyMock.expectLastCall.asStub();
```

Si `EasyMock.expectLastCall.asStub();` aparece **inmediatamente después** de un método, se considera stub. Se utiliza en métodos **void** que **no tienen valor de retorno**, en los que no se puede poner `.andStubReturn(...)`.

3. Llamamos a `EasyMock.replay(...)` para **activar** el doble.

```java
EasyMock.replay(dep1);
```

Si **no cambiamos el estado del doble a "replay"** las expectativas **NO** se tendrán en cuenta, por lo que **si se invoca al doble** desde nuestro SUT **se devolverán los valores por defecto**.

___
### Ejemplo de programación de expectativas

```java
//creamos el doble
Dependencia dep = EasyMock.niceMock(Dependencia.class);

//programamos las expectativas
//CADA vez que nuestro SUT invoque a servicio4 con un 12, devolverá 25
//independientemente del número de invocaciones
EasyMock.expect(dep.servicio4(12)).andStubReturn(25);

//si nuestro SUT invoca a servicio4 con cualquier otro valor, devolverá 30
//independientemente del número de veces que se invoque
EasyMock.expect(dep.servicio4(EasyMock.not(EasyMock.eq(12)))).andStubReturn(30);

//si nuestro SUT invoca servicio5(8) siempre -> el stub devolverá null todas las veces
//null es el valor por defecto para los Strings
//si nuestra SUT no invoca nunca servicio5(3), el test NO fallará
EasyMock.expect(dep.servicio5(3)).andStubReturn("pepe");
```

Los métodos `not()` y `eq()` admiten como parámetro tanto tipos primitivos como objetos.

```java
//otros métodos que pueden usarse
and(X first, X second), or(X first, X second)//X puede ser de tipo primitivo o un objeto
lt(X value), leq(X value), geq(X value), gt(X value) //Para X = tipo primitivo
startsWith(String prefix), contains(String substring), endsWith(String suffix)
isNull(), notNull()
```

___
### Ejemplos: Driver con STUBS y EasyMock

![item](../img/ppss/ejemplo%201%20easymock.png)

![item](../img/ppss/ejemplo%202%20easymock.png)

___
## Objetos STUB vs Objetos MOCK
### STUB

- Se **centra** en **entradas indirectas** que la SUT utiliza
- **No** puede hacer **que el test falle**, simplemente devuelve datos.
### MOCK

- **Comprueba interacciones** (cantidad de llamadas, orden, parámetros).
- Puede **forzar un fallo** en caso de que **no se cumplan las expectativas**.

![item](../img/ppss/stub%20vs%20mock.png)

___
## EasyMock y tipos de dobles

- `niceMock(...)`: **no falla con métodos sin programar**. Útil como stub.
- `mock(...)`: **no chequea orden**, pero **falla si hay llamadas no programadas**.
- `strictMock(...)`: **chequea el orden de las invocaciones y falla si difiere de lo esperado**.

![item](../img/ppss/easymock%20y%20tipos%20de%20dobles.png)

___
## EasyMock: Implementación de MOCKS

1. Crear **mock** (`mock(...)` o `strictMock(...)`) a partir de una clase o interfaz.

```java
import org.easymock.EasyMock;
...
//si sólo invocamos a 1 método de dep1 desde nuestra SUT
Dependencia1 dep1 = EasyMock.mock(Dependencia1.class);

//en cualquier otro caso
Dependencia2 dep2 = EasyMock.strictMock(Dependencia2.class);
```

Para `dep2` si que importa el orden de invocaciones porque utiliza `strictMock(...)`.

2. **Programar expectativas detalladas** (métodos, parámetros, valores devueltos, número de invocaciones, etc.).

```java
//metodo1() será invocado sólo una vez desde nuestro SUT con los
//parámetros indicados y devolverá 9
EasyMock.expect(dep2.metodo1("xxx",7)).andReturn(9);
//metodo1() será invocado 1 vez desde SUT y devolverá una excepción

EasyMock.expect(dep2.metodo1("yy",4)).andThrow(new MyException("message"));
//metodo2() será invocado 1 vez desde nuestra SUT.
//metodo2() es un método que devuelve void
dep1.metodo2(15);
```

3. **SIEMPRE** se ACTIVA el mock usando el método `replay()`.

```java
EasyMock.replay(dep1,dep2);
```

> Si no activamos el mock las expectativas no tienen efecto.

4. **SIEMPRE** Verificar que la SUT invoca a los mocks. **Confirma que las interacciones reales coinciden con las programadas**.

```java
EasyMock.verify(dep1,dep2);
```

> Si no invocamos a alguna expectativa desde la SUT se lanzará la excepción `AssertionError`.

___
### Ejemplo de programación de expectativas

- Cuando **ejecutamos la SUT** durante las pruebas, el mock **registrará TODAS las interacciones desde el SUT**.

Para especificar las expectativas podemos indicar:
#### Número de invocaciones

```java
expect(mock.metodoX("parametro")) //invocamos al métodoX(), con el parámetro especificado
	.andReturn(42).times(3) //devuelve 42 las tres primeras veces
	.andThrow(new RuntimeException(), 4) //las siguientes 4 llamadas devuelven una excepción
	.andReturn(-42); //la siguiente llamada devuelve -42 (una única vez)
```

Las expectativas se pueden **encadenar**:

```java
expect(mock.operation()).andReturn(true).times(5)
.andThrow(new RuntimeException("message"));

// en lugar de

expect(mock.operation().andReturn(true).times(5);
expectLastCall().andThrow(new RuntimeException("message"));
```
#### Valores de parámetros

- Comparación por `equals()` o por coincidencia exacta para comparar **objetos**.
- Patrones como `anyObject()`, `same(obj)` (exactamente la misma instancia especificada), `isNull()`, `notNull()`.
#### Orden de invocación de expectativas

- Si creamos dos `strictMock` independientemente, no se checa el orden **entre** ellos.

```java
Doc1 mock1 = EasyMock.strictMock(Doc1.class);
Doc2 mock2 = EasyMock.strictMock(Doc2.class);
/* si las expectativas determinan un cierto orden
	entre las invocaciones a mock1 y mock2,
	si nuestra SUT NO sigue ese orden de invocaciones
	el test NO falla */
replay(mock1,mock2);
//invocamos a nuestro SUT
verify(mock1,mock2);
```

- Para chequear también el orden entre múltiples mocks, se utiliza `IMocksControl` con `createStrictControl()`.
	- A partir de ese `ctrl`, se invocan `ctrl.mock(Clase.class)` para crear los mocks.
	- `ctrl.replay()` y `ctrl.verify()` validan las interacciones en conjunto.

```java
IMocksControl ctrl = EasyMock.createStrictControl();
Doc1 mock1 = ctrl.mock(Doc1.class);
Doc2 mock2 = ctrl.mock(Doc2.class);
//si las expectativas determinan un cierto orden
//entre las invocaciones a mock1 y mock2,
//si nuestro SUT no sigue ese orden de invocaciones
//el test fallará
ctrl.replay(); //no es necesario usar parámetros
//invocamos a nuestro SUT
ctrl.verify();
```

___
### Ejemplo de uso de mocks con EasyMock

![item](../img/ppss/mocks%20con%20easymock.png)

![item](../img/ppss/mocks%20con%20easymock%201.png)

___
## Diferencia EasyMock:STUBS y EasyMock:MOCKS

El **proceso de implementación** es el mismo para ambos. Tanto con stubs como con mocks sigues estos pasos básicos:

1. **Identificar** las dependencias externas.
2. Asegurarte de que la SUT es testable.
3. **Implementar** el doble (ya sea stub o mock).
4. **Implementar** el driver de prueba.

La diferencia radica en la configuración del doble:

- Con **stubs** usas métodos como `andStubReturn(...)` para definir respuestas fijas, enfocándote en la verificación del estado de la SUT.
- Con **mocks** defines expectativas precisas sobre las interacciones (llamadas, orden, parámetros) utilizando métodos como `expect(...)`, `andReturn(...)`, `andThrow(...)`, etc.

> Las **STUBS** se configuran para **devolver datos predefinidos** sin comprobar las interacciones (número, orden o parámetros de las llamadas). **Verificación basada en el estado**.
> Los **MOCKS** definen y modifican esas interacciones que los stubs no tienen en cuenta. **Verificación basada en el comportamiento**.

___
## Partial Mocking

A veces podemos necesitar proporcionar una implementación ficticia de **sólo de algunos métodos concretos** de la clase, no toda entera (partial mocking). 
Esto ocurre cuando se hacen **llamadas entre métodos de su misma clase**.

```java
ToMock mock = partialMockBuilder(ToMock.class).addMockedMethod("mockedMethod").mock(); 
// podría ser también .strictMock() o .mock() dependiendo de lo queramos hacer

// Ejemplo
EasyMock.partialMockBuilder(Rectangle.class).addMockedMethod("convertX","convertY").strictMock();
```

- El método añadido con `addMockecdMethod()` será "mocked" (sustituido por su doble), el resto se ejecutan con el código original. 

![item](../img/ppss/partial%20mocking.png)

- **Constructor con parámetros**: se ilustra `withConstructor(...)` para crear un objeto con un constructor personalizado.

![item](../img/ppss/constructor%20con%20parámetros.png)

![item](../img/ppss/driver%20S06.png)