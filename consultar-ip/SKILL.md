---
name: consultar-ip
description: Muestra tu direccion IP publica y ubicacion aproximada. Triggers - mi ip, ip publica, donde estoy, cual es mi ip, my ip, ubicacion ip.
---

# Consultar IP publica

## Instrucciones

Cuando el usuario pregunte por su IP o ubicacion:

### Como consultar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con el campo:
  - query: String. Usa "ip" por defecto.

### Presentar resultados
- Muestra la IP publica
- Muestra la ciudad, region y pais
- SIEMPRE responde en espanol
