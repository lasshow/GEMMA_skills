---
name: tip-calculator
description: Calcula propinas y divide cuentas entre personas. Para restaurantes y pagos compartidos. Triggers - propina, cuenta, dividir cuenta, split, tip, pagar cuenta, cuanto dejo, cuanto toca a cada uno.
---

# Calculadora de Propinas y Cuentas

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - total: Number. Total de la cuenta.
  - tip_percent: Number. Porcentaje de propina (por defecto 10).
  - people: Number. Numero de personas (por defecto 1).
  - currency: String. Moneda (por defecto "EUR").

### Presentar resultados
- Muestra desglose claro: subtotal, propina, total, por persona
- SIEMPRE responde en espanol
