import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "900px"

# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    XXL = "2.5em"

class Color(Enum):
    PRIMARY = "#060443"
    SECONDARY = "#531757"
    BACKGROUND = "#31175e"
    CONTENT = "#7c849c"

SHADOW_VALUE = f"0 0 10px {Color.PRIMARY.value}, 0 0 20px {Color.PRIMARY.value}, 0 0 30px rgba(83, 23, 87, 0.5)"
class Font(Enum):
    DEFAULT = "Poppins-Light"
    TITLE = "Poppins-Bold"
    LOGO = "Comfortaa-Medium"
    COURIER = "Courier New, Courier, monospace"

# Styles
navbar_p = dict(
    font_family=Font.LOGO.value,
    font_size=Size.BIG.value
)

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
}

# --- Objeto Theme ---
# El argumento 'components' es donde defines los estilos base para tipos de componentes.
CUSTOM_THEME = rx.theme(
    name="custom_theme",
    components=BASE_STYLE,
)