

def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(board[i])
    cnt = 1
    while cnt != 0:
        cnt = 0
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j][0] == 'o':
                    continue

                if board[i][j][0] == board[i][j+1][0] and board[i][j][0] == board[i+1][j][0] and board[i][j][0] == board[i+1][j+1][0]:
                    cnt += 1
                    if 'x' not in board[i][j]:
                        board[i][j] = (board[i][j][0], 'x')
                    if 'x' not in board[i][j+1]:
                        board[i][j+1] = (board[i][j+1][0], 'x')
                    if 'x' not in board[i+1][j]:
                        board[i+1][j] = (board[i+1][j][0], 'x')
                    if 'x' not in board[i+1][j+1]:
                        board[i+1][j+1] = (board[i+1][j+1][0], 'x')
        for i in range(m):
            for j in range(n):
                if 'x' in board[i][j]:
                    board[i][j] = 'x'
        board = list(map(list, zip(*board)))
        for j in range(n):
            while 'x' in board[j]:
                board[j].remove('x')
                board[j].insert(0, 'o')
                answer += 1
    
        board = list(map(list, zip(*board)))



    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))

# CCBDE
# AAADE
# AAABF
# CCBBF


# oooDE
# oooDE
# CCBBF
# CCBBF



# ooBDE
# ooBDE
# oooBF
# oooBF