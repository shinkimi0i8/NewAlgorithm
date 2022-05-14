def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        for line in board:
            if line[move - 1] != 0:
                if basket and basket[-1] == line[move - 1]:
                    basket = basket[:-1]
                    line[move - 1] = 0
                    answer += 2
                    print(basket)
                else:
                    print(line[move - 1])
                    basket.append(line[move - 1])
                    line[move - 1] = 0
                    print('두번째', basket)
                break

    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))


# [0, 0, 0, 0, 0],
# [0, 0, X, 0, X], 
# [0, 2, 5, 0, X], 
# [X, 2, 4, 4, 2], 
# [X, 5, 1, 3, 1]]