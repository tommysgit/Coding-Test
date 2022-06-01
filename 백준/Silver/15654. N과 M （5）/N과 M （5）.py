import itertools
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
permu = itertools.permutations(num, M)
for i in permu:
    print(*i)