from itertools import combinations

def solution(relation):
    answer = 0
    
    # 조합 리스트
    c_lst = []
    
    # 유일성 만족 리스트
    unique = []
    
    # 가능한 모든 후보키 조합의 개수를 만들기
    for i in range(1,len(relation[0])+1):
        c = combinations(list(range(0,len(relation[0]))),i)
        c_lst.extend(c)
        
    # 유일성 확인
    for c_ in c_lst: 
        temp = [] # 각 조합에 따른 데이터를 모은 list
        for a in relation: 
            temp2 = [] # 각 조합의 데이터 값
            for b in c_: 
                temp2.append(a[b])

            temp.append(tuple(temp2))
		
        # 중복 제거를 했을 때 개수가 원래의 데이터 개수와 같다면 유일성 만족
        if len(set(temp)) == len(relation):
            unique.append(c_)
    
    unique_set = set(unique)
    
    # 최소성 만족
    # ex) a = (0,1) / b = (0,1,2)라고 가정한다면 b는 2라는 컬럼을 굳이 안넣어도 유일성을 만족하기 때문에 최소성 만족x  
    for i in range(len(unique)-1):
        for j in range(i+1, len(unique)):
            a = unique[i]
            b = unique[j]
            if set(a) & set(b) == set(a):
                unique_set.discard(b)
                
    return len(unique_set)


# from itertools import combinations



# # [(('100',), ('200',), ('300',), ('400',), ('500',), ('600',)), (('100', 'ryan'), ('200', 'apeach'), ('300', 'tube'), ('400', 'con'), ('500', 'muzi'), ('600', 'apeach')), (('100', 'music'), ('200', 'math'), ('300', 'computer'), ('400', 'computer'), ('500', 'music'), ('600', 'music')), (('100', '2'), ('200', '2'), ('300', '3'), ('400', '4'), ('500', '3'), ('600', '2')), (('ryan', 'music'), ('apeach', 'math'), ('tube', 'computer'), ('con', 'computer'), ('muzi', 'music'), ('apeach', 'music')), (('100', 'ryan', 'music'), ('200', 'apeach', 'math'), ('300', 'tube', 'computer'), ('400', 'con', 'computer'), ('500', 'muzi', 'music'), ('600', 'apeach', 'music')), (('100', 'ryan', '2'), ('200', 'apeach', '2'), ('300', 'tube', '3'), ('400', 'con', '4'), ('500', 'muzi', '3'), ('600', 'apeach', '2'))]    
# # (('100', 'ryan', 'music', '2'), ('200', 'apeach', 'math', '2'), ('300', 'tube', 'computer', '3'), ('400', 'con', 'computer', '4'), ('500', 'muzi', 'music', '3'), ('600', 'apeach', 'music', '2'))

# def check_overlapped(lst1, lst2):
    
#     lst2 = list(map(list, lst2))
#     print('======', lst2)
#     lst1 = list(map(list, lst1))
#     print('XXX', lst1)

#     for i in range(len(lst1)):
#         for j in range(len(lst2)):
#             if len(lst2[j] + list(lst1[i][0])) != set(len(lst2[j] + list(lst1[i][0]))):
#                 return 0 
    

        


#     return 1

# # https://studyandwrite.tistory.com/400

# def solution(relation):
    
#     length = len(relation)
#     infos = len(relation[0])
    
#     keys = []
#     for i in range(1, infos+1):
#         check = []
#         for j in range(length):
#             check.append(list(combinations(relation[j], i)))
#         tmp = list(zip(*check))
        
#         for k in range(len(tmp)):
#             if len(tmp[k]) == len(set(tmp[k])):
#                 # print('tmp[k]',tmp[k])
#                 # print(keys)
#                 if len(keys) != 0:
#                     if check_overlapped(keys, tmp[k]):
#                         keys.append(tmp[k])
#                 else:
#                     keys.append(tmp[k])
    
#     return len(keys)

# print(
#     solution(
#         [
#             ["100", "ryan", "music", "2"],
#             ["200", "apeach", "math", "2"],
#             ["300", "tube", "computer", "3"],
#             ["400", "con", "computer", "4"],
#             ["500", "muzi", "music", "3"],
#             ["600", "apeach", "music", "2"],
#         ]
#     )
# )


# # from itertools import combinations
# # from collections import deque


# # def solution(relation):
# #     answer = 0
# #     row = len(relation)
# #     col = len(relation[0])

# #     candidates = []

# #     for i in range(1, col +1):
# #         candidates.extend(combinations(range(col), i))

# #     print(candidates)
    
# #     unique = deque()
# #     for candidate in candidates:
# #         tmp = [tuple([item[i] for i in candidate]) for item in relation]
# #         if row == len(set(tmp)):
# #             unique.append(candidate)
    
# #     answer = 0

# #     while len(unique) > 0:
# #         tmp = unique.popleft()
# #         if tmp != 'X':
# #             answer += 1
# #             for j in range(len(unique)):
                
# #                 if zip(tmp) in list(zip(*unique[j])):
# #                     print('8888')
# #                     unique[j] = 'X'
        





#     # return answer

# #http://localhost:8888/notebooks/answer/02_01_%ED%95%A8%EC%88%98.ipynb







# # from itertools import combinations


# # def solution(relation):
# #     answer = 0
# #     length = len(relation)

# #     number, name, major, grade = zip(*relation)
# #     print(name)

# #     number_set, name_set, major_set, grade_set = map(set, zip(*relation))
# #     key_candidates_set = [number_set, name_set, major_set, grade_set]
# #     tmp = [number, name, major, grade]
# #     key_candidates = []
# #     idx = 0
# #     for key_candidate in key_candidates_set:
# #         # 단일 후보키
# #         if len(key_candidate) == length:
# #             answer += 1
# #         else:
# #             key_candidates.append(tmp[idx])
# #         idx += 1
# #     combination_lst = []
# #     print('여기는 키', key_candidates)
    
    
# #     tmp_lst = []
# #     if len(key_candidates) == len(set(zip(*key_candidates))):
# #         answer += 1

# #     elif len(key_candidates) >= 3:
# #         for i in range(2, len(key_candidates)):
# #             print(len(key_candidates))
# #             combination_lst += list(combinations(key_candidates, i))
# #         print(combination_lst)
# #     print(name_set)

# #     return answer


# # print(
# #     solution(
# #         [
# #             ["100", "ryan", "music", "2"],
# #             ["200", "apeach", "math", "2"],
# #             ["300", "tube", "computer", "3"],
# #             ["400", "con", "computer", "4"],
# #             ["500", "muzi", "music", "3"],
# #             ["600", "apeach", "music", "2"],
# #         ]
# #     )
# # )
