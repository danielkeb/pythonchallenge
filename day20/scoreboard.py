from turtle import Turtle
FONT=("Courier", 24, "normal")
ALIGNMENT="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        self.color("white")
        self.goto(0,267)
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
        

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()