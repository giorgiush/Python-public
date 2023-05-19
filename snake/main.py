from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

screen.listen()

food = Food()

scoreboard = Scoreboard()

snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snakes[0].distance(food) <= 15:
        food.relocate()
        scoreboard.wrt()
        snake.grow()
    elif int(snake.snakes[0].xcor()) <= -300 or int(snake.snakes[0].xcor()) >= 300 or int(snake.snakes[0].ycor()) <= -300 or int(snake.snakes[0].ycor()) >= 300:
        game_on = False
        scoreboard.over()
    for i in snake.snakes[1:]:
        if snake.snakes[0].distance(i) < 10:
            scoreboard.over()
            game_on = False


screen.exitonclick()


