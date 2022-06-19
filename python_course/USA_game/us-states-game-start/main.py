from turtle import Screen, Turtle
import pandas

data = pandas.read_csv("python_course/USA_game/us-states-game-start/50_states.csv")
states = data.state.to_list()

win = Screen()
pen = Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
win.title("U.S. States Game")
win.bgpic("python_course/USA_game/us-states-game-start/blank_states_img.gif")
win.setup(width=725, height=491)

correct = 0
checked = []

while correct != 50:
    answer = win.textinput(title=f"{correct}/50 States Correct", prompt="What's another state name?").title()
    if answer == "Exit":
        break
    if answer in states and answer not in checked:
        checked.append(answer)
        correct += 1
        info = data[data["state"]==answer]
        pen.goto(int(info.x), int(info.y))
        pen.write(answer, align="center")

missed = []
for state in states:
    if state not in checked:
        missed.append(state)

states_to_learn = pandas.DataFrame({
    "Missed":missed
})

print(states_to_learn)

states_to_learn.to_csv("python_course/USA_game/us-states-game-start/states_to_learn.csv")

win.mainloop()