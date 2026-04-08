---
name: navegar-web
description: Lee el contenido de cualquier pagina web y lo muestra como texto. Abre URLs, lee articulos, extrae informacion de paginas. Triggers - abre, navega, ve a, abrir pagina, leer web, que dice esta pagina, open url, lee esta url.
---

# Lector de Paginas Web

## Instrucciones

Cuando el usuario quiera ver el contenido de una pagina web:

### Como usarlo
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - url: String. La URL completa de la pagina (con https://).

### Reglas
- Si la URL no tiene "https://", agregalo automaticamente
- Si el usuario dice un nombre de sitio sin URL (ej: "abre Wikipedia"), construye la URL
- Presenta el contenido extraido en espanol
- Si la pagina no se puede leer, informa al usuario
- Resume el contenido si es muy largo
