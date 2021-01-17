from tkinter import *

class data:
    player = ""
    o = set()
    x = set()

def check_win():
    win=[{0,11,22},{1,11,21},{2,11,20},{10,11,12},{1,2,0},{20,21,22},{0,10,2,0},{2,12,22}]
    for i in win:
        if data.o in i:
            print("o win")
        elif data.x in i:
            print("x win")
def click(event):
    i,j = event.widget.position
    if data.player == "o":
        text = Label(master=window,text = "o",font = ("Pixeboy",80),fg = "blue")
        text.grid(row=i, column=j)
        data.player = "x"
        round.configure(text="x")
        a = int(str(i)+str(j))
        data.o.add(a)
    else:
        text = Label(master=window, text="x",font = ("Pixeboy",80),fg = "red")
        text.grid(row=i, column=j)
        data.player = "o"
        round.configure(text="o")
        a = int(str(i) + str(j))
        data.x.add(a)
    check_win()

def new_game(size=3):
    for i in range(size):
        for j in range(size):
            bt = Button(master=window, width=size*bt_size,height = size*bt_size)
            bt.grid(row = i, column = j)
            bt.position = (i,j)
            bt.bind("<Button-1>",click)

window = Tk()
bt_size = 5
window.title("tic tac toe")
data = data()
data.player = "o"
round = Label(master=window,text = "o",font = ("Pixeboy",80))
round.grid(row=0, column=3)
new_game()
window.mainloop()
