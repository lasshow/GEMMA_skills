# GemmaBot - Agente IA Local para Android

Agente personal inteligente con **Gemma 4** que corre 100% en tu telefono. Controlable via **Telegram** y/o **WhatsApp**. Puede controlar tu telefono: abrir apps, enviar SMS, encender linterna, ajustar volumen, buscar en internet, y mucho mas.

**Todo local. Todo privado. Sin nube.**

## Arquitectura

```
Tu (Telegram/WhatsApp)
    |
    v
Bot Python/Node.js (Termux)
    |
    v
Gemma 4 E4B (llama.cpp, localhost:8080)
    |
    v
Tool Router --> Tasker MCP --> Android (apps, hardware, sistema)
           --> wttr.in (clima)
           --> DuckDuckGo/Wikipedia (busqueda)
           --> SQLite (notas)
```

## Requisitos

### Hardware
- Android 10+ con 6GB+ RAM (para E4B) o 3GB+ (para E2B)
- ~4GB almacenamiento para el modelo

### Apps necesarias
- **Termux** (F-Droid, NO Play Store)
- **Termux:API** (F-Droid) - para control de hardware
- **Tasker** (Play Store, $3.49) - opcional, para acciones avanzadas
- **Tasker MCP Server** - opcional, puente LLM-Tasker

## Instalacion rapida

```bash
# En Termux:
git clone https://github.com/lasshow/GEMMA_skills.git
cd GEMMA_skills/gemmabot
bash scripts/install_termux.sh
```

## Configuracion

```bash
# Editar config
cp config/config.example.yaml config/config.yaml
nano config/config.yaml
# -> Pega tu token de Telegram (de @BotFather)
# -> Configura numeros autorizados
```

## Uso

```bash
# Solo Telegram
bash scripts/start.sh telegram

# Solo WhatsApp
bash scripts/start.sh whatsapp

# Ambos
bash scripts/start.sh ambos
```

## Acciones disponibles

| Accion | Ejemplo | Requiere |
|--------|---------|----------|
| Linterna | "enciende la linterna" | termux-api |
| WiFi | "apaga el wifi" | termux-api |
| Volumen | "sube el volumen al 10" | termux-api |
| SMS | "manda SMS a mama: llego tarde" | termux-api |
| Abrir app | "abre YouTube" | Tasker |
| Screenshot | "toma una captura" | Tasker |
| Alarma | "pon alarma a las 7:00" | Tasker |
| Calendario | "agenda reunion manana a las 10" | Tasker |
| Clima | "que clima hace en Madrid?" | internet |
| Buscar | "busca receta de tortilla" | internet |
| Notas | "apunta: comprar leche" | local |
| Shell | "ejecuta: ls -la" | termux |

## Canales de mensajeria

### Telegram (recomendado)
- Sin riesgo de ban
- API oficial con @BotFather
- Comandos: /start, /help, /clear, /status

### WhatsApp - Baileys (avanzado)
- Conecta via QR como WhatsApp Web
- **RIESGO**: posible ban de cuenta
- Requiere Node.js

### WhatsApp - Tasker (seguro)
- Via AutoNotification + Tasker
- Sin riesgo de ban
- Solo responde a notificaciones
- Ver: `channels/whatsapp_tasker.md`

## Seguridad

- Lista blanca de usuarios/numeros autorizados
- Comandos shell peligrosos bloqueados
- Todo corre localmente, sin enviar datos a servidores externos
- El modelo Gemma 4 procesa todo on-device
