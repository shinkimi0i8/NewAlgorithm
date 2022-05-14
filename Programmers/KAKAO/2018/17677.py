import copy

def gather(str1):
    lst = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            lst.append(str1[i]+str1[i+1])
    return lst


def solution(str1, str2):

    lst1 = gather(str1.lower())
    lst2 = gather(str2.lower())
    if len(lst1) > len(lst2):
        lst1, lst2 = lst2, lst1


    tmp = copy.deepcopy(lst2)
    lst2_1 = copy.deepcopy(lst2)
    gyo = 0
    hap = len(tmp)

    for i in lst1:
        if i in lst2:
            gyo += 1
            lst2.remove(i)
            continue
    for j in lst1:
        if j in lst2_1:
            lst2_1.remove(j)
            continue
        else:
            hap += 1

    if hap != 0:
        answer = int(gyo/hap * 65536)
    else:
        answer = 65536
    return answer


print(solution("FRANCE", "french"))