from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.listen()
screen.tracer(0)

ball = Ball()

rscore = Score((100, 250))
lscore = Score((-100, 250))

rpaddle = Paddle("right")
lpaddle = Paddle("left")


screen.onkeypress(rpaddle.up, "Up")
screen.onkeypress(rpaddle.down, "Down")
screen.onkeypress(lpaddle.up, "w")
screen.onkeypress(lpaddle.down, "s")


game = True
while game:
    screen.update()
    sleep(ball.mspeed)
    ball.move()
    if ball.distance(rpaddle) < 50 and ball.xcor() >= 330 or ball.distance(lpaddle) < 50 and ball.xcor() <= -330:
        ball.bounce()
    if ball.xcor() > 400:
        ball.reset()
        rscore.update_score()
        sleep(1)
    if ball.xcor() < -400:
        ball.reset()
        lscore.update_score()
        sleep(1)


screen.exitonclick()
