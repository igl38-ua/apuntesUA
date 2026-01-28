# Resumen

- **Fase** → Representa un paso lógico dentro del ciclo de vida.  
- **Goal** → Es una tarea específica asociada a una fase.  
- **Plugin** → Conjunto de goals que pueden ejecutarse en diferentes fases.

___
# Fases, Goals y Plugins

Maven es una herramienta de construcción de proyectos Java basada en la ejecución de un **ciclo de vida** predefinido, compuesto por **fases**. Cada fase puede contener varias **goals**, que son las tareas específicas a ejecutar. Estas goals pertenecen a **plugins**, que encapsulan la funcionalidad adicional de Maven.
### 1. Ciclos de vida en Maven

Maven tiene **tres ciclos de vida principales**, cada uno compuesto por varias fases:

1. **Default Lifecycle** (Ciclo de vida por defecto)
    
    - Compuesto por **23 fases** que van desde la validación del proyecto hasta su despliegue.
    - Incluye fases importantes como `compile`, `test`, `package`, `install`, `deploy`.
2. **Clean Lifecycle**
    
    - Formado por **3 fases** (`pre-clean`, `clean`, `post-clean`).
    - Se encarga de eliminar archivos generados en construcciones anteriores.
3. **Site Lifecycle**
    
    - Formado por **4 fases** (`pre-site`, `site`, `post-site`, `deploy-site`).
    - Se usa para generar documentación del proyecto.

---
### 2. Fases en Maven

Las fases en Maven son **niveles lógicos** en el ciclo de vida de construcción. No ejecutan acciones directamente, sino que **ejecutan las goals asociadas a ellas**.

Ejemplos de fases en el **Default Lifecycle**:

- **`compile`**: Compila el código fuente.
- **`test`**: Ejecuta las pruebas unitarias usando JUnit o TestNG.
- **`package`**: Empaqueta el proyecto en un JAR o WAR.
- **`install`**: Instala el artefacto en el repositorio local (`~/.m2/repository`).
- **`deploy`**: Copia el artefacto en un repositorio remoto.

🔹 **Ejemplo de ejecución de fases**:  
Si ejecutas:

```sh
mvn package
```

Se ejecutarán **todas las fases anteriores** en orden hasta `package`.

---
### 3. Goals en Maven

Las goals son **tareas concretas** ejecutadas dentro de una fase. Cada fase puede tener varias goals asociadas.  
Por ejemplo:

- La fase **`compile`** ejecuta la goal `compiler:compile`.
- La fase **`test`** ejecuta la goal `surefire:test`.

**Ejecución directa de una goal:**

```sh
mvn compiler:compile
```

Esto ejecutará solo esa goal sin importar en qué fase del ciclo de vida se encuentre el proyecto.
El nombre de una goal SIEMPRE va precedida del nombre del plugin separado por ":".

---
### 4. Plugins en Maven

Los plugins son **conjuntos de goals** que se pueden ejecutar en diferentes fases del ciclo de vida.  
Algunos ejemplos comunes:

#### 🔹 Plugin `maven-compiler-plugin`

Usado para compilar el código fuente.

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

Este plugin tiene goals como:

- `compiler:compile` → Se ejecuta en la fase `compile`.
- `compiler:testCompile` → Se ejecuta en la fase `test-compile`.

#### 🔹 Plugin `maven-surefire-plugin`

Usado para ejecutar pruebas unitarias.

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.2</version>
</plugin>
```

Este plugin ejecuta la goal `surefire:test` en la fase `test`.

#### 🔹 Plugin `maven-jar-plugin`

Usado para empaquetar el código en un JAR.

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <version>3.2.0</version>
</plugin>
```

Se ejecuta en la fase `package`.

---
### 5. Cómo modificar o agregar Plugins y Goals

Si queremos asociar una goal a una fase específica, la agregamos en la sección `<executions>` del `pom.xml`:

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.1</version>
    <executions>
        <execution>
            <id>custom-compile</id>
            <phase>compile</phase>
            <goals>
                <goal>compile</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

---
### 6. Ejecución en IntelliJ

En **IntelliJ**, puedes ejecutar las fases y goals desde la **Maven Tool Window**, donde puedes:

- Ver todos los plugins instalados.
- Ejecutar directamente una fase o una goal específica.
- Configurar Run Configurations para automatizar builds.

