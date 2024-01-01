from turtle import Screen, Turtle
from createpaddle import Paddle
from ball import Ball
import time
screen=Screen()
screen.title("pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on= True

while is_game_on:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    time.sleep(0.1)
    screen.update()
    ball.refresh()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()