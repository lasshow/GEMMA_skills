"""
Consulta de clima via wttr.in (sin API key, CORS nativo).
"""

import httpx


async def get_weather(city: str, lang: str = "es") -> str:
    """Obtiene el clima actual de una ciudad."""
    try:
        url = f"https://wttr.in/{city}?format=j1&lang={lang}"
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(url)
            resp.raise_for_status()

        data = resp.json()
        current = data["current_condition"][0]

        temp = current["temp_C"]
        feels = current["FeelsLikeC"]
        desc = current.get("lang_es", [{}])
        desc_text = desc[0].get("value", current.get("weatherDesc", [{}])[0].get("value", "")) if desc else ""
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        wind_dir = current["winddir16Point"]

        result = (
            f"Clima en {city}:\n"
            f"- Temperatura: {temp}C (sensacion {feels}C)\n"
            f"- Condicion: {desc_text}\n"
            f"- Humedad: {humidity}%\n"
            f"- Viento: {wind} km/h ({wind_dir})"
        )

        # Pronostico siguiente
        if "weather" in data and len(data["weather"]) > 1:
            tomorrow = data["weather"][1]
            max_t = tomorrow["maxtempC"]
            min_t = tomorrow["mintempC"]
            result += f"\n- Manana: {min_t}C - {max_t}C"

        return result

    except Exception as e:
        return f"Error consultando clima: {e}"
