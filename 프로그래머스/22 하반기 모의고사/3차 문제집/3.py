from collections import deque
def solution(distance, scope, times):
    answer = 0
    order = []
    for a, b in zip(scope, times):
        order.append([min(a[0], a[1]), max(a[0],a[1]),b[0],b[1]])
    order.sort(key = lambda x : x[0])
    queue = deque(order)
    #print(queue)
    # 현재범위가 근무상태인지 체크
    for i in range(1 , distance +1):
        #print("tt")
        # i번째 위치 진입
        answer += 1
        # 감시 범위 밖
        if not queue or answer < queue[0][0]:
            continue
        # 경계 범위이면 시간 체크
        elif queue[0][0] <= answer and answer <= queue[0][1]:
            cur_time = answer % (queue[0][2] + queue[0][3])
            # 근무시간
            if cur_time <= queue[0][2] and cur_time != 0:
                break
        if answer == queue[0][1]:
            queue.popleft()
    # 거리를 1씩 증가시키면서 현재 범위에 근무중인 경비병의 상태를 확인
    return answer