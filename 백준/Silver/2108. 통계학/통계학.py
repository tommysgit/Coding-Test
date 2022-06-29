import sys
import collections

N = int(input())
# N개의 수를 입력받고 평균, 중앙값, 최빈값, 범위(최대 최소차이)를 구한다.
result = []
for i in range(N):
    num = int(sys.stdin.readline())
    result.append(num)
result.sort()
cnt = collections.Counter(result)
print(int(round(sum(result)/len(result), 0)))
print(result[len(result)//2])
cnt_list = cnt.most_common(2)
if N>1:
    if cnt_list[0][1]== cnt_list[1][1]:
       print(cnt_list[1][0])
    else:
       print(cnt_list[0][0])
else:
    print(result[0])
print(result[len(result)-1] - result[0])
