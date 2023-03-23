def area(r):
    return 3.14 * (r ** 2)
def perimetro(r):
    return 3.14 * r * 2

while True:
    try:
        raio = float(input("Informe o raio do circulo: "))
        if raio != 0:
            print(area(raio))
            print(perimetro(raio))
            break
        else:
            print('Informe um número diferente de 0')
    except:
        print('Valor inválido!')