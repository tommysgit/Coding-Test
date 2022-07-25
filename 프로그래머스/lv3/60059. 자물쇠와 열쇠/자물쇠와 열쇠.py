def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    # 3 <= M <= N
    # 전략 자물쇠의 3배 크기의 그래프를 생성
    # 정중앙에 자물쇠를 놓고
    # 
    # key를 시계방향으로 90도 회전
    def right_rotation(key):
        return list(map(list, zip(*key[::-1])))
    # 자물쇠가 맞는지 확인
    def check(lock):
        for i in range(N):
            for j in range(N):
                if lock[N+i][N+j] != 1:
                    return False
        return True
    # 새로운 크기의 자물쇠 배치
    new_lock = [[0]*N*3 for _ in range(N*3)]
    # N~2N까지가 정중앙
    for i in range(N):
        for j in range(N):
            new_lock[N+i][N+j] = lock[i][j]
    # key를 4번 회전
    for i in range(4):
        key = right_rotation(key)
        # 왼쪽위에서 2N까지 자물쇠 위치 세팅
        for i_lock in range(N*2):
            for j_lock in range(N*2):
                # 키를 꼽는다.
                for i_key in range(M):
                    for j_key in range(M):
                        new_lock[i_lock+i_key][j_lock+j_key] += key[i_key][j_key]
                # 가운데 락이 맞는지 확인
                if check(new_lock):
                    return True
                # 맞지않으면 다시 키를 뺀다.
                for i_key in range(M):
                    for j_key in range(M):
                        new_lock[i_lock+i_key][j_lock+j_key] -= key[i_key][j_key]
    return answer