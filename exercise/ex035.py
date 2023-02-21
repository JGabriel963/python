r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')