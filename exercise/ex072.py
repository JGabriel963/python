numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    try:
        num = int(input('Digite um número entre 0 e 10: '))
        while num > 10:
            num = int(input('Tente novamente. Digite um número entre 0 e 10: '))
        print(f'Vocẽ digitou o número {numbers[num]}')
    except:
        print('Valor não é um número.')
    option = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while option not in "SN":
        option = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if option == "N":
        break