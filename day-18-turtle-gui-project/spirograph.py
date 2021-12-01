import  turtle as tur
tur.colormode(255)
import random
t = tur.Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for i in range(36):
    t.color(random_color())
    t.setheading(i*10)
    t.circle(50)

screen = Screen()
screen.exitonclick()
