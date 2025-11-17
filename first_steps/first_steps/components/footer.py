import reflex as rx
import datetime
# Styles
import first_steps.styles.styles as styles
from first_steps.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.image(
                src="/logotipo.png",
                width="25px", 
                height="25px"
            ),
            rx.text(f"© 2010-{datetime.date.today().year}"),
            rx.link(
                "DATA RIDERS",
                href="https://datariders.io/",
                is_external=True,
                font_size=Size.DEFAULT
            ),
            rx.text(
                "- Todos los Derechos Reservados.",
                font_size=Size.DEFAULT
            ),
            margin=Size.DEFAULT,
        ),
        width="100%",
        border_top="0.125rem dashed white"
    )