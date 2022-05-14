def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key = len)
    tmp = ''
    for i in s:
        ele = i.split(',')
        for j in ele:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))