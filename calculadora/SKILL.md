---
name: calculadora
description: Calcula expresiones matematicas con precision. Aritmetica, algebra, trigonometria, porcentajes, conversiones. Triggers - calcula, cuanto es, suma, resta, multiplica, divide, porcentaje, raiz, seno, coseno.
---

# Calculadora Matematica

## Instrucciones

Cuando el usuario pida un calculo matematico:

### Como calcular
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con el campo:
  - expression: String. La expresion matematica a evaluar.

### Formatos soportados
- Aritmetica: "2 + 3 * 4", "100 / 7"
- Potencias: "Math.pow(2, 10)", "2**10"
- Raiz: "Math.sqrt(144)"
- Trigonometria: "Math.sin(Math.PI/2)", "Math.cos(0)"
- Porcentajes: "250 * 0.21" (21% de 250)
- Constantes: "Math.PI", "Math.E"

### Presentar resultados
- Muestra el resultado con precision apropiada
- Explica el calculo brevemente si es complejo
- SIEMPRE responde en espanol
