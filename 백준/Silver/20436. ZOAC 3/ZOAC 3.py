L, R = map(str, input().split())
string = input()
keyboard = []
keyboard.append(['q','w','e','r','t','y','u','i','o','p'])
keyboard.append(['a','s','d','f','g','h','j','k','l'])
keyboard.append(['z','x','c','v','b','n','m'])
my_hash = {}
r_set = set(('y','u','i','o','p','h','j','k','l','b','n','m'))
for i in range(3):
    for j in range(len(keyboard[i])):
        my_hash[keyboard[i][j]] = (i+1,j+1)
time = 0
for i in string:
    time += 1
    if i == R or i == L:
        continue
    cur_r, cur_c = my_hash[i]
    if i in r_set:
        right_r, right_c = my_hash[R]
        time += (abs(cur_r - right_r) + abs(cur_c - right_c))
        R = i
    else:
        left_r, left_c = my_hash[L]
        time += (abs(cur_r - left_r) + abs(cur_c - left_c))
        L = i
print(time)