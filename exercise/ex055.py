qtd = menor = maior = 0
for i in range(5):
    weight = float(input(f'Peso da {i + 1}º pessoa: '))
    qtd += 1
    if qtd == 1:
        menor = maior = weight
    else:
        if weight > maior:
            maior = weight
        elif weight < menor:
            menor = weight
print(f'O maior peso lido foi de {maior}')
print(f'O menor peso lido foi de {menor}')

