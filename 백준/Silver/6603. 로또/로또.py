import itertools
while(1):
    TC = (list((map(int, input().split()))))
    k = TC[0]
    S = TC[1:]
    for i in itertools.combinations(S, 6):
        print(*i)
    if k == 0 : exit()
    print()