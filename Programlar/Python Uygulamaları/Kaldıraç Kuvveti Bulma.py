from tkinter import *
import tkinter.messagebox
anapencere = Tk()                                   #yük x yük kolu = kuvvet x kuvvet kolu
anapencere.geometry("250x98")
anapencere.title("Kaldıraç Kuvveti Bulma")
anapencere.resizable(width=False,height=False)
yazi = Label(anapencere,text="Kuvvet Kolu")
yazi2 = Label(anapencere,text="Yük")
yazi3 = Label(anapencere,text="Yük Kolu")
entiri = Entry(anapencere)
entiri2 = Entry(anapencere)
entiri3 = Entry(anapencere)
def getentiri():
    global kuvvetkolu,yuk,yukkolu
    kuvvetkolu = int(entiri.get())
    yuk = int(entiri2.get())
    yukkolu = int(entiri3.get())
    yuktoplam =  yuk * yukkolu
    m= yuktoplam/kuvvetkolu
    tkinter.messagebox.showinfo("Sonuç","Kuvvet : %s"%m)


batin = Button(anapencere,text="Devam",command=getentiri)
yazi.grid(row=0,column=0)
yazi2.grid(row=1,column=0)
yazi3.grid(row=2,column=0)
entiri.grid(row=0,column=1)
entiri2.grid(row=1,column=1)
entiri3.grid(row=2,column=1)
batin.grid(row = 3 , column = 3)




































anapencere.mainloop()


























