num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
option = 0
while option != 5:
    print('''       [ 1 ] somar
       [ 2 ] multiplicar
       [ 3 ] maior
       [ 4 ] novos números
       [ 5 ] sair do progama''')
    option = int(input('>>>>> Qual é a sua opção? '))
    if option == 1:
        print(f'A soma entre {num1} + {num2} é {num1 + num2}')
    elif option == 2:
        print(f'O resultado de {num1} x {num2} é {num1 * num2}')
    elif option == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}')
        elif num2 > num1:
            print(f'Entre {num1} e {num2} o maior valor é {num2}')
        else:
            print('Ambos os números são iguais')
    elif option == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')
    else:
        print("Opção inválida. Tente novamente!")
    print('=-=' * 10)