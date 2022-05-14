'''
cpp, java, python 중 하나
백, 프론트 중 하나
주니어, 시니어 중 하나
피자, 치킨 중 하나

'''

def solution(info, query):
    
    for i in range(len(info)):
        info[i] = set(info[i].split())

    for j in range(len(query)):
        query[j] = list(query[j].split())
        while len(query[j]) != 5:
            query[j].remove('and')
    
    answer = []
    tmp = []

    for k in range(len(query)):
        value = 0
        tmp = []
        for x in range(len(info)):
            cnt = 0
            for l in range(4):
                if query[k][l] != '-':
                    if query[k][l] not in info[x]:
                        # print(query[k][l], info[x])
                        break
                    else:
                        # print('else 문', query[k][l], info[x])
                        cnt += 1
                        if cnt == 4:
                            tmp.append(sorted(info[x]))
                else:
                    cnt += 1
                    if cnt == 4:
                        tmp.append(sorted(info[x]))
                        
        if tmp:
            for a in range(len(tmp)):
                if int(tmp[a][0]) >= int(query[k][4]):
                    value += 1

            answer.append(value)
           
            

    return answer

print(solution(	["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))