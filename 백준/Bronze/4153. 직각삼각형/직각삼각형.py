output = []
while(True):
    side = list(map(int, input().split()))
    if side[0]==side[1]==side[2]==0:
        break
    side.sort(reverse=True)
    a = side[0]*side[0]
    b = side[1]*side[1]
    c = side[2]*side[2]
    if a==b+c:
        output.append("right")
    else:
        output.append("wrong")
for i in output:
    print(i)