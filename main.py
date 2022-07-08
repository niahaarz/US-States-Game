from label import Label
import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S States Game")
image = "test.gif"
screen.addshape(image)
turtle.shape(image)

test_label = Label()
states = pd.read_csv('50_states.csv')
states_list = states['state'].to_list()

guessed_states = []


while len(guessed_states) < 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states found", prompt="What's another state name?").title()

    if answer_state == 'Exit':
        missing_states = [state for state in states_list if state not in guessed_states]
        results_df = pd.DataFrame(missing_states)
        results_df.to_csv('results.csv', mode='w')
        break
        
    if answer_state in states_list and answer_state not in guessed_states:

        guessed_states.append(answer_state)
        indiv_state = states[states.state == answer_state]
        position = (int(indiv_state.x), int(indiv_state.y))
        area_label = answer_state
        test_label.create_label(position, area_label)




screen.exitonclick()