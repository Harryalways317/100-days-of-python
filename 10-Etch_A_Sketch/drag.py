import turtle
tim = turtle.Turtle()
screen = turtle.Screen()
listener = turtle.listen()



def forward():
    tim.forward(10)
def backward():
    tim.back(10)
def left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)
def right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


turtle.onkey(fun = forward , key = "w")
turtle.onkey(fun = backward , key = "s")
turtle.onkey(fun = left , key = "a")
turtle.onkey(fun = right , key = "d")
turtle.onkey(fun = clear , key = "c")
screen.exitonclick()