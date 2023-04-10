people = []
person = {}
soma = media = 0
while True:
    try:
        person.clear()
        person['nome'] = input("Nome: ").strip()
        sexo = input("Sexo: [M/F]").strip().upper()[0]
        while sexo not in "MF":
            print("ERRO! Por favor, digite apenas M ou F.")
            sexo = input("Sexo: [M/F]").strip().upper()[0]
        person['sexo'] = sexo
        person['idade'] = int(input("Idade: "))
        soma += person['idade']
        option = input('Quer continuar? [S/N] ').strip().upper()[0]
        while option not in "SN":
            print("ERRO! Responda apenas S ou N.")
            option = input('Quer continuar? [S/N] ').strip().upper()[0]
        people.append(person.copy())
        if option == "N":
            break
    except:
        print('Valor iválido!')
print("-=" * 40)
media = soma / len(people)
print(people)
print(f'A) Ao todo temos {len(people)} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in people:
    if p['sexo'] in "F":
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média:')
for p in people:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print("Encerrado")