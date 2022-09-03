def solution(a, b, n):
    answer = 0
    share, rest =divmod(n, a)
    # 3, 2, 21
    # 14 14 / 14 + 8 , 2
    while share:
        answer += (share*b)
        n = (rest + share*b)
        share, rest = divmod(n,a)

    return answer