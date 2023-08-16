# 백준 2178 미로탐색
# 최단거리 탐색 알고리즘 BFS
# 체크배열필요( 있어야 밑으로 가지 없으면 탐색하면 위로도 갈수 있으니까) 내가 방문하고 방문하지 않은 칸으로만 가게 구현 해야되서

from collections import deque

#    북 동 남 서
dy = (-1,0,1,0)
dx = (0,1,0,-1)
N, M = map(int, input().split())
board = [input() for _ in range(N)]  # 이거는 ['101111', '101010', '101011', '111011'] 이런식으로 리스트에 문자열로 담는거임

# 미로에서 벗어나면 안되니까 유효범위 체크
def is_valid_coord(y,x):
    return 0 <= y < N and 0 <= x < M  # 입력은 4 6 이지만 이차원리스트 인덱스는 그거보다 한개 작으니까

def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True #시작점은 1
    dq = deque()
    dq.append((0,0,1)) # 0,0은 시작위치고 1은 지나온 개수 세야하니까(시작점도 한개 세라고 했으니까)
    while dq:
        y, x, d = dq.popleft()

        if y == N-1 and x == M-1:
            return d
        
        nd = d + 1 # 여기 위치 중요
        for k in range(4): #이건 미로가 현시점으로 4방향 갈 수 있으니까
            ny = y + dy[k]  # dy = (0,1,0-1) dx = (1,0,-1,0) 이거니까 무조건 4방향중 한방향씩 움직이면서 탐색
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny,nx,nd))

print(bfs())