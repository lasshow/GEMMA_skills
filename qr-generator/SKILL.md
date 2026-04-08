---
name: qr-generator
description: Genera codigos QR a partir de texto, URLs, contactos o WiFi. Muestra el QR directamente en el chat. Triggers - qr, codigo qr, genera qr, qr code, crear qr, qr wifi, qr contacto, qr url.
---

# Generador de Codigos QR

## Instrucciones

Cuando el usuario quiera generar un codigo QR:

### Como generar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - text: String. El contenido del QR.
  - type: String. Tipo: "text" (por defecto), "url", "wifi", "contact".

Para WiFi, el text debe tener formato: "SSID|password|WPA"
Para contacto: "nombre|telefono|email"

### Presentar resultados
- Muestra el QR generado
- Indica que contenido tiene el QR
- SIEMPRE responde en espanol
