A, B =map(int, input().split())

# 최대 공약수
def least_cf(A,B):
    if B>A:
        A, B = B, A
    share, rest = divmod(A,B)
    if rest>0:
        return least_cf(B, rest)
    else:
        return B

# 최소 공배수
def least_cm(A, B):
    tmp_cf = least_cf(A,B)
    shareA = A//tmp_cf
    shareB = B//tmp_cf
    return tmp_cf*shareA*shareB

leastCf = least_cf(A,B)
leastCm = least_cm(A, B)
print(leastCf)
print(leastCm)