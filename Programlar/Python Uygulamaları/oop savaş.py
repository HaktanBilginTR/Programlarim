import random,time

class NPC:

    def __init__(self,name,bullet,HP = 100):
        self.name = name
        self.bullet = bullet
        self.HP = HP
    def Attack(self):
        global cpu_num, bullet_change
        while True:
            cpu_num = random.randrange(1, 3)
            if cpu_num == self.name:
                continue
            else:
                break
        bullet_change = random.randrange(1,11)
        self.bullet -= bullet_change
        print("isim: ", self.name, "harcanan mermi:" , bullet_change,"kalan mermi: " , self.bullet)
    def Hurt(self):
        global bullet_change, cpu_num
        if cpu_num == self.name:
            self.HP -= bullet_change * 2
        print("isim: " ,self.name,"kalan can: ", self.HP)

Ahmet = NPC(1,30)
Mehmet = NPC(2,30)

Ahmet.Attack()
time.sleep(0.25)
Mehmet.Hurt()

