def tabuada(x):
    if type(x) != int or x <= 0:
        return Exception
    tab = []
    for i in range(1, x + 1):
        tab.append(x * i)
    return tab

assert tabuada(1) == [1]
assert tabuada(5) == [5, 10, 15, 20, 25]
assert tabuada(10) == [10, 20, 30, 40, 60, 70, 80, 90, 100]
assert tabuada(3.5) == Exception
assert tabuada(0) == Exception
assert tabuada(-5) == Exception
assert tabuada("7") == Exception
assert tabuada(True) == Exception
assert tabuada(False) == Exception

print("Teste OK")