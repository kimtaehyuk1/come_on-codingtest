from collections import deque
# 북 동 남 서
dy = [-1,0,1,0]
dx = [0,1,0,-1]

def solution(maps):
    
    # 입력에서 타겟좌표 설정
    N = len(maps)
    M = len(maps[0])
    
    # 유효범위 체크하기
    def is_valid(y,x):
        return 0 <=y<N and 0<=x<M
    
    def bfs():
        # 다시 안돌아가게 체크셋 만들기
        chk = set()
        # start좌표 찍기
        chk.add((0,0))
        # 큐만들기
        dq = deque()
        # 시작 위치와 카운트셀 항목넣기
        dq.append((0,0,1)) # 처음것도 세기 때문에
        
        while dq:
            (y,x,d) = dq.popleft()
            
            # 목표지점까지 가면 스탑
            if (y,x) == (N-1,M-1):
                return d
            
            nd = d+1
            # 4방향 탐색
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if is_valid(ny,nx) and (ny,nx) not in chk and maps[ny][nx] == 1:
                    chk.add((ny,nx))
                    dq.append((ny,nx,nd))
                    
        return -1
    
    return bfs()

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))