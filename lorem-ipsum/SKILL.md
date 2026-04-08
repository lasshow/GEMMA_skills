---
name: lorem-ipsum
description: Genera texto de relleno Lorem Ipsum y variantes en espanol. Para diseno y maquetacion. Triggers - lorem ipsum, texto de relleno, placeholder text, texto de prueba, parrafo de ejemplo, generar texto.
---

# Generador de Texto de Relleno

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - type: String. "paragraphs", "sentences", "words". Por defecto "paragraphs".
  - count: Number. Cantidad a generar. Por defecto 3.
  - lang: String. "latin" (lorem ipsum clasico) o "es" (espanol). Por defecto "latin".

### Presentar resultados
- Muestra el texto generado listo para copiar
- SIEMPRE responde en espanol
