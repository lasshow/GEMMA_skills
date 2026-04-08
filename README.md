# GEMMA Skills + GemmaBot Agent

Skills personalizados en espanol para **Google AI Edge Gallery** con modelos Gemma 4 (E2B/E4B) on-device + **GemmaBot**: agente IA local controlable via Telegram/WhatsApp que puede controlar tu telefono.

## Dos proyectos, un repositorio

| Parte | Descripcion | Interfaz |
|-------|-------------|----------|
| **A) AI Edge Gallery Skills** | 19 skills JS/Text/Native para Edge Gallery | Chat en Edge Gallery app |
| **B) [GemmaBot Agent](gemmabot/)** | Agente IA completo con control del telefono | Telegram / WhatsApp |

---

## Parte B: GemmaBot Agent (NUEVO)

Agente personal con Gemma 4 que corre en Termux. Controlable via Telegram y/o WhatsApp. Puede: encender linterna, enviar SMS, abrir apps, buscar en internet, tomar notas, y mas. **Todo local y privado.**

```bash
# Instalacion rapida en Termux:
git clone https://github.com/lasshow/GEMMA_skills.git
cd GEMMA_skills/gemmabot
bash scripts/install_termux.sh
bash scripts/start.sh telegram
```

Ver documentacion completa: **[gemmabot/README.md](gemmabot/README.md)**

---

## Parte A: AI Edge Gallery Skills

## Instalacion rapida

En AI Edge Gallery → Agent Skills → (+) → **Load skill from URL** → pega la URL:

> **IMPORTANTE:** Activa maximo 3-4 skills a la vez para evitar errores de memoria.

### Internet y Busqueda
| Skill | URL | Tipo |
|-------|-----|------|
| buscar-web | `https://lasshow.github.io/GEMMA_skills/buscar-web` | JS |
| noticias | `https://lasshow.github.io/GEMMA_skills/noticias` | JS |
| navegar-web | `https://lasshow.github.io/GEMMA_skills/navegar-web` | JS |
| resumir-pagina | `https://lasshow.github.io/GEMMA_skills/resumir-pagina` | JS |

### Comunicacion (via deep links + intents)
| Skill | URL | Tipo |
|-------|-----|------|
| enviar-whatsapp | `https://lasshow.github.io/GEMMA_skills/enviar-whatsapp` | Text |
| enviar-correo | `https://lasshow.github.io/GEMMA_skills/enviar-correo` | Native |
| enviar-sms | `https://lasshow.github.io/GEMMA_skills/enviar-sms` | Native |
| llamar-telefono | `https://lasshow.github.io/GEMMA_skills/llamar-telefono` | Text |
| abrir-enlace | `https://lasshow.github.io/GEMMA_skills/abrir-enlace` | Text |

### Utilidades
| Skill | URL | Tipo |
|-------|-----|------|
| clima | `https://lasshow.github.io/GEMMA_skills/clima` | JS |
| calculadora | `https://lasshow.github.io/GEMMA_skills/calculadora` | JS |
| conversor-unidades | `https://lasshow.github.io/GEMMA_skills/conversor-unidades` | Text |
| generador-contrasenas | `https://lasshow.github.io/GEMMA_skills/generador-contrasenas` | JS |
| ejecutar-python | `https://lasshow.github.io/GEMMA_skills/ejecutar-python` | JS |
| consultar-ip | `https://lasshow.github.io/GEMMA_skills/consultar-ip` | JS |
| temporizador | `https://lasshow.github.io/GEMMA_skills/temporizador` | JS |

### Productividad
| Skill | URL | Tipo |
|-------|-----|------|
| notas-rapidas | `https://lasshow.github.io/GEMMA_skills/notas-rapidas` | JS |
| segundo-cerebro | `https://lasshow.github.io/GEMMA_skills/segundo-cerebro` | Text |
| traductor | `https://lasshow.github.io/GEMMA_skills/traductor` | Text |

**Total: 19 skills** - Todos en espanol, sin API key.

## Tipos de skills

- **JS**: Ejecuta JavaScript en WebView oculto (fetch APIs, calculos, etc.)
- **Text**: Solo instrucciones para el modelo (no requiere JS)
- **Native**: Usa intents nativos de Android (email, SMS)

## Truco de deep links

Los skills de comunicacion (WhatsApp, llamar, abrir enlace) usan un truco descubierto: Edge Gallery renderiza **links Markdown clickeables** que al tocarlos abren la app correspondiente:
- `[Enviar WhatsApp](https://wa.me/34666123456?text=Hola)` → abre WhatsApp
- `[Llamar](tel:+34666123456)` → abre marcador
- `[Abrir Maps](https://maps.google.com/?q=Bilbao)` → abre Google Maps

## Configuraciones recomendadas

**Asistente diario (3 skills):**
buscar-web + enviar-whatsapp + clima

**Productividad (3 skills):**
notas-rapidas + calculadora + traductor

**Comunicacion completa (4 skills):**
enviar-whatsapp + enviar-correo + llamar-telefono + abrir-enlace

## Mobile Actions (FunctionGemma 270M)

Ademas de los Agent Skills, descarga **MobileActions-270M** (276 MB) para:
- Encender/apagar linterna
- Crear contactos
- Abrir Google Maps
- Crear eventos en calendario
- Abrir configuracion WiFi

## Notas tecnicas

- APIs con CORS nativo: DuckDuckGo, Wikipedia, wttr.in, ipapi.co, rss2json.com
- Proxy CORS: corsproxy.io (para paginas arbitrarias)
- Deep links: wa.me, tel:, mailto:, maps.google.com (via Markdown clickeable)
- Almacenamiento local: localStorage para notas-rapidas
- Python: Pyodide (WebAssembly) para ejecutar-python
- Crypto: Web Crypto API para generador-contrasenas

## Links utiles

- [Google AI Edge Gallery - GitHub](https://github.com/google-ai-edge/gallery)
- [Skills de la comunidad](https://github.com/google-ai-edge/gallery/discussions/categories/skills)
- [DuckDuckGo skill (wafwoof)](https://wafwoof.github.io/edge-gallery-duckduckgo/)
- [Google News skill (wafwoof)](https://wafwoof.github.io/edge-gallery-googlenews/)
