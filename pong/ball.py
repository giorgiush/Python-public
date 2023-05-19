from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.mspeed = 0.1

    def move(self):
        self.goto(x=self.xcor() + self.x, y=self.ycor() + self.y)
        if int(self.ycor()) >= 280 or int(self.ycor()) <= -280:
            self.y *= -1

    def bounce(self):
        self.x *= -1
        self.mspeed *= 0.8


    def reset(self):
        self.home()
        self.bounce()
        self.mspeed = 0.1




