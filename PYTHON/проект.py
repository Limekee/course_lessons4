import random
a = (input('имя фамилия: '))
b = int(input('количество вопросов: '))
k = 0
for i in range(b):
    f1 = random.randint(1, 10)
    f2 = random.randint(1, 10)
    d = int(input(str(f1)+ "*"+ str(f2)+'= '))
    if d == f1*f2:
        k+=1
print('вы решили '+ str(k)+'/' +str(b) + "вопросов")
if 90 <=k/b*100<=100:
    print('ваша оценка 5!')
if 80<=k/b*100<=89:
    print('ваша оценка 4!')
if 70 <= k/b*100 < 79:
    print('ваша оценка 3!')
if k/b*100 < 70:
    print('ваша оценка 2!')



