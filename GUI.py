from tkinter import *
window=Tk()
def pri():
    username = name.get()
    print(username)
button=Button(window,text="click",command=pri)
button.place(x=100,y=100)
name = Entry(window)
name.place(x=100,y=50)

window.mainloop()
