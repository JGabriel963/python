num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'"{i}"', end=" ")
        cont += 1
    else:
        print(i, end=" ")
print()
print(f'O número {num} foi divisível {cont} vezes')
if cont == 2:
    print("É PRIMO!")
else:
    print('NÃO É PRIMO!')
