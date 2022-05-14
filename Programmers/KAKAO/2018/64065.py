def solution(s):
    total_lst = []
    tmp_lst = []
    s = s[1:-1]
    for i in range(len(s)):
        if s[i] == '{' or s[i] == '\'':
            continue
        elif s[i] == ',':
            s[i-1] == '}'
        elif s[i] == '}':

            total_lst.append(tmp_lst)
            tmp_lst = []
        else:
            tmp_lst.append(int(s[i]))
    total_lst.sort(key=len)
    answer = []

    for j in range(len(total_lst)):
        if total_lst[j][-1] not in answer:
            answer.append(total_lst[j][-1])
        else:
            x = -1
            while total_lst[j][x] in answer:
                x -= 1
            answer.append(total_lst[j][x])

    return answer


print(solution("{{20,111},{111}}"))