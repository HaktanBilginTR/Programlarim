def formul(a,b,c):
    if (a+b)>c and(a+c)>b and (c+b)>a and (a-b)<c and (a-c)<b and (c-b)<a:
        print("Bu bir üçgendir")
        return
    else:
        print("Bu bir üçgen değildir")
        return
print("Üçgen sorgulama makinesine hoşgeldiniz\n")
while True:
    a=int(input("1. Kenar :"))
    b=int(input("2. Kenar :"))
    c=int(input("3. Kenar :"))
    formul(a,b,c)