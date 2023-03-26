soma = 0
for i in range(6):
    num = int(input(f"Digite o {i + 1}º número: "))
    if num % 2 == 0:
        soma += num
print(f'A soma de todos os número pares lido é {soma}')