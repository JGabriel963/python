numbers = []
def modificada(arr):
    for i,v in enumerate(arr):
        if v < 0:
            arr[i] = 0
    return numbers
while True:
    try:
        for i in range(10):
            n = int(input(f'Digite o {i + 1}º número inteiro'))
            numbers.append(n)
        print(modificada(numbers))
        break
    except:
        print('Valor inválido!')