import sys
def solution(n, lighthouse):
    sys.setrecursionlimit(1000000)
    def dfs(graph, is_visit, node):
        is_visit[node] = 1
        # 해당 노드의 방문하지 않은 자식노드 반환
        children_node = [ child for child in graph[node] if not is_visit[child]]
        pick, not_pick = 1, 0
        # 리프노드인지 아닌지
        # 리프노드라면 고르지 않아도된다. 
        for child in children_node:
            child_pick, child_not_pick = dfs(graph, is_visit, child)
            # 모든 자식노드를 고르지 않았으면 현재 노드를 골라야함
            # 자식 노드를 골랐으면 현재 노드를 고르지 않아도됨
            # child_not_pick이 무조건 child_pick보다 작지않다. 
            # -> 손자를 모두 고르고 자식을 고르지 않는 경우 때문
            not_pick += child_pick
            pick += min(child_pick, child_not_pick)
        return (pick, not_pick)

    # n개의 노드와 n-1개의 노선 lighthouse
    graph = [[] for _ in range(n+1)]
    is_visit = [0]*(n+1)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    answer = dfs(graph, is_visit, 1)
    return min(answer)