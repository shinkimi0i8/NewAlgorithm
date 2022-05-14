def solution(N, stages):
    answer = []

    fail_lst = []


    for n in range(1, N + 1):
        notclear = 0
        arrival = 0
        for stage in stages:
            if stage > n:
                arrival += 1
            elif stage == n:
                arrival += 1
                notclear += 1
        if arrival != 0:
            fail_lst.append((n, notclear / arrival))
        else:
            fail_lst.append((n, 0))
    
    for a in range(N - 1, 0, -1):
        for b in range(a):
            if fail_lst[b][1] < fail_lst[b + 1][1]:
                fail_lst[b], fail_lst[b + 1] = fail_lst[b + 1], fail_lst[b]
    
    
    for ans in fail_lst:
        answer.append(ans[0])
    return answer



print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))