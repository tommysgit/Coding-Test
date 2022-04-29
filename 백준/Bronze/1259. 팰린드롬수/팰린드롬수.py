isPallen = []
while(True):
    number = str(input())
    if number == '0':
        break
    share, rest = divmod(len(number), 2)
    num1 = number[0:share]
    if rest ==0:
        num2 = number[share:]
    else:
        num2 = number[share+1:]
    num2List = list(num2)
    num2List.reverse()
    num2 = ''.join(num2List)
    if num1==num2:
        isPallen.append('yes')
    else:
        isPallen.append('no')
for i in isPallen:
    print(i)