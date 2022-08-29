from collections import deque 
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        is_visit = [0]*len(graph)
        def dfs(n, group):
            # group을 통하여 a b 를 나눈다.
            is_visit[n] = group
            for next_node in graph[n]:
                if is_visit[next_node] == group: # 같은 그룹이면 False
                    return False
                elif is_visit[next_node] == 0: # 방문하지 않은 노드는 방문
                    if not dfs(next_node, -group):
                        return False
            return True
                    
        for i in range(len(graph)):
            if not is_visit[i]:
                if not dfs(i, 1):
                    return False
        return True
            
