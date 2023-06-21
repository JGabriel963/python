def triangulo(x, y, z):
    if type(x) != int or type(y) != int or type(z) != int:
        return Exception
    if x < y + z and y < x + z and z < x + y:
        if x == y and x == z or y == x and y == z or z == x and z == y:
            return 'Equilátero'
        elif x != y and y == z or x != z and z == y:
            return 'Isóceles'
        elif y != x and x == z or y != z and z == x:
            return 'Isóceles'
        elif z != x and x == y or z != y and y == x:
            return 'Isóceles'
        else:
            return 'Escaleno'

assert triangulo(8, 9, 10) == 'Escaleno'
assert triangulo(7, 7, 7) == 'Equilátero'
assert triangulo(7, 7, 6) == 'Isóceles'
assert triangulo(6, 7, 7) == 'Isóceles'
assert triangulo(7, 6, 7) == 'Isóceles'
assert triangulo(8, 'i', 9) == Exception
assert triangulo(True, 8, 7) == Exception
assert triangulo(5.8, 9, False) == Exception
assert triangulo(9, 6, 8.9) == Exception
assert triangulo('r', 8, 10) == Exception
print('Testes OK!')