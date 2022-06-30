from itertools import combinations
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
house_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house_list.append((i,j))
        if graph[i][j] == 2:
            chicken_list.append((i,j))
min_chicken_distance = 10000
for i in combinations(chicken_list, M):
    i_distance_sum = 0
    for j in range(len(house_list)):
        min_distance = 10000
        house_r, house_c = house_list[j]
        for k in range(M):
            chicken_r , chicken_c = i[k]
            min_distance = min(min_distance, abs(house_r - chicken_r) + abs(house_c - chicken_c))
        i_distance_sum += min_distance
    min_chicken_distance = min(min_chicken_distance, i_distance_sum)
print(min_chicken_distance)