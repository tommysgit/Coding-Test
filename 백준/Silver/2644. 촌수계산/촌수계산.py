n = int(input())
A, B =map(int, input().split())
m = int(input())
link = [[]for i in range(n+1)]
is_visit = [0]*(n+1)
answer = [-1]
def dfs(target, n, count):
    if n == target:
        answer[0] = count
    is_visit[n] = 1
    for i in link[n]:

        if not is_visit[i]:
            dfs(target, i, count+1)
    
for i in range(m):
    a, b =map(int, input().split())
    link[a].append(b)
    link[b].append(a)
dfs(B, A, 0)
print(answer[0])