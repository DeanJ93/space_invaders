import turtle
from turtle import Turtle
import bullet
import constants
import winsound

SPACESHIP_IMAGE = "assets/spaceship2.gif"
STARTING_POSITION = (0, constants.BOTTOM_BARRIER)

turtle.register_shape(SPACESHIP_IMAGE)
bullet_manager = bullet.BulletManager()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SPACESHIP_IMAGE)
        self.go_to_start()
        self._lives = 3
        self.bullets = bullet_manager.all_bullets
        self.shoot_speed = 60

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_left(self):
        if self.xcor() > constants.LEFT_BARRIER:
            self.backward(10)

    def move_right(self):
        if self.xcor() < constants.RIGHT_BARRIER:
            self.forward(10)

    def create_bullet(self):
        winsound.PlaySound('assets/sounds/348164__djfroyd__laser-one-shot-1.wav', winsound.SND_ASYNC)
        bullet_manager.create_bullet(ycor=self.ycor() + 30, xcor=self.xcor())

    def shoot_bullets(self):
        for b in self.bullets:
            b.forward(self.shoot_speed)

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        if lives > 0:
            self._lives = lives

    def decrement_lives(self):
        if self.lives > 0:
            self._lives -= 1

