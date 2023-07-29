# 파이썬이니까 우선순위큐는 젤 작은 값 출력
# 절댓값도 비교해야되고, 원본값도 비교 해야한다.-> 한번의 두개의 정보필요 -> 튜플로 sort하기

#백준 11286문제

import heapq as hq
import sys

pq = []

# N을 받기 위한 for이고
for _ in range(int(sys.stdin.readline())):
    # 들어오는놈이 0인지 아닌지 판별 for
    x = int(sys.stdin.readline())
    if x: #x가 0이 아닐때
        hq.heappush(pq, ( abs(x),x ) ) # 튜플로 절댓값,원본 넣기
        # 이러면 절댓값이 작은순대로(앞에있으니까), 절댓값 같으면 뒤에 원본보고
    else:  # x가 0일때
        if pq: # 리스트에 뭐가 있을때
            print(hq.heappop(pq)[1]) #알아서 두개다 보고 젤 작은거 출력
        else: #리스트에 없을땐 0출력
            print(0)