def binary_search(left, right, n):
    if left > right:
        return left
    mid = (left + right) // 2
    if mid**2 >= n:
        return binary_search(left, mid-1, n)
    else:
        return binary_search(mid+1, right, n)

n = int(input())

print(binary_search(0, n, n))