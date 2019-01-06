sirax=1
from tkinter import *
anapencere = Tk()
anapencere.geometry("177x168")

def x_win():
    if yazi1["text"]=="X" and yazi2["text"]=="X" and yazi3["text"] =="X":
        return print("a")
    elif yazi4["text"] == "X" and yazi5["text"] == "X" and yazi6["text"] =="X":
        return print("a")
    elif yazi7["text"] == "X" and yazi8["text"] == "X" and yazi9["text"] =="X":
        return print("a")
    elif yazi1["text"] == "X" and yazi5["text"] == "X" and yazi9["text"] =="X":
        return print("a")
    elif yazi3["text"] == "X" and yazi5["text"] == "X" and yazi7["text"] =="X":
        return print("a")
    elif yazi1["text"] == "X" and yazi4["text"] == "X" and yazi7["text"] =="X":
        return print("a")
    elif yazi2["text"] == "X" and yazi5["text"] == "X" and yazi8["text"] =="X":
        return print("a")
    elif yazi3["text"] == "X" and yazi6["text"] == "X" and yazi9["text"] =="X":
        return print("a")
def o_win():
    if yazi1["text"] =="O" and yazi2["text"]=="O" and yazi3["text"] =="O":
        return print("b")
    elif yazi4["text"] == "O" and yazi5["text"] == "O" and yazi6["text"]=="O":
        return print("b")
    elif yazi7["text"] == "O" and yazi8["text"] == "O" and yazi9["text"] == "O":
        return print("b")
    elif yazi1["text"] == "O" and yazi5["text"] == "O" and yazi9["text"]=="O":
        return print("b")
    elif yazi3["text"] == "O" and yazi5["text"] == "O" and yazi7["text"]=="O":
        return print("b")
    elif yazi1["text"] == "O" and yazi4["text"] == "O" and yazi7["text"]=="O":
        return print("b")
    elif yazi2["text"] == "O" and yazi5["text"] == "O" and yazi8["text"]=="O":
        return print("b")
    elif yazi3["text"] == "O" and yazi6["text"] == "O" and yazi9["text"]=="O":
        return print("b")



buton1 = Button(anapencere,width=7,height=3)
def buton11():
    global sirax
    sirax=sirax
    buton1.destroy()
    global yazi1
    yazi1=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:
        sirax=0
    else:
        yazi1.config(text="O")

        sirax=1



    yazi1.grid(row=0,column=0)
    return sirax
buton1.config(command=buton11)
buton2 = Button(anapencere,width=7,height=3)
def buton22():
    global sirax
    sirax=sirax
    buton2.destroy()
    global yazi2
    yazi2=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax=0
    else:
        yazi2.config(text="O")

        sirax=1
    yazi2.grid(row=0,column=1)
    return sirax
buton2.config(command=buton22)
buton3 = Button(anapencere,width=7,height=3)
def buton33():
    global sirax
    sirax=sirax
    buton3.destroy()
    global yazi3
    yazi3=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax=0
    else:
        yazi3.config(text="O")
        sirax=1

    yazi3.grid(row=0,column=2)
    return sirax
buton3.config(command=buton33)
buton4 = Button(anapencere,width=7,height=3)
def buton44():
    global sirax
    sirax=sirax
    buton4.destroy()
    global yazi4
    yazi4=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax=0

    else:
        yazi4.config(text="O")

        sirax=1
    yazi4.grid(row=1,column=0)
    return sirax
buton4.config(command=buton44)
buton5 = Button(anapencere,width=7,height=3)
def buton55():
    global sirax
    sirax=sirax
    buton5.destroy()
    global yazi5
    yazi5=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax=0
    else:
        yazi5.config(text="O")

        sirax=1
    yazi5.grid(row=1,column=1)
    return sirax
buton5.config(command=buton55)
buton6 = Button(anapencere,width=7,height=3)
def buton66():
    global sirax
    sirax=sirax
    buton6.destroy()
    global yazi6
    yazi6=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:
        sirax=0
    else:
        yazi6.config(text="O")

        sirax=1
    yazi6.grid(row=1,column=2)
    return sirax
buton6.config(command=buton66)
buton7 = Button(anapencere,width=7,height=3)
def buton77():
    global sirax
    sirax=sirax
    buton7.destroy()
    global yazi7
    yazi7=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax = 0
    else:
        yazi7.config(text="O")

        sirax=0
    yazi7.grid(row=2,column=0)
    return sirax
buton7.config(command=buton77)
buton8 = Button(anapencere,width=7,height=3)
def buton88():
    global sirax
    sirax=sirax
    buton8.destroy()
    global yazi8
    yazi8=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax=0
    else:
        yazi8.config(text="O")

        sirax=1
    yazi8.grid(row=2,column=1)
    return sirax
buton8.config(command=buton88)
buton9 = Button(anapencere,width=7,height=3)
def buton99():
    global sirax
    sirax=sirax
    buton9.destroy()
    global yazi9
    yazi9=Label(anapencere,text="X",font=("Courier",35))
    if sirax == 1:

        sirax=0
    else:
        yazi9.config(text="O")

        sirax=1
    yazi9.grid(row=2,column=2)
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
















anapencere.mainloop()











































