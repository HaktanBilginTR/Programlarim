x = 0
i = 0
liste1 = []
liste2 = []
liste3 = []
while True:
    if 12<x<720:
        while 12<x<=720:
            liste1.append(x)
            x+=4
    else:
        x+=4
        if x > 720:
            break
while True:
    if 30< i <1000:
        while 30< i <1000:
            liste2.append(i)
            i+=6
    else:
        i+=6
        if i > 1000:
            break
for a in liste1:
    if a in liste2:
        liste3.append(a)
print(len(liste3))