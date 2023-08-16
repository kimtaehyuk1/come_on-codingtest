# 백준 14503 로봇청소기 

from collections import deque

#    북 동 남 서
dy = (-1,0,1,0)
dx = (0,1,0,-1)
N, M = map(int, input().split())
cy,cx,cd = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]


def solve(cy,cx,cd):
    cnt = 0 #청소한 장소수
    while 1: #청소기가 더이상 움직이지 못할 때 종료
        # 청소기가 현재위치 청소
        board[cy][cx] = 2
        cnt += 1
        # 4방향 탐색후 청소되지 않은 빈칸이 있으면 왼쪽으로 회전해서 전진, 없으면(else) 후진, 청소할곳없는데 후진도 못하면 종료
        # 근데 이 행위도 반복이 필요 왜? 후진해서 청소방향있으면 다시 그자리에서 탐색해야됨 
        flag = 1
        while flag == 1:
            # 방향확인(왼쪽부터 탐색)
            for nd in ((cd+3)%4, (cd+2)%4,(cd+1)%4,cd):  # for nd in range(4) <- 방향이 없더라면
                ny = cy + dy[nd]
                nx = cx + dx[nd]
                if board[ny][nx] == 0:
                    cy, cx, cd = ny, nx, nd
                    flag = 0
                    break
            else: # for문에서 break하지  않았다. 즉 네방향이 다 청소할때 없다
                by = cy - dy[cd]
                bx = cx - dx[cd]
                if board[by][bx] == 1:
                    return cnt
                else:
                    cy, cx = by, bx


ans = solve(cy,cx,cd)
print(ans)