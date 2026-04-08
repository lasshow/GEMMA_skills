"""
Enruta tool calls de Gemma a las acciones correspondientes.
"""

from actions.tasker_mcp import TaskerMCP
from actions.weather import get_weather
from actions.search import search_web
from actions.notes import NotesDB


class ToolRouter:
    def __init__(self, config: dict):
        self.tasker = TaskerMCP(config.get("tasker_url", "http://localhost:3000"))
        self.notes = NotesDB(config.get("notes_db", "gemmabot_notes.db"))
        self._handlers = {
            "tasker": self._handle_tasker,
            "weather": self._handle_weather,
            "search": self._handle_search,
            "notes": self._handle_notes,
        }

    async def execute(self, tool_calls: list[dict]) -> str:
        """Ejecuta una lista de tool calls y devuelve resultados."""
        results = []
        for call in tool_calls:
            tool = call.get("tool", "")
            params = call.get("params", {})
            handler = self._handlers.get(tool)
            if handler:
                result = await handler(params)
                results.append(f"[{tool}] {result}")
            else:
                results.append(f"[{tool}] Error: herramienta desconocida")
        return "\n".join(results)

    async def _handle_tasker(self, params: dict) -> str:
        task = params.get("task", "")
        task_params = params.get("params", {})
        return await self.tasker.run_task(task, task_params)

    async def _handle_weather(self, params: dict) -> str:
        city = params.get("city", "Madrid")
        return await get_weather(city)

    async def _handle_search(self, params: dict) -> str:
        query = params.get("query", "")
        return await search_web(query)

    async def _handle_notes(self, params: dict) -> str:
        action = params.get("action", "list")
        if action == "add":
            return self.notes.add(params.get("text", ""))
        elif action == "list":
            return self.notes.list_all()
        elif action == "delete":
            return self.notes.delete(params.get("id", 0))
        elif action == "search":
            return self.notes.search(params.get("query", ""))
        return "Accion de notas desconocida"
