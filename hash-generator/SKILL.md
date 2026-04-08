---
name: hash-generator
description: Genera hashes criptograficos SHA-1, SHA-256, SHA-512. Util para verificar archivos y seguridad. Triggers - hash, sha, sha256, sha512, sha1, checksum, hashear, cifrar texto.
---

# Generador de Hashes

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - text: String. El texto a hashear.
  - algorithm: String. Uno de: "SHA-1", "SHA-256", "SHA-512". Por defecto "SHA-256".

### Presentar resultados
- Muestra el hash resultante
- Indica el algoritmo usado
- SIEMPRE responde en espanol
