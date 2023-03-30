primeiro = int(input("Primeiro termo: "))
razao = int(input('Razão PA: '))
c = 1
pa = primeiro
more = 10
total = 0
while more != 0:
    total = total + more
    while c <= total:
        print(f'{pa} -> ', end='')
        pa += razao
        c += 1
    print('PAUSA')
    c = 1
    more = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM')
