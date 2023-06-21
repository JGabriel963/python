def potencia(x, z):
    if type(x) != int or type(z) != int:
        return Exception
    return x ** z

assert potencia(2, 2) == 4
assert potencia(3, 3) == 27
assert potencia(2, 4) == 16
assert potencia(True, 8) == Exception
assert potencia(9, 2.7) == Exception
assert potencia('r', 9) == Exception
print('Teste OK!')