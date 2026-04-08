"""
Cliente para Tasker MCP Server.
Ejecuta acciones en el telefono Android via Tasker.
Ref: https://github.com/dceluis/tasker-mcp
"""

import httpx


class TaskerMCP:
    def __init__(self, base_url: str = "http://localhost:3000"):
        self.base_url = base_url.rstrip("/")

    async def run_task(self, task: str, params: dict) -> str:
        """Ejecuta una tarea en Tasker."""
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.post(
                    f"{self.base_url}/task",
                    json={"name": task, "params": params},
                )
                if resp.status_code == 200:
                    data = resp.json()
                    return data.get("result", "Tarea ejecutada correctamente")
                return f"Error Tasker: HTTP {resp.status_code}"
        except httpx.ConnectError:
            return self._fallback_termux(task, params)
        except Exception as e:
            return f"Error Tasker: {e}"

    def _fallback_termux(self, task: str, params: dict) -> str:
        """Fallback: ejecutar via termux-api directamente."""
        import subprocess

        commands = {
            "linterna": self._cmd_flashlight,
            "wifi": self._cmd_wifi,
            "volumen": self._cmd_volume,
            "notificacion": self._cmd_notification,
            "enviar_sms": self._cmd_sms,
            "shell": self._cmd_shell,
        }

        handler = commands.get(task)
        if handler:
            return handler(params)
        return f"Tarea '{task}' no disponible sin Tasker MCP. Instala Tasker."

    def _cmd_flashlight(self, params: dict) -> str:
        import subprocess
        state = params.get("state", "on")
        subprocess.run(["termux-torch", state], capture_output=True)
        return f"Linterna {'encendida' if state == 'on' else 'apagada'}"

    def _cmd_wifi(self, params: dict) -> str:
        import subprocess
        state = params.get("state", "on")
        enable = "true" if state == "on" else "false"
        subprocess.run(["termux-wifi-enable", enable], capture_output=True)
        return f"WiFi {'activado' if state == 'on' else 'desactivado'}"

    def _cmd_volume(self, params: dict) -> str:
        import subprocess
        level = params.get("level", 7)
        stream = params.get("stream", "media")
        subprocess.run(
            ["termux-volume", stream, str(level)], capture_output=True
        )
        return f"Volumen {stream} ajustado a {level}"

    def _cmd_notification(self, params: dict) -> str:
        import subprocess
        titulo = params.get("titulo", "GemmaBot")
        texto = params.get("texto", "")
        subprocess.run(
            ["termux-notification", "-t", titulo, "-c", texto],
            capture_output=True,
        )
        return f"Notificacion enviada: {titulo}"

    def _cmd_sms(self, params: dict) -> str:
        import subprocess
        numero = params.get("numero", "")
        mensaje = params.get("mensaje", "")
        if not numero:
            return "Error: numero no proporcionado"
        subprocess.run(
            ["termux-sms-send", "-n", numero, mensaje],
            capture_output=True,
        )
        return f"SMS enviado a {numero}"

    def _cmd_shell(self, params: dict) -> str:
        import subprocess
        command = params.get("command", "")
        if not command:
            return "Error: comando vacio"
        # Seguridad: bloquear comandos peligrosos
        blocked = ["rm -rf /", "mkfs", "dd if=", ":(){ :|:& };:"]
        for b in blocked:
            if b in command:
                return f"Comando bloqueado por seguridad: {b}"
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        output = result.stdout or result.stderr or "Ejecutado sin salida"
        return output[:1000]  # Limitar salida
