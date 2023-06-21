def positivo_negativo(x):
    if type(x) != int:
        return Exception
    return True if x >= 0 else False

assert positivo_negativo(3) == True
assert positivo_negativo(5) == True
assert positivo_negativo(-7) == False
assert positivo_negativo(-67) == False
assert positivo_negativo("12") == Exception
assert positivo_negativo(True) == Exception
assert positivo_negativo(False) == Exception
assert positivo_negativo(10.5) == Exception

print("Testes OK!!")