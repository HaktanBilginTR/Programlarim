import random
import time
import turtle
sayi = random.randrange(0,10)
print("Oh ,Selam Hoşgeldin.")
time.sleep(1)
print("Oyun Oynayalım Mı ??? E/H")
while True:
    uuuuu = input()
    if uuuuu == "E" or uuuuu == "e":
        print("Şimdi Seninle Bir Tahmin Etme Oyunu Oynayacağız.")
        print("Şimdi 0 İle 10 Arası Tahmin Ettiğin Sayıyı Söyle :")
        while True:
            try:
                tahmin = int(input())
            except ValueError or NameError or TypeError:
                print(":)")
                continue
            if tahmin <0:
                print("0 İle 10 Arası Dedik!")
                tahmin = None
                continue
            elif tahmin >10:
                print("0 İle 10 Arası Dedik!")
                tahmin = None
                continue
            if tahmin == sayi:
                print("TEBRİKLERR!!!!")
                time.sleep(3)
                quit()
            elif tahmin < sayi:
                print("Biraz Daha Yükselt.")
                tahmin = None
            elif tahmin > sayi:
                print("Çok Yüksektesin Düş Az.")
                tahmin = None
    elif uuuuu == "H" or uuuuu == "h":
        smiles = turtle.Turtle()
        smiles.penup()
        smiles.goto(-105, 155)
        smiles.pendown()
        smiles.goto(-45, 115)
        smiles.penup()
        smiles.goto(-75, 75)
        smiles.pendown()
        smiles.circle(10)
        smiles.penup()
        smiles.goto(105, 155)
        smiles.pendown()
        smiles.goto(45, 115)
        smiles.penup()
        smiles.goto(75, 75)
        smiles.pendown()
        smiles.circle(10)
        smiles.penup()
        smiles.goto(0, 25)
        smiles.pendown()
        smiles.circle(-100, 80)
        smiles.penup()
        smiles.setheading(180)
        smiles.goto(0, 25)
        smiles.pendown()
        smiles.circle(100, 80)
        turtle.done()
        quit()
    if uuuuu != "H" or uuuuu != "h" or uuuuu != "E" or uuuuu != "e":
        print("HAHAA BENİ KANDIRABİLECEĞİNİ Mİ SANDIN !?!?!?!?")