# WhatsApp via Tasker + AutoNotification (Ruta Segura)

Alternativa a Baileys que NO tiene riesgo de ban.

## Requisitos

1. **Tasker** (Play Store, $3.49)
2. **AutoNotification** (Play Store, gratis con compra in-app)
3. **Termux** con Gemma 4 corriendo

## Configuracion

### Paso 1: Perfil en Tasker

```
Perfil: WhatsApp Intercept
  Evento: AutoNotification Intercept
  Filtro:
    - App: WhatsApp
    - Titulo: (nombre del contacto autorizado)

Tarea: Procesar con Gemma
  1. Variable Set: %mensaje = %antext
  2. Variable Set: %remitente = %antitle
  3. Shell: curl -s -X POST http://localhost:8080/v1/chat/completions \
       -H "Content-Type: application/json" \
       -d '{"messages":[{"role":"system","content":"Eres GemmaBot..."},{"role":"user","content":"'%mensaje'"}],"max_tokens":512}' \
       > /tmp/gemma_response.json
  4. Shell: cat /tmp/gemma_response.json | python3 -c "import sys,json; print(json.load(sys.stdin)['choices'][0]['message']['content'])"
  5. Variable Set: %respuesta = %stdout
  6. AutoNotification Reply: %respuesta
```

### Paso 2: Habilitar permisos

1. Abrir AutoNotification > Configuracion > Habilitar Notification Listener
2. Dar permiso a Tasker para Accessibility Service
3. En WhatsApp > Notificaciones > Activar notificaciones emergentes

### Paso 3: Filtrar contactos

Para que solo responda a ciertos contactos, anadir en el filtro:
- Titulo contiene: "Mama" OR "Trabajo" OR "Jefe"

O usar Variable Match en Tasker para lista de numeros autorizados.

## Ventajas vs Baileys

- Sin riesgo de ban
- No necesita Node.js
- Funciona con WhatsApp oficial
- Mas estable a largo plazo

## Limitaciones

- Solo responde a mensajes que generan notificacion
- Si WhatsApp esta en primer plano, no se genera notificacion
- Respuesta limitada a la ventana de reply de la notificacion
- No puede enviar mensajes proactivamente (solo responder)
