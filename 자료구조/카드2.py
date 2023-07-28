# 문제 url : boj.kr/2164

# queue로 앞에꺼 제거, 남은 맨앞 제거후 뒤에 삽입!

from collections import deque


# 시간 복잡도를 따져야되


N = int(input())
dq = deque()
# deque에 1~N까지 담기
for i in range(1,N+1):
    dq.append(i)
# 선언 할때 부터 담아보기
#dq = deque(range(1,N+1))


# dq의 길이가 1보다 크면 두 행위(queue로 앞에꺼 제거, 남은 맨앞 제거후 뒤에 삽입!) 반복
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft()) # append는 뒤에 넣는건데 앞에서 뺀 값을 뒤로.
#   print(dq)

print(dq.pop())
# 출력값
# deque([1, 2, 3, 4, 5, 6])
# deque([3, 4, 5, 6, 2])
# deque([5, 6, 2, 4])
# deque([2, 4, 6])
# deque([6, 4])
# deque([4])