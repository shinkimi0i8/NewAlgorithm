import math


def solution(fees, records):
    answer = []
    records_arr = []
    ans_dict = {}

    for record in records:
        records_arr.append((record.split()[1], int(record.split()[0][:2]) * 60 + int(record.split()[0][3:]), record.split()[2]))
        # [('5961', 334, 'IN'), ('0000', 360, 'IN'), ('0000', 394, 'OUT'), ('5961', 479, 'OUT'), ('0148', 479, 'IN'), ('0000', 1139, 'IN'), ('0148', 1149, 'OUT'), ('5961', 1379, 'IN'), ('5961', 1380, 'OUT')]
    
    for record_arr in records_arr:
        if not record_arr[0] in ans_dict:
            ans_dict[record_arr[0]] = [-1 * record_arr[1], 1]
        else:
            if ans_dict.get(record_arr[0])[1] % 2:
                ans_dict[record_arr[0]] = [ans_dict.get(record_arr[0])[0] + record_arr[1], ans_dict.get(record_arr[0])[1] + 1]
            else:
                ans_dict[record_arr[0]] = [ans_dict.get(record_arr[0])[0] - record_arr[1], ans_dict.get(record_arr[0])[1] + 1]
    for key in ans_dict:
        if ans_dict.get(key)[1] % 2: # 만일 출차가 안 된 경우(홀수번 입력된 경우)
            ans_dict[key] = [ans_dict.get(key)[0] + 1439, ans_dict.get(key)[1] + 1]
        if math.ceil(((ans_dict[key][0] - fees[0]) / fees[2])) >= 0: # 기본 요금 이상일 때만
            ans_dict[key][0] = fees[1] + math.ceil(((ans_dict[key][0] - fees[0]) / fees[2])) * fees[3]
        else:
            ans_dict[key][0] = fees[1]
    # {'5961': [146, 4], '0000': [334, 4], '0148': [670, 2]}

    # 딕셔너리 정렬
    sorted_lst = sorted(ans_dict.items())
    
    # 키 오름차순으로 리스트 추가
    for i in range(len(sorted_lst)):
        answer.append(sorted_lst[i][1][0])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))