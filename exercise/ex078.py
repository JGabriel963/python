list = []
maior = menor = 0
for i in range(5):
    value = int(input(f'Digite um valor para a Posição {i}: '))
    if i == 0:
        maior = menor = value
    else:
        if value > maior:
            maior = value
        if value < menor:
            menor = value
    list.append(value)
print("=-" * 30)
print(f'Você digitou os valores {list}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(list):
    if v == maior:
        print(f'{i}...')
print(f'O menor valor digitado foi {menor} nas posições', end='')
for i, v in enumerate(list):
    if v == menor:
        print(f'{i}...')
