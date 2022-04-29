A, B, V = map(int, input().split()) 
day = A-B # 하루에 올라갈 수 있는 거리
target = V-A # 
output = 0
if target == 0: # V - A가 0이면 하루만에 도착  -> 밤을 안거쳐서 내려갈일이없음
    print(1)
else:
    share, rest = divmod(target,day) # 나누어 떨어지면 1을 더한다. 
    #몫이 있을경우와 없을 경우가 있다. 몫이 있으면 처음에 A를 뺀(하루)와 나머지 만큼의 하루를 더 계산
    if rest == 0:
        output = share + 1
    else:
        output = share+2
    print(output)