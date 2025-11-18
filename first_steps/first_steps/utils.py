import reflex as rx

index_title = "DEMO | Data Riders"
contact_title = "DEMO | Contacto"
index_description = "Landing page para mostrar las distintas DEMO publicadas en charlas o reuniones"
index_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]


def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'"),