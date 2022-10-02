N = int(input())
chickens = list(map(int, input().split()))
k = int(input())

t_a = []
p = N // k
for i in range(0, len(chickens), p):
    t = chickens[i : i + p]
    t.sort()
    t_a += t
print(*t_a)