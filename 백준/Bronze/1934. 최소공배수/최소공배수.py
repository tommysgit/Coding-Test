T = int(input())
result = []
for i in range(T):
    A, B = map(int, input().split())
    gcd = 1
    for i in reversed(range(1, A+1)):
        if (A%i==0)and(B%i==0):
            gcd = i
            break
    result.append(int(A*B/gcd))
for i in result:
    print(i)