from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('white')
screen.title('Turtle Crossing Game ')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True


# Function to detect collision of turtle with cars
def collision(turtle_player, cars):
    for car in cars:
        if turtle_player.distance(car) < 20:
            return True
    return False


while game_is_on:
    for i in range(5):
        time.sleep(.1)
        screen.update()

        # Collision
        if collision(player, car_manager.cars):
            scoreboard.game_over()
            game_is_on = False
            break

        # Detect when current level is passed
        if player.ycor() > 280:
            scoreboard.level_up()
            car_manager.level_up()
            player.level_up()

        car_manager.move_cars()
    car_manager.add_random_car()

screen.exitonclick()
