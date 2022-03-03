from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.add_random_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_random_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape('square')
        car.shapesize(1, 2)
        car.goto(-280, random.randint(-250, 250))
        car.speed(1)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
