def convert_from_decimal_to_larger_bases(number, base):

    strings = "0123456789ABCDEFGHIJ"
    result = ""
    if number == 0:
        return 0
    else:
        while number > 0:
            digit = number % base
            result = strings[digit] + result
            number = number // base
    
        return result


def solution(n, t, m, p):

    total = ''
    for i in range(t * m):
        total += str(convert_from_decimal_to_larger_bases(i, n))
    answer = ''

    for j in range(t):
        answer += total[j * m + p - 1]

    return answer


print(solution(2, 4, 2, 1))
