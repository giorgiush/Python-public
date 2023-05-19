import turtle
import random
screen = turtle.Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "purple", "blue", "green"]
turtles = ["red", "orange", "purple", "blue", "green"]
speed = [1, 20, 10, 15, 0, 5]
distance = [0, 0, 0, 0, 0]
finishline = []
choice = screen.textinput("Choose your turtle", "red/orange/purple/blue/green")

x = -100
for i in range(5):
    turtles[i] = turtle.Turtle()
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-230, x)
    x += 50

while len(finishline) < 5:
    for i in range(5):
            s = random.choice(speed)
            turtles[i].fd(s)
            distance[i] += s
            if distance[i] >= 400:
                finishline.append(turtles[i])
if finishline[0] == choice:
    screen.textinput("YOU WIN", "message to your turtle:")
else:
    screen.textinput("YOU LOSE", "message to your turtle:")


screen.exitonclick()