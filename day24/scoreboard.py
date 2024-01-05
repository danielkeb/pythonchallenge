from turtle import Turtle


FONT=("Courier", 24, "normal")
ALIGNMENT="center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        with open("./day24/data.txt") as data:
            self.high_score= int(data.read())
        self.color("white")
        self.goto(0,267)
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score:{self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./day24/data.txt", "w") as highscore:
                highscore.write(f"{self.high_score}")
        
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)
        

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()