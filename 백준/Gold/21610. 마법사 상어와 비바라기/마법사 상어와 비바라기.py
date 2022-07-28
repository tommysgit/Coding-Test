from collections import deque
N, M = map(int, input().split())
graph = [[0]*N for i in range(N)]
move = []
nr = [0,0, -1, -1, -1, 0, 1, 1, 1]
nc = [0,-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(N):
    tmp_line = list(map(int, input().split()))
    for j in range(len(tmp_line)):
        graph[i][j] = tmp_line[j]
for i in range(M):
    d, s = map(int, input().split())
    move.append((d,s))
# (N,1) (N,2) (N-1,1) (N-1,2)비구름 생성
# 좌표값 보정
def correction(mr, mc):
    if mr == -1:
        mr = N-1
    if mr == N:
        mr = 0
    if mc == -1:
        mc = N-1
    if mc == N:
        mc = 0
    return mr, mc

# move만큼 이동 후 물의 양 증가
def move_cloud(d, s, cloud, is_visited):
    for i in range(len(cloud)):
            r, c = cloud.popleft()
            mr, mc = (r + nr[d]*s)%N , (c + nc[d]*s)%N
            mr, mc = correction(mr, mc)
            cloud.append((mr,mc))
    #print("cloud ", cloud)
    for cor in cloud:
        r, c = cor
        graph[r][c] += 1
        is_visited[r][c] = 1
    return cloud
# 물 복사 마법
def copy_water(cloud):
    for cor in cloud:
        r ,c = cor
        count = 0
        # 1 3 5 7 확인
        for i in [2, 4, 6, 8]:
            mr = r + nr[i]
            mc = c + nc[i]
            if mr < 0 or mc < 0 or mr >= N or mc >= N or graph[mr][mc] == 0:
                continue
            count += 1
        graph[r][c] += count
def recreate_cloud(cloud, is_visited):
    while cloud:
        cloud.popleft()
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and is_visited[i][j] == 0:
                cloud.append((i,j))
                graph[i][j] -= 2
    
cloud = deque([(N -1,0), (N-1,1), (N-2, 0), (N-2, 1)])
for i in range(len(move)):
    d, s = move[i]
    is_visited = [[0]*N for i in range(N)]
    cloud = move_cloud(d, s, cloud, is_visited)
    copy_water(cloud)
    #print(graph)
    recreate_cloud(cloud, is_visited)
    #print(graph)
# water_sum = [sum(i) for i in graph]
# print(sum(water_sum))
sum = 0
for i in range(N):
    for j in range(N):
        sum += graph[i][j]
print(sum)