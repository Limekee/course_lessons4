from tkinter import *
import requests
from bs4 import BeautifulSoup as bus
from datetime import datetime
window = Tk()
window.geometry('400x400+230+200')
window.title('Панель валют')
window.resizable(height=False, width=False)
p2=PhotoImage(file='Безымянный1.png')
l6=Label(image=p2)
l6.place(x=0, y=0)
#http://www.cbr.ru/scripts/XML_daily.asp?
p1 = PhotoImage(file='Безымянный.png')
l1=Label(window, image=p1)
l1.place(x=0, y=0)
l2=Label(window, text='Курс валют от \nбанка \nКод Будущего', font=('Arial', 22))
l2.place(x=180, y=30)

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today().strftime('%d/%m/%Y')
response = requests.get(url+'date_req='+today)
xml = bus(response.content, features="xml")
def getCourse(id):
    return xml.find('Valute', {'ID': id}).Value.text
usd_course = Label(window, text ='$'+ getCourse('R01235'), font=('Arial', 16))
usd_course.place(x=150, y=200)
l3=Label(window, text='€'+getCourse('R01239'),  font=('Arial', 16))
l3.place(x=150, y=230)
l4=Label(window, text='Дата:'+today.replace('/', '.'), font=('Arial', 12))
l4.place(x=250, y=355)
l5=Label(window, text='¥'+getCourse('R01375'), font=('Arial', 14))
l5.place(x=150, y=260)

window.mainloop()
