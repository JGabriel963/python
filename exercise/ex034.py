salario = float(input("Qual o salário do funcionário? R$"))
aumento = 0
if salario > 1250:
    aumento = salario + ((salario * 10 )/ 100)
else:
    aumento = salario + ((salario * 15) / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora.')