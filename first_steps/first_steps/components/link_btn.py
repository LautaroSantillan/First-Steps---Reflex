import reflex as rx

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
            padding_right=Size.DEFAULT.value,
            width="100%"
        ),
        href=url,
        is_external=True,
        align_items="start"
    )