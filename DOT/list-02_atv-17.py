number_w = []
def ocorrencia(v):
    cont = 0
    for i, c in enumerate(number_w):
        if v == c:
            print(f'O valor {v} ocorre no índice {i}')
            cont += 1
    if cont > 0:
        print(f'Número de ocorrências: {cont}')
    else:
        print(f'Não há nenhuma ocorrência do valor {v}')

while True:
    try:
        for i in range(10):
            n = int(input(f'Digite o {i}º número:_'))
            number_w.append(n)
        value = int(input('Digite um valor:_'))
        ocorrencia(value)
        break
    except:
        print('Valor inválido!')