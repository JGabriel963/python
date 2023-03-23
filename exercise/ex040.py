nota_1 = float(input("Primeira nota: "))
nota_2 = float(input('Segunda nota: '))
media = (nota_1 + nota_2) / 2
if media < 5:
    print('REPROVADO(A)')
elif 5 < media < 6.9:
    print("RECUPERAÇÃO")
elif media > 7:
    print('APROVADO(A)')