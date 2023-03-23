def media(n1, n2):
    m = (n1 + n2) / 2
    if m >= 6:
        return f'Media: {m:.2f}\nPARABÉNS! Você foi aprovado'
    else:
        return f'Media: {m:.2f}'

while True:
    try:
        nota1 = float(input('Informe a primeira nota: '))
        nota2 = float(input("Informe a segunda nota: "))
        print(media(nota1, nota2))
        break
    except:
        print("Valor inválido")