N = int(input())
A = list(map(int, input().split()))
plus, minus, product, division = map(int, input().split())
stack = []
max_val = (-1e9)
min_val = (1e9)
# 최대가 나오는 방법
# 값을 크기 순서로 나열하고 큰 값부터 곱, 더하기, 빼기, 나누기 순서로 계산

def dfs(depth, val, plus, minus, product, division):
    global max_val
    global min_val
    if depth == len(A):
        max_val = max(max_val, val)
        min_val = min(min_val, val)
    #print(depth, val, plus, minus, product, division)
    if plus:
        dfs(depth + 1, val + A[depth], plus - 1,  minus, product, division)
    if minus:
        dfs(depth+1, val - A[depth], plus, minus - 1, product, division)
    if product:
        dfs(depth + 1, val * A[depth], plus, minus, product - 1, division)
    if division:
        # // 연산은 음수의 경우 정수값하나가 더 올라가서 주의
        dfs(depth+1, int(val/ A[depth]), plus, minus, product, division - 1)
        
    
dfs(1, A[0], plus, minus, product, division)
print(max_val)
print(min_val)