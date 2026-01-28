# Resumen

- El código de una **SUT** debe ser **igual** al de las pruebas, no se puede alterar la SUT para hacer las pruebas.
- Para **probar los componentes de manera aislada** hay que controlar las **dependencias externas**, **inyectando dobles** que las sustituyan.
- Los **seams** son puntos del código donde se puede alterar la SUT sin modificar el código.
- Debe haber un seam por cada dependencia externa para que un componente sea testable. **A través del seam se inyectan los dobles**.
- Las **líneas** de código desde las que se **llama a las dependencias externas** son **candidatas** a SEAM.
- Hay **cuatro pasos** para automatizar las pruebas:
	- **Identificar** las dependencias externas.
	- **Refactorizar** la SUT si es necesario.
	- **Implementar** el doble (**STUB**).
	- **Implementar** el **driver**. 

___
# Dependencias externas
## Pruebas unitarias y dependencias externas

El código de la unidad a probar (SUT) debe ser **igual** que el que se utilizará en producción. **No está permitido alterar puntualmente el código de la SUT** para realizar las pruebas.
Por ejemplo:

```java
public class GestorPedidos {
	private Facturas facturas;
		1.public Facturas generarFacturas() {
		2.    //... código
		3.    boolean ok = facturas.pendientes(); // dependencia, entrada indirecta
		4.    if (ok) {
		5.       //sentencias then
		6.    } else {
		7.       //sentencias else
		8.    }
		9.    return facturas;
		10.}
}
```

La variable `ok` es una **entrada indirecta** de la SUT, una **dependencia**.

___
## Código testable y control de dependencias

Para probar los componentes de forma aislada hay que poder controlar las dependencias externas. Para ello desarrollamos los **DOBLES**, que sustituyen a las dependencias externas durante las pruebas. 
### Seams

- Un **seam** es un punto del código donde se puede alterar el comportamiento de la SUT sin modificar su código.
- Para que un componente sea testable debe disponer de **un seam por cada dependencia externa**, para que en las pruebas se puedan **inyectar los dobles** en lugar de usar las dependencias reales.
- Si la SUT **no tiene un seam** e debe **refactorizar** para crearlo.

> A través de los seam enabling points, desde los **dobles** se inyectan las dependencias externas en la SUT. 
### Como identificar un Seam

Las líneas de código desde las que se llama a las dependencias externas son candidatas a SEAM.

![item](../img/ppss/identificar%20seams.png)

- En el primer caso **NO** es un seam porque el objeto se crea dentro del método, con lo que no se le puede inyectar un doble sin modificar el código de la SUT. 
- En el segundo caso **SI** lo es porque podemos manipular el objeto con funciones externas 
- fuera de la SUT. Con un stub, un mock...

___

En caso de que los objetos se declaren en la SUT, se consideran seams si utilizan setters, getters y otros métodos que pueden ser sustituibles mediante una stub o mock. 

```java
public class CustomSpreadsheet {

	public Cell getCell (){ // Aquí se inyecta el doble durante las pruebas
		return new ValueCell();
	}

	// SUT
	public Spreadsheet buildSheet(){
		Cell myCell = getCell();
		myCell.recalculate(); //seam
	}
}

public class TestableCustomSpreadsheet extends CustomSpreadSheet {
	@Override
	public Cell getCell(){
		return new DoubleCell(); // desde aquí se inyecta el doble
	}
}

public class DoubleCell extends Cell{
	@Override
	public recalculate(){
		...
	}
}
```

___
## Pasos a seguir para automatizar las pruebas
### D1. Identificar las dependencias externas

 - Localizar todas las llamadas a métodos de otras unidades que afecten al comportamiento de la SUT.
### D2. Refactorizar la SUT si es necesario

- Asegurarse de que las **dependencias son inyectables** para poder usar un doble (stub), **refactorizando** la SUT si fuera necesario.
- Formas de **INYECTAR** el doble en nuestra SUT (Dependency Injection):
	1. Como un **PARÁMETRO** de nuestra SUT.
	2. A través del **CONSTRUCTOR** de la clase que contiene nuestra SUT.
	3. A través de un **MÉTODO SETTER** de la clase que contiene nuestra SUT.
	4. A través de un método de **FACTORÍA LOCAL** de la clase que contiene nuestra SUT, o una **CLASE FACTORIA**.
### D3. Implementar el doble (STUB o MOCK)

- Un **stub controla las entradas indirectas** que la dependencia podría dar a la SUT.
- El stub **hereda o implementa la misma interfaz/clase** que la dependencia real, **sobre escribiendo** el método correspondiente con la lógica necesaria para devolver datos controlables en las pruebas.
### D4. Implementar el driver

- El **test crea la SUT e inyecta el stub** en lugar de la dependencia real. Fase *Arrange*
- En la fase *Act* se **invoca** al método de la SUT.
- En la fase *Assert* se verifica el estado resultante.

Esto consiste en **verificación basada en el estado**, ya que se analiza el estado final de la SUT, no las interacciones o llamadas concretas.

![item](../img/ppss/fase%204%20implementacion%20del%20dirver.png)

![item](../img/ppss/implementación%20driver%20codigo.png)

___
## [Flujo de dependencias externas y ficheros en STUBs](S05.1%20-%20Flujo%20de%20dependencias%20y%20ficheros%20en%20STUBs.md)

___
## Ejemplos

Se usa una **factoría local** para refactorizar la SUT. Opción 4 de D2.

![item](../img/ppss/ejemplo%202%20dependencias.png)

Se usa la **clase factoría** para refactorizar la SUT. Opción 3 de D2.

![item](../img/ppss/ejemplo%203%20dependencias.png)

___

Siguiente -> [S06 - Dependencias externas 2 (mocks)](S06%20-%20Dependencias%20externas%202%20(mocks).md)