import sqlite3
import time
con = sqlite3.connect("MasaVerileri.db")
cursor = con.cursor()
def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS  MasaVerileri (İsim STR,Boyut STR,Renk STR ) ")
tabloolustur()
def degerekle():
    masa_isim = str(input("Masa İsmi Giriniz : "))
    masa_boyut = str(input("Boyut Giriniz :"))
    masa_renk = str(input("Renk Giriniz :"))
    cursor.execute("INSERT INTO MasaVerileri (İsim , Boyut , Renk)  VALUES(?,?,?)",(masa_isim,masa_boyut,masa_renk))
    con.commit()
    print("EKLENDİ")
    time.sleep(1)
    print("Ne Yapmak İstiyorsunuz ?")
    print("Masalara Bak : Bak \nMasa Ekle : Ekle")
def degeral():
    cursor.execute("SELECT * FROM MasaVerileri")
    data = cursor.fetchall()
    for i in data:
        print(i)
    time.sleep(8)
    print("Ne Yapmak İstiyorsunuz ?")
    print("Masalara Bak : Bak \nMasa Ekle : Ekle")
class Masa:
    def __init__(self,isim = "Masa",boyut="30" ,renk = "beyaz"):
        self.isim = isim
        self.boyut = boyut
        self.renk = renk
    def ozellikler(self):
        print("----------Basılıyor----------")
        print("İsimi :",self.isim+ "Boyutu : ",self.boyut + " Rengi : " , self.renk,)
tabloolustur()
print("Ne Yapmak İstiyorsunuz ?")
print("Masalara Bak : Bak \nMasa Ekle : Ekle")
while True:
    deger = input()
    if deger == "ekle" or deger == "Ekle":
        degerekle()
    if deger == "bak" or deger == "Bak":
        degeral()