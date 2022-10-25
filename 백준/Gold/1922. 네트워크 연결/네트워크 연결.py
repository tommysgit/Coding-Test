import heapq


N = int(input())
M = int(input())
q = []
ans = 0
# 특정 원소가 속한 집한 찾기
def find_parent(parent, x):
    # 루트를 찾을 때까지 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b 

for i in range(M):
    # a, b 연결 비용 c
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a,b))
parent = [i for i in range(N+1)]
while q:
    c, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += c

print(ans)