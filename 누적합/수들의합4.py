# 문제 url: https://www.acmicpc.net/problem/2015
# 여기서 부분합은 연속적인 수들의 합이 목표값 K이어야 한다는 것이다.

# 입력
import sys
N,M = map(int,sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

# 누적합 구하기
psum = [0] * N # 크기가 N인 배열 만들기
psum[0] = a[0] # psum의 첫번째는 직접 받는 수 밖에 없음.
for i in range(1,N):
    psum[i] = psum[i-1] + a[i]

count = {} # count[key] = 내앞에 psum값이 key인것의 개수 쉽게 구하려고 
answer = 0

# 우선 풀이과정 먼제 이해하고 밑에는 flow 타보기
# for i in range(N):
#     goal = psum[i] - M  # 그림에서 보다시피, M(목표값) = psum[i] - goal (예를들어 psum[i]값이 3이면 전꺼봤을때 1일 놈 찾아야된다. => goal 개수 2개)

#     if goal in count:
#         answer += count[goal] #count안에 goal이 들어있는 수만큼 더하는거

#     if goal  == 0:
#         answer += 1
        
#     if psum[i] not in count:
#         count[psum[i]] = 0  #초기화

#     count[psum[i]] += 1

# print(answer)


# ------------------------------------------------------------내가 더 간단하게 풀어보겟어

for i in range(N):
    goal = psum[i] - M
    if goal in psum:
        answer += 1

print(answer)