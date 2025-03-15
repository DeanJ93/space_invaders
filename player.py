import turtle
from turtle import Turtle
import bullet
import constants
from sound_manager import play_sound
import os

SPACESHIP_IMAGE = os.path.join("assets", "images", "spaceship2.gif")
STARTING_POSITION = (0, constants.BOTTOM_BARRIER)
shoot_sound = os.path.join("assets","sounds","348164__djfroyd__laser-one-shot-1.wav")

turtle.register_shape(SPACESHIP_IMAGE)
bullet_manager = bullet.BulletManager()


class Player(Turtle):
    explosion_sound = os.path.join("assets","sounds","medium-explosion-40472.mp3")

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(SPACESHIP_IMAGE)
        self.go_to_start()
        self._lives = 5
        self.bullets = bullet_manager.all_bullets
        self.shoot_speed = 40

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_left(self):
        if self.xcor() > constants.LEFT_BARRIER:
            self.backward(10)

    def move_right(self):
        if self.xcor() < constants.RIGHT_BARRIER:
            self.forward(10)

    def create_bullet(self):
        if len(self.bullets) == 0:
            play_sound(shoot_sound)
            bullet_manager.create_bullet(ycor=self.ycor() + 30, xcor=self.xcor())

    def shoot_bullets(self):
        for b in self.bullets:
            b.forward(self.shoot_speed)

    def reset_player(self):
        self.go_to_start()
        self.decrement_lives()
        play_sound(sound_file=self.explosion_sound)

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

