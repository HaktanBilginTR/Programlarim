



from tkinter import *
import tkinter.messagebox
import time


anapencere=Tk()
anapencere.title("Hesap Makinesi")
anapencere.geometry('{}x{}'.format(244,78 ))
#######################
def karealma(x):
    try:
        x = int(x)
        p=x*x

        return tkinter.messagebox.showinfo("Sonuç","Sonucunuz : %s"%p)
    except ValueError:
        tkinter.messagebox.showerror("Hata","Hata Oluştu")
def ucgensorgulama(a,b,c):
    try:
        if (a+b)>c and(a+c)>b and (c+b)>a and (a-b)<c and (a-c)<b and (c-b)<a:
            tkinter.messagebox.showinfo("Sonuç","Bu Bir Üçgendir!")
            return
        else:
            tkinter.messagebox.showinfo("Sonuç","Bu Bir Üçgen Değildir!")
            return
    except ValueError:
        print("Lütfen Birdaha Deneyin")

def pisagor(a,b):
    try:
        a = int(a)
        b = int(b)
        p=a*a+b*b
        import math
        sqr=math.sqrt(p)
        sqr=float(sqr)
        return tkinter.messagebox.showinfo("Sonuç","Sonucunuz : %s"%sqr)
    except ValueError:
        tkinter.messagebox.showerror("Hata","Bir Hata Oluştu")
def faktoriel(sayi):
    faktor = 1
    try:
        sayi = int(sayi)
        if sayi <= 0:
            print("Negatif Olmayan Sayı Giriniz.")
            return
        else:
            for i in range(1,sayi+1):
                faktor = faktor * i

            tkinter.messagebox.showinfo("Sonuç" , "Sonucunuz : %s"%faktor)
            return
    except ValueError:
        tkinter.messagebox.showerror("Hata","Hata Oluştu")

def getalkh():
    x = entryKh.get()
    karealma(x)


    return
def getalfh():
    sayi = entryFh.get()
    faktoriel(sayi)

    return
def getalus():
    a = entryUs.get()
    b = entryUs2.get()
    c = entryUs3.get()
    ucgensorgulama(a,b,c)

    return
def getalpb():
    a = entryPb.get()
    b = entryPb2.get()
    pisagor(a,b)

    return



def KHTK():
    global Kh
    Kh=Tk()
    Kh.title("Kare Hesaplama")
    global entryKh
    entryKh=Entry(Kh)
    entryKh.grid(row=1 , column= 1)
    butonkhtk = Button(Kh,text="Al",command=getalkh)
    butonkhtk.grid(row=3 , column = 1)
    Kh.geometry('{}x{}'.format(125, 50))



    Kh.mainloop()
def FHTK():
    global Fh
    Fh=Tk()
    Fh.title("Faktöriyel Hesaplama")
    global entryFh
    entryFh=Entry(Fh)
    entryFh.grid(row=1 , column= 1)
    butonfhtk = Button(Fh,text="Al",command=getalfh)
    butonfhtk.grid(row=3, column=1)
    Fh.geometry('{}x{}'.format(125, 50))

def USTK():
    global Us
    Us = Tk()
    Us.title("Üçgen Sorgulama")
    global entryUs
    global entryUs2
    global entryUs3
    entryUs = Entry(Us)
    entryUs2 = Entry(Us)
    entryUs3 = Entry(Us)
    entryUs.grid(row=1 , column = 1)
    entryUs2.grid(row=2 , column = 1)
    entryUs3.grid(row=3 , column = 1)
    butonustk = Button(Us,text="Al",command = getalus)
    butonustk.grid(row=4 , column = 1)
    Us.geometry('{}x{}'.format(125, 100))

def PBTK():
    global Pb
    Pb= Tk()
    Pb.title("Pisagor Bağıntısı")
    global entryPb
    global entryPb2
    entryPb = Entry(Pb)
    entryPb2 = Entry(Pb)
    entryPb.grid(row = 1 , column = 1)
    entryPb2.grid(row= 2 , column= 1)
    butonpbtk = Button(Pb,text="Al",command=getalpb)
    butonpbtk.grid(row=4,column=1)
    Pb.geometry('{}x{}'.format(125, 75))

def DORT():
    DOTK = Tk()
    kasa = []
    def alan_guncelle(sayi):
        icerik = hesap_alani.get() + sayi
        hesap_alani.delete(0, END)
        hesap_alani.insert(0, icerik)
        return icerik

    def islem_yap(islem):
        icerik = hesap_alani.get()

        if len(kasa) == 0:
            kasa.append(alan_guncelle(""))
            kasa.append(islem)
            hesap_alani.delete(0, END)
        #        print(kasa)
        elif icerik == "" and len(kasa) == 2 and (islem == "+" or islem == "*" or islem == "-" or islem == "/"):
            kasa[1] = islem
            hesap_alani.delete(0, END)
        elif icerik != "" and len(kasa) == 2 and (islem == "+" or islem == "*" or islem == "-" or islem == "/"):
            sayi1, sayi2 = float(kasa[0]), float(icerik)
            if islem == "+":
                sonuc = sayi1 + sayi2
            elif islem == "-":
                sonuc = sayi1 - sayi2
            elif islem == "*":
                sonuc = sayi1 * sayi2
            elif islem == "/":
                if sayi2 != 0 or sayi2 != 00 or sayi2 != 000:
                    sonuc = sayi1 / sayi2
                else:
                    sonuc = sayi2
                    print(" Sıfra Bölme Hatası")
            kasa[0], kasa[1] = str(sayi2), islem
            hesap_alani.delete(0, END)

            hesap_alani.insert(0, sonuc)
            print(kasa)
            return sonuc
        if islem == "=":
            return sonuc_goster(islem_yap(kasa[1]))



    def sonuc_goster(sayi):
        hesap_alani.delete(0, END)
        hesap_alani.insert(0, sayi)
        time.sleep(2)

    hesap_alani = Entry(DOTK)
    hesap_alani.insert(0, "")
    hesap_alani.grid(row=0, columnspan=5)

    buton_01 = Button(DOTK, text="1", command=lambda: alan_guncelle(str(1)))
    buton_01.grid(row=1, column=0)
    buton_02 = Button(DOTK, text="2", command=lambda: alan_guncelle(str(2)))
    buton_02.grid(row=1, column=1)
    buton_03 = Button(DOTK, text="3", command=lambda: alan_guncelle(str(3)))
    buton_03.grid(row=1, column=2)
    buton_topla = Button(DOTK, text="+", command=lambda: islem_yap(str("+")))
    buton_topla.grid(row=1, column=3)
    buton_esittir = Button(DOTK, text="=", command=lambda: islem_yap(str("=")))
    buton_esittir.grid(rowspan=4, column=4, sticky=W + E + N + S)

    buton_04 = Button(DOTK, text="4", command=lambda: alan_guncelle(str(4)))
    buton_04.grid(row=2, column=0)
    buton_05 = Button(DOTK, text="5", command=lambda: alan_guncelle(str(5)))
    buton_05.grid(row=2, column=1)
    buton_06 = Button(DOTK, text="6", command=lambda: alan_guncelle(str(6)))
    buton_06.grid(row=2, column=2)
    buton_cikart = Button(DOTK, text="-", command=lambda: islem_yap(str("-")))
    buton_cikart.grid(row=2, column=3)

    buton_07 = Button(DOTK, text="7", command=lambda: alan_guncelle(str(7)))
    buton_07.grid(row=3, column=0)
    buton_08 = Button(DOTK, text="8", command=lambda: alan_guncelle(str(8)))
    buton_08.grid(row=3, column=1)
    buton_09 = Button(DOTK, text="9", command=lambda: alan_guncelle(str(9)))
    buton_09.grid(row=3, column=2)
    buton_carp = Button(DOTK, text="*", command=lambda: islem_yap(str("*")))
    buton_carp.grid(row=3, column=3)

    buton_0 = Button(DOTK, text="0", command=lambda: alan_guncelle(str("0")))
    buton_0.grid(row=4, column=0)
    buton_00 = Button(DOTK, text="00", command=lambda: alan_guncelle(str("00")))
    buton_00.grid(row=4, column=1)
    buton_000 = Button(DOTK, text="000", command=lambda: alan_guncelle(str("000")))
    buton_000.grid(row=4, column=2)
    buton_bol = Button(DOTK, text="/", command=lambda: islem_yap(str("/")))
    buton_bol.grid(row=4, column=3)




#########################




buton1=Button(anapencere,command= KHTK)
buton2=Button(anapencere,command=FHTK)
buton3=Button(anapencere,command=USTK)
buton4=Button(anapencere,command=PBTK)
buton5=Button(anapencere,command=DORT)




buton1.config(text="Kare Hesaplama", width=16)
buton2.config(text="Faktöriyel Hesaplama", width=16)
buton3.config(text="Üçgen Sorgulama", width=16)
buton4.config(text="Pisagor Bağıntısı", width=16)
buton5.config(text="Dört İşlem",width= 34)


buton1.grid(row = 0 , column = 0)
buton2.grid(row = 0 , column = 1)
buton3.grid(row = 1 , column = 0)
buton4.grid(row = 1 , column = 1)
buton5.grid(row= 2 , columnspan=2)







anapencere.mainloop()