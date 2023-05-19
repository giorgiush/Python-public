from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        self.side = side
        super().__init__()
        self.create("fastest", "white", "square", 1, 5)

    def create(self, speed, color, shape, width, length):
        self.speed(speed)
        self.color(color)
        self.shape(shape)
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.penup()
        self.setheading(90)
        if self.side == "right":
            self.goto(x=350, y=0)
        else:
            self.goto(x=-350, y=0)

    def up(self):
        if int(self.ycor()) <= 220:
            self.fd(50)

    def down(self):
        if int(self.ycor()) >= -220:
            self.bk(50)
