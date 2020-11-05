import random
from tkinter import *


def check():
    user = int(box1.get())
    if user<num:
        text1.configure(text="น้อยไป")
    elif user>num:
        text1.configure(text="มากไป")
    elif user==num:
        text1.configure(text="win!!!")
    else:
        text1.configure(text="error")


num = random.randint(0,20)


window = Tk()
window.minsize(400,200)
text1 = Label(window,text="")
text1.pack()
box1 = Entry(window)
box1.pack()
button1 = Button(window,text="click",command=check)
button1.pack()
text2 = Label(window,text="")
text2.pack()
window.mainloop()