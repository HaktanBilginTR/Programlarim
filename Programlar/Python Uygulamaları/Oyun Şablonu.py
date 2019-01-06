i=0
while True:
    print("Hoşgeldin")
    print("Başlamak İçin Herhangi Bir Tuşa Bas")
    o = input()
    if o != "ع":
        break
print('Oyuna Başlamak İçin "Başla" ')
print('Ayarlara Girmek İçin "Ayarlar" ')
print('Yapımcılar\'a Bakmak İçin "Yapımcılar" Yazmanız Yeterli ')
while True:
    p = input()
    if p == "Ayarlar":
        print("Metin Tabanlı Bir Oyunda Nasıl Bir Ayar Olabilir Ki :)")
        import time
        time.sleep(2)
        print('Oyuna Başlamak İçin "Başla" ')
        print('Yapımcılar\'a Bakmak İçin "Yapımcılar" Yazmanız Yeterli ')
    elif p == "Yapımcılar":
            print("Kod Yapım: Ömer Haktan Bilgin")
            import time
            time.sleep(2)
            print('Oyuna Başlamak İçin "Başla" ')
            print('Ayarlara Girmek İçin "Ayarlar" Yazmanız Yeterli ')
    elif p == "Başla":

        print("v")
    else:
        while True:
            if i == 0:
                print("Lütfen Düzgün Bir Şey Yazın")
                i += 1
                break

            elif i == 1:
                print("Adam Gibi Bir Şey Yaz Lan")
                i +=1
                break
            else:
                print("LAAAAAAAAAANNNNNNNNNNNNN!!!!!")