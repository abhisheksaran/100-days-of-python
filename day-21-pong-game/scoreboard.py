import time
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.hideturtle()
        self.goto(pos)
        self.score = 0
        self.color('white')
        self.write("{}".format(self.score), False, align='center', font=('Courier', 50, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write("{}".format(self.score), False, align='center', font=('Courier', 50, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER. \nYour Score is: {}".format(self.score), False,
                   align='center', font=('Courier', 20, 'normal'))
        time.sleep(2)
        self.clear()
        self.write("Want to play again ?", False, align='center', font=('Courier', 20, 'normal'))


