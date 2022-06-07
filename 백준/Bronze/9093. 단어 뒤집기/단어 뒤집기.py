T = int(input())
result = [[]for _ in range(T)]
def reverse_str(strings : str, index):
    stack = strings.split()
    tmp = ""
    for i in (stack):
        tmp += i[::-1] + " "
    result[index].append(tmp)
for i in range(T):
    strings = (input())
    reverse_str(strings, i)
for i in range(T):
    print(*result[i])