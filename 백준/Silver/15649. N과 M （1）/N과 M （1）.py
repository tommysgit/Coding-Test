import itertools
N, M = map(int, input().split())
numbers = list(range(1,N+1))
nPr = itertools.permutations(numbers, M)
for i in (nPr):
    print(*list(i))
