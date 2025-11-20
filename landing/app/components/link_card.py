import reflex as rx

from app.styles.styles import Size, Color, Weight, SizesImg

def link_card(url: str, image: str, title: str, description: str) -> rx.Component:
    return rx.link(
        rx.box(
            rx.hstack(
                rx.image(
                    src=image,
                    display=["none", "block"],
                    width=SizesImg.IMG_HEADER.value,
                    margin_right=Size.DEFAULT.value,
                    border_radius=Size.SEMISMALL.value,
                    object_fit="cover",
                ),
                rx.vstack(
                    rx.text(
                        title,
                        font_size=Size.MEDIUM.value,
                        font_weight=Weight.BOLD.value,
                        color=Color.WHITE.value,
                        text_overflow="ellipsis",
                        no_of_lines=1,
                    ),
                    rx.text(
                        description,
                        font_size=Size.DEFAULT.value,
                        color=Color.WHITE.value,
                        text_overflow="ellipsis",
                        no_of_lines=2,
                    ),
                    align_items="start"
                ),
                align_items="center",
                width="100%"
            ),
            width="100%",
            padding=Size.MEDIUM.value,
            border_radius=Size.DEFAULT.value,
            background_color=Color.BLUE_BTN.value,
            _hover={
                "background_color": Color.BLUE_BTN_2.value,
                "box_shadow": f"0 0 10px {Color.GRADIENT_START.value}",
                "transform": "translateY(-5px)",
                "cursor": "pointer",
            },
            transition="all 0.3s ease-in-out",
        ),
        href=url,
        is_external=True,
        text_decoration="none",
        width="100%"
    )