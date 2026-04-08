---
name: clima
description: Consulta el clima actual y pronostico de cualquier ciudad del mundo usando wttr.in. NO requiere API key. Triggers - clima, tiempo, temperatura, llueve, pronostico, weather, hace frio, hace calor.
---

# Clima actual

## Instrucciones

Cuando el usuario pregunte por el clima o tiempo de una ciudad:

### Como consultar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - city: String. Nombre de la ciudad (ej: "Bilbao", "Madrid", "New York").
  - lang: String. "es" para espanol, "en" para ingles.

### Presentar resultados
- Indica temperatura actual, condicion (soleado, nublado, lluvia, etc.)
- Menciona humedad y viento si estan disponibles
- SIEMPRE responde en espanol
