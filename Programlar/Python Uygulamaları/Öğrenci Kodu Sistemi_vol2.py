from tkinter import *
import tkinter.messagebox
def sss():
    global a
    a=str(giris1.get())
    b=str(giris2.get())
    c=str(giris3.get())
    try:
        m = ((int(a)) - (len(a)) + (int(a) * int(a)) // (int(3) + (int(b)) * (int(c) + int(16))))+1000

    except ValueError :
        tkinter.messagebox.showerror("Hata","Lütfen Bir Daha Giriniz")
        giris1.delete(0,END)
        giris2.delete(0,END)
        giris3.delete(0,END)

    try:

        tkinter.messagebox.showinfo("Öğrenci Kodu Sistemi", "Giriş Kodunuz : %s" % m)
        anapencere.quit()
    except UnboundLocalError:
        print("")


anapencere=Tk()
yazi1 = Label (text = "Öğrenci Numaranızı Giriniz :")
yazi2 = Label (text = "Kimlik Numaranızın İlk Rakamı :")
yazi3 = Label (text = "Kimlik Numaranızın Son Rakamı :")
anapencere.title("Öğrenci Kodu Sistemi")

anapencere.resizable(width=False, height=False)
anapencere.geometry('{}x{}'.format(357, 94))
yazi1.grid(row = 0  ,column = 1)
yazi2.grid(row = 1  ,column = 1)
yazi3.grid(row = 2  ,column = 1)




giris1=Entry(anapencere)
giris2=Entry(anapencere)
giris3=Entry(anapencere)
giris1.grid(row = 0 ,column = 3)
giris2.grid(row = 1 ,column = 3)
giris3.grid(row = 2 ,column = 3)

buton=Button(anapencere)
buton.config(text="Devam!")
buton.config(command=sss)
buton.grid(row = 4 , column = 3)
anapencere.mainloop()