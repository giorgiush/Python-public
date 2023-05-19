from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(y=-280, x=0)

    def move(self):
        self.fd(10)

    def reset(self):
        self.goto(y=-280, x=0)
