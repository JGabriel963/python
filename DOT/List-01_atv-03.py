def celsius(t):
    return ((t - 32) / 9) * 5

while True:
    try:
        temperatura = float(input('Informe uma temperatura em Fahrenheit: '))
        print(f'{celsius(temperatura):.2f}ºC')
        break
    except:
        print('Valor iválido!')