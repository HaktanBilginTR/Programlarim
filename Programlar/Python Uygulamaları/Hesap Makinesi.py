###############Functions
def karealma(x):
    try:
        x = int(x)

        p=x*x

        return print("Sayınız :",p)
    except ValueError:
        print("Lütfen Birdaha Deneyin")
def ucgensorgulama(a,b,c):
    try:
        if (a+b)>c and(a+c)>b and (c+b)>a and (a-b)<c and (a-c)<b and (c-b)<a:
            print("Bu bir üçgendir.")
            return
        else:
            print("Bu bir üçgen değildir.")
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
        return print("3. Kenar :",sqr)
    except ValueError:
        print("Lütfen Birdaha Deneyin")
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
            print("Faktöriyeliniz:", faktor)
            return
    except ValueError:
        print("Lütfen Birdaha Deneyin")
##############################
print("Kare Hesaplama İçin : Kh\nFaktoriyel Hesaplama İçin : Fh\nÜçgen Sorgulama İçin : Üs\nPisagor Bağıntısı Bulma İçin : Pb\n4 İşlem İçin : İş ")
while True:
    v = input()
    while v == "Kh":
        x = input("Karesini Almak İstediğiniz Sayıyı Girin :")
        karealma(x)
        import time
        time.sleep(1)
        print("Kare Hesaplama İçin : Kh\nFaktoriyel Hesaplama İçin : Fh\nÜçgen Sorgulama İçin : Üs\nPisagor Bağıntısı Bulma İçin : Pb\n4 İşlem İçin : İş Yazınız")
        v= None
        x = None
        p = None
        break
    while v == "Fh":
        sayi = input("Sayı Giriniz :")
        faktoriel(sayi)
        import time
        time.sleep(1)
        print("Kare Hesaplama İçin : Kh\nFaktoriyel Hesaplama İçin : Fh\nÜçgen Sorgulama İçin : Üs\nPisagor Bağıntısı Bulm İçin : Pb\n4 İşlem İçin : İş Yazınız")
        v = None
        sayi = None
        faktor = None
        i = None
        break
    while v == "Üs":
        a = input("1. Kenar :")
        b = input("2. Kenar :")
        c = input("3. Kenar :")
        ucgensorgulama(a, b, c)
        import time
        time.sleep(1)
        print("Kare Hesaplama İçin : Kh\nFaktoriyel Hesaplama İçin : Fh\nÜçgen Sorgulama İçin : Üs\nPisagor Bağıntısı Bulma İçin : Pb\n4 İşlem İçin : İş Yazınız")
        v =None
        a= None
        b= None
        p= None
        sqr = None
        break
    while v == "Pb":
        a = input("1. Kenar :")
        b = input("2. Kenar :")
        pisagor(a, b)
        import time
        time.sleep(1)
        print("Kare Hesaplama İçin : Kh\nFaktoriyel Hesaplama İçin : Fh\nÜçgen Sorgulama İçin : Üs\nPisagor Bağıntısı Bulma İçin : Pb\n5 İşlem İçin : İş Yazınız")
        v = None
        break
    while v == "İş":
        d = 1
        a = input("1. Sayıyı Giriniz:")
        c = input("Yapacağınız İşlemi Seçiniz:")
        b = input("2. Sayıyı Giriniz:")
        if a == int and b == int and c == int:
            print("Adam Gibi Bir Şey Yaz Lan!")
        elif c == "+":
             d = int(a) + int(b)
             print("Sonuç :", d)
        elif c == "-":
             d = int(a) - int(b)
             print("Sonuç :", d)
        elif c == "*":
             d = int(a) * int(b)
             print("Sonuç :", d)
        elif c == "/":
             d = int(a) / int(b)
             print("Sonuç :", d)
        a = None
        c = None
        b = None
        d = None
        v = None
        import time
        time.sleep(1)
        print("Kare Hesaplama İçin : Kh\nFaktoriyel Hesaplama İçin : Fh\nÜçgen Sorgulama İçin : Üs\nPisagor Bağıntısı Bulma İçin : Pb\n4 İşlem İçin : İş Yazınız")
        break