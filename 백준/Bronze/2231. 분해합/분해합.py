N = int(input())
output = 0
for i in range(1,N+1):
    val = int(i) #245
    tmp = val #245
    strVal = str(i) #245 str
    for j in strVal:
        tmp = tmp + int(j) # 245 + 2 + 4 + 5
    con = tmp
    if con ==N:
        output = val
        break
print(output)  