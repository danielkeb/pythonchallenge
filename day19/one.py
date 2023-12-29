from turtle import Turtle, Screen

tim=Turtle()

screen=Screen()

def mov_forward():
    tim.forward(10)


def mov_backward():
    tim.backward(10)



def turn_left():
    new_heading=tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading=tim.heading() - 10
    tim.setheading(new_heading)


def mov_up():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

 
    

screen.listen()
screen.onkey(mov_forward, 's') 
screen.onkey(turn_left, 'l') 
screen.onkey(turn_right, 'r') 
#screen.onkey(clear, 'c') 
screen.onkey(key='Left',fun=mov_backward)
screen.onkey(key='Up',fun=mov_up)
screen.exitonclick()
clear()