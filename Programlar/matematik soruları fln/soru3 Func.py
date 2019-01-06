def material():
    global x,i,liste1,liste2,liste3
    x = 0
    i = 0
    liste1 = []
    liste2 = []
    liste3 = []
def altili(i):
    while True:
        if 30 < i < 1000:
            while 30 < i < 1000:
                liste2.append(i)
                i += 6
        else:
            i += 6
            if i > 1000:
                break
def dortlu(x):
    while True:
        if 12 < x < 720:
            while 12 < x <= 720:
                liste1.append(x)
                x += 4
        else:
            x += 4
            if x > 720:
                break
def listeleme():
    for a in liste1:
        if a in liste2:
            liste3.append(a)
    return print(len(liste3))
def bipbop():
    material()
    dortlu(x)
    altili(i)
    listeleme()
bipbop()