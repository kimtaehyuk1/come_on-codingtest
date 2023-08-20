from collections import deque

def solution(prices):
    answer = []
    # 처음으로 prices를 큐에 담기
    dq = deque(prices)
    # 앞에서 부터 한개씩 빼서 뒤와 비교하여 cnt센거 answer에 append하고
    while dq:
        cnt = 0
        current = dq.popleft()
        # 맨앞빼서 뒤와비교, 맨뒤꺼 빼고 큐비어서 이거 하면 뻑안나고 cnt 0 찍히니까 통과
        for i in dq:
            # 우선 무조건 1개는 추가
            cnt += 1
            if current > i:
                break
        answer.append(cnt)
    

    return answer