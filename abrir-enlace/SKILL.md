---
name: abrir-enlace
description: Abre cualquier URL en el navegador externo del telefono, abre Google Maps, YouTube, o cualquier app mediante enlaces clickeables. Triggers - abre en el navegador, abrir url, abrir pagina en chrome, ir a, open link, abrir mapa, abrir youtube.
---

# Abrir Enlaces Externos

## Instrucciones

Cuando el usuario quiera abrir una pagina web, app o ubicacion en su telefono, genera un enlace Markdown clickeable que se abrira en la app correspondiente.

### Formato OBLIGATORIO
SIEMPRE genera el enlace en este formato Markdown exacto:

**Toca para abrir:**
[Texto descriptivo](URL_COMPLETA)

### Tipos de enlaces soportados

**Paginas web (abre en Chrome/navegador):**
[Abrir Google](https://www.google.com)
[Abrir Wikipedia](https://es.wikipedia.org)

**Google Maps (abre en Maps):**
[Ver en Google Maps](https://maps.google.com/?q=Bilbao+Espana)
[Buscar restaurantes cerca](https://maps.google.com/?q=restaurantes+cerca+de+mi)

**YouTube (abre en YouTube):**
[Buscar en YouTube](https://www.youtube.com/results?search_query=TERMINO)

**Google Search (abre busqueda en Chrome):**
[Buscar en Google](https://www.google.com/search?q=TERMINO)

**Email (abre Gmail):**
[Enviar email](mailto:ejemplo@gmail.com?subject=Asunto&body=Mensaje)

**Telefono (abre marcador):**
[Llamar](tel:+34666123456)

### Reglas
- SIEMPRE usa formato Markdown: [texto](url)
- SIEMPRE agrega https:// si falta
- Si el usuario dice "abre YouTube", genera enlace a youtube.com
- Si dice "busca X en Google", genera enlace de busqueda Google
- Si dice "como llegar a X", genera enlace de Google Maps
- Responde brevemente en espanol y luego pon el enlace
- Puedes generar MULTIPLES enlaces si es util
