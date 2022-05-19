import sys
sys.setrecursionlimit(64*64)
N = int(input())
video = []
for i in range(N):
    video.append(str(input()))
    
def devide(video, n,r,c):
    global N
    if n == 1:
        return (video[r][c])
    next_n = n//2
    upper_left = (devide(video, next_n,r,c))
    upper_right = (devide(video, next_n, r, c + next_n))
    lower_left = (devide(video, next_n, r+next_n, c))
    lower_right = (devide(video, next_n, r+next_n, c+next_n))
    if (upper_left == upper_right == lower_left == lower_right) and len(upper_left)==1:
        return (upper_left)
    else:
        return "("+(upper_left)+upper_right+lower_left+lower_right+")"
    
print(devide(video, N,0,0))