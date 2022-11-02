from collections import deque
N = int(input())
graph = []
ans, max_num = 0, 0
max_area = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    tmp_max = max(tmp)
    max_num = max(max_num, tmp_max)
def bfs(rain, is_visit, r, c):
    is_visit[r][c] = 1
    q = deque()
    q.append((r,c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            mr, mc = r + dr[i], c + dc[i]
            if 0 <= mr < N and 0 <= mc < N and is_visit[mr][mc] == 0 and graph[mr][mc] > rain:
                is_visit[mr][mc] = 1
                q.append((mr,mc))
    return
# 최고 비의 높이만큼 반복
# r,c의 높이가 rain이하는 잠긴다.
for rain in range(max_num):
    is_visit = [[0]*N for i in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if is_visit[r][c] == 0 and graph[r][c] > rain:
                cnt += 1
                bfs(rain, is_visit, r, c)
    ans = max(ans, cnt)
print(ans)