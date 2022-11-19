
def solution(number, k):
    answer = []
    for num in number: 
        while answer and k > 0 and answer[-1] < num:
            answer.pop()
            k-=1
        answer.append(num)
        
    for i in range(k):
        del answer[answer.index(min(answer))]
    return (''.join(answer))