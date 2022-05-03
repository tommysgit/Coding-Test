N = int(input())
cordinate = [[0 for cor in range(2)] for row in range(N)]
for i in range(N):
    x, y = map(int,  input().split())
    cordinate[i][0] = x
    cordinate[i][1] = y
cordinate.sort(key=lambda x: (x[0], x[1]))
for i in range (len(cordinate)):
    print(cordinate[i][0], cordinate[i][1])