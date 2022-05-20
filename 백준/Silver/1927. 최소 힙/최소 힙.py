import heapq
import sys

N = int(sys.stdin.readline())
heap = []
prints = []
for i in range(N):
    X = int(sys.stdin.readline())
    if X!=0:
        heapq.heappush(heap, X)
    else:
        if len(heap) <=0:
            prints.append(0)
        else:
            prints.append(heapq.heappop(heap))
for i in range(len(prints)):
    print(prints[i])