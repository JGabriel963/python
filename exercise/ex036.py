house = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
years = int(input("Quantos anos de financiamento: "))
prestacao = house / (years * 12)
print(f'Para pagar uma casa de R${house:.2f} em {years} anos a prestação será de R${prestacao}')
if prestacao < (salario * 30) / 100:
    print("Empréstimo pode ser CONCEBIDO!")
else:
    print("Empréstimo NEGADO!")