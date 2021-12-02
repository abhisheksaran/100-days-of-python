from turtle import Turtle, Screen
t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_right():
    new_heading = t.heading()-10
    t.setheading(new_heading)

def turn_left():
    new_heading = t.heading()+10
    t.setheading(new_heading)

def turn_clockwise():
    t.right(10)

def turn_anticlockwise():
    t.left(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(key="l", fun=turn_right)
screen.onkey(key="h", fun=turn_left)
screen.onkey(key="k", fun=move_forwards)
screen.onkey(key="j", fun=move_backwards)
screen.onkey(key="a", fun=turn_clockwise)
screen.onkey(key="d", fun=turn_anticlockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
