# 1967
import sys
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
max_cost = 0
# 각 노드별로 왼쪽과 오른쪽의 최장거리를 구하고 거리가 최대가 되는 노드를 택한다
def dfs(i, cost):
    global max_cost
    # i번째 노드를 방문
    # i번째 노드의 좌 우 최장거리는 아직 0
    left, right = 0, 0
    # i번째 노드와 연결된 좌우 노드를 탐색
    for next_node, dist in graph[i]:
        # 연결된 다음 노드의 최대 비용을 반환
        new_cost = dfs(next_node, dist)
        # 연결된 자식 노드의 개수가 1개일 경우 왼쪽으로
        # 2개일 경우 오른쪽으로
        # 3개 이상일 경우 왼쪽 오른쪽중 거리가 더 작은 곳을 갱신한다.
        if left <= right:
            left = max(left, new_cost)
        else:
            right = max(right, new_cost)
    # 해당 노드 기준 최장거리와 기존 최장거리를 비교하여 갱신
    max_cost = max(max_cost, left+right)
    return max(left+cost, right+cost)
dfs(1, 0)
print(max_cost)
