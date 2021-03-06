from turtle import Turtle, position
ALIGNMENT = "center"
ALIGNMENT_LEFT = "left"
ALIGNMENT_RIGHT = "right"
FONT = ("Arial", 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self,type):
        self.score = 0
        super().__init__()
        self.penup()
        if type.lower() == "right":
            self.goto(200,260)
        if type.lower() == "left":
            self.goto(-200,260)
        
        self.pendown()
        self.hideturtle()
        self.color("white")
        self.write(f"Scoreboard: 0",move=False, align=ALIGNMENT, font=FONT)
        
        
    def scoreboard(self):
        self.write(f"Scoreboard: {self.score}",move=False, align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",move=False,align=ALIGNMENT , font= FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.scoreboard()
    
    
        