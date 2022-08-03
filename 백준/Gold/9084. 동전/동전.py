# 9084
T = int(input())
 
def dp(amount):
    d = [0]*(amount+1)
    d[0] = 1
    for coin in coin_list:
        for i in range(1, amount+1):
            if i >= coin:
                d[i] += d[i-coin]
    print(d[amount])
    
for i in range(T):
    # 동전 가지수
    N = int(input())
    # 동전 금액 오름차순
    coin_list = list(map(int, input().split()))
    # 금액
    amount = int(input())
    dp(amount)
