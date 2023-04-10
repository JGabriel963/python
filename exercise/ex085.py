list = [[], []]
for i in range(7):
    value = int(input(f'Digite o {i + 1}º valor: '))
    if value % 2 == 0:
        list[0].append(value)
    else:
        list[1].append(value)

print('-=' * 30)
list[0].sort()
list[1].sort()
print(f'Os valores pares digitados foram: {list[0]}')
print(f'Os valores ímpares digitados foram: {list[1]}')