N, M = map(int, input().split())
number = list(map(int, input().split()))
sum = 0
minor = -1
for i in range(len(number)-2):

    if len(number) - (i+2)<=0:
        break
    for j in range(i+1,len(number)-1):
        for k in range(j+1,len(number)):
            tmp = int(number[i]) + int(number[j]) + int(number[k])
            if M-tmp >=0 and(minor == -1 or minor> M-tmp):# M과 i,j,k자리의 합의 차가 기존보다 낮으면 sum에 추가
                minor =M- tmp
                sum = tmp
print(sum)