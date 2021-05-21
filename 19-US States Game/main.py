import turtle
import pandas
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US States Game")
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
print(data)
states = data['states'].to_list()
x_coods = data['x'].to_list()
y_coods = data['y'].to_list()

found = 0
while found!= len(data):
    answer_state = screen.textinput(title="Guess The State",prompt="Ehat's another state name")

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)



turtle.mainloop()
screen.exitonclick()