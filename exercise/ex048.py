cont = 0
soma = 0
for i in range(1, 500 + 1):
    if i % 2 == 1 and i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma de todos os {cont} valores solicitador é {soma}')