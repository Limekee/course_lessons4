import random
from pars1 import *
import vk_api
from pars2 import get_wiki_article
from vk_api.longpoll import VkLongPoll, VkEventType
pp1={'AUD': 'R01010', 'AZN': 'R01020A', 'GBP': 'R01035', 'AMD': 'R01060', 'BYN': 'R01090B', 'BGN': 'R01100', 'BRL': 'R01115', 'HUF': 'R01135', 'VND': 'R01150', 'HKD': 'R01200', 'GEL': 'R01210', 'DKK': 'R01215', 'AED': 'R01230', 'USD': 'R01235', 'EUR': 'R01239', 'EGP': 'R01240', 'INR': 'R01270', 'IDR': 'R01280', 'KZT': 'R01335', 'CAD': 'R01350', 'QAR': 'R01355', 'KGS': 'R01370', 'CNY': 'R01375', 'MDL': 'R01500', 'NZD': 'R01530', 'NOK': 'R01535', 'PLN': 'R01565', 'RON': 'R01585F', 'XDR': 'R01589', 'SGD': 'R01625', 'TJS': 'R01670', 'THB': 'R01675', 'TRY': 'R01700J', 'TMT': 'R01710A', 'UZS': 'R01717', 'UAH': 'R01720', 'CZK': 'R01760', 'SEK': 'R01770', 'CHF': 'R01775', 'RSD': 'R01805F', 'ZAR': 'R01810', 'KRW': 'R01815', 'JPY': 'R01820'}
def main():
    token = "vk1.a.KgOd163IgPd8GPTzSJnFe7ltWsklV_DH75NRG90PCSM0gsvPczE68-_muejqNjgHW4wE-pIum7dAjswUS9xDqhQ875qizgvyJNBaowwyRzpBUAD0kazOG1RutIlz9aK-M6aG9XsGEb06DuusoLw2B5ifnTbemzJM2tdVBEJ_Hhm3Gv0cWIaDq-KU7DwT0dEEnJrjDSIWA2ISFrxy9ewwqw"
    vk_session=vk_api.VkApi(token=token)
    vk=vk_session.get_api()
    longpoll=VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW and event.to_me:
            msg=event.text
            user_id=event.user_id
            random_id=random.randint(1, 100000000000)
            if msg[:2]=='-к':
                response=getCourse(pp1[msg[3:]])
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=response+' рублей')

            elif msg[:2].lower()=='ви':
                response= get_wiki_article(msg[2:])
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=response)
            else:
                response='неизвестная команда'
                vk.messages.send(user_id=event.user_id, random_id=random_id, message=response)


main()