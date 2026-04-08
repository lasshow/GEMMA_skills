"""
Bot de Telegram para GemmaBot.
Recibe mensajes, los procesa con Gemma 4 y responde.
"""

import asyncio
import logging
import yaml
from pathlib import Path
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Importar desde el directorio padre
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.gemma_client import GemmaClient
from core.tool_router import ToolRouter

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def load_config() -> dict:
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    if config_path.exists():
        return yaml.safe_load(config_path.read_text(encoding="utf-8"))
    return {}


config = load_config()
gemma = GemmaClient(config.get("gemma_url", "http://localhost:8080"))
router = ToolRouter(config)

# IDs de usuarios autorizados (seguridad)
ALLOWED_USERS: set[int] = set(config.get("telegram_allowed_users", []))


def is_authorized(user_id: int) -> bool:
    if not ALLOWED_USERS:
        return True  # Si no hay lista, permitir todos
    return user_id in ALLOWED_USERS


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola! Soy GemmaBot, tu asistente personal con IA local.\n\n"
        "Puedo:\n"
        "- Controlar tu telefono (linterna, WiFi, apps...)\n"
        "- Buscar en internet\n"
        "- Consultar el clima\n"
        "- Guardar notas\n"
        "- Y mucho mas!\n\n"
        "Todo corre localmente en tu telefono. Privado y offline.\n"
        "Escribe /help para ver comandos."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Comandos:\n"
        "/start - Iniciar\n"
        "/help - Esta ayuda\n"
        "/clear - Limpiar historial de conversacion\n"
        "/status - Ver estado del sistema\n\n"
        "O simplemente escribe lo que necesites!"
    )


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gemma.clear_history()
    await update.message.reply_text("Historial limpiado.")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        import httpx
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{gemma.base_url}/health")
            gemma_status = "Online" if resp.status_code == 200 else "Offline"
    except Exception:
        gemma_status = "Offline"

    await update.message.reply_text(
        f"Estado del sistema:\n"
        f"- Gemma 4: {gemma_status}\n"
        f"- Historial: {len(gemma.history)} mensajes\n"
        f"- URL modelo: {gemma.base_url}"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_authorized(update.effective_user.id):
        await update.message.reply_text("No autorizado.")
        return

    user_text = update.message.text
    if not user_text:
        return

    # Indicador de "escribiendo..."
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action="typing"
    )

    try:
        response = await gemma.chat(user_text)

        # Si hay tool calls, ejecutarlas
        if response["tool_calls"]:
            tool_results = await router.execute(response["tool_calls"])

            # Enviar resultados de tools a Gemma para respuesta final
            final = await gemma.chat(
                f"Resultados de las herramientas:\n{tool_results}\n\n"
                f"Resume los resultados para el usuario de forma clara y concisa."
            )
            reply = final["text"] or tool_results
        else:
            reply = response["text"]

        # Telegram tiene limite de 4096 chars
        if len(reply) > 4000:
            for i in range(0, len(reply), 4000):
                await update.message.reply_text(reply[i:i + 4000])
        else:
            await update.message.reply_text(reply)

    except Exception as e:
        logger.error(f"Error procesando mensaje: {e}")
        await update.message.reply_text(
            f"Error procesando tu mensaje. Verifica que Gemma este corriendo.\n"
            f"Detalle: {str(e)[:200]}"
        )


def main():
    token = config.get("telegram_token", "")
    if not token:
        print("ERROR: Configura telegram_token en config/config.yaml")
        print("Crea un bot con @BotFather en Telegram y pega el token.")
        return

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("GemmaBot Telegram iniciado. Esperando mensajes...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
