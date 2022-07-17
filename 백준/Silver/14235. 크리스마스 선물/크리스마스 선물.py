from collections import deque
import heapq
import sys


n = int(input())
gift = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().strip().split()))
    if a[0] == 0:
        if len(gift) == 0:
            print(-1)
        else:
            print(heapq.heappop(gift)[1])
        
    if len(a)>1:
        for j in range(1, len(a)):
            heapq.heappush(gift, (-a[j], a[j]))