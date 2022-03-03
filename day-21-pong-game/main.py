import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=800)
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))


screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

score_r = Scoreboard((50, 350))
score_l = Scoreboard((-50, 350))
next_throw_right = True
ball_speed = .1
while score_l.score < 10 and score_r.score < 10:
    # print("next lap")
    ball = Ball(next_throw_right)

    game_is_on = True
    while game_is_on:
        ball.move()
        time.sleep(.05)
        screen.update()

        # Detect collision of ball with upper and lower walls
        if ball.ycor() > 390 or ball.ycor() < -390:
            ball.setheading(360-ball.heading())
            # print("walls")

        # Detect collision of ball with paddles
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 440) or (ball.distance(l_paddle) < 50 and ball.xcor() < -440) :
            if ball.heading() <= 180:
                # print(ball.heading())
                ball.setheading(180-ball.heading())
                # print(ball.heading())
            else:
                # print(ball.heading())
                ball.setheading(540-ball.heading())
                # print(ball.heading())
            # print("paddles")

        # Detect ball which passed without touching right peddle
        if ball.xcor() > 510:
            ball.reset()
            score_l.update_score()
            next_throw_right = False
            game_is_on = False
            # print("right paddle")

        # Detect ball which passed without touching left peddle
        if ball.xcor() < -510:
            ball.reset()
            score_r.update_score()
            next_throw_right = True
            game_is_on = False
            # print("left paddle")
    ball_speed = ball_speed * .9
    time.sleep(ball_speed)

    # print("start next lap")

screen.exitonclick()