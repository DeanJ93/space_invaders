from turtle import Turtle

TITLE_FONT = ("Arial", 24, "bold")
INSTRUCTIONS_FONT = ("Arial", 16, "normal")

class TitleScreen(Turtle):

    def __init__(self, screen, start_func, exit_func, title):
        super().__init__()
        self.screen = screen
        self.start_func = start_func
        self.exit_func = exit_func
        self.title = title
        self.penup()
        self.hideturtle()

    def show_title_screen(self):
        self.show_title()
        self.show_instructions()
        self.setup_listeners()

    def show_title(self):
        self.color("white")
        self.goto(0, 50)
        self.write(self.title, align="center", font=TITLE_FONT)

    def show_instructions(self):
        self.goto(0, -20)
        self.write("Press SPACE to start or 'q' to exit", align="center", font=INSTRUCTIONS_FONT)

    def setup_listeners(self):
        self.screen.listen()
        self.screen.onkey(self.start_func, "space")  # Call start_game() when SPACE is pressed
        self.screen.onkey(self.exit_func, "q")

    def clear_screen(self):
        self.clear()
