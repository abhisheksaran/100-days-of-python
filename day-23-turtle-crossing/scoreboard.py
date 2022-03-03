from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-240, 250)
        self.write('Level:{}'.format(self.level), False, align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write('Level:{}'.format(self.level), False, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align='Center', font=FONT)

