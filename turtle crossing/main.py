from time import sleep
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Score


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()

score = Score()
x = car = Car()
car_list = [x]


player = Player()
screen.onkey(player.move, "Up")

s = 0
game_on = True
while game_on:
    screen.update()
    if s % 6 == 0:
        x = car = Car()
        car_list.append(x)
        s = 0
    for car in car_list:
        car.move()
    sleep(score.difficulty)
    s += 1
    if player.ycor() > 300:
        score.update()
        player.reset()
    for car in car_list:
        if player.distance(car) < 20:
            score.end()
            game_on = False


screen.exitonclick()

