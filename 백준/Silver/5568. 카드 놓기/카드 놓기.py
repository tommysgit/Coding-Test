from itertools import permutations

n = int(input())
k = int(input())
numbers = []
for i in range(n):
    numbers.append(str(input()))

combi = []
for p in permutations(numbers,k):
    s = ''
    for n in p:
        s += n
    combi.append(s)
print(len(set(combi)))