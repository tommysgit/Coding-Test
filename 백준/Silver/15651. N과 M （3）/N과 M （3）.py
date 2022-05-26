import itertools
N, M = map(int, input().split())
for i in (itertools.product(list(range(1,N+1)), repeat=M)):
    print(*i)