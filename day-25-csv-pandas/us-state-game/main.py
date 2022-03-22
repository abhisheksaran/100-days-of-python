import turtle
import pandas
import time
from pandas.errors import InvalidIndexError

t = turtle.Turtle()
t.hideturtle()
screen = turtle.Screen()
screen.title("U.S. State games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < len(all_states):
    screen.update()
    time.sleep(.1)
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(all_states)}", prompt="What's another state?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        state_data = data[data["state"] == answer_state]
        # print(state_data)
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)
    else:
        print("No uch State or State already guessed.")


