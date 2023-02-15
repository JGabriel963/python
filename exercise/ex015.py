# 60 reais por dia e 0.15 por Km
days = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pay = (days * 60) + (km * 0.15)
print(f'O total a pagar é de R${pay:.2f}')