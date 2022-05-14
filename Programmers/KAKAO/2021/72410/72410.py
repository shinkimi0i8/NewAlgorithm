# 새로운 아이디 입력 -> 규칙에 안 맞음 -> 유사 & 규칙에 맞는 아이디 추천

# 길이 3 <= 아이디 <= 15
# 소문자, 숫자, 하이픈, 밑줄, 마침표
# 마침표는 처음과 끝 X 연속 X

def solution(new_id):

    # 1단계 모든 대문자를 대응되는 소문자로 치환
    fixed_id = new_id.lower()
    ans_id = ''
    
    # 2단계 조건 외 문자는 모두 제거
    for i in range(len(fixed_id)):
        if fixed_id[i].isdecimal() or fixed_id[i].isalpha() or fixed_id[i] in ('-', '_', '.'):
            
            # 3단계 마침표 연속 제거
            if len(ans_id) > 0 and ans_id[-1] == '.' and fixed_id[i] == '.':
                pass
            else:
                ans_id += fixed_id[i]

    # 4단계 마침표가 처음이나 끝에 위치한다면 제거
    while len(ans_id) > 0 and ans_id[0] == '.':
        ans_id = ans_id[1:]

    while len(ans_id) > 0 and ans_id[-1] == '.':
        ans_id = ans_id[:-1]
    
    # 5단계 빈 문자열 a
    if ans_id == '':
        ans_id = 'a'

    # 6단계 문자열 깅이 15로
    if len(ans_id) >= 16:
        ans_id = ans_id[:15]
    while len(ans_id) > 0 and ans_id[-1] == '.':
        ans_id = ans_id[:-1]

    # 7단계 2 이하 문자열 3으로
    while len(ans_id) < 3:
        ans_id += ans_id[-1]
    
    return ans_id

# print(solution("123_.def"))