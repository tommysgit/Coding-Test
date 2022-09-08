from collections import deque
#from time import time

#start = time()
my_hash = {}
answer_list = list(map(int, input().split()))
for i in range(10):
    my_hash[i] = answer_list[i]
user_answer = deque()
cnt = 0
def back_track(pick, ans, depth):
    global cnt
    if depth == 10:
        if ans >= 5:
            cnt += 1
        return
    
    for num in range(1,6):
        if depth > 1 and pick[-2] == pick[-1] and pick[-1] == num:
            continue
        pick.append(num)
        tmp = ans + 1 if my_hash[depth] == num  else ans
        back_track(pick, tmp, depth + 1)
        pick.pop()
back_track(user_answer, 0, 0)
print(cnt)