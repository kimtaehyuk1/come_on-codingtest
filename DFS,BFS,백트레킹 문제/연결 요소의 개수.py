# 백준 11724 연결 요소의 개수 문제
# 정점이 N * N-1 /2 개로 많기 때문에 인접행렬이 낫다.
# 인접행렬에 그래프를 담고 연결요소 개수를 세기 위해 
# 리스트에 다 False로 시작 위치 잡아주고 그 정점갓을때 연결되어있는 놈 True로 바꾸고(DFS로 탐색), 리스트를 1씩 늘려가면서 True되있으면 패스하고 False
# 되어 있는거 있으면 +1 하고 또 연결되어있는거 True로 바꿔서 끝까지 갔을때 답은 + 몇 되어있느냐가 연결리스트 개수의 답임
# 즉 체크리스트 만들고 내가 방문하지 않은 노드가 있다면 +1하고 탐색 돌리고 이런식..

# 정점시작이 1이라는점 가만

import sys
sys.setrecursionlimit(10 ** 6) # 이건 DFS탐색할때 파이썬 특성상 10의3승인데 더 들어가라고 쓰는거
input = sys.stdin.readline

#입력(N은 정점 M은 간선)
N, M = map(int, input().split())
# 인접행렬(2차원 행렬 디폴트)
adj = [[0]*N for _ in range(N)]
# 인접행렬에 간선 1표시(무방향인거 고려)
for _ in range(M):
    a, b = map(lambda x: x -1 ,map(int, input().split())) # 입력값 그대로에서 1씩 빼주기 왜? 리스트는0부터 시작인데 문제에서 정점은 1부터 시작이니까 <- 리스트에 맞춘거
    adj[a][b] = adj[b][a] = 1

# 체크리스트 만들기
ans = 0
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:  # if adj[now][nxt]: 여기까지 해도 답은 나오지만 이러면 1에서 탐색해서 2간선을 찾았는데 2갈때 또 1을 찾기때문에 불필요
            # dfs가기전에 chk리스트 체크
            chk[nxt] = True
            dfs(nxt)


for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i) # 처음간 정점 True한후 dfs로 탐색해서 탐색된거 True로 바꾸는 dfs 함수 짜기


print(ans)