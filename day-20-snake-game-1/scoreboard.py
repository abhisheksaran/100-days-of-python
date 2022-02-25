import time
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 280)
        self.score = 0
        self.color('white')
        self.write("Score: {}".format(self.score), False, align='center', font=('Courier', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score), False, align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER. \nYour Score is: {}".format(self.score), False,
                   align='center', font=('Courier', 20, 'normal'))
        time.sleep(2)
        self.clear()
        self.write("Want to play again ?", False, align='center', font=('Courier', 20, 'normal'))


