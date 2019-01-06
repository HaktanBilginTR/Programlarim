def materyaller():
    global sesliler,sayac,liste,harfsayi,sessizharf,sayilar,sessizliste,sayiliste
    sesliler = ["e""u""ı""o""ü""a""i""ö"]
    sayac = 0
    harfsayi = 0
    sessizharf=0
    sayilar = 0
    liste = []
    sessizliste = []
    sayiliste = []
def kelimesor():
    global kelime
    kelime = str(input("Yazıyı Giriniz Giriniz :"))
def ikili():
    materyaller()
    kelimesor()
def tara():
    for harf in kelime:
        if harf == "e" or harf == "u" or harf == "ı" or harf == "o" or harf == "ü" or harf == "a" or harf == "i" or harf == "ö" or harf == "E" or harf == "U" or harf == "I" or harf == "O" or harf == "Ü" or harf == "A" or harf == "İ" or harf == "Ö":
            global sayac
            sayac+=1
            liste.append(harf)
        elif harf == "1" or harf == "2" or harf == "3" or harf == "4" or harf == "5" or harf == "6" or harf == "7" or harf == "8" or harf == "9" or harf == "0":
            global sayilar
            sayilar+=1
            sayiliste.append(harf)
        else:
            global sessizharf
            sessizharf+=1
            sessizliste.append(harf)
        global harfsayi
        harfsayi+=1
    return sayac
def ekranabas():
    print("*****************************\nYazı",harfsayi,"Harflidir\nYazı İçerisinde",sayac,"Adet Sesli Harf Vardır Ve Bunlar\n",liste,"'Dir\nYazı İçerisinde",sessizharf,"Adet Sessiz Harf Vardır Ve Bunlar\n",sessizliste,"'Dir\nYazı İçerisinde",sayilar,"Adet Sayı Vardır Ve Bunlar\n",sayiliste,"'Dir\n*****************************")
def calis():
    ikili()
    tara()
    ekranabas()
def wayl():
    while True:
        calis()
wayl()