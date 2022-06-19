count = [0]*26
S = input()
for i in S:
    count[ord(i)-97] +=1
print(*count)