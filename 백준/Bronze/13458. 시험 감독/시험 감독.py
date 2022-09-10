N = int(input())
exam_room = list(map(int, input().split()))

B, C = map(int, input().split())
cnt = 0
# 한 시험장에서 총 감독관 감시가능한 수 B명 부감독관 C명
# 한 시험장의 총감독관 1명이상 부감독관 여러명 가능
for people in exam_room:
    people -= B
    if people < 0:
        cnt += 1
        continue
    share, rest = divmod(people, C)
    if rest:
        cnt += (share + 2)
    else:
        cnt += (share + 1)
print(cnt)