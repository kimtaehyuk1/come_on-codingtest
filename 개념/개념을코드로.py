# 순열과 조합이 있는데 순열은 permutations 쓰고 조합은 밑에처럼
# 순열은 걍 다 나열이고 조합은 순서상관 안하고 나열(순열보다 수 더 적음) 
from itertools import combinations
v = [0,1,2,3]
for i in combinations(v,2):
    print(i)

# for i in range(1,2):
#     print(i)

# print(10/4)
# print(10//4)

# board = [input() for _ in range(4)]
# print(board)