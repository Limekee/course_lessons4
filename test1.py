from random import *
class User:
    def __init__(self, name):
        self.hp = 100
        self.name=name
    def atack(self, enemy, hero):
        enemy.hp-=randint(5, 20)
        if enemy.hp<=0:
            print(f'{hero.name} атаковал противника. У противника не осталось здоровья')
        elif enemy.hp>=0:
            print(f'{hero.name} атаковал противника. У противника осталось {enemy.hp} здоровья')
    def print(self):
        print(f'Имя:{self.name},  здоровье:{self.hp}')
class Mag(User):
    def __init__(self, name):
        super().__init__(name)
        self.frak='Маг'
    def print(self):
        print(f'Имя:{self.name}, класс:{self.frak},  здоровье:{self.hp}')
class Voin(User):
    def __init__(self, name):
        super().__init__(name)
        self.frak="Воин"
    def print(self):
        print(f'Имя:{self.name}, класс:{self.frak},  здоровье:{self.hp}')
class Luchnick(User):
    def __init__(self, name):
        super().__init__(name)
        self.frak="Лучник"
    def print(self):
        print(f'Имя:{self.name}, класс:{self.frak},  здоровье:{self.hp}')
voin1=Voin('Nekros')
voin2=Mag('Kratos')
voin1.print()
voin2.print()
ch=randint(1, 2)
if ch==1:
    while voin1.hp > 0 and voin2.hp > 0:
        voin1.atack(voin2, voin1)
        if voin1.hp<= 0 or voin2.hp <= 0:
            break
        voin2.atack(voin1, voin2)
elif ch==2:
    while voin1.hp > 0 and voin2.hp > 0:
        voin2.atack(voin1, voin2)
        if voin1.hp<= 0 or voin2.hp <= 0:
            break
        voin1.atack(voin2, voin1)
