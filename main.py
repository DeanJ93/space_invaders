import turtle
from turtle import Turtle, Screen
import player
import scoreboard
import lives_manager
import time
import enemies
import threading

turtle.colormode(255)

screen = Screen()
screen.setup(800, 600)
screen.title("Space Invaders")
screen.bgpic("assets/background2.gif")
screen.tracer(0)

player = player.Player()
scoreboard = scoreboard.Scoreboard()
lives_manager = lives_manager.LivesManager()
enemy_manager = enemies.EnemyManager()

screen.listen()
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.create_bullet, key="space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    lives_manager.update_lives(player.lives)
    enemy_manager.move_enemies()

    #Shoots player's bullets up the screen
    player.shoot_bullets()

    #detect bullet collision with enemy
    for bullet in player.bullets:
        for enemy in enemy_manager.all_enemies:
            if bullet.distance(enemy) < 5:
                print("bullet hit")
                print(f"Bullet pos = {bullet.pos()}")
                print(f"Enemy pos = {enemy.pos()}")
                break


    #create enemy bullets
    # screen.ontimer(enemy_manager.create_bullet, 10000)
    # enemy_manager.shoot_bullets()


screen.mainloop()
