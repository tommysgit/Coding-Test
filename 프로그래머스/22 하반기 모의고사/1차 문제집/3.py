from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[]for i in range(n+1)]
    distance = [1e9] * (n+1)
    def bfs(is_visit):
        q = deque([])
        q.append((destination, 0))
        distance[destination] = 0
        is_visit[destination] = 1
        while q:
            source, dist = q.popleft()
            distance[source] = min(distance[source], dist)

            # is_visit[source] = 1
            # distance[source] = dist
            for next_source in graph[source]:
                if not is_visit[next_source]:
                    is_visit[next_source] = 1
                    q.append((next_source, dist + 1))
        
    for i in range(len(roads)):
        a, b = roads[i]
        #print(a,b)
        graph[a].append(b)
        graph[b].append(a)
    # source의 리스트를 차례대로 목적지까지 최소거리 반환
    is_visit = [0]*(n+1)
    bfs(is_visit)
    for source in sources:
        dist = distance[source]
        if dist == 1e9:
            answer.append(-1)
        else:
            answer.append(dist)
    return answer