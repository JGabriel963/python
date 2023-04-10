from random import randint
def pares(arr):
    cont = 0
    for i, v in enumerate(arr):
        if v % 2 == 0:
            cont += 1
    return cont

def list_pares(arr):
    pares = []
    for i, v in enumerate(arr):
        if v % 2 == 0:
            pares.append(v)
    return pares

def impares(arr):
    cont = 0
    for i, v in enumerate(arr):
        if v % 2 == 1:
            cont += 1
    return cont

def list_impares(arr):
    impares = []
    for i, v in enumerate(arr):
        if v % 2 == 0:
            impares.append(v)
    return impares

while True:
    try:
        numbers = []
        for i in range(100):
            numbers.append(randint(1, 100))
        print(numbers)
        print(f'Quantidade de números pares: {pares(numbers)}')
        print(f'Lista com números pares: {list_pares(numbers)}')
        print(f'Quantidade de números ímpares: {impares(numbers)}')
        print(f'Lista com números ímpares: {list_impares(numbers)}')
        break
    except:
        print('Valor inválido!')