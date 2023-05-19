from turtle import Turtle
from random import choice

COLORS = ("red", "orange", "blue", "green", "purple")
POSITION = []
for i in range(-240, 241, 60):
    POSITION.append(i)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.spawn()

    def spawn(self):
        y = [range(-250, 251, 10)]
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.goto(x=300, y=choice(POSITION))
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move(self):
        self.setpos(x=self.xcor()-10, y=self.ycor())

