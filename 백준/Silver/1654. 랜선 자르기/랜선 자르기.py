K, N = map(int, input().split())
lans = []
for i in range(K):
    lans.append(int(input()))
def binary_search(lans, left, right, target):
    while left <=right:
        mid = (left+right)//2
        get_lans = 0
        # mid로 lans 배열을 돌면서 나누고 몫을 get_lans에 할당
        for i in lans:
            if i>=mid:
                get_lans += i//mid
        # get_lans가 target보다 작으면 길이를 더 짧게 잘라야 하므로 right = mid-1
        if get_lans< target:
            right = mid-1
        else:
            left = mid+1
    return right
output = binary_search(lans, 1, max(lans), N)
print(output)
            