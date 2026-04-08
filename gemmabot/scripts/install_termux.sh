#!/bin/bash
# ============================================
# GemmaBot - Instalacion automatica en Termux
# ============================================
# Ejecutar: bash install_termux.sh
# ============================================

set -e

echo "=========================================="
echo "  GemmaBot - Instalador para Termux"
echo "=========================================="
echo ""

# 1. Actualizar paquetes
echo "[1/7] Actualizando paquetes..."
pkg update -y && pkg upgrade -y

# 2. Instalar dependencias del sistema
echo "[2/7] Instalando dependencias del sistema..."
pkg install -y python git cmake make clang nodejs-lts termux-api

# 3. Instalar termux-api (para control de hardware sin Tasker)
echo "[3/7] Verificando termux-api..."
if ! command -v termux-torch &> /dev/null; then
    echo "AVISO: Instala la app Termux:API desde F-Droid para control de hardware"
    echo "https://f-droid.org/packages/com.termux.api/"
fi

# 4. Instalar dependencias Python
echo "[4/7] Instalando dependencias Python..."
pip install -r requirements.txt

# 5. Compilar llama.cpp para Gemma 4
echo "[5/7] Compilando llama.cpp..."
if [ ! -d "$HOME/llama.cpp" ]; then
    git clone https://github.com/ggerganov/llama.cpp.git "$HOME/llama.cpp"
fi
cd "$HOME/llama.cpp"
git pull
cmake -B build
cmake --build build --config Release -j$(nproc)
cd -

# 6. Descargar modelo Gemma 4
echo "[6/7] Descargando modelo Gemma 4 E4B..."
MODEL_DIR="$HOME/models"
mkdir -p "$MODEL_DIR"
if [ ! -f "$MODEL_DIR/gemma-4-e4b-it.gguf" ]; then
    echo "Descargando Gemma 4 E4B (Q4_K_M)..."
    echo "NOTA: Necesitas cuenta en HuggingFace y aceptar la licencia de Gemma"
    echo "Visita: https://huggingface.co/google/gemma-4-e4b-it-gguf"
    echo ""
    echo "Descarga manual:"
    echo "  huggingface-cli download google/gemma-4-e4b-it-gguf gemma-4-e4b-it-Q4_K_M.gguf --local-dir $MODEL_DIR"
    echo ""
    echo "O usa ollama:"
    echo "  ollama pull gemma4:e4b"
else
    echo "Modelo ya descargado."
fi

# 7. Configuracion
echo "[7/7] Configuracion..."
CONFIG_DIR="$(dirname "$0")/../config"
if [ ! -f "$CONFIG_DIR/config.yaml" ]; then
    cp "$CONFIG_DIR/config.example.yaml" "$CONFIG_DIR/config.yaml"
    echo "Archivo config.yaml creado. Editalo con tus tokens:"
    echo "  nano $CONFIG_DIR/config.yaml"
fi

# Instalar dependencias Node.js (opcional, para WhatsApp)
echo ""
echo "=== OPCIONAL: WhatsApp con Baileys ==="
read -p "Instalar soporte WhatsApp? (s/n): " install_wa
if [ "$install_wa" = "s" ]; then
    cd "$(dirname "$0")/.."
    npm install
    echo "WhatsApp instalado. Ejecuta: npm run whatsapp"
    cd -
fi

echo ""
echo "=========================================="
echo "  Instalacion completada!"
echo "=========================================="
echo ""
echo "Pasos siguientes:"
echo "1. Edita config/config.yaml con tu token de Telegram"
echo "2. Descarga el modelo Gemma 4 (ver instrucciones arriba)"
echo "3. Ejecuta: bash scripts/start.sh"
echo ""
echo "Para Telegram: crea un bot con @BotFather"
echo "Para WhatsApp: ejecuta npm run whatsapp y escanea QR"
echo ""
