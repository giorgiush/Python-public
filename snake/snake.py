from turtle import Turtle

class Snake():

    def __init__(self):
            self.snakes = []
            self.cor = 0
            for _ in range(3):
               self.create()

    def create(self):
        self.snake = Turtle()
        self.snake.penup()
        self.snake.shape("square")
        self.snake.color("white")
        self.snake.speed("fastest")
        self.snake.goto(x=self.cor, y=0)
        self.cor -= 20
        self.snakes.append(self.snake)
    def grow(self):
        self.snake = Turtle()
        self.snake.penup()
        self.snake.shape("square")
        self.snake.color("white")
        self.snake.speed("fastest")
        self.snake.goto(self.snakes[-1].position())
        self.snakes.append(self.snake)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
                    x = self.snakes[i - 1].xcor()
                    y = self.snakes[i - 1].ycor()
                    self.snakes[i].goto(x, y)
        self.snakes[0].fd(20)
