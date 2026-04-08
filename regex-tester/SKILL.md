---
name: regex-tester
description: Prueba expresiones regulares contra texto. Muestra coincidencias, grupos y capturas. Triggers - regex, expresion regular, regexp, patron, match, test regex, probar regex.
---

# Probador de Regex

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - pattern: String. La expresion regular.
  - text: String. El texto donde buscar.
  - flags: String. Flags opcionales ("g", "i", "gi", etc.). Por defecto "g".

### Presentar resultados
- Muestra coincidencias encontradas
- Muestra grupos de captura si existen
- Indica posicion de cada match
- SIEMPRE responde en espanol
