import turtle
import pandas

screen = turtle.Screen()
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
screen.title("US Guessing Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")

score = 0
guessed_list = []
full_list = data.state.to_list()
new_list = []

while score != 50:
    answer = screen.textinput(title=f"Guess the state  {score}/50", prompt="What is another state's name?").title()

    if answer == "Exit":
        break

    for a in data.state:

        if answer == a:
            guessed_list.append(a)
            score += 1
            x_cord = data.loc[data["state"] == a, "x"].values[0]
            y_cord = data.loc[data["state"] == a, "y"].values[0]

            tim.goto(x_cord, y_cord)
            tim.write(a, move=True, font=("Arial", 10, "normal"))

new_list = [n for n in full_list if n not in guessed_list]

with open("Unguessed.txt", "a") as file:
    for x in new_list:
        file.write(f"{x}\n")
