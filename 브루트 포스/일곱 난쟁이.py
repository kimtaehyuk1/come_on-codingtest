# 백준 2309번


# 퓰이 첫번째(조합을 이용하여)
from itertools import combinations

# heights = [ int(input()) for _ in range(9) ]
# for combi in combinations(heights, 7):
#     if sum(combi) == 100:
#         for i in sorted(combi):
#             print(i)
#         break




# 풀이 두번째(쌩코딩)
# 9개에서 7개를 뽑는다 = 두개를 뽑아서(for문 2개) 뺀다
heights = [ int(input()) for _ in range(9) ]
heights.sort()
tot = sum(heights)

def f():
    for i in range(8):
        for j in range( i+1, 9):
            if tot - heights[i] - heights[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(heights[k])

                return # 함수로 만들어줌으로서 만약 결과값(합해서100되는거) 많아도 초기 한번나오면 return하고 끝

f()