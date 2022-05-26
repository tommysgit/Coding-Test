import itertools
N, M = map(int, input().split())
combi = itertools.combinations(list(range(1, N+1)), M)
output = []
for i in (combi):
    if list(i) not in output:
        output.append(list(i))
for i in output:
    print(*i)