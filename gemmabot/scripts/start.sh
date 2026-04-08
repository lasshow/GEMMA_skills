#!/bin/bash
# ============================================
# GemmaBot - Script de arranque
# ============================================
# Ejecutar: bash start.sh [telegram|whatsapp|ambos]
# ============================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BOT_DIR="$(dirname "$SCRIPT_DIR")"
MODEL_DIR="$HOME/models"
LLAMA_CPP="$HOME/llama.cpp/build/bin/llama-server"

# Modelo por defecto
MODEL_FILE="${MODEL_DIR}/gemma-4-e4b-it-Q4_K_M.gguf"
PORT=8080

echo "=========================================="
echo "  GemmaBot - Iniciando"
echo "=========================================="

# Verificar modelo
if [ ! -f "$MODEL_FILE" ]; then
    echo "ERROR: Modelo no encontrado en $MODEL_FILE"
    echo "Descarga primero: bash scripts/install_termux.sh"
    exit 1
fi

# Verificar llama.cpp
if [ ! -f "$LLAMA_CPP" ]; then
    echo "ERROR: llama.cpp no compilado"
    echo "Ejecuta: bash scripts/install_termux.sh"
    exit 1
fi

# Arrancar llama.cpp server en background
echo "[1/2] Arrancando Gemma 4..."
$LLAMA_CPP \
    -m "$MODEL_FILE" \
    --host 0.0.0.0 \
    --port $PORT \
    -c 4096 \
    -ngl 99 \
    --threads $(nproc) &

LLAMA_PID=$!
echo "  llama.cpp PID: $LLAMA_PID (puerto $PORT)"

# Esperar a que el servidor este listo
echo "  Esperando a que el modelo cargue..."
for i in $(seq 1 60); do
    if curl -s "http://localhost:$PORT/health" > /dev/null 2>&1; then
        echo "  Gemma 4 listo!"
        break
    fi
    sleep 2
done

# Determinar canal
CHANNEL="${1:-telegram}"

echo "[2/2] Arrancando bot ($CHANNEL)..."
cd "$BOT_DIR"

case "$CHANNEL" in
    telegram)
        python channels/telegram_bot.py
        ;;
    whatsapp)
        node channels/whatsapp_baileys.js
        ;;
    ambos)
        python channels/telegram_bot.py &
        TELEGRAM_PID=$!
        node channels/whatsapp_baileys.js &
        WHATSAPP_PID=$!
        echo "Telegram PID: $TELEGRAM_PID"
        echo "WhatsApp PID: $WHATSAPP_PID"
        echo "Presiona Ctrl+C para detener todo."
        wait
        ;;
    *)
        echo "Uso: bash start.sh [telegram|whatsapp|ambos]"
        kill $LLAMA_PID 2>/dev/null
        exit 1
        ;;
esac

# Limpiar al salir
trap "kill $LLAMA_PID 2>/dev/null; echo 'GemmaBot detenido.'" EXIT
