import reflex as rx 

def navbar():
    return rx.flex(
        rx.box(
            rx.image(src='/Polydelta_Logo_WhiteBG_2023.png')
        ),
        rx.center(
            rx.menu(
                rx.menu_button("Menu"),
                rx.menu_list(
                      rx.menu_item('Home'),
                      rx.menu_item('About')
                )
            )

        ),
        justify_content = 'space-between'

    )