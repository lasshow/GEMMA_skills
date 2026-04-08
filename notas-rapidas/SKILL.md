---
name: notas-rapidas
description: Guarda, lee y organiza notas rapidas en el telefono. Funciona offline con almacenamiento local. Triggers - nota, apunta, recuerda, anota, guarda esto, mis notas, lista de notas, borrar nota.
---

# Notas Rapidas

## Instrucciones

Sistema de notas persistentes almacenadas localmente en el telefono.

### Acciones disponibles

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - action: String. Una de: "add", "list", "delete", "clear"
  - text: String (solo para "add"). El texto de la nota a guardar.
  - id: Number (solo para "delete"). El indice de la nota a borrar (empezando en 0).

### Ejemplos de uso
- "apunta que tengo cita el martes" -> action: "add", text: "Cita el martes"
- "mis notas" -> action: "list"
- "borra la nota 2" -> action: "delete", id: 1
- "borra todas las notas" -> action: "clear"

### Presentar resultados
- Al guardar: confirma que se guardo
- Al listar: muestra todas las notas numeradas con fecha
- SIEMPRE responde en espanol
