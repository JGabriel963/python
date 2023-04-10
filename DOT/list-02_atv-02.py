from random import randint

def negativos(arr):
    cont = 0
    for i, v in enumerate(arr):
        if v < 0:
            cont += 1
    return cont

def soma(arr):
    cont = 0
    for i, v in enumerate(arr):
        if v > 0:
            cont += v
    return cont

while True:
    try:
        numbers = []
        for i in range(10):
            numbers.append(randint(-100, 100))
        print(numbers)
        print(f'Quantidade de números negativos: {negativos(numbers)}')
        print(f'A soma de todos os números negativos: {soma(numbers)}')
        break
    except:
        print('ERROR!!!')