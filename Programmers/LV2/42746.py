def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))