stop = 0
soma = 0
cont = 0
while stop != 999:
    stop = int(input('Digite um número [999 para parar]: '))
    if stop != 999:
        cont += 1
        soma += stop
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')