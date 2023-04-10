list = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicionao ao final da lista.')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1


