from random import randint
dado = []
def lancamentos(x):
    for i in range(x):
        dado.append(randint(1, 6))
        print(f'{i + 1}º vez: {dado[i]}')
def contador(arr):
    ocorrencias = {}
    for i in arr:
        if i in ocorrencias:
            ocorrencias[i] += 1
        else:
            ocorrencias[i] = 1
    return ocorrencias
while True:
    try:
        n = int(input('Quantas vezes será lançado o dado?_'))
        lancamentos(n)
        quantidade = contador(dado)
        print(quantidade)
        break
    except:
        print("Valor inválido!")