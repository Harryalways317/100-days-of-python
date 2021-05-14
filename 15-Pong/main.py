from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
screen.listen()


rightPaddle = Paddle("right")
leftPaddle = Paddle("left")
ball = Ball()
rightScoreboard = ScoreBoard("right")
leftScoreboard = ScoreBoard("left")
#screen.update()
screen.onkey( leftPaddle.up, "w")
screen.onkey( leftPaddle.down, "s")
screen.onkey( rightPaddle.up, "Up")
screen.onkey( rightPaddle.down, "Down")

game_is_on = True



while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move()
    
    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with Paddle
    if (ball.distance(rightPaddle) < 50 and ball.xcor() > 320) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #collision with out of bounds Right
    if ball.distance(rightPaddle) > 50 and ball.xcor() > 380:
        leftScoreboard.increase_score()
        ball.goto(0,0)
    #collision with out of bounds Left
    if ball.distance(leftPaddle) > 50 and ball.xcor() < -380:
        rightScoreboard.increase_score()
        ball.goto(0,0)




screen.exitonclick()