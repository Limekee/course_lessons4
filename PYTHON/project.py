from tkinter import *
from random import randint
root = Tk()
root.title("таблица умножения")
root.geometry('700x500')
e11=[]
d11=[]
d22=[]
s=0
y = 0#количество праивльных ответов
def g1():
    global s, l1, y, e2
    h = int(e2.get()) + 2
    g = h
    d = h
    j = h
    while (h - 1) != 0:
        d1 = randint(2, 10)
        d11.append(d1)
        d2 = randint(2, 10)
        d22.append(d2)
        h = h - 1
    e1.place(x=410, y=220)
    l1.place(x=0, y=0, width=700, height=500)
    if s!=g-1:
        l1['text'] = str(d11[s]) + '*' + str(d22[s])+'='
        s += 1
        e111 = e1.get()
        if e111=='':
            e11.append(0)
        elif e111!='':
            e11.append(e111)
    k=0
    if s==g-1:
        b1['text'] = 'закончить'
        del e11[0]
        e111 = e1.get()
        if e111 == '':
            e11.append(0)
        elif e111 != '':
            e11.append(e111)
        for i in range(0, d-1):
            if k<d:
                if d11[k] * d22[k] == int(e11[k]):
                    y += 1
                k+=1
        rr=(y/(j-2))*100
        l2 = Label(text='вы решили ' + str(y) + ' из ' + str(j-2) + ' примеров верно', font=('Arial', 30), fg='white',
                   bg='red')
        l2.place(x=0, y=0, height=500, width=700)
        if rr==100:
            l5 = Label(text='ваша оценка 5', font=('Arial', 30), fg='white', bg='red')
            l5.place(x=200, y=300)
        if 85<=rr<100:
            l5 = Label(text='ваша оценка 4', font=('Arial', 30), fg='white', bg='red')
            l5.place(x=200, y=300)
        if 60<=rr<85:
            l5 = Label(text='ваша оценка 3', font=('Arial', 30), fg='white', bg='red')
            l5.place(x=200, y=300)
        if rr<60:
            l5 = Label(text='ваша оценка 2', font=('Arial', 30), fg='white', bg='red')
            l5.place(x=200, y=300)
    return s, e1

l3 = Label(text='ТРЕНАЖЕР "ТАБЛИЦА УМНОЖЕНИЯ"', font=('Arial', 24), fg='white', bg='red')
l3.place(width=700, height=50, x=0, y=0)
l4 = Label(text='ВВЕДИТЕ КОЛИЧЕСТВО ВОПРОСОВ:', font=('Arial', 20), fg='white', bg='red')
l4.place(width=700, height=50, x=0, y=100)
e2 = Entry(font=('Arial', 20), fg='white', bg='red')
e2.place(x=600, y=100, width=90, height=40)
l1 = Label(text='', font=('Arial', 40), fg='black', bg='white')
e1 = Entry(font=('Arial', 40), fg='white', bg='red')
b1=Button(text='ответить!',  font=('Arial', 20), fg='white', bg='red', command=g1)
b1.place(x=270, y=300)

root.mainloop()