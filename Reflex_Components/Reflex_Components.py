from rxconfig import config
import reflex as rx
from .components.navbar import navbar
from .components.button import button


style = {
    "font_family": "Arial",
    "font_size": "16px",
}


class State(rx.State):
    """The app state."""
    pass


def index() -> rx.Component:
    return rx.container(
        navbar(),
        rx.heading(
            "DM Sans Header"
        ),
        rx.text(
            "DM Sans Text"
        ),
        rx.button_group(
            button("Small Button",size = "sm"),
            button("Medium Button",size = "md"),
            button("Large Button",size = "lg"),
            space="1em"
        )
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=["styles.css"]
)
app.add_page(index)
app.compile()
