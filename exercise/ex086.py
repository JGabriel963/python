matriz = [[], [], []]
for i in range(3):
    for c in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))

print("-=" * 30)
for i in range(3):
    for c in range(3):
        print(f'[ {matriz[0][i]} ] ', end="")
    print()


