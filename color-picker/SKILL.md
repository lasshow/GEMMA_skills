---
name: color-picker
description: Convierte colores entre formatos HEX, RGB, HSL. Muestra paletas y colores complementarios. Triggers - color, hex, rgb, hsl, paleta, color picker, convertir color, colores complementarios.
---

# Conversor de Colores

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - action: String. Una de: "convert", "palette", "random"
  - color: String (para "convert"). Color en cualquier formato: "#FF5733", "rgb(255,87,51)", "hsl(14,100%,60%)"
  - count: Number (para "palette" y "random"). Cantidad de colores (por defecto 5).

### Presentar resultados
- Muestra el color en todos los formatos (HEX, RGB, HSL)
- Para paletas: muestra colores complementarios/analogos
- SIEMPRE responde en espanol
