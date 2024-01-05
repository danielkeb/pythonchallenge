from turtle import  Turtle
MOVE_DISTANCE = 20
STARTING_POSITION=[(0, 0), (-20, 0), (-40,0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self, position):
            square=Turtle("square")
            square.color("white")
            square.penup()
            square.goto(position)
        
            self.segment.append(square)

    
    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]
        
    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            x_seg=self.segment[seg_num- 1].xcor()
            y_seg=self.segment[seg_num -1].ycor()
            self.segment[seg_num].goto(x_seg,y_seg)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
       

    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)
