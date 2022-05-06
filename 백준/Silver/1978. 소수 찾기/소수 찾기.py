N = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(len(numbers)):
    num = numbers[i]
    if num == 1 :
        continue
    elif num == 2 :
        count +=1
        continue
    isDecimal = True
    for j in range(2,num):
        share, rest = divmod(num, j)
        if rest == 0:
            isDecimal = False
    if isDecimal == True:
        count += 1
print(count)