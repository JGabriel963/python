option = 'S'
qtd = soma = menor = maior = 0
while option in "S":
    num = int(input('Digite um número: '))
    qtd += 1
    option = input('Quer continua? [S/N] ').upper().strip()[0]
    while option not in "SN":
        option = input('Por favor, deseja continua? [S/N] ').upper().strip()[0]
    soma += num
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {qtd} números e a média foi {(soma / qtd):.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

