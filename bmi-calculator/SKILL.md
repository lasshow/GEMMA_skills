---
name: bmi-calculator
description: Calcula el Indice de Masa Corporal (IMC/BMI) y clasifica el resultado. Triggers - imc, bmi, peso ideal, indice masa corporal, cuanto deberia pesar, peso saludable.
---

# Calculadora de IMC

## Instrucciones

Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - weight: Number. Peso en kilogramos.
  - height: Number. Altura en centimetros.

### Presentar resultados
- Muestra el IMC calculado con clasificacion OMS
- Indica rango de peso saludable
- SIEMPRE anade aviso de que consulte un profesional de salud
- SIEMPRE responde en espanol
