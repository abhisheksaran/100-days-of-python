from turtle import Turtle, Screen
import random
t = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
race_is_on = False
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter the color: ")
colors = ['red', 'green', 'blue']
turtles = []
for i in range(3):
    t = Turtle()
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y= -100+i*100)
    turtles.append(t)

if user_bet:
    race_is_on=True

while race_is_on :
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("Hey, you won the bet!!")
            else:
                print("Hey, you lost the bet, the winning color is {}.".format(winning_color))

screen.exitonclick()

