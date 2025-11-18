"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
# Styles
import first_steps.styles.styles as styles

from first_steps.pages.index import index
from first_steps.pages.contact import contact

app = rx.App(
    theme=styles.CUSTOM_THEME
)
