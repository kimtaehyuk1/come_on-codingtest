# 아이디어: 
import math
from itertools import permutations
answer = 0
# 리스트를 쪼개는것과 그냥 문자열을 쪼개는거 다른거네
set_list = set()

def prime(x):
        if x <= 1:
             return False
        if x == 2:
             return True
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

numbers = '17'
numbers2 = [num for num in numbers]
# print(numbers2)
for i in range(1,len(numbers)+1):
    a = [''.join(permu) for permu in permutations(numbers2,i)]
    for j in a:
        j = int(j)
        set_list.add(j)

for k in set_list:
     if prime(k):
          answer += 1

print(answer)
