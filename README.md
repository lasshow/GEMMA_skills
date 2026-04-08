# GEMMA Skills - Google AI Edge Gallery

Skills personalizados en español para **Google AI Edge Gallery** con modelos Gemma 4 (E2B/E4B) on-device.

## Instalacion rapida (via URL)

En AI Edge Gallery → Agent Skills → (+) → **Load skill from URL** → pega la URL:

| Skill | URL | API Key |
|-------|-----|---------|
| buscar-web | `https://lasshow.github.io/GEMMA_skills/buscar-web` | No |
| noticias | `https://lasshow.github.io/GEMMA_skills/noticias` | No |
| clima | `https://lasshow.github.io/GEMMA_skills/clima` | No |
| navegar-web | `https://lasshow.github.io/GEMMA_skills/navegar-web` | No |
| resumir-pagina | `https://lasshow.github.io/GEMMA_skills/resumir-pagina` | No |
| calculadora | `https://lasshow.github.io/GEMMA_skills/calculadora` | No |
| ejecutar-python | `https://lasshow.github.io/GEMMA_skills/ejecutar-python` | No |
| consultar-ip | `https://lasshow.github.io/GEMMA_skills/consultar-ip` | No |
| traductor | `https://lasshow.github.io/GEMMA_skills/traductor` | No |
| enviar-correo | `https://lasshow.github.io/GEMMA_skills/enviar-correo` | No |
| enviar-sms | `https://lasshow.github.io/GEMMA_skills/enviar-sms` | No |

## Skills incluidos

### Busqueda e Internet
| Skill | Tipo | Descripcion |
|-------|------|-------------|
| **buscar-web** | JS | Busca en DuckDuckGo + Wikipedia + DuckDuckGo HTML (via corsproxy.io) |
| **noticias** | JS | Titulares de Google News RSS via rss2json.com |
| **navegar-web** | JS | Lee contenido de cualquier pagina web via proxy CORS |
| **resumir-pagina** | JS | Extrae y resume texto de cualquier URL |

### Utilidades
| Skill | Tipo | Descripcion |
|-------|------|-------------|
| **clima** | JS | Clima actual y pronostico via wttr.in (sin API key) |
| **calculadora** | JS | Calcula expresiones matematicas con precision |
| **ejecutar-python** | JS | Ejecuta codigo Python en el telefono via Pyodide (WebAssembly) |
| **consultar-ip** | JS | Muestra tu IP publica y ubicacion |
| **traductor** | Text-Only | Traductor multilingue (usa las capacidades del modelo) |

### Comunicacion
| Skill | Tipo | Descripcion |
|-------|------|-------------|
| **enviar-correo** | Native | Redacta y envia emails via Gmail |
| **enviar-sms** | Native | Envia mensajes SMS |

## IMPORTANTE: Maximo 3-4 skills activos

Los modelos E2B/E4B tienen contexto limitado. Activa solo los skills que necesites en cada momento.

**Configuracion recomendada para uso diario:**
- buscar-web + clima + enviar-correo (3 skills)

## Mobile Actions (control del telefono)

Ademas de los Agent Skills, Edge Gallery soporta **Mobile Actions** con el modelo FunctionGemma 270M (276 MB):

| Accion | Comando de ejemplo |
|--------|-------------------|
| Linterna ON/OFF | "Enciende la linterna" |
| Crear contacto | "Crea un contacto Juan Garcia 666123456" |
| Enviar email | "Envia email a test@mail.com" |
| Abrir mapa | "Muestra Bilbao en el mapa" |
| WiFi settings | "Abre configuracion WiFi" |
| Evento calendario | "Crea evento manana a las 15:00 reunion" |

Para usarlo: descarga MobileActions-270M desde la app (seccion Mobile Actions).

## Skills de la comunidad recomendados (sin API key)

| Skill | URL para cargar | Autor |
|-------|----------------|-------|
| DuckDuckGo | `https://wafwoof.github.io/edge-gallery-duckduckgo/` | @wafwoof |
| Google News | `https://wafwoof.github.io/edge-gallery-googlenews/` | @wafwoof |

Mas skills en: [GitHub Discussions - Skills](https://github.com/google-ai-edge/gallery/discussions/categories/skills)

## Notas tecnicas

- Skills JS usan APIs con CORS nativo (DuckDuckGo, Wikipedia, wttr.in, ipapi.co, rss2json)
- Para leer paginas arbitrarias se usa corsproxy.io como proxy CORS
- GitHub Pages sirve los archivos con MIME types correctos (.nojekyll incluido)
- Skills nativos usan `run_intent` (solo send_email y send_sms soportados)
