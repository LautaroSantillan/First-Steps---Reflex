import reflex as rx
from first_steps.components.info import info
import first_steps.styles.styles as styles

def header() -> rx.Component:
    return rx.vstack(
        rx.text(
            "¡Expandi tu negocio con nosotros!",
            font_size=[styles.Size.BIG.value, styles.Size.XXL.value],
            font_style="italic",
            margin_bottom=styles.Size.SMALL.value,
            font_weight="bold",
            font_family=styles.Font.COURIER.value,
            text_align="center",
            width="100%"
        ),
        rx.text(
            "Decisiones inteligentes que transforman tu negocio. Tomá decisiones basadas en datos y elevá tu empresa al siguiente nivel.",
            font_size=styles.Size.MEDIUM.value,
            font_family=styles.Font.DEFAULT.value,
            font_weight="400",
            padding_x=["20px", "30px"]
        ),
        rx.flex(
            info("15+", "años de experiencia"),
            info("...+", "cantidad de proyectos"),
            info("...+", "clientes satisfechos"),
            justify_content="center", 
            gap=styles.Size.DEFAULT.value,
            width="100%",
            display=["grid", "flex", "flex"],
            grid_template_columns={"base": "1fr"}, # Una sola columna en móvil
            align_items=["center", "normal"]
        ),
        width="100%",
        margin_bottom="5px"
    )