from os import system as s
import time
class Tank:
    def __init__(self):
        self.f1 = '      ███████ ]▄▄▄▄▄▄▄▄'
        self.f2 = '  ▂▄▅█████████▅▄▃▂     '
        self.f3 = '[███████████████████]  '
        self.f4 = '  ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤     '
    def left(self):
        s('cls')
        self.f1= ' '+self.f1
        self.f2= ' '+self.f2
        self.f3= ' '+self.f3
        self.f4= ' '+self.f4
        print(f'{t1.f1}\n{t1.f2}\n{t1.f3}\n{t1.f4}')
        time.sleep(0.2)
t1=Tank()

for i in range(1000):
    t1.left()
p=input()



