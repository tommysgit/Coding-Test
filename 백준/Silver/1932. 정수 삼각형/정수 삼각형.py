# 1932

n = int(input())
graph = []
dp = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    dp.append([0 for j in range(i+1)])

answer = graph[0][0]
def dfs(depth):
    global answer
    if depth == n:
        return
    dp[depth][0] = dp[depth-1][0] + graph[depth][0]
    dp[depth][depth] = dp[depth-1][depth-1] + graph[depth][depth]
    answer = max(answer, dp[depth][0], dp[depth][depth])
    for idx in range(1, depth):
        dp[depth][idx] = max(dp[depth-1][idx-1], dp[depth-1][idx])
        dp[depth][idx] += graph[depth][idx]
        answer = max(answer, dp[depth][idx])
    dfs(depth+1)

dp[0][0] = graph[0][0]
dfs(1)
print(answer)