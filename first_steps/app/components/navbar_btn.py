import reflex as rx
import app.styles.styles as styles

def navbar_btn(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.text(text),
            bg="none",
            _hover={
                "border":"0.125rem solid #fff",
                "background_color":f"{styles.Color.GRADIENT.value}",
                "box_shadow": f"{styles.SHADOW_VALUE}",
                "transform": "translateY(-2px)",
                "transition": "all 0.3s ease-in-out",
                "cursor": "pointer"
            },
        ),
        href=url,
        is_external=False,
        position="relative",
        letter_spacing="0.125rem",
        text_decoration="none",
        color="white"
    )