import reflex as rx
from first_steps.components.navbar_btn import navbar_btn

import first_steps.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
            rx.image(
                src="/logo-data-riders.png",
                width="100px", 
                height="auto",
                alt="Logotipo de Data Riders"
            ),
            navbar_btn("CONTACTO", "https://google.com"),
            z_index="999",
            bg=styles.Color.BACKGROUND.value,
            #padding_top="1.25rem",
            padding_left="0.625rem",
            padding_right="0.625rem",
            display="flex",
            justify_content="space-evenly",
            align_items="center",
            text_transform="uppercase",
            height="6rem",
            line_height="3.125rem",
            border_bottom="0.125rem dashed white"
    )