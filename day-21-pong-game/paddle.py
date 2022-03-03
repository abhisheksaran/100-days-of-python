from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, pos):
        self.penup()
        self.goto(pos)
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.speed(0)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)



