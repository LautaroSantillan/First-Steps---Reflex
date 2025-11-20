import reflex as rx
import datetime
# Styles
import app.styles.styles as styles
from app.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.image(
                src="/logotipo.png",
                width="25px", 
                height="25px"
            ),
            rx.text(f"© 2010-{datetime.date.today().year} DATA RIDERS - Todos los Derechos Reservados."),
            margin=Size.DEFAULT,
        ),
        width="100%",
        border_top=f"0.125rem dashed {styles.Color.BLUE_BTN.value}",
        text_align="center"
    )