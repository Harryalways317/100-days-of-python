import turtle
import pandas
screen = turtle.Screen()
image = "indiamap.gif"
screen.addshape(image)
screen.title("Indian States Game")
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv()


turtle.mainloop()
screen.exitonclick()
