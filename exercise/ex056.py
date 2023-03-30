women = soma = velho = 0
nome_velho = ''
for i in range(4):
    print("-" * 5 + f' {i + 1}º PESSOA ' + "-" * 5)
    name = input('Nome: ')
    age = int(input("Idade: "))
    if i == 0:
        velho = age
        nome_velho = name
    else:
        if age > velho:
            velho = age
            nome_velho = name
    soma += age
    sexo = input("Sexo [M/F]: ").strip().upper()[0]
    if sexo == "F" and age < 20:
        women += 1
print(f'A média de idade do grupo é de {(soma / 4):.1f} anos.')
print(f'O homem mais velho tem {velho} anos e se chama {nome_velho}.')
print(f'Ao todo são {women} mulheres com menos de 20 anos.')