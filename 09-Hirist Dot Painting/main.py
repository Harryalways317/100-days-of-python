from turtle import Turtle,colormode,Screen
import random
# import colorgram

# colors = colorgram.extract("09-Hirist Dot Painting/1.jpg", 10)
# rgb_colors = [i.rgb for i in colors]
# rgb_tuple = [tuple(i) for i in rgb_colors]
# print(rgb_tuple)

#10x10 rows of spots
# spots around 20 in size
#space around 50 in size

color_list = [(206, 45, 79), (8, 61, 119), (82, 255, 184),(249, 181, 172),(27, 154, 170),(255, 180, 0),(205, 193, 207),(161, 205, 241),(188, 74, 20), (56, 34, 13), (156, 34, 113), (149, 26, 9), (37, 22, 77), (24, 31, 60), (224, 31, 160),(113, 167, 210), (45, 85, 143), (27, 21, 238)]
timmy = Turtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
colormode(255)
for i in range(10):
    for j in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
    
    timmy.backward(500)
    timmy.left(90)
    timmy.forward(50)
    timmy.right(90)
timmy.hideturtle()
screen = Screen()
screen.exitonclick()