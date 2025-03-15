from turtle import Turtle
from constants import LEFT_BARRIER

starting_ycor = -150
starting_xcor = (LEFT_BARRIER - 20)

class Barrier:
    def __init__(self):
        self.parts = []
        self.ycor = starting_ycor
        self.xcor = starting_xcor

    def create_barrier(self):
        for j in range(4):
            for i in range(4):  # Create 3 small squares per barrier
                part = Turtle()
                part.shape("square")
                part.color("green")
                part.penup()
                part.goto(self.xcor + (i * 20),
                          self.ycor)
                self.parts.append(part)
            self.xcor += 150

    def check_collision(self, bullet):
        """Remove part of the barrier if hit by a bullet."""
        for part in self.parts:
            if part.distance(bullet) < 20:  # Collision detection
                part.hideturtle()
                self.parts.remove(part)
                return True  # Bullet should disappear after hit
        return False

    def reset_barrier(self):
        self.parts.clear()
        self.xcor = starting_xcor
        self.ycor = starting_ycor

