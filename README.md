# GEMMA Skills + GemmaBot Agent

Skills personalizados en espanol para **Google AI Edge Gallery** con modelos Gemma 4 (E2B/E4B) on-device + **GemmaBot**: agente IA local controlable via Telegram/WhatsApp que puede controlar tu telefono.

## Dos proyectos, un repositorio

| Parte | Descripcion | Interfaz |
|-------|-------------|----------|
| **A) AI Edge Gallery Skills** | 33 skills JS/Text/Native para Edge Gallery | Chat en Edge Gallery app |
| **B) [GemmaBot Agent](gemmabot/)** | Agente IA completo con control del telefono | Telegram / WhatsApp |

---

## Parte B: GemmaBot Agent

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

En AI Edge Gallery → Agent Skills → (+) → **Load skill from URL** → pega la URL.

> **IMPORTANTE:** Activa maximo 3-4 skills a la vez para evitar errores de memoria.

---

### Internet y Busqueda

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| Buscar Web | `https://lasshow.github.io/GEMMA_skills/buscar-web` | JS |
| Noticias | `https://lasshow.github.io/GEMMA_skills/noticias` | JS |
| Navegar Web | `https://lasshow.github.io/GEMMA_skills/navegar-web` | JS |
| Resumir Pagina | `https://lasshow.github.io/GEMMA_skills/resumir-pagina` | JS |

### Comunicacion

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| Enviar WhatsApp | `https://lasshow.github.io/GEMMA_skills/enviar-whatsapp` | Text |
| Enviar Correo | `https://lasshow.github.io/GEMMA_skills/enviar-correo` | Native |
| Enviar SMS | `https://lasshow.github.io/GEMMA_skills/enviar-sms` | Native |
| Llamar Telefono | `https://lasshow.github.io/GEMMA_skills/llamar-telefono` | Text |
| Abrir Enlace | `https://lasshow.github.io/GEMMA_skills/abrir-enlace` | Text |

### Utilidades

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| Clima | `https://lasshow.github.io/GEMMA_skills/clima` | JS |
| Calculadora | `https://lasshow.github.io/GEMMA_skills/calculadora` | JS |
| Conversor Unidades | `https://lasshow.github.io/GEMMA_skills/conversor-unidades` | Text |
| Generador Contrasenas | `https://lasshow.github.io/GEMMA_skills/generador-contrasenas` | JS |
| Ejecutar Python | `https://lasshow.github.io/GEMMA_skills/ejecutar-python` | JS |
| Consultar IP | `https://lasshow.github.io/GEMMA_skills/consultar-ip` | JS |
| Temporizador | `https://lasshow.github.io/GEMMA_skills/temporizador` | JS |

### Productividad

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| Notas Rapidas | `https://lasshow.github.io/GEMMA_skills/notas-rapidas` | JS |
| Segundo Cerebro | `https://lasshow.github.io/GEMMA_skills/segundo-cerebro` | Text |
| Traductor | `https://lasshow.github.io/GEMMA_skills/traductor` | Text |
| Pomodoro | `https://lasshow.github.io/GEMMA_skills/pomodoro` | JS |
| Cuenta Atras | `https://lasshow.github.io/GEMMA_skills/cuenta-atras` | JS |

### Generadores y Aleatorio

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| Generador QR | `https://lasshow.github.io/GEMMA_skills/qr-generator` | JS |
| Dados y Aleatorio | `https://lasshow.github.io/GEMMA_skills/dice-random` | JS |
| Lorem Ipsum | `https://lasshow.github.io/GEMMA_skills/lorem-ipsum` | JS |
| Hash Generator | `https://lasshow.github.io/GEMMA_skills/hash-generator` | JS |

### Desarrollo

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| JSON Formatter | `https://lasshow.github.io/GEMMA_skills/json-formatter` | JS |
| Base64 Tools | `https://lasshow.github.io/GEMMA_skills/base64-tools` | JS |
| Regex Tester | `https://lasshow.github.io/GEMMA_skills/regex-tester` | JS |
| Color Picker | `https://lasshow.github.io/GEMMA_skills/color-picker` | JS |

### Finanzas y Conversiones

| Skill | Copiar URL | Tipo |
|-------|-----------|------|
| Conversor Divisas | `https://lasshow.github.io/GEMMA_skills/conversor-divisas` | JS |
| Calculadora Propinas | `https://lasshow.github.io/GEMMA_skills/tip-calculator` | JS |
| Calculadora IMC | `https://lasshow.github.io/GEMMA_skills/bmi-calculator` | JS |
| Zonas Horarias | `https://lasshow.github.io/GEMMA_skills/timezone-converter` | JS |

---

**Total: 33 skills** - Todos en espanol, sin API key.

## Copiar rapido (URLs listas para pegar)

```
https://lasshow.github.io/GEMMA_skills/buscar-web
https://lasshow.github.io/GEMMA_skills/noticias
https://lasshow.github.io/GEMMA_skills/navegar-web
https://lasshow.github.io/GEMMA_skills/resumir-pagina
https://lasshow.github.io/GEMMA_skills/enviar-whatsapp
https://lasshow.github.io/GEMMA_skills/enviar-correo
https://lasshow.github.io/GEMMA_skills/enviar-sms
https://lasshow.github.io/GEMMA_skills/llamar-telefono
https://lasshow.github.io/GEMMA_skills/abrir-enlace
https://lasshow.github.io/GEMMA_skills/clima
https://lasshow.github.io/GEMMA_skills/calculadora
https://lasshow.github.io/GEMMA_skills/conversor-unidades
https://lasshow.github.io/GEMMA_skills/generador-contrasenas
https://lasshow.github.io/GEMMA_skills/ejecutar-python
https://lasshow.github.io/GEMMA_skills/consultar-ip
https://lasshow.github.io/GEMMA_skills/temporizador
https://lasshow.github.io/GEMMA_skills/notas-rapidas
https://lasshow.github.io/GEMMA_skills/segundo-cerebro
https://lasshow.github.io/GEMMA_skills/traductor
https://lasshow.github.io/GEMMA_skills/pomodoro
https://lasshow.github.io/GEMMA_skills/cuenta-atras
https://lasshow.github.io/GEMMA_skills/qr-generator
https://lasshow.github.io/GEMMA_skills/dice-random
https://lasshow.github.io/GEMMA_skills/lorem-ipsum
https://lasshow.github.io/GEMMA_skills/hash-generator
https://lasshow.github.io/GEMMA_skills/json-formatter
https://lasshow.github.io/GEMMA_skills/base64-tools
https://lasshow.github.io/GEMMA_skills/regex-tester
https://lasshow.github.io/GEMMA_skills/color-picker
https://lasshow.github.io/GEMMA_skills/conversor-divisas
https://lasshow.github.io/GEMMA_skills/tip-calculator
https://lasshow.github.io/GEMMA_skills/bmi-calculator
https://lasshow.github.io/GEMMA_skills/timezone-converter
```

## Configuraciones recomendadas

**Asistente diario (3 skills):**
buscar-web + clima + notas-rapidas

**Productividad (4 skills):**
pomodoro + notas-rapidas + cuenta-atras + traductor

**Comunicacion completa (4 skills):**
enviar-whatsapp + enviar-correo + llamar-telefono + abrir-enlace

**Developer tools (4 skills):**
json-formatter + regex-tester + base64-tools + ejecutar-python

**Viajero (3 skills):**
conversor-divisas + timezone-converter + traductor

**Salud y finanzas (3 skills):**
bmi-calculator + tip-calculator + calculadora

## Tipos de skills

- **JS**: Ejecuta JavaScript en WebView oculto (fetch APIs, calculos, etc.)
- **Text**: Solo instrucciones para el modelo (no requiere JS)
- **Native**: Usa intents nativos de Android (email, SMS)

## Truco de deep links

Los skills de comunicacion usan un truco descubierto: Edge Gallery renderiza **links Markdown clickeables** que al tocarlos abren la app correspondiente:
- `[Enviar WhatsApp](https://wa.me/34666123456?text=Hola)` → abre WhatsApp
- `[Llamar](tel:+34666123456)` → abre marcador
- `[Abrir Maps](https://maps.google.com/?q=Bilbao)` → abre Google Maps

## Mobile Actions (FunctionGemma 270M)

Ademas de los Agent Skills, descarga **MobileActions-270M** (276 MB) para:
- Encender/apagar linterna
- Crear contactos
- Abrir Google Maps
- Crear eventos en calendario
- Abrir configuracion WiFi

## Notas tecnicas

- APIs con CORS nativo: DuckDuckGo, Wikipedia, wttr.in, ipapi.co, rss2json.com, frankfurter.app, qrserver.com
- Proxy CORS: corsproxy.io (para paginas arbitrarias)
- Deep links: wa.me, tel:, mailto:, maps.google.com (via Markdown clickeable)
- Almacenamiento local: localStorage para notas-rapidas, pomodoro
- Python: Pyodide (WebAssembly) para ejecutar-python
- Crypto: Web Crypto API para generador-contrasenas y hash-generator
- Colores: conversion HEX/RGB/HSL nativa en color-picker
- Divisas: API Banco Central Europeo (frankfurter.app) para conversor-divisas

## Links utiles

- [Google AI Edge Gallery - GitHub](https://github.com/google-ai-edge/gallery)
- [Skills de la comunidad](https://github.com/google-ai-edge/gallery/discussions/categories/skills)
- [DuckDuckGo skill (wafwoof)](https://wafwoof.github.io/edge-gallery-duckduckgo/)
- [Google News skill (wafwoof)](https://wafwoof.github.io/edge-gallery-googlenews/)
- [Tasker MCP Server](https://github.com/dceluis/tasker-mcp)
- [OpenClaw](https://github.com/openclaw/openclaw)
