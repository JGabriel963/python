from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for i in range(7):
    nasc = int(input(f'Em que ano a {i + 1}º pessoa nasceu? '))
    if ano_atual - nasc >= 18:
        maior += 1
    else:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')