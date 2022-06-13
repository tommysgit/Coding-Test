# 1874
import sys
n = int(input())
sequence_num = []
stack3 = []
result = []
stack = []
cur = 1
is_fail =0
for i in range(n):
    sequence_num.append(int(sys.stdin.readline()))
# for i in reversed(range(1, n+1)):
#     stack.append(i)
for i in sequence_num:
    while cur <= i:
        stack3.append(cur)
        result.append("+")
        cur += 1
    num = stack3.pop()
    result.append("-")
    stack.append(num)
    # if i != num  :
    #     print("No")
    #     is_fail = 1
    #     break
if  2*n == len(result) and stack == sequence_num:
    for i in result:
        print(i)
else:
    print("NO")