import sys
sys.setrecursionlimit(10**6)
def dfs(edge, node, is_visit):
    if is_visit[node]:
        print(node)
        return
    is_visit[node] = 1

    for next_node in edge[node]:
        dfs(edge, next_node, is_visit)
        
    return

T = int(input())
for i in range(T):
    N = int(input())
    edge = [[]for i in range(N+1)]
    for j in range(N):
        # A는 B의 부모 노드
        A, B = map(int, sys.stdin.readline().split())
        line_list = []
        is_visit = [0]*(N+1)
        if j == N-1:
            # 공통조상 타겟
            for target in [A,B]:
                dfs(edge, target, is_visit)
        else:
            edge[B].append(A)