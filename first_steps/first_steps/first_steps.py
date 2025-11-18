"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
# Components
from first_steps.components.navbar import navbar
from first_steps.views.header.header import header
from first_steps.components.footer import footer
from first_steps.components.links import links
# Styles
import first_steps.styles.styles as styles

class State(rx.State):
    """The app state."""

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_Width=styles.MAX_WIDTH,
                width="100%",
                margin_bottom="20px"
                #margin_y=styles.Size.BIG.value
            ),
        ),
        footer(),
        background_image=f"linear-gradient(to top, #000, #31175e)",
        min_height="100vh",
        display="grid"
    )

app = rx.App(
    theme=styles.CUSTOM_THEME
)
app.add_page(
    index,
    title="DEMO | Data Riders",
    image="../assets/logo-data-riders.png"
)
