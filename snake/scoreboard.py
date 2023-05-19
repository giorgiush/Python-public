from turtle import Turtle


def high_score():
    with open("high_score.txt", mode="r") as file:
        return file.read()


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = high_score()
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.speed("fastest")
        self.penup()
        self.goto(x=-120, y=260)
        self.pendown()
        self.wrt()

    def wrt(self):
        self.clear()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", align='left', font='6')
        self.score += 1

    def over(self):
        self.home()
        self.write(f"GAME OVER", align='center', font='10')
        if int(high_score()) < self.score - 1:
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.score - 1}")
