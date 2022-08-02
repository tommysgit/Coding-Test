# 1967
import heapq


n = int(input())
edge = []
INF = (1e9)
max_cost = 0
graph = [[] for i in range(n+1)]
def dijkstra(start, cost):
    global max_cost
    q = []
    heapq.heappush(q, (start, 0))
    cost[start] = 0
    max_idx = 0
    while q:
        # 현재 노드의 번호와 start와의 거리값
        now, dist = heapq.heappop(q)
        # 이미 다른노드를 거친 값이 더 작은경우 건너뛴다.
        if cost[now] < dist:
            continue
        # now에 있는 그래프 순환
        for node in graph[now]:
            # 기존 now까지 거리 + now와 연결된 노드의 거리를 합하여 최단거리 최신화
            new_dist = dist + node[1]
            if new_dist < cost[node[0]]: # 새로운 거리가 기존 거리보다 짧으면 갱신
                if max_cost < new_dist:
                    max_cost = new_dist
                    max_idx = node[0]
                cost[node[0]] = new_dist
                heapq.heappush(q, (node[0], new_dist))
   #max_cost = max(max_cost, max(cost[1:]))
    #print(max_idx, max_cost)
    return max_idx
for i in range(n-1):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

# 루트에서 최장거리와 최장거리에서 최장거리
max_dist = dijkstra(1, [INF] * (n+1))
dijkstra(max_dist, [INF] * (n+1))
print(max_cost)
