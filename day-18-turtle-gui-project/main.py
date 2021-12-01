from turtle import Turtle, Screen
import random
t = Turtle()
t.shape("turtle")
t.pensize(15)
t.speed(0)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
dirs = [0, 90, 180, 270]
for i in range(1000):
    t.color(random.choice(colours))
    t.setheading(random.choice(dirs))
    t.forward(30)


screen = Screen()
screen.exitonclick()
