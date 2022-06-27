result = []
N = int(input())
N_num = list(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))
def binary_search(left,right,target):
    while left<=right:
        mid = (left + right) // 2
        if N_num[mid] == target:
            return mid
        elif N_num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None
N_num.sort()
hash_num = {i : 0 for i in set(N_num)}
for i in N_num:
    hash_num[i] += 1
for i in M_num:
    tmp = hash_num.get(i)
    if tmp != None:
        result.append(tmp)
    else:
        result.append(0)
print(*result)