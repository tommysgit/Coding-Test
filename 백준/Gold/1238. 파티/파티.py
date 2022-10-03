import heapq

N, M, X = map(int, input().split())
edges = [[] for i in range(N+1)]
for i in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((end, cost))
# N개의 노드에서 X까지 가는 최단경로, X에서 돌아오는 최단경로를 구해야 한다.
def dijkstra(start, distance):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next in edges[now]:
            cost = dist + next[1]
            # 기존 거리보다 거쳐가는 것이 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance

ans = [0]*(N+1)
for start in range(1, N+1):
    distance = [1e9]*(N+1)
    s_dist = dijkstra(start, distance)
    if start == X:
        for j in range(1, N+1):
            ans[j] += s_dist[j]
    else:
        ans[start] += s_dist[X]
print(max(ans))