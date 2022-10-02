def d_c(s):
    if len(s) == 1:
        return s
    mid = len(s) // 3
    m = [' ']*mid
    l = d_c(s[:mid])
    r = d_c(s[mid*2:])
    return l + m + r

while True:
    try:
        N = int(input())
        s = d_c(['-']*(3**N))
        print(''.join(s))
    except:
        break