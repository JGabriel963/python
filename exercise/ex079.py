numbers = []
while True:
    value = int(input('Digite um valor: '))
    if value not in numbers:
        numbers.append(value)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    option = input('Quer continuar? [S/N] ').strip().upper()[0]
    while option not in "SN":
        option = input('Por favor, informe se desja continuar: [S/N] ').strip().upper()[0]
    if option == "N":
        break
numbers.sort()
print(f'Você digitou os valores {numbers}')