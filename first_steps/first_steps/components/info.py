import reflex as rx
import first_steps.styles.styles as styles

def info(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            title,
            color=styles.Color.CONTENT.value,
            font_weight="bold"
        ),
        f"{body}",
        font_size=styles.Size.DEFAULT.value,
        font_family=styles.Font.COURIER.value,
        margin_x=["0", "15px"],
        width=["100%", "auto"]
    )