from copy import deepcopy


wheels = []
for i in range(4):
    wheels.append(list(str(input())))
# 회전 횟수
K = int(input())
k_list = []
def check_left(w_num):
    if wheels[w_num-1][2] != wheels[w_num][6]:
        return 1
    else:
        return 0
def check_right(w_num):
    if wheels[w_num+1][6] != wheels[w_num][2]:
        return 1
    else:
        return 0
# 특정 바퀴 회전
def rotation_wheel(w_num, d, is_visit):
    # 1번이면 오른쪽 바퀴만 4번이면 왼쪽 바퀴만 확인
    # 2, 3번이면 양쪽 바퀴 확인
    is_visit[w_num] = 1
    if w_num == 0:
        if not is_visit[1] and check_right(w_num):
            rotation_wheel(w_num+1, -d, is_visit)
        
    elif w_num == 3:
        if not is_visit[2] and check_left(w_num):
            rotation_wheel(w_num-1, -d, is_visit)
    else:
        if not is_visit[w_num-1] and check_left(w_num):
            rotation_wheel(w_num-1, -d, is_visit)
        if not is_visit[w_num+1] and check_right(w_num):
            rotation_wheel(w_num+1, -d, is_visit)
    # 반 시계방향 첫번째 값을 마지막 값으로
    if d < 0 :
        wheels[w_num].append(wheels[w_num][0])
        del wheels[w_num][0]
    # 시계방향 마지막 값을 첫번째 값으로
    else:
        tmp = deepcopy(wheels[w_num])
        wheels[w_num].clear()
        wheels[w_num].append(tmp[7])
        for i in range(7):
            wheels[w_num].append(tmp[i])
# 회전 방법 / 톱니바퀴 번호, 방향
for i in range(K):
    wheel_num, d = map(int, input().split())
    wheel_num -= 1
    is_visit = [0]*4
    rotation_wheel(wheel_num, d, is_visit)
# 점수 계산
def calculate_score():
    score = 0

    if wheels[0][0] == '1':
        score += 1
    if wheels[1][0] == '1':
        score += 2
    if wheels[2][0] == '1':
        score += 4
    if wheels[3][0] == '1':
        score += 8
    return score
#print(wheels)
print(calculate_score())