# 백준 17136 색종이 붙이기
# 골드2 난이도
# 색종이를 덮는다는건 체크 기준 우측 밑으로 덮는다는거

board = [list(map(int, input().split())) for _ in range(10) ]
ans = 25
# 사용한 색종이들 개수 기록 1~5크기까지
paper = [0] * 6


def is_possible(y,x,sz):
    if paper[sz] == 5:
        return False

    # 범위 체크
    if y + sz > 10 or x + sz > 10:
        return False

    # 사이즈 만큼 1로 이루어져 있는지 검사
    for i in range(sz):
        for j in range(sz):
            if board[y + i][x + j] == 0:
                return False

    return True #위의 조건 다 통과하면 가능하다

def mark(y,x,sz,v):
    for i in range(sz):
        for j in range(sz):
            board[y + i][x + j] = v

    if v: # v가 1인경우 즉 색조이 사용 안한경우
        paper[sz] -= 1 # 원상복구 시키는거니까 색종이 다시 띈거임.
    else: # 색종이 사용한 경우 0인경우
        paper[sz] += 1


# 빽트레킹으로 문제 풀이
def backtracking(y, x):
    global ans
    if y==10: # 10존재안하므로 완성됫다
        ans = min(ans,sum(paper))
        return
    
    # x가 10인 경우는 다음줄로 내려간다
    if x == 10:
        backtracking(y+1,0)
        return
    
    # 현재 칸이 0인 경우 다음 칸을 보면 됨
    if board[y][x] == 0:
        backtracking(y,x+1)
        return

    # 여기까지오면 1인경우만 일로 올거다
    # 색종이 사이즈 1부터 5까지 대보고 가능하면 덮고
    for sz in range(1,6):
        # 색종이 덮을 수 있는지 검사
        if is_possible(y, x, sz):
            # 가능하면 색종이 덮는다
            mark(y, x, sz, 0) # 0으로 덮는다
            #print(board)
            # 다음좌표로 진행해보고 ---> 이건 1이였을때 다음 좌표 접근해야지 다시 함수들어와서 다음께1인지 0인지 다시 보지
            backtracking(y,x+1)
            #print(board)
            # 원상복구
            mark(y, x, sz, 1)
            print(board)

# x좌표가 10되는순간 다음줄로 넘어가고

backtracking(0,0)
print(-1 if ans==25 else ans ) # 불가능한 경우 그냥 25일테니까