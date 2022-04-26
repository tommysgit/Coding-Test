N, K = map(int, input().split())
N = list(range(1, N+1))
sequence = []
cur = len(N)-1
while(len(N)>0):
    if len(N) == 1:
        sequence.append(N[0])
        del N[0]
        break
    for i in range(K):
        if cur == len(N)-1:
            cur = 0
        else:
            cur = cur + 1
    sequence.append(N[cur])
    del N[cur]
    if len(N) == 1:
        sequence.append(N[0])
        del N[0]
        break
    else:
        if cur == 0:
            cur = len(N) - 1
        else :
            cur = cur -1
final = sequence
output = "<"
for i in range(len(final)):
    output = output + str(final[i])
    if i == len(final)- 1:
        output = output + ">"
    else:
        output = output + ", "
print(output)