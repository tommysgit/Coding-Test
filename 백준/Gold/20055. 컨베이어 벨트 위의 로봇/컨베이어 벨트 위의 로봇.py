N, K = map(int, input().split())
up_robot = [0]*N
down_robot = [0]*N
is_robot = [0]*(N)
count, step = 0, 0
#durability = [0]*(2*N)
# 벨트와 로봇을 한칸씩 뒤로 민다.
def one(belt):

    tmp_belt = []
    tmp_robot = [0]*N
    tmp_belt.append(belt[-1])
    # N번째 로봇은 내려준다.
    is_robot[N-1] = 0
    # 벨트 돌리기
    for i in range(2*N-1):
        tmp_belt.append(belt[i])
    # 로봇 돌리기
    for i in range(1, N):
        tmp_robot[i] = is_robot[i-1]
    
    return tmp_belt, tmp_robot
# 로봇의 위치에 다음 인덱스의 내구도와 로봇이 있는지를 확인하고 이동시킨다.        
def two(belt):
    for i in reversed(range(N)):
        # i 번째에 로봇이 있고
        if is_robot[i] == 1:
            # i+1이 N번째이면 로봇 제거
            if i+1 == N:
                is_robot[N-1] = 0
                continue
            # i+1 번째에 로봇이 없고 내구도가 1이상이면 옮긴다.
            if is_robot[i+1] == 0 and belt[i+1]>0:
                is_robot[i+1] = 1
                is_robot[i] = 0
                belt[i+1] -= 1
        
    
def three(belt):
    if belt[0] != 0:
        belt[0] -= 1
        is_robot[0] = 1
    
# 내구도
durability = list(map(int, input().split()))
# 벨트 단계별 실행
while durability.count(0) < K:
    step += 1
    durability, is_robot = one(durability)
    two(durability)
    three(durability)
    
print(step)