from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600, height= 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()  
food=Food()
score=Scoreboard()

screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.right,'Right')
screen.onkey(snake.left,'Left')


is_game_on=True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.refresh()
        
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -290 or snake.head.ycor() > 280:
        is_game_on=False
        score.game_over()

    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10 :
            
            is_game_on= False
            score.game_over()



screen.exitonclick()