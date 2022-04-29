TestCase = int(input())
output = []
for case in range(TestCase): #테스트 케이스별로 k층 n호의 거주인들을 계산
    # k-1 층의 1~n호까지 사람들
    k = int(input()) # k층 
    n = int(input()) # n호
    cur = [0 for i in range(0,n)]
    bottom = [0 for i in range(0,n)]
    tmp =0
    for i in range(k+1): # 층의 반복 0층부터 k층까지 
        if sum(cur)!=0:
            bottom = list(cur)
        for j in range(n): # 호수의 반복  1호부터 n호까지 -> 0~n-1
            if i ==0: # 0층은 j만큼의 인원수가 들어간다.
               bottom[j] = j+1
            else: 
                tmp = sum(bottom[0:j+1])
                cur[j] = tmp
    output.append(cur[-1])
for v in output:
    print(v)