from rxconfig import config
import reflex as rx
from .components.navbar import navbar
from .components.button import button

style = {
    "font_family": "MyFont",
    "font_size": "16px",
}

select_size = "md"

class appState(rx.State):
    """The slection of which service design topic you are interested in"""
    designStep: str = "Research"
    location: str = "In Person"
    numPeople: str = "1"
    time: str = "30 mins"
    totalText: str = ""

    #function for dynamically setting a text at the end to gather all of these into one narrative. Will be activated on button click.
    def setTotalText(self):
        self.totalText = (
            f"I am in the {self.designStep} phase of the service design process. "
            f"I am facilitating a(n) {self.location} experience for {self.numPeople} "
            f"person(s). This experience will take {self.time}"
        )

def index() -> rx.Component:    
    return rx.container(
        navbar(),
        rx.heading(
            "Service Design App",
            style={"text-align": "center"}  # Center the heading
        ),
        rx.vstack(
            rx.text(
                "I want to..."
            ),
            rx.select(
                ["Research","Visualize","Ideate","Prototype","Implement/Facilitate"], 
                value = appState.designStep, 
                on_change = appState.set_designStep,
                size = select_size 
            ),
            rx.text(
                "I want to facilitate this experience..."
            ),
            rx.select(
                ["In Person","Virtual","Unsure"], 
                value = appState.location,
                on_change = appState.set_location,
                size = select_size 
            ),
            rx.text(
                "This experience is for ... people"
            ),
            rx.select(
                ["1","2-5","6-10","10+"],
                value = appState.numPeople,
                on_change = appState.set_numPeople,
                size = select_size 
            ),
            rx.text(
                "Amount of time"
            ),
            rx.select(
                ["30 mins","1-2 hours","2+ hours"], 
                value = appState.time,
                on_change = appState.set_time,
                size = select_size 
            ),
            rx.button(
                "Update Text",
                on_click = appState.setTotalText,
                style = {"margin-top": "10px"}
            ),
            style={"margin": "20px"}  # You can adjust the value to set the desired spacing
        ),
        rx.text(
            appState.totalText
        ),
        # rx.button_group(
        #     button("Small Button",size = "sm"),
        #     button("Medium Button",size = "md"),
        #     button("Large Button",size = "lg"),
        #     space="1em"
        # )
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=["styles.css"]
)
app.add_page(index)
app.compile()
