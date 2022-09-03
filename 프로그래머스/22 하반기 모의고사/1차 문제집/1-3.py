from collections import deque
def solution(order):
    answer = 0
    conveyor = list(range(1, len(order)+1))
    conveyor = deque(conveyor)
    conveyor_assist = deque()
    order = deque(order)
    while order:
        order_num = order[0]
        del order[0]
        # 해당 순서가 컨베이어 벨트에 있는지 확인
        if order_num >= conveyor[0]:
            while order_num > conveyor[0]:
                conveyor_assist.append(conveyor.popleft())
            if conveyor[0] == order_num:
                if len(conveyor) > 1:
                    conveyor.popleft()
                answer += 1
        else:
            if conveyor_assist and conveyor_assist[-1] == order_num:
                answer += 1
                conveyor_assist.pop()
            else:
                break
    return answer