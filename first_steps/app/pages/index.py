
import reflex as rx
from rxconfig import config
import app.utils as utils
# Components
from app.components.navbar import navbar
from app.views.header.header import header
from app.components.footer import footer
from app.components.links import links
# Styles
import app.styles.styles as styles

@rx.page(
    title=utils.INDEX_TITLE,
    description=utils.INDEX_DESCRIPTION,
    meta=utils.INDEX_META
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_bottom="20px"
            ),
        ),
        footer(),
        background_image=f"linear-gradient(to top, #000, #31175e)",
        min_height="100vh",
        display="grid",
        color="white"
    )