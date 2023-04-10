ficha = []
while True:
    name = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([name, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    while resp not in "SN":
        resp = input('Por favor, deseja continuar? [S/N] ').strip().upper()[0]
    if resp == "N":
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        break
    print(f'Notas de {ficha[notas][0]} são {ficha[notas][1]}')