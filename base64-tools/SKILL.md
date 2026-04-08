---
name: base64-tools
description: Codifica y decodifica texto en Base64, URL encode/decode, y HTML entities. Util para desarrolladores. Triggers - base64, encode, decode, codificar, decodificar, url encode, html encode.
---

# Herramientas de Codificacion

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - action: String. Una de: "base64_encode", "base64_decode", "url_encode", "url_decode", "html_encode", "html_decode"
  - text: String. El texto a procesar.

### Presentar resultados
- Muestra el texto original y el resultado
- Indica que codificacion se uso
- SIEMPRE responde en espanol
