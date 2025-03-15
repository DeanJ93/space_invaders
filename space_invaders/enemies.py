from turtle import Turtle
import random
import turtle
import os

import constants
import bullet

ALIEN_IMAGE = os.path.join("assets","images", "alien.gif")
turtle.register_shape(ALIEN_IMAGE)
starting_xcor = -150
starting_ycor = 150
MOVE_SPEED = 1

bullet_manager = bullet.BulletManager()
bullet_manager.move_direction = -90
bullet_manager.bullet_color = "green"

class EnemyManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.all_enemies = []
        self.hideturtle()
        self.ycor = starting_ycor
        self.xcor = starting_xcor
        #self.speed("slowest")
        self.move_direction = 180
        self.shoot_positions = []
        self.bullets = bullet_manager.all_bullets
        self.shoot_speed = 40

    def create_enemies(self):
        for x in range(1,56):
            new_enemy = Turtle()
            new_enemy.penup()
            new_enemy.start_x = self.xcor  # Store original x position
            new_enemy.start_y = self.ycor  # Store original y position
            new_enemy.shape(ALIEN_IMAGE)
            new_enemy.goto(x=self.xcor, y=self.ycor)
            self.xcor += 35
            if x % 11 == 0:
                self.ycor -= 35
                self.xcor = starting_xcor
            self.all_enemies.append(new_enemy)

    def move_enemies_down(self):
        for e in self.all_enemies:
            # enemies will stop moving down before getting to close to player.
            if e.ycor() > (constants.BOTTOM_BARRIER + 80):
                y = e.ycor()
                y -= 40
                e.sety(y)

    def move_enemies(self):
        if len(self.all_enemies) > 0:
            for enemy in self.all_enemies:
                enemy.setheading(self.move_direction)
                enemy.forward(MOVE_SPEED)
                if enemy.xcor() == constants.LEFT_BARRIER:
                    self.move_direction = 0
                if enemy.xcor() == constants.RIGHT_BARRIER:
                    # move all enemies down
                    self.move_enemies_down()
                    self.move_direction = 180


    def create_bullet(self):
        # random_chance = random.randint(1,11)
        # if random_chance == 1:
        if self.all_enemies:
            random_position = random.choice(self.all_enemies[-11:])
            bullet_manager.create_bullet(ycor=random_position.ycor(), xcor=random_position.xcor())


    def shoot_bullets(self):
        for b in self.bullets:
            b.forward(self.shoot_speed)

            if b.pos()[1] < -300:
                self.bullets.remove(b)

    def reset_enemies(self):
        self.ycor = starting_ycor
        self.xcor = starting_xcor
        if len(self.all_enemies) > 0:
            for e in self.all_enemies:
                e.hideturtle()
            self.all_enemies.clear()



