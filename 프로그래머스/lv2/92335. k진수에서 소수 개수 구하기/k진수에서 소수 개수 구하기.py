import math
def solution(n, k):
    answer = 0
    changed_num = str(n)
    # n을 k진수로 변환
    # k를 나눈 나머지를 stack에 넣고 pop을 이용하여 숫자의 앞에서 부터 채워준다.
    def change_decimal(n, k):
        stack = []
        result = ''
        while n >= k:
            n, rest = divmod(n, k)
            stack.append(str(rest))
        if n != 0:
            stack.append(str(n))
        while stack:
            result += stack.pop()
        return result
    # 소수인지 판별 하는 함수 
    # 처음에 for 문으로 모든 수로 나누어 떨어지는지 확인했다가 시간초과나서 제곱근으로 나누어도 된다는 것을 알고 변경
    def prime_num(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    # 리스트에 쌓여있는 수가 조건에 해당하는지 판별하는 함수
    # 코드가 중복되어 함수로 변경하였음
    def check(tmp_num, answer):
        if tmp_num:
                num = ''.join(str(s) for s in (tmp_num))
                if prime_num(int(num)):
                    answer += 1
                tmp_num.clear()
        return answer
    # 10진수가 아닌 수는 k진수로 변경한다.
    if k != 10:
        changed_num = change_decimal(n,k)
    tmp_num = []
    # 변경된 모든 수를 돌며 리스트에 넣고 0을 만나면 쌓여있는 리스트가 조건에 해당하면 answer을 증가
    # 0을 만났을 때만 리스트 안의 값을 확인하니 0으로 끝나지 않은 수를 고려하여 한번 더 확인한다.
    for i in range(len(changed_num)):
        if changed_num[i] == '0':
            answer = check(tmp_num, answer)
            continue
        tmp_num.append(changed_num[i])
    answer = check(tmp_num, answer)
    
    return answer