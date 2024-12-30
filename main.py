from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
paddle1 = Paddle((370, 0))
paddle2 = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong game")
paddle1.move_paddle("Up", "Down")
paddle2.move_paddle("w", "s")
screen.tracer(0)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle1) < 60 and ball.xcor() > 340:
        ball.bounce_paddle()

    if ball.distance(paddle2) < 60 and ball.xcor() < -340:
        ball.bounce_paddle()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()








screen.exitonclick()