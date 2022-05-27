T = int(input())
output=[]
for i in range(T):
    num = int(input())
    dp = [0] *(num+1)
    dp[1] = 1
    if num>1:
        dp[2] = 2
    if num>2:
        dp[3] = 4
    if num>3:
        for i in range(4,num+1):    
            dp[i] = dp[i-1]+dp[i-3] + dp[i-2]
    output.append(dp[num])
    
for i in output:
    print(i)