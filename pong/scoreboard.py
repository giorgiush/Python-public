from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.score, align='center', font='10')
        self.score += 1

