from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.relocate()

    def relocate(self):
        self.hideturtle()
        self.goto(x=randrange(-280, 280, 10), y=randrange(-280, 280, 10))
        self.showturtle()
