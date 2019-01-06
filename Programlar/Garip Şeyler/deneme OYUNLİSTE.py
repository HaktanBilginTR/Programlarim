import requests
from bs4 import BeautifulSoup
import time

oyunlar  ={}
url = "https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/"
url2 = "https://store.steampowered.com/app/359550/Tom_Clancys_Rainbow_Six_Siege/"
url3 = "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"
liste =[]
r = requests.get(url)
r2 = requests.get(url2)
r3 = requests.get(url3)
soup = BeautifulSoup(r.content,"html.parser")
soup2 = BeautifulSoup(r2.content,"html.parser")
soup3 = BeautifulSoup(r3.content,"html.parser")
for kelimegruplari in soup.find_all("div",{"class":"game_purchase_price price"}):
    Parapub = kelimegruplari.text
    Parapub = Parapub.replace("\n","")
    Parapub = Parapub.replace("\t", "")
    Parapub = Parapub.replace("\r", "")
    kelimegruplari = None


for oyunismi in soup.find_all("h1"):
    oyunismi = oyunismi.text
    liste.append(oyunismi)
    oyunismi = None
pabci =liste[0]
pabci = pabci.replace("Buy","")
oyunlar.update({pabci:Parapub})
liste = []

##########################
for kelimegruplari in soup2.find_all("div",{"class":"game_purchase_price price"}):
    Parar6s = kelimegruplari.text
    Parar6s = Parar6s.replace("\n","")
    Parar6s = Parar6s.replace("\t","")
    Parar6s = Parar6s.replace("\r","")
    liste.append(Parar6s)
r6starterpara = liste[0]
r6standartpara = liste[1]
liste = []
for oyunismi in soup2.find_all("h1"):
    oyunismi = oyunismi.text
    oyunismi.replace("Buy","")
    liste.append(oyunismi)
r6_1 = liste[0] #starter
r6_2 = liste[1] #standart
r6_1 = r6_1.replace("Buy","")
r6_2 = r6_2.replace("Buy","")
oyunlar.update({r6_1:r6starterpara,r6_2:r6standartpara})
liste = []
kelimegruplari = None
oyunismi = None
###########################################
print(oyunlar)












time.sleep(10)