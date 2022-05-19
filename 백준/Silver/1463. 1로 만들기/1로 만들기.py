N = int(input())
dp = [0]*(N+1)
dp[1] = 0
if 2<=N:
    dp[2] = 1
if 3<=N:
    dp[3] = 1
# 1에서 출발하여 dp[N+1]까지 1을 더하거나 3을 곱하거나 2를 곱하거나 최소한의 연산으로 도달하도록
for i in range(4,N+1):
    three_share, three_rest = divmod(i, 3)
    two_share, two_rest = divmod(i, 2)
    # i일때 가능한 수 나머지가 0이면 몫*2 혹은 3 or 
    mins = []
    if three_rest == 0:
        mins.append(dp[three_share]+1)
    if two_rest == 0:
        mins.append(dp[two_share] + 1)
    if three_rest != 0:
        mins.append(dp[three_share*3] + three_rest)
    if two_rest != 0:
        mins.append(dp[two_share*2] + two_rest)
    dp[i] = min(mins)
print(dp[N])