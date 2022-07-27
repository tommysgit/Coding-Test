# 17144
R, C, T = map(int, input().split())
graph = []
start = []
nr = [-1 , 1, 0, 0]
nc = [0, 0, -1, 1]
#is_dust = [[0]*C for i in range(R)]
for i in range(R):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    if -1 in tmp:
        start.append((i, 0))
def bfs(graph):
    tmp_graph = [[0]*C for i in range(R)]
    for r in range(R):
        for c in range(C):
            count = 0
            amount = graph[r][c]//5
            if graph[r][c] >= 5:
                for i in range(4):
                    mr = r + nr[i]
                    mc = c + nc[i]
                    if mr < 0 or mc < 0 or mr >= R or mc >= C or graph[mr][mc] == -1:
                        continue
                    count += 1

                    tmp_graph[mr][mc] += amount
            tmp_graph[r][c] += (graph[r][c] - count*amount)
   # print(tmp_graph)
    return tmp_graph
def start_clear(r,c,d):
    # r, 1 부터 r-1, 0까지 d에 따른 회전
    # 반시계 방향은 범위밖까지 우 위 좌 아 순서대로
    # 시계 방향은 범위밖까지 우 아 좌 위
    fix_r = r
    fix_c = c
    if d == 1:
        while r >= 1 :
            graph[r][c] = graph[r-1][c]
            r -= 1
        while c < C-1:
            graph[r][c] = graph[r][c+1]
            c += 1
        while r < fix_r: # 0 2
            graph[r][c] = graph[r+1][c]
            r += 1
        while c > 0:
            graph[r][c] = graph[r][c-1]
            c -= 1
    else:
        while r < R-1:
            graph[r][c] = graph[r+1][c]
            r += 1
        while c < C-1:
            graph[r][c] = graph[r][c+1]
            c += 1
        while r > fix_r:
            graph[r][c] = graph[r-1][c]
            r -= 1
        while c > 0:
            graph[r][c] = graph[r][c-1]
            c -= 1
    graph[fix_r][fix_c] = -1 
    graph[fix_r][fix_c+1] = 0
    return
# 확산
for time in range(T):
    graph = bfs(graph)
    start_clear(start[0][0], start[0][1], 1)
    start_clear(start[1][0], start[1][1], -1)
def cal():
    sum_dust = 0
    for i in graph:
        sum_dust += sum(i)
    return sum_dust + 2
#print(graph)
print(cal())