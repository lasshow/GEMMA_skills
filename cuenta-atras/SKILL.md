---
name: cuenta-atras
description: Cuenta atras para eventos importantes. Cuantos dias faltan para una fecha. Triggers - cuanto falta, dias para, countdown, cuenta atras, cuantos dias, faltan dias, cuando es.
---

# Cuenta Atras

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - action: String. "countdown" o "between".
  - date: String. Fecha objetivo en formato "YYYY-MM-DD".
  - date2: String (solo para "between"). Segunda fecha.
  - event: String. Nombre del evento (opcional).

### Presentar resultados
- Muestra dias, horas restantes
- Si la fecha ya paso, indica cuanto hace
- SIEMPRE responde en espanol
