from turtle import Turtle,Screen
import random
trim=Turtle()
colours = ["red", "green", "darkgreen", "DeepSkyBlue","wheat","orange","CornflowerBlue"]
directions = [0, 90, 180, 270]
trim.pensize(15)
trim.speed('fastest')
for _ in range(200):
    trim.color(random.choice(colours))
    trim.forward(30)
    trim.setheading(random.choice(directions))




scr=Screen()
scr.exitonclick()