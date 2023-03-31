soma = qtd = 0
while True:
    value = int(input('Digite um valor (999 para parar): '))
    if value == 999:
        break
    qtd += 1
    soma += value
print(f'A soma dos {qtd} valores foi {soma}')