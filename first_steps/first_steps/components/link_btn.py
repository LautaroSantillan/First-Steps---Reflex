import reflex as rx

import first_steps.styles.styles as styles
from first_steps.styles.styles import Size as Size

def link_btn(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(
                "zoom_in",
                tag="arrow_forward",
                size=18, 
                color=rx.color("white", 12)
            ),
            rx.text(text),
            justify_content="start", 
            gap=Size.DEFAULT.value,
            width="100%",
            background_color=styles.Color.SECONDARY.value,
            _hover={
                "background_color":f"{styles.Color.BACKGROUND.value}",
                "box_shadow": f"{styles.SHADOW_VALUE}",
                "transform": "translateY(-2px)",
                "transition": "all 0.3s ease-in-out",
                "cursor": "pointer"
            },
            transition="all 0.3s ease-in-out"
        ),
        href=url,
        is_external=True,
        width="100%",
        align_items="start"
    )