import turtle
from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
for i in range(4):
    timmy.fd(50)
    timmy.right(90)
my_screen = Screen()
my_screen.exitonclick()
