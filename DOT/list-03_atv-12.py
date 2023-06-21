def ordem(x, y):
    if type(x) != int or type(y) != int:
        return Exception
    ordem = [x, y]
    ordem.sort()
    return ordem


assert ordem(3, 5) == [3, 5]
assert ordem(8, 4) == [4, 8]
assert ordem(3, -2) == [-2, 3]
assert ordem(-5, -6) == [-6, -5]
assert ordem(True, 8) == Exception
assert ordem(False, 30) == Exception
assert ordem(8, True) == Exception
assert ordem(30, False) == Exception
assert ordem("40", 60) == Exception
assert ordem(80, "28") == Exception

print("Teste Ok")