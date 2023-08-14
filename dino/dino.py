import time
from tkinter import *
from time import sleep
from random import randint
w = Tk()
w.geometry('600x500')
c1=Canvas(w, width=2200, height=500)
c1.place(in_=w, x=0, y=0)
class Dino:
    def __init__(self):
        self.body=PhotoImage(file='imgonline-com-ua-Resize-10vIHjYLhHaVT6.png')
        self.jump=10
        self.x=50
        self.y=250
        self.w=70
        self.h=71
    def up(self, event):
        if self.y==250:
            for i in range(36):
                time.sleep(0.01)
                self.y-=5
                c1.move(id1, 0, -5)
                w.update()
            w.update()#обновление окна
            time.sleep(0.01)
            for i in range(36):
                self.y += 5
                time.sleep(0.01)
                c1.move(id1, 0, 5)
                w.update()

class Kaktus:
    def __init__(self, x):
        self.body=PhotoImage(file='kak.png')
        self.y=250
        self.x=x
        self.v=5
    def left(self):
        while self.x<(-60):
            self.x-=self.v
            sleep(0.01)
            c1.move(id, 0, self.v)
            w.update()
d1=Dino()
id1=c1.create_image(d1.x, d1.y, image=d1.body)
kaktuses=[Kaktus(400*x+x*3) for x in range(1, 11)]
c1.create_rectangle(0, 285, 600, 500)
for i in kaktuses:
    id = c1.create_image(i.x, i.y, image=i.body)
    i.left()


w.bind("<Key-Up>", d1.up)
w.mainloop()