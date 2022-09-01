import math
def solution(fees, records):
    my_hash = {}
    sum_hash = {}
    
    def to_min(strings):
        return int(strings[:2])*60 + int(strings[3:])
    # 입차만하고 출차를 안했을 수 있다. 출차를 안한 차량은 23:59에 출차한 것으로 간주
    for i in records:
        time, car_id, status = map(str, i.split())
        # 총 시간을 기록할 해시 테이블을 초기화
        if not sum_hash.get(car_id):
            sum_hash[car_id] = 0
        minutes = to_min(time)
        # 입차한 경우 시간 기록
        if status == "IN":
            my_hash[car_id] = minutes
        else:
            sum_hash[car_id] += (minutes - my_hash[car_id])
            my_hash[car_id] = -1
    # 차량 목록 해시를 돌며 출차를 안한 차량이 있으면 시간을 더해준다.
    for i in my_hash:
        if my_hash[i] != -1:
            sum_hash[i] += (to_min("23:59") - my_hash[i])
            my_hash[i] = 0
    # 요금 배열을 기준으로 계산
    for i in sum_hash:
        # 기본 시간을 넘기면 단위 시간을 적용한다.
        if sum_hash[i] >= fees[0]:
            sum_hash[i] = fees[1] + math.ceil((sum_hash[i] - fees[0])/fees[2]) * fees[3] 
        else:
            sum_hash[i] = fees[1]
    answer = sorted(sum_hash.keys())
    for i in range(len(answer)):
        answer[i] = sum_hash[answer[i]]
    return answer