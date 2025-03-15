from turtle import Turtle

TITLE_FONT = ("Arial", 24, "bold")
INSTRUCTIONS_FONT = ("Arial", 16, "normal")

# A base class for screens
class GameScreen(Turtle):
    
    def __init__(self, screen, text):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.screen = screen
        self.text = text

    def show_text(self):
        self.color("white")
        self.goto(0, 50)
        self.write(self.text, align="center", font=TITLE_FONT)

    def clear_screen(self):
        self.clear()

class TitleScreen(GameScreen):

    def __init__(self, screen, start_func, exit_func, text):
        super().__init__(screen, text)
        self.start_func = start_func
        self.exit_func = exit_func

    def show_title_screen(self):
        self.show_text()
        self.show_instructions()
        self.setup_listeners()

    def show_instructions(self):
        self.goto(0, -20)
        self.write("Press SPACE to start or ESC to exit", align="center", font=INSTRUCTIONS_FONT)

    def setup_listeners(self):
        self.screen.listen()
        self.screen.onkey(self.start_func, "space")  # Call start_game() when SPACE is pressed
        self.screen.onkey(self.exit_func, "Escape")
