aluno = {}
aluno['nome'] = input('Nome: ').strip()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situação'] = "Reprovado"
elif aluno['media'] < 7:
    aluno['situação'] = "Recuperação"
else:
    aluno['situação'] = "Aprovado"
print('-=' * 30)
for k, v in aluno.items():
    print(f'   - {k} é igual a {v}')