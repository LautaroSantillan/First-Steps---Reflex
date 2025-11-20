import reflex as rx
from app.components.info import info
import app.styles.styles as styles

def header() -> rx.Component:
    return rx.vstack(
        rx.text(
            "¡Expandi tu negocio con nosotros!",
            font_size=[styles.Size.LARGE.value, styles.Size.XXL.value],
            margin_bottom=styles.Size.SMALL.value,
            font_weight=styles.Weight.BOLD.value,
            font_family=styles.Font.DEFAULT.value,
            text_align="center",
            width="100%"
        ),
        rx.text(
            "Decisiones inteligentes que transforman tu negocio. Tomá decisiones basadas en datos y elevá tu empresa al siguiente nivel.",
            font_size=styles.Size.MEDIUM.value,
            font_family=styles.Font.DEFAULT.value,
            font_weight=styles.Weight.MEDIUM.value,
            padding_x=["20px", "30px"]
        ),
        rx.flex(
            info("+15", "años de experiencia"),
            info("+...", "cantidad de proyectos"),
            info("+...", "clientes satisfechos"),
            justify_content="center", 
            gap=styles.Size.DEFAULT.value,
            width="100%",
            display=["grid", "flex", "flex"],
            grid_template_columns={"base": "1fr"},
            align_items=["center", "normal"]
        ),
        width="100%",
        margin_bottom="5px"
    )