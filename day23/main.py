import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

turtle= Player()
cary =CarManager()
score= Scoreboard()
screen.listen()

screen.onkey(turtle.go_up,"Up")
screen.onkey(turtle.right_side, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cary.create_cars()
    cary.move_cars()

    #detect collision with cars
    for car in cary.all_cars:
        if car.distance(turtle) < 20:  

            game_is_on =False
            score.game_over()
    if turtle.is_finished_line():
        turtle.go_to_start()
        cary.level_up()
        score.l_point()


    #detect collision 
screen.exitonclick()

