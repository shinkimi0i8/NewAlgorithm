from itertools import product
def solution(numbers, target):
    # l = [(x, -x) for x in numbers]
    # print(l)
    # print(*l)
    # s = list(map(sum, product(*l)))
    # print(s)
    # return s.count(target)
    leaves = [0]

    for num in numbers:
        tmp = []

        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
            print(tmp)

        leaves = tmp

    cnt = 0
    for leaf in leaves:
        if leaf == target:
            cnt += 1

    return cnt


print(solution([4, 1, 2, 1], 4))
