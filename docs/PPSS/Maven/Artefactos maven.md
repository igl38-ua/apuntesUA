## **¿Qué son los artefactos en Maven?**

Un **artefacto** en Maven es **cualquier archivo construido, utilizado o generado** en el proceso de construcción de un proyecto. Los artefactos pueden ser:

✅ **Librerías (`.jar`)**: Dependencias externas que usa tu proyecto.  
✅ **Archivos compilados (`.class`)**: Código fuente transformado en bytecode.  
✅ **Archivos empaquetados (`.jar`, `.war`, `.ear`)**: Aplicaciones listas para ejecutarse o desplegarse.  
✅ **Plugins de Maven (`maven-compiler-plugin`, `maven-surefire-plugin`)**: Herramientas usadas en la construcción del proyecto.  
✅ **Archivos de documentación (`.zip`, `.xml`)**: Generados por el ciclo de vida `site`.

Cada artefacto en Maven **tiene una identificación única** dentro del repositorio de Maven. Esto permite que distintos proyectos lo usen sin conflictos.

---

## **📌 ¿Cómo se identifican los artefactos en Maven?**

Maven identifica un artefacto con **tres coordenadas principales**:

```xml
<groupId>org.junit.jupiter</groupId>
<artifactId>junit-jupiter-api</artifactId>
<version>5.11.4</version>
```

➡ **Formato de identificación:**  
`groupId:artifactId:version`

Ejemplo de artefacto específico:

```
org.junit.jupiter:junit-jupiter-api:5.11.4
```

**Explicación de cada coordenada:**

1. **`groupId`** → Identifica el grupo u organización del artefacto. Ej: `org.apache.maven.plugins`
2. **`artifactId`** → Nombre del artefacto. Ej: `maven-compiler-plugin`
3. **`version`** → Versión específica del artefacto. Ej: `3.8.1`

📌 **Opcionalmente**, se puede incluir: 4. **`packaging`** → Formato del artefacto (`jar`, `war`, `pom`, `ear`, etc.).

```xml
<packaging>jar</packaging>
```

Si no se especifica, el valor por defecto es **`jar`**.

Ejemplo completo:

```
org.apache.maven.plugins:maven-compiler-plugin:3.8.1:jar
```

---

## **📌 ¿Dónde se almacenan los artefactos en Maven?**

Los artefactos Maven se **descargan y almacenan en repositorios**.

### **📍 1. Repositorio Local (`~/.m2/repository/`)**

📌 Cuando Maven descarga un artefacto, lo guarda en el directorio:

```
C:\Users\tu-usuario\.m2\repository\  (Windows)
~/.m2/repository/  (Linux/macOS)
```

Ejemplo:

```
~/.m2/repository/org/junit/jupiter/junit-jupiter-api/5.11.4/junit-jupiter-api-5.11.4.jar
```

➡ **Cada artefacto se organiza por carpetas basadas en su groupId y version**.

### **📍 2. Repositorio Remoto (Maven Central y otros)**

Si un artefacto no está en el repositorio local, **Maven lo busca en repositorios remotos** como:

🔹 [**Maven Central Repository**](https://mvnrepository.com/)  
🔹 Repositorios privados de empresas  
🔹 Otros repositorios públicos

Ejemplo: Si agregas esta dependencia:

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter-api</artifactId>
    <version>5.11.4</version>
</dependency>
```

Maven **descargará automáticamente** `junit-jupiter-api-5.11.4.jar` desde **Maven Central** si no está en tu repositorio local.

### **📍 3. Repositorio de tu organización**

Las empresas pueden tener **repositorios internos** con artefactos privados.  
Se configuran en `pom.xml` así:

```xml
<repositories>
    <repository>
        <id>mi-repositorio-interno</id>
        <url>https://repo.miempresa.com/maven2</url>
    </repository>
</repositories>
```

---

## **📌 Tipos de artefactos en Maven**

Los artefactos pueden tener distintos **tipos de empaquetado**, definidos en el `pom.xml`:

|**Tipo**|**Extensión**|**Descripción**|
|---|---|---|
|**`jar`**|`.jar`|Archivo Java compilado (el más común).|
|**`war`**|`.war`|Aplicación web para servidores como Tomcat.|
|**`ear`**|`.ear`|Aplicación empresarial Java EE.|
|**`pom`**|`.pom`|Proyecto padre de Maven, sin código fuente.|
|**`zip`**|`.zip`|Archivo comprimido con documentación o código.|

Ejemplo:

```xml
<packaging>war</packaging>
```

Si ejecutas:

```sh
mvn package
```

✔ Maven generará un `mi-proyecto.war` en la carpeta `target/`.

---

## **📌 ¿Cómo se generan los artefactos en Maven?**

Maven **genera artefactos** cuando ejecutas comandos como:

### 🔹 **1. `mvn package` → Genera un `.jar` o `.war`**

```sh
mvn package
```

✔ Compila el código y crea el artefacto en `target/`.

Ejemplo de salida:

```
[INFO] Building jar: /ruta/del/proyecto/target/mi-proyecto-1.0.0.jar
```

### 🔹 **2. `mvn install` → Instala el artefacto en el repositorio local**

```sh
mvn install
```

✔ Copia el `.jar` generado en `~/.m2/repository/` para que otros proyectos lo usen.

Ejemplo:

```
~/.m2/repository/com/ejemplo/mi-proyecto/1.0.0/mi-proyecto-1.0.0.jar
```

### 🔹 **3. `mvn deploy` → Sube el artefacto a un repositorio remoto**

Si trabajas en equipo y quieres compartir el artefacto:

```sh
mvn deploy
```

✔ Sube el `.jar` a un repositorio remoto, como Nexus o Artifactory.

---

## **📌 Artefactos en la práctica**

En la práctica 1:

✅ **Cuando ejecutas `mvn package`, se generará un artefacto `.jar`** en `target/`.  
✅ **Cuando ejecutas `mvn install`, ese `.jar` se guardará en `~/.m2/repository/`.**  
✅ **Puedes usar el comando `mvn dependency:tree` para ver qué artefactos usa tu proyecto.**

---

## **📌 Resumen**

📌 **Un artefacto Maven es cualquier archivo utilizado o generado en la construcción de un proyecto.**  
📌 **Cada artefacto tiene una identificación única (`groupId:artifactId:version`).**  
📌 **Los artefactos se almacenan en el repositorio local (`~/.m2/repository/`) y, si no existen, Maven los descarga del repositorio remoto.**  
📌 **Los artefactos pueden ser `.jar`, `.war`, `.ear`, `.pom`, etc.**  
📌 **Los comandos `mvn package`, `mvn install` y `mvn deploy` generan y almacenan artefactos.**
