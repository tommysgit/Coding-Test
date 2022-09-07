from itertools import combinations

INF = 1e9
N, M = map(int, input().split())
graph = []
houst_list = []
chicken_list = []
answer = INF
def cal(chicken):
    global answer
    dist_sum = 0
    for hr, hc in houst_list:
        dist = INF
        for cr, cc in chicken:
            dist = min(dist, abs(hr-cr) + abs(hc-cc))
        dist_sum += dist
    answer = min(answer, dist_sum)
                        

        
    
for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c] == 1:
            houst_list.append((r,c))
        elif row[c] == 2:
            chicken_list.append((r,c))
for combi in combinations(chicken_list, M):
    cal(combi)
print(answer) 