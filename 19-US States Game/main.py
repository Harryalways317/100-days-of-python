import turtle
import pandas
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US States Game")
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(data)
all_states = data['state'].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",prompt="What's another state name").title()
    if answer_state == "Exit":
        remaining_states = [state for state in all_states if state not in guessed_states]
        remaining_states_dict = {"missed_states":remaining_states}
        with open("answers.csv",'w') as answer_file:
            df = pandas.DataFrame(remaining_states_dict)
            answer_file.write(df.to_csv())
        t = turtle.Turtle()
        t.goto(0,0)
        t.write("see the answers in csv")
        turtle.exitonclick()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        guessed_states.append(state_data.state.item())
        t.write(state_data.state.item())

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)



turtle.mainloop()
screen.exitonclick()