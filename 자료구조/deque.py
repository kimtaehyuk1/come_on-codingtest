from collections import deque

dq = deque()
dq.append(123)  # deque는 앞뒤 다 넣을수 있는데 이건 오른쪽으로 넣기
dq.appendleft(465) # 이놈은 왼쪽(앞으로)넣기
dq.appendleft(789)
print(dq)
# 여기까지 형태가 dq [ 789 456 123]


print(dq.pop()) # 오르쪽(뒤에서)빼기
print(dq.popleft()) # 왼쪽(앞에서) 빼기