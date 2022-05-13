N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))
pivot = [[False for col in range(N)] for row in range(N)]
blue = 0
white = 0

def find_color(list, pivot, n, r,c):
    # 재귀로  width가 1이 나올때까지 가고 반환 받은 4개의 색상이 모두 같으면 fix
    global white
    global blue
    width = n//2
    is_success = [1]*4
    if n==1:
        return -1
    elif n==2: # n == 2 이면 각 칸을 확인하고 하나라도 다르면 칸별로 색의 숫자를 up / 다 같으면 해당 색의 번호를 return
        one_width = [list[r][c], list[r+1][c], list[r][c+1], list[r+1][c+1]]
        if not (one_width[0]==one_width[1]==one_width[2]==one_width[3]): # 다른 값이 하나라도 있으면 blue or white count
                for i in range(len(one_width)):
                    if one_width[i]== 1:
                        blue+=1
                    else:
                        white+=1
                return -1
        else: # 값이 모두 같으면 색 반환
            return one_width[0]
    else:
        is_success[0] = find_color(list, pivot, width,r,c) # 0 0/ 2 0 /0 2 /2 2
        is_success[1] = find_color(list, pivot, width,r+width,c)
        is_success[2] = find_color(list, pivot, width,r,c+width)
        is_success[3] = find_color(list, pivot, width,r+width,c+width)
        
        # 다 같은 색일 경우 , -1이 아니고
        if ((is_success[0] == is_success[1]== is_success[2]== is_success[3]!=-1)):
            if n==N:
                if is_success[0] == 1:
                    blue +=1
                else:
                    white+=1
            # if is_success[0] == 0:
            #     white+=1
            # else:
            #     blue+=1
            return is_success[0]
        else: # 다른 색이 하나라도 있으면 돌아가면서 색을 카운트
            for i in range(len(is_success)):
                if is_success[i] == 0:
                    white+=1
                elif is_success[i] == 1:
                    blue+=1
            return -1
find_color(paper, pivot, N,0,0)
print(white)
print(blue)