# m = {}
# m["taehyuk"] = 100
# m["taejun"] = 200
# for k in m:
#     print(k,m[k])

# A = [2,7,3,4,1]

# I = list(range(5))

# I = sorted(I, key= lambda i: A[i])

# print(I)


# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]
# coins.reverse()

# print(coins)


# for i in range(7,7):
#     print(i)

# from itertools import combinations

# list = [(1,2), (6,8),(3,4),(1,4)]


# for combi in combinations(list,3):
#     print(combi)

# print('김태혁', end='')
# print('김태준')

# N, M = map(int, input().split())
# board = [input() for _ in range(N)]

# print(board[0][1])

# dy = (0,1,0,-1)
# print(dy[-2])

# numbers = [1, 2, 4, 5]

# for num in numbers:
#     if num == 3:
#         print("숫자 3을 찾았습니다.")
#         break
# else:
#     print("숫자 3을 찾지 못했습니다.")

# for i in range(5,0,-1):
#     print(i, end='')

# sequence = [1, 1, 1, 2, 3, 4, 5]
# k = 5
# answers = []
# sum = 0
# l = 0
# r = -1

# while True:
#     if sum < k:
#         r += 1
#         if r >= len(sequence):
#             break
#         sum += sequence[r]
#     else:
#         sum -= sequence[l]
#         if l >= len(sequence):
#             break
#         l += 1
#     if sum == k:
#         answers.append([l, r])

# print(answers)

# ans = [[0, 3], [4, 4], [6, 6]]
# ans = sorted(ans, key=lambda x: (x[1]-x[0], x[0]))
# print(ans)

from collections import deque 
#   북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# 아이디어: 레버까지 bfs가고 레버에서 EXIT까지 bfs로 간다.

