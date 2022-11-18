from collections import deque
def bfs(n, is_visit, edges, wire):
    is_visit[n] = 1
    q = deque()
    cnt = 0
    q.append(n)
    while q:
        n = q.popleft()
        cnt += 1
        for next_node in edges[n]:
            if is_visit[next_node] == 0:
                #print(wire, n, next_node, n in wire and next_node in wire)
                if n in wire and next_node in wire:
                    continue
                is_visit[next_node] = 1
                q.append(next_node)
    return cnt
def solution(n, wires):
    answer = 1e9
    edges = [[] for i in range(n+1)]
    for i, v in enumerate(wires):
        a, b = v
        edges[a].append(b)
        edges[b].append(a)
    # edge들을 돌면서 하나씩 끊는다.
    for wire in wires:
        is_visit = [0]*(n+1)
        tmp = []
        for node in range(1, n+1):
            # bfs edge는 빼고 bfs
            if is_visit[node] == 0:
                result = bfs(node, is_visit, edges, wire)
                tmp.append(result)
        if len(tmp) == 2:
            answer = min(answer, abs(tmp[0] - tmp[1]))
                
    return answer