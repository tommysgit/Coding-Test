from collections import deque


n = int(input())
graph = [str(input()) for i in range(n)]


board = [[[0,0,0,0] for c in range(n)]for r in range(n)]
is_visit = [[[0,0,0,0] for c in range(n)] for r in range(n)]
def reverse_d(d):
    if d == 0:
        return 1
    if d == 1:
        return 0
    if d == 2:
        return 3
    if d == 3:
        return 2 
def bfs():
    # 북, 남, 서, 동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque()
    q.append((0, 0, 0))
    while q:
        r, c, cnt= q.popleft()
        if (r,c) == (n-1,n-1):
            if is_visit[r][c][0] == 1 and is_visit[r][c][2] == 1:
                break
        for i in range(4):
            mr, mc = r + dr[i], c + dc[i]
            d = reverse_d(i)
            if 0 <= mr < n and 0 <= mc < n and is_visit[mr][mc][d] == 0:
                is_visit[mr][mc][d] = 1
                if graph[mr][mc] == '0':
                    board[mr][mc][d] = cnt + 1
                    q.append((mr,mc,cnt+1))
                else:
                    q.appendleft((mr,mc,cnt))
                    board[mr][mc][d] = cnt
    return
bfs()

print(min(board[n-1][n-1][0], board[n-1][n-1][2]))