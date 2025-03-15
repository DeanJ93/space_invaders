from turtle import Turtle
import os

import constants

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ALIGNMENT = "center"
POSITION = (0, 260)
HIGH_SCORE_FILE = os.path.join(SCRIPT_DIR, "high_score.txt")
FONT = ('Arial', 25, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self._score = 0
        self._high_score = 0
        self.set_high_score()
        self.pencolor("white")
        self.hideturtle()
        self.goto(POSITION)
        self.update_scoreboard()

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score >= 0:
            self._score = score

    def add_score(self, points):
        if points > 0:
            self._score += points

    def set_high_score(self):
        try:
            # Read the existing high score
            with open(HIGH_SCORE_FILE) as file:
                content = file.read().strip()
                self._high_score = int(content) if content else 0  # Handle empty file
        except FileNotFoundError:
            self._high_score = 0  # Default if file doesn't exist

        # Update high score if the current score is higher
        if self.score > self._high_score:
            self._high_score = self.score
            with open(HIGH_SCORE_FILE, "w") as file:
                file.write(str(self._high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self._score}      High Score: {self._high_score}", align=ALIGNMENT, font=constants.FONT)

    def save_high_score(self):
        self.set_high_score()