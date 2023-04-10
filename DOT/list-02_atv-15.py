list_e = []
def list_d(arr):
    arr.reverse()
    list_d = arr[:]
    return list_d

while True:
    try:
        for i in range(10):
            n = int(input(f'Digite o {i + 1}º número:_'))
            list_e.append(n)
        print(list_e)
        print(list_d(list_e))
        break
    except:
        print('Valor inválido!')