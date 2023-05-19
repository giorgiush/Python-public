from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US State Guessing Game")
screen.addshape("./day_25_US_States/blank_states_img.gif")
screen.setup(width=730, height=500)

turtle = Turtle()
turtle.shape("./day_25_US_States/blank_states_img.gif")

writer = Turtle()
writer.speed("fastest")
writer.hideturtle()

def write(state, coordinates):
    writer.penup()
    writer.goto(coordinates)
    writer.pendown()
    writer.write(state, align="center")

def get_states_list():
   data = pandas.read_csv("./day_25_US_States/50_states.csv")
   return data["state"].to_list()

def get_coordinates():
    data = pandas.read_csv("./day_25_US_States/50_states.csv")
    x_cor = data["x"].to_list()
    y_cor = data["y"].to_list()
    list = []
    for i in range(50):
        list.append((x_cor[i], y_cor[i]))
    return list


states_list = get_states_list()
coordinates_list = get_coordinates()
guessed_list = []

x = 0
while x < 50:
    guess = (screen.textinput(title=f"{x}/50 Guessed", prompt="Guess the State")).title()
    if guess in states_list and guess not in guessed_list:
        cor = coordinates_list[states_list.index(guess)]
        write(state=guess, coordinates=cor)
        guessed_list.append(guess)
        x += 1
    else:
        print("try again")


screen.exitonclick()