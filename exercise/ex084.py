people = []
cont = menor = maior = 0
while True:
    dados = []
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    if cont == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cont += 1
    people.append(dados)
    option = input('Quer continuar? [S/N] ').strip().upper()[0]
    while option not in "NS":
        option = input('Por favor, deseja continuar? [S/N] ').strip().upper()[0]
    if option == "N":
        break
print("-=" * 30)
print(f'Ao todo, você cadstrou {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end="")
for i in range(len(people)):
    if people[i][1] == maior:
        print(f'[{people[i][0]}] ', end="")
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end="")
for i in range(len(people)):
    if people[i][1] == menor:
        print(f'[{people[i][0]}] ', end="")
