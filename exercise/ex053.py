frase = input('Digite um frase: ').strip().upper()
words = frase.split()
together = ''.join(words)
inverse = ''
for l in range(len(together) - 1, - 1, -1):
    inverse += together[l]
print(f'O inverso de {frase} é {inverse}')
if inverse == frase:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
