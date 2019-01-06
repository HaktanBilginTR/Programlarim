import time
import tkinter.messagebox
class ain:
    kaka = []
    y1 = True
    y2 = True
    y3 = True
    kaka.append(y1 and y2 and y3)
    def kiril(self,sayi):
        global y1,y2,y3
        if sayi == "y1":
            self.y1 = False
            return self.y1
        elif sayi == "y2":
            self.y2 = False
            return self.y2
        elif sayi == "y3":
            self.y3 = False
            return self.y3
    def pirt(self):
        print("*******************")
        print(self.y1,self.y2,self.y3)



