import reflex as rx
from first_steps.components.link_btn import link_btn

def header() -> rx.Component:
    return rx.vstack(
        rx.text("Decisiones inteligentes que transforman tu negocio."),
        rx.text("Tomá decisiones basadas en datos y elevá tu empresa al siguiente nivel."),
        rx.hstack(
            link_btn("Visualizar DEMOS", "https://google.com"),
            link_btn("Contacto", "https://google.com"),
        ),
    )