def solution(n, arr1, arr2):

    array1 = []
    array2 = []
    mix = ['' for _ in range(n)]
    print(mix)

    for element in arr1:
        element = str(bin(element))[2:]
        while len(element) < n:
            element = '0' + element
        tmp = []
        for num in element:
            tmp.append(int(num))
        array1.append(tmp)

    for element in arr2:
        element = str(bin(element))[2:]
        while len(element) < n:
            element = '0' + element
        tmp = []
        for num in element:
            tmp.append(int(num))
        array2.append(tmp)

    for i in range(n):
        for j in range(n):
            if (array1[i][j] - 1) * (array2[i][j] - 1) > 0:
                mix[i] += ' '
            else:
                mix[i] = str(mix[i]) + '#'

    print(mix)
    return mix


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
