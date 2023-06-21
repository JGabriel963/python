def conceito(x):
    if type(x) != float or x < 0 or x > 10:
        return Exception
    if 0.0 <= x <= 4.9:
        return "D"
    elif 5 <= x <= 6.9:
        return "C"
    elif 7 <= x <= 8.9:
        return "B"
    elif 9 <= x <= 10:
        return "A"

assert conceito(0.0) == "D"
assert conceito(4.9) == "D"
assert conceito(5.00001) == "C"
assert conceito(6.9) == "C"
assert conceito(7.) == "B"
assert conceito(8.9) ==  "B"
assert conceito(9.) ==  "A"
assert conceito(10.) ==  "A"
assert conceito("12") == Exception
assert conceito(True) == Exception
assert conceito(False) == Exception
assert conceito(3) == Exception
assert conceito(-7) == Exception
assert conceito(10.5) == Exception

print("Testes OK!!")