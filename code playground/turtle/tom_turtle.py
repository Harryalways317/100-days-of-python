from turtle import Turtle,Screen

tom_the_turtle = Turtle()
tom_the_turtle.shape("turtle")
tom_the_turtle.color("red")
tom_the_turtle.pencolor("blue")
def square():
    for i in range(0,4):
        tom_the_turtle.forward(100)
        tom_the_turtle.right(90)
def dashed_line(length):
    for i in range(0,steps=5,length=10):
        tom_the_turtle.forward(steps)
        tom_the_turtle.pendown()
        tom_the_turtle.forward(steps)
        tom_the_turtle.penup()

screen = Screen()
screen.exitonclick()