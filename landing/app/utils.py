import reflex as rx

# Metadatos para la página principal (index)
INDEX_TITLE = "DEMO | Data Riders"
INDEX_DESCRIPTION = "Landing page para mostrar las distintas DEMO publicadas en charlas o reuniones"
INDEX_META = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "content": INDEX_TITLE},
    {"name": "og:description", "content": INDEX_DESCRIPTION},
    {"rel": "icon", "href": "../assets/logotipo.png", "type": "image/png"}
]

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")