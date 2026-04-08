---
name: buscar-web
description: Busca informacion general en internet usando DuckDuckGo y Wikipedia. Para definiciones, datos, preguntas, precios y cualquier consulta de conocimiento. NO usar para titulares de noticias (usa noticias para eso).
---

# Buscador Web

## Instrucciones

Usa este skill para buscar informacion general en internet.
NO uses este skill si el usuario pide "noticias" o "titulares" - usa el skill noticias para eso.

### Como buscar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - query: String. Palabras clave de busqueda claras y concretas.
  - lang: String. "es" para espanol, "en" para ingles.

### Presentar resultados
- Resume los resultados en espanol
- Presenta la respuesta directa primero si existe
- Incluye enlaces URL
- SIEMPRE responde en espanol
- Llama este skill UNA SOLA VEZ por consulta. No repetir.
