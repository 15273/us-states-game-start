import turtle
import pandas
m = "med"
m.lower()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
screen.setup(height=491, width=725)
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 Guess the State",
                                    prompt="What's another state's name?r").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        print(missing_state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





