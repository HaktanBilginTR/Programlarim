sirax=1
from tkinter import *
import tkinter.messagebox
anapencere = Tk()
anapencere.geometry("177x168")





buton1 = Button(anapencere,width=7,height=3)
def buton11():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton1.config(text="X")
        sirax=0
    else:
        buton1.config(text="O")
        sirax=1
    return sirax
buton1.config(command=buton11)
buton2 = Button(anapencere,width=7,height=3)
def buton22():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton2.config(text="X")
        sirax=0
    else:
        buton2.config(text="O")
        sirax=1
    return sirax
buton2.config(command=buton22)
buton3 = Button(anapencere,width=7,height=3)
def buton33():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton3.config(text="X")
        sirax=0
    else:
        buton3.config(text="O")
        sirax=1
    return sirax
buton3.config(command=buton33)
buton4 = Button(anapencere,width=7,height=3)
def buton44():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton4.config(text="X")
        sirax=0
    else:
        buton4.config(text="O")
        sirax=1
    return sirax
buton4.config(command=buton44)
buton5 = Button(anapencere,width=7,height=3)
def buton55():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton5.config(text="X")
        sirax=0
    else:
        buton5.config(text="O")
        sirax=1
    return sirax
buton5.config(command=buton55)
buton6 = Button(anapencere,width=7,height=3)
def buton66():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton6.config(text="X")
        sirax=0
    else:
        buton6.config(text="O")
        sirax=1
    return sirax
buton6.config(command=buton66)
buton7 = Button(anapencere,width=7,height=3)
def buton77():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton7.config(text="X")
        sirax=0
    else:
        buton7.config(text="O")
        sirax=1
    return sirax
buton7.config(command=buton77)
buton8 = Button(anapencere,width=7,height=3)
def buton88():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton8.config(text="X")
        sirax=0
    else:
        buton8.config(text="O")
        sirax=1
    return sirax
buton8.config(command=buton88)
buton9 = Button(anapencere,width=7,height=3)
def buton99():
    global sirax
    sirax=sirax
    if sirax == 1:
        buton9.config(text="X")
        sirax=0
    else:
        buton9.config(text="O")
        sirax=1
    return sirax
buton9.config(command=buton99)



buton1.grid(row=0,column=0)
buton2.grid(row=0,column=1)
buton3.grid(row=0,column=2)
buton4.grid(row=1,column=0)
buton5.grid(row=1,column=1)
buton6.grid(row=1,column=2)
buton7.grid(row=2,column=0)
buton8.grid(row=2,column=1)
buton9.grid(row=2,column=2)
def x_win():
    if buton1["text"]=="X" and buton2["text"]=="X" and buton3["text"] =="X":
        return True
    elif buton4["text"] == "X" and buton5["text"] == "X" and buton6["text"] =="X":
        return True
    elif buton7["text"] == "X" and buton8["text"] == "X" and buton9["text"] =="X":
        return True
    elif buton1["text"] == "X" and buton5["text"] == "X" and buton9["text"] =="X":
        return True
    elif buton3["text"] == "X" and buton5["text"] == "X" and buton7["text"] =="X":
        return True
    elif buton1["text"] == "X" and buton4["text"] == "X" and buton7["text"] =="X":
        return True
    elif buton2["text"] == "X" and buton5["text"] == "X" and buton8["text"] =="X":
        return True
    elif buton3["text"] == "X" and buton6["text"] == "X" and buton9["text"] =="X":
        return True
def o_win():
    if buton1["text"] =="O" and buton2["text"]=="O" and buton3["text"] =="O":
        return True
    elif buton4["text"] == "O" and buton5["text"] == "O" and buton6["text"]=="O":
        return True
    elif buton7["text"] == "O" and buton8["text"] == "O" and buton9["text"] == "O":
        return True
    elif buton1["text"] == "O" and buton5["text"] == "O" and buton9["text"]=="O":
        return True
    elif buton3["text"] == "O" and buton5["text"] == "O" and buton7["text"]=="O":
        return True
    elif buton1["text"] == "O" and buton4["text"] == "O" and buton7["text"]=="O":
        return True
    elif buton2["text"] == "O" and buton5["text"] == "O" and buton8["text"]=="O":
        return True
    elif buton3["text"] == "O" and buton6["text"] == "O" and buton9["text"]=="O":
        return True

while True:
    if x_win() == True:
        tkinter.messagebox.showinfo("Tebrikler!","X Kazandı !!!")
        anapencere.mainloop()
    if o_win() == True:
        tkinter.messagebox.showinfo("Tebrikler!","O Kazandı !!!")
        anapencere.mainloop()
    anapencere.mainloop()
    continue








