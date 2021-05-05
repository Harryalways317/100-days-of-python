from turtle import Screen,Turtle
screen = Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")

pos = [-40,-20,0]
snake = []
for i in range(3):
    a_snake = Turtle(shape="square")
    a_snake.penup()
    a_snake.color("white")
    a_snake.goto(pos[i],0)
    snake.append(a_snake)





screen.exitonclick()