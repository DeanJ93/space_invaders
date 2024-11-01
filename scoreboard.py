from turtle import Turtle
import constants

ALIGNMENT = "center"
POSITION = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", align=ALIGNMENT, font=constants.FONT)