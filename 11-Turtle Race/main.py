from turtle import Turtle,Screen
import random
screen = Screen()

screen.screensize(canvwidth=480,canvheight=360)
all_turtles = []
colors = ['red','blue','green','yellow','orange']
y_cood = [-80,-40,0,40,80]

for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setposition(-350,y_cood[i])
    all_turtles.append(new_turtle)
user_bet = screen.textinput('place your bet', 'Which color will reaches finish line first')


if user_bet.lower() in colors:
    is_race_on = True
else:
    is_race_on = False
    print("Wrong color entered")


while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 290:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()