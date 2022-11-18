import math
from itertools import permutations
def solution(numbers):
    def prime_check(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    answer = 0
    num_set = set([])
    for i in range(1, len(numbers)+1):
        for permu in permutations(numbers, i):
            num = int(''.join(permu))
            if num not in num_set:
                num_set.add(int(''.join(permu)))
                if num >= 2 and prime_check(num):
                    answer += 1

    return answer