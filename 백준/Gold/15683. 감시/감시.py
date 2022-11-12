from copy import deepcopy
d = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2,3]],
    [[0,2], [0,3], [1,3], [1,2]],
    [[0,1,2], [0, 2,3], [0, 1, 3], [1,2,3]],
    [[0,1,2,3]]
]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
target = [1,2,3,4,5]
target_cor = []
N, M = map(int, input().split())
graph = []
answer = [1e9]
for i in range(N):
    tmp =list(map(int, input().split()))
    graph.append(tmp)
    for j in range(M):
        if tmp[j] in target:
            target_cor.append((i,j))
def check(graph):
    cnt = 0
    for r in range(N):
        cnt += graph[r].count(0)
    return cnt
def fill(r, c, dir, graph):
    mr = r + dr[dir]
    mc = c + dc[dir]
    while 0 <= mr < N and 0 <= mc < M:
        if graph[mr][mc] == 6:
            break
        if graph[mr][mc] == 0:
            graph[mr][mc] = '#'
        mr += dr[dir]
        mc += dc[dir]

def dfs(n, graph):
    answer[0] = min(answer[0], check(graph))
    if n == len(target_cor):
        return
    tmp_graph = deepcopy(graph)
    r, c = target_cor[n]
    for next in d[graph[r][c]]:
        for i in next:
            fill(r,c, i, tmp_graph)
        dfs(n+1, tmp_graph)
        tmp_graph = deepcopy(graph)
dfs(0, graph)
print(answer[0])