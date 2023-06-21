def categoria(x):
    if type(x) != int or x < 5:
        return Exception
    if 5 <= x <= 7:
        return "Infantil A"
    elif 8 <= x <= 10:
        return "Infantil B"
    elif 11 <= x <= 13:
        return "Juvenil A"
    elif 14 <= x <= 17:
        return "Juvenil B"
    elif x >= 18:
        return "Adulto"

assert categoria(5) == "Infantil A"
assert categoria(7) == "Infantil A"
assert categoria(8) == "Infantil B"
assert categoria(10) == "Infantil B"
assert categoria(11) == "Juvenil A"
assert categoria(13) == "Juvenil A"
assert categoria(14) == "Juvenil B"
assert categoria(17) == "Juvenil B"
assert categoria(18) == "Adulto"
assert categoria(30) == "Adulto"
assert categoria("12") == Exception
assert categoria(True) == Exception
assert categoria(False) == Exception
assert categoria(3) == Exception
assert categoria(-7) == Exception
assert categoria(10.5) == Exception
print("Testes OK!!")