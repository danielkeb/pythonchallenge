from turtle import Screen, Turtle
from createpaddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.title("pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


ball = Ball()
scoreboard= Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on= True

while is_game_on:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
#detect collisions
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()