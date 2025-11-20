import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "900px"

# Sizes
class Size(Enum):
    ZERO = "0px !important" # 0px
    SMALL = "0.5em"         # 8px
    SEMISMALL = "0.8em" 	# 12px
    DEFAULT = "1em"         # 16px
    MEDIUM_SMALL="1.2em"    # 19px
    MEDIUM = "1.5em"        # 24px
    LARGE = "2em"           # 32px
    XL = "2.5em"            # 40px
    XXL = "3em"             # 48px

class Color(Enum):
    TITLE_BLUE="#000E42"
    GRADIENT_START = "rgb(232,61,129)"
    GRADIENT_END = "rgb(43,25,151)"
    GRADIENT="linear-gradient(134.98deg, #E83D81 0%, #2B1997 142.29%);"
    PINK_BTN="#E83D81"
    DARK_BLUE = "#000642"
    WHITE = "#FFFFFF"
    BLACK = "#000000"
    DEFAULT_BG = "#F2F2F2"
    BLUE_BTN="#201997"
    ERROR_RED = "#EF4E4E"
    CANCEL_BG = "#AD0626"
    GREEN = "#008000"
    GREY = "#A5A5A5"
    BLUE_BTN_2 = "#6639E4"

SHADOW_VALUE = f"0 0 10px {Color.GRADIENT_START.value}, 0 0 20px {Color.GRADIENT_END.value}, 0 0 30px rgba(83, 23, 87, 0.5)"

class Font(Enum):
    DEFAULT = "Poppins"

# Tamaños
class Weight(Enum):
    REGULAR="300"
    MEDIUM="500"
    BOLD="700"

class SizesImg(Enum):
    IMG_HEADER = "10%"
    LOGO_HEADER = "7%"

# Styles
navbar_p = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.LARGE.value
)

BASE_STYLE = {
    "font_family": Font.DEFAULT.value
}

# --- Objeto Theme ---
# El argumento 'components' es donde defines los estilos base para tipos de componentes.
CUSTOM_THEME = rx.theme(
    name="custom_theme",
    components=BASE_STYLE,
)

# # # Estilos globales

# BASE_STYLE = {
#     "font-family":FONT_FAMILY,
#     rx.heading: {
#         "font-family":FONT_FAMILY,
#     },
#     rx.dialog.title: {
#         "font-family":FONT_FAMILY,
#     },
#     rx.dialog.description: {
#         "font-family":FONT_FAMILY,
#     },
#     rx.text: {
#         "font-family":FONT_FAMILY,
#     },
#     rx.link: {
#         "text_decoration": "none",
#         "color": "white"
#     },
#     rx.button: {
#         "cursor": "pointer"
#     }
# }