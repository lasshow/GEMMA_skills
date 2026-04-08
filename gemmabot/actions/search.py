"""
Busqueda web via DuckDuckGo API + Wikipedia (sin API key).
"""

import httpx


async def search_web(query: str, lang: str = "es") -> str:
    """Busca informacion en DuckDuckGo y Wikipedia."""
    results = []

    # DuckDuckGo Instant Answer API
    try:
        ddg_url = (
            f"https://api.duckduckgo.com/"
            f"?q={query}&format=json&no_html=1&skip_disambig=1&kl={lang}-{lang}"
        )
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(ddg_url)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("AbstractText"):
                    results.append(f"Respuesta: {data['AbstractText']}")
                    if data.get("AbstractURL"):
                        results.append(f"Fuente: {data['AbstractURL']}")
                if data.get("Answer"):
                    results.append(f"Dato: {data['Answer']}")
                # Temas relacionados
                for topic in (data.get("RelatedTopics") or [])[:3]:
                    if isinstance(topic, dict) and topic.get("Text"):
                        results.append(f"- {topic['Text'][:200]}")
    except Exception:
        pass

    # Wikipedia API
    try:
        wiki_params = {
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": query,
            "gsrlimit": "2",
            "prop": "extracts",
            "explaintext": "1",
            "exintro": "1",
            "origin": "*",
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(
                f"https://{lang}.wikipedia.org/w/api.php",
                params=wiki_params,
            )
            if resp.status_code == 200:
                data = resp.json()
                pages = data.get("query", {}).get("pages", {})
                for page in sorted(pages.values(), key=lambda p: p.get("index", 99))[:2]:
                    extract = page.get("extract", "")
                    if len(extract) > 50:
                        if len(extract) > 500:
                            extract = extract[:500] + "..."
                        title = page.get("title", "")
                        results.append(f"\nWikipedia - {title}:\n{extract}")
    except Exception:
        pass

    if not results:
        return f"No se encontraron resultados para: {query}"

    return "\n".join(results)[:2000]
