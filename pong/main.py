from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_border()

    if ball.xcor() > 320 and r_paddle.distance(ball) < 50 or ball.xcor() < -320 and l_paddle.distance(ball) < 50:
        ball.paddle_bounce()

    if ball.xcor() > 440:
        ball.reset()
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()

    if ball.xcor() < -440:
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
