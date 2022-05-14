def distancing(place):
    fail = 0
    for i in range(2, 7):
        for j in range(2, 7):
            if place[i][j] == 'P':
                # 맨하튼 거리 1로 맞닿아 있는 경우
                if place[i-1][j] == 'P' or place[i][j-1] == 'P' or place[i][j+1] == 'P' or place[i+1][j] == 'P':
                    fail = 1
                    break

            
                # 맨하튼 거리 2로 대각선으로 맞닿아 있는 경우
                elif place[i-1][j-1] == 'P':
                    if place[i-1][j] != 'X' or place[i][j-1] != 'X':
                        fail = 1
                        break
                elif place[i+1][j+1] == 'P':
                    if place[i+1][j] != 'X' or place[i][j+1] != 'X':
                        fail = 1
                        break
                elif place[i-1][j+1] == 'P':
                    if place[i-1][j] != 'X' or place[i][j+1] != 'X':
                        fail = 1
                        break
                elif place[i+1][j-1] == 'P':
                    if place[i+1][j] != 'X' or place[i][j-1] != 'X':
                        fail = 1
                        break
                
                # 맨하튼 거리 2로 직선으로 맞닿아 있는 경우
                elif place[i-2][j] == 'P':
                    if not place[i-1][j] == 'X':
                        fail = 1
                        break
                elif place[i][j-2] == 'P':
                    if not place[i][j-1] == 'X':
                        fail = 1
                        break    
                elif place[i][j+2] == 'P':
                    if not place[i][j+1] == 'X':
                        fail = 1
                        break  
                elif place[i+1][j] == 'P':
                    if not place[i+1][j] == 'X':
                        fail = 1
                        break  
        if fail == 1:
            break
    if fail == 1:
        return 0
    
    else:
        return 1

def solution(places):
    for i in range(len(places)):
        places[i] = ['OOOOO'] + ['OOOOO'] + places[i]
        for j in range(len(places[i])):
            places[i][j] = 'OO' + places[i][j] + 'OO'
        places[i] = places[i] + ['OOOOOOOOO'] + ['OOOOOOOOO']
    # print(places)
    answer = []
    for place in places:
        answer.append(distancing(place))
    


    return answer




print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# P : 응시자
# O : 빈테이블
# X : 파티션

# "POOOP"
# "OXXOX"
# "OPXPX"
# "OOXOX"
# "POXXP"

# "POOPX"
# "OXPXP"
# "PXXXO"
# "OXXXO"
# "OOOPP"



# def distancing(place):
#     fail = 0
#     for i in range(5):
#         for j in range(5):
#             if place[i][j] == 'P':
#                 if place[i-1][j] == 'P' or place[i][j-1] == 'P' or place[i][j+1] == 'P' or place[i+1][j] == 'P':
#                     fail = 1
#                     break
#                 elif place[i-1][j-1] == 'P':
#                     if not place[i-1][j] == 'X' and place[i][j-1] == 'X':
#                         fail = 1
#                         break
#                 elif place[i+1][j+1] == 'P':
#                     if not place[i+1][j] == 'X' and place[i][j+1] == 'X':
#                         fail = 1
#                         break
#                 elif place[i-1][j+1] == 'P':
#                     if not place[i-1][j] == 'X' and place[i][j+1] == 'X':
#                         fail = 1
#                         break
#                 elif place[i+1][j-1] == 'P':
#                     if not place[i+1][j] == 'X' and place[i][j-1] == 'X':
#                         fail = 1
#                         break
#         if fail == 1:
#             break
#     if fail == 1:
#         return 0
    
#     else:
#         return 1

# def solution(places):
#     for i in range(len(places)):
#         places[i] = ['OOOOO'] + places[i]
#         for j in range(len(places[i])):
#             places[i][j] = 'O' + places[i][j] + 'O'
#         places[i] = places[i] + ['OOOOOOO']
#     answer = []
#     for place in places:
#         answer.append(distancing(place))
    


#     return answer