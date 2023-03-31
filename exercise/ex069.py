def line():
    print('-' * 20)

maior = men = women = 0
while True:
    try:
        line()
        print('CADASTRE UMA PESSOA')
        line()
        age = int(input('Idade: '))
        if age > 18:
            maior += 1
        sex = input('Sexo: [M/F] ').strip().upper()[0]
        while sex not in "MF":
            sex = input('Por favor, insira seu sexo: [M/F]').strip().upper()[0]
        if sex == "M":
            men += 1
        if sex == "F" and age < 20:
            women += 1
        line()
        option = input('Quer continuar? [S/N] ').strip().upper()[0]
        while option not in "SN":
            option = input('Valor inválido. Desja continuar? [S/N] ').strip().upper()[0]
        if option == "N":
            break
    except:
        print('Valor inválido. Tente novamente.')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {men} homem cadastrado' if men == 1 else f'Ao todo temos {men} homens cadastrados')
print(f'E temos {women} mulher com menos de 20 anos' if women == 1 else f'E temos {women} mulheres com menos de 20 anos.')