from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, throw_right):
        super().__init__()

        self.create_ball(throw_right)

    def create_ball(self, throw_right):
        self.penup()
        self.shape('circle')
        # shapesize(2, 2)
        self.color('red')

        if throw_right:
            self.setheading(random.randint(-60, 60))
        else:
            self.setheading(random.randint(120, 240))
        # self.move((350, 0))

    def move(self):
        self.forward(20)

