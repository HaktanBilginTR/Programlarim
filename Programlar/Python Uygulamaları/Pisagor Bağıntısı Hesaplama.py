print("Pisagor Bağıntısı Bulma Aracına Hoşgeldin\n")

def pisagor(a,b):
    p=a*a+b*b
    import math
    sqr=math.sqrt(p)
    sqr=float(sqr)
    return print("3. Kenar :",sqr)
while True:
    a=int(input("1. Kenar :"))
    b=int(input("2. Kenar :"))
    pisagor(a,b)
    continue