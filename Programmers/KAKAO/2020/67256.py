def solution(numbers, hand):
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    index_lst = [('X', 'X')]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            index_lst.append((i, j))
    answer = ''
    left = 10
    right = 12
    for number in numbers:
        if number == '*':
            number = 10
        if number == 0:
            number = 11
        if number == '#':
            number = 12
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right = number
        else:

            left_distance = abs(index_lst[number][0] - index_lst[left][0]) + abs(index_lst[number][1] - index_lst[left][1])
            right_distance = abs(index_lst[number][0] - index_lst[right][0]) + abs(index_lst[number][1] - index_lst[right][1])
            if left_distance > right_distance:
                answer += 'R'
                right = number
            elif left_distance < right_distance:
                answer += 'L'
                left = number
            else:
                if hand == 'right':
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number
    
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))