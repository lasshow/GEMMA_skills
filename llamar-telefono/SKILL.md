---
name: llamar-telefono
description: Inicia una llamada telefonica generando un enlace clickeable. El usuario toca y se abre el marcador. Triggers - llama, llamar, telefono, marca, haz una llamada, call, ring.
---

# Llamar por Telefono

## Instrucciones

Cuando el usuario quiera hacer una llamada telefonica:

### Proceso
1. Si el usuario da un numero, usalo directamente
2. Si solo da un nombre, PREGUNTA el numero
3. Genera un enlace clickeable con formato tel:

### Formato OBLIGATORIO
Responde asi:

**Llamando a [nombre/numero]:**
[Tocar para llamar](tel:+CODIGOPAIS_NUMERO)

### Ejemplos

Usuario: "llama al 666123456"
Respuesta:
**Llamar al 666123456:**
[Tocar para llamar](tel:+34666123456)

Usuario: "llama a emergencias"
Respuesta:
**Llamar a Emergencias (112):**
[Tocar para llamar](tel:112)

### Reglas
- SIEMPRE incluye codigo de pais si el usuario no lo da (pregunta el pais)
- Para Espana usa +34, Mexico +52, Argentina +54
- Numeros de emergencia: 112 (Europa), 911 (America)
- Formato tel: SIN espacios ni guiones: tel:+34666123456
- SIEMPRE responde en espanol
