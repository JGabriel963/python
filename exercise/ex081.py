list = []
while True:
    try:
        value = int(input('Digite um valor: '))
        list.append(value)
        option = input('Quer continuar? [S/N] ').strip().upper()[0]
        while option not in "SN":
            option = input('Quer continuar? [S/N] ').strip().upper()[0]
        if option == "N":
            break
    except:
        print('Valor inválido.')
print(f'Você digitou {len(list)} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decresente são {list}')
if 5 in list:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')