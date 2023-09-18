# 이거 딱봐도 스택을 이용해서 푸는 문제

def solution(ingredient):
    answer = 0

    # 스택만들기
    making = []
    # 정답순서 햄버거 배열 만들기
    hamburger = [1,2,3,1]

    for i in ingredient:
        making.append(i)
        # 여기가 핵심 포인트인데 [-4:]이렇게 하면 계속 밀리면서 체킹한다
        if making[-4:] == hamburger:
            answer += 1
            # 햄버거 만들어졌으니까 4번만큼 오른쪽에서 빼주기
            for _ in range(4):
                making.pop()

    return answer


ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))