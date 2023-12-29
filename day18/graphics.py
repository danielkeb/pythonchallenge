from turtle import Turtle,Screen
import random
trim=Turtle()
# for _ in range(15):
#     trim.forward(10)
#     trim.penup()
#     trim.forward(10)
#     trim.pendown()
colours = ["red", "green", "darkgreen", "DeepSkyBlue","white", "orange","CornflowerBlue"]
def draw_shape(number_side):
    number_angles = 360 / number_side
    for _ in range(number_side):
        trim.forward(100)
        trim.right(number_angles)

for shape_in_angles in range(3, 11):
    trim.color(random.choice(colours))

    draw_shape(shape_in_angles)






scr=Screen()
scr.exitonclick()