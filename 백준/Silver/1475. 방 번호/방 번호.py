N = (input())
def count_num(num):
    cur_count = [0]*10

    for i in range(len(num)):
        if num[i] == '9' or num[i] == '6':
            if cur_count[6] == cur_count[9]:
                cur_count[int(num[i])] +=1
            else:
                # 6, 9 두 인덱스 중 작은 값의 인덱스를 찾아야 한다.
                mins = 6 if cur_count[6]<cur_count[9] else 9

                cur_count[mins] +=1
        else:
            cur_count[int(num[i])] +=1
    print(max(cur_count))

count_num(N)