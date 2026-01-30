# apuntesUA

Apuntes en Markdown publicados con MkDocs.

## Instalación

```bash
python3 -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -r requirements.txt
```

## Desarrollo local

```bash
.venv/bin/mkdocs serve
```

## Build

```bash
.venv/bin/mkdocs build
```

## Deploy a GitHub Pages (rama `gh-pages`)

Esto compila y publica **solo** el contenido generado (lo de `site/`) en la rama `gh-pages`.

```bash
.venv/bin/mkdocs gh-deploy --clean --force
```

Notas:

- Por defecto usa la rama `gh-pages` y publica en la raíz del branch.