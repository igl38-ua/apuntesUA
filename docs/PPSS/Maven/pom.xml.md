### **📌 ¿Qué es el `pom.xml` en Maven?**

El archivo `pom.xml` (**Project Object Model**) es el **corazón** de cualquier proyecto Maven. Es un archivo XML que **define la configuración y la estructura del proyecto**, incluyendo:

✔ **Coordenadas del proyecto** (identificación única).  
✔ **Dependencias** (librerías externas necesarias).  
✔ **Fases y plugins** (configuración del proceso de construcción).  
✔ **Propiedades y configuración general**.  
✔ **Gestión de repositorios (locales/remotos)**.

Maven **lee el `pom.xml` para ejecutar la construcción** del proyecto de manera automática, sin necesidad de escribir scripts de compilación manualmente.

---

### **📌 Estructura básica de `pom.xml`**

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>

    <!-- 📌 Coordenadas del proyecto -->
    <groupId>com.ejemplo</groupId>
    <artifactId>mi-proyecto</artifactId>
    <version>1.0.0</version>

    <!-- 📌 Propiedades globales -->
    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
    </properties>

    <!-- 📌 Dependencias (librerías externas) -->
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.11.4</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <!-- 📌 Configuración de plugins -->
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

---

## **📌 Explicación de las secciones del `pom.xml`**

### **1️⃣ Coordenadas del Proyecto**

Estas etiquetas identifican de forma única un proyecto Maven:

```xml
<groupId>com.ejemplo</groupId>   <!-- Organización o empresa -->
<artifactId>mi-proyecto</artifactId>   <!-- Nombre del proyecto -->
<version>1.0.0</version>   <!-- Versión del proyecto -->
```

➡ Esto define el **artefacto Maven** generado, como:  
`com.ejemplo:mi-proyecto:1.0.0`

---

### **2️⃣ Propiedades**

```xml
<properties>
    <maven.compiler.source>11</maven.compiler.source>
    <maven.compiler.target>11</maven.compiler.target>
</properties>
```

✔ Permite definir **valores reutilizables** en el `pom.xml`.  
✔ Aquí se especifica que el código debe compilarse con **Java 11**.

---

### **3️⃣ Dependencias (librerías externas)**

```xml
<dependencies>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.11.4</version>
        <scope>test</scope>
    </dependency>
</dependencies>
```

✔ Agrega librerías externas necesarias para el proyecto.  
✔ **Ejemplo:** La dependencia `JUnit 5.11.4` permite ejecutar pruebas unitarias.  
✔ El atributo **`scope="test"`** indica que esta dependencia **solo se usa en pruebas**.

➡ Cuando agregamos una dependencia, Maven la **descarga automáticamente** desde **Maven Central Repository** y la almacena en `~/.m2/repository/`.

---

### **4️⃣ Configuración de Plugins**

Los **plugins** en Maven permiten ejecutar tareas específicas en diferentes fases del ciclo de vida.

#### **Ejemplo: Plugin de compilación (`maven-compiler-plugin`)**

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.1</version>
    <configuration>
        <source>11</source>
        <target>11</target>
    </configuration>
</plugin>
```

✔ **Se usa para compilar código Java.**  
✔ Define que la versión de Java es **11**.  
✔ Se ejecuta automáticamente en la fase `compile` de Maven.

#### **Ejemplo: Plugin para ejecutar pruebas (`maven-surefire-plugin`)**

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.2</version>
</plugin>
```

✔ Se ejecuta en la fase `test`.  
✔ Permite ejecutar pruebas con JUnit.

---

### **5️⃣ Configuración de Construcción (`<build>`)**

Dentro de la etiqueta `<build>`, podemos modificar cómo se genera el proyecto:

```xml
<build>
    <plugins>
        <!-- Aquí van los plugins -->
    </plugins>
</build>
```

✔ **Define los plugins que se ejecutarán en cada fase**.  
✔ **Personaliza el proceso de construcción del proyecto**.

---

## **📌 ¿Para qué sirve `pom.xml`?**

✔ 📌 **Define la estructura del proyecto y sus dependencias**.  
✔ 📌 **Automatiza la compilación, empaquetado y pruebas**.  
✔ 📌 **Evita incluir manualmente archivos `.jar`**, ya que Maven los descarga automáticamente.  
✔ 📌 **Permite configurar fases y plugins específicos** para tareas como pruebas, empaquetado y despliegue.  
✔ 📌 **Facilita el uso de diferentes entornos de desarrollo** con versiones consistentes de dependencias.

---

## **📌 Ejemplo de uso en la práctica**

Si necesitas compilar y probar tu proyecto Maven, **Maven usará `pom.xml` para saber qué hacer**.

Ejemplo de ejecución:

```sh
mvn compile
```

✔ Maven buscará en `pom.xml` qué dependencias necesita.  
✔ Descargará automáticamente cualquier `.jar` faltante.  
✔ Compilará el código con el `maven-compiler-plugin`.

Si ejecutamos:

```sh
mvn test
```

✔ Ejecutará las pruebas usando `maven-surefire-plugin` y JUnit.

Si ejecutamos:

```sh
mvn package
```

✔ Empaquetará el proyecto en un `.jar` o `.war` en la carpeta `target/`.

---

## **📌 Resumen**

📌 **`pom.xml` es el archivo central de configuración de Maven.**  
📌 **Define coordenadas, dependencias, plugins y procesos de construcción.**  
📌 **Maven usa `pom.xml` para automatizar la compilación, pruebas y empaquetado.** 
📌 **Evita la necesidad de configurar manualmente el entorno.**
