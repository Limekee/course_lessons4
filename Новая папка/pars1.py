import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.today()
today=today.strftime('%d/%m/%Y')
payload={'date_req':today}

response = requests.get(url, params=payload)
xml=bs(response.content, features='xml')
def getCourseInfo(id):
    a1 = str(xml.find('Valute', {'ID': id}).Value.text)
    a2 = str(xml.find('Valute', {'ID': id}).Name.text)
    a3 = str(xml.find('Valute', {'ID': id}).Nominal.text)
    return (f'({a3}шт.) {a2} стоит(ят) {a1} руб.')
def check_planet():
    mx=0
    biggest_planet = ''
    for i in range(1, 11):
        response=requests.get(f'https://swapi.dev/api/planets/{int(i)}').json()
        if int(response['diameter'])>mx:
            mx=int(response["diameter"])
            biggest_planet = response['name']
    return (f'самый большой диаметр у {biggest_planet}')
def getCourse(id):
    return str(xml.find('Valute', {'ID':id}).Value.text)
def check_starships():
    mx=0
    fastest_starship = ''
    r = [2, 3, 5, 12, 10, 11, 12, 13, 17]
    for i in r:
        response=requests.get(f'https://swapi.dev/api/starships/{int(i)}').json()
        if 'km' in response['max_atmosphering_speed']:
            response['max_atmosphering_speed']=response['max_atmosphering_speed'][:-2]
        if int(response['max_atmosphering_speed'])>mx:
            mx=int(response['max_atmosphering_speed'])
            fastest_starship = response['name']
    return (f'самый корабль быстрый оказался:{fastest_starship}')
def getCourseName(id):
    return str(xml.find('Valute', {'ID':id}).CharCode.text)
pp=['R01010', 'R01020A', 'R01035', 'R01060', 'R01090B', 'R01100', 'R01115', 'R01135', 'R01150', 'R01200', 'R01210', 'R01215', 'R01230', 'R01235', 'R01239', 'R01240', 'R01270', 'R01280', 'R01335', 'R01350', 'R01355', 'R01370', 'R01375', 'R01500', 'R01530', 'R01535', 'R01565', 'R01585F', 'R01589', 'R01625', 'R01670', 'R01675', 'R01700J', 'R01710A', 'R01717', 'R01720', 'R01760', 'R01770', 'R01775', 'R01805F', 'R01810', 'R01815', 'R01820']






