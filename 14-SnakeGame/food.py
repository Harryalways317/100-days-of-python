from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circular")
        self.penup()
        self.shapesize(strech_len = 0.5,strech_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x,rand_y)
        
        food.goto(random.randint(0, 200),random.randint(0, 200))
