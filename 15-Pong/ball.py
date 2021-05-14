from re import S
from turtle import Turtle
import random
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        #self.shapesize(stretch_len=10,stretch_wid=10)
        #self.setheading(random.randint(145,215))
        
        
        
        
    def move(self):
        #self.forward(5)
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)


    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        
        self.x_move *= -1
        self.move_speed = self.move_speed - self.move_speed*0.2
    
    def reset_pos(self):
        self.goto(0,0)
        self.move_speed = 0.1
        time.sleep(0.1)
        
