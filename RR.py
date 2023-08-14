import random
class Tank:
    '''сражение танчиков'''
    def __init__(self, model, armor, health, min_damage, max_damage):
        self.model = model
        self.armor=armor
        self.health = health
        self.damage=random.randint(min_damage, max_damage)
    def shot(self, enemy):
        enemy.health_down(self.damage)
        if enemy.health<=0:
            print(f'ЭКИПАЖ ТАНКА {enemy.model} УНИЧТОЖЕН')
        else:
            print(f'{self.model}:Точно в цель, у противника {enemy.model}'
                  f' осталось {enemy.health}')

    def health_down(self, damage):
        self.health-=damage//self.armor
        print(f'{self.model}: Командир, по экипажу {self.model} попали у нас '
              f'осталось {self.health} ед здоровья')
    def print(self):
        print(f'{self.model}: имеет броню {self.armor} ед при {self.health} ед здоровья'
              f' и урон в {self.damage} единиц')
class MegaTank(Tank):
    def __init__(self, model, armor, health, min_damage, max_damage):
        super().__init__(model, armor, health, min_damage, max_damage)
        self.forceArmor = True
    def health_down(self, damage):
        super().health_down(damage//2)

