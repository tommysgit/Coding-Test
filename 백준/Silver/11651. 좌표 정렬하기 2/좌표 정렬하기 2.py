N = int(input())
cordinateList = [[0 for col in range(2)] for row in range(N)]
xList = []
yList = []
for i in range(N):
    x, y = map(int, input().split())
    cordinateList[i][0] = x
    cordinateList[i][1] = y
    # xList.append(x)
    # yList.append(y)
cordinateList.sort(key=lambda x: (x[1], x[0]))
xList =[i[0] for i in cordinateList]
yList = [i[1] for i in cordinateList]
for i in range(len(xList)):
    print(xList[i], yList[i])