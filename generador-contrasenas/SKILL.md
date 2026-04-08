---
name: generador-contrasenas
description: Genera contrasenas seguras y aleatorias. Personaliza longitud y tipo de caracteres. Triggers - contrasena, password, genera clave, clave segura, generar contrasena, password seguro.
---

# Generador de Contrasenas Seguras

## Instrucciones

Genera contrasenas seguras y aleatorias usando la herramienta JavaScript.

### Como generar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - length: Number. Longitud de la contrasena (por defecto 16).
  - type: String. Tipo: "full" (todo), "alpha" (solo letras+numeros), "pin" (solo numeros).
  - count: Number. Cantidad de contrasenas a generar (por defecto 3).

### Presentar resultados
- Muestra las contrasenas generadas
- Indica la fortaleza estimada
- Recomienda al usuario guardarla en un gestor de contrasenas
- SIEMPRE responde en espanol
