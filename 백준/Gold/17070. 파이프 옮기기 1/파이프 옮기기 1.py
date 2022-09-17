from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for i in range(N)]
dp = [[[0,0,0] for c in range(N)] for r in range(N)]
direction_hash = {}
dir = [[(0, 1, 0, 1, 0), (0, 1, 1, 1, 2)], [(1, 0, 1, 0, 1), (1,0, 1, 1, 2)], [(1, 1, 0, 1, 0), (1, 1, 1, 0, 1), (1, 1, 1, 1, 2)]]
dp[0][1] = [1,0,0]
for r in range(len(graph)):
    for c in range(len(graph)):
        if r==c==0 or (r == 0 and c == 1):
            continue
        if graph[r][c] == 0:
            dp[r][c][0] += (dp[r][c-1][0] + dp[r][c-1][2])
            dp[r][c][1] += (dp[r-1][c][1] + dp[r-1][c][2])
            if 0<= r-1 < N and 0<= c-1 <N and graph[r][c-1] == 0 and graph[r-1][c] == 0:
                dp[r][c][2] += sum(dp[r-1][c-1])
print(sum(dp[N-1][N-1]))