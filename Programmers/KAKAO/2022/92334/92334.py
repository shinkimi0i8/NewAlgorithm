'''
불량 이용자 신고 처리 결과를 메일로 발송
각 유저는 한번에 한명의 유저를 신고할 수 있다.
신고 횟수 제한 X
한 유저를 여러번 신고하더라도 한번으로 처리
K번 이상 신고된 유저는 게시판 이용 정지
해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 이용 정지를 시키면서 메일 발송

입력값 ["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3
'''


def solution(id_list, report, k):
    
    # 중복해서 신고한 애들 제거
    report = list(set(report))
    
    shingo = {} # ID가 누구누구를 신고했는지
    pishingo = {} # ID가 몇번 신고당했는지
    result = {} # ID가 신고한 애들이 얼마나 정지당했는지(= 메일 수신)
    records = [] # report를 이차원 배열로 변경
    for repo in report:
        records.append(repo.split())
        # records == [['신철', '은우'], ['수정', '은우'], ['종민', '신철'], ['종민', '은우'], ['신철', '수정'], ['종민', '수정'], ['은우', '수정']]

    # 딕셔너리마다 키와 값으로 받을 데이터 형식 정의
    for id in id_list:
        shingo[id] = []
        pishingo[id] = 0
        result[id] = 0

    # 신고자와 피신고자 딕셔너리에 이름, 횟수 추가
    for record in records:
        shingo[record[0]].append(record[1])
        # {'신철': ['은우', '수정'], '종민': ['수정', '은우', '신철'], '은우': ['수정'], '수정': ['은우']}
        pishingo[record[1]] += 1
        # shingo == {'신철': ['은우', '수정'], '종민': ['수정', '은우', '신철'], '은우': ['수정'], '수정': ['은우']}

        # pishingo == {'신철': 1, '종민': 0, '은우': 3, '수정': 3}
    

    bans = [] # k번 이상 신고 당해 정지당한 애들 목록
    for key in pishingo:
        if pishingo[key] >= k:
            bans.append(key)
    # bans == ['은우', '수정']
    
    for key in shingo:
        for ban in bans:
            if ban in shingo[key]:
                result[key] += 1
    # result == {'신철': 2, '종민': 2, '은우': 1, '수정': 1}

    final = []

    for key in result:
        final.append(result[key])
    return final


# names = ['신철', '종민', '은우', '수정']
# shingo = ["신철 수정", "신철 은우", "종민 수정", "종민 신철", "종민 은우", "은우 수정", "수정 은우"]
# print(solution(names, shingo, 3))