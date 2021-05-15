from turtle import Turtle, position
ALIGNMENT = "center"
FONT = ("Arial", 24, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            print(file.read())
            self.high_score = int(file.read())
        super().__init__()
        self.penup()
        self.goto(0,270)
        self.pendown()
        self.hideturtle()
        self.color("white")
        #self.write(f"Scoreboard: 0",move=False, align=ALIGNMENT, font=FONT)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score},Highscore: {self.high_score}",move=False, align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(self.high_score)
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",move=False,align=ALIGNMENT , font= FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()
        