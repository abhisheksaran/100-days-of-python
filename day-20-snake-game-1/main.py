from turtle import Screen
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

play_again = True
while play_again:
    snake = Snake()
    mouse = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.turn_left, 'Left')
    screen.onkey(snake.turn_right, 'Right')
    screen.onkey(snake.turn_up, 'Up')
    screen.onkey(snake.turn_down, 'Down')

    game_is_on = True
    while game_is_on:

        screen.update()
        time.sleep(.1)
        snake.move_forwards()

        # Detect collision with food
        if snake.head.distance(mouse) < 15:
            mouse.new_pos()
            scoreboard.update_score()
            snake.extend()

        # Detect collision with wall
        if snake.segments[0].xcor() < -290 or snake.segments[0].xcor() > 290 \
                or snake.segments[0].ycor() < -290 or snake.segments[0].ycor() > 290:
            scoreboard.game_over()
            game_is_on = False
            play_again = 'y' == screen.textinput("Play again", "type 'y' for yes")
            for turtle in screen.turtles():
                turtle.reset()
            break

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                scoreboard.game_over()
                game_is_on = False
                play_again = 'y' == screen.textinput("Play again", "type 'y' for yes")
                for turtle in screen.turtles():
                    turtle.reset()
                break

time.sleep(3)
screen.bye()
