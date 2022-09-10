import sys


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

graph_rowsum = [[0 for col in range(N)]  for row in range(N) ]
for row in range(N):
    row_sum = 0
    for col in range(N):
        graph_rowsum[row][col] += (row_sum + graph[row][col])
        row_sum += graph[row][col]

# x1, y1 부터 x2, y2까지의 합을 순서대로 출력
for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, y2 = x1 - 1 , y1 - 1, y2-1
    max_sum = 0
    for row in range(x1, x2):
        if y1 == 0:
            max_sum += graph_rowsum[row][y2]
            continue
        max_sum += (graph_rowsum[row][y2] - graph_rowsum[row][y1-1])
    print(max_sum)