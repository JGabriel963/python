def days(a, m, d):
    if type(a) == str or type(a) == bool or type(a) == float or type(m) == str or type(m) == bool or type(m) == float or type(d) == str or type(d) == bool or type(d) == float or a < 0 or m < 0 or d < 0:
        return Exception
    return (a * 365) + (m * 30) + d

assert days(2023, 1, 1) == 738426
assert days(2020, 3, 13) == 737403
assert days(2002, 12, 6) == 731096
assert days(1994, 0, 28) == 727838
assert days(0, 8, 30) == 270
assert days(2019, 7, 0) == 737145
assert days("2002", 12, 6) == Exception
assert days(2002, '12', 6) == Exception
assert days(2002, 12, "12") == Exception
assert days(True, 4, 6) == Exception
assert days(2005.5, 8, 27) == Exception
assert days(2008, False, 30) == Exception
assert days(2008, 3.7, 30) == Exception
assert days(2012, 5, True) == Exception
assert days(2004, 5, 12.9) == Exception
assert days(-2004, 6, 4) == Exception
assert days(2004, -6, 4) == Exception
assert days(2004, 7, -3) == Exception


print('Testes OK!!')