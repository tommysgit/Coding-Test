N = int(input())
stairs = [0]
for i in range(N):
    stairs.append(int(input()))

if N  == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
else:
    dp = [0] *(N+1)
    dp[1] = stairs[1]
    dp[2] = stairs[2] + dp[1]
    # dp[i]는 i번째 계단에서의 최대 값
    # i번째에 도달했을 때 i번째 계단과 i-1번째 계단 + i-3번째의 최댓값과 i번째 계단 i-2번째의 최댓값의 합을 비교
    for i in range(3,N+1):
        dp[i] = max(stairs[i]+dp[i-2], stairs[i]+stairs[i-1]+dp[i-3])
    print(dp[N])