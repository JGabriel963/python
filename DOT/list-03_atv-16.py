def media(arr):
    if len(arr) == 0:
        return Exception
    sum = 0
    for i in range(len(arr)):
        if type(arr[i]) != int or arr[i] < 0:
            return Exception
        sum += arr[i]
    return sum / len(arr)

assert media([1, 1, 1, 1, 1, 1]) == 1
assert media([1, 2, 4, 5]) == 3
assert media([10]) == 10
assert media([6]) == 6
assert media([]) == Exception
assert media([-7, 8]) == Exception
assert media([8, -7]) == Exception
assert media(["7", 10]) == Exception
assert media([True]) == Exception
assert media([{}]) == Exception

print("Teste OK")