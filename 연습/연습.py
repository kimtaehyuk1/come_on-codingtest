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
# list = ["119", "97674223", "1195524421"]

# hash_map = {}
# for phone_number in list:
#     hash_map[phone_number] = 1

# for key in hash_map.keys():
#     print(key)

# from collections import deque
# list = deque([])
# #list.append(1)
# print(len(list))

# park = ["OSO","OOO","OXO","OOO"]


# for i,v in enumerate(park):
#     for j,k in enumerate(v):
#         print(v,k)



# tmp = ['b', 'c', 'd', 'e', 'f']
# skip = "wbqd"
# sum = 0
# # tmp 리스트에서 skip 문자열에 포함된 문자 개수 세기
# for i in tmp:
#     if i in skip:
#         sum += 1

# print(sum)
# real = chr(ord('a')+1)

# print(real)

# from itertools import combinations

# items = [2,1,3,4,1]
# for combi in combinations(items,2):
#     print(combi)

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = 	["stanko", "ana", "mislav"]

# participant.sort()
# completion.sort()

# for i, j in zip(participant,completion):
#     print(i,j)

# t = "3141592"
# print(type(t[0:3]))

# one = [1,2,3,4,5] * 2000
# two = [2,1,2,3,2,4,2,5] * 1250
# three = [3,3,1,1,2,2,4,4,5,5] * 1000


# print(len(three))

# list = [1, 5, 2, 6, 3, 7, 4]
# print(list[1:5])

# from itertools import combinations

# d = [1,3,2,5,4]

# for combi in combinations(d,3):
#     print(sum(combi))

# for i in range(10,1,-1):
#     print(i)

# numbers = [3, 2, 2, 2, 1]
# print(sum(numbers))

# s = "try hello world"
# s_list = [i for i in s.split()]
# print(s_list)

# s= "try hello world"

# def solution(s):
#     answer = ''
#     new_list = s.split(' ')
#     for i in new_list:
#         for j in range(len(i)):
#             if j % 2 == 0:
#                 answer += i[j].upper()
#             else:
#                 answer += i[j].lower()
#         answer+= ' '
#     return answer[0:-1]

# print(solution(s))

# piro = [[1,1,1],[5,1,1],[25,5,1]]
# print(piro[1][0])

# from collections import deque

# minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

# minerals_deque = deque()
# for i in minerals:
#     minerals_deque.append(i)

# tmp = minerals_deque.popleft()

# print(tmp)

# ele = [7,9,1,1,4]
# tmp = sum(ele[:2])
# print(tmp)

# from collections import Counter

# numbers = [1, 2, 3, 4, 1, 2, 2, 3, 3, 3]

# numbers_counts = Counter(numbers)

# # print(max(numbers_counts.values()))

# for number, count in numbers_counts.items():
#     if count == max(numbers_counts.values()):
#         print(number)

# a = 78
# b = bin(a)

# print(b[2:].count('1'))


# from collections import deque



# def colletion(n):
#         stk = []
#         isTrue = True
#         for ch in n:
#             if ch == '[' or '(' or '{':
#                 stk.append(ch)
#             if ch == ']' or ')' or '}':
#                 if stk:
#                     stk.pop()
#                 else:
#                     isTrue = False
#                     break
#         if stk:
#             isTrue = False

#         return 1 if isTrue else 0

# n = '[]()'
# print(colletion(n))

# from collections import deque
# list2 = [1]
# dq = deque(list2)
# # dq2 = list(dq)[:2]
# print(len(dq))


# list = [1,2,3,4,5]
# print(list[:2][0])

# targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

# targets.sort(key = lambda x : x[1])

# print(targets)

# list = [-1] * 10

# print(list)

# dp = [float('inf')] * 10

# print(dp)

# from itertools import permutations

# numbers = '17'
# numbers2 = [num for num in numbers]


# for i in range(1,3):
#     a = [''.join(permu) for permu in permutations(numbers2,i)]
#     print(a)\


# numbers = [3, 30, 34, 5, 9]

# str_numbers = [str(num) for num in numbers]
# str_numbers.sort(key = lambda i: i*3 , reverse=True)
# answer = ''.join(str_numbers)
# print(type(answer))

# list = [1,2]*4
# print(list)
# from itertools import permutations
# a = '17'
# list = [num for num in a]
# for i in range(1,len(a)+1):
#     a = [permu for permu in permutations(list,i)]
#     print(a)

# number = "4177252841"
# number = list(number[:5])
# number.sort()
# print(number)

lst = [1,4,5,5]
print(lst.count(5))