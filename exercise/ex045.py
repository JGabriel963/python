from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int(input("Qual é sua jogada? "))
print('-=' * 20)
print(f'Computador jogou {itens[computador]}')
print(f'Você jogou {itens[jogada]}')
print('-=' * 20)
if computador == 0:
    if jogada == 0:
        print('EMPATE!')
    elif jogada == 1:
        print('JOGADOR VENCEU!')
    elif jogada == 2:
        print('JOGADOR PERDEU!')
    else:
        print("OPÇÃ IVÁLIDA!")
elif computador == 1:
    if jogada == 0:
        print('JOGADOR PERDEU!')
    elif jogada == 1:
        print('EMPATE!')
    elif jogada == 2:
        print('JOGADOR VENCEU!')
    else:
        print("OPÇÃ IVÁLIDA!")
elif computador == 2:
    if jogada == 0:
        print("JOGADOR VENCEU!")
    elif jogada == 1:
        print('JOGADOR PERDEU!')
    elif jogada == 2:
        print("EMPATE!")
    else:
        print("OPÇÃ IVÁLIDA!")

