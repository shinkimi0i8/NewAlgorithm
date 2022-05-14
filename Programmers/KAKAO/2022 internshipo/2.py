from collections import deque
import copy


def solution(queue1, queue2):
    copy1 = deque(copy.deepcopy(queue1))
    copy2 = deque(copy.deepcopy(queue2))

    answer = -1
    goal = sum(queue1 + queue2) / 2

    
    success = 0
    cnt1 = 0

    for i in range(len(queue1)):
        copy1 = deque(copy.deepcopy(queue1))
        copy2 = deque(copy.deepcopy(queue2))
        for j in range(len(queue2)):
            copy1.append(copy2.popleft())
            cnt1 += 1
            if sum(copy1) == goal:
                success = 1
                break
        if success == 1:
            break
        print(queue1)
        
        queue2.append(queue1.popleft())
        print(queue2)
        cnt1 += 1

    cnt2 = 0
    for i in range(len(queue2)):
        for j in range(len(queue1)):
            queue2.append(queue1.popleft())
            cnt2 += 1
            if sum(queue2) == goal:
                success = 2
                break
        if success == 2:
            break

        queue2.append(queue1.popleft())
        cnt2 += 1

    cnt = max(cnt1, cnt2)
    if success == 1 or success == 2:
        return cnt
    else:
        return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))