import sys
import itertools
N, M = map(int, input().split())
accum_N = []
# N개의 수
N_list = list(map(int, sys.stdin.readline().strip().split()))
# 누적합
accum = itertools.accumulate(N_list)
for i in accum:
    accum_N.append(i)
# M개의 줄
for i in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    if start > 1:
        print(accum_N[end-1]-accum_N[start-2])
    else:
        print(accum_N[end-1])