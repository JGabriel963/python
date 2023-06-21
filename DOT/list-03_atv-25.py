def fatorial(x):
    if type(x) != int or x < 0:
        return Exception
    fat = 1
    for i in range(2, x + 1):
        fat *= i
    return fat

assert fatorial(5) == 120
assert fatorial(6) == 720
assert fatorial(8) == 40320
assert fatorial(9) == 362880
assert fatorial(-9) == Exception
assert fatorial('t') == Exception
assert fatorial(True) == Exception
assert fatorial(30.7) == Exception
print('Teste OK')