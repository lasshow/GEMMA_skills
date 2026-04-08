# GEMMA Skills - Google AI Edge Gallery

Skills personalizados en español para **Google AI Edge Gallery** con modelos Gemma 4 (E2B/E4B) on-device.

## Skills incluidos

| Skill | Tipo | Descripcion | API Key |
|-------|------|-------------|---------|
| **buscar-web** | JS | Busca en internet (DuckDuckGo + Wikipedia) | No |
| **noticias** | JS | Noticias actuales via Google News RSS | No |
| **navegar-web** | JS | Lee el contenido de cualquier pagina web | No |
| **resumir-pagina** | JS | Extrae y resume texto de cualquier URL | No |
| **enviar-correo** | Native | Redacta y envia emails via Gmail | No |
| **enviar-sms** | Native | Envia mensajes SMS | No |

## Instalacion

### Opcion 1: Importar desde URL
1. En AI Edge Gallery → Agent Skills → (+) → **Load skill from URL**
2. Introduce la URL del skill (necesita GitHub Pages habilitado)

### Opcion 2: Importar localmente
1. Descarga/clona este repositorio
2. Copia cada carpeta de skill a la carpeta `Download` de tu telefono
3. En la app → Agent Skills → (+) → **Import local skill**
4. Selecciona la carpeta del skill → Add

### Opcion 3: Via ADB
```bash
adb push buscar-web/ /sdcard/Download/buscar-web
adb push noticias/ /sdcard/Download/noticias
adb push navegar-web/ /sdcard/Download/navegar-web
adb push resumir-pagina/ /sdcard/Download/resumir-pagina
adb push enviar-correo/ /sdcard/Download/enviar-correo
adb push enviar-sms/ /sdcard/Download/enviar-sms
```

## Notas tecnicas

- Los skills JS usan APIs con CORS nativo (DuckDuckGo, Wikipedia, rss2json)
- Para leer paginas arbitrarias se usa `corsproxy.io` como proxy CORS
- Los skills nativos usan `run_intent` (solo `send_email` y `send_sms` soportados)
- Todos los skills responden en español

## Creditos

Basado en la arquitectura de [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) y skills de la comunidad.
