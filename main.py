import turtle
from turtle import Screen
import time

import player
from scoreboard import Scoreboard
import lives_manager
import enemies
from sound_manager import play_sound
from title_screen import TitleScreen

turtle.colormode(255)

screen = Screen()
screen.setup(800, 600)
screen.title("Space Invaders")
screen.bgpic("assets/background2.gif")
screen.tracer(0)


player = player.Player()
scoreboard = Scoreboard()
lives_manager = lives_manager.LivesManager()
enemy_manager = enemies.EnemyManager()

def exit_game():
    screen.bye()

def start_game():
    title_screen.clear_screen()
    game_over_screen.clear_screen()

    screen.listen()
    screen.onkey(fun=player.move_left, key="Left")
    screen.onkey(fun=player.move_right, key="Right")
    screen.onkey(fun=player.create_bullet, key="space")

    enemy_manager.create_enemies()

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
                if bullet.distance(enemy) < 20:
                    enemy.hideturtle()
                    enemy_manager.all_enemies.remove(enemy)
                    bullet.hideturtle()
                    player.bullets.remove(bullet)
                    scoreboard.add_score(1)
                    scoreboard.update_scoreboard()
                    break


        #create enemy bullets
        if not enemy_manager.bullets:
            enemy_manager.create_bullet()
        else:
            #detect collision with player
            if enemy_manager.bullets[0].distance(player) < 20:
                player.reset_player()
                lives_manager.update_lives(player.lives)
                time.sleep(1)
                screen.update()

        enemy_manager.shoot_bullets()

        # end game if player lives have depleted
        if player.lives == 0:
                game_is_on = False

        if not game_is_on:
            scoreboard.save_high_score()
            game_over_screen.show_title_screen()

def reset_game():
    player.lives = 3
    scoreboard.score = 0
    scoreboard.update_scoreboard()
    enemy_manager.reset_enemies()
    player.go_to_start()

    screen.update()

    start_game()

title_screen = TitleScreen(screen=screen, start_func=start_game, exit_func=exit_game,
                           text="SPACE INVADERS")

title_screen.show_title_screen()

game_over_screen = TitleScreen(screen=screen, start_func=reset_game, exit_func=exit_game, text="GAME OVER")

screen.mainloop()
