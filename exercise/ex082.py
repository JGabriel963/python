list = []
list_par = []
list_impar = []
while True:
    try:
        n = int(input('Digite um número: '))
        list.append(n)
        option = input("Quer continuar? [S/N] ").strip().upper()[0]
        while option not in "NS":
            option = input("Quer continuar? [S/N] ").strip().upper()[0]
        if option == "N":
            break
    except:
        print('Valor inválido. Tente novamente.')
print("-=" * 40)
print(f'A lista completa é {list}')
for i in range(len(list)):
    if list[i] % 2 == 0:
        list_par.append(list[i])
print(f'A lista de pares é {list_par}')
for i, v in enumerate(list):
    if v % 2 == 1:
        list_impar.append(v)
print(f'A lista de ímpares é {list_impar}')