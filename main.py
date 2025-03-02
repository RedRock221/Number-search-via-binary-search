print('Введите вехний порог')
MaxNum = int(input())
temp = MaxNum / 2
i = 0
attempts = 1
XXX = temp

while i != 2:
    print(f' \nПопытка {attempts}')
    print(f'Число: {round(guess)}')
    print(' 1. Больше \n 2. Это моё число \n 3. Меньше')
    print('Ваш ответ: ')
    i = int(input())
    temp =  temp / 2
    if i == 1:  
        guess = guess + temp
    else:
        guess = guess - temp
    var = var + 1  

