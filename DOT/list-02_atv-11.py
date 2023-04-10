people = []
def cadastrar():
    if len(people) == positions:
        return print('Não é possível cadastrar mais nomes')
    else:
        nome = input('Cadastre um nome: ')
        people.append(nome)
    print('Cadastro realizado com sucesso!')

def pesquisar():
    option = str(input('Pesquisar usuário por nome(1) ou por índice(2)? ')).strip().upper()[0]
    while option not in "12":
        option = str(input('Pesquisar usuário por nome(1) ou por índice(2)? ')).strip().upper()[0]
    if option == "1":
        nome = input('Digite o nome que deseja consultar:_')
        if nome in people:
            for i, v in enumerate(people):
              if nome == v:
                  print(f'O nome {v} está na posição {i} da Lista.')
        else:
            print(f'{nome} não está inserido na lista!')
    elif option == "2":
        print('Ainda não está disponível esta opção! Thanks')


def listar():
    for i,v in enumerate(people):
        print(f'Posição {i}: {v}')

def delete():
    option = input('Excluir nome por posição(I) ou por nome(N)?_').strip().upper()[0]
    while option not in "IN":
        option = input('Excluir nome por posição(I) ou por nome(N)?_').strip().upper()[0]
    if option == "I":
        index = int(input('Digite o indice do nome que deseja excluir:_'))
        if index < 0 or index >= len(people):
            print('Não há esta posição na lista!')
        else:
            print(f'{people[index]} será excluido da lista!')
            del people[index]
    elif option == 'N':
        print("Esta função ainda não está disponível!!")


positions = int(input('Digite o número de posições da lista:_'))

while True:
    try:
        print('=' * 10 + 'MENU' + '=' * 10)
        print('''        1) Cadastrar nome
        2) Pesquisar nome
        3) Listar todos os nomes
        4) Excluir nome
        0) Sair do programa ''')
        option = int(input('Digite sua escolha:_'))
        if option == 1:
            cadastrar()
        elif option == 2:
            pesquisar()
        elif option == 3:
            listar()
        elif option == 4:
            delete()
        elif option == 0:
            break
    except:
        print('Valor inválido!')