def peso_ideal(h, s):
    if s not in "MFmf" or type(s) != str and type(h) != float or h <= 0:
        return Exception
    if s in "Mm":
        return round(72.7 * h - 58, 2)
    if s in "Ff":
        return round(62.1 * h - 44.7, 2)

assert peso_ideal(1, "M") == 14.70
assert peso_ideal(1, "F") == 17.40
assert peso_ideal(1.60, "F") == 54.66
assert peso_ideal(1.76, "M") == 69.95
assert peso_ideal(0, "M") == Exception
assert peso_ideal(-1.60, "m") == Exception
assert peso_ideal(0, "f") == Exception
assert peso_ideal(-1.76, "F") == Exception
assert peso_ideal(1.58, "h") == Exception
assert peso_ideal(1.80, "k") == Exception


print("Testes OK")