from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score =1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.updatescore()
        
    def updatescore(self):    
        self.goto(-220, 260)
        self.write(f"Level:{self.l_score}", align='center', font=FONT)

    def game_over(self):    
        self.goto(0, 0)
        self.color('red')
        self.write("Game over", align='center', font=FONT)


    def l_point(self):
        self.l_score+=1
        self.clear()
        self.updatescore()

 
