N = int(input())
d =[0]*(N+1)
count = 0
if N>0:
    d[1] =1
prev = 1
for i in range(2,N+1):
    d[i] = i* d[i-1]
str_num = str(d[N])

# str_num을 뒤에서부터 0이 나왔을때부터 0이 아닌 다른수가 나올때까지 카운트
for i in reversed(str_num):
    i = int(i)
    if prev ==0 and i != 0:
        break
    if prev!=0 and i==0:
        prev = 0
        count+=1
    elif prev ==0 and i ==0:
        count+=1
    
if N == 0:
    print(0)
else:
    print(count)