
import tkinter
from unicodedata import name

win = tkinter.Tk()
win.title("My first GUI")
win.minsize(width=500,height=300)
text= tkinter.Label(text="Harry")
text.pack()
def click_me():
    text["text"] = "i got clicked"
    text.config(text= input.get())


input = tkinter.Entry()
input.pack()
button = tkinter.Button(text= "click me",command=click_me)
button.pack()
win.mainloop()