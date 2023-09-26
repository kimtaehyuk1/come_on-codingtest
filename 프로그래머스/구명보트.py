from collections import deque

# 중요한 개선점 만약 제한이 240인데 50 50 태우는거보다 190 50 이났다 -> 젤 무거운사람과 젤 가벼운 사람

def solution(people, limit):
    answer = 0
    # people sort하기
    people.sort()
    # 디큐에 담기
    dq_people = deque(people)
    # 한 보트에 두명 밖에 못탐.
    while True: #큐에 남아있을때 까지 [50,50,70,80]  , [50,70,80]

        # 수가 짝수 홀수여서 0개 1개남을때 처리해줘야함
        if len(dq_people) == 1:
            answer += 1
            break
        if len(dq_people) == 0:
            break

        # 큐에서 가장 가벼운 사람과 무거운 사람 뽑음
        havy = dq_people.pop()
        thin = dq_people.popleft()
        # 위에거 자체가 이미 빠진거임
        if havy + thin <= limit:
            answer +=1
        else: # 아니면 무거운 사람 태우고 가벼운사람은 다시 넣기
            answer += 1
            dq_people.appendleft(thin)

    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people,limit))