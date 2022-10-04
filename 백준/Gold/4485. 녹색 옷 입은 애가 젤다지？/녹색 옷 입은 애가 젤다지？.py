import heapq
import sys


problem = 0
def dijkstra(cave):
    costs = [[1e9 for c in range(len(cave))] for r in range(len(cave))]
    costs[0][0] = cave[0][0]
    q = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    heapq.heappush(q, (cave[0][0], 0, 0))
    while q:
        cost, r, c = heapq.heappop(q)
        # 방문한 곳의 값이 작으면 건너띄고 크다면 갱신
        if costs[r][c] < cost:
            continue
        for i in range(4):
            mr = r + dr[i]
            mc = c + dc[i]
            if 0<= mr < len(cave) and 0 <= mc < len(cave):
                new_cost = cost + cave[mr][mc]
                if new_cost < costs[mr][mc]:
                    heapq.heappush(q, (new_cost, mr, mc))
                    costs[mr][mc] = new_cost
    return costs[len(cave)-1][len(cave)-1]

            


while 1:
    N = int(input())
    if N == 0:
        break
    problem += 1
    cave = []
    for i in range(N):
        cave.append(list(map(int, sys.stdin.readline().split())))
    cost = dijkstra(cave)
    print("Problem " +str(problem)+ ": " + str(cost))