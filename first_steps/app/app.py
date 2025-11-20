"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
import app.styles.styles as styles
from app.pages import index

# class State(rx.State):
#     """Define your app state here."""

app = rx.App(
    theme=styles.CUSTOM_THEME,
)
