from turtle import Turtle,Screen

tom_the_turtle = Turtle()
tom_the_turtle.shape("turtle")
tom_the_turtle.color("red")
tom_the_turtle.pencolor("blue")
for i in range(0,4):
    tom_the_turtle.forward(100)
    tom_the_turtle.right(90)

screen = Screen()
screen.exitonclick()