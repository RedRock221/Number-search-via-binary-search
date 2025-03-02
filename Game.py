import random


print('--- Добро пожаловать в игру человек ---')
print('------------------------------------------------------------------')
print('*Правила*')
print('Тебе нужно указать максимальное число до которого я смогу загадать число, твоя задача отгадать число,\n я буду тебе подсказывать, говорить больше или меньше у тебя ограниченное количество попыток')
print('------------------------------------------------------------------')
print ('*  так же дам бесплатный совет, используя бинарный алгоритм, если хочешь выйграть')
MaxNum = int(input())
guess = 0

number = random.randint(1, MaxNum)

attempts = MaxNum
var = 0
while attempts != 0:
    attempts = attempts // 2
    var = var + 1


print(f'У тебя попыток {var}')

while number != guess:
    print('Твой число: ')
    guess = int(input())
    var = var - 1
    print(f'осталось {var} попыток') 
    if var <= 0:
        print('- Ты проиграл')
        exit()

    if guess > number and guess < MaxNum:
        print('- Моё число меньше')
    elif  guess < number and guess > 0:
        print('- Моё число больше')
    elif guess == number:
        print('- Твоя взяла, победа за тобой')
    else:
        print(f'- Включи кателок, мы играеим от 0 до {MaxNum}')
  
