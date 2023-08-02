# 백준 1389 케빈 베이컨의 6단계 법칙

# N은 정점이고 , M은 간선이고 양방향그리프이고 최소탐색 구하라 했으니 bfs를 이용해서 구하기

from collections import deque

N , M = map(int, input().split())
# 인접리스트를 이요해서 구하기
adj = [[] for _ in range(N)]
# 간선정보, | 문제는 1베이스이므로 1씩 빼줘서 리스트에 담기 
for _ in range(M):
    a, b = map(lambda x: x -1, map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)


# 어짜피 앞에서 부터들어가고 더 작지않은이상 갱신 안되므로 더 작은 숫자가 답으로 나올것이다.
kevin = [] # 각 노드마다 케빈베이컨수 담아주기
# 비교 대상 선언
ans = (-1,98765432)


# bfs함수 구현
def bfs(start, goal): # start에서 goal까지 가는 최단거리
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0)) #뒤에 0은 거리임
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d
        
        nd = d + 1
        for nxt in adj[now]:  # 인접리스트이므로 adj[now]에 연결될 다음 갈거 있다 그거 하나씩 빼면서
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt,nd))


# 케빈 베이컨수 구하는 함수
def get_kevin(start):
    # start로 시작해서 다른 노드까지 최단거리 구해서 tot에 쌓기 => 이게 케빈 베이컨의 수니까
    tot = 0
    for i in range(N):
        if i != start:
            tot += bfs(start, i)
    return tot


# 케빈 베이컨 수 구해서 넣기
for i in range(N):
    kevin.append(get_kevin(i)) # i 번째 케빈 베이컨수 구하는 함수 




for i, v in enumerate(kevin): # 돌면서 가장 작은 케빈베이컨수 찾아야지 (인덱스와 값 둘다 알아야하니까)
    if ans[1] > v:
        ans = (i, v)


print(ans[0] + 1) # 제로베이스로 했는데 마지막엔 1베이스니까 인덱스+1 해서 되돌리기