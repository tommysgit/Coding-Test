def fibonacci(n):
    if n == 0:
        d[0] = 0
        count[0][0] = 1
        count[0][1] = 0
        return d[0]
    elif n==1:
        count[1][0] = 0
        count[1][1] = 1
        d[1] = 1
        return d[1]
    if d[n] != 0:
        return d[n]
    count[n][0] = count[n-1][0] + count[n-2][0]
    count[n][1] = count[n-1][1] + count[n-2][1]
    d[n] = fibonacci(n-1) + fibonacci(n-2)
    return d[n]
tmp1 = []
d = [0]*41
count = [[0 for i in range(2)] for j in range(41)]
fibo_num = []
N = int(input())
for i in range(N):
    fibo_num.append(int(input()))
    
for i in range(len(fibo_num)):
    for j in range(fibo_num[i]+1):
        fibonacci(j)
for i in range(len(fibo_num)):
    print(*count[fibo_num[i]])