# 20057
import sys
N = int(input())
sys.setrecursionlimit(N*N*10)
start = (N//2, N//2)
is_visit = [[0]*N for i in range(N)]
nr = [0, 1, 0, -1]
nc = [-1, 0, 1, 0]
outside = 0
left = [(-1,-1,0.1), (-1, 0, 0.07), (-2, 0, 0.02), (-1,1, 0.01), (1, -1, 0.1), (1, 1, 0.01), (1,0, 0.07), (2,0, 0.02), (0,-2, 0.05),
(0,-1,0)]
right = [(x,-y,z) for x,y,z in left]
down = [(-y,x,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]
# 좌방향 위 아래 좌
# 아래방향 좌 우 아래
# 우방향 위 아래 우
# 위방향 좌 우 위
d_list = [left, down, right, up]
graph = []
# 모래 뿌리기
def send(r, c,d, graph):
    global outside
    total = 0
    for dx, dy, dz in d_list[d]:
        mr, mc = r + dx, c + dy
        
        if dz == 0:
            new_send = graph[r][c] - total
        else:
            new_send = int(graph[r][c]*dz)
            total += new_send
        # 영역 밖이면 outside 추가
        if mr < 0 or mc < 0 or mr >= N or mc >= N:
            outside += new_send
        else:
            graph[mr][mc] += new_send
        
# 다음 방향
def next_d(d):
    if d == 3:
        return 0
    else:
        return d+1

# 이동방향 좌 아래 우 위
def dfs(r,c, d, graph):
    #print(r,c, d)
    is_visit[r][c] = 1
    mr = r + nr[d]
    mc = c + nc[d]
    # 토네이도가 갈 수 없는 곳이면 종료
    if mr < 0 or mc < 0 or mr >= N or mc >= N or is_visit[mr][mc]:
        return
    #print(mr,mc,d)
    # 모래 뿌리기
    send(mr,mc,d, graph)
    # 다음 이동할 칸 정한 뒤 이동
    tmp_d = next_d(d)
    tmp_r = mr + nr[tmp_d]
    tmp_c = mc + nc[tmp_d]
    if not is_visit[tmp_r][tmp_c]:
        d = tmp_d
    dfs(mr,mc, d, graph)
for i in range(N):
    graph.append(list(map(int, input().split())))
dfs(start[0], start[1], 0, graph)
#print('start')
#for i in graph:
#    print(*i)
print(outside)
