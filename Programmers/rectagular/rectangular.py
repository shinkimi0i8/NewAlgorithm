def solution(w,h):
    answer = w * h
    for j in range(h):
        for i in range(w):
            if i <= j * w / h < i + 1:
                answer -= 1
            elif j <= i * h / w < j + 1:
                answer -= 1

                
    return answer

# 반복되는 것까지는 찾았는데 최대공약수라는 규칙을 못 찾았다...