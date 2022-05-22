N, r, c = map(int, input().split())
n = 2**N
z_num = 0
final = 0
# n x n 크기의 그래프
# n = 1 1개 / n = 2 4개 / n = 3 16개 -> ( 2^n * 2^n ) // 4
# 몇번째 z인지 찾고 좌상은 -3 우상은 -2 좌하는 -1 우하는 -0

def find_z(x,y,r,c,n):
    global z_num
    global final
    divide_n = n//2
    sector_z = ( n*n ) // 16 # n = 3 -> 4 / n = 2 -> 1
    if n==1:
        z_num+=1
        
        if final == 1:
            z_num = z_num*4 - 3 -1
            return 
            
        elif final == 2:
            z_num = z_num*4 - 1 -1

            return
            
        elif final == 3:
            z_num = z_num*4 - 2 -1
            return
            
        elif final == 4:
            z_num = z_num*4 -1
            return 
    else:
        if r< x+divide_n and c<y+divide_n:
            final = 1
            find_z(x,y,r,c,divide_n)
            
        elif r<x+n and c<y+divide_n:
            z_num += (sector_z*2)
            final = 2
            find_z(x+divide_n, y,r,c,divide_n)
            
        elif r<x+divide_n and c<y+n:
            z_num += (sector_z*1)
            final = 3
            find_z(x,y+divide_n,r,c,divide_n)
            
        else:
            z_num += (sector_z*3)
            final = 4
            find_z(x+divide_n,y+divide_n,r,c,divide_n)
            
find_z(0,0,r,c,2**N)
print(z_num)