import reflex as rx
from rxconfig import config
import first_steps.utils as utils
# Components
from first_steps.components.navbar import navbar
from first_steps.views.header.header import header
from first_steps.components.footer import footer
from first_steps.components.links import links
# Styles
import first_steps.styles.styles as styles

@rx.page(
    title=utils.index_description,
    description=utils.index_description,
    meta=utils.index_meta
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_Width=styles.MAX_WIDTH,
                width="100%",
                margin_bottom="20px"
            ),
        ),
        footer(),
        background_image=f"linear-gradient(to top, #000, #31175e)",
        min_height="100vh",
        display="grid"
    )