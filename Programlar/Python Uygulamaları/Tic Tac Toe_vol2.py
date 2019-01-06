from tkinter import *
import tkinter.messagebox
anapencere = Tk()
click = True
def berabere():
    if b1['text'] != '' and b2['text'] != '' and b3['text'] != ''and b4['text'] != ''and b5['text'] != ''and b6['text'] != ''and b7['text'] != ''and b8['text'] != ''and b9['text'] != '':
        return True
def ttt(buttons):
    global click
    if buttons["text"] == ""and click == True:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == "" and click == False:
        buttons["text"] = "O"
        click = True
    if(b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X" or
         b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X" or
         b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X" or
         b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X" or
         b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X" or
         b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X" or
         b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X" or
         b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X"):
         tkinter.messagebox.showinfo("Tebrikler!","X Kazandı !!!")
         anapencere.quit()
    elif(b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O" or
         b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O" or
         b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O" or
         b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O" or
         b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O" or
         b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O" or
         b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O" or
         b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O"):
         tkinter.messagebox.showinfo("Tebrikler!","O Kazandı !!!")
         anapencere.quit()
    elif berabere() == True:
         tkinter.messagebox.showinfo("Berabere !", "Berabere !!!")
         anapencere.quit()
b1 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b1))
b2 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b2))
b3 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b3))
b4 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b4))
b5 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b5))
b6 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b6))
b7 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b7))
b8 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b8))
b9 = Button(anapencere,text="",height=3,width=7,command=lambda:ttt(b9))
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
anapencere.mainloop()