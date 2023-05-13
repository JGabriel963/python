players = []
play = {}
matches = []
while True:
    play.clear()
    matches.clear()
    cont = 0
    play['nome'] = input("Nome do Jogador: ").strip()
    partidas = int(input(f'Quantas partidas {play["nome"]} jogou? '))
    for i in range(partidas):
        matches.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    play['gols'] = matches[:]
    play["total"] = sum(matches)
    # Enquanto não for S ou N
    option = input("Quer continuar? [S/N] ").strip().upper()[0]
    while option not in "SN":
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
    # Salvando informação do jogador
    players.append(play.copy())
    if option == "N":
        break
print(players)

