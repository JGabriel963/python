def intercalar(arr1, arr2):
    list3 = []
    for i in range(10):
        list3.append(list1[i])
        list3.append(list2[i])

    return list3


while True:
    try:
        list1 = []
        list2 = []
        for i in range(10):
            num = int(input(f'{i + 1}º elemento da Lista 1: '))
            list1.append(num)
        for i in range(10):
            num = int(input(f'{i + 1}º elemento da Lista 2: '))
            list2.append(num)
        print(intercalar(list1, list2))
        break
    except:
        print('Valor inválido. Tente novamente!')