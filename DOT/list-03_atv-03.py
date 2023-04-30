def prime(x):
    if type(x) == str or type(x) == bool or type(x) == float:
        return Exception
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

assert prime(0) == False
assert prime(1) == False
assert prime("1") == Exception
assert prime(2) == True
assert prime(3) == True
assert prime(True) == Exception
assert prime(6) == False
assert prime(13) == True
assert prime(13.5) == Exception
assert prime(37) == True
assert prime(50) == False
assert prime(101) == True

print('Testes OK!')