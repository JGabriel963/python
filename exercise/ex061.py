primeiro = int(input("Primeiro termo: "))
razao = int(input('Razão PA: '))
c = 0
pa = primeiro
while c < 10:
    print(f'{pa} -> ', end='')
    pa += razao
    c += 1
print('FIM')