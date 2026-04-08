---
name: noticias
description: SOLO para titulares de prensa RSS de Google News. Usa UNICAMENTE cuando el usuario diga exactamente la palabra "noticias" o "titulares". NO usar para busquedas generales de informacion.
---

# Titulares de Google News RSS

## Instrucciones

IMPORTANTE: Este skill es SOLO para obtener titulares de noticias de Google News.
NO lo uses para buscar informacion general - para eso existe buscar-web.

Solo activa este skill cuando el usuario diga EXACTAMENTE:
- "dame las noticias"
- "titulares de hoy"
- "noticias de [tema]"

### Como obtener titulares
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - topic: String. Tema de las noticias. Usa "" (vacio) para noticias generales.
  - lang: String. "es" para espanol, "en" para ingles.
  - country: String. "ES" para Espana, "MX" para Mexico, "AR" para Argentina.

### Presentar resultados
- Muestra los titulares como lista numerada con fuente y enlace
- SIEMPRE responde en espanol
- Indica la fecha si esta disponible
- NO llames a buscar-web despues de este skill. Los titulares son suficientes.
