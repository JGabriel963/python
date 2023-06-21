def par_impar(x):
    if type(x) != int:
        return Exception
    return True if x % 2 == 0 else False

assert par_impar(6) == True
assert par_impar(7) == False
assert par_impar(-7) == False
assert par_impar(-67) == False
assert par_impar(-24) == True
assert par_impar(-80) == True
assert par_impar("12") == Exception
assert par_impar(True) == Exception
assert par_impar(False) == Exception
assert par_impar(10.5) == Exception
print("Testes OK!!")