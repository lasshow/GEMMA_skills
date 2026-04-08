# Guia de instalacion: GemmaBot Agent

## Paso 1: Instalar Termux

1. Descargar **Termux** desde F-Droid (NO Play Store):
   https://f-droid.org/packages/com.termux/
2. Descargar **Termux:API** desde F-Droid:
   https://f-droid.org/packages/com.termux.api/
3. Dar permisos de bateria sin restricciones a Termux

## Paso 2: Clonar e instalar

```bash
pkg update -y && pkg upgrade -y
pkg install -y git
git clone https://github.com/lasshow/GEMMA_skills.git
cd GEMMA_skills/gemmabot
bash scripts/install_termux.sh
```

## Paso 3: Configurar Telegram

1. Abre Telegram y busca **@BotFather**
2. Envia `/newbot` y sigue las instrucciones
3. Copia el token que te da BotFather
4. Edita `config/config.yaml`:
   ```yaml
   telegram_token: "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
   ```

## Paso 4: Descargar modelo Gemma 4

### Opcion A: Descarga directa (HuggingFace)
```bash
pip install huggingface-hub
huggingface-cli download google/gemma-4-e4b-it-gguf \
    gemma-4-e4b-it-Q4_K_M.gguf \
    --local-dir ~/models
```

### Opcion B: Via Ollama
```bash
pkg install golang
go install github.com/ollama/ollama@latest
ollama pull gemma4:e4b
```

## Paso 5: Arrancar

```bash
bash scripts/start.sh telegram
```

El bot arrancara llama.cpp con el modelo y luego el bot de Telegram.
Abre Telegram y envia `/start` a tu bot.

## Paso 6 (opcional): WhatsApp

### Via Baileys (riesgo de ban):
```bash
npm install  # en directorio gemmabot/
bash scripts/start.sh whatsapp
# Escanea el QR que aparece
```

### Via Tasker (seguro):
Ver `channels/whatsapp_tasker.md` para configuracion paso a paso.

## Paso 7 (opcional): Tasker para acciones avanzadas

1. Instalar **Tasker** (Play Store)
2. Instalar **Tasker MCP Server**: https://github.com/dceluis/tasker-mcp
3. Configurar la URL en `config/config.yaml`:
   ```yaml
   tasker_url: "http://localhost:3000"
   ```

Sin Tasker, GemmaBot usa `termux-api` para acciones basicas (linterna, WiFi, volumen, SMS, notificaciones).

## Solucionar problemas

### "Gemma no responde"
- Verificar que llama.cpp esta corriendo: `curl http://localhost:8080/health`
- Verificar RAM disponible: `free -h`
- Probar con modelo E2B (mas ligero): editar MODEL_FILE en start.sh

### "Bot de Telegram no conecta"
- Verificar token en config.yaml
- Verificar conexion a internet
- Reiniciar: `bash scripts/start.sh telegram`

### "WhatsApp se desconecta"
- Borrar `auth_whatsapp/` y escanear QR de nuevo
- WhatsApp Web solo permite una sesion adicional

### "Termux se cierra en background"
- Desactivar optimizacion de bateria para Termux
- Usar `termux-wake-lock` para mantenerlo activo
