# 백준 1449번 문제

N, L = map(int, input().split())
# 1001로 해야 리스트 인덱스로는 0~1000까지니까
# 전략 : 뚫려있는 구멍만 True로 바꾼후 ->  True를 만나면 테이프 길이만큼 점프하고 ans에 +1, 아닌구간 만나면 그냥 x에 그냥 +1
# X는 처음부터돌면서 검사하는놈, ans는 답 세는놈 
coordi = [False] * 1001

# 입력으로 물이 세는 위치만 좌표값 True로 바꾸기
for i in map(int, input().split()):
    coordi[i] = True

ans = 0
# 인덱스로0 부터 시작한다 가정했으니, x=0부터 시작
x = 0 

while x < 1001:
    if coordi[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)