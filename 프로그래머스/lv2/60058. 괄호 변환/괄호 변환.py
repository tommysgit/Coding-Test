def solution(p):
    answer = ''
    def divide(w):
        left = 0
        right = 0
        for i in range(len(w)):
            if w[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                standard = i + 1
                break

        if standard == len(w) - 1:
            return w, ""
        else:
            return w[:standard], w[standard:]
    # 옳바른 문자열인지 판별
    def is_correct(s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if not stack:
                    return 0
                tmp = stack.pop()
                if tmp != "(":
                    return 0
        return 1
    def to_correct(u):
        s = "("
        
    # u는 균형잡힌 문자열, v는 빈 문자열일 수 있다.
    def recursion_bracket(w):
        # 1
        if not w:
            return ""
        # 2
        u, v = divide(w)
        # 3
        if is_correct(u):
            if v:
                u = u + recursion_bracket(v)
            return u
        # 4
        else:
            tmp = "(" + recursion_bracket(v) + ")"
            if len(u)>3:
                for i in range(1, len(u)-1):
                    if u[i] == "(":
                        tmp += ")"
                    else:
                        tmp += "("
            return tmp
            
        
    answer = recursion_bracket(p)
    
    return answer