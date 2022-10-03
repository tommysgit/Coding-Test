N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort()
ans = 0
for pair in zip(A,B):
    ans += (pair[0]*pair[1])
print(ans)