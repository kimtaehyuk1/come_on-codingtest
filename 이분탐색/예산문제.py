'''
문제 url : https://www.acmicpc.net/problem/2512
'''


# 입력
N = int(input()) # 지방 수
req = list(map(int,input().split())) # 지방 당 요청예산 입력 # input().split()을 해야 리스트로 갈린다
M = int(input()) # 정부가 줄수 있는 총예산

lo = 0
hi = max(req)
mid = (lo + hi) // 2
ans = 0


# 정해진 mid를 상한선으로 봤을때, 가능한지 알려주는 함수 짜기
def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M #어렵게 한번에 쓴건데 req있는거 한개씩꺼내서 mid와 그값중에 최소값을 다 더한게 총 예산 M보다 작아야 True


while lo <= hi:
    if is_possible(mid): # 함수안에서 True or False 반환하도록하는 함수 만들어준느게 파라메트릭 서치인데 여기 내용이 어떻게 달라지는것이다.
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1

    mid = (lo + hi) // 2

print(ans)