while True:
    d = 1
    a = input("1. Sayıyı Giriniz:")
    c = input("Yapacağınız İşlemi Seçiniz:")
    b = input("2. Sayıyı Giriniz:")
    if a == int and b == int and c == int:
        print("Adam Gibi Bir Şey Yaz Lan!")
    elif c == "+":
        d = int(a)+int(b)
        print("",d)
    elif c == "-":
        d = int(a)-int(b)
        print("",d)
    elif c == "*":
        d = int(a)*int(b)
        print("",d)
    elif c == "/":
        d = int(a)/int(b)
        print("",d)