from turtle import Turtle


class BulletManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_bullets = []
        self.ycor = 0
        self.xcor = 0
        self.bullet_color = "red"
        self.move_direction = 90

    def create_bullet(self, ycor, xcor):
        self.xcor = xcor
        self.ycor = ycor
        new_bullet = Turtle("circle")
        new_bullet.penup()
        new_bullet.color(self.bullet_color)
        new_bullet.shapesize(0.3,0.3)
        new_bullet.goto(self.xcor, self.ycor)
        new_bullet.setheading(self.move_direction)
        self.all_bullets.append(new_bullet)

    def remove_bullet(self, bullet):
        bullet.hideturtle()
        self.all_bullets.remove(bullet)


