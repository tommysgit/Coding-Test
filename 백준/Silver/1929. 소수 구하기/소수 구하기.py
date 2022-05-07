N, M = map(int, input().split())
numbers = list(range(N,M+1))
decimal = []
# 숫자가 소수인지 판별
def disc_decimal(number):
    if number<2:
        return False
    i = 2
    isDescimal = True
    while i*i<=number:
        
        if number%i==0:
            isDescimal = False
            break
        i +=1
    return isDescimal
for i in range(len(numbers)):
    if  disc_decimal(numbers[i]):
        decimal.append(numbers[i])
for i in range(len(decimal)):
    print(decimal[i])