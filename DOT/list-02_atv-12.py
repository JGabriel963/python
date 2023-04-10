from random import choice
def nota():
    cont = 0
    for i in range(30):
        if gabarito[i] == respostas[i]:
            cont += 1
    return cont

respostas = []
for i in range(30):
    respostas.append(choice('ABCDE'))
gabarito = []
while True:
    try:
        for i in range(len(respostas)):
            lesson = input(f'Resposta da {i + 1}º questão:_').strip().upper()[0]
            gabarito.append(lesson)
        print(f'Gabarito: {gabarito}')
        print(f'Cartão resposta: {respostas}')
        print(f'Pontos: {nota()}')
        break
    except:
        print('Valor inválido! Tente novamente.')