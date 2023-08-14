from tkinter import *
root=Tk()
root.geometry('300x400')
l1=Label(text='', bg='black', fg='white', font=('Arial', 20)).place(x=0, y=0, width=300, height=60)
print(l1)
# list1=[Button(text=str(i), command='', fg='black', font=('Arial', 20)) for i in range(10)]
# x, y=0, 100 # координаты(x) первой строки и нуля(Y всех)
# w, h=50, 40# ширина - высота кнопки
# x1, x2=0, 0#координаты по x второй и третьей строк соответсвенно
# for id, i in enumerate(list1):
#     if id==0:
#         i.place(x=x+w, y=y+h*3, width=w, height=h)
#     if 1<=id<=3:
#         i.place(x=x, y=y, width=w, height=h)
#         x+=w
#     if 4<=id<=6:
#         i.place(x=x1, y=y+h, width=w, height=h)
#         x1 += 50
#     if 7<=id<=9:
#         i.place(x=x2, y=y+h*2, width=w, height=h)
#         x2 += 50
def t6(t):
    global l1
    t.config(text='6')
b1 = Button(text='6', command=t6(l1)).place(x=100, y=100)
root.mainloop()
# import tkinter as tk
#
# class Test():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.text = tk.StringVar()
#         self.text.set("Test")
#         self.label = tk.Label(self.root, textvariable=self.text)
#
#         self.button = tk.Button(self.root,
#                                 text="Click to change text below",
#                                 command=self.changeText)
#         self.button.pack()
#         self.label.pack()
#         self.root.mainloop()
#
#     def changeText(self):
#         self.text.set("Text updated")
#
# app=Test()


