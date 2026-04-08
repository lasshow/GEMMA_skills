---
name: conversor-divisas
description: Convierte entre monedas del mundo con tipos de cambio actualizados. EUR, USD, GBP, MXN, ARS, COP y mas. Triggers - cambio, divisa, euros a dolares, dolares a euros, tipo de cambio, convertir moneda, cuantos euros, cuantos dolares.
---

# Conversor de Divisas

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - amount: Number. Cantidad a convertir.
  - from: String. Moneda origen (codigo ISO: EUR, USD, GBP, MXN, etc.).
  - to: String. Moneda destino.

### Presentar resultados
- Muestra la conversion con tipo de cambio
- Indica la fuente de los datos
- SIEMPRE responde en espanol
