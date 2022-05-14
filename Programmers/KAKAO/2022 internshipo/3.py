import copy

def solution(alp, cop, problems):
    answer = 0


    problems.sort(key=lambda x:-x[0])
    max_alp = problems[0][0]
    problems.sort(key=lambda x:-x[1])
    max_cop = problems[0][1]
    problems.sort(key=lambda x:(-x[4], -x[2], -x[3]))


    done = 0
    for i in range(len(problems)):
        alp += problems[i][2]
        cop += problems[i][3]
        answer += problems[i][4]

        if alp >= max_alp and cop >= max_cop:
            for j in range(i):
                alp -= problems[j][2]
                cop -= problems[j][3]
                if alp >= max_alp and cop >= max_cop:
                    answer -= problems[j][4]
                else:
                    done = 1
                    break
        if done == 1:
            break
    print(alp)
    print(cop)   

    return answer

print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))