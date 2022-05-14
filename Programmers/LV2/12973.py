# https://programmers.co.kr/learn/courses/30/lessons/12973

'''
소문자 문자열로 시작
문자열에서 같은 알파벳 2개가 붙어있는 짝을 찾는다.
그 둘을 제거한뒤, 앞뒤로 문자열을 이어 붙임
문자열을 모두 제거할 수 있다면 1, 아니면 0을 반환

'''


def solution(s):
    answer = -1
    new_str = [s[0]]

    while True:
        done = 0
        for i in range(1, len(s)):
            if len(new_str) == 0:
                new_str.append(s[i])
            else:
                if new_str[-1] == s[i]:
                    new_str.pop()
                    done = 1
                else:
                    new_str.append(s[i])

        s = new_str

        if done == 0:
            answer = 0
            break
        if len(s) == 0:
            answer = 1
            break

    return answer


# def solution(s):
#     answer = -1
#     new_str = s[0]

#     while True:
#         done = 0
#         for i in range(1, len(s)):
#             if len(new_str) == 0:
#                 new_str += s[i]
#             else:
#                 if new_str[-1] == s[i]:
#                     new_str = new_str[:-1]
#                     done = 1
#                 else:
#                     new_str += s[i]

#         s = new_str

#         if done == 0:
#             answer = 0
#             break
#         if len(s) == 0:
#             answer = 1
#             break

#     return answer

print(solution('baabaa'))
print(solution('cdcd'))
