import reflex as rx 

def button(button_text:str = "Click Me!",
           size: str = "md",
):
    return rx.button(
        button_text,
        size = size,
        color_scheme = "blue",
        bg = "#006EC7",
    )


