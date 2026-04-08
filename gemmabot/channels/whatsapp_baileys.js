/**
 * Bot de WhatsApp para GemmaBot usando Baileys.
 * Conecta via QR como WhatsApp Web.
 * Envia mensajes a Gemma 4 via HTTP y responde.
 *
 * AVISO: Usar Baileys puede resultar en ban de cuenta.
 * Alternativa segura: Tasker + AutoNotification (ver whatsapp_tasker.md)
 */

const {
  default: makeWASocket,
  useMultiFileAuthState,
  DisconnectReason,
} = require("@whiskeysockets/baileys");
const { Boom } = require("@hapi/boom");
const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

// Cargar config
const configPath = path.join(__dirname, "..", "config", "config.yaml");
let config = {};
if (fs.existsSync(configPath)) {
  config = yaml.load(fs.readFileSync(configPath, "utf8")) || {};
}

const GEMMA_URL = config.gemma_url || "http://localhost:8080";
const ALLOWED_NUMBERS = new Set(config.whatsapp_allowed_numbers || []);

function isAuthorized(jid) {
  if (ALLOWED_NUMBERS.size === 0) return true;
  const number = jid.split("@")[0];
  return ALLOWED_NUMBERS.has(number);
}

async function chatWithGemma(message) {
  const payload = {
    messages: [
      {
        role: "system",
        content: fs.readFileSync(
          path.join(__dirname, "..", "core", "system_prompt.txt"),
          "utf8"
        ),
      },
      { role: "user", content: message },
    ],
    temperature: 0.7,
    max_tokens: 2048,
    stream: false,
  };

  const resp = await fetch(`${GEMMA_URL}/v1/chat/completions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!resp.ok) throw new Error(`Gemma error: ${resp.status}`);
  const data = await resp.json();
  return data.choices[0].message.content;
}

async function executeToolCalls(content) {
  // Intentar parsear tool calls del contenido
  try {
    let parsed;
    if (content.includes("```json")) {
      const start = content.indexOf("```json") + 7;
      const end = content.indexOf("```", start);
      parsed = JSON.parse(content.substring(start, end).trim());
    } else {
      parsed = JSON.parse(content);
    }

    if (parsed.tool_calls) {
      // Enviar a tool_router via HTTP bridge
      const resp = await fetch("http://localhost:8081/tools", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ tool_calls: parsed.tool_calls }),
      });
      if (resp.ok) {
        const result = await resp.json();
        return result.text || JSON.stringify(result);
      }
    }
  } catch {
    // No es JSON, devolver contenido tal cual
  }
  return content;
}

async function startBot() {
  const { state, saveCreds } = await useMultiFileAuthState("auth_whatsapp");

  const sock = makeWASocket({
    auth: state,
    printQRInTerminal: true,
  });

  sock.ev.on("creds.update", saveCreds);

  sock.ev.on("connection.update", ({ connection, lastDisconnect }) => {
    if (connection === "close") {
      const reason = new Boom(lastDisconnect?.error)?.output?.statusCode;
      if (reason !== DisconnectReason.loggedOut) {
        console.log("Reconectando...");
        startBot();
      } else {
        console.log("Sesion cerrada. Borra auth_whatsapp/ y escanea QR de nuevo.");
      }
    } else if (connection === "open") {
      console.log("GemmaBot WhatsApp conectado!");
    }
  });

  sock.ev.on("messages.upsert", async ({ messages }) => {
    for (const msg of messages) {
      if (!msg.message || msg.key.fromMe) continue;

      const jid = msg.key.remoteJid;
      if (!isAuthorized(jid)) continue;

      const text =
        msg.message.conversation ||
        msg.message.extendedTextMessage?.text ||
        "";

      if (!text.trim()) continue;

      console.log(`[${jid}]: ${text}`);

      try {
        let response = await chatWithGemma(text);
        response = await executeToolCalls(response);

        // Limitar a 4096 chars por mensaje de WhatsApp
        if (response.length > 4000) {
          response = response.substring(0, 4000) + "\n[...]";
        }

        await sock.sendMessage(jid, { text: response });
        console.log(`[GemmaBot]: ${response.substring(0, 100)}...`);
      } catch (err) {
        console.error("Error:", err.message);
        await sock.sendMessage(jid, {
          text: `Error: ${err.message}\nVerifica que Gemma este corriendo.`,
        });
      }
    }
  });
}

startBot().catch(console.error);
