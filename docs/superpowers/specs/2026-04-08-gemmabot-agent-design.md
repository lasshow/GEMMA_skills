# GemmaBot Agent - Spec de Diseno

**Fecha**: 2026-04-08
**Estado**: Aprobado

## Objetivo

Crear un agente IA local que corra Gemma 4 en el movil Android, controlable via WhatsApp y/o Telegram, capaz de ejecutar acciones en el telefono (abrir apps, enviar mensajes, controlar hardware, etc.). Todo offline y privado.

## Arquitectura

### Parte A (existente): AI Edge Gallery Skills
- 19 skills JS/Text/Native para Google AI Edge Gallery
- Sin cambios. Se mantienen tal cual.

### Parte B (nuevo): GemmaBot Agent
- Bot Python/Node.js corriendo en Termux
- Gemma 4 E4B/E2B via llama.cpp server (localhost:8080)
- Interfaces: Telegram (python-telegram-bot) y WhatsApp (Baileys)
- Control del telefono via Tasker MCP

### Flujo
```
Usuario (Telegram/WhatsApp)
    -> Bot (Termux)
    -> Gemma 4 (llama.cpp local)
    -> Tool calls JSON
    -> Tasker MCP -> Acciones Android
    -> Respuesta al usuario
```

## Componentes

### core/gemma_client.py
- Cliente HTTP para llama.cpp server
- Envio de prompts con system prompt + tools
- Parsing de respuestas con tool calls

### core/tool_router.py
- Recibe tool calls JSON de Gemma
- Enruta a la accion correspondiente (tasker, weather, search, notes)
- Devuelve resultados consolidados

### core/system_prompt.txt
- Prompt del sistema en espanol
- Define persona del agente
- Lista tools disponibles con esquema JSON

### channels/telegram_bot.py
- Bot Telegram con python-telegram-bot
- Recibe mensajes -> gemma_client -> responde

### channels/whatsapp_baileys.js
- Bot WhatsApp con Baileys (Node.js)
- Conecta via QR como WhatsApp Web
- HTTP bridge a gemma_client Python

### actions/tasker_mcp.py
- Cliente para Tasker MCP Server
- Acciones: abrir app, SMS, linterna, WiFi, BT, volumen, brillo, screenshot, shell

### actions/weather.py
- API wttr.in (CORS nativo, sin API key)

### actions/search.py
- DuckDuckGo API + Wikipedia

### actions/notes.py
- CRUD notas con SQLite local

### config/config.example.yaml
- Tokens (Telegram), puertos, modelo Gemma, acciones habilitadas

### config/actions.yaml
- Catalogo de acciones con nombre, descripcion, parametros JSON schema

### scripts/install_termux.sh
- Instalacion automatica: Python, Node.js, llama.cpp, dependencias

### scripts/start.sh
- Arranca llama.cpp + bot en un solo comando

## Stack Tecnico
- Python 3.11+ (core, Telegram, acciones)
- Node.js 18+ (solo WhatsApp Baileys, opcional)
- llama.cpp (Gemma 4 E4B/E2B)
- Tasker + Tasker MCP Server (control Android)
- SQLite (notas)
- YAML (config)

## Riesgos
- WhatsApp via Baileys: riesgo de ban (alternativa: Tasker+AutoNotification)
- Gemma E2B puede ser limitado para tool calling complejo (E4B recomendado)
- Tasker MCP requiere Tasker premium ($3.49)
- KV cache en contextos largos puede agotar RAM
