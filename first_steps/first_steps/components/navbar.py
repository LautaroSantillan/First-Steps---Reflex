import reflex as rx

from first_steps.components.navbar_btn import navbar_btn
from first_steps.routes import Route
import first_steps.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
            rx.link(
                rx.image(
                    src="/logo-data-riders.png",
                    width=["80px", "100px", "100px"], 
                    height="auto",
                    alt="Logotipo de Data Riders"
                ),
                href=Route.INDEX.value,
                _hover={
                    "cursor": "pointer",
                    "box_shadow": f"{styles.SHADOW_VALUE}",
                    "transform": "translateY(-2px)",
                    "transition": "all 0.3s ease-in-out",
                    "cursor": "pointer"
                },
            ),
            rx.center(
                navbar_btn("SITIO OFICIAL", "https://datariders.io/", display=["none", "flex", "flex"]),
                navbar_btn("CONTACTO", Route.CONTACT.value),
                gap=["1rem", "3rem"],
                display="flex"
            ),
            z_index="999",
            bg=styles.Color.BACKGROUND.value,
            padding_left="0.625rem",
            padding_right="0.625rem",
            display="flex",
            justify_content=["space-around", "space-evenly"],
            align_items="center",
            text_transform="uppercase",
            height="6rem",
            line_height="3.125rem",
            border_bottom="0.125rem dashed #fff"
    )