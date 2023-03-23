def epar(x):
    if x % 2 == 0:
        return True
    else:
        return False

while True:
    try:
        num = int(input("Digite um número: "))
        print(epar(num))
        break
    except:
        print('Valor inválido!')