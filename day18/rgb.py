import turtle as t
import random
trim=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color



directions = [0, 90, 180, 270]
trim.pensize(15)
trim.speed('fastest')
for _ in range(200):
    trim.color(random_color())
    trim.forward(30)
    trim.setheading(random.choice(directions))





