liste1 = []
liste2 = []
liste3 = []
i = 32
x = 36
while 32 <= i <= 110:
    liste1.append(i)
    i += 4
while 36 <= x <= 110:
    liste2.append(x)
    x += 6
for a in liste1:
    if a in liste2:
        liste3.append(a)
print("Sonuç :", len(liste3))