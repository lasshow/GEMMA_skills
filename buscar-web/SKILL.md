---
name: buscar-web
description: Busca informacion en internet combinando DuckDuckGo y Wikipedia. Encuentra respuestas, datos, definiciones, biografias y cualquier tema. Triggers - busca, googlea, investiga, que es, quien es, precio, search, como se hace, informacion sobre, dime sobre.
---

# Buscador Web

## Instrucciones

Cuando el usuario quiera buscar CUALQUIER cosa en internet, usa esta herramienta.

### Como buscar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - query: String. Palabras clave de busqueda claras y concretas.
  - lang: String. "es" para espanol, "en" para ingles. Usa el mismo idioma que el usuario.

### Presentar resultados
- Resume los resultados en espanol de forma clara
- Presenta primero la respuesta directa si existe
- Luego los resultados web
- Luego Wikipedia si aplica
- Incluye los enlaces URL cuando esten disponibles
- Si no hay resultados, sugiere al usuario otros terminos
- SIEMPRE responde en espanol
