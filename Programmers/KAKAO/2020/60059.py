def keying(key, lock, N):
    max_len = N + len(key) - 1
    for k in range(max_len):
        for l in range(max_len):
            fail = 0
            for p in range(len(key)):
                for q in range(len(key)):
                    lock[k+p][l+q] += key[p][q]

                    if lock[k+p][l+q] == 2:
                        fail = 1

            
            for y in range(len(key) -1, len(key) + N-1):
                if 0 in lock[y][len(key) -1: len(key) + N-1]:
                    fail = 1
                    break
            

            if fail == 0:
                return True
            for p in range(len(key)):
                for q in range(len(key)):

                    lock[k+p][l+q] -= key[p][q]


    return False
            
            
def rotate(array):
    return list(zip(*array[::-1]))




def solution(key, lock):
    N = len(lock)
    for i in range(N):
        lock[i] = [0] * (len(key) - 1) + lock[i] + [0] * (len(key) - 1)
    lock = [[0] * (2 * len(key) + N - 2) for _ in range(len(key) -1)] + lock + [[0] * (2 * len(key) + N - 2) for _ in range(len(key) -1)]
    
    if keying(key, lock, N) == True:
        return True
    else:
        for j in range(3):
            key = rotate(key)
            if keying(key, lock, N) == True:
                return True
    return False
        

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# 000
# 100
# 011

# 111
# 110
# 101