import turtle

import pandas as pd
screen=turtle.Screen()
screen.title("U.S. State Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

screen.setup(width=700,height=800)

data=pd.read_csv("50_states.csv")
all_states= data.state.to_list() 

guessed_states=[]
print(guessed_states)
while len(guessed_states) < 50:
    answer_state= screen.textinput(title=f"{len(guessed_states)}/50 Guessed correct", prompt="What's another state's name?r").title()
    if answer_state =='Exit':
        missing_states=[stat for stat in all_states if stat not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        mss=pd.DataFrame(missing_states)
        mss.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state == answer_state]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    

myguss=pd.DataFrame(guessed_states)
myguss.to_csv('guessed_states.csv')

