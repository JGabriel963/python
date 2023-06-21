def valores_s(n):
    if type(n) != int or n < 0:
        return Exception
    s = 1
    for i in range(n):
        s += 1/(i + 1)
    return s

assert valores_s(1)
assert fatorial(-9) == Exception