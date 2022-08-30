from collections import deque


N = int(input())
graph = []
dr = [-1, 0,1, 0]
dc = [0,-1,0, 1]
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    if 9 in tmp:
        r, c = i, graph[i].index(9)
# v : 상어 크기, f : 현재 먹은 물고기 , s : 지난 시간
def bfs(r,c ,v):
    is_visit =  [[0 for i in range(N)] for j in range(N)]
    distance =  [[0 for i in range(N)] for j in range(N)]
    tmp = []
    is_visit[r][c] = 1
    queue = deque([])
    queue.append((r,c))
    while queue:
        r, c,  = queue.popleft()
        for i in range(4):
            mr = r + dr[i]
            mc = c + dc[i]
            if mr < 0 or mc < 0 or mr >= N or mc >= N or is_visit[mr][mc]:
                continue
            if graph[mr][mc] > v :
                continue
            is_visit[mr][mc] = 1
            distance[mr][mc] = distance[r][c] + 1
            queue.append((mr,mc))
            # 먹이
            if graph[mr][mc] != 0 and graph[mr][mc] < v:
                tmp.append((mr,mc, distance[mr][mc]))
    # 가까운 거리 순 정렬
    return sorted(tmp, key= lambda x : [x[2], x[0], x[1]])
v, f, s = 2, 0, 0
graph[r][c] = 0
while 1:
    result = bfs(r,c, v)
    if len(result) == 0:
        break
    result = result[0]
    r, c = result[0], result[1]
    s += result[2]
    f += 1
    graph[r][c] = 0
    if v == f:
        v += 1
        f = 0
print(s)