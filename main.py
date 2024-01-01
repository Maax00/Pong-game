from turtle import Turtle, Screen
from scoreboard import Score_Board
from paddle import Right_Paddle, Left_Paddle
from prep import draw_field
from ball import Ball
import time

GAME_SPEED = 0.05
WIDTH = 1000
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Welcome to PONG")
screen.tracer(0)

right_score = Score_Board(location=(100, 240))
left_score = Score_Board(location=(-200, 240))
field = draw_field()
right_paddle = Right_Paddle()
left_paddle = Left_Paddle()
ball = Ball()

screen.listen()
screen.onkey(right_paddle.r_up, "o")
screen.onkey(right_paddle.r_down, "l")
screen.onkey(left_paddle.l_up, "w")
screen.onkey(left_paddle.l_down, "s")

game_on = True
while game_on:
    time.sleep(GAME_SPEED)
    screen.update()
    ball.move()
    if abs(ball.ycor()) > 260:
        ball.bounce()
    if ball.distance(right_paddle) < 40 and ball.xcor() > 420:
        ball.bounce_x()
        GAME_SPEED *= 0.9
    if ball.distance(left_paddle) < 40 and ball.xcor() < -420:
        ball.bounce_x()
        GAME_SPEED *= 0.9

    if ball.xcor() < -470:
        right_score.score_right()
        ball.ball_reset()
        GAME_SPEED = 0.05

    if ball.xcor() > 470:
        left_score.score_left()
        ball.ball_reset()
        GAME_SPEED = 0.05

screen.exitonclick()
