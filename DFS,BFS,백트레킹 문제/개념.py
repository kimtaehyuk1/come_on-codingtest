#  코드로 그래프를 나타내는 방법

# 1. 인접행렬, 2. 인접리스트(연결리스트)
# 인접행렬에서 행은 출발 노드 열은 도착노드 1의 위치보고 간선을 그으면 된다. <- 이건 방향그래프 일때
# 인접행렬에서 무방향일땐 한 간선당, 1이 두개(양쪽)

# 인접리스트는 인접행렬처럼 0이 할당되지 않고 간선이 있는 부분만 나타남

# 인접행렬은 시간을 단축시키고, 인접리스트는 공간을 단축시키는데
# 만약 공간이 많으면 인접행렬을 쓰는게 낫다.


# DFS (깊이 우선 탐색) 
'''
!특징!
1. 스택 or 재귀를 사용해서 구현한다. (보통 재귀를 많이 쓰는데 그거 자체각 스택을 이용하는거라.. 뭐...)
2. DFS는 완전탐색이라 모든 경우 다봄 (순서가 중요하다)
'''

adj = [[0]*13 for _ in range(13)] # 행이 13, 열이 13인 2차원 행렬 만들어줌. <- 인접행렬
print(adj)
# 간선이 어디 있냐에 따라
adj[0][1] = adj[0][7] = 1 # 이렇게 인접행렬에 쭉 표시하기

def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)


dfs(0)


# BFS
'''
!특징!
1. 얘도 완전탐색
2. 큐를 사용해서 구현한다
'''
# 이놈도 구현하기 위해 인접행렬이 주어졌다고 가정했을때
from collections import deque

def bfs():
    dq = deque()
    dq.append(0) # 탐색시작할 루트 노드
    while dq:
        now = dq.popleft() # 하나씩 뺴면서 밑에 탐색할거있나 검사
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs()

# 중요!!!!
'''
DFS는 자신이 찾는 첫번째 만나는 노드가 최단거리라는거 보장 못하는데 BFS는 탐색하다가 원하는 놈 만나면 최단거리라 생각하고 탐색 종료(보장됨)
결론적으로 최단거리 탐색 -> BFS
'''
# 간선개수가 적으면 인접리스트가 개이득 간선이 많으면 인접행렬이 이득