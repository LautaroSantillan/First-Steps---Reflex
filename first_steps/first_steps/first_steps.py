"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
import first_steps.styles.styles as styles

# class State(rx.State):
#     """Define your app state here."""

app = rx.App(
    theme=styles.CUSTOM_THEME
)