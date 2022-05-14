import copy

def solution(n, times):
    answer = 0
    times_copy = copy.deepcopy(times)
    # 아직 대기실에 남은 사람
    left -= len(times)

    # 최종 소요시간 (짧게 걸리는 시간을 기준으로 반복)
    answer += min(times)
    
    # 어차피 가장 짧게 걸리는 아이를 기준으로 항상 구분이 되게 되어있음
    while left > 0:
        n -= len(times)
        answer += min(times)

    return answer


print(solution(6, [7, 10]))