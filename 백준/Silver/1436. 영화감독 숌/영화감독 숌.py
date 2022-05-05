N = int(input())
count = 0
number = 0
while(True):
    if '666' in str(number):
        count += 1
    if count == N:
        break
    number += 1
print(number)