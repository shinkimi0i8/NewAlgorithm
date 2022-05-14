'''
스카피 = 새로운 메뉴
기존에는 단품으로
코스요리로 재구성
이전에 가장 많이 함께 주문한 단품 메뉴를 코스로
단 코스요리 메뉴는 최소 2가지 이상의 단품메뉴
최소 2명 이사으이 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보
'''

from itertools import combinations

def solution(orders, course):
    answer = []

    for cour in course:
        comb = []
        comb_dict = {}
        for order in orders:
            comb = comb + list(combinations(sorted(order), cour))
        print(comb)
        for co in comb:
            if co in comb_dict:
                comb_dict[co] += 1
            else:
                comb_dict[co] = 1

        print(comb_dict)
   
        # 딕셔너리 값이 2 미만일 경우는 삭제하기

        max_value = 2
        max_lst = []
        for example in comb_dict.keys():
            if comb_dict[example] > max_value:
                max_lst = [example]
                max_value = comb_dict[example]
            elif comb_dict[example] == max_value:
                max_lst.append(example)
        answer += max_lst
    print(answer)
    answer.sort()
    for k in range(len(answer)):
        answer[k] = "".join(answer[k])

    
    
    return answer


print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))