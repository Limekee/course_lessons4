import requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = 'date_req='+ str(datetime.today())[8:10]+'/'+str(datetime.today())[5:7]+'/'+str(datetime.today())[0:4]
print(url+today)
response = requests.get(url+today)
xml = BeautifulSoup(response.content, features="xml")
def get_course(id):
    course = xml.find('Valute', {'ID': id}).CharCode.text
    return course

pp=['R01010', 'R01020A', 'R01035', 'R01060', 'R01090B', 'R01100', 'R01115', 'R01135', 'R01150', 'R01200', 'R01210', 'R01215', 'R01230', 'R01235', 'R01239', 'R01240', 'R01270', 'R01280', 'R01335', 'R01350', 'R01355', 'R01370', 'R01375', 'R01500', 'R01530', 'R01535', 'R01565', 'R01585F', 'R01589', 'R01625', 'R01670', 'R01675', 'R01700J', 'R01710A', 'R01717', 'R01720', 'R01760', 'R01770', 'R01775', 'R01805F', 'R01810', 'R01815', 'R01820']
pp1={}
for i in pp:
    pp1[get_course(i)]=i
def course (valute_from, valute_to, amount):
    nom_to_necov = xml.find('Valute', {'ID': pp1[valute_to]}).Value.text#курс в указанном номинале
    nom_to_colvo=xml.find('Valute', {'ID': pp1[valute_to]}).Nominal.text# количество рублей по курсу
    nom_to=float(nom_to_necov.replace(',', '.'))/float(nom_to_colvo.replace(',', '.'))#сколько за 1 валюту рублей куда переводим

    nom_from_necov = xml.find('Valute', {'ID': pp1[valute_from]}).Value.text
    nom_from_colvo = xml.find('Valute', {'ID': pp1[valute_from]}).Nominal.text
    nom_from = float(nom_from_necov.replace(',', '.')) / float(nom_from_colvo.replace(',', '.'))  # сколько за 1 валюту рублей откуда переводим

    result_rub=amount*nom_from
    result_in_value=result_rub /nom_to
    s = open('па.txt', 'a')
    s.write(f'переводим из:{valute_from}\n')
    s.write(f'переводим в:{valute_to}\n')
    s.write(f'сумма в {valute_from}: {amount}\n')
    s. write(f'результат перевода:{result_in_value}\n')
    s.write('_'*100)
    s.close()
    return result_in_value
fromm = input('from:')
too=input('to:')
summ = input('summ:')
print(course(fromm, too, int(summ)))










