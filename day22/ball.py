from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")

        self.color("purple")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0,0)
        self.refresh()
        self.y_move= 10
        self.x_move =10
        

    def refresh(self):
        new_y= self.ycor() + self.y_move
        new_x= self.xcor() + self.x_move
        
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1