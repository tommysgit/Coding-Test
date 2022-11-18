from itertools import combinations_with_replacement
def back_track(alphabet, stack, ans, answer, cnt):
    
    if ''.join(stack) == ans:
            print(cnt)
            answer[0] = cnt[0]
    cnt[0] += 1
    if len(stack) == 5:
        return
        
    
    for i in range(5):
        stack.append(alphabet[i])
        back_track(alphabet, stack, ans, answer, cnt)
        stack.pop()
    
def solution(word):
    answer = [0]
    alphabet = ['A', 'E', 'I', 'O', 'U']
    stack = []
    back_track(alphabet, stack, word, answer, [0])
    
    return answer[0]