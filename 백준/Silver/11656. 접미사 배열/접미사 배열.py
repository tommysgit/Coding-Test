strings = input()
result = []
for i in range(len(strings)):
    result.append(strings[i:])
result.sort()
for i in result:
    print(i)