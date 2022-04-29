N = int(input())
number = 0 
i = 0
while(True):
    if i==0:
        number= number+1
    else:
        number = number+6*i
    i= i+1
    if number>=N:
        break        
print(i)