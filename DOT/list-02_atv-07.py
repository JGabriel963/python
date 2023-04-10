from random import randint

def verificar(arr, n):
    if n not in arr:
        return f'O número {n} não está na lista.'
    else:
        return f'O número {n} está na lista.'

while True:
    try:
        list = []
        for i in range(10):
            list.append(randint(1,10))

        num = int(input('Digite um número: '))
        print(list)
        print(verificar(list, num))
        break
    except:
        print('Valor inválido.Tente novamente!')
