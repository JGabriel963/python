while True:
    try:
        numbers = []
        n = int(input('Quantos números deseja inserir na lista? '))
        for i in range(n):
            numbers.append(int(input(f'{i + 1}º valor: ')))
        numbers.reverse()
        print(numbers)
        break
    except:
        print('Valor inválido')