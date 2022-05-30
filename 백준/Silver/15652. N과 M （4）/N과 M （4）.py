import itertools
N, M = map(int, input().split())
combi = itertools.combinations_with_replacement(range(1, N+1), M)
for i in combi:
    print(*i)