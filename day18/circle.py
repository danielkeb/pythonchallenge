import turtle as t
screen=t.Screen()
import random
trim=t.Turtle()
t.colormode(255)
trim.speed("fastest")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color
def draw_spinography(size_of_gap):
    for _ in range(int(360 / size_of_gap)):

        trim.color(random_color())
        trim.circle(100)
        current_heading=trim.heading()
        trim.setheading(current_heading + size_of_gap)
        trim.circle(100)
draw_spinography(5)

screen.exitonclick()





