def faktoriel(sayi):
    faktor = 1
    if sayi <= 0:
        print("Negatif Olmayan Sayı Giriniz.")
    else:
        for i in range(1,sayi+1):
            faktor = faktor * i
        print("Faktöriyeliniz:", faktor)
while True:
    sayi = int(input("Sayı Giriniz :"))
    faktoriel(sayi)






































