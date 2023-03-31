from random import randint
win = 0
while True:
    try:
        computador = randint(1, 10)
        value = int(input('Digite um valor: '))
        option = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
        while option not in "PI":
            option = input('Informe sua escolha. Par ou Ímpar? [P/I] ').strip().upper()[0]
        print('-' * 50)
        print(f'Você jogou {value} e o computador {computador}. ', end='')
        if (value + computador) % 2 == 0:
            print(f'Total de {value + computador} DEU PAR')
            print('-' * 50)
            if option == "P":
                print("Você VENCEU!")
                win += 1
                print("Vamos jogar novamente...")
                print('=-' * 15)
            else:
                print("Você PERDEU!")
                break
        else:
            print(f'Total de {value + computador} DEU ÍMPAR')
            print('-' * 50)
            if option == "I":
                print("Você VENCEU!")
                win += 1
                print("Vamos jogar novamente...")
                print('=-' * 15)
            else:
                print("Você PERDEU!")
                break
    except:
        print('Valores inválido!')

print(f'GAME OVER! Você venceu {win} vezes.' if win > 1 else f'GAME OVER! Você venceu {win} vez.')
print('=-' * 15)