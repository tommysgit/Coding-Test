T = int(input())
output = []

def comb(arr, n):
    result = []
    if n > len(arr):
        return 0
    
    if n == 1:
        return len(arr)
    else:
        for i in range(len(arr) -n +1):
            for j in comb(arr[i+1], n-1):
                result.append()

for i in range(T):
    n = int(input())
    hash_map = dict()
    for j in range(n):
        fashion, sort = input().split()
        if sort not in hash_map:
            hash_map[sort] = [fashion]
        else:
            hash_map[sort].append(fashion)
    keys = hash_map.keys()
    count = 1
    # 모든 의상의 종류의 개수 +1 (입지 않을 경우) 를 곱한다.
    for j in keys:
        count *= (len(hash_map.get(j))+1)
    count -=1
    output.append(count)
for i in range(len(output)):
    print(output[i])  