from random import choice
def verificar(arr, c):
    cont = 0
    for i, v in enumerate(arr):
        if v == c:
            cont += 1
    return f'A letra {c} aparece {cont} vezes'

while True:
    try:
        list = []
        for i in range(10):
            letra = choice('abcdefghijklmnopqrstuvwxyz')
            list.append(letra)
        word = input('Diigte uma letra: ').strip().lower()[0]
        if word.isalpha():
            print(list)
            print(verificar(list, word))
            break
        else:
            print('Por favor, digite uma letra!')
    except:
        print('Valor inválido.')