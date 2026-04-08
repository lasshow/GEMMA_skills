"""
Cliente HTTP para Gemma 4 corriendo en llama.cpp server.
Envia prompts y parsea respuestas con tool calls.
"""

import json
import httpx
from pathlib import Path

SYSTEM_PROMPT_PATH = Path(__file__).parent / "system_prompt.txt"


class GemmaClient:
    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url.rstrip("/")
        self.system_prompt = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
        self.history: list[dict] = []

    async def chat(self, user_message: str) -> dict:
        """Envia mensaje al modelo y devuelve respuesta parseada.

        Returns:
            {"text": str, "tool_calls": list[dict] | None}
        """
        self.history.append({"role": "user", "content": user_message})

        messages = [{"role": "system", "content": self.system_prompt}]
        # Mantener solo ultimos 20 mensajes para no desbordar contexto
        messages.extend(self.history[-20:])

        payload = {
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2048,
            "stream": False,
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            resp = await client.post(
                f"{self.base_url}/v1/chat/completions",
                json=payload,
            )
            resp.raise_for_status()

        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": content})

        return self._parse_response(content)

    def _parse_response(self, content: str) -> dict:
        """Extrae tool_calls del JSON si existen."""
        tool_calls = None

        # Buscar bloque JSON con tool_calls
        try:
            # Intentar parsear todo el contenido como JSON
            parsed = json.loads(content)
            if isinstance(parsed, dict) and "tool_calls" in parsed:
                tool_calls = parsed["tool_calls"]
                return {"text": "", "tool_calls": tool_calls}
        except json.JSONDecodeError:
            pass

        # Buscar JSON embebido en markdown ```json ... ```
        if "```json" in content:
            start = content.index("```json") + 7
            end = content.index("```", start)
            json_str = content[start:end].strip()
            try:
                parsed = json.loads(json_str)
                if isinstance(parsed, dict) and "tool_calls" in parsed:
                    tool_calls = parsed["tool_calls"]
                    text = content[:content.index("```json")].strip()
                    return {"text": text, "tool_calls": tool_calls}
            except json.JSONDecodeError:
                pass

        return {"text": content, "tool_calls": None}

    def clear_history(self):
        """Limpia el historial de conversacion."""
        self.history.clear()
