from tkinter.scrolledtext import ScrolledText
from turtle import Screen, screensize
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen_size = screensize()
    print('####################')
    print(screen_size)
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
    #collision with wall
    if snake.head.xcor() >  280 or snake.head.xcor() < -280 or snake.head.ycor() >  280 or snake.head.xcor() < -280:
        scoreboard.reset()
        snake.reset()
    
    #collision with tail
    for segment in snake.segments[1:]:   #dont cross the head as head is the first element
        if snake.head.distance(segment) < 10 :
            scoreboard.reset()
            snake.reset()


screen.exitonclick()