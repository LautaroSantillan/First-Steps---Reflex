"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
# Components
from first_steps.components.navbar import navbar
from first_steps.views.header.header import header
from first_steps.components.footer import footer
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
                max_Width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
            ),
        ),
        footer(),
        background_image="linear-gradient(to top, #000, #31175e)",
        #background_color=styles.Color.PRIMARY.value,
        min_height="100vh",
        display="grid",
        grid_template_rows="auto 1fr auto"
    )

app = rx.App(
    theme=styles.CUSTOM_THEME
)
app.add_page(
    index,
    title="DEMO | Data Riders",
    image="../assets/logo-data-riders.png"
)
