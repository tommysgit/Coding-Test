N = int(input())
graph = [list(map(int, input().split())) for r in range(N)]
def devide(size, x, y):
    if size == 2:
        tmp = [graph[x][y], graph[x][y+1], graph[x+1][y], graph[x+1][y+1]]
        tmp.sort()
        return tmp[2]
    n = size // 2
    A = devide(n, x, y)
    B = devide(n, x, y+n)
    C = devide(n, x+n, y)
    D = devide(n, x+n, y+n)
    ans = [A,B,C,D]
    ans.sort()
    return ans[2]
print(devide(len(graph), 0, 0))