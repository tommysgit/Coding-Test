n, m = map(int, input().split())
d = [0] * (n+1)
d[0] = 1
d[1] = 1
for i in range(2, n+1):
    d[i] = i * d[i-1]
print(d[n] // (d[n-m] * d[m]))