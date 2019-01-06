import sqlite3
import time
Boru_adi = None

con = sqlite3.connect("database.db")
cursor = con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS database (Boru_adi STR,Dn FLOAT,Nominal_Size STR,Dis_Cap FLOAT,Kalinlik FLOAT,Agirlik FLOAT,Test_Basinci FLOAT)")

def degerekleme():
    Boru_adi = str(input("Boru Adı : "))
    DN = float(input("DN:"))
    Nominal_Size = float(input("Nominal Size:"))
    Dis_Cap=float(input("Dış Çap:"))
    Kalinlik=float(input("Kalınlık:"))
    Agirlik=float(input("Ağırlık:"))
    Test_Basinci=float(input("Test Basıncı:"))
    cursor.execute("INSERT INTO database (Boru_adi,Dn,Nominal_Size,Dis_Cap,Kalinlik,Agirlik,Test_Basinci) VALUES(?,?,?,?,?,?,?)",(Boru_adi,DN,Nominal_Size,Dis_Cap,Kalinlik,Agirlik,Test_Basinci))
    con.commit()
def degeral():
    cursor.execute("SELECT * FROM database")
    data = cursor.fetchall()
    for i in data:
        print(i)



tabloolustur()
print("Boru Eklemek İçin : 'Boru Ekle'\nBoruları Görmek İçin : 'Boruları Gör'\nYazınız")
while True:
    uuu = input("")

    if uuu == "Boru Ekle":
        while True:
            degerekleme()
            print("Boru Eklemek İçin : 'Boru Ekle'\nBoruları Görmek İçin : 'Boruları Gör'\nYazınız")
            uuu= None
            break
    elif uuu == "Boruları Gör":
        while True:
            degeral()
            time.sleep(2)
            print("Boru Eklemek İçin : 'Boru Ekle'\nBoruları Görmek İçin : 'Boruları Gör'\nYazınız")
            uuu= None
            break