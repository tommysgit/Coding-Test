import sys
N = int(input())
heap =[]
answer = -1
# 최대한 늦게 몇시에 시작해야 N개의 일을 끝낼 수 있는가.
for i in range(N):
    T, S = map(int, sys.stdin.readline().strip().split())
    heap.append((S,T))
# 늦게 끝내도 되는 순으로 정렬
heap.sort(reverse=True)
# 가장 늦게 끝내도 되는일을 끝내는 시간 계산, 즉 가장 늦게 시작해도 되는 시간
answer = heap[0][0] - heap[0][1]
for i in range(1,N):
    # i번째 일을 끝내야 하는 시기가 기존 시기보다 빠르다면 갱신
    if answer > heap[i][0]:
        answer = heap[i][0] - heap[i][1]
        
    # 기존에 늦게 끝내도 되는 시기안에 끝낼 수 있다면 그 일을 그냥 끝낸다.
    else:
        answer -= heap[i][1]
print(answer if answer > -1 else -1)