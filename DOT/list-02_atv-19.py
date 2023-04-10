list_r = []
list_s = []
def list_x():
    list_x = []
    for i in range(5):
        list_x.append(list_r[i])
    for i in range(10):
        list_x.append(list_s[i])
    return list_x

while True:
    try:
        for i in range(5):
            n = int(input(f'{i + 1}º elemento da Lista R:_'))
            list_r.append(n)
        for i in range(10):
            n = int(input(f'{i + 1}º elemento da Lista S:_'))
            list_s.append(n)
        print(list_x())
        break
    except:
        print('Valor inválido! Tente novamente.')