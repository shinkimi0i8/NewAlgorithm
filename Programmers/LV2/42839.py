from itertools import permutations


def solution(numbers):
    answer = 0
    num_lst = []
    for i in range(len(numbers)):
        num_lst.append(numbers[i])
    perm_lst = []
    tmp_lst = []
    for j in range(1, len(num_lst) + 1):
        tmp_lst = list(permutations(num_lst, j))
        for k in range(len(tmp_lst)):
            tmp = ''
            for l in range(len(tmp_lst[k])):
                tmp += tmp_lst[k][l]
            perm_lst.append(int(tmp))
    perm_lst = list(set(perm_lst))
    if 0 in perm_lst:
        perm_lst.remove(0)
    if 1 in perm_lst:
        perm_lst.remove(1)

    for perm in perm_lst:
        failure = 0
        for p in range(2, perm // 2 + 1):
            if perm % p == 0:
                failure = 1
                break
        if failure != 1:
            answer += 1

    return answer


print(solution('17'))
print(solution('011'))
