---
name: temporizador
description: Crea temporizadores y cronometros visuales dentro del chat. Cuenta atras con alarma sonora. Triggers - temporizador, timer, cuenta atras, cronometro, pon un timer, alarma de cocina, X minutos.
---

# Temporizador y Cronometro

## Instrucciones

Cuando el usuario quiera un temporizador o cuenta atras:

### Como crear temporizador
Llama la herramienta `run_js` con los siguientes parametros exactos:
- data: Un string JSON con los campos:
  - minutes: Number. Minutos para la cuenta atras.
  - seconds: Number (opcional). Segundos adicionales.
  - label: String (opcional). Etiqueta del temporizador (ej: "Pasta", "Descanso").

### Presentar resultados
- Confirma el temporizador creado
- Indica que sonara una alarma al terminar
- SIEMPRE responde en espanol
