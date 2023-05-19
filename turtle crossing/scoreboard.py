from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        self.difficulty = 0.1
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(x=-260, y=260)
        self.pendown()
        self.update()

    def update(self):
        self.clear()
        self.write(self.level, align='center', font='10')
        self.level += 1
        self.difficulty *= 0.9

    def end(self):
        self.penup()
        self.home()
        self.pendown()
        self.write("GAME OVER", align='center', font='100')

