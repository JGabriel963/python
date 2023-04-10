numbers_x = []
def copy():
    list_r = []
    for i,v in enumerate(numbers_x):
        if v < 0:
            list_r.append(v)
        else:
            list_r.append(0)
    return list_r

while True:
    try:
        for i in range(10):
            n = int(input(f'Digite o {i + 1} número:_'))
            numbers_x.append(n)
        print(numbers_x)
        print(copy())
        break
    except:
        print('Valor inválido!!')