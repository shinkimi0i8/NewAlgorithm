from itertools import permutations

def solution(expression):
    answer = 0
    arranged = []
    
    tmp_idx = 0

    for i in range(len(expression)):
        if expression[i].isdigit() == False:
            arranged.append(expression[tmp_idx:i])
            arranged.append(expression[i])
            tmp_idx = i+1
    arranged.append(expression[tmp_idx:])

    buho_nums = len(arranged) // 2

    order = list(permutations(range(buho_nums), buho_nums))
    
    answer_lst = []




    return answer

print(solution("100-200*300-500+20"))