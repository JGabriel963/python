import random
ordem = []
for i in range(4):
    nome = ordem.append(input(f'{i + 1}º nome: '))
random.shuffle(ordem)
print(f'A ordem de aprentação será\n{ordem}')