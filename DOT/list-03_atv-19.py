def divisores(x):
    if type(x) != int or x < 0:
        return Exception
    cont = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cont += 1
    return cont

assert divisores(2) == 2
assert divisores(13) == 2
assert divisores(15) == 4
assert divisores(20) == 6
assert fatorial(-9) == Exception
assert divisores('t') == Exception
assert divisores(True) == Exception
assert divisores(30.7) == Exception
print('Teste OK!')