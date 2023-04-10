list_x = []
def list_y(arr):
    list_y = []
    for i, v in enumerate(arr):
        if i % 2 == 0:
            list_y.append(v / 2)
        else:
            list_y.append(v * 3)
    return list_y


while True:
    try:
        for i in range(1, 10 + 1):
            n = int(input(f'Digite o {i + 1}º número:_'))
            list_x.append(n)
        print(list_x)
        print(list_y(list_x))
        break
    except:
        print('Valor inválido!')