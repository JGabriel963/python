peso = float(input('Qual o seu peso? (kg) '))
height = float(input('Qual é sua alturaw? (m) '))
imc = peso / (height ** 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print("ABAIXO DO PESO.")
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO.')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBSIDADE MORBIDA')