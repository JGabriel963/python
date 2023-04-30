def perfect(x):
    if type(x) == str or type(x) == bool or type(x) == float or x < 1:
        return Exception
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    if sum == x:
        return True
    else:
        return False

assert perfect(6) == True
assert perfect(28) == True
assert perfect(496) == True
assert perfect(8128) == True
assert perfect(7) == False
assert perfect(100) == False
assert perfect(0) == Exception
assert perfect(-1) == Exception
assert perfect("6") == Exception
assert perfect(6.2) == Exception
assert perfect(True) == Exception
assert perfect(False) == Exception

print('Testes OK!!')