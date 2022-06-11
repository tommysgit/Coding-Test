from collections import deque
N, K = map(int, input().split())
queue = deque(list(range(1, N+1)))
i = 0
result = []
while queue:
    i+=1
    tmp = queue.popleft()
    if i == K:
        i=0
        result.append(str(tmp))
    else:
        queue.append(tmp)
print("<" + ", ".join(result)+ ">")