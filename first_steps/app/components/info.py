import reflex as rx
import app.styles.styles as styles

def info(title: str, body: str) -> rx.Component:
    return rx.hstack(
        rx.text(
            title,
            color=styles.Color.BLUE_BTN_2.value,
            font_weight=styles.Weight.BOLD.value
        ),
        f"{body}",
        font_size=styles.Size.MEDIUM.value,
        font_family=styles.Font.DEFAULT.value,
        margin_x=["0", "15px"],
        width=["100%", "auto"]
    )