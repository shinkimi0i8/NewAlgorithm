
from collections import deque


def shiftRow(array):
    array.appendleft(array.pop())
    return array

def rotate(array):


    array[0].appendleft('x')
    
    tmp = array[0].pop()
    array = [deque(x) for x in zip(*array)]
    tmp2 = array[-1].popleft()
    array[-1].appendleft(tmp)
    array[-1].appendleft(tmp2)
    tmp = array[-1].pop()
    array = [deque(x) for x in zip(*array)]
     
    tmp2 = array[-1].pop()
    array[-1].append(tmp)
    array[-1].append(tmp2)
    tmp = array[-1].popleft()
    array = [deque(x) for x in zip(*array)]

    tmp2 = array[0].pop()
    array[0].append(tmp)
    array[0].append(tmp2)
    array[0].popleft()
    array = [deque(x) for x in zip(*array)]
    
    return deque(array)


  


def solution(rc, operations):

    rc = deque(map(deque, rc))

    for operation in operations:
        if operation == "Rotate":
            rc = rotate(rc)
        elif operation == 'ShiftRow':
            rc = shiftRow(rc)
            
    answer = list(map(list, rc))
    return answer
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))

