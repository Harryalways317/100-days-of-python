import imp
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,type):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.x_move = 20
        self.y_move = 20
        if type.lower() == "right":
            self.setpos(360,0)
        if type.lower() == "left":
            self.setpos(-360,0)

    def up(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)
    
    

