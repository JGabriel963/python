player = {}
partidas = []
cont = 0
player['nome'] = input('Nome do jogador: ').strip()
tot = int(input(f'Quantas partidas {player["nome"]} jogou? '))
for c in range(tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
player['gols'] = partidas[:]
for i, v in enumerate(partidas):
    cont += v
player['total'] = cont
print('-=' * 40)
print(player)
print('-=' * 40)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 40)
print(f'O jogador {player["nome"]} jogou {tot} partidas.')
for i, v in enumerate(partidas):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um toal de {player["total"]}')