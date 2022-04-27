T = input()
output = []
for i in range(int(T)):
    H, W, N = map(int, input().split()) #층수, 층마다 세대 수, N번째 들어온 사람
    share, rest = divmod(N, H) #몫이 세대 호수 나머지는 층수 / 몫 만큼 층수를 돌아 1호부터 채우고 나머지만큼 다음 호수를 층별로 차례대로 채운다
    if rest>0:
        share = share+1
    else:
        rest = H
    if len(str(share)) == 1:
        share = '0' + str(share)
    output.append(str(rest) + str(share))
for i in output:
    print(i)