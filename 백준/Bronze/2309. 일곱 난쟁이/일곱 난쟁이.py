from itertools import combinations
h = []
def find(pivot):
    
    pass
for i in range(9):
    h.append(int(input()))
combi = list(combinations(h, 7))
for i in range(len(combi)):
    if sum(combi[i]) == 100:
        output = sorted(combi[i])
        for j in output:
            print(j)
        break