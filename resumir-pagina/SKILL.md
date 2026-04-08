---
name: resumir-pagina
description: Lee y resume el contenido de cualquier pagina web. Extrae texto de URLs, articulos, noticias y blogs. Triggers - resume esta pagina, lee este articulo, que dice esta web, extrae texto de, summarize page, resumir.
---

# Resumidor de Paginas Web

## Instrucciones

Cuando el usuario quiera resumir una pagina web:

### Como usarlo
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - url: String. La URL completa de la pagina a resumir.

### Presentar resultados
- Resume el contenido en 3-5 puntos clave en espanol
- Menciona el titulo del articulo si se encontro
- Si el usuario pide algo especifico, enfocate en eso
- Maximo 300 palabras en el resumen
- Si la pagina no carga, informa al usuario
