N = int(input())
list_n = list(map(int, input().split()))
list_n.sort()
M = int(input())
list_m = list(map(int, input().split()))
output = []
def binary_search(list ,left, right, target):
    exist = False
    while left<=right:
        mid = (left+right)//2
        if list[mid]>target:
            right = mid-1
        elif list[mid]<target:
            left = mid+1
        else:
            exist = True
            break
    return exist
for i in list_m:
    output.append(binary_search(list_n, 0, len(list_n)-1, i))
for i in range(len(output)):
    if output[i] == True:
        print(1)
    else:
        print(0)