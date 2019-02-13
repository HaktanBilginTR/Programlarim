import time
saat, dakika = 6, 55


def yazdir():
    print(saat, ":", dakika)

yazdir()
while True:
    time.sleep(60)
    dakika += 1
    if dakika == 60:
        dakika = 0
        saat += 1
    if saat == 24:
        saat = 0
    else:
        pass
    yazdir()
