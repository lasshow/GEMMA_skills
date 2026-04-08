---
name: dice-random
description: Generador aleatorio - dados, monedas, numeros, listas, nombres. Para juegos, sorteos y decisiones aleatorias. Triggers - dado, tirar dado, aleatorio, random, moneda, cara o cruz, sorteo, elegir, numero aleatorio, d20.
---

# Generador Aleatorio

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - type: String. Uno de: "dice", "coin", "number", "pick", "shuffle"
  - sides: Number (para "dice"). Caras del dado (6, 20, 100...). Por defecto 6.
  - count: Number (para "dice"). Cantidad de dados. Por defecto 1.
  - min: Number (para "number"). Minimo. Por defecto 1.
  - max: Number (para "number"). Maximo. Por defecto 100.
  - items: Array de strings (para "pick" y "shuffle"). Lista de opciones.

### Presentar resultados
- Presenta el resultado de forma divertida
- Para dados de rol (d20): anade contexto de juego
- SIEMPRE responde en espanol
