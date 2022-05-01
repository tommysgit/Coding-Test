N = int(input())
word = []
for i in range(N):
    word.append(str(input()))
word.sort(key=lambda x:(len(x), x))
result =[]
for i in word:
    if i not in result:
        result.append(i)
for i in result:
    print(i)