N = int(input())
count = 0
for i in range(N):
    tmp = []
    word = str(input())
    isGroup = 1
    for index, spell in enumerate(word):
        if spell not in tmp:
            tmp.append(spell)
        elif spell in tmp and index != 0 and word[index-1] != spell:
            isGroup = 0
    if isGroup == 1:
        count = count + 1
print(count)