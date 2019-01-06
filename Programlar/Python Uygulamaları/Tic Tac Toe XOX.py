import time



print("---------------------------------")
print("Tic Tac Toe/XOX Oyununa Hoşgeldin\n1. Oyuncu = X\n2. Oyuncu = O")
print("---------------------------------")
liste = []
def x_win():
    if liste[0] == "X" and liste[1] == "X" and liste[2] == "X":
        return True
    elif liste[3] == "X" and liste[4] == "X" and liste[5] == "X":
        return True
    elif liste[6] == "X" and liste[7] == "X" and liste[8] == "X":
        return True
    elif liste[0] == "X" and liste[3] == "X" and liste[6] == "X":
        return True
    elif liste[1] == "X" and liste[4] == "X" and liste[7] == "X":
        return True
    elif liste[2] == "X" and liste[5] == "X" and liste[8] == "X":
        return True
    elif liste[0] == "X" and liste[4] == "X" and liste[8] == "X":
        return True
    elif liste[2] == "X" and liste[4] == "X" and liste[6] == "X":
        return True

def o_win():
    if liste[0] == "O" and liste[1] == "O" and liste[2] == "O":
        return True
    elif liste[3] == "O" and liste[4] == "O" and liste[5] == "O":
        return True
    elif liste[6] == "O" and liste[7] == "O" and liste[8] == "O":
        return True
    elif liste[0] == "O" and liste[3] == "O" and liste[6] == "O":
        return True
    elif liste[1] == "O" and liste[4] == "O" and liste[7] == "O":
        return True
    elif liste[2] == "O" and liste[5] == "O" and liste[8] == "O":
        return True
    elif liste[0] == "O" and liste[4] == "O" and liste[8] == "O":
        return True
    elif liste[2] == "O" and liste[4] == "O" and liste[6] == "O":
        return True
def berabere():
    if liste[0] != 1 and liste[1] != 2 and liste[2] != 3 and liste[3] != 4 and liste[4] != 5 and liste[5] != 6 and liste[6] != 7 and liste[7] != 8 and liste[8] != 9:
        return True
while True:
    for i in range(0,3):
        liste.append(i+1)
    print(liste[0],"",liste[1],"",liste[2])

    for i in range(3,6):
        liste.append(i+1)
    print(liste[3],"",liste[4],"",liste[5])
    for i in range(6,9):
        liste.append(i+1)
    print(liste[6], "", liste[7], "", liste[8])

    break



while True:
    if x_win() == True:
        print("1. OYUNCU KAZANDI")
        time.sleep(5)
        break
    elif o_win() == True:
        print("2. OYUNCU KAZANDI")
        time.sleep(5)
        break
    elif berabere() == True:
        print("BERABERE")
        time.sleep(5)
        break
    giris = int(input("1. Oyuncu :"))

    if giris == liste[0]:
        liste[0] = "X"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[1]:
        liste[1] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[2]:
        liste[2] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[3]:
        liste[3] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[4]:
        liste[4] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break

        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[5]:
        liste[5] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[6]:
        liste[6] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[7]:
        liste[7] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[8]:
        liste[8] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris == liste[9]:
        liste[9] = "X"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    if x_win() == True:
        print("1. OYUNCU KAZANDI")
        time.sleep(5)
        break

    elif o_win() == True:
        print("2. OYUNCU KAZANDI")
        time.sleep(5)
        break
    elif berabere() == True:
        print("BERABERE")
        time.sleep(5)
        break
    giris2 = int(input("2. Oyuncu :"))
    if x_win() == True:
        print("1. OYUNCU KAZANDI")
        time.sleep(5)
        break

    elif o_win() == True:
        print("2. OYUNCU KAZANDI")
        time.sleep(5)
        break
    elif berabere() == True:
        print("BERABERE")
        time.sleep(5)
        break
    if giris2 == liste[0]:
        liste[0] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[1]:
        liste[1] = "O"

        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[2]:
        liste[2] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:

            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[3]:
        liste[3] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[4]:
        liste[4] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[5]:
        liste[5] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[6]:
        liste[6] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[7]:
        liste[7] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    elif giris2 == liste[8]:
        liste[8] = "O"
        print(liste[0],"",liste[1],"",liste[2])
        print(liste[3],"",liste[4],"",liste[5])
        print(liste[6],"",liste[7],"",liste[8])
        if x_win() == True:
            print("1. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif o_win() == True:
            print("2. OYUNCU KAZANDI")
            time.sleep(5)
            break
        elif berabere() == True:
            print("BERABERE")
            time.sleep(5)
            break
    if x_win() == True:
        print("1. OYUNCU KAZANDI")
        time.sleep(5)
        break
    elif o_win() == True:
        print("2. OYUNCU KAZANDI")
        time.sleep(5)
        break
    elif berabere() == True:
        print("BERABERE")
        time.sleep(5)
        break