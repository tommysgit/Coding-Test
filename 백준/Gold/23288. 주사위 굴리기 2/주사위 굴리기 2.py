from collections import deque


N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for r in range(N)]
dice = [0,1,2,3,4,5,6]
dr = [0, 0, 0, 1, -1]
dc = [0, 1, -1, 0, 0]
answer = 0
def bfs(r, c, score):
    q = deque([])
    q.append((r,c))
    cnt = 1
    is_visit = [[0 for c in range(M)] for r in range(N)]
    is_visit[r][c] = 1
    while q:
        r, c = q.popleft()
        for i in range(1, 5):
            mr, mc = r + dr[i], c + dc[i]
            if not 0 <= mr < N or not 0 <= mc < M :
                continue
            if is_visit[mr][mc] == 1:
                continue
            if graph[mr][mc] == score:
                is_visit[mr][mc] = 1
                cnt += 1
                q.append((mr, mc))
    return cnt * score
def clockwise(dir):
    if dir == 1:
        return 3
    elif dir == 2:
        return 4
    elif dir == 3:
        return 2
    else:
        return 1
def counter_clockwise(dir):
    if dir == 1:
        return 4
    elif dir == 2:
        return 3
    elif dir == 3:
        return 1
    else:
        return 2
def counter_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    else:
        return 3
def turn(cur, dir, dice):
    r, c = cur
    mr, mc = r + dr[dir], c + dc[dir]
    if not 0<=mr<N or not 0<=mc<M:
        return turn(cur, counter_dir(dir), dice)
    
    # 동
    if dir == 1:
        x, a, b, c, d, e, f = dice
        dice = [x, d, b, a, f, e, c]
    # 서
    elif dir == 2:
        x, a, b, c, d, e, f = dice
        dice = [x, c, b, f, a, e, d]
    # 남
    elif dir == 3:
        x, a, b, c, d, e, f = dice
        dice = [x, b, f, c, d, a, e]
    # 북
    else:
        x, a, b, c, d, e, f = dice
        dice = [x, e, a, c, d, f, b]
    return mr, mc, dice, dir
def round(dir, dice, clock):
    x, a, b, c, d, e, f = dice
    if clock == 1:
        dice = [x, a, d, b, e, c, f]
        return clockwise(dir), dice
    else:
        dice = [x, a, c, e, b, d, f]
        return counter_clockwise(dir), dice
dir, cur = 1, (0,0)
for i in range(K):
    r, c , dice, dir = turn(cur, dir, dice)
    cur = (r,c)
    score = graph[r][c]

    if dice[6] > score:
        dir = clockwise(dir)
    elif dice[6] < score:
        dir = counter_clockwise(dir)
    score = bfs(r, c, score)
    answer += score
print(answer)