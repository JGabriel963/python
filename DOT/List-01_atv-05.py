def peso_ideal(h, s):
    if s == 1:
        return f'Peso ideal: {((62.1 * h) - 58):.2f}'
    elif s == 2:
        return f'Peso ideal: {((72.7 * h) - 44.7):.2f}'

while True:
    try:
        altura = float(input("Digite sua altura: "))
        sexo = int(input("Informe seu sexo: (1 - femenino / 2 - masculino) "))
        if sexo == 1 or sexo ==2:
            print(peso_ideal(altura, sexo))
            break
        else:
            print('Opção para sexo inválida! Tente novamente. ', end='')
    except:
        print("Valor inválido!")