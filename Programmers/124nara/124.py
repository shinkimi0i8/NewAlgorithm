def solution(d):
    answer = ''

    while d:
        if d % 3 == 0:
            answer += '4'
        if d % 3 == 1:
            answer += '1'
        if d % 3 == 2:
            answer += '2'
        if d <= 3:
            break
        d = d // 3
    
    answer = "".join(reversed(answer))
        
    return str(answer)

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))
print(solution(20))
print(solution(35))



# tmp = ''
# while d:
#     if d % 3 == 0:
#         tmp += '4'
#     if d % 3 == 1:
#         tmp += '1'
#     if d % 3 == 2:
#         tmp += '2'
    
#     d = d // 3

# tmp = "".join(reversed(tmp))
# print(int(tmp))