# 14503
from collections import deque


N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
nr = [-1, 0, 1, 0]
nc = [0, -1, 0, 1]
answer = [0]
def up_d(d):
    if d == 3:
        return 0
    else:
        return d+1

# 북 서 남 동
# d 북 동 남 서
def dfs(r,c,d):
    queue = deque()
    queue.append((r,c,d))
    graph[r][c] = 2
    answer[0] += 1
    while queue:
        r, c, d = queue.popleft()
        # 탐색
        for i in range(4):
            # 탐색할 방향
            d = up_d(d)
            mr = r + nr[d]
            mc = c + nc[d]
            # 영역 밖이거나
            # 벽 혹은 이미 청소한 부분이면 통과
            # if mr < 0 or mc < 0 or mr >= N or mc >= M:
            #     continue
            if graph[mr][mc] != 0:
                continue
            # 청소 가능한 곳이면 그 방향으로 가서 청소
            # graph[mr][mc]가 0인곳만 여기까지 올 수 있다.
            queue.append((mr,mc,d))
            answer[0] += 1
            graph[mr][mc] = 2
            break
        # 네 방향 청소가 이미 되어있거나 벽인 경우
        if not queue:
            # 왼쪽 방향으로 두번 이동시켜 뒤에 좌표를 찾아낸다.
            md = up_d(d)
            md = up_d(md)
            mr = r + nr[md]
            mc = c + nc[md]
            # 뒤에가 벽이거나 범위 밖인 경우
            if graph[mr][mc] == 1:
                return
            else:
                queue.append((mr,mc,d))
        
for i in range(N):
    graph.append(list(map(int, input().split())))
if d == 1:
    d = 3
elif d ==3:
    d = 1
dfs(r,c,d)
print(answer[0])
