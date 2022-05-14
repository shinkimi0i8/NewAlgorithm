from collections import deque


def solution(scoville, K):
    scoville.sort()

    cnt = 0
    while True:
        scoville = deque(scoville)
        a = scoville.popleft()
        b = scoville.popleft()
        c = a + 2 * b
        scoville.append(c)
        list(scoville).sort()
        cnt += 1
        if scoville[0] >= K:
            break

        if len(scoville) == 2:
            if scoville[0] + 2 * scoville[1] < K:
                return -1
    return cnt


print(solution([1, 2, 3, 9, 10, 12], 7))
