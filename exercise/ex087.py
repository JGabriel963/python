matriz = [[], [], []]
soma = soma_3 = maior = 0
for i in range(3):
    for c in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))

print("-=" * 30)
for i in range(3):
    for c in range(3):
        print(f'[ {matriz[i][c]} ] ', end="")
        if matriz[i][c] % 2 == 0:
            soma += matriz[i][c]
    print()
print("-=" * 30)
print(f'A soma dos valores pares é {soma}')
for i in range(3):
    soma_3 += matriz[2][i]
print(f'A soma dos valores da terceira coluna é {soma_3}')
for i in range(3):
    if i == 0:
        maior = matriz[1][i]
    else:
        if matriz[1][i] > maior:
            maior = matriz[1][i]
print(f'O maior valor da segunda linha é {maior}.')