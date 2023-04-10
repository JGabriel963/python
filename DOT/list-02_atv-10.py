from random import randint

def maior(arr):
    big = 0
    position = 0
    for i, v in enumerate(arr):
        if i == 0:
            position = i
            big = v
        else:
            if v > big:
                position = i
                big = v
    return f'O maior número é o {big} que está na posição {position}'

def menor(arr):
    small = 0
    position = 0
    for i, v in enumerate(arr):
        if i == 0:
            position = i
            small = v
        else:
            if v < small:
                position = i
                small = v
    return f'O menor número é o {small} que está na posição {position}'

while True:
    number = []
    for i in range(15):
        number.append(randint(1, 20))
    print(number)
    print(maior(number))
    print(menor(number))
    break