# 백준 15686 치킨배달 문제
# 준네 어렵다..

from itertools import combinations 
N , M = map(int, input().split())
# 다 입력으로 안받고 집과, 치키집만 입력 좌표로 받기 위함
houses = []
chickens = []
# 입력된 거중에 집과 치킨집 좌표 따기
for i in range(N):
    for j, v in enumerate(map(int,input().split())): # j가 인덱스 v가 값
        if v == 1:
            houses.append((i,j)) # 이렇게 좌표받기
        if v == 2:
            chickens.append((i,j))

# 최소로 찾을거니까 무한대 ans를 찾아야됨. 밑에가 가장 무한대인 거리의  치킨거리부터 생각해서 가장 끝에 있을때
ans = 2 * N * len(houses)


def get_dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])


# 우선 첫번째는 최대 13개중에 남길거 M을 고르는거
for combi in combinations(chickens, M):
    tot = 0 # 여기 위치 중요함. !!!다른 경우의수는 리셋되서 들어가서 세야하니까!!!! 이건 도시의 치킨거리 구하려고
    # 치킨거리구해서 다 더해서 도시 치킨거리 구하기
    for house in houses:
        tot += min(get_dist(house,chicken) for chicken in combi) # 골라진 combi에서 하나씩 뽑아서 치킨집이라고 하고 하우스 1개와 치킨집들간의 최소거리 구해야됨 -> 그후 최소거리 들의 합이 도시의 치킨거리
# 결국 위의 tot이 거리 치킨거리 구한거 그걸 M무작위로 젤 작은거 고르는거
    ans = min(ans,tot)

print(ans)