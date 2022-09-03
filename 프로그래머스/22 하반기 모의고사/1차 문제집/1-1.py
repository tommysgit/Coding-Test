from collections import Counter
def solution(X, Y):
    answer = ''
    x_count = Counter(X)
    y_count = Counter(Y)
    x_count = sorted(x_count.items(), key = lambda x : -int(x[0]))
    for x, num in x_count:
        if x in y_count:
            answer += (x * min(num, y_count[x]))

    if len(answer) == 0:
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    return answer