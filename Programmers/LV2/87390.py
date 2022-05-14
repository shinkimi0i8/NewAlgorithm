


def solution(n, left, right):
    tmp = []

    for i in range(left, right+1):
        if i % n > (i // n):
            tmp.append(i % n + 1)
        else:
            tmp.append(i // n + 1)

    
    return tmp


print(solution(4, 7, 14))


# 시간초과

# def solution(n, left, right):
#     tmp = [[0 for _ in range(n)] for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             if i > j:
#                 tmp[i][j] = i+1
#             else:
#                 tmp[i][j] = j+1

#     answer = []

#     for k in range(n):
#         answer += tmp[k]


#     answer = answer[left:right+1]

#     return answer


# print(solution(4, 7, 14))
