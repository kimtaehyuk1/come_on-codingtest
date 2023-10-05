# 1. 사회자 숫자 좌표알기 -> 세로 가로 대각선 체크 배열에 적절히 카운트 해주기
# 2. 각 체크 배열의 5인거 세기 >= 빙고이다.

# 입력받기
arr = [list(map(int,input().split())) for _ in range(5)]
# 사회자가 부르는거 걍 일차원 리스트로 받기
lst = []
for _ in range(5):
    lst += list(map(int,input().split()))


# i,j는 순서대로 행렬이다. i,j좌표에 어떤 숫자가 있는지 알아야되지
pos_list = [0] * 26
for i in range(5):
    for j in range(5):
        pos_list[arr[i][j]] = (i,j) #  pos_list의 값에 죄표가 들어있다.

# v배열들 엮어서 걍 이중으로 만들기
v = [[0]*10 for _ in range(4)] # 4개필요(가로,세로,대각선 다른방향 두개), 10인이유는 대각선이 9개니까 걍 넉넉하게
# 사회자가 부르는 좌표를 읽어서, 빈도수 체크, 5인개수가 3개 이상이면 종료
for n in lst:
    # 좌표받기
    i, j = pos_list[n]
    # 좌표들을 방문 배열에 한개씩 넣기 [0]부터 세로부터
    v[0][j] += 1 # 세로
    v[1][i] += 1 # 가로
    v[2][i-j] += 1 #대각선
    v[3][i+j] += 1 #대각선
    cnt = 0
    for k in v:
        cnt += k.count(5)

    if cnt >= 3:
        break
# 몇번째에 빙고가 됬냐 구현 -> 아무거나 v[0]에서 sum 구하면됨
print(sum(v[0]))
     