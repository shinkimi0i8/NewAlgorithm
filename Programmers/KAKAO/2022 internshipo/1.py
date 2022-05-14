def solution(survey, choices):
    answer = ''
    
    personality = {
        'A': 0,
        'N': 0,
        'C': 0,
        'F': 0,
        'M': 0,
        'J': 0,
        'R': 0,
        'T': 0
    }
 
    lst = [('R', 'T'),('C', 'F'),('J', 'M'),('A', 'N')]

    for i in range(len(choices)):
        if choices[i] > 4:
            if choices[i] == 5:
                personality[survey[i][1]] += 1
            elif choices[i] == 6:
                personality[survey[i][1]] += 2
            elif choices[i] == 7:
                personality[survey[i][1]] += 3
        
        elif choices[i] < 4:
            if choices[i] == 3:
                personality[survey[i][0]] += 1
            elif choices[i] == 2:
                personality[survey[i][0]] += 2
            elif choices[i] == 1:
                personality[survey[i][0]] += 3
    for ele in lst:
        if personality[ele[0]] > personality[ele[1]]:
            answer += ele[0]
        elif personality[ele[0]] < personality[ele[1]]:
            answer += ele[1]
        else:
            answer += min(ele[0], ele[1])


    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))