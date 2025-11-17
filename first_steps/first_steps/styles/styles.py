import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"

class Color(Enum):
    PRIMARY = "#060443"
    SECONDARY = "#531757"
    BACKGROUND = "#31175e"
    CONTENT = "#7c849c"

class Font(Enum):
    DEFAULT = "Poppins-Light"
    TITLE = "Poppins-Bold"
    LOGO = "Comfortaa-Medium"

# Styles
navbar_p = dict(
    font_family=Font.LOGO.value,
    font_size=Size.BIG.value
)


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "Button": {
        "width": "100%",
        "height": "100%",
        "white_space": "normal",
        "text_align": "start",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.BACKGROUND.value,
        "_hover":{
            "background_color": Color.PRIMARY.value
        }  
    },
    "Link": {
        "text_decoration": "none",
        "_hover": {}
    }
}

# --- Objeto Theme ---
# El argumento 'components' es donde defines los estilos base para tipos de componentes.
CUSTOM_THEME = rx.theme(
    name="custom_theme",
    components=BASE_STYLE,
)