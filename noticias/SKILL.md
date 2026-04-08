---
name: noticias
description: Muestra las noticias mas recientes de Google News. Busca noticias por tema o muestra las principales del dia. Triggers - noticias, news, que paso hoy, ultimas noticias, actualidad, noticias de, titulares.
---

# Noticias en tiempo real

## Instrucciones

Cuando el usuario quiera ver noticias actuales o buscar noticias sobre un tema:

### Como buscar noticias
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - topic: String. Tema de las noticias. Usa "" (vacio) para noticias generales del dia.
  - lang: String. "es" para espanol, "en" para ingles.
  - country: String. "ES" para Espana, "MX" para Mexico, "AR" para Argentina, "US" para EEUU.

### Presentar resultados
- Muestra las noticias como lista con titulo, fuente y enlace
- Si el usuario pregunta sobre un tema concreto, destaca las noticias mas relevantes
- SIEMPRE responde en espanol
- Indica la fecha/hora de publicacion si esta disponible
