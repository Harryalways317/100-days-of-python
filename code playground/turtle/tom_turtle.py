from turtle import Turtle,Screen
import random
tom_the_turtle = Turtle()
tom_the_turtle.shape("turtle")
tom_the_turtle.color("red")
tom_the_turtle.pencolor("blue")
def square():
    for i in range(0,4):
        tom_the_turtle.forward(100)
        tom_the_turtle.right(90)
def dashed_line(steps=5,length=10):
    for i in range(0,length):
        tom_the_turtle.forward(steps)
        tom_the_turtle.pendown()
        tom_the_turtle.forward(steps)
        tom_the_turtle.penup()
def draw_poly(sides):
    for i in range(2,sides):
        angle = 360 / i
        sides = i
        for j in range(i):
            tom_the_turtle.forward(40)
            tom_the_turtle.right(angle)

def random_walk():
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    directions = [0, 90, 180, 270]
    tom_the_turtle.pensize(15)
    tom_the_turtle.speed("fastest")

    for _ in range(200):
        tom_the_turtle.color(random.choice(colours))
        tom_the_turtle.forward(30)
        tom_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()