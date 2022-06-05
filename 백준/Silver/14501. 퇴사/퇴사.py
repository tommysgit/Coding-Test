# 14501
N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)
dp = [0]*(N+1)
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())
stack = []
result = []

def find(index):

    for i in range(index+1):
        if i - 1+ T[i] !=index:
            continue
        dp[index] = max(dp[index], max(dp[:i])+P[i])  

for i in range(1,N+1):
    find(i)
print(max(dp))