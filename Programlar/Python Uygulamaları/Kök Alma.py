import math
print("Hoşgeldiniz")
def alma():
    print("Sayıyı Giriniz :")
    try:
        global a
        a = int(input())
        a = math.sqrt(a)
    except ValueError or UnboundLocalError:
        print("*******\nHata\n*******")
    try:
        if a == None:
            return
    except NameError:
        pass
    else:
        print(a)
        a = None
while True:
    alma()