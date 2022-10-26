from collections import deque
import sys

M, N, H = map(int, input().split())
def bfs():
    dh = [-1, 1, 0, 0, 0, 0]
    dr = [0, 0, -1, 1, 0, 0]
    dc = [0, 0, 0, 0, -1, 1]
    while q:
        h, r, c = q.popleft()
        for i in range(6):
            mh = h + dh[i]
            mr = r + dr[i]
            mc = c + dc[i]
            if 0 <= mh < H and 0 <= mr < N and 0 <= mc < M:
                if graph[mh][mr][mc] == 0:
                    graph[mh][mr][mc] = graph[h][r][c] + 1
                    q.append((mh, mr, mc))

# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없음
graph = []
#is_visit = [[ [ 0 for c in range(M)] for r in range(N)] for h in range(H)]
is_done = 0
q = deque()
for h in range(H):
    height = []
    for r in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        for c in range(M):
            if tmp[c] == 1:
                q.append((h,r,c))
            elif tmp[c] == 0:
                is_done = 1
        height.append(tmp)
    graph.append(height)

bfs()
ans = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            ans = max(ans, graph[h][r][c])
            if graph[h][r][c] == 0:
                is_done = -1

if is_done == -1 or is_done == 0:
    print(is_done)
else:
    print(ans-1)       