# 14890
N, L = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def is_way(way, is_runway):
    # i번째부터 L길이만큼의 위치들의 높이가 같거나 1만차이나야한다. 
    prev = way[0]
    for i in range(1, N):
        # prev와 cur이 2이상 차이나면 false
        if abs(prev - way[i]) > 1:
            return 0
        # 내리막길
        elif prev - way[i] == 1 :
            # i번째부터 L길이 뒤만큼 높이가 같은지 확인
            if i+L > N:
                return 0
            if len(set(way[i:i+L])) > 1:
                return 0
            # 경사로 생성
            for j in range(i, i+L):
                if is_runway[j] == 1:
                    return 0
                is_runway[j] = 1
            
        # 오르막길
        elif prev - way[i] == -1:
            # i번쨉부터 L길이 앞에까지 높이가 같은지 확인
            if i - L < 0:
                return 0
            if len(set(way[i-L:i])) > 1:
                return 0
            for j in range(i-L, i):
                if is_runway[j] == 1:
                    return 0
                is_runway[j] = 1
        prev = way[i]
    return 1
    
count = 0
for row in range(N):
    if is_way(graph[row], [0]*N):
        #print(graph[row])
        count += 1

for col in map(list, zip(*graph)):
    if is_way(col, [0]*N):
        #print(col)
        count += 1
print(count)