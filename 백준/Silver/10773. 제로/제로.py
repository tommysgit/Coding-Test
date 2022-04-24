K = int(input())
numbers = []
realNumbers = []
for i in range(K):
    numbers.append(int(input()))
for number in numbers:
    if number == 0:
        realNumbers.pop()
    else:
        realNumbers.append(number)
print(sum(realNumbers))