class Solution:
    def isValid(self, s: str) -> bool:
        answer = False
        s_hash = {')' : '(', ']' : '[' , '}' : '{'}
        close_list = [']', '}', ')']
        stack = []
        for c in s:
            if c in close_list:
                if stack:
                    last_c = stack[-1]
                    # 스택의 끝부분과 현재 문자비교
                    # 다르다면 종료 같으면 pop
                    if s_hash[c] != last_c:
                        break
                    else:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            answer = False
        else:
            answer = True
        return answer