# 백준 1018 체스판 다시 칠하기
# 어떻게 푸는지 생각 안나면 완전탐색부터 접근
# N과 M이 주워졌을때 8x8로 짜르는 경우가 (N - 7)(M - 7) 이고 64개만큼 제대로 되어있는지 봐야되고 왼쪽상단이 b,w로 두경우 이므로 *2
# 따라서 총 (N,M이 최대 50이니까) 43 * 43 * 64 * 2 = 236672 니까 완전탐색으로 해도된다.

# 이해: 8x8보다 큰걸 찾앗다 가정해서 그걸 8x8로 자르는 경우중에서 가장 적게 색칠해도 되는 경우 몇개를 색칠하냐는문제지 8x8을 고르는 경우의수는 필요 없다
# 즉 젤 많이 바꿔봐야 32



# 누적합으로도 풀어보기
N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 64 # ans최소로 답 구할거기 때문에 8x8일때 가장 많이 칠하는 수가 32임으로 32보다만 크게 하면 된다

def fill(y,x,bw):
    global ans
    cnt = 0
    #8x8안에서 돌면서 체크할 for문
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0: #즉 i + j가 짝수일때(0포함)
                if board[y + i][ x + j ] == bw:
                    cnt += 1
            else:
                if board[y + i][ x + j ] != bw:
                    cnt += 1

    ans = min(ans,cnt)


# 여긴 8x8넘어갈때 처리해주는거
for i in range(N - 7):
    for j in range(M - 7):
        fill(i, j, 'B')
        fill(i, j, 'W')


print(ans)