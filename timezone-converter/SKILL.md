---
name: timezone-converter
description: Convierte horas entre zonas horarias del mundo. Util para reuniones internacionales. Triggers - hora en, que hora es en, zona horaria, timezone, convertir hora, hora tokyo, hora nueva york, diferencia horaria.
---

# Conversor de Zonas Horarias

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - action: String. Una de: "convert", "now", "meeting"
  - time: String (para "convert"). Hora en formato "HH:MM".
  - from_zone: String (para "convert"). Zona origen (ej: "Europe/Madrid").
  - to_zone: String (para "convert" y "now"). Zona destino.
  - zones: Array de strings (para "meeting"). Lista de zonas para comparar.

### Zonas comunes
- Europe/Madrid, Europe/London, America/New_York, America/Los_Angeles
- America/Mexico_City, America/Bogota, America/Buenos_Aires
- Asia/Tokyo, Asia/Shanghai, Australia/Sydney

### Presentar resultados
- Muestra hora convertida con nombre de ciudad
- Para meeting: muestra hora en todas las zonas
- SIEMPRE responde en espanol
