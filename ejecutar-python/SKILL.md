---
name: ejecutar-python
description: Ejecuta codigo Python directamente en el telefono usando Pyodide. Calcula, procesa datos, genera texto. Triggers - python, ejecuta codigo, calcula, programa, script, run python, codigo.
---

# Ejecutar Python

## Instrucciones

Cuando el usuario quiera ejecutar codigo Python o necesite calculos complejos:

### Como ejecutar
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con el campo:
  - code: String. El codigo Python a ejecutar. IMPORTANTE: usa print() para mostrar resultados.

### Reglas
- SIEMPRE incluye print() para que el resultado sea visible
- El codigo se ejecuta via Pyodide (Python en WebAssembly)
- Soporta librerias estandar de Python
- La primera ejecucion puede tardar unos segundos en cargar Pyodide
- SIEMPRE responde en espanol explicando el resultado
