import reflex as rx

from app.components.navbar_btn import navbar_btn
from app.routes import Route
import app.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
            rx.link(
                rx.image(
                    src="/logo-data-riders.png",
                    width=["80px", "100px", "110px"], 
                    height="auto",
                    alt="Logotipo de Data Riders"
                ),
                href="https://datariders.io/",
                is_external=True,
                _hover={
                    "cursor": "pointer",
                    "transform": "translateY(-2px)",
                    "transition": "all 0.3s ease-in-out",
                    "cursor": "pointer"
                },
            ),
            rx.center(
                navbar_btn("SITIO OFICIAL", "https://datariders.io/"),
                gap=["1rem", "3rem"],
                display="flex"
            ),
            z_index="999",
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