STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    
    def up(self):
        if self.ycor()< FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)
