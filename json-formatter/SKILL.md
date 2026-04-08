---
name: json-formatter
description: Formatea, valida y minifica JSON. Util para desarrolladores y APIs. Triggers - json, formatear json, validar json, minificar json, json bonito, pretty json, json lint.
---

# Formateador JSON

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - action: String. Una de: "format", "minify", "validate"
  - json_text: String. El JSON a procesar.

### Presentar resultados
- Para format: muestra el JSON identado con 2 espacios
- Para minify: muestra el JSON en una sola linea
- Para validate: indica si es valido y muestra errores si los hay
- SIEMPRE responde en espanol
