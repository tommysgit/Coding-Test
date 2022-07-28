N = int(input())
X = list(map(int, input().split()))
# 입력 받은 값들을 0부터 순번으로 나타낸다.
my_hash = {}
for x in X:
    if not my_hash.get(x):
        my_hash[x] = 0
sorted_list = sorted(my_hash.items(), key= lambda x : x[0])
count = 0
for i in sorted_list:
    my_hash[i[0]] = count
    count += 1
result = [my_hash[X[i]] for i in range(len(X))]
print(*result)