import reflex as rx

def navbar_btn(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.text(text)
        ),
        href=url,
        is_external=True,
    )