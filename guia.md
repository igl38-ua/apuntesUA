# Guía de modificación de enlaces de Obsidian a Markdown web
## Enlaces de imágenes y ficheros .md

- **Original**: \[[ada/imagen.png]]
- **Nuevo**: \[imagen](img/ada/imagen.png)

___

- **Original**: \[[ADA/Cotas.md]]
- **Nuevo**: \[Cotas](ADA/Cotas.png)

___

- Todos los ficheros de apuntes van en la carpeta `docs` en su correspondiente subcarpeta.
- Todas las imágenes van en la carpeta `img` en su correspondiente subcarpeta.
- Se deben respetar los espacios en los nombres de los ficheros sustituyéndolos por `%20` en la parte del link externo ( ).
    - Esto no es necesario para las rutas relativas en `mkdocs.yml`.