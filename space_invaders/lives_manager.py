from turtle import Turtle
from constants import FONT

ALIGNMENT = "Left"
POSITION = (-100, -280)

class LivesManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(POSITION)

    def update_lives(self, lives):
        self.clear()
        self.write(f"Lives: {lives}", align=ALIGNMENT, font=FONT)
