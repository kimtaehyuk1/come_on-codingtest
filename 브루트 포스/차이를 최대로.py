# 문제 url: https://www.acmicpc.net/problem/10819
# 인접한 두수의 차이가 최대가 되게해서 더하는거(짜피 절댓값)
# 예) 3 7 5 -> 4 + 2 =6 이런식인데 이 차이가 최대가 되도록 재배치 하라는것.

# Brute Force는 = 무식하게 모든 경우의 수를 다 해보는 것이다.
# 즉 모든 순열에 대해서 차이의 합을 구해서 가장 큰 놈을 선택하겠다.

from itertools import permutations

# 입력
N = int(input())
a = list(map(int, input().split()))

ans = -1
for p in list(permutations(a)): #a가 입력됫을때 나올 수 있는 모든 순열 경우 구해줌
    sum = 0  # sum=0을 이위치에 넣어줘야 한개씩 순열 가지고 올때, sum 영향 안받음.
    for i in range(N-1): #인접 한거 뺴는거니까 range범위 조심
        sum += abs(p[i]-p[i+1])

    if ans < sum:
        ans = sum

print(ans)