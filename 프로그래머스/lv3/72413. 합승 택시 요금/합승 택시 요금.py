import heapq
def solution(n, s, a, b, fares):
    # n은 노드의 개수
    # s에서 a와 b로가는 최소비용을 구한다.
    INF = int(1e9)
    distance = [INF] * (n+1)
    answer = INF
    graph = [[] for i in range(n+1)]
    def dijkstra(start, fee, fees, answer):
        q = []
        heapq.heappush(q, (fee, start))
        fees[start] = fee
        while q:
            fee, now = heapq.heappop(q)
            # ?
            if fees[now] < fee:
                continue
            # 현재 노드와 연결된 노드들과 최소거리 비교
            for i in graph[now]:
                # 다음 노드 까지의 비용
                cost = fee + i[1]
                if cost < fees[i[0]]:
                    fees[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        # print(fees)
        # print(answer, distance[start], fees[a], fees[b],min(answer, distance[start] + fees[a] + fees[b]))
        # 현재 노드의 최단거리와 목적지들의 최단거리합과 현재 최소 비용을 비교하여 작은 값 할당
        return min(answer, distance[start] + fees[a] + fees[b])
    
    # 그래프를 초기화
    for i in fares:
        start, end, fee = i
        graph[start].append((end,fee))
        graph[end].append((start,fee))
    # 시작 지점으로부터 노드간 최소거리 구한다.
    answer = dijkstra(s, 0, distance, answer)
    for i in range(1, n+1):
        if i == s:
            continue
        tmp_distance = [INF] * (n+1)
        # s기준의 i까지 최소거리부터 다익스트라를 돌려준다.
        answer = dijkstra(i, 0, tmp_distance, answer)
        #print(answer)
    return answer