def comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return f'{dia1}/{mes1}/{ano1}'
    elif ano2 > ano1:
        return f'{dia2}/{mes2}/{ano2}'
    elif mes1 > mes2:
        return f'{dia1}/{mes1}/{ano1}'
    elif mes2 > mes1:
        return f'{dia2}/{mes2}/{ano2}'
    elif dia1 > dia2:
        return f'{dia1}/{mes1}/{ano1}'
    elif dia2 > dia1:
        return f'{dia2}/{mes2}/{ano2}'
    else:
        return "As datas são iguais"

print("Digite a primeira data:")
dia1 = int(input("Dia: "))
mes1 = int(input("Mês: "))
ano1 = int(input("Ano: "))

# Lê a segunda data
print("Digite a segunda data:")
dia2 = int(input("Dia: "))
mes2 = int(input("Mês: "))
ano2 = int(input("Ano: "))

# Chama a função comparar_datas e imprime a mensagem retornada
mensagem = comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2)
print(mensagem)