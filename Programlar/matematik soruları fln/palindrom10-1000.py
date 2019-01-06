def palindrom(veri):
    if len(veri) == 3:
        if veri[:1] == veri[2:]:
            return True
        else:
            return False
    elif len(veri) == 2:
        if veri[0] == veri[1]:
            return True
        else:
            return False
liste = []
for a in range(10,1001):
    a = str(a)
    palindrom(a)
    if palindrom(a) == True:
        liste.append(a)
    elif palindrom(a) == False:
        pass
print(len(liste))
