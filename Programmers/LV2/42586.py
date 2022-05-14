import math


def solution(progresses, speeds):
    answer = []
    max_time = 0

    for i in range(len(progresses)):
        # 최대시간은 항상 그 날을 넘으니까 반올림 아닌 올림
        x = math.ceil((100 - progresses[i]) / speeds[i])
        if x >= max_time:
            max_time = x
    cnt = 0

    # 최종 결과가 max_time을 넘기지 않으므로 그 안에서 for문
    for j in range(max_time + 1):
        if progresses[0] + j * speeds[0] >= 100:
            cnt += 1
            progresses = progresses[1:]
            speeds = speeds[1:]
            while progresses:
                if progresses[0] + j * speeds[0] >= 100:
                    cnt += 1
                    progresses = progresses[1:]
                    speeds = speeds[1:]
                else:
                    break

        if cnt > 0:
            answer.append(cnt)
            cnt = 0

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
