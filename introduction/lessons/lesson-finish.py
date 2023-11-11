teams = [
    {"name": "Palmeiras", "players": ["Eduardo", "Jão", "Pedro"]},
    {"name": "Flamengo", "players": ["Eduardo", "Pedro"]},
]


def line(value):
    decoration = "=" * value
    return decoration


def index_team():
    index = int(input("Digite o index do time: "))
    return index


def add_team():
    name = str(input("Digite o nome do Time: "))
    team = {"name": name, "players": []}
    teams.append(team)
    print(line(20))


def remove_team():
    index = index_team()
    del teams[index]


def list_team():
    for k, i in enumerate(teams):
        name = i["name"]
        players = len(i["players"])
        print(f"index: {k} \nNome: {name} \nQtd de jogadores: {players}")
        print(line(5))
    print(line(20))


def add_player():
    index = index_team()
    player = str(input("Digite o nome do jogador: "))
    team = teams[index]
    team["players"].append(player)
    print(line(20))


def remove_player():
    index = index_team()
    player = str(input("Digite o nome do jogador: "))
    team = teams[index]
    team["players"].remove(player)


def list_players():
    index = index_team()
    team = teams[index]
    for i in team["players"]:
        print(i)
    return line(20)


def choise(option):
    if option == 1:
        add_team()
    elif option == 2:
        remove_team()
    elif option == 3:
        list_team()
    elif option == 4:
        add_player()
    elif option == 5:
        remove_player()
    elif option == 6:
        list_players()


option = 0
while option != 7:
    menu = """
1 - Adicionar um time
2 - Remover um time
3 - Listar times
4 - Adicionar jogador em um time
5 - Remover jogador em um time
6 - Listar jogadores de um time
7 - Sair
  """
    print(menu)

    option = int(input("Digite sua escolha: "))
    if option == 7:
        print("The end!")
        break
    else:
        choise(option)
