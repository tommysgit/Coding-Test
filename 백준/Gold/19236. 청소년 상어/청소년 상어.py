from copy import deepcopy


graph = [[0 for i in range(4)] for j in range(4)]
direction = [[0 for i in range(4)] for j in range(4)]
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, -1, -1, -1, 0, 1, 1, 1]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(8):
        s, r = divmod(j, 2)
        if r :
            direction[i][s] = tmp[j]
        else:
            graph[i][s] = tmp[j]
answer = [0]
def dfs(sr, sc, sd, graph, direction, count, n):
    count += graph[sr][sc]
    answer[0] = max(answer[0], count)
    graph[sr][sc] = 0
    direction[sr][sc] = 0
    # 물고기 번호순 이동
    for num in range(1, 17):
        fr, fc = -1, -1
        for r in range(4):
            for c in range(4):
                # 물고기 발견
                if graph[r][c] == num:
                    fr, fc = r, c
                    break
        if fr == -1 and fc == -1:
            continue
        fd = direction[fr][fc]
        # 방향대로 움직인다.
        for i in range(fd, fd+8):
            if i > 8:
                i = (i) % 8
            mr, mc = fr + dr[i], fc + dc[i]
            # 범위 밖이거나 상어인 경우 반시계 45도 회전하여 물고기이동
            if mr < 0 or mc < 0 or mr >= 4 or mc >= 4 or (mr == sr and mc == sc):
                continue 
            # 이동가능한 방향 i
            direction[fr][fc] = i
            graph[fr][fc], graph[mr][mc] = graph[mr][mc], graph[fr][fc]
            direction[fr][fc], direction[mr][mc] = direction[mr][mc], direction[fr][fc]
            break
    # 상어 이동

    for j in range(1,5):
        d_sr, d_sc = sr + dr[sd]*j, sc + dc[sd]*j

        if d_sr < 0 or d_sc < 0 or d_sr > 3 or d_sc > 3 or graph[d_sr][d_sc] == 0:
            continue
        dfs(d_sr, d_sc, direction[d_sr][d_sc],  deepcopy(graph), deepcopy(direction), count, n+1)
dfs(0, 0, direction[0][0], deepcopy(graph), deepcopy(direction), 0, 0)
print(answer[0])