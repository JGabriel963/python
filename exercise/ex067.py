while True:
    try:
        value = int(input('Quer ver a tabuada de qual valor? '))
        if value < 0:
            break
        print('-' * 20)
        for i in range(1, 10 + 1):
            print(f'{value} x {i} = {value * i}')
        print('-' * 20)
    except:
        print('Valor inválido! Tente novamente.')
print('PROGRAMA DE TABUADA ENCERRADO.')